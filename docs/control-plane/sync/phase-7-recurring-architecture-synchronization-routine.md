# Phase 7 recurring architecture synchronization routine
Version: 1.0
Status: Accepted
Task: P7.2 — Recurring architecture synchronization after every accepted delta
Artifact ID: sync.phase7-recurring-architecture-sync.v1
Sync scope: Accepted recurring architecture-sync checklist and execution routine for every accepted delta that could pressure canon, semantics, architecture, or repo-boundary truth.

This artifact is accepted for downstream use.
It turns the one-time Phase 3 architecture sync pass into a recurring post-delta routine that keeps accepted control-plane changes aligned with canon, semantics, architecture, and forbidden-shortcut constraints.

## 1. Purpose

This routine exists to:

- force every accepted delta through one explicit architecture-alignment review instead of relying on memory or informal diff reading,
- preserve the accepted three-layer boundary, run-native substrate, lane-separated governance, and Platform Gate posture across later release-, packet-, and sync-level changes,
- hand both humans and Factory one stable checklist and one stable execution wrapper for recurring sync work.

## 2. Scope boundaries

### In scope

- accepted deltas that touch `bp.phase6-*`, `pkt.phase6-*`, `cp.phase6-*`, or `sync.*` artifacts,
- accepted changes to registry, dependency-graph, manifest, or current-state datasets that could shift repo-boundary truth,
- recurring review of canon, semantic, architecture, repo-boundary, and forbidden-shortcut pressure points named in `cp.phase7-architecture-sync-checklist-data.v1`.

### Out of scope

- auto-accepting human-owned architecture meaning,
- replacing the accepted Phase 3 sync pass with a new ontology or review surface,
- marking downstream artifacts stale automatically without the explicit stale-detection rules introduced later in Phase 7,
- product-runtime verification beyond the accepted control-plane and release-contract scope already present in the repo.

## 3. Governing baseline

This routine inherits and re-checks the accepted architecture baseline from:

- `cp.master-plan.v1`
- `cp.artifact-control-plane-spec.v1`
- `sync.phase7-carry-forward-delta-pack.v1`
- `cp.phase7-delta-pack-index-data.v1`
- `arch.phase3-architecture-sync-pass.v1`
- `arch.phase3-platform-gate-spec.v1`
- `cp.forbidden-shortcuts-register.v1`
- `surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1`
- `surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1`

The machine-readable recurring checklist for this routine lives in `cp.phase7-architecture-sync-checklist-data.v1`.

## 4. Operating loop

### 4.1 Recurring sync sequence

1. After an accepted delta is prepared, run `python3 scripts/wrappers/run_phase7_architecture_sync.py`.
2. Review every checklist group in `cp.phase7-architecture-sync-checklist-data.v1` against the accepted delta and the affected artifact refs named by the current delta pack.
3. If a checklist prompt reveals drift, capture it in the active delta pack or carry-forward entry and either fix the issue immediately or hand it forward as a stale candidate for the later stale-detection loop.
4. Record one explicit architecture-sync outcome per checklist group: `aligned`, `review_required`, or `stale_candidate`.

### 4.2 Required checklist groups

Every recurring sync pass must cover:

- topology and layer-boundary preservation,
- run, context, and provenance continuity,
- governance, proof, and writeback-lane discipline,
- projection-grammar plus repo-boundary discipline,
- forbidden-shortcut and Platform Gate regression review.

### 4.3 Escalation rule

- If any checklist group identifies layer-ownership drift, transcript-truth drift, writeback-lane collapse, projection/private-backend drift, or Platform Gate weakening, the change may not be treated as architecture-aligned until the issue is resolved or explicitly handed forward as a stale candidate.
- The recurring sync routine may prepare the evidence, but human review remains authoritative for final architecture meaning and stale-review outcomes.

## 5. Validation and review

- Run `python3 scripts/validators/validate_control_plane_integrity.py`.
- Run `python3 scripts/validators/validate_phase7_sync_artifacts.py`.
- Run `python3 scripts/wrappers/run_phase7_architecture_sync.py`.
- Keep the architecture-sync outcome attached to the active delta pack or carry-forward entry instead of replacing the accepted Phase 3 baseline artifact.

## 6. Acceptance notes

- This routine preserves the accepted Phase 3 sync logic as a recurring review loop rather than re-deriving architecture meaning from scratch after every change.
- Later Phase 7 automation may classify stale or gate follow-up work automatically, but recurring architecture synchronization must remain visible and attributable.
