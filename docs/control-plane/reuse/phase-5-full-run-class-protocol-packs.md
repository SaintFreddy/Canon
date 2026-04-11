# Phase 5 full run-class protocol packs
Version: 1.0
Status: Accepted
Task: P5.3 — Full run-class protocol packs
Artifact ID: reuse.phase5-run-class-protocol-packs.v1
Reuse scope: Accepted machine-usable run-class protocol pack covering per-class schemas, context/strategy bindings, verifier packs, governance defaults, failure mappings, and fixtures

## 1. Purpose

This pack turns the accepted run-class taxonomy plus the accepted Phase 5 governance and proof layers into the full operational protocol-pack baseline.

It exists to:

- bind each base run class to a versioned protocol contract instead of leaving reusable execution as a loose prompt or applet convention,
- make intake schema, contract schema, result schema, proof schema, Context Recipe, Strategy Preset, verifier pack, failure classes, and fixture bindings explicit per run class,
- lock the conservative authority, side-effect, review-hook, and writeback posture that later reusable-execution and Task Studio work must project unchanged.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- full protocol-pack specialization for all seven accepted base run classes,
- intake, contract, result, and proof schema refinements beyond the P2.2 skeleton,
- Context Recipe and Strategy Preset contract expectations for each run class,
- verifier-pack, threshold-profile, failure-class, and fixture bindings per run class,
- authority defaults, side-effect preview posture, review hooks, and writeback defaults per run class,
- protocol versioning and lifecycle rules required for reusable execution and Task Studio continuity.

### Out of scope

- Workflow, Trigger, Applet, Pack, or Integration composition semantics beyond referencing the protocol packs,
- org-local or domain-local protocol variants,
- UI layout or interaction design for Queue, Monitor, Inspector, or Task Studio surfaces,
- runtime implementation details outside the accepted architecture contracts.

## 3. Protocol-pack interpretation rules

### 3.1 Invariant-preservation rule

`sem.phase2-run-class-taxonomy-protocol-kernel.v1`, `reuse.phase5-governance-authority-writeback-spec.v1`, `reuse.phase5-proof-validation-evaluation-spec.v1`, `rel.r6-governed-agent-applet-chat-contract.v1`, and `rel.r7-commissioning-bridge-contract.v1` remain binding.
`GI-01` through `GI-10`, `PI-01` through `PI-10`, and `RC-07` remain the minimum contract floor for this deeper pack.
This pack deepens them; it does not revise or bypass them.

### 3.2 Protocol-pack-not-new-ontology rule

A protocol pack specializes the accepted `Protocol` object for one accepted `run_class`.
Context Recipe, Strategy Preset, Verifier Pack, Workflow, Trigger, Applet, and Task Studio projections may consume protocol packs, but they may not replace run-class meaning, invent a second reusable-execution ontology, or translate object identity during R7 -> Task Studio handoff.

### 3.3 Conservative-default and single-lane rule

Protocol packs stay conservative by default:

- read-first unless the accepted run class already allows a tighter writable default,
- no hidden widening through Context Recipe, Strategy Preset, applet settings, or background execution,
- no mixed-lane writeback defaults,
- no memory, canon, workflow, or export write default in a run-class pack,
- only `transform` may default to artifact-lane proposal posture.

### 3.4 Versioned-specialization rule

Material change to required fields, verifier-slot severity, threshold posture, authority/writeback default, failure mappings, fixture expectations, or handoff guarantees increments `protocol_version`.
Background execution, replay, and Task Studio handoff preserve the originating `protocol_id`, `protocol_version`, and `run_class` instead of silently retargeting work to a new contract.

## 4. Cross-run-class summary

