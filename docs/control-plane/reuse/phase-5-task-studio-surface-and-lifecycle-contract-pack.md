# Phase 5 Task Studio surface and lifecycle contract pack
Version: 1.0
Status: Accepted
Task: P5.5 — Task Studio surface and lifecycle contract pack
Artifact ID: reuse.phase5-task-studio-surface-lifecycle-contract-pack.v1
Reuse scope: Accepted Task Studio app-model contract for surfaces, lifecycle stages, layout rules, and progressive disclosure over accepted commissioned-work semantics

## 1. Purpose

This pack turns the accepted commissioning, governance, proof, protocol, and reusable-execution composition baselines into the Task Studio app-model contract.

It exists to:

- define the named Task Studio surfaces and the shared grammar each one projects,
- make the core commissioned-work lifecycle explicit as the primary Task Studio loop,
- lock layout and progressive-disclosure rules so Task Studio remains run-native, governable, proof-returning, and Task Studio-safe rather than prompt-centric or app-private.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- Task Studio named surfaces and their shared-grammar mapping,
- lifecycle stages for commissioned work,
- layout rules for primary vs companion surfaces,
- progressive-disclosure rules for contract, evidence/context, strategy, authority, proof, delta, and writeback,
- continuity rules for R7 handoff, reusable-execution lineage, and failed/blocked/background runs inside Task Studio.

### Out of scope

- P5.6 V1 inclusion/exclusion decisions and onboarding/category-teaching specifics,
- exact R7 -> Task Studio routing matrices beyond the identity/visibility invariants below,
- P6.1 route/module/component architecture,
- component-level UI styling or implementation details.

## 3. Surface and lifecycle interpretation rules

### 3.1 North-star and continuity-preservation rule

`TS-01` through `TS-06`, `RI-05`, `RI-08`, `rel.r7-commissioning-bridge-contract.v1`, and `reuse.phase5-workflow-trigger-applet-pack-integration-binding-specs.v1` remain binding.
`GI-01` through `GI-10`, `PI-01` through `PI-10`, and `RC-07` remain the minimum floor for Task Studio surfaces and lifecycle behavior.
Task Studio is a projection change over already-accepted commissioned-work semantics, not a rewrite destination or a new ontology.

### 3.2 Alias-to-grammar and one-substrate rule

Every Task Studio surface alias resolves to one or more accepted P2.6 grammar contracts.
No route, pane, tab, or panel may create substitute IDs, route-local truth, or view-private task semantics beneath those aliases.

### 3.3 Run-native and lane-visible rule

Task Studio is run-native, not prompt-centric.
`Commission`, `Contract`, `Evidence Pack`, `Context Pack`, `Authority Scope`, `Run`, `Proof Bundle`, `State Delta`, `Writeback Proposal`, `Review`, and `Approval Decision` remain explicit and inspectable throughout the app model.
Task-family labels stay a projection over the accepted base run classes rather than a new Task Studio-only taxonomy.

### 3.4 Stage-centered progressive-disclosure rule

The core Task Studio loop is `commission -> interpret -> lock -> execute -> inspect -> accept/branch -> persist selectively`.
Each lifecycle moment has one primary consequential surface center, with Inspector, Ledger, Compare, Timeline, Queue / Inbox, or Diff / Merge companions when governance, proof, delta, branching, or persistence semantics materially matter.

### 3.5 Failure and handoff continuity rule

Failed, blocked, background, or resumed work remains inspectable inside Task Studio.
R7 handoff preserves shared IDs and reusable-execution lineage (`protocol_id`, `protocol_version`, `workflow_id`, `applet_id`, `trigger_id`, `pack_id`, and `integration_binding_ref` where present) one step away from the primary commissioned-work surfaces.

## 4. Cross-surface and lifecycle summary

| Lifecycle stage | Primary surface center | Companion surfaces | Continuity center | What must stay visible |
| --- | --- | --- | --- | --- |
| `commission` | `Task Home` or `New Commission Sheet` | Browser / Library, Inspector | Commission intake continuity | Objective, task-family/run-class framing, source refs, resumable shared IDs |
| `interpret` | `Task Contract Panel`, `Evidence Pack Builder`, `Context Inspector`, `Strategy Board` | Compare View, Browser / Library | Contract/evidence/context/strategy shaping | Deliverable shape, evidence inclusion/exclusion, context recipe, option set, strategy rationale |
| `lock` | `Authority Panel` with `Task Contract Panel` companion | Context Inspector, Ledger | Frozen admitted basis and review path | Authority scope, proof plan, side-effect preview, writeback preview, review path |
| `execute` | `Live Run View` | Timeline, Inspector, Console | Run execution continuity | Current phase, blocked reason, child-run lineage, pending approvals, reusable-execution refs |
| `inspect` | `Result Canvas` | `Proof Ledger`, `Delta Inspector` | Result/proof/delta continuity | Result state, proof/evaluator outcome, delta state, failure basis |
| `accept/branch` | `Result Canvas` plus `Strategy Board` | `Proof Ledger`, `Delta Inspector`, Compare View | Review or branch continuation | Approval conditions, branch/replay choices, residual uncertainty, comparison basis |
| `persist selectively` | `Writeback Panel` | `Proof Ledger`, Queue / Inbox, Diff / Merge View | Lane-separated persistence continuity | Lane-local proposals, approval state, residual operations, apply/compensation status |

