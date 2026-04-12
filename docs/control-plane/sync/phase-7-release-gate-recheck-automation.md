# Phase 7 release-gate recheck automation
Version: 1.0
Status: Accepted
Task: P7.4 — Release gate re-check automation
Artifact ID: sync.phase7-release-gate-recheck-automation.v1
Sync scope: Accepted release-gate recheck routine for selecting Platform Gate and R1-R7 structural validation follow-ups from accepted stale-detection output after accepted changes.

This artifact is accepted for downstream use.
It turns accepted stale-detection output into one explicit release-readiness recheck routine instead of relying on ad hoc judgment about which release gates are pressured.

## 1. Purpose

This routine exists to:

- consume the accepted stale-detection output produced by `sync.phase7-stale-regeneration-loop.v1`,
- choose the Platform Gate or release-contract rechecks that matter for the current accepted change,
- record one explicit `release-gate follow-up state` for the active delta pack or carry-forward entry.

## 2. Scope boundaries

### In scope

- accepted stale-detection reports derived from `cp.phase7-stale-regeneration-rules-data.v1`,
- structural release-readiness rechecks over `arch.phase3-platform-gate-spec.v1`, `rel.chat-native-maturity-matrix.v1`, `rel.chat-native-milestone-architecture-plan.v1`, and the accepted R1-R7 release, blueprint, and packet artifacts,
- automated command selection and optional execution through `cp.phase7-release-gate-recheck-matrix-data.v1`.

### Out of scope

- inventing runtime gate tests that do not exist in this repo,
- auto-accepting human-owned release readiness or Platform Gate passage,
- replacing `sync.phase7-recurring-architecture-sync.v1` or `sync.phase7-stale-regeneration-loop.v1` with a second sync model.

## 3. Governing baseline

This routine inherits and operationalizes:

- `cp.master-plan.v1`
- `cp.artifact-control-plane-spec.v1`
- `sync.phase7-carry-forward-delta-pack.v1`
- `sync.phase7-recurring-architecture-sync.v1`
- `sync.phase7-stale-regeneration-loop.v1`
- `cp.phase7-delta-pack-index-data.v1`
- `cp.phase7-architecture-sync-checklist-data.v1`
- `cp.phase7-stale-regeneration-rules-data.v1`
- `arch.phase3-platform-gate-spec.v1`
- `rel.chat-native-maturity-matrix.v1`
- `rel.chat-native-milestone-architecture-plan.v1`
- `cp.phase6-release-blueprint-index-data.v1`
- `cp.phase6-execution-packet-index-data.v1`

The machine-readable release-gate routing baseline for this routine lives in `cp.phase7-release-gate-recheck-matrix-data.v1`.

## 4. Operating loop

### 4.1 Recheck selection sequence

1. Start from an accepted stale-detection report, or let `python3 scripts/wrappers/run_phase7_release_gate_rechecks.py --changed-artifact <artifact-ref> ...` generate one through the accepted P7.3 wrapper.
2. Match the stale report’s changed and impacted artifact refs against `cp.phase7-release-gate-recheck-matrix-data.v1`.
3. Select every matching release gate and always include `arch.phase3-platform-gate-spec.v1` when any R1-R7 release gate is selected.

### 4.2 Recheck execution

- Use `--run-commands` when the selected structural rechecks should execute immediately.
- Treat the matrix commands as structural release-readiness checks only: sync validators, architecture-sync review, release-blueprint validation, and release-local packet validation.
- If the selected commands do not run, record `release-gate follow-up state` as `recheck_required` rather than treating release readiness as complete.

### 4.3 Carry-forward handoff

- Write the resulting `release-gate follow-up state` (`not_required`, `recheck_required`, `recheck_pass`, or `recheck_fail`) into the active delta pack and any related carry-forward entry.
- Keep human-owned Platform Gate and release acceptance decisions explicit even when all selected structural rechecks pass.

## 5. Validation and review

- Run `python3 scripts/validators/validate_control_plane_integrity.py`.
- Run `python3 scripts/validators/validate_phase7_sync_artifacts.py`.
- Run `python3 scripts/wrappers/run_phase7_release_gate_rechecks.py --changed-artifact <artifact-ref> ...`.
- Run the existing Phase 6 blueprint and packet validators before accepting changes to `cp.phase7-release-gate-recheck-matrix-data.v1`.

## 6. Acceptance notes

- This routine routes structural rechecks from accepted stale-detection output; it does not claim that this repo contains the full runtime substrate needed for final launch decisions.
- Platform Gate remains a human-owned blocker even when this automation successfully selects and runs every available structural recheck.