| Run class | Protocol pack | Primary contract outcome | Authority default | Writeback default | Verifier floor | Primary fixture focus |
| --- | --- | --- | --- | --- | --- | --- |
| `compare` | `protocol.compare.core@1.0.0` | Ranked differences and recommendation basis over explicit targets | Read-only evidence/context/artifact access | `none` | 2 blocking slots + advisory coverage | Branch compare, adaptation compare, Task Studio compare |
| `synthesize` | `protocol.synthesize.core@1.0.0` | Bounded answer or draft grounded in explicit evidence | Read-only evidence/context access | `none` unless contracted artifact proposal | 2 blocking slots + contradiction discipline | Bounded answer, contextual draft, commissioned synthesis |
| `extract` | `protocol.extract.core@1.0.0` | Structured record plus field/span mapping | Read-only evidence/context access | `none` unless contracted artifact proposal | 2 blocking slots + advisory normalization | Structured extraction and source capture |
| `transform` | `protocol.transform.core@1.0.0` | Candidate revision or change-set over an explicit target artifact | Artifact-target read plus artifact proposal authority | `artifact` only | 3 blocking slots | Artifact revision, prompt adaptation, proposal generation |
| `audit` | `protocol.audit.core@1.0.0` | Findings plus pass/fail/exception basis | Read-only target/policy access | `none` | 2 blocking slots + contradiction/exception handling | Policy audit, ledger review, acceptance inspection |
| `plan` | `protocol.plan.core@1.0.0` | Plan, option set, checkpoints, or branch recommendations | Read-only evidence/context/branch access | `none` | 2 blocking slots + advisory branch consistency | Branch planning and alternate-assumption plans |
| `triage` | `protocol.triage.core@1.0.0` | Recommended downstream run class, scope summary, and contract draft basis | Intake and routing only | `none` | 3 blocking slots | Commission preflight and Task Studio intake |

## 5. Shared protocol-pack contract model

### 5.1 Required protocol-pack elements

| Element | Contract |
| --- | --- |
| `protocol_id` + `protocol_version` | Stable protocol identity plus semantic version for one run class; reusable execution must pin both |
| `run_class` | One accepted base run class from `sem.phase2-run-class-taxonomy-protocol-kernel.v1` |
| `intake_schema_ref` | Named schema contract for admitted inputs, frozen basis refs, and scope-bearing refs |
| `contract_schema_ref` | Named schema contract for the governing Contract fields when commissioned or consequential work is in play |
| `result_schema_ref` | Named schema contract for class-specific outputs, proof/delta refs, and any optional proposal refs |
| `proof_schema_ref` | Named schema contract for class-specific proof sections that bind into the shared P5.2 proof model |
| `proof_policy_ref` | Binding to the shared proof-assembler, threshold-profile, and failure-taxonomy rules applied to the class-specific proof schema |
| `context_recipe_ref` | Named Context Recipe that selects the exact admitted basis, compilation order, and explicit exclusions |
| `strategy_preset_ref` | Named Strategy Preset that constrains execution order, refusal posture, and verifier emphasis without widening authority |
| `verifier_pack_ref` | Named Verifier Pack carrying slot set, slot severity, rubric focus, and threshold profile |
| `authority_default` | Conservative default read/write envelope derived from the accepted run class |
| `side_effect_default` | Default side-effect class for tool use during protocol execution; never hides external-write risk |
| `review_hook_set` | Named review-trigger vocabulary indicating which P5.1 approval paths can be activated |
| `writeback_default` | Default lane posture: `none` or one explicit lane only |
| `failure_class_set` | Named subset of the accepted detailed failure taxonomy that the protocol pack uses as first-line failure mapping |
| `fixture_set_ref` | Named fixture family bundle for golden, edge-case, regression, background-parity, and handoff-continuity tests |

### 5.2 Versioning and lifecycle rules

1. `protocol_id` stays stable while `protocol_version` carries material semantic change.
2. Backward-incompatible field, proof, governance, or fixture changes require a new major version.
3. Additive optional fields or advisory slots may increment the minor version only when older runs remain interpretable without semantic ambiguity.
4. Clarification-only changes that do not alter runtime meaning, review posture, or verifier expectations may increment the patch version.
5. Workflow, Trigger, Applet, or Task Studio projections pin an exact `protocol_version`; they may not silently float to a newer version.
6. Domain-specific overlays must derive from these base pack contracts rather than mutating them in place.

