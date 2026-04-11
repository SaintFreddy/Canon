# Phase 5 full proof, validation, and evaluation spec
Version: 1.0
Status: Accepted
Task: P5.2 — Full proof / validation / evaluation spec
Artifact ID: reuse.phase5-proof-validation-evaluation-spec.v1
Reuse scope: Accepted machine-usable proof pack for verifier packs, proof assembly, scoring/rubric rules, evaluation fixtures, replay/regression suites, and task-family proof sections

## 1. Purpose

This pack turns the accepted invariant proof layer and accepted Phase 5 governance boundary into the full operational proof, validation, and evaluation spec.

It exists to:

- define how verifier packs, proof assembly, scoring, and failure handling become machine-usable,
- make replay, regression, and Task Studio proof continuity explicit instead of relying on ad hoc review judgment,
- lock the operational proof sections that later protocol packs, reusable execution specs, and Task Studio surfaces must project unchanged.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- verifier-pack and evaluator contract rules,
- proof assembler inputs, outputs, and assembly constraints,
- scoring thresholds, pass/fail rubrics, and detailed failure taxonomy,
- evaluation fixtures and benchmark dataset rules,
- replay/regression suite rules,
- task-family proof and evaluator sections for every base run class,
- proof continuity through R7 and into Task Studio.

### Out of scope

- domain-specific business evaluators,
- org-local scoring policies outside the shared threshold profile shape,
- UI layout details for ledgers, inspectors, or dashboards,
- protocol-specific intake/result schemas,
- repo/package implementation details beyond accepted architecture contracts.

## 3. Proof and evaluation interpretation rules

### 3.1 Invariant-preservation rule

`reuse.phase2-proof-validation-invariants.v1`, `reuse.phase2-governance-authority-writeback-invariants.v1`, `reuse.phase5-governance-authority-writeback-spec.v1`, and `rel.r7-commissioning-bridge-contract.v1` remain binding.
`PI-01` through `PI-10`, `RC-01` through `RC-08`, and the governance-fit constraints around proof stay in force as the minimum floor for this deeper pack.

### 3.2 Proof-attaches-to-run rule

Proof is a structured object attached to one `run_id`.
Verifier results, ledger views, monitor summaries, and approval decisions may project or consume proof, but they may not replace the Proof Bundle as the authoritative evaluation object.

### 3.3 Frozen-basis and blocking-failure rule

Replay, regression, background parity, and Task Studio continuity all use frozen admitted basis and create new historical records.
Missing basis, unresolved authority/policy violations, required validator failures, or uninspected execution failures remain explicit blocking states rather than being narrated away.

## 4. Verifier-pack and evaluator contract model

### 4.1 Contract elements

| Element | Contract |
| --- | --- |
| Verifier Pack | Versioned evaluator contract naming run-class scope, slot definitions, threshold profile, fixture-set refs, and failure mappings |
| Verifier Slot | One required or advisory evaluation position with named inputs, severity, rubric dimension, and failure mapping |
| Threshold Profile | Numeric minima and target scores per slot severity plus pack-level outcome rules |
| Evaluator Result | Slot-level outcome record carrying score, outcome band, failure refs, evidence refs, and rationale refs |
| Evaluation Summary | Pack-level `pass`, `pass_with_warnings`, `fail`, or `blocked` result derived from slot outcomes rather than prose or approval state |

### 4.2 Outcome-band semantics

| Outcome band | Meaning | Pack-level posture |
| --- | --- | --- |
| `pass` | All required blocking slots meet threshold and no blocking failure class remains | Eligible for normal downstream review/acceptance |
| `pass_with_warnings` | Blocking slots pass but advisory deficits, unresolved non-blocking uncertainty, or warning-level evaluator findings remain | Proof stays usable but warnings must remain visible |
| `fail` | At least one blocking slot misses threshold or a blocking failure class is triggered | Result may not masquerade as accepted proof |
| `blocked` | Required basis, authority/policy gate, or required evaluator execution is missing before normal scoring can complete | No consequential acceptance or apply path may proceed |

