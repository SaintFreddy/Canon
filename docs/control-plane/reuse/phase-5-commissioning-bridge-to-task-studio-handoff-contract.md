# Phase 5 Commissioning Bridge -> Task Studio handoff contract
Version: 1.0
Status: Accepted
Task: P5.7 — Commissioning Bridge -> Task Studio handoff contract
Artifact ID: reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1
Reuse scope: Accepted handoff contract mapping accepted R7 commissioning semantics into Task Studio surfaces and lifecycle without ontology translation

This artifact is accepted for downstream use.
It defines exact projection and continuity rules from R7 into Task Studio surfaces.
It depends on the accepted P5.6 V1 scope pack and does not alter accepted R7, Task Studio, governance, proof, or reusable-execution semantics.

## 1. Purpose

This pack turns the accepted R7 handoff obligation and Task Studio app-model baseline into one exact projection contract.

It exists to:

- map the R7 commissioning payload onto Task Studio surfaces and lifecycle stages without object translation,
- make the exact preserved IDs, refs, proof/governance continuity, and reusable-execution lineage explicit,
- decompose view-specific R7 additions such as `Acceptance Stack` and `Chat-to-Run Handoff` into the accepted Task Studio app model,
- protect `P6.1` and later package work from inventing app-private handoff state machines.

## 2. Scope boundaries

### In scope

- the exact preserved handoff payload from R7 into Task Studio,
- the projection of R7 additions and shared objects onto Task Studio surfaces,
- lifecycle landing and routing rules for handoff states,
- continuity rules for identity, lineage, proof, governance, delta, writeback, reusable execution, and failure/resume,
- explicit boundary locks that keep Task Studio a projection change rather than a semantic rewrite.

### Out of scope

- changing R7 shared-object meaning or Task Studio surface meaning,
- changing V1 inclusion/exclusion policy beyond the accepted P5.6 scope boundary,
- route/module/component implementation detail that belongs to `P6.1`,
- repo/package architecture that belongs to `P6.2`,
- inventing a mandatory new shared-object schema for handoff identity.

## 3. Handoff interpretation rules

### 3.1 Projection-not-translation rule

Task Studio inherits the accepted R7 commissioned-work payload as the same shared objects with the same meaning.
The handoff is a projection change over the existing `Commission -> Contract -> Run` chain, not an export/import step, ontology translation, or app-local re-creation.

### 3.2 Exact-payload-preservation rule

The handoff preserves `Commission`, `Contract`, `Run`, `Authority Scope`, `Proof Bundle`, `State Delta`, `Writeback Proposal`, linked `Review` / `Approval Decision` history, linked artifact refs, and relevant evidence/context lineage.
If reusable execution materially governs the work, `protocol_id`, `protocol_version`, `workflow_id`, `applet_id`, `trigger_id`, `pack_id`, and `integration_binding_ref` remain inspectable after handoff.

### 3.3 Stage-landing-over-export/import rule

Handoff lands into one or more Task Studio surfaces according to lifecycle state.
Even when V1 prefers `Task Home` as the initial entry, the landing must deep-link to the same shared objects and the same stage-specific truth surfaces one step away without lossy translation.

### 3.4 Acceptance-Stack-decomposition rule

`Acceptance Stack` remains a chat-domain projection alias, not a new shared object.
Inside Task Studio it decomposes into `Proof Ledger`, `Delta Inspector`, and `Writeback Panel` over the same `Review`, `Approval Decision`, `State Delta`, and `Writeback Proposal` records.

### 3.5 Shared-ID-and-lineage rule

The handoff keeps stable shared IDs and lineage refs, including `commission_id`, `contract_id`, `run_id`, `proof_bundle_id`, `state_delta_id`, `writeback_proposal_id`, linked artifact refs, `amends_contract_ref`, and frozen admitted-basis lineage.
This pack does not invent a mandatory `handoff_id`; if a later accepted shared-object pack introduces one, it must be additive rather than replacing the preserved R7 payload.

### 3.6 Failure-and-resume-parity rule

Failed, blocked, background, resumed, and compensating work remains inspectable inside Task Studio with the same proof, delta, approval, and reusable-execution lineage floor as in R7.
Resume reopens the same shared object chain; compensation is new governed work, not silent undo.

## 4. Exact preserved handoff payload

