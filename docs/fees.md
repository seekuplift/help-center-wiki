# Fees

--8<-- "includes/test-banner.md"

Seek Uplift takes a **bonding-curve trading fee** while a coin is on its curve.
After the opening anti-sniper window, that fee is **1.25% of traded volume**.
This page is the source of truth for that split.

It is also what **Review fees** in the Launch wizard opens.

!!! warning "Phase A — manual distribution today; automatic on-chain routing is the plan"
    Directed’s share is currently swept and distributed **manually by the
    team**, not by an on-chain program yet. This page does **not** claim those
    funds are locked, and milestone / cause **release is the intended path**,
    not a live spend mechanism today.

## Post-decay bonding-curve fee (1.25% of traded volume)

Of the **1.25%** fee, **16%** goes to the creator and **84%** is SeekUplift’s
partner share. Directed is **half of that partner share** (42% of the fee).
Creator’s 16% is **untouched** by the directed split.

| Recipient | Share of the 1.25% fee | of traded volume |
|---|---|---|
| Creator | 16% | 0.20% |
| Directed | 42% (half of SeekUplift’s 84% partner share) | 0.525% |
| SeekUplift | 42% (the other half of the partner share) | 0.525% |

84% of 1.25% is **1.05% of volume**; half of that is **0.525%**. Creator 16% of
the fee is **0.20% of volume**.

Do **not** read this as an unscoped “50% of fees” or “50% of trading fees.” The
50/50 split is **of SeekUplift’s partner share of this bonding-curve fee**, not
of all fees a trade might pay.

### Example: $100 traded (after the anti-sniper window)

| Recipient | Amount |
|---|---|
| Creator | $0.20 |
| Directed | $0.525 |
| SeekUplift | $0.525 |
| **Total fee** | **$1.25** |

The trader still pays whatever extra the curve’s optional dynamic fee and
ordinary SOL gas add. Those are **not** in this table.

## What this table does not include

These are **not** part of the 1.25% split above:

- DAMM v2 LP fees after graduation
- Pool-creation fees
- Leftover / migration proceeds
- Partner surplus
- Base-token fee dust
- SOL network (gas) fees
- The optional extra dynamic fee on the curve

## Opening anti-sniper window

At pool open the bonding-curve fee starts at **99%** and decays to the
**1.25%** post-decay base over about **10 minutes**. That window is a sniper
deterrent, not the long-run split in the table.

Buying in those first minutes is expensive by design. Wait for the fee to
decay unless you understand the cost.

## Extra dynamic fee

The curve may charge an **optional extra dynamic fee** on top of the base,
depending on pool config. That extra is **not** in the 0.20 / 0.525 / 0.525
table.

## Directed funds (Phase A)

Directed’s 0.525% of traded volume is the half of SeekUplift’s partner share
pointed at the project (idea) or the causes a meme backs.

- **Idea:** held for the project; the intended path is release as milestones
  are met.
- **Meme:** held for exceptional causes the meme backs.

Today, the 1.25% fee and the creator’s 16% share are collected and split
automatically on-chain. The rest — including the Directed / SeekUplift split —
is currently swept and divided **manually by the team**, not by an automatic
on-chain program. A fully automatic, on-chain distribution mechanism is the
direction we're building toward, not something live today. Milestone / cause
spend is **not live**. We do **not** claim the funds are locked.

Creators still claim **their** 0.20% of volume from **Rewards**. That claim
path *is* on-chain and automatic today. See [Creators](creators.md).

## Launch cost (not a trading fee)

Creating a pool is a one-time on-chain rent deposit, shown in the wizard as
**Launch cost ≈0.013 SOL**. That is not “gas” in the usual sense and is not
the 1.25% trading fee. A separate **Launch fee** row appears only if a pool
config actually charges one (shipped configs currently report none).

Details: [Launch a coin](launching.md).
