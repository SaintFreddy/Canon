# Phase 2 proof and validation invariants
Version: 1.0
Status: Accepted
Task: P2.4 — Proof / validation invariants
Artifact ID: reuse.phase2-proof-validation-invariants.v1
Reuse scope: Accepted invariant layer for proof expectations, uncertainty labeling, omission handling, contradiction handling, replay/comparison expectations, and failure taxonomy

## 1. Purpose

This pack defines the minimum proof and validation invariants that later proof packs, release packs, and Task Studio work must preserve.

It exists to:

- keep proof task-shaped instead of generic explanation-first,
- make uncertainty, omission, and contradiction handling explicit,
- define replay/comparison proof expectations before deeper evaluation work.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- proof object integrity,
- run-class proof minima,
- uncertainty, omission, and contradiction invariants,
- replay/comparison proof expectations,
- invariant-level failure classes.

### Out of scope

- full verifier-pack definitions,
- scoring thresholds and evaluation rubrics,
- fixture suites and benchmark harnesses,
- domain-specific proof packs,
- full failure recovery mechanics.

## 3. Invariant interpretation rules

### 3.1 Thin-layer rule

This pack locks only the invariant layer.
It does not attempt to become the full proof/evaluation spec.

### 3.2 Proof-is-not-prose rule

Proof is a structured object attached to a run.
It is not equivalent to answer prose, UI summaries, or approval state.

### 3.3 Frozen-basis rule

Accepted proof must be traceable back to the frozen admitted basis of the run.

## 4. Invariant catalog

| Invariant ID | Category | Rule | Attached objects |
| --- | --- | --- | --- |
| `PI-01` | Proof object integrity | Every terminal run emits exactly one `Proof Bundle` and one `State Delta`, including failed and no-op runs. | Run, Proof Bundle, State Delta |
| `PI-02` | Proof object integrity | Proof remains append-only, attached to one `run_id`, and distinct from result prose, delta, review, and approval state. | Run, Proof Bundle, Review, Approval Decision |
| `PI-03` | Run-class proof shape | Proof shape is selected by `run_class` plus `proof_policy_ref`, not by prompt text, surface, or mode. | Run Class, Protocol, Proof Bundle |
| `PI-04` | Uncertainty labeling | `uncertainty_items` are mandatory, explicit, and tied to the affected claim, field, option, or recommendation. | Proof Bundle |
| `PI-05` | Omission handling | Material omissions, excluded sources, missing fields, or unavailable inputs must be explicit in proof and may not be hidden in summary prose. | Proof Bundle, Evidence Pack, Context Pack |
| `PI-06` | Contradiction handling | Material contradictions must be recorded explicitly and marked handled or unresolved; unresolved material contradiction cannot masquerade as settled proof. | Proof Bundle, Evidence Pack, Context Pack |
| `PI-07` | Replay/comparison integrity | Replay, retry, and branch execution create new Run/Proof/Delta records and must reference frozen snapshots, packs, and lineage objects explicitly. | Run, Branch, Checkpoint, Proof Bundle, State Delta |
| `PI-08` | Validator continuity | Required verifier-slot outcomes attach to proof and are never hidden in logs, prose, or view-only state. | Protocol, Proof Bundle, Verifier results |
| `PI-09` | Governance fit | Proof may justify proposals but may not widen authority, apply writeback, or replace review/approval objects. | Proof Bundle, Writeback Proposal, Review, Approval Decision |
| `PI-10` | Failure inspectability | Failed execution, replay, or compare work must still emit inspectable proof/failure basis and a delta state. | Run, Proof Bundle, State Delta |

## 5. Run-class proof minima

| Run class | Invariant proof minimum | Verifier floor |
| --- | --- | --- |
| `compare` | comparison axes, explicit target refs, material differences, recommendation basis, uncertainty/omission | 2 slots minimum |
| `synthesize` | claim-to-evidence map, coverage notes, contradiction capture, uncertainty/omission | 2 slots minimum |
| `extract` | field-to-span map, normalization notes, missing-field handling distinct from uncertainty | 2 slots minimum |
| `transform` | lineage basis, desired-change -> proposed-change trace, validation results, risk notes | 3 slots minimum |
| `audit` | criteria-evaluation matrix, pass/fail/exception basis, evidence refs, contradiction capture | 2 slots minimum |
| `plan` | assumption set, dependency map, option tradeoffs, branch/checkpoint rationale | 2 slots minimum |
| `triage` | intake completeness, routing basis, scope/authority gap notes, risk basis | 2 slots minimum |

