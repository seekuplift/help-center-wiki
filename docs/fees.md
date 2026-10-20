# Fees

--8<-- "includes/test-banner.md"

Every trade pays a fee set by the coin's **fee tier** (picked at launch,
permanent). Meteora takes **20%** of that fee first. SOL gas is separate.

## The split

Every trading fee is divided the same way, on the bonding curve and
after graduation. The production launch config isn't final yet, so
**TBD** values for it are filled in once it is. The configs rolling out
next (the split below) are enforced on-chain.

### Standard configs (creator share 30%)

| Recipient | Share of every trading fee |
|---|---|
| Meteora (protocol) | **20%** |
| Creator | **24%** |
| SeekUplift launchpad | **24%** |
| Project or cause | **32%** |

Meteora takes 20% first. Of the remaining 80%, the creator gets 30%
(24% of the total). The other 70% is the partner share, split 30/70
to SeekUplift and 40/70 to the project or cause. In exact terms that
is 42.85% / 57.15% of the partner share; rounding favors the cause.

### Cause-only configs (memecoins only)

Some meme launches use a **cause-only** config (flat 1.25%, 5% or 10%).
The creator gets nothing and SeekUplift keeps nothing.

| Recipient | Share of every trading fee |
|---|---|
| Meteora (protocol) | **20%** |
| Creator | **0%** |
| SeekUplift launchpad | **0%** |
| Cause | **80%** |

## Fee tiers

The production launch config's schedule is **TBD**. The configs rolling
out next offer:

| Tier | Fee |
|---|---|
| 1.25% → 0.30% | **1.25%** on the curve; after graduation falls toward **0.30%** as market cap grows |
| Flat 1.25% / 5% / 10% | Same rate on every trade, before and after graduation |

Every tier, flat ones included, opens at **99%** and falls linearly over
20 periods of 75 slots (1,500 slots, about 10 minutes) to its own fee.

Flat tiers on the curve also add a small volatility surcharge when
trading is hectic (up to about +0.25% / +1% / +2% for the 1.25% / 5% /
10% tiers). The Launch wizard shows the exact schedule before you sign.

## Fee-on-transfer coins

!!! info "Upcoming, not live"
    Fee-on-transfer coins are **not available yet**. This section
    describes how they will work.

A coin can be launched as a **fee-on-transfer** coin (a Token-2022
transfer fee). The coin itself takes **1%, 5% or 10%** of every
transfer, **on top of** the trading fee above:

- It applies to buys, sells, and plain wallet-to-wallet transfers, on
  any venue, before and after graduation.
- The rate is fixed at launch and can never be changed.
- Meteora takes no cut of it, and the creator gets none.

| Config | Creator | Launchpad | Cause |
|---|---|---|---|
| Standard | 0% | **42.85%** | **57.15%** |
| Cause-only | 0% | 0% | **100%** |

The cause share is set aside on-chain, held by the program and not by
the team. Payouts start in a later release. SeekUplift claims the
launchpad share.

What you'll see: buyers receive slightly fewer tokens, and a seller's
tokens are reduced by the fee before the swap. Quotes in the app show
amounts **net of the fee**.

## What happens at graduation

When the curve fills, Meteora moves the coin to a DAMM v2 pool.

| Item | What applies |
|---|---|
| Migration fee set in our configs | **0%** (partner and creator migration fee), and a **0** pool-creation fee |
| Meteora protocol migration fee | **0.2%** of the liquidity being migrated |
| Pool trading fee after graduation | Same rate as the tier (flat tiers), or 1.25% falling toward 0.30% (market-cap tier) |
| Meteora share of that fee | **20%** by default, taken before the split above |
| Liquidity | Permanently locked: **70%** held by SeekUplift's claim account and **30%** by the creator (standard); **100%** on cause-only |

Locked liquidity can't be withdrawn; only its trading fees are
claimed. After Meteora's 20%, the rest follows the split above.

**Fee-on-transfer coins** graduate differently. The pool is funded with
amounts **after** the transfer fee, and the pool's starting liquidity is
reduced by the larger of the two transfer fees. Anything left
undeposited goes to Meteora's protocol migration fee.
