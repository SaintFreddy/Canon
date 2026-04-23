# Remediation packet — thaw timestamp authority
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-thaw-timestamp-authority.v1
Prerequisite condition: (a) Clock decision
Target repo: `agentic-engine`

Scaffold only. Execution requires `pkt.remediate-clock-timeprovider.v1` landed.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-thaw-timestamp-authority.v1",
  "title": "Remove synthetic thaw timestamps and source from injected Clock",
  "task_id": "P4p.step20.remediation.thaw",
  "objective": "Eliminate synthetic thaw timestamps in context-compiler / replay paths. The thaw operation must either carry the original frozen timestamp forward, or source a new timestamp from the injected Clock with explicit semantic labeling.",
  "scope": [
    "Identify every site that currently fabricates a thaw timestamp (snapshot-freezer, replay, compiler-pipeline).",
    "Replace synthetic values with either: (a) pass-through of the frozen document's timestamp, or (b) an injected-clock read with an explicit field name (e.g., thawedAt) distinct from frozenAt.",
    "Add a test asserting thawedAt != frozenAt in production Clock but thawedAt == the clock's controlled value in DeterministicClock."
  ],
  "out_of_scope": [
    "Changing the replay protocol contract.",
    "Modifying frozenAt hash inclusion (separate packet)."
  ],
  "source_authority_refs": [
    "canon-now.md condition (a)",
    "canon-knowledgebase/post-reopen-decisions/condition-a.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6",
    "AGENTIC_ENGINE_AUDIT_LOG.md synthetic-thaw findings"
  ],
  "file_whitelist_ref": "wl.remediate-thaw-timestamp-authority.v1",
  "deliverables": [
    "Updated compiler-pipeline / snapshot-freezer thaw paths.",
    "Explicit thawedAt vs frozenAt naming.",
    "Regression test.",
    "Draft carry-forward entry."
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

## File whitelist `wl.remediate-thaw-timestamp-authority.v1`

- `packages/context-compiler/src/compiler-pipeline.ts`
- `packages/context-compiler/src/snapshot-freezer.ts`
- `packages/context-compiler/src/__tests__/*.test.ts`
- Any package with a `thaw` verb (enumerate at planning time)

## Completion signal

- No `new Date()` inside thaw code paths.
- thawedAt and frozenAt never share the same field.
- Deterministic-replay regression covers thaw.
- `pnpm typecheck` + `pnpm test` green.