## 5. Proof assembler contract

### 5.1 Assembly inputs and outputs

| Input or output family | Required? | Role |
| --- | --- | --- |
| `run_ref` and `run_class` | Yes | Anchor proof to one consequential run and task family |
| Frozen admitted basis refs (`input_snapshot_ref`, evidence/context refs, lineage refs) | Yes | Preserve traceability back to the exact basis under evaluation |
| Protocol / proof-policy / verifier-pack refs | Yes | Select the proof shape, slot set, and threshold profile |
| Validator and evaluator results | Yes when slots are required | Provide slot-level outcomes that the assembler must embed rather than summarize away |
| `uncertainty_items`, `omission_items`, `contradiction_items` | Yes when relevant | Keep non-settled or incomplete basis explicit |
| `state_delta_ref` and linked writeback refs | Yes for consequential work; delta always required | Preserve governance fit and change visibility |
| Failure diagnostics and adapter refs | Conditional but mandatory on failure | Keep `PI-10` failure inspectability explicit |
| Proof Bundle output | Yes | Terminal authoritative proof object |
| Evaluation Summary output | Yes | Machine-usable overall proof/evaluator verdict linked into the bundle |

### 5.2 Assembly rules

1. Every terminal run emits exactly one Proof Bundle and one State Delta, including failed and no-op runs.
2. The assembler may use only the frozen admitted basis plus linked evaluator outputs; it may not invent unstated basis or fill gaps from transcript convenience.
3. Evaluator results attach to proof as structured records, not just aggregate prose or hidden logs.
4. Review, Approval Decision, and Writeback Proposal refs may be linked from proof, but proof may not replace those governance objects.
5. A failed or blocked run still emits proof/failure basis, delta state, and evaluator/validator posture sufficient for replay, audit, and regression inspection.

## 6. Scoring thresholds, pass/fail rubrics, and detailed failure taxonomy

### 6.1 Default threshold profile

| Threshold profile rule | Contract |
| --- | --- |
| Blocking slot minimum | `score >= 0.80` is required to pass a blocking slot |
| Blocking slot target | `score >= 0.90` is the expected stable target for a healthy implementation |
| Advisory slot minimum | `score >= 0.70` keeps the slot warning-level instead of fail-level |
| Pack `pass` | All blocking slots meet minimum and no blocking failure class is present |
| Pack `pass_with_warnings` | All blocking slots meet minimum, but one or more advisory slots miss target or warning-only proof issues remain explicit |
| Pack `fail` | Any blocking slot misses minimum or a blocking failure class is triggered |
| Pack `blocked` | Required basis, authority/policy gate, or required evaluator execution is missing before normal scoring |

### 6.2 Shared rubric dimensions

| Rubric dimension | What it measures | Applies most strongly to |
| --- | --- | --- |
| Basis fidelity | Whether proof stays anchored to the frozen admitted basis and target refs | All run classes |
| Schema/result fit | Whether result and proof satisfy declared protocol/result shapes | `extract`, `transform`, `triage` |
| Coverage and completeness | Whether material evidence, fields, targets, or options are covered | `synthesize`, `extract`, `compare`, `audit` |
| Uncertainty and contradiction discipline | Whether uncertainty, omissions, and contradictions remain explicit and correctly handled | All run classes |
| Lineage and change safety | Whether proposed changes, comparisons, or branches preserve explicit lineage and risk basis | `transform`, `compare`, `plan` |
| Governance and policy fit | Whether proof stays inside authority, review, and writeback boundaries | `transform`, `audit`, `triage` |
| Recommendation or routing quality | Whether the recommended path is explicit, class-fit, and justified | `compare`, `plan`, `triage` |

### 6.3 Detailed failure taxonomy

