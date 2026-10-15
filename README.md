# Seek Uplift Help Center Wiki

A static help-center wiki for the **Seek Uplift** app, built with
[MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme,
plus a SeekUplift brand layer (dark navy, sprout teal, Space Grotesk / DM Sans,
Token Sprout logo). Project JavaScript is limited to Algolia DocSearch / Ask
AI. Analytics and cookie-consent plugins are OFF on purpose: the wiki renders
inside the app's incognito WebView, where anything that touches browser
storage misbehaves. Ask AI is optional: `searchMode` in `algolia-public.js`
is the operator switch, Material lunr stays if Algolia config is missing
or the widget fails to load, and empty DeepSeek credits remount keyword
search instead of leaving an Ask AI error on screen.

This repo is one of the independent git repos under the
`solana/meteora-scaffold-3` workspace root (the root itself is not a git repo).
It is the deliverable for ticket **HC-2** in
`redesign/launchpad-mobile-redesign/tickets-help-center.md`. Design context:
`docs/superpowers/specs/2026-08-27-in-app-help-center-design.md`, section 2
"Wiki".

## Layout

```
wiki/
├── .github/workflows/deploy.yml   # CI pipeline: mkdocs build → GitHub Pages
├── .gitignore                     # ignores site/ and .venv/
├── includes/
│   └── test-banner.md             # shared PUBLIC TEST admonition (not a page)
├── docs/
│   ├── assets/
│   │   ├── logo.png               # Token Sprout header mark
│   │   └── favicon.png
│   ├── javascripts/
│   │   ├── algolia-public.js      # public search-only config + searchMode
│   │   └── algolia-init.js        # DocSearch v5 + Ask AI (lunr / keyword fallback)
│   ├── stylesheets/
│   │   ├── extra.css              # SeekUplift palette, type, surfaces
│   │   └── algolia.css            # DocSearch header slot
│   ├── index.md                   # help-center home (user-facing)
│   ├── getting-started.md
│   ├── fees.md                    # bonding-curve fee split (source of truth)
│   ├── launching.md
│   ├── support.md                 # help and FAQ
│   └── privacy.md
├── overrides/
│   └── main.html                  # theme-color + Space Grotesk
├── scripts/
│   ├── algolia_http.py            # Algolia Search + Agent Studio REST
│   ├── algolia_records.py         # markdown → Algolia records
│   ├── index_algolia.py           # push records (needs write key)
│   ├── setup_algolia.py           # indexes, DeepSeek provider, agent
│   └── test_algolia_records.py    # record-shape unit tests
├── mkdocs.yml                     # MkDocs + Material + brand layer
├── README.md                      # this file (operators / agents)
└── requirements.txt               # pinned mkdocs + mkdocs-material
```

User-facing copy lives in `docs/`. This README is for operators and agents
(build, deploy, how to add a page). Do not put agent instructions on a wiki
page — testers read those pages inside the app.

## Build by hand

The build is fully reproducible locally — you do not need CI to produce the
site.

```sh
# from the wiki/ repo root
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs build --strict --clean
```

`mkdocs build` writes the static site to `site/` (gitignored). To preview it
locally instead:

```sh
.venv/bin/mkdocs serve
# open http://127.0.0.1:8000
```

To serve the already-built `site/` with a plain static server (used for the
360px mobile check):

```sh
cd site && python3 -m http.server 8000
```

## Deploy by hand

The deploy pipeline lives in `.github/workflows/deploy.yml`. It runs
`mkdocs build` and publishes `site/` to **GitHub Pages** for this repo.

**Operator-authorized public TEST deploy (2026-09-01):** corp account
`seekuplift`, repo `help-center-wiki`, GitHub Pages via Actions. The historical
HC-2 "agent never deploys" override is superseded for this one-time test
stand-up. Reproducible sequence:

1. Create the GitHub repo under the corp account (`gh repo create …`).
2. Push this repo's `main` branch to the remote.
3. In the GitHub repo: **Settings → Pages → Build and deployment → Source**
   → select **GitHub Actions** (or `gh api …/pages` with `build_type=workflow`).
4. Trigger the workflow (push to `main`, or Actions → "Run workflow"). The
   `build` job runs `mkdocs build --strict --clean`, optionally reindexes
   Algolia (see below), and uploads `site/`; the `deploy` job publishes it
   to Pages.
5. Record the Pages URL in this README and in `mkdocs.yml`'s `site_url`.
   Hit URLs in Algolia are built from `site_url` — if the public origin
   changes, update `site_url` and reindex.

If GitHub Pages is unavailable, the same `site/` directory can be deployed to
any static host (Cloudflare Pages, Netlify, S3 + CloudFront) — `mkdocs build`
produces plain HTML/CSS/JS with no server-side runtime.

## Deployed URL (PUBLIC TEST)

```
https://seekuplift.github.io/help-center-wiki/
```

**This is a public TEST deployment** under the corp GitHub account
`seekuplift/help-center-wiki`. It exists so the in-app Help → Wiki path can be
exercised end to end. **No production promises** — content may be incomplete,
wrong, or taken down without notice.

**HC-3 consumes this URL as `EXPO_PUBLIC_WIKI_URL`** in the Seek Uplift app
(`redesign/launchpad-mobile-redesign`). Set it in the app `.env` and re-export
web with `npx expo export -p web --clear` (Metro's transform cache ignores env).
`mkdocs.yml` `site_url` is already set to the same origin.

**Activating the wiki in shipped APKs is an EAS Update, not an app release.** The
MVP APK bakes no wiki URL, so the in-app **Guides & FAQ** row (and the launch
flow's **Review fees** link) stays hidden until we publish the flip:

```sh
eas update --channel production --environment production --message "enable help-center wiki"
```

Operational gotchas:

- The URL must be set as an **EAS environment variable** (environment
  `production`) for the bundle build — local `.env` is gitignored and never
  reaches EAS. An update built without it silently re-hides the row (no error).
- Sign the update per HITL-10 if the APK pins the code-signing cert.
- The app's `runtimeVersion` policy is `appVersion`: the update reaches only
  binaries on the same `expo.version` (do not bump for an update), and the next
  new APK must bake the URL into its embedded bundle.

Full procedure: `redesign/launchpad-mobile-redesign/docs/prod/operations-runbook.md`
→ *Releasing an update*.

## Algolia search and Ask AI — deployment

Search is two independent surfaces. GitHub Pages ships HTML/JS. Algolia holds
the searchable records. A Pages deploy without a reindex leaves search stale.
A reindex without a Pages deploy updates hits but not the widget or
`assistantId`.

### What the visitor gets

| Public config in `algolia-public.js` | Header search |
|---|---|
| `searchMode: "lunr"` (keys may stay) | Material lunr (always built) |
| Missing `appId` / search key / `indexName` | Material lunr |
| `searchMode: "keyword"` | DocSearch v5 keyword search, no Ask AI tab |
| `searchMode: "askAi"` (needs `assistantId`) | DocSearch v5 keyword search **and** Ask AI |
| `searchMode` omitted, `assistantId` set | Same as `"askAi"` |
| `searchMode` omitted, `assistantId` empty | Same as `"keyword"` |
| DocSearch CDN or Algolia API unreachable | Lunr (init script no-ops on failure) |
| Ask AI completion returns quota/auth error | Keyword search for the rest of that tab |

Ask AI is the assistant tab inside the DocSearch modal, not a second widget.
Do not empty `assistantId` to turn Ask AI off — change `searchMode` so
turning it back on is one field.

### Switching search modes

Edit `docs/javascripts/algolia-public.js`, commit, push `main` (or run
**Build and deploy wiki to GitHub Pages**). Already-open tabs keep the old
JS until refresh. This is the site-wide switch; there is no Algolia-dashboard
toggle that hides the widget.

**Ask AI off, keep Algolia keyword search** (typical when DeepSeek credits
are gone and you do not want anyone to hit the Ask AI tab):

```js
"searchMode": "keyword"
```

**MkDocs / Material lunr only** (no Algolia widget):

```js
"searchMode": "lunr"
```

**Ask AI back on** after topping up DeepSeek or finishing the outage:

```js
"searchMode": "askAi"
```

Leave `appId`, `apiKey`, `indexName`, `markdownIndexName`, and `assistantId`
in place. `scripts/setup_algolia.py` **preserves** `searchMode` if it is
already `keyword` or `lunr`, so a setup re-run does not silently re-enable
Ask AI.

Do **not** unpublish the Agent Studio agent or rotate the DeepSeek key as
the kill switch — the Ask AI tab still renders and then errors. Do **not**
drop `ALGOLIA_WRITE_API_KEY` from Actions; that only skips reindexing.

**Automatic fallback** (no deploy): DocSearch Ask AI posts to Agent Studio
`/completions`. If that returns 401/402, a non-Cloudflare 403, or a 4xx/5xx
body that looks like quota/credits/billing, the init script destroys the
Ask AI widget and remounts keyword search. `sessionStorage` remembers that
for the tab so later wiki pages in the same visit never open the Ask AI
tab. The in-app incognito WebView may refuse storage; then the remount
still holds for the current page only.

That fallback cannot hide the very first failed Ask AI turn (the completion
has to fail before we know credits are gone). It also cannot change what
other visitors see — only `searchMode` + a Pages deploy does that. Prefer
the operator switch as soon as you know DeepSeek is empty. Keyword search
does not use DeepSeek, so falling all the way back to lunr on a credit
error would throw away working search.

### Secrets vs public config

Safe to commit (`docs/javascripts/algolia-public.js`):

- Algolia **application ID**
- **Search-only** API key (ACL: `search`)
- Index names `help_center` and `help_center_markdown`
- Agent Studio **agent ID** (`assistantId`), once setup has created it
- `searchMode` (`askAi` / `keyword` / `lunr`)

Never commit, never put in `mkdocs.yml` or the JS files:

- Algolia **write / admin** key (`addObject`, `deleteObject`, `editSettings`,
  `settings`)
- **DeepSeek** API key (Ask AI LLM; billed by DeepSeek)

Local / CI environment names:

| Variable | Used by | Required for |
|---|---|---|
| `ALGOLIA_APP_ID` | setup, index, CI | both |
| `ALGOLIA_SEARCH_API_KEY` | setup (written into public JS) | Ask AI setup |
| `ALGOLIA_WRITE_API_KEY` or `ALGOLIA_ADMIN_API_KEY` | setup, index, CI | both |
| `DEEPSEEK_API_KEY` | setup only | Ask AI agent |

### First-time (human, once per Algolia app)

1. Confirm the Algolia application has **Generative AI / Agent Studio**
   enabled (Dashboard → Generative AI). Without that, `setup_algolia.py`
   can still save index settings, then fails with *This feature is not
   enabled for this application.* Keyword search can ship; Ask AI cannot.
2. Export the four variables above in the shell. Do not write them to a
   file in this repo.
3. From the wiki repo root:

   ```sh
   .venv/bin/python scripts/setup_algolia.py
   .venv/bin/python scripts/index_algolia.py
   ```

4. Commit the updated `docs/javascripts/algolia-public.js` (it now
   contains `assistantId` and `searchMode`). Push so Pages serves the
   widget with Ask AI, unless you left `searchMode` at `keyword` or `lunr`.
5. In GitHub → `seekuplift/help-center-wiki` → Settings → Secrets and
   variables → Actions, add:

   - `ALGOLIA_APP_ID`
   - `ALGOLIA_WRITE_API_KEY`

   Do **not** add the DeepSeek key or the search-only key as Actions
   secrets. DeepSeek is only needed for setup/provider create. The
   search-only key is already in the committed public JS.

`setup_algolia.py` is idempotent: it reuses a DeepSeek provider and the
agent named **Seek Uplift Help Center**, publishes the agent, and allows
origins `https://seekuplift.github.io`, `http://127.0.0.1:8000`, and
`http://localhost:8000`. If the public origin changes, add the new origin
and re-run setup.

### Every content deploy

The Pages workflow (`.github/workflows/deploy.yml`) is:

1. `mkdocs build --strict --clean`
2. `python scripts/index_algolia.py` **if** `ALGOLIA_WRITE_API_KEY` is set
3. Upload `site/` and deploy to GitHub Pages

Missing Algolia secrets **skip indexing** (`exit 0`) and still publish the
site. That is intentional so a Pages-only test deploy cannot be blocked by
Algolia. It also means a push that only changes `docs/*.md` will show new
pages in the wiki but **old** Algolia hits until the secret is present or
someone runs `index_algolia.py` by hand.

Reindex by hand (same write key in the environment):

```sh
.venv/bin/python scripts/index_algolia.py
```

`index_algolia.py` clears and replaces both indexes from `docs/*.md` plus
`mkdocs.yml` `nav` (lvl0 section titles) and `site_url` (absolute hit URLs).
PUBLIC TEST banners / `--8<--` snippets are stripped so Ask AI does not
quote them as product copy.

`mkdocs build` does **not** talk to Algolia. `requirements.txt` stays
MkDocs-only; the index/setup scripts use the stdlib HTTP client.

### Runtime (after Pages is live)

The in-app WebView loads the Pages origin. DocSearch then calls:

- `cdn.jsdelivr.net` for `@docsearch/js@5` and `@docsearch/css@5`
- Algolia search hosts (`{appId}-dsn.algolia.net` / `*.algolianet.com`)
- Agent Studio completions (Ask AI only), restricted to the allowed
  origins above

Those are XHR/script loads, not WebView navigations, so the app host
allowlist does not need Algolia hosts. If jsdelivr or Algolia is blocked,
lunr remains. DocSearch is initialized with
`disableUserPersonalization: true` so it does not use `localStorage`
(unreliable in the incognito WebView).

Indexed hit URLs use `mkdocs.yml` `site_url`
(`https://seekuplift.github.io/help-center-wiki/`). Local `mkdocs serve`
still searches the production index; clicking a hit opens the Pages URL,
not `http://127.0.0.1:8000`.

### Failure modes worth checking before a “search is live” call

- **Agent Studio 403 “feature is not enabled”** — turn the product on in
  the dashboard; re-run setup. Keyword search can already be live.
- **Write key lacks `settings` / `addObject`** — index step fails; Pages
  HTML still deploys; lunr or stale Algolia remains.
- **CI secret missing** — look for `Skipping Algolia index` in the build
  log. Pages succeeded; search was not refreshed.
- **`site_url` / Pages path prefix wrong** — hits 404. Reindex after
  fixing `site_url`.
- **`searchMode` is `"keyword"` or `"lunr"`** — Ask AI tab is off until
  you set `"askAi"` and redeploy. `assistantId` can stay in the file.
- **`assistantId` empty while `searchMode` is `"askAi"`** — no Ask AI tab.
  Keyword DocSearch still mounts if the other public fields are set.
- **Ask AI shows an error then the tab disappears** — DeepSeek quota/auth
  failed; this tab now uses keyword search. Set `searchMode` to
  `"keyword"` and deploy so every visitor skips Ask AI.
- **New markdown page not in `nav:`** — page is reachable and lunr-indexed
  at build; Algolia lvl0 falls back to `"Help Center"` until it is in
  `nav` and reindexed.

Ask AI LLM usage is billed by DeepSeek, not by this repo. Algolia search
operations count against the Algolia app plan.

## Adding a page (for agents and humans)

1. Create `docs/<page>.md`. Markdown only — no front matter required.
2. Add the page to the `nav:` list in `mkdocs.yml`. Without a `nav:` entry the
   page is still reachable via search but not from the side/top nav.
3. Rebuild: `.venv/bin/mkdocs build --strict --clean` (or `mkdocs serve` to
   preview). `--strict` will fail the build on broken links or missing
   references, which is what you want before a deploy.
4. Commit the new `docs/<page>.md` and the `mkdocs.yml` change in this repo
   only (never stage across the workspace-root boundary — see the root
   `AGENTS.md`).
5. Push (the human) to trigger the Pages deploy. If Algolia CI secrets are
   set, that push also reindexes; otherwise run `scripts/index_algolia.py`
   so DocSearch/Ask AI see the new page.

Markdown extensions enabled in `mkdocs.yml`: `admonition`, `pymdownx.details`,
`pymdownx.superfences` (fenced code with syntax highlighting),
`pymdownx.tabbed`, `pymdownx.snippets` (shared `includes/test-banner.md` on
every page except the longer home warning), `tables`, and `toc` with permalink
anchors. Use them. Visual brand lives in `docs/stylesheets/extra.css` and
`overrides/main.html`. Do not add page-level HTML/CSS. The only project
JavaScript is Algolia Ask AI (`docs/javascripts/algolia-*.js`).

Every user-facing page must keep a **PUBLIC TEST — NOT PRODUCTION** warning.
Home has the long form; other pages include `includes/test-banner.md` via
`--8<--`. Do not drop the banner because the copy got “more production-ready.”

## Mobile (360px) check

The site must be legible at 360px width with **no horizontal page scroll**.
Verify after adding or editing a page:

```sh
.venv/bin/mkdocs build --strict --clean
cd site && python3 -m http.server 8000
# then, at viewport width 360, check:
#   document.documentElement.scrollWidth <= document.documentElement.clientWidth
#   and that the hamburger drawer (label.md-header__button[for="__drawer"]) opens
```

Measured for HC-2 with headless Chromium at 360x640 against `docs/index.md`:
`scrollWidth == clientWidth == 360` before and after opening the drawer, drawer
opens, no console errors.

Note the mechanism: Material at 360px **wraps** wide content
(`pre { white-space: pre-wrap }` plus `overflow-wrap: break-word` on
`.md-typeset`) rather than scrolling it inside a container. Either behaviour
satisfies the requirement — what must hold is that the *page* never scrolls
horizontally. Brand CSS in `docs/stylesheets/extra.css` must keep that wrap
and must not introduce a page-level horizontal scroll. No analytics or
cookie-consent plugins. Algolia Ask AI is the only project JavaScript; it
must keep the 360px no-horizontal-scroll rule (icon-only DocSearch button).

## License / scope

This repo holds only the help-center wiki source and its build/deploy pipeline.
It does not contain app or backend code. Cross-repo rules live in the
workspace root `AGENTS.md`.