| Shared object or ref | R7 source / continuity center | Task Studio destination surfaces | Must remain unchanged |
| --- | --- | --- | --- |
| `Commission` | `Commission Card`, `Chat-to-Run Handoff` | `Task Home`; `New Commission Sheet` when intake shaping is still active | `commission_id`, objective, source anchors, priority, and resumable continuity |
| `Contract` | `Contract Draft`, `Run Preflight`, handoff payload | `Task Contract Panel` | `contract_id`, `run_class`, deliverable shape, acceptance policy, and `amends_contract_ref` lineage |
| `Authority Scope` | `Run Preflight`, handoff payload | `Authority Panel` with `Task Contract Panel` companion | explicit grants, limits, review path, side-effect preview, and writeback preview |
| `Evidence Pack` | admitted-basis shaping before launch, handoff refs | `Evidence Pack Builder` | source refs, inclusion/exclusion choices, and pinned evidence state |
| `Context Pack` and frozen admitted basis | `Run Preflight`, handoff refs | `Context Inspector` | compiled context refs, `input_snapshot_ref` / frozen basis lineage, and admission rationale |
| `Run` | `Live Monitor`, handoff payload | `Live Run View`; `Result Canvas` after terminal state | `run_id`, lifecycle state, child-run lineage, pending approvals, and diagnostics continuity |
| `Proof Bundle` | `Proof Ledger`, `Acceptance Stack`, handoff payload | `Proof Ledger` | `proof_bundle_id`, evaluator results, slot outcomes, uncertainty, and failure basis |
| `State Delta` | `Delta Inspector`, `Acceptance Stack`, handoff payload | `Delta Inspector` | `state_delta_id`, lane-separated target refs, and explicit empty/failure delta state |
| `Writeback Proposal` | `Acceptance Stack`, handoff payload | `Writeback Panel` | `writeback_proposal_id`, lane-local proposal state, apply status, and compensation lineage |
| `Review` / `Approval Decision` | `Acceptance Stack`, handoff payload | `Proof Ledger`; `Writeback Panel` | attributable, append-only review and approval history |
| Linked artifacts | run result, delta/apply refs, handoff payload | `Result Canvas`; `Delta Inspector`; `Writeback Panel` | artifact refs and focal/result continuity remain shared rather than re-created |
| Reusable-execution refs | R6/R7 lineage carried through handoff | `Task Contract Panel`; `Authority Panel`; `Live Run View`; `Context Inspector` | `protocol_id`, `protocol_version`, `workflow_id`, `applet_id`, `trigger_id`, `pack_id`, and `integration_binding_ref` remain refs, not app-local metadata |

## 5. R7 projection additions -> Task Studio decomposition

| R7 addition or projection | Task Studio target | Decomposition contract |
| --- | --- | --- |
| `Commission Card` | `Task Home`; `New Commission Sheet` when still shaping intake | Continues to project the same `Commission` and linked `Contract` rather than becoming a Task Studio-private task shell |
| `Contract Draft` | `Task Contract Panel` | Continues to project the same `Contract` record and amendment lineage rather than a new draft-only object family |
| `Run Preflight` | `Task Contract Panel` + `Authority Panel` + `Context Inspector` | Continues to project `Contract`, `Authority Scope`, and frozen admitted basis instead of a transient wizard-only state |
| `Live Monitor` | `Live Run View` | Continues to project the same `Run`, child-run lineage, approvals, and diagnostics refs |
| `Proof Ledger` | `Proof Ledger` | Continues to project the same `Proof Bundle`, `Review`, and `Approval Decision` records |
| `Delta Inspector` | `Delta Inspector` | Continues to project the same `State Delta` and target refs |
| `Acceptance Stack` | `Proof Ledger` + `Delta Inspector` + `Writeback Panel` | Decomposes into proof/review, delta, and apply surfaces without inventing a replacement object |
| `Chat-to-Run Handoff` | `Task Home` or lifecycle-primary deep link | Carries the preserved payload into Task Studio as a route/selection envelope, not an export/import or rewrite step |

## 6. Lifecycle landing and routing matrix

| R7 state or moment | Task Studio landing surface | Required companions | Routing rule |
| --- | --- | --- | --- |
| Commission captured but not yet fully shaped | `Task Home` or `New Commission Sheet` | Inspector, Browser / Library as needed | If work remains intake-shaped, land where commission shaping can continue without hiding source anchors or shared IDs |
| Contract shaping or amendment in progress | `Task Contract Panel` | `Evidence Pack Builder`, `Context Inspector`, `Strategy Board` when needed | Land directly in contract/evidence/context shaping rather than flattening into a chat summary |
| Run Preflight / lock stage | `Authority Panel` with `Task Contract Panel` companion | `Context Inspector`, `Proof Ledger` if review context is already material | Land where authority scope, frozen basis, proof plan, and side-effect/writeback preview remain explicit |
| Run executing, blocked, background, or resumed | `Live Run View` | Timeline, Inspector, Console | Land where run state, blocked reason, approvals, and child-run lineage remain inspectable |
| Terminal result inspection | `Result Canvas` | `Proof Ledger`, `Delta Inspector` | Land where result/proof/delta continuity is explicit instead of collapsed into one answer surface |
| Review, accept, branch, or replay decision | `Result Canvas` + `Proof Ledger` | `Delta Inspector`, `Strategy Board`, Compare View as needed | Land where recommendation basis, residual uncertainty, and branch options stay visible |
| Selective persistence / apply | `Writeback Panel` | `Proof Ledger`, Diff / Merge View, Queue / Inbox as needed | Land where lane-by-lane review, apply state, and compensation posture remain attributable |

