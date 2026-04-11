# Phase 6 Task Studio surface contract pack
Version: 1.0
Status: Review-ready
Task: P6.1 — Surface contract packs
Artifact ID: surf.phase6-task-studio-surface-contract-pack.v1
Surface scope: Review-ready Phase 6 Task Studio surface contract pack mapping named Task Studio surfaces, route contracts, lifecycle landings, and R7 handoff continuity onto the shared grammar

This artifact is review-ready for human acceptance.
It turns the accepted Task Studio surface/lifecycle baseline plus the review-ready P5.6/P5.7 support packs into a Phase 6 route-contract layer.
It does not define concrete URL paths, packages, or components.

## 1. Purpose

This pack defines the Task Studio surface contracts that later route, module, and component work must implement.

It exists to:

- map each named Task Studio surface to a stable route-contract and shared grammar composition,
- make lifecycle-primary and companion-surface expectations explicit,
- apply the review-ready V1 overlay and the review-ready R7 handoff continuity rules at the surface-contract layer.

## 2. Scope boundaries

### In scope

- Task Studio named surface contracts,
- lifecycle route and companion-surface matrix,
- V1 overlay rules for surface emphasis and landing behavior,
- R7 -> Task Studio handoff landing and continuity rules.

### Out of scope

- repo/package/module architecture,
- concrete URL paths, filesystem layout, or component hierarchies,
- changes to Task Studio semantics already fixed in `P5.5`,
- changes to V1 scope or handoff meaning beyond the review-ready P5.6/P5.7 support boundary.

## 3. Task Studio interpretation rules

### 3.1 Route-contract-not-module rule

A Task Studio surface contract names a stable route-level work area and its required grammar composition.
It does not by itself dictate package boundaries, component files, or implementation framework structure.

### 3.2 Named-surface-to-grammar rule

Every Task Studio surface alias must resolve to the exact accepted grammar composition already fixed in `P5.5`.
No Task Studio route may create a new grammar family or a Task Studio-private replacement object.

### 3.3 Lifecycle-primary-plus-companion rule

Each commissioned-work stage keeps one primary route-contract surface and a constrained set of companion surfaces when proof, delta, compare, branching, or apply semantics materially matter.
Companions enrich the same shared objects; they do not replace them.

### 3.4 V1-overlay rule

The review-ready `P5.6` V1 scope pack narrows default emphasis, primary-vs-companion posture, and landing preference only.
This pack therefore keeps route contracts stable while allowing a review-ready home-first versus stage-first landing preference over the same object graph.

### 3.5 R7-handoff-continuity rule

The review-ready `P5.7` handoff contract defines exact payload preservation from R7 into Task Studio.
This pack therefore treats handoff as a route-selection and surface-cluster problem over the same shared objects rather than a new intake or transfer ontology.

## 4. Route-contract summary

| Route contract ID | Surface alias | Shared grammar composition | Primary shared objects | Minimum companions when materially relevant |
| --- | --- | --- | --- | --- |
| `TS-SC-01` | `Task Home` | `Browser / Library + Queue / Inbox + Board` | `Commission`, `Contract`, `Run`, `Assignment`, workflow/applet refs | `Inspector` when a selection expands |
| `TS-SC-02` | `New Commission Sheet` | `Composer + Inspector` | draft `Commission`, `Source Reference`, task-family/run-class framing | `Browser / Library` for source pick-up when needed |
| `TS-SC-03` | `Task Contract Panel` | `Inspector` with structured edit affordances | `Contract`, run class, protocol/version pins, acceptance policy | `Evidence Pack Builder`, `Context Inspector`, `Authority Panel` as needed |
| `TS-SC-04` | `Evidence Pack Builder` | `Browser / Library + Inspector + Compare View` | `Evidence Pack`, `Source Reference`, inclusion/exclusion state | `Task Contract Panel`, `Context Inspector` |
| `TS-SC-05` | `Context Inspector` | `Inspector` | `Context Pack`, frozen admitted basis, context lineage | `Task Contract Panel`, `Authority Panel` |
| `TS-SC-06` | `Strategy Board` | `Board + Inspector + Compare View` | plan/branch state, option set, workflow-stage clusters | `Result Canvas`, `Task Contract Panel` |
| `TS-SC-07` | `Authority Panel` | `Inspector` | `Authority Scope`, review path, side-effect preview, writeback preview | `Task Contract Panel`, `Proof Ledger`, `Context Inspector` |
| `TS-SC-08` | `Live Run View` | `Live Monitor + Timeline + Inspector + Console` | `Run`, workflow/app context, child runs, pending approvals | none beyond built-in composition |
| `TS-SC-09` | `Result Canvas` | `Canvas` | run result, linked `Artifact`, next consequential actions | `Proof Ledger`, `Delta Inspector`, `Strategy Board` as needed |
| `TS-SC-10` | `Proof Ledger` | `Ledger` | `Proof Bundle`, evaluator results, `Review`, `Approval Decision` | `Result Canvas`, `Writeback Panel` |
| `TS-SC-11` | `Delta Inspector` | `Inspector` with `Diff / Merge View` companion | `State Delta`, target refs, lane-separated change state | `Result Canvas`, `Writeback Panel` |
| `TS-SC-12` | `Writeback Panel` | `Diff / Merge View + Ledger + Queue / Inbox` | `Writeback Proposal`, `Review`, `Approval Decision`, apply/compensation refs | `Proof Ledger`, `Delta Inspector` |