## 5. Shared Task Studio contract model

### 5.1 Task-family framing

| Task Studio family | Accepted run class | Primary continuity note |
| --- | --- | --- |
| Compare | `compare` | Task Studio compares explicit targets without inventing a Task Studio-private class |
| Synthesize | `synthesize` | Result-focused work stays bounded and grounded in explicit evidence/context |
| Extract | `extract` | Structured capture remains distinct from synthesis and stays traceable to spans/fields |
| Transform | `transform` | Targeted artifact change remains the only default artifact-write-eligible class |
| Audit | `audit` | Evaluation remains criteria-based rather than generic review chat |
| Plan | `plan` | Planning, options, and branch rationale stay explicit and replayable |
| Triage | `triage` | Intake classification and commissioning escalation stay explicit rather than bridge-private |

### 5.2 Surface alias-to-grammar mapping

| Task Studio surface | Shared grammar composition | Primary shared objects |
| --- | --- | --- |
| `Task Home` | Browser / Library + Queue / Inbox + Board | Commission, Contract, Run, Assignment, Workflow/Applet refs |
| `New Commission Sheet` | Composer + Inspector | Draft Commission, Source Reference, task-family/run-class framing |
| `Task Contract Panel` | Inspector with structured edit affordances | Contract, run class, protocol/version pins, acceptance policy |
| `Evidence Pack Builder` | Browser / Library + Inspector + Compare View | Evidence Pack, Source Reference, inclusion/exclusion state |
| `Context Inspector` | Inspector | Context Pack, context recipe lineage, frozen admitted basis |
| `Strategy Board` | Board + Inspector + Compare View | Plan/branch state, workflow stages, option set, checkpoints |
| `Authority Panel` | Inspector | Authority Scope, review path, side-effect/writeback preview, integration-binding scope |
| `Live Run View` | Live Monitor + Timeline + Inspector + Console | Run, Workflow, child runs, pending approvals, diagnostics refs |
| `Result Canvas` | Canvas with Inspector/Ledger companions | Run result, Artifact, next actions |
| `Proof Ledger` | Ledger | Proof Bundle, evaluator results, Review, Approval Decision |
| `Delta Inspector` | Inspector with Diff / Merge companion | State Delta, lane-separated change state, target refs |
| `Writeback Panel` | Diff / Merge View + Ledger + Queue / Inbox | Writeback Proposal, Review, Approval Decision, apply/compensation refs |

### 5.3 Shared visibility and continuity rules

1. Task Studio route or panel changes preserve stable shared-object IDs instead of creating app-private cards or shadow state.
2. Contract, evidence, context, strategy, authority, proof, delta, and writeback remain inspectable as separate semantic clusters throughout the lifecycle.
3. Summaries or default views may compress presentation, but one click or one panel away must recover the linked structured objects and their history.
4. `protocol_id`, `protocol_version`, `workflow_id`, `applet_id`, `trigger_id`, `pack_id`, and `integration_binding_ref` remain inspectable at execute, inspect, and persist stages wherever reusable-execution lineage materially matters.
5. Queue / Inbox, Board, Browser / Library, Live Monitor, Ledger, and Inspector remain projections over shared objects; they never become the semantic source of truth.

## 6. Surface specs

### 6.1 Intake and shaping surfaces

