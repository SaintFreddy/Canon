# Remediation packet — frozenAt placement
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-frozenat-in-hashed-doc.v1
Prerequisite conditions: depends on (a) Clock decision + a coupled PROV decision on frozenAt hash inclusion
Target repo: `agentic-engine`

This packet is a scaffold. Execution requires BOTH:
1. Condition (a) decided and `pkt.remediate-clock-timeprovider.v1` landed.
2. An explicit plan-owner decision that `frozenAt` belongs inside the hashed compiled-context document (recorded in `canon-knowledgebase/post-reopen-decisions/frozenat-hash-inclusion.md`).

## Packet brief

```json
{
  "packet_id": "pkt.remediate-frozenat-in-hashed-doc.v1",
  "title": "Move frozenAt inside the hashed compiled-context document",
  "task_id": "P4p.step20.remediation.frozenat",
  "objective": "Include frozenAt (sourced from the injected Clock) in the hashed compiled-context document so frozen contexts replay byte-identically and downstream audit replay becomes possible.",
  "scope": [
    "Modify packages/core/src/compiled-context.ts so frozenAt is a hashed field, sourced from the injected clock.",
    "Update packages/context-compiler snapshot-freezer to assert frozenAt is present before hashing.",
    "Add a regression test proving two freezes with the same DeterministicClock produce identical digests.",
    "Update provenance emitters if they currently read frozenAt from outside the hash."
  ],
  "out_of_scope": [
    "Changing the hash function itself.",
    "Redesigning provenance envelope shape beyond the frozenAt field.",
    "Clock seam introduction (pre-requisite packet handles that)."
  ],
  "source_authority_refs": [
    "canon-now.md condition (a)",
    "canon-knowledgebase/post-reopen-decisions/condition-a.md",
    "canon-knowledgebase/post-reopen-decisions/frozenat-hash-inclusion.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6",
    "AGENTIC_ENGINE_AUDIT_LOG.md PROV-002, PROV-004, PKG-CC-003"
  ],
  "file_whitelist_ref": "wl.remediate-frozenat-in-hashed-doc.v1",
  "deliverables": [
    "Updated compiled-context.ts (hash inclusion of frozenAt).",
    "Updated snapshot-freezer.ts pre-hash assertion.",
    "Deterministic-replay regression test.",
    "Provenance emitter fix if currently reading frozenAt outside the hash.",
    "Draft carry-forward entry."
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.deterministic-replay.regression" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high",
  "carry_forward_topics": [
    "hash inclusion rules",
    "snapshot-freezer assertions",
    "provenance reader migration"
  ]
}
```

## File whitelist `wl.remediate-frozenat-in-hashed-doc.v1`

- `packages/core/src/compiled-context.ts`
- `packages/context-compiler/src/snapshot-freezer.ts`
- `packages/provenance/src/**/*.ts` (only files that currently read frozenAt; enumerate at planning time)
- `packages/core/src/__tests__/compiled-context.deterministic-replay.test.ts`
- `packages/context-compiler/src/__tests__/snapshot-freezer.deterministic.test.ts`

## Completion signal

- Two back-to-back freezes with identical DeterministicClock produce byte-identical digests.
- Existing compiled-context fixtures updated without breaking consumers.
- `pnpm typecheck` + `pnpm test` green.
