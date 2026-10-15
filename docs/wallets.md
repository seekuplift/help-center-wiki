# Wallets

--8<-- "includes/test-banner.md"

Seek Uplift never holds your keys. Your Solana wallet signs connections
and transactions; the app cannot move funds without your approval.
The one exception is the optional **instant wallet** (below), a separate
wallet run by magic.link that signs trades without a prompt.

## Connect

**Account → Connect wallet** (or take a gated action like Buy) and
approve in the wallet. On Android, pick from **Select a wallet** (the
built-in Seeker wallet is **Seeker Wallet**); on web, use a
wallet-standard browser wallet. No wallet yet? Screens recommend
**Jupiter Wallet** — a suggestion, not a requirement.

Some actions (posting, follows, token reports, creator dashboard) also need a
**sign-in**: a message signature that moves no funds. If the session
expired, tap the action again.

## Switch and disconnect

On the trade sheet, **Switch wallet** re-authorizes the wallet app so you
can pick another account. **Instant wallet** (offered once when you buy;
set it up later in **Account → Instant trading**) is a separate in-app
wallet, run by magic.link, that trades launchpad coins without per-trade
approvals. Setup is a one-time, non-refundable **10 SKR** fee plus an email
code. You fund it from your external wallet (currently up to 1 SOL and
1,000,000 SKR), it pays its own SOL trade fees, and you can **Withdraw**
everything back at any time. Unlinking or replacing it asks your external
wallet to sign. On Account, **Disconnect wallet** drops the session,
optionally clearing local wallet-linked data too.

## Prompts

| Prompt | Moves funds? |
|---|---|
| Connect / Sign in | No |
| Buy / sell / launch / claim / SKR swap | **Yes** — review amounts |

Reject a prompt and nothing moves. If the wallet never shows an approval,
reconnect and retry.

Seek Uplift will **never** ask for your seed phrase, private keys, or
wallet password. See [Privacy and safety](privacy.md).
