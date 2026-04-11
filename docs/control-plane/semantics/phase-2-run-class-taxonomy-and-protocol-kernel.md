# Phase 2 run-class taxonomy and protocol-kernel pack
Version: 1.0
Status: Accepted
Task: P2.2 — Run-class taxonomy + protocol kernel
Artifact ID: sem.phase2-run-class-taxonomy-protocol-kernel.v1
Semantic scope: Accepted base run classes, Task Studio task-family mapping, protocol-kernel skeletons, authority defaults, verifier slots, and writeback defaults

## 1. Purpose

This pack turns the P2.1 object model into a typed execution taxonomy.

It exists to:

- replace vague generic-task language with base run classes,
- map Task Studio task families onto shared run classes,
- define the minimum protocol-kernel skeleton that reusable execution will extend later.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- base run classes,
- V1 Task Studio task-family mapping,
- protocol-kernel required fields,
- intake/result/proof schema skeletons,
- authority defaults,
- verifier slots,
- writeback defaults.

### Out of scope

- full task-family proof packs,
- full governance invariants,
- full release-specific semantic packs,
- workflow/trigger/applet packaging detail,
- technical runtime/storage/API architecture.

## 3. Taxonomy rules

### 3.1 V1 mapping rule

Task Studio V1 uses a direct one-to-one mapping between task family and base run class:

- Compare -> `compare`
- Synthesize -> `synthesize`
- Extract -> `extract`
- Transform -> `transform`
- Audit -> `audit`
- Plan -> `plan`
- Triage -> `triage`

Later work may add subtypes under these classes, but V1 does not introduce a second parallel taxonomy.

### 3.2 Projection-not-class rule

The following are not run classes:

- branch/replay,
- background execution,
- Protocol/Applet packaging,
- chat mode projections,
- Task Studio surface arrangements.

These are projections, modifiers, or packaging forms over the run classes below.

### 3.3 Boundary decisions locked here

| Decision | Locked interpretation |
| --- | --- |
| `synthesize` vs `transform` | `synthesize` creates a bounded new result from evidence/context; `transform` changes an explicit target artifact or asset under governed scope |
| `synthesize` / `extract` write default | No durable writeback by default; artifact-lane proposal only when the contract explicitly asks for it |
| `transform` write default | Artifact-lane proposal is the only default-eligible write lane; memory/canon/export/workflow require explicit objective and authority |
| proof scope at P2.2 | P2.2 defines proof skeletons and verifier slots only; full proof packs arrive later |

### 3.4 Conservative-default rule

Authority and writeback defaults stay conservative:

- read-first by default,
- no hidden memory or canon promotion,
- no cross-lane mixed write default,
- no reusable agent/applet behavior before explicit verifier and authority semantics exist.

## 4. Base run-class taxonomy

| Run class | Task Studio family | Purpose | Typical target shape | Default authority | Default writeback | Default verifier slots |
| --- | --- | --- | --- | --- | --- | --- |
| `compare` | Compare | Contrast sources, artifacts, branches, or options | Comparison set / ranked differences / recommendation | `read_only` | `none` | `diff_alignment`, `source_parity`, `coverage` |
| `synthesize` | Synthesize | Produce a bounded answer or draft from evidence/context | Answer, summary, draft artifact candidate | `read_only` | `none` unless contract requests artifact proposal | `grounding`, `coverage`, `contradiction_check` |
| `extract` | Extract | Pull structured facts, spans, or fields from evidence | Structured record / field map / citation map | `read_only` | `none` unless contract requests artifact proposal | `traceability`, `field_completeness`, `normalization_check` |
| `transform` | Transform | Derive or revise an explicit target artifact or asset | Candidate revision / change set / proposal set | `artifact_write_proposal` | `artifact` by default | `lineage_guard`, `change_safety`, `policy_check` |
| `audit` | Audit | Evaluate a target against policy, contract, or criteria | Findings / pass-fail-exception set | `read_only` | `none` | `policy_check`, `exception_capture`, `contradiction_check` |
| `plan` | Plan | Shape strategy, options, assumptions, or branch structure | Plan / branch options / checkpoints | `read_only` | `none` | `assumption_coherence`, `dependency_check`, `branch_consistency` |
| `triage` | Triage | Classify intake and route work into commission/contract form | Recommended run class / scope summary / risk and priority | `intake_route_only` | `none` | `scope_sufficiency`, `authority_sufficiency`, `routing_fit` |

