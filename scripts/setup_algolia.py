#!/usr/bin/env python3
"""Create Algolia indexes, DeepSeek provider, and Agent Studio agent.

Env (never commit these):
  ALGOLIA_APP_ID              default YN9LHHY3JW
  ALGOLIA_ADMIN_API_KEY or ALGOLIA_WRITE_API_KEY
  ALGOLIA_SEARCH_API_KEY      public search-only key written into algolia-public.js
  DEEPSEEK_API_KEY

Idempotent: reuses an existing DeepSeek provider and an agent named
"Seek Uplift Help Center".
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from algolia_http import (  # noqa: E402
    AlgoliaError,
    KEYWORD_INDEX,
    KEYWORD_SETTINGS,
    MARKDOWN_INDEX,
    MARKDOWN_SETTINGS,
    agent_studio,
    env_app_id,
    env_deepseek_key,
    env_search_key,
    env_write_key,
    set_index_settings,
)

AGENT_NAME = "Seek Uplift Help Center"
PUBLIC_JS = ROOT / "docs" / "javascripts" / "algolia-public.js"
SEARCH_MODES = ("lunr", "keyword", "askAi")
SEARCH_MODE_RE = re.compile(r'"searchMode"\s*:\s*"(lunr|keyword|askAi)"')

INSTRUCTIONS = """You are a helpful assistant embedded in the Seek Uplift help-center wiki, a public TEST help center for a SKR-based Solana launchpad.

