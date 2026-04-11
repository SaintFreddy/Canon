# Phase 2 core object and state-machine spec pack
Version: 1.0
Status: Accepted
Task: P2.1 — Core object and state-machine spec pack
Artifact ID: sem.phase2-core-object-state-machines.v1
Semantic scope: Shared first-class object contracts, identity rules, and lifecycle/state-machine semantics for the core shared-environment object model

## 1. Purpose

This pack defines the first shared semantic contracts that downstream release, architecture, storage, and API work can code against.

It exists to:

- turn the accepted Phase 1 canon into explicit object contracts,
- make identity and lifecycle rules concrete before technical architecture work,
- keep consequential truth in shared primitives instead of transcript or app-private state.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- first-class shared objects,
- identity rules,
- lifecycle states and transition rules,
- core cross-object reference rules,
- related support objects required to make the main state machines coherent.

### Out of scope

- run-class taxonomy details beyond the `run_class` slot,
- proof policy detail by task family,
- UI projection grammar,
- runtime/process architecture,
- storage/indexing topology,
- repo/package layout.

## 3. Contract baseline

### 3.1 Common envelope

Every first-class object in this pack carries the following common fields.

| Field | Required | Meaning |
| --- | --- | --- |
| `object_type` | Yes | Stable family tag such as `run`, `artifact`, `branch`, `contract` |
| Primary typed ID (`run_id`, `artifact_id`, and so on) | Yes | Immutable family-specific identifier |
| `schema_version` | Yes | Semantic contract version used to interpret the payload |
| `lifecycle_state` | Yes | Current state from the object family state machine |
| `created_at` | Yes | Creation timestamp |
| `created_by_actor_ref` | Yes | Actor responsible for creation |
| `workspace_ref` | Yes unless explicitly global | Owning shared-environment scope |
| `lineage_refs` | Conditional | Parent/derivation links when the object is not original |
| `review_refs` | Conditional | Linked reviews governing approval or challenge |
| `provenance_refs` | Conditional | Run/source/proof links supporting inspectability |

### 3.2 Identity rules

| Rule ID | Rule |
| --- | --- |
| `IR-01` | IDs are typed, opaque, immutable, and never reused for a different semantic object. |
| `IR-02` | Surface changes, app changes, and mode changes never change the underlying object ID. |
| `IR-03` | Replay, retry, branch fork, contract amendment, or proposal regeneration creates a new object record rather than mutating historical identity. |
| `IR-04` | `*_ref` points to exactly one object; `*_refs` is an ordered list when order affects meaning. |
| `IR-05` | Proof Bundle, State Delta, Approval Decision, and Checkpoint are append-only records once created; later review may change linked state, not payload history. |
| `IR-06` | Artifact continuity uses a stable `artifact_id` plus explicit revision references; no silent in-place mutation is allowed. |
| `IR-07` | Durable writeback lanes stay typed and separate: artifact, memory, canon, workflow, and export. |
| `IR-08` | Transcript/session state alone never satisfies first-class identity requirements. |

### 3.3 Core cross-object references

| Reference field | Meaning |
| --- | --- |
| `run_ref` | Reference to the consequential run that produced or consumed the object |
| `artifact_ref` | Reference to the continuity anchor artifact |
| `branch_ref` | Reference to the semantic branch containing the work |
| `proof_bundle_ref` | Reference to the proof record for a run or commissioned result |
| `state_delta_ref` | Reference to the semantic delta emitted by a run |
| `writeback_proposal_ref` | Reference to one lane-specific persistence proposal |
| `commission_ref` | Reference to the commissioned-work request object |
| `contract_ref` | Reference to the scoped executable contract |
| `protocol_ref` | Reference to the reusable execution contract |
| `applet_ref` | Reference to the installed/operating reusable execution instance |
| `review_ref` | Reference to the review container governing a decision |
| `approval_decision_ref` | Reference to one attributable decision record |

## 4. Object family summary

