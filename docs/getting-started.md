# Getting started

--8<-- "includes/test-banner.md"

This page walks a first session: accept Privacy & Terms, connect a wallet, get
the quote token if you need it, and make a small buy. Nothing here is
financial advice — only you decide whether to sign a transaction.

## 1. First launch

On a fresh install the app shows a short welcome, then **Privacy & Terms**.

- **Continue** opens Privacy Policy and Terms in one sheet.
- **I agree to the Privacy Policy and Terms** is what actually starts the app.
- Close, swipe away, or use Back **without** agreeing and you stay on the
  welcome screen. That is expected.

A later policy or terms version can ask you to review again.

Privacy choices (analytics, data export, deletion) live in **Account → Privacy
Center** after you are in. See [Privacy and safety](privacy.md).

## 2. Find your way around

The tab bar has five places:

| Tab | What it is |
|---|---|
| **Home** | The token feed. Filter New / Bonding / Graduated, search, sort. |
| **Callouts** | Coins people are calling out on X. Marked **BETA**. |
| **Launch** | Plant an idea or a meme. |
| **Progress** | News and, when you follow coins, personalized updates. |
| **Account** | Wallet, holdings, rewards, settings, legal. |

The help icon is on every screen. That is how you got here.

## 3. Connect a wallet

You can browse Home, news, and token pages without a wallet. Connecting unlocks
buy, sell, launch, claim, follow, report, and community posting.

=== "On Android (Seeker and other devices)"

    1. Tap **Connect wallet** on Account, or take a gated action such as Buy.
    2. If more than one wallet is installed, pick one from **Select a wallet**.
       The built-in Seeker wallet is labeled **Seeker Wallet**.
    3. Approve the connection in that wallet.

    Compatible Solana wallets work. If you need an install recommendation, the
    app points to **Jupiter Wallet**.

=== "On the web"

    1. Use a wallet-standard browser wallet (for example Jupiter’s extension).
    2. Tap **Connect wallet** and approve in the wallet.
    3. After a reload, a connected session should stay connected. You still
       approve each transaction yourself.

Connecting is **not** the same as signing a trade. The app does not pop a
signature on its own when a screen opens. Every sign starts from an action you
tapped — Buy, Launch, Claim, Sign in, and so on.

More detail: [Wallets](wallets.md).

## 4. Get the quote token

Launchpad buys on the curve pay in the launchpad's **quote token** (SKR
today), not SOL.

- SOL still pays network fees and is what you swap *into* it.
- On **Account**, SOL and the quote token sit above your launchpad holdings.
  Tap it to open **Get the quote token** (a SOL → quote-token swap).
- Max leaves a small SOL reserve so you can still pay fees.

If you tap Buy with only SOL, the trade sheet can run a combined swap-then-buy
flow (shown as **Get SKR & Buy** today): a SOL → quote-token swap, then the
token buy. You approve **each** step in your wallet. That is two signatures,
on purpose.

## 5. Find a token and buy

1. On **Home**, stay on **Bonding** to see coins still on the curve. **New** is
   the last 24 hours on-curve. **Graduated** have left the curve.
2. Open a token. Buy / Sell sits under the header.
3. Enter an amount in the quote token, or use the quick percentage chips.
   **Max** uses your full quote-token balance (buy) or the exact token
   holding (sell).
4. Review the wallet prompt. Cancel there and **no funds move**.

!!! warning "The first ~10 minutes are not the 1.25% fee"
    At pool open the bonding-curve fee starts at **99%** and decays to **1.25%**
    over about ten minutes. That window is a sniper deterrent. Read
    [Fees](fees.md) before you trade a brand-new pool.

After a buy, the app may ask if you want to **follow** the coin. That is
optional. After a full sell, a followed coin is unfollowed for you, with Undo.
See [Communities](communities.md).

## If something fails

- A declined wallet prompt is safe: nothing moved. Retry when you are ready.
- “Live prices paused” on the top bar means the live stream is reconnecting,
  stale, or offline. Pull to refresh when you are back online.
- Kill the app mid-sign on Android: the app reconciles silently on relaunch.
  Check the wallet and Solscan if you are unsure whether a transaction landed.

Still stuck? [Getting help](support.md).
