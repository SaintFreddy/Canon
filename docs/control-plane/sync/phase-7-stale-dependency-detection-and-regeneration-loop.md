# Phase 7 stale dependency detection and regeneration loop
Version: 1.0
Status: Accepted
Task: P7.3 — Stale dependency detection and regeneration loop
Artifact ID: sync.phase7-stale-regeneration-loop.v1
Sync scope: Accepted stale-detection and regeneration loop for tracing accepted upstream changes through the dependency graph, preparing stale markers, and reporting regeneration commands.

This artifact is accepted for downstream use.
It turns the accepted dependency graph, delta-pack baseline, and recurring architecture checklist into one explicit stale-detection and regeneration loop.

## 1. Purpose

This loop exists to:

- detect which accepted downstream artifacts are pressured when accepted upstream truth changes,
- translate graph propagation modes into explicit stale, revalidation, or manual-review actions,
- report the regeneration commands and optional stale-marker updates needed to keep accepted artifacts coherent.

## 2. Scope boundaries

### In scope

- accepted artifacts represented in `cp.artifact-registry-data.v1` and `cp.dependency-graph-data.v1`,
- accepted release, packet, sync, and control-plane datasets that inherit stale behavior through explicit graph edges,
- optional registry/graph stale-marker updates for `auto` propagation edges only,
- regeneration-command reporting and execution through the accepted rules frozen in `cp.phase7-stale-regeneration-rules-data.v1`.

### Out of scope

- auto-accepting human-owned stale reviews or architecture meaning,
- inventing new edge types, propagation modes, or stale rules outside the accepted P0.1 catalogs,
- silently mutating accepted truth without the corresponding delta-pack and carry-forward updates.

## 3. Governing baseline

This loop inherits and operationalizes:

- `cp.master-plan.v1`
- `cp.artifact-control-plane-spec.v1`
- `sync.phase7-carry-forward-delta-pack.v1`
- `sync.phase7-recurring-architecture-sync.v1`
- `cp.phase7-delta-pack-index-data.v1`
- `cp.phase7-architecture-sync-checklist-data.v1`
- `cp.artifact-registry-data.v1`
- `cp.dependency-graph-data.v1`

The machine-readable regeneration rules for this loop live in `cp.phase7-stale-regeneration-rules-data.v1`.

## 4. Operating loop

### 4.1 Detection sequence

1. Run `python3 scripts/wrappers/run_phase7_stale_detection.py --changed-artifact <artifact-ref> ...` after an accepted upstream change is known.
2. Traverse the reverse dependency graph from every changed artifact and translate each encountered propagation mode into `mark_stale`, `manual_review`, `revalidate`, or `ignore`.
3. Attach regeneration commands from `cp.phase7-stale-regeneration-rules-data.v1` to every impacted artifact.

### 4.2 Regeneration and stale markers

- Use `--run-regeneration` when the loop should execute the reported regeneration commands immediately.
- Use `--apply-registry` only when `auto` propagation should update artifact and graph node statuses to `stale`.
- `manual_review` and `revalidate` outcomes remain visible and attributable; they do not silently become accepted again.

### 4.3 Carry-forward and sync handoff

- Feed any `manual_review` or `stale_candidate` outcome back into the active delta pack and recurring architecture-sync report.
- Treat the stale-detection output as one explicit input to later release-gate rechecks instead of relying on ad hoc diff reading.

## 5. Validation and review

- Run `python3 scripts/validators/validate_control_plane_integrity.py`.
- Run `python3 scripts/validators/validate_phase7_sync_artifacts.py`.
- Run `python3 scripts/wrappers/run_phase7_stale_detection.py --changed-artifact <artifact-ref> ...`.
- Keep stale-marker updates synchronized with the registry, dependency graph, and carry-forward log whenever `--apply-registry` is used.

## 6. Acceptance notes

- This loop reuses accepted graph semantics and rule catalogs rather than inventing a second stale-detection model.
- Later release-gate automation may consume its output, but stale detection remains the explicit place where downstream pressure and regeneration commands are surfaced.