| Object | Owner layer | Identity anchor | Mutability mode | Primary downstream use |
| --- | --- | --- | --- | --- |
| Run | Shared environment | `run_id` | Mutable only through lifecycle-state progress | Execution, replay, proof, delta, writeback linkage |
| Artifact | Shared environment | `artifact_id` + revision refs | Root stable, revisions append-only | Artifact-centered continuity from R4 onward |
| Branch | Shared environment | `branch_id` | Mutable through branch lifecycle only | Alternate semantic lines of work and replay |
| Proof Bundle | Shared environment projection over engine proof form | `proof_bundle_id` | Payload append-only | Proof, uncertainty, contradiction, validation basis |
| State Delta | Shared environment projection over engine delta form | `state_delta_id` | Payload append-only | Proposed semantic change summary |
| Writeback Proposal | Shared environment | `writeback_proposal_id` | Mutable through explicit decision states | Durable persistence by lane |
| Memory Object | Shared environment | `memory_id` | State-governed durable object | Explicit memory lane |
| Canon Object | Shared environment | `canon_object_id` | State-governed durable object | Accepted knowledge / canon lane |
| Commission | Shared environment | `commission_id` | Mutable through commissioned-work lifecycle | Serious work request continuity |
| Contract | Shared environment | `contract_id` | New contract record on material amendment | Executable scope and acceptance basis |
| Protocol | Shared environment | `protocol_id` + `protocol_version` | Versioned reusable contract | Reusable execution kernel |
| Applet | Shared environment | `applet_id` | Mutable through install/enable lifecycle | Governed reusable execution instance |
| Review | Shared environment | `review_id` | Mutable through review lifecycle | Explicit review/approval container |
| Approval Decision | Shared environment | `approval_decision_id` | Payload append-only | Attributable decision record |

## 5. Core object contracts

### 5.1 Run

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `run_id` | Yes | Consequential execution identity |
| `run_class` | Yes | Typed execution class slot to be expanded in P2.2 |
| `objective_spec` | Yes | What the run is trying to accomplish |
| `input_snapshot_ref` | Yes | Frozen admission input set for replay/audit |
| `evidence_pack_ref` | Conditional | Explicit evidence input when applicable |
| `context_pack_ref` | Conditional | Explicit context input when applicable |
| `branch_ref` | Conditional | Branch carrying this run’s semantic line |
| `contract_ref` | Conditional | Required for commissioned work |
| `authority_scope_ref` | Conditional | Governing authority boundary |
| `proof_bundle_ref` | Terminal | Proof emitted by the run |
| `state_delta_ref` | Terminal | Delta emitted by the run, even if empty |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `prepared` | Inputs assembled but not yet admitted | `admitted`, `cancelled` |
| `admitted` | Inputs frozen enough to execute | `executing`, `cancelled` |
| `executing` | Consequential work in progress | `completed`, `failed`, `cancelled` |
| `completed` | Terminal success | None |
| `failed` | Terminal failure with inspectable proof/failure basis | None |
| `cancelled` | Terminal stop before or during execution | None |

#### Identity and lifecycle rules

1. A retry, replay, or branch execution creates a new `run_id`.
2. Every terminal run must link to exactly one `proof_bundle_ref` and one `state_delta_ref`.
3. A run may appear in chat, Artifact Workspace, R7, or Task Studio without changing identity.

### 5.2 Artifact

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `artifact_id` | Yes | Stable continuity anchor |
| `artifact_kind` | Yes | Typed artifact family |
| `head_revision_ref` | Yes | Current accepted or active revision |
| `origin_run_ref` | Yes | First run that produced the artifact root |
| `focal_scope_ref` | Conditional | Surface/app context currently centering the artifact |
| `latest_delta_refs` | Conditional | Recent deltas affecting the artifact |
| `latest_writeback_proposal_refs` | Conditional | Open or latest proposals touching the artifact lane |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `draft` | Artifact root exists but no accepted working revision yet | `active`, `archived` |
| `active` | Artifact is a live continuity anchor | `superseded`, `archived` |
| `superseded` | A newer artifact root replaces this one as continuity center | `archived` |
| `archived` | Retained for history only | None |

#### Identity and lifecycle rules

1. `artifact_id` stays stable while revisions change through approved artifact-lane writeback only.
2. Revision changes update `head_revision_ref`; they do not mutate history in place.
3. Artifact continuity does not replace run identity; it anchors visible continuity above it.

