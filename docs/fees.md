# Fees

--8<-- "includes/test-banner.md"

Every trade pays a fee set by the coin's **fee tier** (picked at launch,
permanent). Meteora takes **20%** of that fee first.

## The split today

Coins launching now sit on a single live config. Its post-Meteora
remainder splits:

| Recipient | Share* |
|---|---|
| Creator | **16%** |
| Partner wallet | **84%** |

\* Of trading fees, after Meteora's 20% protocol share.

Example — a $100 trade at 1.25%: $1.25 fee → $0.25 Meteora, **$0.16**
creator, **$0.84** to the partner wallet.

The partner-wallet share is not split on-chain — the team distributes it
**manually**: part to SeekUplift, part to the project or cause the coin
backs (see the funding modes below). After graduation the creator earns
nothing further: **100% of the migrated pool's locked liquidity belongs
to the partner position**, so post-graduation LP fees accrue there.

## The new fee configs (rolling out, not yet live)

The next configs change the remainder to a three-way on-chain split —
the same on the curve and after graduation:

| Recipient | Share* |
|---|---|
| Creator | **30%** |
| SeekUplift | **30%** |
| Project or cause | **40%** |

\* Of trading fees, after Meteora's 20% protocol share.

Example under the new configs — a $100 trade at 1.25%: $1.25 fee →
$0.25 Meteora, **$0.30** creator, **$0.30** SeekUplift, **$0.40**
project or cause.

It is also what **Review fees** in the Launch wizard opens. A coin's
exact schedule is fixed by the config it launched under — the wizard
shows it before you sign.

## Fee tiers

The live config has one schedule: **99% → 1.25%** over ~10 min
(anti-sniper), then a flat **1.25%** — there is no tier picker yet. The
new configs offer:

| Tier | On the curve | After graduation |
|---|---|---|
| 1.25% → 0.30% | **99% → 1.25%** over ~10 min (anti-sniper), then **1.25%** | **1.25% → 0.30%** as market cap grows |
| Flat 1.25% | Same flat 1.25% on every trade | Same flat rate |
| Flat 5% / Flat 10% | Same flat base on every trade | Same flat rate |

Some new configs also offer cause-only variants where the creator share
is 0% and the whole remainder goes to the project or cause.

A volatility fee can add to the on-curve fee during sharp price moves
(capped at about 20% of the base fee). It does not apply after
graduation. SOL gas is separate.

## Notes

- Creators claim their on-curve share on-chain from **Rewards**.
  After-graduation fees are not claimable in the app yet. See
  [Creators](creators.md).
- The project-or-cause share is distributed **manually** for now — not
  automatic, not locked, spend not live. Some idea coins release their
  share per **approved milestone** instead — see
  [Launch a coin](launching.md).
- Not part of this split: SOL gas, launch costs, DAMM v2 LP mechanics
  outside the fee above.

## What the project-or-cause share does in each cause funding mode

- **Philanthropic fund** — held in the fund vault; the **Philanthropic
  fund** page in the app shows the public ledger of contributions and
  disbursements.
- **Curated cause / Giveth project** — earmarked for the named cause or
  project.
- **Decide later** — held until the creator picks from the Creator
  Dashboard, or falls back to the philanthropic fund at the **90-day**
  deadline.
- **X / Reddit account** (deferred) — held until the named account claims and picks
  (or the **90-day** claim deadline passes, then the philanthropic fund).
- **DAO** — planned, not selectable yet.

The philanthropic fund is spent at SeekUplift's discretion and every payout is
published — it is never a guaranteed donation to a specific cause. Idea
coins use idea funding modes instead (see [Launch a coin](launching.md)).
