# Launch a coin

--8<-- "includes/test-banner.md"

The **Launch** tab deploys a coin on Meteora's Dynamic Bonding Curve on
Solana mainnet. The mint is permanent. Review every wallet prompt before
you sign.

## Idea or meme

| Type | Project-or-cause fees go to |
|---|---|
| **An idea** | The project, released as milestones are met |
| **A meme with impact** | Exceptional causes the meme backs |

Both share the same split: **Creator 30% · SeekUplift 30% · Project or
cause 40%** (after Meteora's 20%). Full table: [Fees](fees.md).
**Review fees** on that step opens the Fees page.

Startup create is currently turned off.

## Fee tier

Where more than one is offered, pick a **fee tier** (**1.25% → 0.30%**,
**Flat 5%**, or **Flat 10%**). It sets the coin's trading fee
forever — **this choice is permanent**. Detail lines show the curve rate
and the after-graduation rate before you confirm.

## What to fill in

Required: logo, name (3–32 chars), symbol (max 10), description — plus
use case, problem, and prototype link for ideas.

Optional: **creator first buy** (defaults to 100 SKR to seed your own
position; clear to skip; not offered on every config), website, X, and —
for meme coins — a **cause funding mode** (see below).

Uploads pin **before** you sign and may become public permanently. No gas
is spent on upload.

## Cause funding mode (meme coins)

Pick where the coin's **40% project-or-cause share** goes. **Managed
fund** is the default and preselect. The other live options are a
**curated cause**, a **specific Giveth project**, and **decide later**.
Letting an **X or Reddit account** choose is deferred — those rows
appear in the picker once their config enables them. **DAO** is shown
as planned — it cannot be selected yet.

- **Managed fund** — the share goes to the SeekUplift-managed fund, spent
  at SeekUplift's discretion with every payout published. It is never a
  guaranteed donation to a specific cause.
- **Curated cause / Giveth project** — the share is earmarked for the
  cause basket or project you name.
- **Decide later** — you pick the destination from the Creator Dashboard
  within **90 days** of launch.
- **X / Reddit account** (deferred, not selectable yet) — the named
  account claims the choice with **Claim as @handle** (a fresh X
  verification, or the wallet's verified Reddit link) within **90
  days**, then picks the destination within **30 days**.
- Anything undecided at the deadline **falls back to the managed fund**.

The choice is **permanent once final** — it cannot be changed after it
lands. Review & launch restates your pick before you sign.

## Review and sign

**Review & launch** shows your entries. **Launch cost ≈0.013 SOL** is a
one-time rent deposit, not a trading fee. A **Launch fee** row appears
only if the config charges one.

After launch: share the mint, trading starts on the curve (the opening
fee depends on the tier — see [Fees](fees.md)), creator fees accrue to
**Account → Rewards**, and only the creator wallet can edit description,
image, and socials (on configs that grant it update authority).