### 5.3 Branch

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `branch_id` | Yes | Semantic branch identity |
| `parent_branch_ref` | Conditional | Parent branch when forked |
| `fork_checkpoint_ref` | Yes for non-root branches | Checkpoint from which the branch forked |
| `continuity_anchor_refs` | Yes | Runs/artifacts/contracts anchoring the branch |
| `active_context_pack_ref` | Conditional | Active context basis for replay |
| `head_run_ref` | Conditional | Most recent run on the branch |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `open` | Branch accepts new runs and checkpoints | `frozen`, `merged`, `abandoned` |
| `frozen` | Branch preserved for compare/replay without active mutation | `open`, `merged`, `abandoned` |
| `merged` | Branch outputs accepted into another continuity line | None |
| `abandoned` | Branch intentionally not continued | None |

#### Identity and lifecycle rules

1. Forking creates a new `branch_id`; transcript copies are never branches.
2. A branch preserves checkpoint and pack lineage explicitly.
3. Mode switches are projections over a branch, not new branch identities.

### 5.4 Proof Bundle

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `proof_bundle_id` | Yes | Proof record identity |
| `run_ref` | Yes | Run this proof belongs to |
| `evidence_refs` | Yes | Evidence supporting the result |
| `uncertainty_items` | Yes, possibly empty | Explicit uncertainty markers |
| `omission_items` | Yes, possibly empty | Known omissions or blind spots |
| `contradiction_items` | Yes, possibly empty | Contradictions discovered during the run |
| `validator_result_refs` | Conditional | Validator outcomes attached to this proof |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `collected` | Proof payload captured from the run | `reviewed` |
| `reviewed` | Proof inspected by a reviewer or validator workflow | `accepted`, `challenged` |
| `accepted` | Proof basis accepted for downstream use | None |
| `challenged` | Proof remains attached but is marked disputed | `reviewed` |

#### Identity and lifecycle rules

1. Proof payload is append-only once created.
2. Review changes state classification, not the historical proof payload.
3. Proof remains distinct from prose persuasion or UI summary.

### 5.5 State Delta

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `state_delta_id` | Yes | Semantic delta identity |
| `run_ref` | Yes | Run that emitted the delta |
| `affected_lane_refs` | Yes | One or more lanes touched by the delta |
| `target_object_refs` | Yes, possibly empty | Objects potentially changed |
| `change_items` | Yes | Structured summary of proposed semantic changes |
| `empty_delta_flag` | Yes | Explicitly marks no-op runs |
| `derived_writeback_proposal_refs` | Conditional | Lane-specific proposals created from this delta |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `recorded` | Delta captured from the run | `scoped` |
| `scoped` | Target lanes/objects resolved for review | `closed`, `superseded` |
| `closed` | All derived proposals terminal or delta confirmed no-op | None |
| `superseded` | Later accepted work replaces this delta before closure | None |

#### Identity and lifecycle rules

1. A delta is never the same thing as a writeback proposal.
2. One run emits one delta record, even if the delta is empty.
3. Lane separation must be visible in `affected_lane_refs`.

### 5.6 Writeback Proposal

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `writeback_proposal_id` | Yes | Proposal identity |
| `lane` | Yes | Exactly one lane: `artifact`, `memory`, `canon`, `workflow`, or `export` |
| `state_delta_ref` | Yes | Delta this proposal derives from |
| `target_object_refs` | Yes | Objects or scopes the proposal would modify |
| `operation_set` | Yes | Proposed create/update/supersede operations |
| `authority_scope_ref` | Yes | Authority boundary governing application |
| `review_ref` | Yes | Review container for decisioning |
| `approval_decision_refs` | Conditional | Decisions taken against this proposal |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `drafted` | Proposal shaped from a delta | `submitted`, `withdrawn` |
| `submitted` | Awaiting review/decision | `partially_approved`, `approved`, `rejected`, `withdrawn` |
| `partially_approved` | Some operations approved, some still pending | `approved`, `rejected`, `withdrawn` |
| `approved` | Approved but not yet applied | `applied` |
| `rejected` | Terminal refusal | None |
| `withdrawn` | Removed before application | None |
| `applied` | Terminal committed change | None |

