---
name: post-reopen-remediation
description: Execute a bounded post-reopen remediation packet against agentic-engine under the Phase 4+ audit-reopen hold. Use when a task references one of the `pkt.remediate-*` packets and the prerequisite plan-owner decision is recorded. Stops hard if baton state is still `stop` for that condition.
---

# Post-reopen remediation packet execution

## Required inputs

- selected remediation packet ID (one of `pkt.remediate-*.v1`)
- confirmation that the prerequisite reopen-condition decision is recorded durably
- packet file path under `docs/control-plane/implementation/packets/remediation/`

## Gating rules (read first)

1. Read `canon-now.md` at the workspace root.
2. If `Baton state` is `stop — audit-reopen hold` AND the packet's `prerequisite_condition` is NOT listed in the recorded plan-owner decisions, stop and report: "Remediation packet `<id>` gated by undecided reopen condition `<x>`; cannot proceed."
3. If the packet's prerequisite decision is recorded, the baton is authorized for that specific bounded step only. Do not chain into unrelated remediation packets within the same run.

## Instructions

1. Read `/AGENTS.md`, `/Canon/AGENTS.md`, and the nearest descendant `AGENTS.md` files for the touched paths (typically `agentic-engine/`).
2. Read the governing accepted artifacts named by the packet brief:
   - the relevant cited findings in `AGENTIC_ENGINE_AUDIT_LOG.md`
   - the governing rows in `CANON_PLAN_IMPACT_REPORT.md`
   - the recorded plan-owner decision for this packet's condition
3. Treat the packet brief's `file_whitelist_ref` as the execution boundary. Do not edit files outside the whitelist.
4. Stay inside `agentic-engine/` unless the packet explicitly whitelists `Canon/` control-plane files.
5. Use accepted artifacts by default; draft/stale artifacts are not execution authority.
6. Implement the fix as minimally as the decision allows. No scope widening for "while we're here" improvements.
7. Add or update deterministic-replay regression tests where the packet requires them.
8. Run the repo's real validators: `corepack pnpm typecheck && corepack pnpm test`. Both must be green before you claim completion.
9. Prepare a carry-forward entry describing the packet, the decision it implements, the files changed, and the remaining follow-on steps; do not self-accept.
10. Do NOT edit `canon-now.md` or `canon-knowledgebase/canon-phase-4-plus-plan.md`. Those are human-owned authority records.

## Verification

- No `Date.now()`, `new Date()`, `performance.now()`, or `localeCompare` calls outside the symbols the decision explicitly permits.
- `contracts/exports.json` stays additive; no removed exports without a deprecation note.
- `pnpm typecheck` green.
- `pnpm test` green, including any new regression tests the packet required.
- If the packet changed any `@canon/*` package signature, the other packages in the workspace still build.

## Output

Return:

- restated objective (paraphrase the packet brief)
- recorded decision being implemented (quote the accepted option)
- files changed (full list)
- validator results (typecheck + test output summary)
- proposed next bounded step (for the next packet in the remediation queue)
- draft carry-forward entry (for human acceptance)

## Never do

- reopen accepted baseline decisions
- invent a "quick fix" that contradicts the recorded plan-owner decision
- cross-contaminate two remediation packets in one PR
- touch `Canon/packages/`, `Canon/services/`, or `Canon/workers/` quarantined draft state
- mark the packet complete before `pnpm typecheck` and `pnpm test` pass
- append to `AGENTIC_ENGINE_AUDIT_LOG.md` or edit `CANON_PLAN_IMPACT_REPORT.md`
- use `--auto high` or `--skip-permissions-unsafe`