## 5. Run-class schema skeletons

| Run class | Intake schema skeleton | Result schema skeleton | Proof schema skeleton |
| --- | --- | --- | --- |
| `compare` | `objective_spec`, `comparison_target_refs`, `evidence_pack_ref`, `context_pack_ref?`, `branch_ref?`, `authority_scope_ref` | `difference_set`, `ranking_or_recommendation`, `proof_bundle_ref`, `state_delta_ref` | `comparison_axes`, `evidence_refs`, `material_differences`, `uncertainty_items`, `omission_items` |
| `synthesize` | `objective_spec`, `evidence_pack_ref`, `context_pack_ref`, `artifact_ref?`, `branch_ref?`, `authority_scope_ref` | `synthesized_result`, `artifact_candidate_ref?`, `proof_bundle_ref`, `state_delta_ref` | `claim_to_evidence_map`, `coverage_notes`, `uncertainty_items`, `contradiction_items`, `omission_items` |
| `extract` | `objective_spec`, `evidence_pack_ref`, `extraction_schema_ref`, `context_pack_ref?`, `authority_scope_ref` | `structured_record`, `field_span_map`, `artifact_candidate_ref?`, `proof_bundle_ref`, `state_delta_ref` | `field_to_span_map`, `normalization_notes`, `missing_field_list`, `uncertainty_items` |
| `transform` | `objective_spec`, `target_artifact_ref`, `desired_change_spec`, `evidence_pack_ref?`, `context_pack_ref?`, `contract_ref?`, `authority_scope_ref` | `proposed_change_set`, `candidate_revision_ref`, `writeback_proposal_ref?`, `proof_bundle_ref`, `state_delta_ref` | `lineage_basis`, `change_rationale`, `validation_results`, `risk_notes`, `uncertainty_items` |
| `audit` | `objective_spec`, `audit_target_refs`, `criteria_ref`, `evidence_pack_ref?`, `context_pack_ref?`, `authority_scope_ref` | `finding_set`, `pass_fail_exception_summary`, `review_ref?`, `proof_bundle_ref`, `state_delta_ref` | `criteria_evaluation_matrix`, `exception_items`, `evidence_refs`, `contradiction_items`, `uncertainty_items` |
| `plan` | `objective_spec`, `planning_scope_ref`, `evidence_pack_ref?`, `context_pack_ref?`, `branch_ref?`, `authority_scope_ref` | `plan_steps`, `option_set`, `checkpoint_refs?`, `branch_recommendations?`, `proof_bundle_ref`, `state_delta_ref` | `assumption_set`, `dependency_map`, `option_tradeoffs`, `uncertainty_items` |
| `triage` | `objective_spec`, `commission_ref?`, `intake_material_refs`, `risk_inputs?`, `authority_scope_ref?` | `recommended_run_class`, `scope_summary`, `priority_risk_summary`, `contract_draft_ref?`, `proof_bundle_ref`, `state_delta_ref` | `intake_completeness`, `routing_basis`, `authority_gap_notes`, `uncertainty_items` |

## 6. Task-family and release mapping

| Run class | Primary release/scenario fit | Task Studio role | Notes |
| --- | --- | --- | --- |
| `compare` | R3 compare/replay views, `GS-15` | Direct Compare family | Compare is semantic work, not just a UI diff |
| `synthesize` | R1-R2 bounded answers, R4 artifact drafting, `GS-01`, `GS-02`, `GS-03`, `GS-06` | Direct Synthesize family | Common early wedge class |
| `extract` | R1-R2 source/field capture, evidence shaping | Direct Extract family | Keeps structured capture distinct from synthesis |
| `transform` | R4 artifact proposals, R5 prompt adaptation, R6 protocolization inputs, `GS-06`, `GS-08`, `GS-09`, `GS-10` | Direct Transform family | Only base class with default artifact-write eligibility |
| `audit` | R4 review, R6 queue/inbox, R7 proof/delta inspection, `GS-07`, `GS-11`, `GS-13` | Direct Audit family | Evaluation, not comparison or synthesis |
| `plan` | R3 branch/assumption work, `GS-04`, `GS-16` | Direct Plan family | Branching is a modifier over planning runs, not a separate class |
| `triage` | R7 commissioning preflight, `GS-12` | Direct Triage family | Intake classification before downstream execution |