#### Identity and lifecycle rules

1. One proposal belongs to exactly one lane.
2. Cross-lane changes require multiple proposals, not one mixed-lane object.
3. Application is explicit and terminal; no silent background mutation is allowed.

### 5.7 Memory Object

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `memory_id` | Yes | Durable memory object identity |
| `memory_kind` | Yes | Memory class/category |
| `scope_ref` | Yes | Scope in which the memory applies |
| `statement` | Yes | Memory content carried as explicit semantic data |
| `supporting_refs` | Yes | Supporting source/run/proof references |
| `freshness_policy` | Conditional | Expiry or refresh rule |
| `last_review_ref` | Conditional | Most recent review of the memory |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `candidate` | Proposed but not yet activated | `active`, `retired` |
| `active` | Available for governed use | `suspended`, `retired` |
| `suspended` | Temporarily excluded from active injection/use | `active`, `retired` |
| `retired` | No longer used, retained for history | None |

#### Identity and lifecycle rules

1. Memory activation must come through explicit lane-governed writeback, not hidden sludge.
2. Suspending a memory object does not erase provenance.
3. Memory and canon are separate object families even if both hold durable statements.

### 5.8 Canon Object

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `canon_object_id` | Yes | Accepted-knowledge object identity |
| `canon_scope` | Yes | Scope of truth claim |
| `statement` | Yes | Canonical accepted statement |
| `acceptance_basis_refs` | Yes | Reviews/approvals/sources supporting acceptance |
| `source_authority_refs` | Conditional | Source authorities backing the claim |
| `supersedes_ref` | Conditional | Prior canon object replaced by this one |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `candidate` | Proposed for canon lane review | `accepted`, `rejected` |
| `accepted` | Canonically accepted for the scope | `superseded`, `retired` |
| `rejected` | Terminal refusal | None |
| `superseded` | Replaced by a newer canon object | `retired` |
| `retired` | Historical only | None |

#### Identity and lifecycle rules

1. Canon remains human-owned meaning even when Factory assists with shaping it.
2. Accepted canon cannot be silently edited in place; replacement uses `supersedes_ref`.
3. Canon does not collapse into memory and memory does not silently promote into canon.

### 5.9 Commission

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `commission_id` | Yes | Serious-work request identity |
| `requestor_ref` | Yes | Actor commissioning the work |
| `objective` | Yes | Requested outcome or decision |
| `scope_summary` | Yes | Initial scope boundary |
| `priority` | Yes | Priority/risk classification |
| `authority_scope_ref` | Conditional | Requested authority envelope |
| `contract_ref` | Conditional | Accepted contract governing execution |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `draft` | Commission being shaped | `submitted`, `cancelled` |
| `submitted` | Ready for triage | `triaged`, `cancelled` |
| `triaged` | Work classified and routed | `authorized`, `cancelled` |
| `authorized` | Approved to proceed under a contract | `active`, `cancelled` |
| `active` | Consequential commissioned work underway | `completed`, `cancelled` |
| `completed` | Terminal completion | None |
| `cancelled` | Terminal stop | None |

#### Identity and lifecycle rules

1. Commission is the request continuity anchor; Contract is the executable narrowing of that request.
2. R7 and Task Studio preserve `commission_id` across the handoff.
3. Serious work must not bypass commission/contract semantics once that bridge is in play.

### 5.10 Contract

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `contract_id` | Yes | Executable scope identity |
| `commission_ref` | Yes | Commission this contract serves |
| `run_class` | Yes | Contracted class of work |
| `scope_definition` | Yes | Boundaries and exclusions |
| `deliverable_schema_refs` | Yes | Expected outputs |
| `authority_scope_ref` | Yes | Authority available under this contract |
| `acceptance_policy` | Yes | How fulfillment is judged |
| `amends_contract_ref` | Conditional | Prior contract replaced or amended |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `draft` | Contract being shaped | `proposed`, `terminated` |
| `proposed` | Ready for acceptance decision | `accepted`, `terminated` |
| `accepted` | Approved but not yet underway | `active`, `superseded`, `terminated` |
| `active` | Governing one or more runs | `fulfilled`, `superseded`, `terminated` |
| `fulfilled` | Terminal successful completion | None |
| `superseded` | Replaced by a later accepted amendment | None |
| `terminated` | Terminal cancellation/stop | None |