| Surface | Primary shared objects | Required behaviors | Boundary lock |
| --- | --- | --- | --- |
| `Task Home` | Commission, Contract, Run, Assignment, Workflow/Applet refs | Start new commissioned work, resume existing work, filter by task family and lifecycle state, preserve deep links into stage-specific surfaces | Must not become a dashboard-only second truth model or replace stage-specific semantic surfaces |
| `New Commission Sheet` | Draft Commission, Source Reference, task-family/run-class framing | Capture objective, attach sources, set initial task-family intent, and create the draft Commission / Contract path explicitly | Must not execute serious work directly or remain the sole source of truth once work becomes consequential |
| `Task Contract Panel` | Contract, run class, protocol/version pins, acceptance policy | Make deliverable shape, protocol pins, proof/review hooks, and acceptance basis explicit and editable in structured form | Must not collapse back into a prompt-only blob or hide executable scope in free-form prose |
| `Evidence Pack Builder` | Evidence Pack, Source Reference, inclusion/exclusion state, comparison refs | Build or adjust the Evidence Pack, preserve pins/exclusions and lineage, expose source-region links, support compare when evidence selection changes materially | Must not hide retrieval/admission decisions or silently substitute memory/canon for explicit evidence state |
| `Context Inspector` | Context Pack, context recipe lineage, frozen admitted basis, memory/canon notes | Show compiled context, frozen basis, inclusion/exclusion reasons, compaction notes, and bound reusable-execution refs | Must not be debug-only or force governance-critical context semantics into Console alone |
| `Strategy Board` | Plan/branch state, workflow stages, option set, checkpoints | Show option set, branch/replay choices, workflow stage order, and next-action strategy without losing explicit object refs | Must not turn explicit strategy and branch state into opaque agent theater or hidden chain-of-thought requirements |
| `Authority Panel` | Authority Scope, review path, side-effect preview, writeback preview, integration-binding scope | Expose grants, limits, proof plan, review path, side-effect class, writeback lanes, and scoped reusable-execution/binding context before execution or apply | Must not reduce authority to a confirmation modal or bury scope decisions in settings text |

### 6.2 Execution and inspection surfaces

| Surface | Primary shared objects | Required behaviors | Boundary lock |
| --- | --- | --- | --- |
| `Live Run View` | Run, Workflow, child runs, pending approvals, diagnostics refs | Show current phase, completed phases, blocked reasons, child-run lineage, pending approvals, and resumable state in governable terms | Must not become spinner-only UI, agent theater, or console-only truth for failed/background work |
| `Result Canvas` | Run result, Artifact, linked proof/delta refs, next actions | Present the focal result and its task-family fit while linking to proof, delta, branch, and persistence affordances | Must not collapse consequential work into one answer blob that replaces proof, delta, or review state |
| `Proof Ledger` | Proof Bundle, evaluator results, Review, Approval Decision | Surface structured claims, evidence refs, slot outcomes, failure codes, review history, and approval state as ledger entries | Must not reduce proof, review, and approval into prose-only summaries or hidden logs |
| `Delta Inspector` | State Delta, lane-separated change state, target refs | Inspect explicit proposed or observed change state, including empty/failure deltas, target identity, and lane separation | Must not hide consequence state behind chat summaries or silent mutation semantics |
| `Writeback Panel` | Writeback Proposal, Review, Approval Decision, apply/compensation refs | Support lane-by-lane selective acceptance, conditions, residual operations, apply status, and compensation lineage | Must not become one-click save, mixed-lane convenience, or silent proposal application |

## 7. Lifecycle stage contract

| Stage | Primary surface center | Required shared objects | Required disclosure | Exit / continuation |
| --- | --- | --- | --- | --- |
| `commission` | `Task Home` / `New Commission Sheet` | Draft Commission, Source Reference, task-family/run-class intent | Objective, source anchors, run-class intent, resumable identity | Produce a draft Commission and intake basis or remain explicitly blocked |
| `interpret` | `Task Contract Panel`, `Evidence Pack Builder`, `Context Inspector`, `Strategy Board` | Contract, Evidence Pack, Context Pack draft, strategy/branch state | Deliverable shape, evidence admission, context basis, strategy/options | Contract/evidence/context/strategy become explicit enough to lock or stay inspectably incomplete |
| `lock` | `Authority Panel` with `Task Contract Panel` companion | Authority Scope, frozen admitted basis, proof plan, review path | Objective/contract fit, authority scope, frozen basis, verifier plan, side-effect preview, writeback preview, review path, failure/compensation posture | Execution is admitted with explicit scope or blocked with explicit reasons |
| `execute` | `Live Run View` | Run, Workflow/Applet lineage, child runs, pending approvals | Current phase, expected next transitions, blocked reasons, diagnostics refs, reusable-execution lineage | Reach terminal run state or explicit blocked/failure state |
| `inspect` | `Result Canvas`, `Proof Ledger`, `Delta Inspector` | Run result, Proof Bundle, State Delta, linked Artifact refs | Result shape, proof/evaluator outcome, delta state, failure basis | Operator chooses accept/branch or returns to shaping/execution with explicit reason |
| `accept/branch` | `Result Canvas` + `Strategy Board` companions | Review, Approval Decision, Branch/Compare refs, residual uncertainty | Approval conditions, branch/replay/compare choices, recommendation basis, unresolved uncertainty | Produce review/branch continuation or advance to persistence with explicit residual work |
| `persist selectively` | `Writeback Panel` with `Proof Ledger` companion | Writeback Proposal, Review, Approval Decision, apply/compensation refs | Lane-local operations, approval state, residual operations, apply result, compensation path | Produce applied, partially applied, deferred, rejected, or compensating continuation with append-only history |

