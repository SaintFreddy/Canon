# Remediation packet — Replay-compare id-aligned diff variant
Version: 1.0
Status: Authorized
Task: Phase 4+ step 20 — post-reopen remediation wave D
Artifact ID: pkt.remediate-replay-compare-diff-semantics.v1
Prerequisite condition: (h) replay-compare diff-semantics
Target repo: `agentic-engine`

Plan-owner decision recorded at `canon-knowledgebase/post-reopen-decisions/condition-h.md`.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-replay-compare-diff-semantics.v1",
  "title": "Add id-aligned diff variant to replay-compare; document positional diff as historical",
  "task_id": "P4p.step20.remediation.h",
  "objective": "Ship diffByStableId() as the production replay-compare path while preserving the positional-index diff with a clear JSDoc warning.",
  "scope": [
    "Add workers/replay-compare/src/diff-by-stable-id.ts (or equivalent) implementing id-aligned diff.",
    "Update workers/replay-compare/src/diff.ts JSDoc with the warning about positional-index semantics.",
    "Update contracts/exports.json to export diffByStableId additively.",
    "Add workers/replay-compare/src/__tests__/diff-by-stable-id.test.ts covering add/remove/modify/reorder.",
    "Leave positional diff tests as-is."
  ],
  "out_of_scope": [
    "Deleting positional diff (Option B was not accepted).",
    "Migrating every caller to id-aligned (that is a separate downstream packet).",
    "Changing the diff output schema beyond adding the new entry point."
  ],
  "source_authority_refs": [
    "canon-now.md condition (h)",
    "canon-knowledgebase/post-reopen-decisions/condition-h.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6 row 9",
    "AGENTIC_ENGINE_AUDIT_LOG.md WRK-RC-002"
  ],
  "file_whitelist_ref": "wl.remediate-replay-compare-diff-semantics.v1",
  "deliverables": [
    "New diff-by-stable-id module",
    "Updated positional diff JSDoc",
    "contracts/exports.json additions",
    "New regression test suite",
    "Draft carry-forward entry"
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## File whitelist `wl.remediate-replay-compare-diff-semantics.v1`

- `workers/replay-compare/src/diff-by-stable-id.ts` (new)
- `workers/replay-compare/src/diff.ts`
- `workers/replay-compare/src/__tests__/diff-by-stable-id.test.ts` (new)
- `workers/replay-compare/src/index.ts`
- `contracts/exports.json`

## Completion signal

- `diffByStableId()` available on public exports.
- Regression test matrix covers add/remove/modify/reorder with stable ids.
- Positional diff JSDoc contains the warning.
- `pnpm typecheck` + `pnpm test` green.