#### Identity and lifecycle rules

1. Material amendment creates a new `contract_id` and links via `amends_contract_ref`.
2. Contract acceptance does not replace run identity; it governs later runs.
3. Task Studio inherits contract semantics instead of inventing new task-only truth.

### 5.11 Protocol

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `protocol_id` | Yes | Stable protocol identity |
| `protocol_version` | Yes | Material version of the protocol contract |
| `run_class` | Yes | Run class the protocol packages |
| `intake_schema_ref` | Yes | Expected input shape |
| `result_schema_ref` | Yes | Expected result shape |
| `proof_policy_ref` | Yes | Proof expectations linked to the protocol |
| `verifier_pack_refs` | Conditional | Attached verifier sets |
| `writeback_defaults` | Conditional | Default lane policy for runs created from this protocol |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `draft` | Protocol under definition | `validated` |
| `validated` | Shape passes protocol checks | `approved`, `draft` |
| `approved` | Accepted for use but not yet active | `active`, `deprecated` |
| `active` | Available to instantiate runs/applets | `deprecated`, `retired` |
| `deprecated` | Still readable, discouraged for new work | `active`, `retired` |
| `retired` | No longer instantiable | None |

#### Identity and lifecycle rules

1. Protocol packages run semantics; it does not invent a second execution ontology.
2. Material semantic changes increment `protocol_version`.
3. Prompt assets may feed a protocol, but they do not replace protocol identity.

### 5.12 Applet

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `applet_id` | Yes | Installed reusable execution identity |
| `protocol_ref` | Yes | Governing protocol |
| `protocol_version` | Yes | Protocol version this applet is pinned to |
| `trigger_ref` | Conditional | Trigger object for scheduled/evented execution |
| `context_recipe_ref` | Conditional | Reusable context recipe |
| `strategy_preset_ref` | Conditional | Reusable strategy preset |
| `policy_binding_refs` | Conditional | Policy bindings active for the applet |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `draft` | Applet configuration being shaped | `installed`, `retired` |
| `installed` | Installed but not running automatically | `enabled`, `disabled`, `retired` |
| `enabled` | Allowed to launch governed runs | `paused`, `disabled`, `retired` |
| `paused` | Temporarily not launching new runs | `enabled`, `disabled`, `retired` |
| `disabled` | Installed but inactive | `enabled`, `retired` |
| `retired` | No longer usable | None |

#### Identity and lifecycle rules

1. Applets remain projections over Run/Protocol semantics.
2. Background execution still emits Run, Proof Bundle, State Delta, and Writeback Proposal objects.
3. Installing or enabling an applet never grants hidden authority beyond `policy_binding_refs` and linked authority scope.

### 5.13 Review

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `review_id` | Yes | Review container identity |
| `review_kind` | Yes | What is being reviewed |
| `subject_refs` | Yes | Objects under review |
| `required_roles` | Yes | Which roles must decide |
| `decision_policy` | Yes | Unanimous, quorum, single-authority, and so on |
| `open_item_refs` | Conditional | Unresolved sub-items |
| `final_decision_refs` | Conditional | Recorded decisions resolving the review |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `open` | Review created but not yet worked | `in_progress`, `cancelled` |
| `in_progress` | Decisions actively being gathered | `partially_decided`, `resolved`, `cancelled` |
| `partially_decided` | Some decisions recorded, more still required | `resolved`, `cancelled` |
| `resolved` | Decision policy satisfied | `closed` |
| `closed` | Historical and no longer open to new decisions | None |
| `cancelled` | Terminal stop without resolution | None |

#### Identity and lifecycle rules

1. A review is the decision container, not the decision itself.
2. One review may govern several related proposals, but lane separation must still remain visible.
3. Review resolution does not erase the linked approval decision history.

### 5.14 Approval Decision

#### Required object-specific fields