## 8. Layout and progressive-disclosure rules

### 8.1 Layout rules

1. Each lifecycle stage has one primary consequential surface center; Inspector, Ledger, Compare, Timeline, Queue / Inbox, or Diff / Merge companions appear when their semantic cluster materially matters.
2. `Task Home` may aggregate resumable work, but it may not replace the stage-specific surfaces that hold contract, authority, proof, delta, or writeback truth.
3. Route, pane, and panel swaps preserve stable shared IDs and selected-object continuity; layout changes do not create new meaning-bearing objects.
4. Governance-critical semantics must not live only in `Console`; Console remains a diagnostic companion, not the primary semantic source.
5. Task Studio layout may vary cosmetically, but it may not alter the `Commission -> Contract -> Run` chain, lane separation, or handoff continuity rules.

### 8.2 Progressive-disclosure rules

1. Default views may summarize, but contract, evidence, context, strategy, authority, proof, delta, and writeback must remain one step away from the primary surface.
2. Pre-execution disclosure must expose objective/contract fit, authority scope, frozen admitted basis, proof/verifier plan, side-effect preview, writeback preview, review path, and failure/compensation posture.
3. During execution, current phase, blocked state, pending approvals, and reusable-execution lineage must remain inspectable without leaving the app model.
4. After execution, proof, delta, review, and apply state remain inspectable even when the default surface foregrounds the result.
5. Failed, blocked, and background runs may summarize by default, but they may not disappear into scheduler or monitor-only state.
6. Branch/replay/compare continuation remains explicit at the `accept/branch` stage rather than being folded into generic retry controls.

## 9. Scenario and shortcut grounding

| Task Studio area | Strongest claims / scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| Run-native commissioning loop | `TS-01`, `TS-02`, `TS-03`, `GS-12`, `EC-06` | `fs.no-master-chat-truth`, `fs.no-agent-builder-first` |
| Proof / delta / writeback inspectability | `TS-04`, `GS-07`, `GS-13`, `EC-03` | `fs.no-silent-proposal-application` |
| Handoff continuity and shared IDs | `RI-05`, `RI-08`, `GS-14`, `EC-07` | `fs.no-separate-backend-per-view`, `fs.no-master-chat-truth` |
| Task-family, branch, and planning continuity | `TS-05`, `GS-15`, `GS-16` | `fs.no-separate-backend-per-view`, `fs.no-transcript-first-rewrite-trap` |
| Reusable-execution lineage inside Task Studio | `TS-06`, `GS-10`, `GS-11`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-separate-backend-per-view` |

## 10. Boundary locks for downstream work

1. `P5.6` may narrow V1 surface exposure, onboarding, and category teaching, but it may not redefine the lifecycle loop, task-family mapping, or progressive-disclosure rules in this pack.
2. `P5.7` must preserve the exact R7 handoff payload plus the P5.4 reusable-execution refs inside Task Studio surfaces rather than recreating them as app-local metadata.
3. `P6.1` surface-contract work must map routes, modules, and layouts onto these accepted surface aliases and grammar compositions instead of redefining Task Studio semantics.
4. Task Studio remains a general commissioned-work app and must not drift into prompt-centric chat, code-editing-first ontology, or hidden orchestration theater.
5. No Task Studio surface may collapse proof, delta, review, approval, or lane-separated persistence into one persuasive or one-click convenience surface.

## 11. Downstream implications

### 11.1 For P5.6

- the V1 scope pack should choose which task families, surfaces, and disclosure paths are exposed first while preserving the lifecycle and alias rules here,
- onboarding or category-teaching refinements may narrow defaults, but they should not reclassify run classes or demote explicit governance/proof surfaces.

### 11.2 For P5.7 and P6.1

- commissioning-handoff work should use this pack as the Task Studio app-model baseline for shared IDs, reusable-execution lineage, proof/delta visibility, and lane-separated persistence,
- later route/module contracts should implement these surfaces and companions as projections over the shared object set rather than inventing app-private state machines.

## 12. Review notes

Human review should confirm that this pack:

- specifies Task Studio as a real app model rather than a future-only idea,
- keeps the commissioned-work lifecycle explicit and stage-centered,
- preserves alias-to-grammar mapping and shared-object continuity across Task Studio surfaces,
- avoids bleeding V1 scope choices or route/module implementation detail into the semantic contract.
