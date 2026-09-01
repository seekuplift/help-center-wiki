"""Minimal Algolia Search + Agent Studio REST helpers (stdlib only)."""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any

DEFAULT_APP_ID = "YN9LHHY3JW"
DEFAULT_SEARCH_KEY = "8e1024885365e67a9c4c641a60a7e8a1"
KEYWORD_INDEX = "help_center"
MARKDOWN_INDEX = "help_center_markdown"


class AlgoliaError(RuntimeError):
    def __init__(self, status: int, body: str, url: str):
        super().__init__(f"Algolia {status} {url}: {body}")
        self.status = status
        self.body = body
        self.url = url


def env_app_id() -> str:
    return os.environ.get("ALGOLIA_APP_ID") or DEFAULT_APP_ID


def env_search_key() -> str:
    return os.environ.get("ALGOLIA_SEARCH_API_KEY") or DEFAULT_SEARCH_KEY


def env_write_key() -> str:
    key = os.environ.get("ALGOLIA_ADMIN_API_KEY") or os.environ.get(
        "ALGOLIA_WRITE_API_KEY"
    )
    if not key:
        raise SystemExit(
            "Set ALGOLIA_ADMIN_API_KEY or ALGOLIA_WRITE_API_KEY in the environment. "
            "Do not put write keys in the repo."
        )
    return key


def env_deepseek_key() -> str:
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        raise SystemExit("Set DEEPSEEK_API_KEY in the environment.")
    return key


def _request(
    method: str,
    url: str,
    *,
    headers: dict[str, str],
    body: Any | None = None,
) -> Any:
    data = None
    req_headers = dict(headers)
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        req_headers.setdefault("Content-Type", "application/json")
    req_headers.setdefault(
        "User-Agent",
        "SeekUpliftWiki/1.0 (Algolia; +https://seekuplift.github.io/help-center-wiki/)",
    )
    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        raise AlgoliaError(exc.code, err_body, url) from exc


def _hosts(app_id: str) -> list[str]:
    # `{appId}.algolia.net` does not always resolve; DSN + algolianet fallbacks do.
    aid = app_id.lower()
    return [
        f"{app_id}-dsn.algolia.net",
        f"{app_id}-1.algolianet.com",
        f"{app_id}-2.algolianet.com",
        f"{app_id}-3.algolianet.com",
        f"{app_id}.algolia.net",
        f"{aid}.algolia.net",
    ]


def _first_ok(
    method: str,
    path: str,
    *,
    app_id: str,
    api_key: str,
    extra_headers: dict[str, str] | None = None,
    body: Any | None = None,
) -> Any:
    headers = {
        "x-algolia-application-id": app_id,
        "x-algolia-api-key": api_key,
    }
    if extra_headers:
        headers.update(extra_headers)
    last_err: Exception | None = None
    for host in _hosts(app_id):
        url = f"https://{host}{path}"
        try:
            return _request(method, url, headers=headers, body=body)
        except AlgoliaError as exc:
            # Cloudflare 1010 on one edge (DSN) is not the API's answer —
            # try the next host. Real 4xx from Agent Studio / Search still raise.
            if exc.status == 403 and "cloudflare" in exc.body.lower():
                last_err = exc
                continue
            raise
        except Exception as exc:  # DNS / connect
            last_err = exc
            continue
    raise last_err or RuntimeError(f"No Algolia host reachable for {path}")


def search_api(
    app_id: str,
    api_key: str,
    method: str,
    path: str,
    body: Any | None = None,
) -> Any:
    return _first_ok(method, path, app_id=app_id, api_key=api_key, body=body)


def agent_studio(
    app_id: str,
    api_key: str,
    method: str,
    path: str,
    body: Any | None = None,
) -> Any:
    # Docs name `{APPLICATION_ID}.algolia.net/agent-studio`. That host does not
    # resolve on this network; the Search DSN / algolianet hosts do, and they
    # serve the same Agent Studio API. `_first_ok` skips Cloudflare 1010.
    return _first_ok(
        method,
        f"/agent-studio{path}",
        app_id=app_id,
        api_key=api_key,
        extra_headers={"accept": "application/json"},
        body=body,
    )


KEYWORD_SETTINGS = {
    "searchableAttributes": [
        "unordered(hierarchy.lvl0)",
        "unordered(hierarchy.lvl1)",
        "unordered(hierarchy.lvl2)",
        "unordered(hierarchy.lvl3)",
        "unordered(hierarchy.lvl4)",
        "unordered(hierarchy.lvl5)",
        "unordered(hierarchy.lvl6)",
        "content",
    ],
    "attributesToRetrieve": [
        "hierarchy",
        "content",
        "anchor",
        "url",
        "url_without_anchor",
        "type",
        "lang",
        "language",
    ],
    "attributesToHighlight": ["hierarchy", "content"],
    "attributesToSnippet": ["content:10"],
    "attributesForFaceting": ["filterOnly(type)", "filterOnly(lang)", "filterOnly(language)"],
    "distinct": True,
    "attributeForDistinct": "url",
    "customRanking": [
        "desc(weight.pageRank)",
        "desc(weight.level)",
        "asc(weight.position)",
    ],
    "camelCaseAttributes": ["hierarchy", "content"],
}

MARKDOWN_SETTINGS = {
    "searchableAttributes": ["title", "heading", "unordered(text)"],
    "attributesToHighlight": ["title", "text"],
    "attributesForFaceting": ["filterOnly(lang)"],
    "ignorePlurals": True,
    "minProximity": 1,
    "removeStopWords": False,
    "removeWordsIfNoResults": "lastWords",
    "typoTolerance": False,
    "advancedSyntax": False,
}


def wait_task(app_id: str, api_key: str, index: str, task_id: Any, timeout: float = 60) -> None:
    """Block until an indexing task is published. Clear-then-batch without this
    can leave the index empty: Algolia runs tasks asynchronously, and a later
    clear can wipe a batch that already returned 200."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        data = search_api(app_id, api_key, "GET", f"/1/indexes/{index}/task/{task_id}")
        if isinstance(data, dict) and data.get("status") == "published":
            return
        time.sleep(0.25)
    raise TimeoutError(f"Algolia task {task_id} on {index} not published within {timeout}s")


def replace_all_objects(app_id: str, api_key: str, index: str, objects: list[dict]) -> None:
    cleared = search_api(app_id, api_key, "POST", f"/1/indexes/{index}/clear")
    if isinstance(cleared, dict) and "taskID" in cleared:
        wait_task(app_id, api_key, index, cleared["taskID"])
    if not objects:
        return
    batch_size = 500
    for i in range(0, len(objects), batch_size):
        chunk = objects[i : i + batch_size]
        batched = search_api(
            app_id,
            api_key,
            "POST",
            f"/1/indexes/{index}/batch",
            {"requests": [{"action": "addObject", "body": obj} for obj in chunk]},
        )
        if isinstance(batched, dict) and "taskID" in batched:
            wait_task(app_id, api_key, index, batched["taskID"])


def set_index_settings(app_id: str, api_key: str, index: str, settings: dict) -> None:
    result = search_api(app_id, api_key, "PUT", f"/1/indexes/{index}/settings", settings)
    if isinstance(result, dict) and "taskID" in result:
        wait_task(app_id, api_key, index, result["taskID"])
