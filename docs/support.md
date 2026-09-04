# Getting help

--8<-- "includes/test-banner.md"

Three in-app doors, from the help icon on every screen:

| Row | Use it when |
|---|---|
| **Guides & FAQ** | You want to understand how something works (this wiki). |
| **Report a bug** | Something in the app broke, looks wrong, or crashed. |
| **Contact support** | You need a human on your account, a transaction, or a policy issue. |

Account also has **Support**. Same destination as Contact support.

This wiki is a **public test**. If a page is wrong or missing, prefer
**Report a bug** or **Contact support** over treating the wiki as law.

## Report a bug

You do not need to be signed in.

1. Tap help on the screen where it broke (that is the screenshot we capture).
2. Choose **Report a bug**.
3. Describe what went wrong (required, up to 4,000 characters).
4. Optionally add an email for follow-up, and extra photos.
5. Expand **We'll include background info.** if you want the exact list.
6. Remove the screenshot if you do not want it sent (balances can be visible).
7. **Send report**.

On the **web** build there is no automatic screenshot; notes and details still
go through. You can attach photos on Android when the picker is available.

You should get a confirmation, or an error that keeps your notes so you can
retry. If images are too large, the report can still land **without** them —
the success copy will say so.

To keep the public write path healthy, reports are rate-limited (currently
**5 per hour** per IP).

### What a bug report includes

Along with your notes (and email if you added one):

- App version, build, platform, OS, device, language
- The screen you were on
- A random install id (not a push token)
- Whether a wallet is connected, and the address if you are signed in
- Live stream health
- Backend URL and Solana cluster
- Feature flags in effect
- Recent diagnostic events (secrets already redacted)
- Timestamp
- Optional screenshot (Android) and extra images you attached

The Privacy Center has a **Bug reports** section that matches this list. Email,
when provided, is stored on the backend for follow-up (default 90 days) and is
**not** copied into a public issue.

Do **not** put seed phrases, private keys, or passwords in notes or screenshots.

## Contact support

Opens the existing support surface:

- **Ticket** intake when live chat is off (the usual default).
- **Live chat** when that channel is enabled.

Support chat is provided by a third-party vendor. If you continue, they may
receive your IP, device metadata, and the messages you send. Their privacy
policy is linked in-app.

**Never** paste a seed phrase, private key, or password into support.

If in-app chat cannot load, use **Open chat in browser** / **Open in browser**.

## This wiki

On Android the wiki opens inside the app. In-wiki links stay in the viewer;
links that leave this site open in the system browser. Header Back leaves
the wiki and returns to the app — it does not walk previous wiki pages.

On the web, Guides & FAQ opens a **new browser tab**.

If the viewer fails, **Open in browser** loads the same URL.

## Security issues

Do not file a security vulnerability as a normal bug report or a public
support ticket.

Open **Account → Security Policy** and follow that document. Seek Uplift will
never ask for your seed phrase as part of a “verification.”
