# Creators

--8<-- "includes/test-banner.md"

If you launched a coin, two Account rows matter: **Rewards** (claim trading
fees) and **Edit your tokens** (metadata, community, drafts).

Only the **wallet that launched the pool** can claim and edit. Keep that wallet.
Name and symbol cannot be changed later.

## Claim creator fees

**Account → Rewards** lists pools you created.

- **CLAIMABLE NOW** is what you can claim today.
- Per-pool **Claim**, plus **Claim all** when at least one pool has a balance.
- Zero-claimable rows show the amount only — no disabled button.
- If claimable or lifetime totals span more than one quote token, each token
  is on its own line.

Claiming is an on-chain transaction. Approve it in your wallet. Success shows
the pool (or pool count) and a Solscan link.

This is your **0.20% of traded volume** (16% of the 1.25% bonding-curve fee).
It is **not** Directed’s 0.525%. Directed funds accumulate in treasury (Phase
A) and are not a claim button. See [Fees](fees.md).

**Earn more** offers **Launch a coin** — ideas are coins, there is no separate
“submit an idea” path.

## Edit coin details

**Account → Edit your tokens** (screen title: Creator dashboard).

1. Connect the creator wallet and sign in (message prompt — no funds move).
2. Pick the coin if you have more than one.
3. Edit description, image, website, X, Telegram, and (for ideas) prototype.

Save uploads the new image/metadata, then asks for a **wallet signature**, then
syncs the backend cache. Until that signature, nothing on-chain changes.

- Clearing a link and saving removes it.
- You cannot edit another creator’s coin; those fields stay locked.
- After save, the feed can take a moment to catch up.

## Follower themes and drafts

On the same dashboard, when people follow your coin and say why, you see
**aggregated, anonymized interest themes** — not anyone’s verbatim note.

You can draft an update addressed to a theme and submit it for review.
Moderation checks safety **and** relevance. Approved drafts can reach matching
followers as personalized Progress items and, if they opted in, a push.

Broadcast access can wait until the coin has enough followers (so early
followers stay anonymous) and enough trading activity to cover moderation.
If the panel is empty, that is often why — not a bug.

Public holder posts on the token’s Community tab are separate: they do not
send pushes. See [Communities](communities.md).

## Directed funds (honest status)

Directed’s 0.525% of volume is held for the project (idea) or the causes a
meme backs. **Today, that share is swept and tracked manually by the team** —
not by an on-chain program. Automatic, trustless on-chain distribution is the
goal we're building toward, not something live yet. Milestone / cause spend is
not live. We do not call those funds locked.

When automatic on-chain distribution ships, it will be documented here and on
[Fees](fees.md). Until then, do not promise supporters that a treasury spend
already happens.