### 5.3 Shared governance and proof binding rules

1. Every protocol pack binds `proof_policy_ref` to the shared P5.2 proof assembler rules, the default threshold profile, and the class-specific proof schema below.
2. Every protocol intake requires `objective_spec` and `input_snapshot_ref`.
3. `authority_scope_ref` is mandatory whenever the protocol reads beyond the default wedge or proposes writable behavior.
4. `contract_ref` is mandatory whenever the run is commissioned or requests writable behavior beyond the base default.
5. Context Recipes may assemble only explicit frozen refs and allowed policy/context inputs; they may not pull hidden transcript truth or ambient memory.
6. Strategy Presets may narrow ordering, refusal posture, and verifier emphasis, but they may not widen authority, suppress contradictions, or bypass verifier slots.
7. `reversible_external_write` or `irreversible_external_write` side effects are never default protocol posture; they require explicit contract, authority, review hooks, and lane-local policy outside the base run-class default.

### 5.4 Review-hook vocabulary

| Review hook | Meaning |
| --- | --- |
| `scope_widening_review` | Authority or source-access widening must route through the P5.1 scope-widening path before the next consequential run |
| `artifact_lane_apply_review` | Artifact-lane proposal application requires explicit Review and Approval Decision objects |
| `memory_lane_apply_review` | Memory-lane proposal application requires explicit lane-local review; never a protocol default |
| `canon_promotion_review` | Canon promotion requires explicit acceptance-basis review; never a protocol default |
| `workflow_export_apply_review` | Workflow or export apply paths require explicit lane-local review; never a protocol default |
| `background_enablement_review` | Writable background enablement requires the explicit P5.1 approval path before Applet/Trigger enablement |
| `compensation_review` | Compensation or superseding action requires explicit follow-up review rather than silent undo |

## 6. Run-class protocol packs

