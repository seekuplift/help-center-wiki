# Tickets: Cause funding modes — help-center copy

Status: implemented 2026-10-01 (commit `22f6bab`; tbd/x/reddit availability corrected in
`69dafbf`). The source spec was human-reviewed and approved 2026-09-28. 1 ticket, done.

Source spec: `../docs/superpowers/specs/2026-09-28-cause-funding-modes-design.md`
(workspace-local). App half: `../redesign/launchpad-mobile-redesign/specs/tickets-cause-funding.md`.

**Non-negotiables:**
- **Match what ships.** Copy lands with or after CF-APP-1, never before, and describes only the
  modes the app actually offers.
- **Honest copy.** The managed fund is spent at SeekUplift's discretion, and every payout is
  published. It is never presented as a guaranteed donation. DAO is "planned", with no date.
  Distribution stays "manual for now" until the router era.
- **Idea funding is separate.** The ideacoin funding modes have their own wiki ticket (not filed
  yet). This ticket doesn't describe them, and never presents a cause as an idea coin's
  destination.

## CF-WIKI-1: Document cause funding modes and the managed fund

**What to build:** update the help center for meme and startup coins:
- `docs/launching.md`: the donation list at launch becomes the mode list. Managed fund is the
  default, alongside curated cause, specific Giveth project, decide later, let an X or Reddit
  account choose, and DAO (planned).
- `docs/creators.md`, "Project-or-cause funds": deciding later from the Creator Dashboard, the
  90-day deadline, and the fallback to the managed fund.
- `docs/fees.md`: what happens to the 40% share in each mode, and a link to the fund page.
- `docs/faq.md`: "What is the managed fund?", "Why is the DAO option not available?" and "Can I
  change my choice?" (no, once it's final).

**Blocked by:** app CF-APP-1 (and CF-APP-3 for the fund-page link).

- [x] Every mode named in the copy exists in the app build it describes.
- [x] The DAO wording matches the app's explainer: planned, no date, and dependent on safeguards
      that make sure the funds can only reach causes.
- [x] Idea-coin pages are unchanged by this ticket.
- [x] `mkdocs build --strict` passes.

[2026-10-01: implemented. `docs/launching.md` gained the cause funding mode section (managed default, cause, project, decide later, X/Reddit, DAO planned, permanence + deadline fallback); `docs/creators.md` covers the dashboard pick, 90-day deadline, claim flow and fallback; `docs/fees.md` covers the 40% share per mode with the Fund page link; `docs/faq.md` gained the cause funding section. Verified `mkdocs build --strict` (via `uv run`, mkdocs-material) — clean.]
