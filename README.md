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

**Per the HC-2 operator scope override, an agent never performs the deploy.**
The human does it. The exact by-hand sequence:

1. Create the GitHub repo (the human does this — agents must not run
   `gh repo create`, `git remote add`, or `git push`).
2. Push this repo's `main` branch to the new remote.
3. In the GitHub repo: **Settings → Pages → Build and deployment → Source**
   → select **GitHub Actions**.
4. Trigger the workflow (push to `main`, or run it from the Actions tab with
   "Run workflow"). The `build` job runs `mkdocs build --strict --clean` and
   uploads `site/`; the `deploy` job publishes it to Pages.
5. Copy the resulting Pages URL (printed by the `deploy` job as
   `page_url`, and shown in the repo's Pages settings) into the
   `TODO: deployed URL` line below and into `mkdocs.yml`'s `site_url`.

If GitHub Pages is unavailable, the same `site/` directory can be deployed to
any static host (Cloudflare Pages, Netlify, S3 + CloudFront) — `mkdocs build`
produces plain HTML/CSS/JS with no server-side runtime.

## TODO: deployed URL

```
TODO: deployed URL — fill in after the human performs the GitHub Pages deploy.
```

**HC-3 consumes this URL as `EXPO_PUBLIC_WIKI_URL`** in the Seek Uplift app
(`redesign/launchpad-mobile-redesign`). Until a real URL is set here, the
app's wiki row stays hidden by design (HC-1 gates it behind
`Boolean(process.env.EXPO_PUBLIC_WIKI_URL)`).

When the URL is known:

1. Set it in `.env` of the app repo as
   `EXPO_PUBLIC_WIKI_URL=https://<org>.github.io/<repo>/`.
2. Set it here in `mkdocs.yml` as `site_url:` so MkDocs emits canonical links
   and sitemap entries against the real origin.
3. Re-export the app web build with `npx expo export -p web --clear` (Metro's
   transform cache ignores env).

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
