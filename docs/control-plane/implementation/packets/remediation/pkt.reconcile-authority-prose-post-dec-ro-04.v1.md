# pkt.reconcile-authority-prose-post-dec-ro-04.v1

- **Packet ID**: `pkt.reconcile-authority-prose-post-dec-ro-04.v1`
- **Authority**: DEC-RO-04 recorded at `canon-knowledgebase/post-reopen-decisions/condition-e-license.md`
- **Carry-forward**: CF-0095 (extends)
- **Scope**: `SaintFreddy/Canon` workspace-level authority files (AGENTIC_WORKFLOW.md + CANON_PLAN_IMPACT_REPORT.md)
- **Ordering**: After `pkt.add-proprietary-license.v1` (Canon side) has merged. The LICENSE file must exist before prose that references "our LICENSE" makes sense.
- **Execution mode**: **Semi-autonomous** — droid drafts the exact edits, opens a PR, but flags this as a special-case authority edit in the PR body so a human can confirm before auto-merge.

## Why this is a separate packet

The LICENSE packet's executing droid was appropriately conservative and did NOT touch `AGENTIC_WORKFLOW.md` or `CANON_PLAN_IMPACT_REPORT.md` because those are marked read-only in `canon-now.md`. DEC-RO-04's decision record explicitly authorizes two narrow edits to those files, but "explicit decision-record authorization" is rare enough that it warrants its own packet rather than being rolled into the broader LICENSE packet.

## Goal

Execute the two narrow, decision-authorized edits to authority-adjacent prose so documented posture matches DEC-RO-04 reality:

1. **AGENTIC_WORKFLOW.md §9 L426** — the "public SDK posture" phrasing. Two variants; executor picks based on context and documents choice in PR body:
   - **Variant A (preferred)**: Mark the phrase as aspirational / not current. Example patch:
     > Before: `Canon aims for public SDK posture with community-friendly tooling.`
     > After: `Canon aims for public SDK posture with community-friendly tooling *[aspirational only; not current license posture. DEC-RO-04 (2026-04-24) set current LICENSE to Proprietary / All Rights Reserved; see `canon-knowledgebase/post-reopen-decisions/condition-e-license.md` for revisit conditions.]*`
   - **Variant B (fallback)**: Remove the phrasing entirely if Variant A breaks §9's flow.

2. **CANON_PLAN_IMPACT_REPORT.md §6 row 6** — append a single new row (not modify existing rows) in the §6 decision ledger noting DEC-RO-04 landed on Option 4. Exact append format:
   > `| e.2 | LICENSE choice | 2026-04-24 | SaintFreddy | Option 4 — Proprietary / All Rights Reserved | DEC-RO-04 | See canon-knowledgebase/post-reopen-decisions/condition-e-license.md |`
   Adjust column format to match the existing table header in §6.

## File whitelist

- `AGENTIC_WORKFLOW.md` (modify §9 only; do NOT touch other sections)
- `CANON_PLAN_IMPACT_REPORT.md` (append one row to §6 only; do NOT modify existing rows or sections)

Do NOT modify:
- `canon-now.md`
- `AGENTIC_ENGINE_AUDIT_LOG.md`
- Any other file — these 2 edits are narrow exceptions; everything else is out of scope.

## Forbidden

- Do NOT rewrite or rephrase any existing prose in §9 or §6 beyond the specific markup addition / row append described above.
- Do NOT treat this packet as authorization to make other authority-record edits. Each such edit requires its own decision record + its own packet.
- Do NOT touch §1-§8 or §10+ of AGENTIC_WORKFLOW.md. Only §9 L426 area is authorized.

## Verification

- `git diff AGENTIC_WORKFLOW.md` shows ONE additive change in the §9 area (aspirational markup) OR one small deletion (Variant B).
- `git diff CANON_PLAN_IMPACT_REPORT.md` shows exactly ONE new row appended to §6, no other changes.
- PR body quotes the exact before/after for each change so reviewer can verify the narrow scope.

## PR labelling

PR title must start with: `chore(authority-edit):` — this signals to human reviewers that this is an authorized exception to the usual read-only rule.

## Human-merge preference

Despite auto-merge being enabled elsewhere, this PR should NOT auto-merge by admin squash unless a human approves, because the edits touch authority-adjacent files. The PR body should explicitly note: "Human review preferred before merge."