Run-class minima remain invariant-level only.
Full proof sections and evaluators are later work.

## 6. Replay and comparison expectations

| Expectation ID | Expectation | Failure class if broken |
| --- | --- | --- |
| `RC-01` | Replay/compare work must have explicit objective, frozen inputs, and class-fit target refs before proof can be accepted. | `intake_or_scope_insufficient` |
| `RC-02` | Replay/compare output must still return task-shaped proof plus delta, not transcript-only narrative. | `proof_shape_violation` |
| `RC-03` | Replay must reference `input_snapshot_ref`, explicit evidence/context refs, and branch/checkpoint lineage; new attempt means new historical record. | `replay_basis_invalid` |
| `RC-04` | Compare work must name targets, axes, material differences, and recommendation basis; UI/view diff alone is insufficient. | `comparison_basis_invalid` |
| `RC-05` | Missing, excluded, or non-parity material across compared/replayed bases must surface explicitly in proof. | `evidence_or_coverage_insufficient`, `material_omission_unhandled` |
| `RC-06` | Cross-source or cross-branch contradiction cannot be narrated away; unresolved conflict remains explicit. | `material_contradiction_unresolved` |
| `RC-07` | Same verifier-slot minima and authority limits apply in replay, background, and Task Studio projections. | `validator_failure`, `authority_or_policy_violation` |
| `RC-08` | Failed replay/compare runs still emit inspectable proof/failure basis and delta state. | `execution_or_adapter_failure` |

## 7. Failure-class baseline

| Failure class | Meaning |
| --- | --- |
| `intake_or_scope_insufficient` | Admitted basis is missing required objective, scope, or target information |
| `proof_shape_violation` | Returned proof does not satisfy the run-class-shaped minimum |
| `replay_basis_invalid` | Replay or retry cannot prove frozen lineage/basis continuity |
| `comparison_basis_invalid` | Comparison lacks explicit targets, axes, or material-difference basis |
| `evidence_or_coverage_insufficient` | Evidence or coverage is too incomplete for the stated objective |
| `material_omission_unhandled` | Material omission is visible but unresolved for the current acceptance claim |
| `material_contradiction_unresolved` | Material contradiction remains unresolved while the result claims settlement |
| `validator_failure` | Required verifier slot fails or does not run when required |
| `authority_or_policy_violation` | Proof path violates the approved authority or policy boundary |
| `execution_or_adapter_failure` | Execution or adapter failure prevents normal completion but still must remain inspectable |

## 8. Boundary locks for downstream work

1. Hedging language does not substitute for explicit uncertainty items.
2. Missing fields do not silently collapse into uncertainty; they remain omission-handling facts.
3. Replay proof is about semantic basis continuity, not transcript similarity.
4. Compare proof is about named targets and material differences, not just visual diff output.
5. Approval may accept a result only with the proof object that actually supports it.

## 9. Deferred to later proof/evaluation packs

| Later pack | Deferred detail |
| --- | --- |
| `P5.2` full proof / validation / evaluation spec | verifier-pack definitions, scoring thresholds, pass/fail rubrics, proof assemblers, replay/regression fixtures, task-family proof sections, benchmark datasets |

## 10. Downstream implications

### 10.1 For P2.5 and P4 release packs

- release semantic packs should state how each projection exposes these proof invariants instead of replacing them with answer-first summaries.

### 10.2 For P5.2 and Task Studio proof surfaces

- later proof packs should deepen these invariants rather than revise them.

## 11. Review notes

Human review should confirm that this pack:

- keeps proof attached to runs and shaped by run class,
- makes uncertainty, omission, contradiction, and replay basis explicit,
- preserves inspectable failure handling,
- avoids overreaching into full evaluation machinery that belongs later.