## 7. Protocol-kernel contract

### 7.1 Required protocol-kernel fields

The protocol kernel extends the P2.1 `Protocol` object with the following required contract fields.

| Field | Required | Meaning |
| --- | --- | --- |
| `protocol_id` | Yes | Stable protocol identity |
| `protocol_version` | Yes | Material semantic version |
| `run_class` | Yes | One base run class from Section 4 |
| `intake_schema_ref` | Yes | Schema skeleton specialization for admitted inputs |
| `result_schema_ref` | Yes | Schema skeleton specialization for terminal result payload |
| `proof_policy_ref` | Yes | Proof expectations for the run class |
| `authority_default` | Yes | Conservative default authority envelope for this protocol |
| `verifier_slots` | Yes | Named verifier positions expected for this run class |
| `writeback_default` | Yes | Default lane stance: `none` or one explicit lane |

### 7.2 Required intake rules

Every protocol kernel must enforce all of the following:

1. `objective_spec` is mandatory.
2. Admitted work must point to a frozen `input_snapshot_ref`.
3. Class-conditioned refs such as `evidence_pack_ref`, `context_pack_ref`, `artifact_ref`, `branch_ref`, and `commission_ref` must be explicit rather than inferred from transcript state.
4. `contract_ref` is required when the work is commissioned or when writable authority is requested.
5. `authority_scope_ref` must exist whenever the protocol would read beyond the default wedge or would propose writeback.

### 7.3 Required result rules

Every protocol kernel result must:

1. emit one `proof_bundle_ref`,
2. emit one `state_delta_ref` even if the delta is empty,
3. keep class-specific payload separate from proof/delta,
4. return `writeback_proposal_ref` values only when lane-specific proposals were explicitly generated.

### 7.4 Required proof rules

Every protocol kernel proof skeleton must include:

- `evidence_refs`,
- `uncertainty_items`,
- `omission_items`,
- `contradiction_items` when relevant,
- the verifier results that fill the class-specific `verifier_slots`.

## 8. Default authority, verifier, and writeback policy

| Run class | Authority default | Verifier slot minimum | Writeback default |
| --- | --- | --- | --- |
| `compare` | read-only evidence/context/artifact access | 2 slots minimum | none |
| `synthesize` | read-only evidence/context access | 2 slots minimum | none; artifact proposal only if contracted |
| `extract` | read-only evidence/context access | 2 slots minimum | none; artifact proposal only if contracted |
| `transform` | artifact-target read plus artifact-lane proposal authority | 3 slots minimum | artifact lane only |
| `audit` | read-only target/policy access | 2 slots minimum | none |
| `plan` | read-only evidence/context/branch access | 2 slots minimum | none |
| `triage` | intake and routing authority only | 2 slots minimum | none |

Additional policy locks:

- memory, canon, workflow, and export writes are never default writeback lanes,
- partial approval is allowed only through separate lane-specific proposals,
- background execution does not expand authority beyond the linked protocol/applet defaults.

## 9. Anti-drift rules and edge cases

1. Task-family labels are user-facing projections over run classes, not a second ontology.
2. Prompt assets may feed a protocol, but they do not replace protocol identity or run class.
3. Branching, replay, and compare views do not turn into private backend semantics.
4. No protocol may default to mixed-lane writeback.
5. No protocol may hide memory or canon promotion behind read-only labeling.
6. No applet may bypass explicit verifier slots or authority defaults.
7. R7 -> Task Studio handoff preserves run-class meaning instead of reclassifying work into app-private types.

## 10. Downstream implications

### 10.1 For P2.3 and P2.4

- governance and proof invariants should attach to these run classes and protocol fields rather than generic task blobs.

### 10.2 For P2.5

- release semantic packs should expose these run classes as projections over shared primitives, not substitute classes.

### 10.3 For P4.8, P4.9, and P5.3

- governed applet chat, Commissioning Bridge, and full protocol packs should extend this taxonomy rather than inventing a new reusable-execution model.

## 11. Review notes

Human review should confirm that this pack:

- makes run classes explicit and bounded,
- keeps Task Studio family labels aligned to shared run classes,
- preserves conservative authority and writeback defaults,
- does not reintroduce transcript-first, agent-builder-first, or app-private ontology drift.