### 6.1 `compare`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.compare.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.compare.policy.v1` binding `schema.compare.proof.v1`, `verifier.compare.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.compare.intake.v1` | `objective_spec`, `comparison_target_refs`, `evidence_pack_ref`, `context_pack_ref?`, `branch_ref?`, `input_snapshot_ref`, `authority_scope_ref?`, `contract_ref?` |
| Contract schema | `schema.compare.contract.v1` | `comparison_axes`, `materiality_policy`, `ranking_policy?`, `recommendation_shape`, `acceptance_policy_ref?`, `external_read_policy?` |
| Result schema | `schema.compare.result.v1` | `difference_set`, `ranking_or_recommendation`, `proof_bundle_ref`, `state_delta_ref`, `artifact_candidate_ref?` |
| Proof schema | `schema.compare.proof.v1` | `comparison_axes`, `evidence_refs`, `material_differences`, `recommendation_basis`, `uncertainty_items`, `omission_items`, `contradiction_items?`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.compare.evidence-first.v1` — bind explicit targets and axes first, compile only admitted evidence/context/branch refs, exclude ambient transcript and memory state |
| Strategy Preset | `strategy.compare.bind-diff-rank.v1` — bind targets -> compute material differences -> rank or recommend only after coverage and uncertainty capture |
| Verifier Pack | `verifier.compare.core.v1` — `diff_alignment` (blocking), `source_parity` (blocking), `coverage` (advisory); threshold `threshold.default.v1` |
| Failure class set | `failure.compare.core.v1` — `comparison_target_unbound`, `basis_ref_missing`, `coverage_below_minimum`, `material_omission_unhandled`, `validator_slot_failed` |
| Fixture set | `fixture.compare.core.v1` — golden branch compare, prompt/adaptation compare, background parity compare, handoff continuity compare |
| Authority default | Read-only evidence/context/artifact access only |
| Side-effect default | `none`; `read_only_external` only when admitted external read sources are explicit |
| Review hook set | `scope_widening_review`; no apply review by default |
| Writeback default | `none`; artifact-lane proposal only when separately contracted and reviewed |

### 6.2 `synthesize`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.synthesize.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.synthesize.policy.v1` binding `schema.synthesize.proof.v1`, `verifier.synthesize.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.synthesize.intake.v1` | `objective_spec`, `evidence_pack_ref`, `context_pack_ref`, `artifact_ref?`, `branch_ref?`, `input_snapshot_ref`, `authority_scope_ref?`, `contract_ref?` |
| Contract schema | `schema.synthesize.contract.v1` | `deliverable_shape`, `coverage_expectation`, `style_constraints?`, `artifact_candidate_policy`, `acceptance_policy_ref?`, `external_read_policy?` |
| Result schema | `schema.synthesize.result.v1` | `synthesized_result`, `artifact_candidate_ref?`, `proof_bundle_ref`, `state_delta_ref` |
| Proof schema | `schema.synthesize.proof.v1` | `claim_to_evidence_map`, `coverage_notes`, `result_boundary_notes`, `uncertainty_items`, `contradiction_items`, `omission_items`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.synthesize.evidence-grounded.v1` — compile objective, frozen evidence, bounded context, and explicit output-shape constraints while excluding hidden memory or unbound targets |
| Strategy Preset | `strategy.synthesize.ground-then-compose.v1` — gather evidence -> compose bounded result -> run contradiction and omission checks before returning prose or draft output |
| Verifier Pack | `verifier.synthesize.core.v1` — `grounding` (blocking), `coverage` (blocking), `contradiction_check` (blocking when contradictions exist, otherwise advisory) |
| Failure class set | `failure.synthesize.core.v1` — `basis_ref_missing`, `coverage_below_minimum`, `material_contradiction_unresolved`, `material_omission_unhandled`, `validator_slot_failed` |
| Fixture set | `fixture.synthesize.core.v1` — bounded answer, contextual answer, commissioned synthesis, background parity synthesis |
| Authority default | Read-only evidence/context access only |
| Side-effect default | `none`; `read_only_external` only when the admitted basis includes external reads |
| Review hook set | `scope_widening_review`; `artifact_lane_apply_review` only when a separate artifact proposal path is explicitly contracted |
| Writeback default | `none`; artifact-lane proposal only when contracted |

### 6.3 `extract`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.extract.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.extract.policy.v1` binding `schema.extract.proof.v1`, `verifier.extract.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.extract.intake.v1` | `objective_spec`, `evidence_pack_ref`, `extraction_schema_ref`, `context_pack_ref?`, `input_snapshot_ref`, `authority_scope_ref?`, `contract_ref?` |
| Contract schema | `schema.extract.contract.v1` | `required_fields`, `normalization_policy`, `missing_field_policy`, `artifact_candidate_policy?`, `acceptance_policy_ref?`, `external_read_policy?` |
| Result schema | `schema.extract.result.v1` | `structured_record`, `field_span_map`, `artifact_candidate_ref?`, `proof_bundle_ref`, `state_delta_ref` |
| Proof schema | `schema.extract.proof.v1` | `field_to_span_map`, `normalization_notes`, `missing_field_list`, `schema_fit_notes`, `uncertainty_items`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.extract.schema-first.v1` — compile the extraction schema, source spans, allowed normalization refs, and frozen source basis while excluding generative fill-in outside the admitted record |
| Strategy Preset | `strategy.extract.field-trace.v1` — walk fields in schema order -> capture spans -> normalize explicitly -> surface missing fields instead of inventing values |
| Verifier Pack | `verifier.extract.core.v1` — `traceability` (blocking), `field_completeness` (blocking), `normalization_check` (advisory) |
| Failure class set | `failure.extract.core.v1` — `basis_ref_missing`, `schema_contract_violation`, `coverage_below_minimum`, `material_omission_unhandled`, `validator_slot_failed` |
| Fixture set | `fixture.extract.core.v1` — structured extraction, source field capture, regression extraction, handoff continuity extraction |
| Authority default | Read-only evidence/context access only |
| Side-effect default | `none`; `read_only_external` only when external source reads are explicitly admitted |
| Review hook set | `scope_widening_review`; `artifact_lane_apply_review` only when a separate artifact proposal is explicitly contracted |
| Writeback default | `none`; artifact-lane proposal only when contracted |

### 6.4 `transform`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.transform.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.transform.policy.v1` binding `schema.transform.proof.v1`, `verifier.transform.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.transform.intake.v1` | `objective_spec`, `target_artifact_ref`, `desired_change_spec`, `evidence_pack_ref?`, `context_pack_ref?`, `input_snapshot_ref`, `authority_scope_ref`, `contract_ref?` |
| Contract schema | `schema.transform.contract.v1` | `allowed_operation_set`, `validation_gate_refs`, `artifact_revision_policy`, `risk_tolerance`, `apply_requires_review`, `acceptance_policy_ref`, `external_side_effect_policy?` |
| Result schema | `schema.transform.result.v1` | `proposed_change_set`, `candidate_revision_ref`, `writeback_proposal_ref?`, `proof_bundle_ref`, `state_delta_ref` |
| Proof schema | `schema.transform.proof.v1` | `lineage_basis`, `desired_change_to_operation_trace`, `validation_results`, `risk_notes`, `policy_fit_notes`, `uncertainty_items`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.transform.target-lineage.v1` — compile target artifact current revision, lineage chain, desired change, evidence/context basis, and validation rules while excluding hidden durable-state mutation |
| Strategy Preset | `strategy.transform.plan-validate-propose.v1` — establish baseline -> shape bounded change set -> validate -> emit candidate revision and explicit proposal/delta state |
| Verifier Pack | `verifier.transform.core.v1` — `lineage_guard` (blocking), `change_safety` (blocking), `policy_check` (blocking) |
| Failure class set | `failure.transform.core.v1` — `basis_ref_missing`, `schema_contract_violation`, `authority_boundary_violated`, `policy_boundary_violated`, `lineage_trace_missing`, `validator_slot_failed` |
| Fixture set | `fixture.transform.core.v1` — artifact revision, prompt adaptation, proposal generation, background parity transform |
| Authority default | Artifact-target read plus artifact-lane proposal authority only |
| Side-effect default | `none` for proposal generation; `read_only_external` only for admitted validation reads; `reversible_external_write` and `irreversible_external_write` require explicit non-default contract/authority and lane-local review |
| Review hook set | `scope_widening_review`, `artifact_lane_apply_review`, `compensation_review`; other lane-apply hooks only when split into separate explicit proposals |
| Writeback default | `artifact` only |

### 6.5 `audit`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.audit.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.audit.policy.v1` binding `schema.audit.proof.v1`, `verifier.audit.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.audit.intake.v1` | `objective_spec`, `audit_target_refs`, `criteria_ref`, `evidence_pack_ref?`, `context_pack_ref?`, `input_snapshot_ref`, `authority_scope_ref?`, `contract_ref?` |
| Contract schema | `schema.audit.contract.v1` | `severity_policy`, `exception_policy`, `sampling_policy?`, `acceptance_policy_ref?`, `external_read_policy?` |
| Result schema | `schema.audit.result.v1` | `finding_set`, `pass_fail_exception_summary`, `review_ref?`, `proof_bundle_ref`, `state_delta_ref` |
| Proof schema | `schema.audit.proof.v1` | `criteria_evaluation_matrix`, `exception_items`, `evidence_refs`, `contradiction_items`, `uncertainty_items`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.audit.criteria-first.v1` — compile criteria, targets, frozen evidence, and policy refs while excluding implied remediation or silent target mutation |
| Strategy Preset | `strategy.audit.evaluate-exceptions.v1` — evaluate criterion by criterion -> capture pass/fail/exception basis -> surface contradictions and uncertainty instead of settling them narratively |
| Verifier Pack | `verifier.audit.core.v1` — `policy_check` (blocking), `exception_capture` (blocking), `contradiction_check` (advisory unless contradictions remain material) |
| Failure class set | `failure.audit.core.v1` — `basis_ref_missing`, `coverage_below_minimum`, `material_contradiction_unresolved`, `policy_boundary_violated`, `validator_slot_failed` |
| Fixture set | `fixture.audit.core.v1` — policy audit, proof-ledger inspection, review-queue inspection, regression audit |
| Authority default | Read-only target/policy access only |
| Side-effect default | `none`; `read_only_external` only when external policy or evidence reads are admitted |
| Review hook set | `scope_widening_review`; downstream `artifact_lane_apply_review` or `canon_promotion_review` only when remediation or canon action is split into a separate explicit proposal/review path |
| Writeback default | `none` |

### 6.6 `plan`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.plan.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.plan.policy.v1` binding `schema.plan.proof.v1`, `verifier.plan.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.plan.intake.v1` | `objective_spec`, `planning_scope_ref`, `evidence_pack_ref?`, `context_pack_ref?`, `branch_ref?`, `input_snapshot_ref`, `authority_scope_ref?`, `contract_ref?` |
| Contract schema | `schema.plan.contract.v1` | `planning_horizon`, `option_floor`, `checkpoint_policy`, `dependency_depth`, `branch_policy`, `acceptance_policy_ref?` |
| Result schema | `schema.plan.result.v1` | `plan_steps`, `option_set`, `checkpoint_refs?`, `branch_recommendations?`, `proof_bundle_ref`, `state_delta_ref` |
| Proof schema | `schema.plan.proof.v1` | `assumption_set`, `dependency_map`, `option_tradeoffs`, `branch_checkpoint_rationale`, `uncertainty_items`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.plan.assumption-branch.v1` — compile scope, assumptions, dependencies, branch/checkpoint refs, and explicit constraints while excluding hidden durable side effects |
| Strategy Preset | `strategy.plan.option-branch-check.v1` — enumerate assumptions -> build option set -> check dependencies -> preserve branch/checkpoint rationale explicitly |
| Verifier Pack | `verifier.plan.core.v1` — `assumption_coherence` (blocking), `dependency_check` (blocking), `branch_consistency` (advisory) |
| Failure class set | `failure.plan.core.v1` — `basis_ref_missing`, `coverage_below_minimum`, `material_omission_unhandled`, `lineage_trace_missing`, `validator_slot_failed` |
| Fixture set | `fixture.plan.core.v1` — branch planning, alternate-assumption plans, checkpoint planning, Task Studio plan continuity |
| Authority default | Read-only evidence/context/branch access only |
| Side-effect default | `none`; `read_only_external` only when admitted external planning reads are explicit |
| Review hook set | `scope_widening_review`; `workflow_export_apply_review` only when a later explicit workflow/export proposal is created |
| Writeback default | `none` |

### 6.7 `triage`

| Protocol field | Contract |
| --- | --- |
| `protocol_id` | `protocol.triage.core` |
| `protocol_version` | `1.0.0` |
| `proof_policy_ref` | `proof.triage.policy.v1` binding `schema.triage.proof.v1`, `verifier.triage.core.v1`, and `threshold.default.v1` |

| Surface | Ref | Required fields |
| --- | --- | --- |
| Intake schema | `schema.triage.intake.v1` | `objective_spec`, `commission_ref?`, `intake_material_refs`, `risk_inputs?`, `input_snapshot_ref`, `authority_scope_ref?` |
| Contract schema | `schema.triage.contract.v1` | `routing_policy`, `intake_completion_floor`, `priority_policy`, `scope_gap_policy`, `handoff_requirements`, `acceptance_policy_ref?` |
| Result schema | `schema.triage.result.v1` | `recommended_run_class`, `scope_summary`, `priority_risk_summary`, `contract_draft_ref?`, `proof_bundle_ref`, `state_delta_ref` |
| Proof schema | `schema.triage.proof.v1` | `intake_completeness`, `routing_basis`, `authority_gap_notes`, `risk_basis`, `uncertainty_items`, `verifier_results` |

| Execution and governance element | Ref or contract |
| --- | --- |
| Context Recipe | `context-recipe.triage.scope-gap.v1` — compile intake materials, commission/request context, risk inputs, and allowed downstream protocol candidates while excluding hidden scope assumptions |
| Strategy Preset | `strategy.triage.classify-escalate.v1` — verify intake completeness -> classify serious vs casual -> recommend downstream run class -> surface scope gaps and contract-draft needs explicitly |
| Verifier Pack | `verifier.triage.core.v1` — `scope_sufficiency` (blocking), `authority_sufficiency` (blocking), `routing_fit` (blocking) |
| Failure class set | `failure.triage.core.v1` — `basis_ref_missing`, `schema_contract_violation`, `material_omission_unhandled`, `authority_boundary_violated`, `validator_slot_failed` |
| Fixture set | `fixture.triage.core.v1` — commission preflight, scope-gap detection, commissioning escalation, Task Studio intake continuity |
| Authority default | Intake and routing authority only |
| Side-effect default | `none` |
| Review hook set | `scope_widening_review`; downstream contract/authority approval begins after triage, but triage itself has no apply hook |
| Writeback default | `none` |

## 7. Scenario and shortcut grounding

| Protocol-pack area | Strongest scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| Reusable protocol identity, Context Recipe, Strategy Preset, and background parity | `GS-10`, `GS-11`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-separate-backend-per-view` |
| Commissioning and triage continuity into Task Studio | `GS-12`, `GS-13`, `GS-14`, `EC-06`, `EC-07` | `fs.no-master-chat-truth`, `fs.no-silent-proposal-application` |
| Compare and plan task-family continuity | `GS-15`, `GS-16`, `EC-01` | `fs.no-separate-backend-per-view`, `fs.no-transcript-first-rewrite-trap` |
| Transform and writeback-safe protocolization | `GS-06`, `GS-08`, `GS-09`, `EC-03`, `EC-04` | `fs.no-silent-proposal-application`, `fs.no-agent-builder-first` |
| Frozen-basis and proof-bearing result continuity | `GS-01`, `GS-02`, `GS-03`, `EC-10` | `fs.no-master-chat-truth`, `fs.no-transcript-first-rewrite-trap` |