| Detailed failure code | Parent invariant failure class | Meaning |
| --- | --- | --- |
| `basis_ref_missing` | `intake_or_scope_insufficient` | Required frozen basis or target refs are missing |
| `schema_contract_violation` | `proof_shape_violation` | Returned proof/result does not satisfy the declared schema or section contract |
| `coverage_below_minimum` | `evidence_or_coverage_insufficient` | Required coverage falls below the stated objective or fixture expectation |
| `material_omission_unhandled` | `material_omission_unhandled` | Material omission remains visible but unresolved for the claimed acceptance posture |
| `material_contradiction_unresolved` | `material_contradiction_unresolved` | Material contradiction remains unresolved while the result implies settlement |
| `validator_slot_missing` | `validator_failure` | A required verifier slot did not run or did not attach a result |
| `validator_slot_failed` | `validator_failure` | A required verifier slot ran and failed |
| `authority_boundary_violated` | `authority_or_policy_violation` | Proof path exceeds the approved authority boundary |
| `policy_boundary_violated` | `authority_or_policy_violation` | Proof or evaluation bypasses declared policy or routing rules |
| `lineage_trace_missing` | `replay_basis_invalid` | Required lineage or replay/compare trace is missing or invalid |
| `comparison_target_unbound` | `comparison_basis_invalid` | Compare work lacks explicit target identity or axis binding |
| `adapter_failure_unexplained` | `execution_or_adapter_failure` | Execution or adapter failure occurred without inspectable proof/failure basis |

## 7. Evaluation fixtures and benchmark dataset model

### 7.1 Fixture contract families

| Fixture family | Required basis | Primary purpose |
| --- | --- | --- |
| Golden-scenario fixture | Scenario ref, frozen inputs, expected proof sections, expected score band | Prove nominal accepted behavior on named scenarios |
| Edge-case fixture | Edge-case ref, frozen inputs, expected blocking or warning posture | Ensure failure and warning behavior stays explicit |
| Regression fixture | Prior accepted run/proof refs plus frozen basis | Protect against semantic drift over time |
| Background-parity fixture | Interactive and background equivalents plus parity expectations | Enforce `RC-07` across governed/background projections |
| Handoff-continuity fixture | R7 handoff payload refs plus Task Studio continuity expectations | Enforce `GS-14` and `EC-07` continuity |

### 7.2 Dataset rules

1. Every fixture set and benchmark dataset is versioned and frozen; updates create new dataset versions instead of mutating prior expectations.
2. Dataset records must retain run-class coverage, expected proof sections, expected evaluator posture, and linked scenario/edge-case refs.
3. Benchmark or fixture results may be derived views, but their rebuild path must remain traceable to authoritative frozen inputs and evaluator outputs.

## 8. Replay and regression suite model

| Suite type | Required basis | Expected invariant | Failure triggers |
| --- | --- | --- | --- |
| `exact_replay` | Same frozen inputs, same protocol/version, same authority scope | New run/proof/delta records preserve basis continuity | `basis_ref_missing`, `lineage_trace_missing`, `adapter_failure_unexplained` |
| `updated_source_replay` | Updated source refs plus explicit changed-basis declaration | Proof makes changed basis explicit instead of claiming parity | `material_omission_unhandled`, `replay_basis_invalid` |
| `branch_compare_parity` | Explicit compare targets, axes, and branch/checkpoint refs | Compare proof names targets, differences, and recommendation basis | `comparison_target_unbound`, `comparison_basis_invalid` |
| `background_parity` | Interactive/background equivalent protocol/applet context | Same proof and authority minima hold in background execution | `validator_slot_missing`, `authority_boundary_violated`, `RC-07` breach |
| `handoff_continuity` | R7 payload refs and Task Studio-opened object refs | Shared IDs and proof links survive the handoff unchanged | `EC-07`, `lineage_trace_missing` |

## 9. Task-family proof and evaluation sections

### 9.1 `compare`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Explicit target refs, axes, material differences, recommendation basis, uncertainty/omission | 2 slots minimum | Target binding, difference fidelity, recommendation quality | Branch compare, pack diff, adaptation compare |

