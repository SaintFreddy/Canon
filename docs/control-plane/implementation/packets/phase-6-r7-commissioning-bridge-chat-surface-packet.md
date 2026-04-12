# Phase 6 R7 commissioning bridge chat surface packet
Version: 1.0
Status: Accepted
Task: P6.6 — Agent execution packets
Artifact ID: pkt.phase6-r7-commissioning-bridge-chat-surface-packet.v1
Packet scope: Bounded `transform` packet for implementing release-local chat-native commissioning surfaces plus shared projection and inspect helpers for the R7 bridge.
File whitelist ref: wl.phase6-r7-commissioning-bridge-chat-surface.v1

This packet is accepted for downstream use.
It delegates one bounded chat-surface slice of the accepted R7 commissioning bridge implementation blueprint.
It does not authorize writes outside the named whitelist or the selected budget band.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-r7-commissioning-bridge-chat-surface-packet.v1",
  "title": "Phase 6 R7 commissioning bridge chat surface packet",
  "task_id": "P6.6",
  "objective": "Implement the R7 commissioning bridge chat-native commissioning surface slice from the accepted release blueprint without widening into Task Studio or runtime roots outside the whitelist.",
  "scope": [
    "Implement only the R7 chat-native commissioning surface, shared projection-grammar, and shared inspect clusters named in the whitelist.",
    "Preserve the accepted Commission -> Contract -> Run and lane-separated review semantics at the surface layer."
  ],
  "out_of_scope": [
    "Scope widening beyond the named file whitelist or selected budget band.",
    "Semantic changes to accepted release doctrine, repo/package architecture, or documentation-plane ownership.",
    "Package-contract or runtime execution work outside the named surface-validation clusters."
  ],
  "source_authority_refs": [
    "rel.r7-commissioning-bridge-contract.v1"
  ],
  "accepted_artifact_refs": [
    "bp.phase6-r7-commissioning-bridge-blueprint.v1",
    "cp.phase6-release-blueprint-index-data.v1",
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1",
    "cp.phase6-module-test-contracts-data.v1",
    "cp.phase6-fixture-rules-data.v1",
    "cp.context-budget-and-packet-policy.v1"
  ],
  "file_whitelist_ref": "wl.phase6-r7-commissioning-bridge-chat-surface.v1",
  "deliverables": [
    "Implemented R7 chat-native commissioning surfaces plus shared projection and inspect helpers inside the named whitelist.",
    "Validation evidence showing the packet preserved explicit preflight, monitor, proof, and delta visibility."
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
    "r7-commissioning-bridge chat_surface packet",
    "packet template changes",
    "common failure modes",
    "execution guardrail refinements"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: transform.",
    "Packet family: chat_surface.",
    "Prerequisite packets: pkt.phase6-r7-commissioning-bridge-runtime-execution-packet.v1"
  ]
}
```

## File whitelist `wl.phase6-r7-commissioning-bridge-chat-surface.v1`

- `apps/chat-native/r7-commissioning-bridge/`
- `apps/chat-native/r7-live-monitor/`
- `apps/chat-native/r7-chat-to-run-handoff/`
- `packages/projection-grammar/commissioning-projection/`
- `packages/monitor-inspect/commissioning-monitor/`

## Run-class and execution posture

- Run class: `transform`
- Selected budget band: `standard`
- Packet family: `chat_surface`
- Touched roots: `apps/`, `packages/`

## Packet rationale

- This packet slices `bp.phase6-r7-commissioning-bridge-blueprint.v1` along the bounded `chat_surface` family rather than widening one release packet beyond the accepted standard band.
- The whitelist stays inside `apps/`, `packages/` and mirrors the accepted module clusters frozen in `cp.phase6-release-blueprint-index-data.v1`.
- Prerequisite packets: `pkt.phase6-r7-commissioning-bridge-runtime-execution-packet.v1`.
