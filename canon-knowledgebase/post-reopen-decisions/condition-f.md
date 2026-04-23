# Accepted Decision: Condition (f) — Platform Gate truth-status

## Status

ACCEPTED. Recorded durably by plan-owner on 2026-04-23.

## Plan-owner

SaintFreddy (repo owner, Canon plan authority).

## Accepted option

**Option A** — Reopen formally. List remediation sub-gates PG-01.1, PG-07.1, PG-10.1 in the Platform Gate spec.

## Decision statement

`Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` P3.6 acceptance marker changes from `Gate passed` to `Gate reopened — audit-cited contradiction event 2026-04-18`. The prior `passed` state is preserved as append-only history; **do not delete**.

Three new remediation sub-gates are defined:

- **PG-01.1** — engine Clock abstraction landed; stableStringify unified in `@canon/engine-core`; localeCompare purged from replay-sensitive sort paths; `frozenAt` placement decision recorded and implemented.
- **PG-07.1** — credentialScope enforcement landed per condition (b) B-1 Option A.
- **PG-10.1** — `spawnToolSandboxWorker` + `attachToolSandboxWorkerIpc` shipped on public exports per condition (b) B-2 Option A and B-3 Option A.

Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`.

`canon-phase-4-plus-plan §206-207` and every Inherited Baseline item that cites Platform Gate as `passed` gets a footnote: "This inherited baseline remains carry-forward substrate truth, but the gate acceptance marker has been reopened against audit 2026-04-18; see `post-reopen-audit-cited-contradiction-checkpoint`."

`post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint` is formally superseded by `post-reopen-audit-cited-contradiction-checkpoint` (the checkpoint file already exists as the successor).

## Rationale summary

- Option B (retain `passed` with footnotes) trades honesty for cadence. Sets a precedent that `passed` can coexist with audit-cited contradictions against the spec's own exit criteria. Publicly readable as `passed` without the footnote context.
- Option C (freeze Canon entirely) surrenders any bounded progress while decisions are being recorded — a harder stop than today's baton state with no upside.
- Option A is the only option that is honest, explicit, recoverable, and append-only. It matches the `CANON_PLAN_IMPACT_REPORT.md` Section 6 row 10 default recommendation and the successor-checkpoint structure already built into the knowledgebase.

## Coupling with conditions (a) and (b)

This decision is the natural counterpart of:

- **Condition (a) = Option A** (Clock seam landed) closes PG-01.1.
- **Condition (b) = A+A+A** (credentialScope + fork + IPC export) closes PG-07.1 and PG-10.1.

Together, the three decisions form the "Honest now" package: real Clock, real credential enforcement, real fork, formal gate reopen. No carry-forward debt. No retained "passed" status coexisting with cited contradictions.

## What this unblocks

- `pkt.remediate-platform-gate-truth-status.v1` — authorized for execution, but **ordering matters**: under Option A (formal reopen), this packet goes FIRST (before the engine remediation packets) so the gate posture is documented honestly before any remediation work lands.
- Downstream Canon doc synchronization packets:
  - `PG-R1` — Platform Gate spec reopen markup (doc-only edit).
  - `PG-R2` — downstream blueprint footnote sync.
  - `PG-R3` — maturity matrix and high-level architecture footnote sync.

After `PG-R1` + `PG-R2` + `PG-R3` land, the PG-01.1 / PG-07.1 / PG-10.1 sub-gates close as the corresponding engine remediation packets land on `SaintFreddy/agentic-engine`.

## New constraints accepted with this decision

1. Platform Gate spec must show both the prior `passed` marker and the new `reopened` marker. Neither is ever deleted.
2. Canon docs that reference Platform Gate's `passed` state must be synced in the same reopen transaction. Any surface that still says `passed` without the footnote is a lint bug after this decision.
3. Ordinary baton continuation remains paused until PG-01.1, PG-07.1, and PG-10.1 close. The Phase 4+ plan step ledger gets three new gated steps; step 20 narrows to "record remaining 9 decisions + close remediation gates."
4. Release messaging that claimed Platform Gate was passed must be retracted or footnoted. Internal-only for now; public-posture implications when R1 ships externally.

## Reference to draft options analysis

Full option analysis at `/Users/fredericksaintmaximus/Desktop/Canon Dev/decisions/condition-f.md` (draft, preserved as historical record). Cited audit findings: `OWN-001`, `PKG-CORE-THEME-001`, `PKG-CC-002/003`, `PKG-PROV-001/002/004`, `OWN-008`, `PKG-TG-001/011`, `PKG-MG-024`, `PKG-VAL-001..004`, `WRK-TS-001`. Section 5 over-claim entries items 1, 2, 5. Platform Gate mapping at `CANON_PLAN_IMPACT_REPORT.md` Section 4 / L555+.

## Execution posture

- First remediation packet to land under this decision: `pkt.remediate-platform-gate-truth-status.v1` on `SaintFreddy/Canon` (control-plane only, no engine code touched).
- Model: `claude-opus-4-7`, reasoning effort `high`.
- Verification: Platform Gate spec shows both markers; every downstream doc that referenced `passed` is updated; `python3 scripts/validators/validate_control_plane_integrity.py` green; `canon-now.md`, `canon_tasks.md`, carry-forward updated in the same session.
- Human review required on the resulting PR before merge.