Answer accurately and concisely using only the retrieved wiki context.
Before saying information is unavailable, check whether related content exists and summarize that instead.
If nothing relevant is in the context, reply: "I couldn't find this in the help center." Then point the reader at Getting help.
Always include relevant wiki URLs when they are in the context.
Do not invent product behavior, fees, or support commitments.
Ignore PUBLIC TEST banners and deployment warnings; they are chrome, not product documentation.
This wiki is a public test: do not promise SLAs, production support, or that content will stay up.
"""

ALLOWED_DOMAINS = [
    "https://seekuplift.github.io",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]


def _list(app_id: str, key: str, path: str) -> list:
    sep = "&" if "?" in path else "?"
    data = agent_studio(app_id, key, "GET", f"{path}{sep}limit=100")
    if isinstance(data, list):
        return data
    for field in ("items", "agents", "providers", "data"):
        if isinstance(data, dict) and isinstance(data.get(field), list):
            return data[field]
    return []


def ensure_indexes(app_id: str, write_key: str) -> None:
    set_index_settings(app_id, write_key, KEYWORD_INDEX, KEYWORD_SETTINGS)
    set_index_settings(app_id, write_key, MARKDOWN_INDEX, MARKDOWN_SETTINGS)
    print(f"Indexes {KEYWORD_INDEX} and {MARKDOWN_INDEX} settings saved.")


def ensure_provider(app_id: str, write_key: str, deepseek_key: str) -> str:
    providers = _list(app_id, write_key, "/1/providers")
    for provider in providers:
        name = (provider.get("providerName") or provider.get("provider_name") or "").lower()
        if name == "deepseek":
            print(f"Reusing DeepSeek provider {provider.get('id')}.")
            return provider["id"]
    created = agent_studio(
        app_id,
        write_key,
        "POST",
        "/1/providers",
        {
            "name": "Seek Uplift DeepSeek",
            "providerName": "deepseek",
            "input": {"apiKey": deepseek_key},
        },
    )
    print(f"Created DeepSeek provider {created.get('id')}.")
    return created["id"]


def agent_payload(provider_id: str) -> dict:
    return {
        "name": AGENT_NAME,
        "description": "Answers questions from the Seek Uplift help-center wiki.",
        "providerId": provider_id,
        "model": "deepseek-chat",
        "instructions": INSTRUCTIONS,
        "tools": [
            {
                "type": "algolia_search_index",
                "name": "help_center_search",
                "indices": [
                    {
                        "index": MARKDOWN_INDEX,
                        "description": (
                            "Seek Uplift help-center wiki: getting started, wallets, "
                            "account, trading, fees, launching, graduation, creators, "
                            "communities, callouts, privacy, FAQ, and getting help."
                        ),
                    }
                ],
            }
        ],
    }


def ensure_agent(app_id: str, write_key: str, provider_id: str) -> str:
    agents = _list(app_id, write_key, "/1/agents")
    existing = next((a for a in agents if a.get("name") == AGENT_NAME), None)
    payload = agent_payload(provider_id)
    if existing:
        agent_id = existing["id"]
        agent_studio(app_id, write_key, "PATCH", f"/1/agents/{agent_id}", payload)
        print(f"Updated agent {agent_id}.")
    else:
        created = agent_studio(app_id, write_key, "POST", "/1/agents", payload)
        agent_id = created["id"]
        print(f"Created agent {agent_id}.")
    published = agent_studio(app_id, write_key, "POST", f"/1/agents/{agent_id}/publish")
    status = published.get("status") if isinstance(published, dict) else None
    print(f"Published agent {agent_id} (status={status}).")
    return agent_id


def ensure_domains(app_id: str, write_key: str, agent_id: str) -> None:
    existing = _list(app_id, write_key, f"/1/agents/{agent_id}/allowed-domains")
    have = {
        (d.get("domain") or "").rstrip("/")
        for d in existing
        if isinstance(d, dict)
    }
    for domain in ALLOWED_DOMAINS:
        if domain.rstrip("/") in have:
            continue
        try:
            agent_studio(
                app_id,
                write_key,
                "POST",
                f"/1/agents/{agent_id}/allowed-domains",
                {"domain": domain},
            )
            print(f"Allowed domain {domain}.")
        except AlgoliaError as exc:
            if exc.status in (409, 422):
                print(f"Allowed domain {domain} already present ({exc.status}).")
            else:
                raise


def read_existing_search_mode(text: str) -> str:
    """Return a valid searchMode from public JS, defaulting to askAi.

    Re-running setup must not flip an operator kill switch back on.
    """
    match = SEARCH_MODE_RE.search(text)
    if match:
        return match.group(1)
    return "askAi"


def public_js_body(
    app_id: str, search_key: str, assistant_id: str, search_mode: str
) -> str:
    if search_mode not in SEARCH_MODES:
        raise ValueError(f"searchMode must be one of {SEARCH_MODES}, got {search_mode!r}")
    config = {
        "appId": app_id,
        "apiKey": search_key,
        "indexName": KEYWORD_INDEX,
        "markdownIndexName": MARKDOWN_INDEX,
        "assistantId": assistant_id,
        "searchMode": search_mode,
    }
    return (
        "/* Public Algolia DocSearch config. Safe to commit: search-only key.\n"
        "   Admin / write keys must never be placed here.\n"
        "\n"
        "   searchMode is the operator switch (commit + push to Pages):\n"
        '     "askAi"   — DocSearch keyword search + Ask AI tab\n'
        '     "keyword" — DocSearch keyword search only (no Ask AI tab)\n'
        '     "lunr"    — Material MkDocs search only\n'
        "   Keep assistantId even when searchMode is keyword or lunr so turning\n"
        '   Ask AI back on is one field. README: "Switching search modes". */\n'
        "window.__ALGOLIA_DOCSEARCH = "
        + json.dumps(config, indent=2)
        + ";\n"
    )


def write_public_js(app_id: str, search_key: str, assistant_id: str) -> None:
    if search_key in ("", None):
        raise SystemExit("Refusing to write an empty search key.")
    search_mode = "askAi"
    if PUBLIC_JS.exists():
        search_mode = read_existing_search_mode(PUBLIC_JS.read_text(encoding="utf-8"))
        if search_mode != "askAi":
            print(
                f"Preserving searchMode={search_mode} from existing public JS. "
                'Set searchMode to "askAi" in that file to turn Ask AI back on.'
            )
    body = public_js_body(app_id, search_key, assistant_id, search_mode)
    if "ALGOLIA_ADMIN" in body or env_write_key() in body:
        raise SystemExit("Refusing to write a write/admin key into algolia-public.js.")
    PUBLIC_JS.write_text(body, encoding="utf-8")
    print(
        f"Wrote {PUBLIC_JS.relative_to(ROOT)} with "
        f"assistantId={assistant_id} searchMode={search_mode}."
    )


def main() -> int:
    app_id = env_app_id()
    write_key = env_write_key()
    search_key = env_search_key()
    if search_key == write_key:
        raise SystemExit("Search key and write key must not be the same value.")
    deepseek_key = env_deepseek_key()

    try:
        ensure_indexes(app_id, write_key)
        provider_id = ensure_provider(app_id, write_key, deepseek_key)
        agent_id = ensure_agent(app_id, write_key, provider_id)
        ensure_domains(app_id, write_key, agent_id)
        write_public_js(app_id, search_key, agent_id)
    except AlgoliaError as exc:
        print(
            f"Algolia API error {exc.status} on {exc.url}\n{exc.body}\n"
            "If this is 403/404, open the Algolia dashboard for this app → "
            "Generative AI → enable Agent Studio, then re-run this script. "
            "A write key needs the editSettings ACL. "
            "Keyword indexes can still be filled with scripts/index_algolia.py.",
            file=sys.stderr,
        )
        return 1
    print("Setup complete. Commit docs/javascripts/algolia-public.js.")
    print(
        "Add ALGOLIA_APP_ID and ALGOLIA_WRITE_API_KEY as GitHub Actions secrets "
        "so deploys reindex."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