## 8. Boundary locks for downstream work

1. `P5.4` must compose Workflow, Trigger, Applet, Pack, and Integration specs from these accepted protocol-pack refs, schema refs, Context Recipe refs, Strategy Preset refs, verifier packs, and review-hook sets instead of inventing a separate reusable-execution model.
2. `P5.5` and `P5.7` must project `protocol_id`, `protocol_version`, `run_class`, proof bindings, review hooks, and writeback posture directly into Task Studio and commissioning/handoff flows.
3. Later domain-specific protocol overlays may narrow fields, fixtures, or advisory slots, but they may not widen authority, erase proof sections, or replace the accepted base run classes.
4. Background execution, replay, and Task Studio handoff must preserve shared IDs, frozen-basis lineage, and verifier minima; they may not relax `RC-07`.

## 9. Downstream implications

### 9.1 For P5.4

- reusable-execution composition specs should treat these packs as the authoritative protocol baseline for workflow stages, triggers, applet pinning, and packaged integration bindings,
- applet or workflow configuration may reference `Context Recipe` and `Strategy Preset` refs from this pack, but it may not redefine their semantic meaning.

### 9.2 For P5.5 through P5.7 and Task Studio

- Task Studio surfaces, commissioning flows, and handoff contracts should use this pack as the baseline for typed run-class selection, protocol version pinning, verifier/fixture expectations, and governance posture,
- downstream work should preserve the accepted mapping between Task Studio families and base run classes instead of introducing app-private protocol categories.

## 10. Review notes

Human review should confirm that this pack:

- makes reusable execution typed and versionable at the run-class level,
- binds governance and proof expectations into protocol packs instead of leaving them implicit,
- preserves conservative authority and single-lane writeback defaults,
- keeps background execution and Task Studio handoff inside the same shared run/protocol semantics.
