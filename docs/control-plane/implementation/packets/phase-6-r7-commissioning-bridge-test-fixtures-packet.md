# Phase 6 R7 commissioning bridge test and fixtures packet
Version: 1.0
Status: Accepted
Task: P6.6 — Agent execution packets
Artifact ID: pkt.phase6-r7-commissioning-bridge-test-fixtures-packet.v1
Packet scope: Bounded `transform` packet for implementing release-local contract tests, fixture assets, and validator touchpoints for the R7 commissioning bridge.
File whitelist ref: wl.phase6-r7-commissioning-bridge-test-fixtures.v1

This packet is accepted for downstream use.
It delegates one bounded test-fixtures slice of the accepted R7 commissioning bridge implementation blueprint.
It does not authorize writes outside the named whitelist or the selected budget band.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-r7-commissioning-bridge-test-fixtures-packet.v1",
  "title": "Phase 6 R7 commissioning bridge test and fixtures packet",
  "task_id": "P6.6",
  "objective": "Implement the R7 commissioning-bridge test and fixture slice from the accepted blueprint while preserving handoff-continuity coverage and bounded test-only scope.",
  "scope": [
    "Implement only the R7 contract-test and fixture clusters named in the whitelist.",
    "Preserve explicit handoff-continuity, lane-separated review coverage, and failure-state visibility in test assets."
  ],
  "out_of_scope": [
    "Scope widening beyond the named file whitelist or selected budget band.",
    "Semantic changes to accepted release doctrine, repo/package architecture, or documentation-plane ownership.",
    "App, package, service, or worker implementation outside the named test and fixture clusters."
  ],
  "source_authority_refs": [
    "rel.r7-commissioning-bridge-contract.v1",
    "reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1"
  ],
  "accepted_artifact_refs": [
    "bp.phase6-r7-commissioning-bridge-blueprint.v1",
    "cp.phase6-release-blueprint-index-data.v1",
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1",
    "cp.phase6-fixture-rules-data.v1",
    "cp.context-budget-and-packet-policy.v1"
  ],
  "file_whitelist_ref": "wl.phase6-r7-commissioning-bridge-test-fixtures.v1",
  "deliverables": [
    "Implemented R7 contract tests and fixture assets inside the named whitelist.",
    "Validation evidence covering handoff continuity, failure-state inspection, and lane-separated review behavior."
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
    "r7-commissioning-bridge test_fixtures packet",
    "packet template changes",
    "common failure modes",
    "execution guardrail refinements"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: transform.",
    "Packet family: test_fixtures.",
    "Prerequisite packets: pkt.phase6-r7-commissioning-bridge-task-studio-handoff-packet.v1"
  ]
}
```

## File whitelist `wl.phase6-r7-commissioning-bridge-test-fixtures.v1`

- `tests/contracts/r7-commissioning-bridge/`
- `tests/fixtures/r7-commissioning-bridge/`

## Run-class and execution posture

- Run class: `transform`
- Selected budget band: `standard`
- Packet family: `test_fixtures`
- Touched roots: `tests/`

## Packet rationale

- This packet slices `bp.phase6-r7-commissioning-bridge-blueprint.v1` along the bounded `test_fixtures` family rather than widening one release packet beyond the accepted standard band.
- The whitelist stays inside `tests/` and mirrors the accepted module clusters frozen in `cp.phase6-release-blueprint-index-data.v1`.
- Prerequisite packets: `pkt.phase6-r7-commissioning-bridge-task-studio-handoff-packet.v1`.
