# Launch a coin

--8<-- "includes/test-banner.md"

The **Launch** tab deploys a coin on Meteora's Dynamic Bonding Curve on
Solana mainnet. The mint is permanent. Review every wallet prompt before
you sign.

## Idea or meme

| Type | Project-or-cause fees go to |
|---|---|
| **An idea** | The project |
| **A meme with impact** | Exceptional causes the meme backs |

Both share the same split: **Creator 30% · SeekUplift 30% · Project or
cause 40%** (after Meteora's 20%). Full table: [Fees](fees.md).
Where shown, **Review fees** on that step opens the Fees page.

Startup create is currently turned off. Idea, startup, and meme launches — and
idea/startup and stock-quoted trading — are also unavailable in some regions:
the option stays visible but disabled, with the reason underneath. See
[Privacy and safety](privacy.md).

## Fee tier

Where more than one is offered, pick a **fee tier** (**1.25% → 0.30%**,
**Flat 1.25%**, **Flat 5%**, or **Flat 10%**, plus cause-only variants on
some configs). It sets the coin's trading fee
forever — **this choice is permanent**. Detail lines show the curve rate
and the after-graduation rate before you confirm.

## What to fill in

Required: logo, name (at least 3 characters, max 32 UTF-8 bytes), symbol
(max 10 UTF-8 bytes), description — plus use case, problem, and
prototype link for ideas.

Optional: **creator first buy** (defaults to 100 SKR to seed your own
position; clear to skip; not offered on every config), website, X, and —
for meme coins — a **cause funding mode** (see below).

Uploads pin **before** you sign and may become public permanently. No gas
is spent on upload. Retrying reuses the uploaded image — don't pick a new
one, just tap retry. Uploads are limited (about 10 per hour).

## Cause funding mode (meme coins)

Pick where the coin's **40% project-or-cause share** goes. The
**Philanthropic fund** is the default and preselect. The other live
options are a **curated cause**, a **specific Giveth project**, and
**decide later**.
Letting an **X or Reddit account** choose is deferred — those rows
appear in the picker once their config enables them. **DAO** is shown
as planned — it cannot be selected yet.

- **Philanthropic fund** — the share goes to the SeekUplift
  philanthropic fund, spent at SeekUplift's discretion with every
  payout published. It is never a guaranteed donation to a specific
  cause.
- **Curated cause / Giveth project** — the share is earmarked for the
  cause basket or project you name.
- **Decide later** — you pick the destination from the Creator Dashboard
  within **90 days** of launch.
- **X / Reddit account** (deferred, not selectable yet) — the named
  account claims the choice with **Claim as @handle** (a fresh X
  verification, or the wallet's verified Reddit link) within **90
  days**, then picks the destination within **30 days**.
- Anything undecided at the deadline **falls back to the philanthropic
  fund**.

The choice is **permanent once final** — it cannot be changed after it
lands. Review & launch restates your pick before you sign.

## Idea funding mode (idea coins)

Pick where the coin's **40% idea share** goes. **Direct payout** is the
default — paid to a Solana address you name at launch. Live alternatives:
**decide later** (you pick the final mode within **90 days**, else
community takeover) and an **X or Reddit account** — the choice locks to
the handle at launch, and it has **90 days** to claim, else community
takeover. **Managed by Seek Uplift** and **Realms DAO** are shown but
can't be selected yet.

Some direct-payout coins are additionally released per **approved
milestone** (where enabled): the payout wallet files a public **funding plan** (milestones
with deliverables, evidence, deadlines, amounts; an optional kickoff up to
10%), then submits evidence, and the operator approves each one. Plans,
evidence versions, and verdicts are public on the coin page. A plan that
misses its deadlines can trigger a **milestone default**, moving the
remaining share to community takeover.

## Review and sign

**Review & launch** shows your entries. **Launch cost ≈0.013 SOL** is a
one-time rent deposit, not a trading fee. A **Launch fee** row appears
only if the config charges one.

After launch: share the mint, trading starts on the curve (the opening
fee depends on the tier — see [Fees](fees.md)), creator fees accrue to
**Account → Rewards**, and only the creator wallet can edit description,
image, and socials (on configs that grant it update authority).
