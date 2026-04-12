# Phase 6 R7 commissioning bridge Task Studio handoff packet
Version: 1.0
Status: Accepted
Task: P6.6 — Agent execution packets
Artifact ID: pkt.phase6-r7-commissioning-bridge-task-studio-handoff-packet.v1
Packet scope: Bounded `transform` packet for implementing Task Studio route landings that preserve the accepted R7 commissioning handoff payload without ontology translation.
File whitelist ref: wl.phase6-r7-commissioning-bridge-task-studio-handoff.v1

This packet is accepted for downstream use.
It delegates one bounded task-studio-handoff slice of the accepted R7 commissioning bridge implementation blueprint.
It does not authorize writes outside the named whitelist or the selected budget band.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-r7-commissioning-bridge-task-studio-handoff-packet.v1",
  "title": "Phase 6 R7 commissioning bridge Task Studio handoff packet",
  "task_id": "P6.6",
  "objective": "Implement the R7 Task Studio handoff landing slice from the accepted commissioning-bridge blueprint while preserving the accepted handoff payload and shared IDs.",
  "scope": [
    "Implement only the accepted Task Studio `TS-SC-*` route landings named in the whitelist.",
    "Preserve the exact R7 handoff payload and shared-ID continuity without ontology translation or task-shell recreation."
  ],
  "out_of_scope": [
    "Scope widening beyond the named file whitelist or selected budget band.",
    "Semantic changes to accepted release doctrine, repo/package architecture, or documentation-plane ownership.",
    "Chat-native commissioning surfaces, runtime execution, or test-fixture work outside the named Task Studio route clusters."
  ],
  "source_authority_refs": [
    "rel.r7-commissioning-bridge-contract.v1",
    "reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1",
    "surf.phase6-task-studio-surface-contract-pack.v1"
  ],
  "accepted_artifact_refs": [
    "bp.phase6-r7-commissioning-bridge-blueprint.v1",
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1",
    "cp.phase6-fixture-rules-data.v1",
    "cp.context-budget-and-packet-policy.v1"
  ],
  "file_whitelist_ref": "wl.phase6-r7-commissioning-bridge-task-studio-handoff.v1",
  "deliverables": [
    "Implemented R7 Task Studio route landings inside the named whitelist.",
    "Validation evidence showing preserved handoff payload continuity and shared-ID stability across the landing surfaces."
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
    "r7-commissioning-bridge task_studio_handoff packet",
    "packet template changes",
    "common failure modes",
    "execution guardrail refinements"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: transform.",
    "Packet family: task_studio_handoff.",
    "Prerequisite packets: pkt.phase6-r7-commissioning-bridge-chat-surface-packet.v1"
  ]
}
```

## File whitelist `wl.phase6-r7-commissioning-bridge-task-studio-handoff.v1`

- `apps/task-studio/ts-sc-01-task-home/`
- `apps/task-studio/ts-sc-03-task-contract-panel/`
- `apps/task-studio/ts-sc-05-context-inspector/`
- `apps/task-studio/ts-sc-07-authority-panel/`
- `apps/task-studio/ts-sc-08-live-run-view/`
- `apps/task-studio/ts-sc-10-proof-ledger/`
- `apps/task-studio/ts-sc-11-delta-inspector/`
- `apps/task-studio/ts-sc-12-writeback-panel/`

## Run-class and execution posture

- Run class: `transform`
- Selected budget band: `standard`
- Packet family: `task_studio_handoff`
- Touched roots: `apps/`

## Packet rationale

- This packet slices `bp.phase6-r7-commissioning-bridge-blueprint.v1` along the bounded `task_studio_handoff` family rather than widening one release packet beyond the accepted standard band.
- The whitelist stays inside `apps/` and mirrors the accepted module clusters frozen in `cp.phase6-release-blueprint-index-data.v1`.
- Prerequisite packets: `pkt.phase6-r7-commissioning-bridge-chat-surface-packet.v1`.
