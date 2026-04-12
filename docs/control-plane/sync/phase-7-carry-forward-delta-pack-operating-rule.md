# Phase 7 carry-forward delta pack operating rule
Version: 1.0
Status: Accepted
Task: P7.1 — Carry-forward delta pack after every packet/release
Artifact ID: sync.phase7-carry-forward-delta-pack.v1
Sync scope: Accepted delta-capture template and operating rule for release, packet, and sync changes that must preserve downstream impact and carry-forward continuity.

This artifact is accepted for downstream use.
It defines the minimum delta-pack shape and operating loop that every accepted release, packet, or sync change must follow before downstream work continues.

## 1. Purpose

This rule exists to:

- make every accepted release-, packet-, or sync-scoped change leave one durable and reviewable delta record,
- keep downstream impact capture explicit instead of implicit or transcript-local,
- pair every accepted delta with the registry, dependency-graph, and carry-forward updates needed for later stale detection and revalidation.

## 2. Scope boundaries

### In scope

- accepted changes to `cp.phase6-release-blueprint-index-data.v1`,
- accepted changes to `cp.phase6-execution-packet-index-data.v1`,
- accepted changes to any `bp.phase6-*` release blueprint,
- accepted changes to any `pkt.phase6-*` execution packet,
- accepted changes to any later `sync.*` artifact that modifies Phase 7 delta, sync, stale, or gate routines,
- synchronized updates to `docs/control-plane/artifact-registry.seed.json`, `docs/control-plane/dependency-graph.seed.json`, and `docs/control-plane/core/master-plan.md` whenever accepted artifacts change.

### Out of scope

- reopening accepted source authority or baseline product decisions,
- auto-accepting human-owned meaning or stale review outcomes,
- runtime or product-code mutations outside an explicitly accepted packet scope,
- silent durable-state changes that are not captured through registry/graph/master-plan synchronization.

## 3. Governing baseline

This rule inherits the accepted control-plane model from:

- `cp.master-plan.v1`
- `cp.artifact-control-plane-spec.v1`
- `cp.phase6-release-blueprint-index-data.v1`
- `cp.phase6-execution-packet-index-data.v1`
- `surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1`

The machine-readable coverage map for this rule lives in `cp.phase7-delta-pack-index-data.v1`.

## 4. Operating loop

### 4.1 Triggering accepted changes

1. Before starting the change, verify local `main` matches `origin/main`.
2. If the accepted change touches any tracked release blueprint, execution packet, packet index, release-blueprint index, or accepted Phase 7 sync artifact, prepare a delta pack before marking the task done.
3. The delta pack lives under `docs/control-plane/sync/`, while the carry-forward summary remains append-only in `docs/control-plane/core/master-plan.md`.
4. Registry and dependency-graph updates stay in the same accepted change whenever the delta pack or any touched artifact is part of accepted repo truth.

### 4.2 Required delta pack template

Use this minimum shape for future change-specific delta packs:

```text
# Delta pack — <change slug>
Version: 1.0
Status: Accepted
Task: <phase/task>
Artifact ID: sync.<change-slug>.v1
Sync scope: Accepted delta record for <trigger artifact ref or accepted task>

## 1. Purpose
- What changed and why the change was accepted.

## 2. Scope boundaries
- Trigger artifact refs, touched files, and explicit out-of-scope items.

## 3. Governing baseline
- Source authority refs and accepted artifact refs used to evaluate the change.

## 4. Operating loop
- Accepted change summary
- Affected downstream artifact refs
- Required stale-review or revalidation actions
- Required regeneration or release-gate follow-ups

## 5. Validation and review
- Commands run
- Manual review or approval obligations
- Sync and stale outcomes

## 6. Acceptance notes
- Carry-forward entry ref
- Remaining follow-ups or explicit “None”
```

### 4.3 Minimum captured fields

Every accepted delta pack must capture:

- trigger artifact ref or accepted task ID,
- accepted change summary,
- touched accepted artifact refs,
- affected downstream artifact refs,
- required stale-review or revalidation actions,
- regeneration commands or explicit `None`,
- release-gate follow-up state,
- master-plan carry-forward entry ref.

### 4.4 Coverage rule for Phase 6 assets

- Every artifact listed in `cp.phase7-delta-pack-index-data.v1` is a mandatory delta-capture trigger.
- Release-level changes must cite both the relevant `rel.*` ref and the bounded `bp.phase6-*` or `pkt.phase6-*` refs they affect.
- Packet-family changes must preserve the accepted prerequisite chain and record whether downstream packets, sync packs, or harness outputs need regeneration.

## 5. Validation and review

- Run `python3 scripts/validators/validate_control_plane_integrity.py`.
- Run `python3 scripts/validators/validate_phase7_sync_artifacts.py`.
- Run any validator or wrapper required by the affected release, packet, or sync artifact family before acceptance.
- Append the carry-forward entry only after validators pass and the registry, dependency graph, and master plan are synchronized.

## 6. Acceptance notes

- This artifact establishes the minimum delta-capture loop for Phase 7 without inventing a second control plane.
- Later Phase 7 tasks may extend automation around this rule, but they must preserve the durable delta-pack plus carry-forward pair as the reviewable record of accepted change.
