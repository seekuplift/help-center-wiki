# Account

--8<-- "includes/test-banner.md"

**Account** is your wallet, holdings, and the rest of the app’s settings. Connect
a wallet to see balances. You can still open Support, News, Privacy Center,
Security Policy, and Legal while disconnected.

## Launchpad balance

The headline is **LAUNCHPAD BALANCE** — the USD value of tokens you hold that
were launched on Seek Uplift. It does **not** include SOL or SKR.

When the app can quote an exit, the figure is **estimated proceeds if sold
now**, not a mark-to-market fantasy:

- A caption under the label tells you the basis (“Est. proceeds if sold now”).
- If that number has moved off the spot/paper mark, a **Paper value** line
  sits under the figure.
- A holding with **no trading route** is counted as **$0.00** estimated exit
  (you cannot sell it through the app right now). A quote that merely *failed*
  (timeout, server error) is **not** zeroed — it stays at market value with a
  warning.

Tap the small link under the amount to open the connected wallet app (Android)
or Solscan (web / fallback).

## SOL, SKR, and holdings

Above **Your launchpad holdings**:

| Row | What it is |
|---|---|
| **Solana (SOL)** | Native balance. Pays network fees. |
| **SKR** | Quote token for launchpad buys. Tap the row to **Get SKR**. |

Holdings are the coins you bought or launched. A row with high expected price
impact leads with an estimated exit and keeps market value on a second line.
**No trading route** means Jupiter could not find a path — not “a bad price.”

Pull to refresh if a row looks stale. Disconnecting hides wallet-scoped data;
it does not destroy on-chain balances.

## Get SKR

Tap the SKR row.

1. Choose how much SOL to swap (10 / 25 / 50 / 75% chips, or Max).
2. **Max leaves a small SOL reserve** (~0.005 SOL) so the swap and a later buy
   can still pay fees. Max is never your entire SOL balance.
3. Approve the Jupiter swap in your wallet.

Success offers a Solscan link. If a previous swap is still processing, wait and
retry — starting over can swap twice.

## Menu

| Row | Opens |
|---|---|
| **Rewards** | Creator trading fees you can claim. Amount in the subtitle. |
| **My interests** | Coins you follow, and why. |
| **Edit your tokens** | Creator dashboard: metadata, follower themes, drafts. |
| **Settings** | Appearance (Dark / Light / System). Mainnet only — no Devnet toggle. |
| **Support** | Chat or ticket. Same destination as Help → Contact support. |
| **News** | Progress / news (also a tab). |
| **Privacy Center** | Privacy policy, analytics, your data. |
| **Security Policy** | How to report a vulnerability; which programs the app uses. |
| **Legal** | Terms, plus the local acceptance record for this device. |

**Disconnect wallet** sits at the bottom as an unfilled control. Details:
[Wallets](wallets.md).

## Notifications

In Settings you can opt into alerts such as:

- A token you hold **graduates**
- Holder rank after a buy
- Curve milestones
- News

Permission is requested only when you tap to enable it. If the OS has blocked
notifications, the row should take you to system settings. The app stays fully
usable with notifications off.

## Appearance

Seek Uplift is dark-first. Light is a high-contrast daylight theme. **System**
follows the device. The choice survives a restart.