## 5. Lifecycle route matrix

| Lifecycle stage | Primary route contract | Required companions | Surface-contract rule |
| --- | --- | --- | --- |
| `commission` | `TS-SC-01` or `TS-SC-02` | `Inspector`, `Browser / Library` as needed | Intake remains explicit and source-grounded; resumable identity stays visible |
| `interpret` | `TS-SC-03` / `TS-SC-04` / `TS-SC-05` / `TS-SC-06` | Compare and browse companions as needed | Contract, evidence, context, and strategy shaping stay inspectable rather than chat-private |
| `lock` | `TS-SC-07` with `TS-SC-03` companion | `TS-SC-05`, `TS-SC-10` when review context is material | Authority scope, frozen basis, proof plan, and side-effect preview remain explicit before execution |
| `execute` | `TS-SC-08` | built-in `Timeline`, `Inspector`, `Console` composition | Active, blocked, background, and resumed runs share the same supervision contract |
| `inspect` | `TS-SC-09` | `TS-SC-10`, `TS-SC-11` | Result, proof, and delta remain a single consequential cluster |
| `accept/branch` | `TS-SC-09` | `TS-SC-10`, `TS-SC-11`, `TS-SC-06` | Branch/replay choices remain explicit instead of generic retry controls |
| `persist selectively` | `TS-SC-12` | `TS-SC-10`, `TS-SC-11` | Lane-by-lane apply and compensation remain attributable and inspectable |

## 6. V1 overlay and landing rules

1. V1 may prefer a home-first landing (`TS-SC-01`) or a stage-first landing, but both must preserve the same shared-object selection and deep links into the lifecycle-primary contract above.
2. `TS-SC-06` (`Strategy Board`) remains companion-first in V1 unless planning/branching is the current consequential center.
3. Artifact-lane review/apply is the V1 default happy-path persistence posture; non-artifact lanes remain explicit and recoverable from the same route contracts even when deferred.
4. Reusable-execution refs remain inspectable in `TS-SC-03`, `TS-SC-05`, `TS-SC-07`, and `TS-SC-08`; V1 does not add builder, marketplace, or secret-management routes.
5. No V1 route may collapse proof, delta, review, or writeback into a hidden drawer or persuasive result blob.

## 7. R7 handoff continuity contract

### 7.1 Handoff landing matrix

| R7 projection or state | Task Studio route contract landing | Continuity rule |
| --- | --- | --- |
| `Commission Card` | `TS-SC-01` or `TS-SC-02` | Continue shaping or resuming the same `Commission` and linked `Contract` without task-shell recreation |
| `Contract Draft` | `TS-SC-03` | Preserve the same `Contract` record, run class, and amendment lineage |
| `Run Preflight` | `TS-SC-03` + `TS-SC-07` + `TS-SC-05` | Preserve contract, authority, and frozen admitted basis as the same shared objects |
| `Live Monitor` / active run | `TS-SC-08` | Preserve the same `Run`, approvals, child-run lineage, and diagnostics refs |
| `Proof Ledger` | `TS-SC-10` | Preserve the same `Proof Bundle`, `Review`, and `Approval Decision` records |
| `Delta Inspector` | `TS-SC-11` | Preserve the same `State Delta` and target refs |
| `Acceptance Stack` | `TS-SC-10` + `TS-SC-11` + `TS-SC-12` | Decompose proof/review, delta, and apply surfaces without inventing a replacement object |
| `Chat-to-Run Handoff` | `TS-SC-01` or lifecycle-primary deep link | Act as a route/selection envelope only, not export/import or semantic translation |

### 7.2 Continuity locks

1. Shared IDs and lineage refs remain unchanged across the handoff, including reusable-execution refs when materially relevant.
2. `Acceptance Stack` remains an alias/composition over proof, delta, review, approval, and writeback surfaces rather than a new shared object.
3. Failed, blocked, background, and resumed runs remain inspectable through the same route contracts; no failure state disappears into scheduler-only or monitor-only storage.
4. This review-ready pack does not invent a mandatory `handoff_id` or any other Task Studio-private transfer object.

## 8. Boundary locks for downstream work

1. `P6.2` may map packages and modules around these route contracts, but it may not reinterpret Task Studio semantics or the R7 payload.
2. No Task Studio route contract may create a second truth model beneath the named surface aliases.
3. `Console` remains diagnostic only; it may not be the only place where governance-critical semantics are available.
4. This pack stays `review_ready` until the review-ready P5.6/P5.7 support packs are human-accepted or otherwise resolved.

## 9. Downstream implications

### 9.1 For later route/module work

- route, module, and component planning should use these route-contract IDs and grammar compositions as the Task Studio implementation baseline,
- presentation and navigation may vary, but the named surfaces, companions, and lifecycle-primary ownership may not drift.

### 9.2 For later acceptance work

- once P5.6 and P5.7 are human-accepted, this pack can be promoted from `review_ready` to `accepted` without re-deriving Task Studio routes from scratch.

## 10. Review notes

Human review should confirm that this pack:

- maps each named Task Studio surface to one stable route-contract and grammar composition,
- keeps lifecycle-primary versus companion surface ownership explicit,
- honors the review-ready V1 overlay and the review-ready R7 handoff contract without semantic drift,
- avoids inventing concrete module/package/URL detail that belongs to `P6.2`.
