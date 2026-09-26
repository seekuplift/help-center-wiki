# Graduation

--8<-- "includes/test-banner.md"

Every coin starts on a **bonding curve**. When the curve fills, it
**graduates** to the open market (a DAMM v2 pool, traded via **Jupiter**
instead of Meteora DBC).

Home tabs: **New** (last 24h, on-curve) · **Bonding** (all on-curve) ·
**Graduated** (open market).

## The brief untradeable window

Between curve-full and pool-migrated, neither route works. If a trade
fails with **pool has graduated** or **no route**: close the sheet, pull
to refresh, reopen (route should read **Jupiter**). Do not spam retries.

## Fees after graduation

The same **30 / 30 / 40** split keeps applying after graduation (via the
locked-liquidity shares), at the coin's after-graduation rate — see
[Fees](fees.md). Creator fees earned on the curve stay claimable from
[Rewards](creators.md).
