# Phase 6 R4 artifact workspace surface and validation packet
Version: 1.0
Status: Accepted
Task: P6.6 — Agent execution packets
Artifact ID: pkt.phase6-r4-artifact-workspace-surface-validation-packet.v1
Packet scope: Bounded `transform` packet for implementing release-local app surfaces, projection grammar, inspect helpers, contract tests, and fixture assets inside one release slice.
File whitelist ref: wl.phase6-r4-artifact-workspace-surface-validation.v1

This packet is accepted for downstream use.
It delegates one bounded surface-validation slice of the accepted R4 artifact workspace implementation blueprint.
It does not authorize writes outside the named whitelist or the selected budget band.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-r4-artifact-workspace-surface-validation-packet.v1",
  "title": "Phase 6 R4 artifact workspace surface and validation packet",
  "task_id": "P6.6",
  "objective": "Implement the R4 artifact workspace app, projection, inspect, test, and fixture slice from the accepted release blueprint inside bounded surface-validation scope.",
  "scope": [
    "Implement only the R4 artifact workspace app, projection-grammar, inspect, test, and fixture clusters named in the whitelist.",
    "Keep all surface work projection-only over accepted shared objects and contracts."
  ],
  "out_of_scope": [
    "Scope widening beyond the named file whitelist or selected budget band.",
    "Semantic changes to accepted release doctrine, repo/package architecture, or documentation-plane ownership.",
    "Package-contract or runtime execution work outside the named surface-validation clusters."
  ],
  "source_authority_refs": [
    "rel.r4-artifact-workspace-contract.v1"
  ],
  "accepted_artifact_refs": [
    "bp.phase6-r4-artifact-workspace-blueprint.v1",
    "cp.phase6-release-blueprint-index-data.v1",
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1",
    "cp.phase6-module-test-contracts-data.v1",
    "cp.phase6-fixture-rules-data.v1",
    "cp.context-budget-and-packet-policy.v1"
  ],
  "file_whitelist_ref": "wl.phase6-r4-artifact-workspace-surface-validation.v1",
  "deliverables": [
    "Implemented R4 artifact workspace app surfaces, projection helpers, contract tests, and fixture assets inside the named whitelist.",
    "Validation evidence covering the release-specific fixture families cited by the governing blueprint."
  ],
  "validation_hooks": [
    {
      "hook_id": "vh.dependency.integrity"
    },
    {
      "hook_id": "vh.consistency.cross-pack-review"
    },
    {
      "hook_id": "vh.fixture.or-test-when-applicable"
    },
    {
      "hook_id": "vh.manual.acceptance"
    }
  ],
  "approval_requirements": [
    "Human implementation-owner acceptance before packet promotion or downstream use.",
    "Split or escalate if the work cannot stay inside the named whitelist, selected budget band, or prerequisite chain."
  ],
  "execution_mode": "factory_first",
  "carry_forward_topics": [
    "r4-artifact-workspace surface_validation packet",
    "packet template changes",
    "common failure modes",
    "execution guardrail refinements"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: transform.",
    "Packet family: surface_validation.",
    "Prerequisite packets: pkt.phase6-r4-artifact-workspace-runtime-execution-packet.v1"
  ]
}
```

## File whitelist `wl.phase6-r4-artifact-workspace-surface-validation.v1`

- `apps/chat-native/r4-artifact-workspace/`
- `apps/chat-native/r4-proposal-inbox/`
- `packages/projection-grammar/artifact-workspace-projection/`
- `packages/monitor-inspect/artifact-workspace/`
- `tests/contracts/r4-artifact-workspace/`
- `tests/fixtures/r4-artifact-workspace/`

## Run-class and execution posture

- Run class: `transform`
- Selected budget band: `standard`
- Packet family: `surface_validation`
- Touched roots: `apps/`, `packages/`, `tests/`

## Packet rationale

- This packet slices `bp.phase6-r4-artifact-workspace-blueprint.v1` along the bounded `surface_validation` family rather than widening one release packet beyond the accepted standard band.
- The whitelist stays inside `apps/`, `packages/`, `tests/` and mirrors the accepted module clusters frozen in `cp.phase6-release-blueprint-index-data.v1`.
- Prerequisite packets: `pkt.phase6-r4-artifact-workspace-runtime-execution-packet.v1`.
