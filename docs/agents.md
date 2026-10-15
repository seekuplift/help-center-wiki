# AI agents

--8<-- "includes/test-banner.md"

**SeekUplift Launchpad** has a public skill your own AI agent can use to
find, buy, sell and launch coins for you, without the app.

## Connect your agent

Give your agent this address:

`https://skill.seekuplift.com/skill.md`

That file is the reference for everything the agent can do and how. It
changes as the service does, so this page does not repeat it.

!!! note "Not live yet"
    The skill address goes live with the public release. Its source is at
    [github.com/seekuplift/seekuplift-external-agent-skill](https://github.com/seekuplift/seekuplift-external-agent-skill),
    which is private until then.

## What stays with you

- **Your keys.** The service only builds transactions. Your agent signs
  them with your wallet. Never give a seed phrase to any service.
- **New coins.** Your agent asks you to confirm a coin's details before
  launching it, unless you have told it that it may launch without asking.
  It buys and sells on its own, so put any spending limits in your
  agent's instructions.
- **Creator fees.** Claim them in the app under **Account → Rewards →
  Claim**, with the wallet that paid for the launch. See
  [Creators](creators.md).

Transactions are irreversible, as in the app. Some actions are
unavailable in some regions, and the agent rules can be stricter than the
app's. Your agent tells you which jurisdiction it detected when it is
refused.
