# Privacy and safety

--8<-- "includes/test-banner.md"

The in-app **Privacy Center**, **Legal**, and **Security Policy** are the
documents of record. This page is a plain-language map — if they
disagree, those screens win.

## First launch

The app starts only after you accept the current **Privacy Policy and
Terms**, including the jurisdiction box. A version bump can ask you to review again.

## Availability by region

In the US, UK, and EU/EEA the app is currently a closed beta: you see a
**Seek Uplift Beta** waitlist screen until you're admitted. Joining stores
a device identifier, your notification token (Android) or an optional email
(web), and the country derived from your network location (not your IP).

Some features are unavailable in some regions — currently idea and startup
create/buy/sell in the US and UK, stock-quoted create/buy/sell in the
US, and cause-related visibility and marketing in the US, UK, Australia,
and the UAE. Meme launches are unavailable in those four countries too,
because every meme backs a cause; meme buy/sell is not region-gated.
The list is managed
server-side and can change without an app update (full list: Terms →
Restricted jurisdictions). The app checks your
network location (IP mapped to country, never tied to your wallet).
The lookup itself is kept in memory, but two exceptions store a country:
the beta waitlist keeps it with the waitlist entry, and the app caches
the last country on-device for up to 24h for outage use.
Unavailable actions stay visible but disabled.
If your location can't be determined, no regional restrictions apply; if
our servers can't be reached at all, the app shows a **We're currently
down** screen instead of opening.

## What the app may process

Wallet state and public address, balances and signatures, launch content
and images, reports, bug reports (see [Getting help](support.md)),
support messages, follows and the reasons you give, posts, a linked X
account (if you link one), the instant-wallet email (handled by
magic.link), callout activity tied to your wallet (kept 30 days),
diagnostics, crash reports, and analytics (on after you accept unless you
turn it off or turn on Do Not Sell or Share — both in Privacy Center). On
Android, crash reporting has its own switch in Privacy Center. Report data
is kept up to 24 months, with legal-hold exceptions.

Reports are **wallet-attributed**. Uploads pin via
the backend and, once on-chain, can be public and permanent.

## Rules we never break

- **Never ask for your seed phrase or private keys.**
- **No signature on screen open** — every prompt starts from your tap.
- **Not financial advice.** Mainnet only.
- External links from token metadata ask you to confirm the host first.

Privacy Center handles analytics choices, local data export, and backend
deletion requests (by email).
California rights (know, delete, correct, opt out) start there or via
support.
