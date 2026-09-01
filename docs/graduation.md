# Graduation

--8<-- "includes/test-banner.md"

Every Seek Uplift launch starts on a **bonding curve**. When that curve fills,
the coin **graduates** to the open market.

## On the curve

Home’s lifecycle tabs:

| Tab | Meaning |
|---|---|
| **New** | Launched in the last 24 hours and still on-curve |
| **Bonding** | Every token still on the curve (including New) |
| **Graduated** | Off the curve — open market |

A coin can appear in both **New** and **Bonding**. Status copy is **Raising
liquidity on curve**.

While on-curve:

- Buys and sells route through **Meteora DBC**
- The [1.25% bonding-curve fee](fees.md) (after the anti-sniper window) applies
- Progress toward graduation is visible on the token page and, if you opted in,
  via curve-milestone notifications

## What graduation is

Graduation means the curve is complete and liquidity moves to a **DAMM v2**
pool. After that, the app trades the token through **Jupiter**, not DBC.

Graduation is **not** a hole in trade history. The token page keeps pre- and
post-graduation executions in one continuous chart.

You may get a **graduation** notification for a token you hold or watch if that
alert is enabled in Settings.

## The brief untradeable window

There are three pool states:

1. **Curve active** — trade via DBC.
2. **Curve complete, not yet migrated** — DBC rejects (“pool is completed”)
   and the open-market pool does not exist yet. **Nothing is tradeable.**
3. **Migrated** — trade via Jupiter.

Step 2 is usually short. It lasts until the migration transaction lands
(permissionless on-chain; the in-app UI does not have a “graduate this” button).

If a buy or sell fails with **pool has graduated** or **no route**:

1. Close the trade sheet.
2. Pull to refresh the token page.
3. Open Buy/Sell again — the route should now read **Jupiter**.

Do not spam retries during the window; wait for the new pool.

## Fees after graduation

The 1.25% bonding-curve split **stops** when the coin leaves the curve.

After graduation, pool / LP fees are a different mechanism (DAMM v2 / Jupiter).
They are **not** in the 0.20 / 0.525 / 0.525 table. See [Fees](fees.md) →
“What this table does not include.”

Creator **claim** of fees already earned on the curve remains on
[Rewards](creators.md).

## Selling a graduated token

Same Sell sheet, different route. If Jupiter cannot find a path, Account will
show **No trading route** and treat estimated exit as zero for that holding.
That is “cannot sell through the app right now,” not a displayed bad price.
