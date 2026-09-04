# Wallets

--8<-- "includes/test-banner.md"

Seek Uplift never holds your keys. A Solana wallet you already use signs
connections and transactions. The app talks to that wallet; it cannot move
funds unless you approve a prompt.

## Which wallet

Any compatible Solana wallet can connect.

- **Android:** Mobile Wallet Adapter. If several wallets are installed, the
  in-app **Select a wallet** sheet lists human names only. The built-in Seeker
  wallet is labeled **Seeker Wallet**. Other wallets keep their OS application
  name.
- **Web:** wallet-standard browser wallets.

If you do not have a wallet yet, disconnected screens recommend **Install
Jupiter Wallet** (Play Store / Chrome extension). That is a recommendation, not
a requirement.

## Connect

1. Open **Account**, or tap a gated action (Buy, Launch, Claim, Follow, Report).
2. Approve the connection in your wallet.
3. The connected address appears on Account and on the trade sheet.

The app does **not** fire a signature prompt just because a screen opened.
Signing always starts from a tap you made.

## Connect vs. sign in

Some actions need a **signed-in session** on top of a connection (community
posting, follows, creator dashboard, some reports). That is a short “sign a
message” prompt — it is **not** a transaction and it does not move funds.

If you see **Your session has expired**, tap the action again to sign a fresh
message. The app will not auto-fire that signature.

## Switch wallet

On the Buy / Sell sheet, the connected address is shown under the balance, with
**Switch wallet**. That re-authorizes the current wallet app so you can pick a
different account there.

On Account, **Disconnect wallet** is the way to drop the session entirely.
Disconnect is a ghost button, not a destructive red control. You can:

- **Disconnect only** — leave local records on the device.
- **Disconnect and clear local data** — also wipe wallet-linked local records
  on this device.

After an explicit disconnect, the next connect can choose a wallet again.

## What a wallet prompt is asking

Read it. Typical prompts:

| Prompt | Moves funds? |
|---|---|
| Connect / authorize the app | No |
| Sign in (message) | No |
| Buy / sell / launch / claim / a quote-token swap | **Yes** — review amounts |

Cancel or reject a transaction prompt: **no funds move**. If a stale approval
is still sitting in the wallet, close it before you retry.

If the wallet **never shows** an approval screen and the app says the wallet
didn’t ask you to approve, reconnect and try again. Nothing was signed.

## Android specifics

- The app remembers the wallet you successfully connected and routes later
  prompts to that package.
- Account’s “view full balance” link opens the **connected wallet app** when
  it can; otherwise it opens Solscan for the address.
- Process-kill mid-sign: on relaunch the app checks what landed. Success is
  updated balances, not a recovery popup.

## Web specifics

- A connected session should survive a full page reload without forcing you
  through the picker again.
- Sign-in (the signed message) may need to be repeated after reload for
  session-gated features. Connection itself should persist.

## Never share these

Seek Uplift will **never** ask for:

- Seed phrase / recovery phrase
- Private keys
- Wallet password or biometrics bypass

Those stay in your wallet app. If a site, chat, or “support agent” asks for
them, it is not Seek Uplift. See [Privacy and safety](privacy.md).
