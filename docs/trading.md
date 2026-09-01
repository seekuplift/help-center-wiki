# Buy and sell

--8<-- "includes/test-banner.md"

Open any token from Home, Callouts, or a search. **Buy** and **Sell** sit
directly under the header. This page is how those sheets work — not a
recommendation to trade.

## Quote token is SKR

On-curve buys pay in **SKR**. SOL is for network fees and for swapping *into*
SKR.

- The Buy **BALANCE** line is SKR held, not SOL.
- Amount chips are **10 / 25 / 50 / 75%** of available SKR (buy) or of the
  token you hold (sell). There is no 100% chip.
- **Max** sits on the PAY WITH / SELL label so the number can use the full
  width. Buy Max = all SKR; Sell Max = the exact token holding.

Default typed amount is a small test size (`0.001`). Change it.

## If you only have SOL

The sheet will say you need SKR and offer **Get SKR & Buy**:

1. Approve a **SOL → SKR** swap. This is not the token purchase.
2. Approve the **buy** as a second transaction.

A small leftover SKR (~2% buffer) can remain in the wallet after the buy. If
the swap is submitted but not yet confirmed, **retry** — do not start a second
swap.

You can also buy SKR first from Account → SKR. See [Account](account.md).

## Routes

| Token state | Route you will see |
|---|---|
| Still on the bonding curve | **Meteora DBC** |
| Graduated (migrated pool) | **Jupiter** |

The app picks the route from live pool state. After a coin graduates, close
and reopen the trade sheet if it still looks like a DBC pool.

!!! note "A short pause at graduation"
    When the curve is full but the open-market pool is not created yet,
    neither route works. That window is usually brief. If you see “pool has
    graduated” or “no route,” wait, pull to refresh, and open the sheet again.
    More: [Graduation](graduation.md).

Network fee for a trade is on the order of **~0.00012 SOL** (gas). That is
separate from the bonding-curve trading fee in [Fees](fees.md).

## Review before you sign

The wallet prompt is the last check. Confirm mint, side (buy vs sell), and
amount.

- **Cancel / reject** → no funds moved. Close any leftover approval in the
  wallet before retrying.
- Invalid amounts (`0`, empty, more than you hold) are refused **before** a
  wallet prompt.
- Sell on a token you hold **none** of is an empty state, not an error.

Sell is styled red on purpose so it does not look like Buy.

## After a trade

- Balances and the token page update from confirmed chain state plus the live
  feed. Give indexing a moment if a number looks briefly stale.
- A qualifying sell may offer a **share your gain** card. You can hide the
  dollar amount, hide the token identity, or dismiss with **Not now**.
- **Follow** after a buy is opt-in. A **full sell** (dust left ≤ $0.10) of a
  followed coin unfollows it automatically, with **Undo**. Partial sells do
  not. See [Communities](communities.md).

## Charts and prices

The price chart is an **execution view**: it moves on actual buys and sells,
not on a ticking quote. Ranges are 5m / 1h / 24h / 7d. A window with no trades
in range stays flat and says so.

Headline prices and candles are **display-grade**. They are fine for the UI.
They are **not** an input to fee claims, treasury, or payouts.

Tiny prices use subscript notation (for example $0.0₈1615) so they do not
round to “$0”.

**Price unavailable** means this token has traded but the live price is not
loading. Everything else on the page still shows.

## Report a token

On the token page, **Report** (wallet connected) files:

- Token Policy Violation
- Trademark Infringement
- DMCA

Do not put private personal data in the comment. Reports are attributed to the
connected wallet for abuse prevention. See [Privacy and safety](privacy.md).
