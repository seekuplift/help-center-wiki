# Seek Uplift Help Center Wiki

A static help-center wiki for the **Seek Uplift** app, built with
[MkDocs](https://www.mkdocs.org/) and the
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme,
**used stock** — no custom theme, no project CSS, no project JS, no
`overrides/` directory. Analytics and cookie-consent plugins are OFF on
purpose: the wiki renders inside the app's incognito WebView, where anything
that touches browser storage misbehaves.

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
├── docs/
│   └── index.md                   # the home page (real content, not lorem)
├── mkdocs.yml                     # MkDocs + Material config (stock)
├── README.md                      # this file
└── requirements.txt               # pinned mkdocs + mkdocs-material
```

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
   `build` job runs `mkdocs build --strict --clean` and uploads `site/`; the
   `deploy` job publishes it to Pages.
5. Record the Pages URL in this README and in `mkdocs.yml`'s `site_url`.

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
5. Push (the human) to trigger the Pages deploy.

Markdown extensions enabled in `mkdocs.yml`: `admonition`, `pymdownx.details`,
`pymdownx.superfences` (fenced code with syntax highlighting),
`pymdownx.tabbed`, `tables`, and `toc` with permalink anchors. Use them; do
not add bespoke HTML/CSS.

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

Note the mechanism: stock Material at 360px **wraps** wide content
(`pre { white-space: pre-wrap }` plus `overflow-wrap: break-word` on
`.md-typeset`) rather than scrolling it inside a container. Either behaviour
satisfies the requirement — what must hold is that the *page* never scrolls
horizontally. Do not add project CSS to change this; stock-theme-only is a
ticket constraint.

## License / scope

This repo holds only the help-center wiki source and its build/deploy pipeline.
It does not contain app or backend code. Cross-repo rules live in the
workspace root `AGENTS.md`.
