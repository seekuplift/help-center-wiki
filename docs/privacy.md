# Privacy and safety

--8<-- "includes/test-banner.md"

The in-app **Privacy Center**, **Legal**, and **Security Policy** (all on
Account) are the documents of record for a given app version. This page is a
plain-language map. If they disagree, those screens win — and this wiki is
still a test.

## First launch

The app does not mount Home, tabs, wallet, analytics, uploads, reports, or
support chat until you accept the current **Privacy Policy and Terms** on the
welcome sheet. Closing that sheet without accepting leaves you on welcome.

A policy or terms version bump can ask you to review again. The local
acceptance record (version + time) is visible on **Legal**. There is no in-app
“reset acceptance” button; clearing app storage on the device is what drops
the record.

## What the app may process

When you use the corresponding feature:

- Wallet connection state and, when you take a wallet action, your public
  address
- Token balances and transaction signatures
- Launch form content, images, and metadata
- Token reports and community-post reports
- Bug reports (see [Getting help](support.md))
- Support messages
- Diagnostics and, if you allow it, analytics events

Analytics is **off** until you accept privacy. After that you can turn it off
in Privacy Center. The app must not send raw wallet addresses to analytics.

## Reports

Token and post reports are **wallet-attributed**. We store the mint (or post),
category, optional comment, and connected wallet for abuse prevention
(rate limits, reporter blocks). Reporter wallet is the signed-in session, not
a typed identity.

Do not put private or sensitive personal data in comments. Report records may
be retained for up to 24 months, with legal-hold exceptions. An erasure
request does not always lift an active abuse block.

## Uploads and the chain

Images and metadata go through the Seek Uplift backend (no client-side storage
keys). Once pinned and once a transaction is on Solana, copies can be public,
cached, and hard to erase. Treat anything you upload or sign as potentially
permanent.

## Privacy Center actions

From **Account → Privacy Center** you can typically:

- Read the privacy policy
- Change analytics / “do not sell or share” style choices
- Export or copy a package of **this wallet’s** local data (no secrets)
- Clear diagnostics
- Delete wallet-linked local data
- Request backend deletion

Those actions do what they say — check the result, not only a toast. Use
them carefully; some are destructive.

Bug-report collection is summarized in its own Privacy Center section, with a
link to the full policy.

## Safety rules we will not break

- **We never ask for your seed phrase or private keys.** Not in the app, not
  in support, not by email. Anyone who does is not Seek Uplift.
- **No signature on screen open.** You tap Buy, Launch, Claim, Sign in, etc.
- **Not financial advice.** Token pages, callout scores, labels, and “safety”
  signals are informational.
- **Mainnet only.** There is no user-facing Devnet switch.
- **External links** that the app did not validate (for example a website from
  token metadata) ask you to confirm the host before leaving. Callout source
  posts hand off to the OS / X app.

## Legal and security

| Screen | What it is |
|---|---|
| **Privacy Center** | Privacy policy, toggles, your data. Not terms. |
| **Legal** | Terms & Conditions and the local acceptance record. |
| **Security Policy** | Vulnerability reporting and which on-chain programs the app transacts against. Not legal terms. |

Use Security Policy for product/security vulnerabilities. Use Report a bug for
product defects. Use Contact support for account and policy questions.

California residents: privacy rights (know, delete, correct, opt out of sale
or sharing) are described in the in-app policy. Start from Privacy Center or
Contact support.
