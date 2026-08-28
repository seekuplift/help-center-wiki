# Seek Uplift Help Center

Welcome to the **Seek Uplift** help center. This wiki explains how the app works
and how to get help when something goes wrong.

Seek Uplift is an Expo / Solana Mobile app that runs on Android and the web from
a single codebase. It connects to a Mobile Wallet Adapter wallet on Android and
to wallet-standard browser wallets on web, surfaces live token data fed by the
Seek Uplift backend, and lets you launch, buy, and sell tokens on the
Dynamic Bonding Curve (DBC), claim creator fees, and report issues.

## Where to get help

The app's top bar has a help icon on every screen. Tap it to open the help menu:

| Destination | What it does |
|---|---|
| Wiki | Opens this site inside the app (incognito WebView). |
| Report a bug | Sends a short note plus build/screen context to the team. Anonymous submissions are accepted. |
| Contact support | Opens the existing support chat. |

If you cannot open the app at all, you can also reach this wiki directly in any
browser at the deployed URL recorded in this repo's `README.md`.

## How the app is wired (short version)

- **Wallets** live behind a single seam in `src/solana/wallet/`. Anything that
  touches `@wallet-ui/react-native-kit`, `@solana-mobile/*`, or
  `@wallet-ui/react` stays inside that seam so the rest of the app is
  platform-neutral.
- **Live data** (prices, trades, candles, news, rewards) comes from the Seek
  Uplift backend over a normal HTTP/streaming API. The app never talks to
  gated third-party streams directly.
- **Uploads** go through the backend proxy. The app never holds client-side
  storage credentials and has no direct-upload fallback.
- **Trades** run against the DBC program; the backend serves display-grade
  price data only and is never an input to money-moving computation.

## Reporting a bug from the app

1. Tap the help icon in the top bar.
2. Choose **Report a bug**.
3. Type what went wrong. You do not need to be signed in.
4. Submit. You will see a confirmation with a report id, or an error that tells
   you what to do next without losing what you typed.

To protect the public write path, bug reports are rate-limited per IP
(currently 5 per hour) and notes are capped at 4000 characters.

## A note on price data

Prices, trades, and candles served by the backend are **display-grade**: they
are fine for the UI and analytics, but they are **never** an input to
money-moving computation such as fee distribution, rewards accounting,
treasury settlement, or payout amounts. Settlement paths read finalized
on-chain state with integer math.

## Adding a page

Agents and humans add pages the same way — see `README.md` for the exact steps.
The short version: drop a new `docs/<page>.md`, add an entry to `nav:` in
`mkdocs.yml`, run `mkdocs build` (or `mkdocs serve`) to preview.
