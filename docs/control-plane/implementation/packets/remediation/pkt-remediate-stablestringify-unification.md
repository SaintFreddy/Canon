# Remediation packet — stableStringify unification
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-stablestringify-unification.v1
Prerequisite condition: (d) stableStringify unification into @canon/engine-core
Target repo: `agentic-engine`

This packet is a scaffold. Not authorized for execution until the plan-owner records a decision for condition (d) in `canon-knowledgebase/post-reopen-decisions/condition-d.md`.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-stablestringify-unification.v1",
  "title": "Unify stableStringify into @canon/engine-core and purge divergent copies",
  "task_id": "P4p.step20.remediation.d",
  "objective": "Eliminate stableStringify divergence across packages by making @canon/engine-core the single source, re-exporting from a stable path, and removing or delegating every duplicate implementation.",
  "scope": [
    "Canonicalize stableStringify in @canon/engine-core (or packages/core/src/stable-stringify.ts) with well-defined sort order, number/boolean/null handling, and NaN/Infinity rejection.",
    "Replace every divergent copy in other packages with an import from the canonical location.",
    "Add packages/core/src/__tests__/stable-stringify.cross-package.test.ts asserting every prior caller produces byte-identical output for a fixture set."
  ],
  "out_of_scope": [
    "Changing the canonical hash function or digest semantics (that is a separate PROV decision).",
    "Rewriting provenance/manifest formats.",
    "Canon/ quarantined draft state."
  ],
  "source_authority_refs": [
    "canon-now.md condition (d)",
    "canon-knowledgebase/post-reopen-decisions/condition-d.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6",
    "AGENTIC_ENGINE_AUDIT_LOG.md findings related to stableStringify divergence"
  ],
  "file_whitelist_ref": "wl.remediate-stablestringify-unification.v1",
  "deliverables": [
    "packages/core/src/stable-stringify.ts (canonical).",
    "Every other package's stableStringify replaced with a re-export or direct import.",
    "Cross-package byte-identity regression test.",
    "contracts/exports.json updated.",
    "Draft carry-forward entry."
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.byte-identity.cross-package" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "approval_requirements": [
    "Plan-owner acceptance of condition (d) recorded before execution starts.",
    "Human review of the resulting PR before merge."
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high",
  "carry_forward_topics": [
    "stableStringify canonical rules (sort / NaN / undefined / bigint)",
    "import path migration list",
    "byte-identity regression coverage"
  ]
}
```

## File whitelist `wl.remediate-stablestringify-unification.v1`

- `packages/core/src/stable-stringify.ts` (new or promoted)
- All other `packages/*/src/**/*.ts` files that currently contain a local stableStringify (will be listed explicitly at planning time by grepping for the symbol)
- `packages/core/src/__tests__/stable-stringify.cross-package.test.ts`
- `contracts/exports.json`

## Completion signal

- `grep -rE 'function +stableStringify|const +stableStringify' packages/` returns exactly one non-test match (in the canonical location).
- Cross-package byte-identity test passes.
- `pnpm typecheck` + `pnpm test` green.