When a V1 default chooses `Task Home` first, the landing must preserve direct deep links into the lifecycle-primary surface that already owns the consequential state.

## 7. Continuity rules

### 7.1 Identity and lineage continuity

1. Shared IDs remain stable across the handoff; Task Studio may not mint substitute cards or route-local IDs for the preserved payload.
2. `amends_contract_ref`, child-run lineage, evidence/context refs, frozen admitted basis, and artifact refs remain linked rather than re-authored.
3. Handoff does not erase prior R6 reusable-execution lineage when the run originated from Protocol/Applet/Workflow/Trigger context.
4. Task-family labels remain projections over `run_class`; the handoff may not create a Task-Studio-only family map.

### 7.2 Proof, governance, delta, and writeback continuity

1. `Proof Bundle` remains authoritative and attached to the same `run_id` after handoff.
2. `Acceptance Stack` never replaces `Review`, `Approval Decision`, `State Delta`, or `Writeback Proposal`; it only projects them together in chat.
3. Lane separation remains explicit end-to-end, including empty/failure deltas, partial acceptance, deferred apply, and compensation.
4. Proof, review, and apply state may summarize by default, but they may not disappear into logs or a persuasive answer blob.

### 7.3 Reusable-execution continuity

1. Exact version pinning and scoped binding rules from `P5.4` remain visible wherever they materially govern the handed-off run.
2. `protocol_id`, `protocol_version`, `workflow_id`, `applet_id`, `trigger_id`, `pack_id`, and `integration_binding_ref` remain inspectable refs rather than copied app metadata.
3. No inline secret material crosses the handoff boundary; only refs and scope context do.
4. Background parity remains binding: the same proof and governance minima apply after handoff as before it.

### 7.4 Failure, resume, and compensation continuity

1. Failed, blocked, background, and resumed runs remain fully inspectable in `Live Run View`, `Proof Ledger`, and `Delta Inspector`.
2. Resume continues the same shared object chain instead of spawning a fresh Task Studio-private task shell.
3. Compensation or remediation is new governed work that links back through append-only lineage; it is not silent undo.
4. Missing or deferred writeback does not erase proof, delta, or review history from the handed-off run.

## 8. Scenario and shortcut grounding

| Handoff area | Strongest claims / scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| Projection integrity across the handoff | `RI-05`, `RI-08`, `TS-01`, `TS-06`, `GS-14`, `EC-07` | `fs.no-master-chat-truth`, `fs.no-separate-backend-per-view` |
| Preflight and lock continuity | `GS-12`, `EC-06`, `SS-05` | `fs.no-master-chat-truth` |
| Acceptance Stack decomposition | `TS-04`, `GS-13`, `EC-03` | `fs.no-silent-proposal-application` |
| Family and lifecycle continuity | `TS-05`, `GS-15`, `GS-16`, `SS-09` | `fs.no-transcript-first-rewrite-trap`, `fs.no-separate-backend-per-view` |
| Background/resume parity | `GS-10`, `GS-11`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-separate-backend-per-view` |

## 9. Boundary locks for downstream work

1. `P5.6` may choose a home-first or stage-first default landing, but the exact payload mapping in this pack may not be weakened or replaced.
2. `P6.1` must implement this handoff as route/module contracts over the accepted Task Studio surfaces and shared grammar, not as a new handoff object model.
3. `P6.2` may plan package boundaries around this accepted contract, but it may not reinterpret the handoff as repo-driven semantics.
4. `Acceptance Stack` remains a projection alias/composition; it may not become a replacement shared object or a hidden convenience verdict.
5. No mandatory `handoff_id` or export/import artifact is introduced here; any later formalization must remain additive to the preserved R7 payload.

## 10. Downstream implications

### 10.1 For `P6.1`

- surface-contract work should implement the lifecycle landing matrix and projection decomposition above as the route and companion-surface baseline,
- surface defaults may vary, but they must preserve deep-link continuity into the same shared objects and not hide proof, delta, review, or apply state.

### 10.2 For later repo/package work

- this accepted pack now acts as the semantic handoff baseline for package mapping, event routing, and route/module boundaries,
- later package or route planning may refine implementation detail, but it may not reopen the accepted handoff meaning.

## 11. Review notes

Human review should confirm that this pack:

- maps every consequential R7 object and projection onto accepted Task Studio surfaces without ontology translation,
- keeps `Acceptance Stack` as a decomposition over proof, delta, review, and writeback rather than a new object,
- preserves exact shared IDs, frozen admitted basis lineage, reusable-execution refs, and lane-separated apply history across the handoff,
- avoids inventing a mandatory `handoff_id` or other app-private transfer object.

Human review should also explicitly confirm:

- whether V1 defaults land first in `Task Home` or directly in the lifecycle-primary surface,
- whether `Acceptance Stack` remains a visible alias in V1 copy or only the decomposed Task Studio surfaces are named,
- how much reusable-execution lineage is default-visible versus one click away in the initial build.