| Field | Required | Meaning |
| --- | --- | --- |
| `approval_decision_id` | Yes | Attributable decision identity |
| `review_ref` | Yes | Review this decision belongs to |
| `decision_scope_ref` | Yes | Proposal/object slot the decision applies to |
| `decider_ref` | Yes | Actor or role instance making the decision |
| `outcome` | Yes | `approved`, `approved_with_conditions`, `rejected`, or `deferred` |
| `conditions` | Conditional | Conditions required for approval |
| `rationale_ref` | Conditional | Linked rationale/proof reference |

#### State machine

| State | Meaning | Allowed next states |
| --- | --- | --- |
| `drafted` | Decision being prepared | `recorded`, `withdrawn` |
| `recorded` | Attributable decision entered into history | `superseded` |
| `superseded` | Later decision replaces this decision in the same slot | None |
| `withdrawn` | Draft never recorded | None |

#### Identity and lifecycle rules

1. Decision outcome is data; lifecycle state tracks whether the decision is recorded or superseded.
2. Approval decisions are attributable and inspectable.
3. A later decision does not mutate the historical content of an earlier recorded decision.

## 6. Related support objects

| Object | Required fields | Minimal lifecycle contract | Notes |
| --- | --- | --- | --- |
| Evidence Pack | `evidence_pack_id`, `item_refs`, `selection_policy`, `lineage_refs` | `draft -> frozen -> superseded/archived` | Shared operating pack over engine evidence-set machinery |
| Context Pack | `context_pack_id`, `compiled_input_refs`, `freeze_basis_ref`, `lineage_refs` | `draft -> frozen -> superseded/archived` | Inspectable operating projection over compiled context |
| Checkpoint | `checkpoint_id`, `run_ref`, `branch_ref`, `snapshot_refs` | `captured` terminal | Immutable branch/replay anchor |
| Authority Scope | `authority_scope_id`, `grants`, `limits`, `policy_refs` | `draft -> approved -> expired/revoked` | Governance boundary, not strategy |
| Workflow | `workflow_id`, `protocol_refs`, `handoff_rules`, `policy_refs` | `draft -> approved -> active -> retired` | Reusable packaging object expanded later |
| Trigger | `trigger_id`, `trigger_kind`, `schedule_or_event`, `policy_refs` | `draft -> enabled/disabled -> retired` | Event/schedule starter for applets/workflows |

## 7. Cross-object invariants

1. Every consequential Run terminates with proof and delta objects, even if the delta is empty.
2. Writeback proposals are derived from deltas; deltas are not writebacks.
3. Artifact, memory, canon, workflow, and export persistence remain separate lanes end to end.
4. Commissioned work flows through `Commission -> Contract -> Run`, not directly from transcript request to hidden execution.
5. Branch identity is forked from explicit checkpoints, not cloned transcripts.
6. Task Studio handoff preserves `commission_id`, `contract_id`, `run_id`, `proof_bundle_id`, `state_delta_id`, and `writeback_proposal_id` values.
7. Protocols and applets package run semantics; they never bypass Run/Proof/Delta/Writeback objects.
8. Canon acceptance requires explicit review/approval; memory activation requires explicit lane-governed persistence.
9. Surface or mode projections may foreground different objects but may not create app-private substitutes for them.
10. Repo/package shape cannot be used to redefine object ownership or lifecycle semantics.

## 8. Downstream implications

### 8.1 For P2.2 — Run-class taxonomy + protocol kernel

- `run_class` slots, protocol schemas, verifier packs, and applet defaults should extend these object contracts rather than replace them.

### 8.2 For P2.3 — Governance / authority / writeback invariants

- authority scope, review, approval, and lane separation should be formalized as invariants over the objects defined here.

### 8.3 For P2.5 and P2.6

- release semantic packs and projection grammar work should treat these objects as the substrate below each projection.

### 8.4 For Phase 3 architecture work

- storage, event, IPC, and runtime contracts should map directly onto these identities and transitions.

## 9. Review notes

Human review should confirm that this pack:

- gives downstream work explicit fields, state machines, and identity rules for the major shared objects,
- preserves run consequence, lane separation, artifact continuity, and commission/contract continuity,
- does not let chat, Task Studio, or repo shape become the semantic owner of shared primitives.
