# Fees

--8<-- "includes/test-banner.md"

Every trade pays a fee set by the coin's **fee tier** (picked at launch,
permanent). Meteora takes **20%** of that fee first. The rest splits three
ways — the same split on the curve and after graduation:

| Recipient | Share* |
|---|---|
| Creator | **30%** |
| SeekUplift | **30%** |
| Project or cause | **40%** |

\* Of trading fees, after Meteora's 20% protocol share.

Example — a $100 trade at 1.25%: $1.25 fee → $0.25 Meteora, **$0.30**
creator, **$0.30** SeekUplift, **$0.40** project or cause.

It is also what **Review fees** in the Launch wizard opens.

## Fee tiers

| Tier | On the curve | After graduation |
|---|---|---|
| Market-cap decay | **99% → 1.25%** over ~10 min (anti-sniper), then **1.25%** | **1.25% → 0.30%** as market cap grows |
| Flat 5% / Flat 10% | Same flat base on every trade | Same flat rate |

A volatility fee can add to the curve fee during sharp price moves. SOL gas
is separate.

## Notes

- Creators claim their share on-chain from **Rewards**. See
  [Creators](creators.md).
- The project-or-cause share is distributed **manually** for now — not
  automatic, not locked, spend not live.
- Not part of this split: SOL gas, launch costs, DAMM v2 LP mechanics
  outside the fee above.
