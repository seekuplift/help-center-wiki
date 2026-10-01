# Fees

--8<-- "includes/test-banner.md"

Every trade pays a fee set by the coin's **fee tier** (picked at launch,
permanent). Meteora takes **20%** of that fee first. The rest splits three
ways — the same split on the curve and after graduation:

!!! note "New fee configs"
    The tiers and split on this page describe the new fee configs, which
    are still rolling out. A coin's exact schedule is fixed by the config
    it launched under — the Launch wizard shows it before you sign.

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
| 1.25% → 0.30% | **99% → 1.25%** over ~10 min (anti-sniper), then **1.25%** | **1.25% → 0.30%** as market cap grows |
| Flat 5% / Flat 10% | Same flat base on every trade | Same flat rate |

A volatility fee can add to the curve fee during sharp price moves. SOL gas
is separate.

## Notes

- Creators claim their on-curve share on-chain from **Rewards**.
  After-graduation fees are not claimable in the app yet. See
  [Creators](creators.md).
- The project-or-cause share is distributed **manually** for now — not
  automatic, not locked, spend not live.
- Not part of this split: SOL gas, launch costs, DAMM v2 LP mechanics
  outside the fee above.

## What the 40% share does in each cause funding mode

- **Managed fund** — held in the fund vault; see the **Fund page** in the
  app for the public ledger of contributions and disbursements.
- **Curated cause / Giveth project** — earmarked for the named cause or
  project.
- **Decide later** — held until the creator picks from the Creator
  Dashboard, or falls back to the managed fund at the **90-day**
  deadline.
- **X / Reddit account** (deferred) — held until the named account claims and picks
  (or the **90-day** claim deadline passes, then the managed fund).
- **DAO** — planned, not selectable yet.

The managed fund is spent at SeekUplift's discretion and every payout is
published — it is never a guaranteed donation to a specific cause. Idea
coins have their own funding modes; a cause is never an idea coin's
destination.
