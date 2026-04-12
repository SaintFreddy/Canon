# Phase 6 R1 conversation runtime execution packet
Version: 1.0
Status: Accepted
Task: P6.6 — Agent execution packets
Artifact ID: pkt.phase6-r1-conversation-runtime-execution-packet.v1
Packet scope: Bounded `transform` packet for implementing release-local services and workers behind accepted package contracts and boundary rules.
File whitelist ref: wl.phase6-r1-conversation-runtime-execution.v1

This packet is accepted for downstream use.
It delegates one bounded runtime-execution slice of the accepted R1 conversation implementation blueprint.
It does not authorize writes outside the named whitelist or the selected budget band.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-r1-conversation-runtime-execution-packet.v1",
  "title": "Phase 6 R1 conversation runtime execution packet",
  "task_id": "P6.6",
  "objective": "Implement the R1 conversation runtime services/workers slice from the accepted release blueprint inside bounded execution scope without widening into packages, apps, or tests outside the whitelist.",
  "scope": [
    "Implement only the R1 conversation services and workers named in the whitelist.",
    "Preserve typed control, provenance, review, and worker-boundary rules while keeping scope inside the named execution seams."
  ],
  "out_of_scope": [
    "Scope widening beyond the named file whitelist or selected budget band.",
    "Semantic changes to accepted release doctrine, repo/package architecture, or documentation-plane ownership.",
    "Package-contract, app-surface, or test/fixture work outside the named runtime clusters."
  ],
  "source_authority_refs": [
    "rel.r1-transcript-chat-contract.v1"
  ],
  "accepted_artifact_refs": [
    "bp.phase6-r1-conversation-blueprint.v1",
    "cp.phase6-release-blueprint-index-data.v1",
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1",
    "cp.phase6-module-test-contracts-data.v1",
    "cp.context-budget-and-packet-policy.v1"
  ],
  "file_whitelist_ref": "wl.phase6-r1-conversation-runtime-execution.v1",
  "deliverables": [
    "Implemented R1 conversation services and workers inside the named whitelist.",
    "Runtime-slice validation evidence showing the packet stayed inside accepted execution boundaries."
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
    "r1-conversation runtime_execution packet",
    "packet template changes",
    "common failure modes",
    "execution guardrail refinements"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: transform.",
    "Packet family: runtime_execution.",
    "Prerequisite packets: pkt.phase6-r1-conversation-contracts-objects-packet.v1"
  ]
}
```

## File whitelist `wl.phase6-r1-conversation-runtime-execution.v1`

- `services/environment-shell-api/conversation-entry/`
- `services/execution-control/run-dispatch/`
- `services/model-gateway/chat-turn-execution/`
- `services/event-provenance/run-trace/`
- `workers/context-compiler/compile-run-context/`

## Run-class and execution posture

- Run class: `transform`
- Selected budget band: `standard`
- Packet family: `runtime_execution`
- Touched roots: `services/`, `workers/`

## Packet rationale

- This packet slices `bp.phase6-r1-conversation-blueprint.v1` along the bounded `runtime_execution` family rather than widening one release packet beyond the accepted standard band.
- The whitelist stays inside `services/`, `workers/` and mirrors the accepted module clusters frozen in `cp.phase6-release-blueprint-index-data.v1`.
- Prerequisite packets: `pkt.phase6-r1-conversation-contracts-objects-packet.v1`.
