# Launch a coin

--8<-- "includes/test-banner.md"

The **Launch** tab plants a coin on Meteora’s Dynamic Bonding Curve on Solana
mainnet. The mint is permanent. Review every field and every wallet prompt
before you sign.

Seek Uplift does not validate that a project is real, legal, or a good idea.
Creator-supplied notes are not legal, tax, investment, or securities advice.

## What you can launch

The wizard asks **What are you envisioning?**

| Type | For | Directed fees (Phase A) |
|---|---|---|
| **An idea** | A project worth uplifting | Held for the project; intended path is release as milestones are met |
| **A meme with impact** | A meme that backs exceptional causes | Held for those causes |

Both share the same bonding-curve split of traded volume: **Creator 0.20% ·
Directed 0.525% · SeekUplift 0.525%**. Caption: **of traded volume**, from the
**1.25%** bonding-curve fee. Full table: [Fees](fees.md).

Tap a card to select it, then **Continue**. **Review fees** on that step opens
the Fees page.

Startup create is **not offered** in the default Launch wizard. You can still
browse existing Startup tokens on Home.

## Drafts

Your draft is saved **on this device** (not on a server). You can leave and
finish later. A one-liner above Review launch reminds you of that.

Back (header, swipe, or hardware Back) steps through the wizard instead of
dumping you out of the app. While upload or deploy is in flight, Back is
ignored so a swipe cannot kill the process.

## What to fill in

Required fields come first, then optional, for every type.

**Idea — required**

- Logo (PNG/JPG, about 512×512)
- Name (3–32 characters)
- Symbol (max 10)
- Description
- Use case (pick 1–3)
- Problem you solve
- Prototype link

**Meme — required**

- Logo, name, symbol, description (meme does not collect idea/startup project
  fields)

Then **CREATOR FIRST BUY** (optional, but highlighted). Fresh forms default to
**100 SKR** so the pool is not launched empty. Clear the amount to skip.

- Live `≈ $…` conversion while you type
- Live `≈ N tokens · P% of supply` estimate
- Amounts that would push past graduation are rejected — a first buy that
  large would fail on-chain

**Optional** after that: website, X, and (for ideas) roadmap/whitepaper,
Discord.

!!! warning "Uploads become public"
    Logo and metadata are pinned **before** you sign the launch transaction.
    No gas is spent on upload, but image and metadata may become public,
    copied, cached, and difficult or impossible to erase. Do not upload
    private personal content, images of minors, or anything you cannot make
    public.

## Review, upload, sign

**Review & launch** shows what you typed — description, use case, problem,
links — not plumbing. Links that are valid `https` URLs are tappable for a
preview.

- **Launch cost ≈0.013 SOL** — a one-time rent deposit for mint/pool/vault
  accounts, not a 1.25% trading fee.
- A **Launch fee** row appears only if the config charges one.
- After launch, **only the creator wallet** can edit description, image, and
  socials from Edit your tokens. Name and symbol cannot be changed. Lose that
  wallet and those edits are gone.

Flow:

1. Confirm the upload warning.
2. Logo and metadata pin through the Seek Uplift backend (the app never holds
   storage credentials).
3. Sign the launch in your wallet.
4. On success you land on the new token page with the mint address.

If **upload fails**, nothing was signed and no gas was spent. Retry.

If you kill the app after signing on Android, reopen it and check the token
page / Solscan — the launch may already be live.

## After you launch

- Share the mint. Indexing can lag a few moments; identity still renders from
  the launch route.
- Trading starts on the curve. The opening fee is **not** 1.25% — see
  [Fees](fees.md).
- Claim creator fees later from **Account → Rewards**. Directed funds
  accumulate (Phase A) and are **not** the same as your claimable 0.20%.
- Edit metadata from **Account → Edit your tokens**.

Next: [Graduation](graduation.md) · [Creators](creators.md)