### 9.2 `synthesize`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Claim-to-evidence map, coverage notes, contradiction capture, uncertainty/omission, result summary | 2 slots minimum | Grounding, coverage completeness, contradiction discipline | Bounded answer, contextual answer, commissioned synthesis |

### 9.3 `extract`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Field-to-span map, normalization notes, missing-field handling, schema/result fit | 2 slots minimum | Span fidelity, schema fit, omission handling | Structured extraction, source field capture |

### 9.4 `transform`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Lineage basis, desired-change -> proposed-change trace, validation results, risk notes, governance fit | 3 slots minimum | Change safety, lineage fidelity, policy fit | Artifact revision, prompt adaptation, writeback proposal generation |

### 9.5 `audit`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Criteria-evaluation matrix, pass/fail/exception basis, evidence refs, contradiction capture | 2 slots minimum | Criteria completeness, evidence quality, exception handling | Review queue, proof ledger inspection, policy audit |

### 9.6 `plan`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Assumption set, dependency map, option tradeoffs, branch/checkpoint rationale | 2 slots minimum | Assumption traceability, option quality, branch continuity | Branch planning, alternate-assumption plans |

### 9.7 `triage`

| Required proof sections | Verifier floor | Primary evaluator focus | Fixture focus |
| --- | --- | --- | --- |
| Intake completeness, routing basis, scope/authority gap notes, risk basis, downstream recommended run class | 2 slots minimum | Routing correctness, scope-gap visibility, commissioning fit | Commission preflight, Task Studio intake |

## 10. Scenario and shortcut grounding

| Proof/evaluation area | Strongest scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| Source tracing and frozen-basis proof | `GS-01`, `GS-02`, `GS-03`, `EC-10` | `fs.no-master-chat-truth`, `fs.no-transcript-first-rewrite-trap` |
| Branch/replay/compare proof | `GS-04`, `GS-05`, `EC-01` | `fs.no-transcript-first-rewrite-trap`, `fs.no-separate-backend-per-view` |
| Prompt/adaptation and governed reuse proof | `GS-08`, `GS-09`, `GS-10`, `EC-04`, `EC-05` | `fs.no-separate-backend-per-view`, `fs.no-agent-builder-first` |
| Commissioning, writeback, and Task Studio continuity proof | `GS-12`, `GS-13`, `GS-14`, `EC-06`, `EC-07` | `fs.no-master-chat-truth`, `fs.no-silent-proposal-application` |
| Memory/canon/governance-fit proof | `GS-07`, `GS-11`, `GS-15`, `EC-03` | `fs.no-hidden-memory-sludge`, `fs.no-silent-proposal-application` |

## 11. Boundary locks for downstream work

1. `P5.3` protocol packs must bind verifier-pack refs, proof assembler rules, threshold profiles, failure classes, and fixture sets explicitly instead of inventing per-protocol proof semantics.
2. `P5.4` reusable-execution composition specs must preserve the same proof/evaluator minima in workflow, trigger, applet, and background execution contexts.
3. `P5.5` and `P5.7` must project Proof Bundle, Evaluator Result, regression status, and handoff continuity without creating a second proof truth model.
4. Governance, architecture, or package work may not hide required validator results only in logs or transient monitor state.

## 12. Downstream implications

### 12.1 For P5.3

- protocol packs should attach explicit verifier packs, proof assemblers, threshold profiles, fixture refs, and failure mappings to each run class rather than re-deriving them.

### 12.2 For P5.4 through P5.7 and Task Studio

- reusable execution specs and Task Studio packs should use this spec as the operational proof baseline for background parity, ledger views, regression suites, and handoff continuity.

## 13. Review notes

Human review should confirm that this pack:

- makes verifier/evaluator structure machine-usable,
- keeps proof attached to runs and frozen basis,
- makes replay, regression, and Task Studio continuity explicit,
- preserves governance-fit and failure inspectability without inventing a second proof ontology.

