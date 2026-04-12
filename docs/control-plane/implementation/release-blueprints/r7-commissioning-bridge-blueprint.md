# Phase 6 R7 commissioning bridge implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r7-commissioning-bridge-blueprint.v1
Release ref: rel.r7-commissioning-bridge-contract.v1
Implementation scope: Accepted R7 commissioning-bridge blueprint mapping commission/contract preflight, live monitoring, ledger/delta review, and Task Studio-safe handoff seams onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R7 Commissioning Bridge contract into bounded implementation guidance for Commission -> Contract -> Run preflight, live monitoring, proof/delta/writeback review, and Task Studio-safe handoff continuity.
It does not create runtime code or widen accepted release semantics.

## 1. Purpose

- map explicit commissioning and handoff continuity onto concrete chat-native, Task Studio, package, service, worker, and test clusters without inventing bridge-private ontology,
- name the preflight, authority, monitor, proof, delta, writeback, and handoff seams needed to keep serious work explicit and shared-ID-safe,
- preserve the accepted R7 non-goals so Phase 5 deepening and broader Task Studio implementation do not get pre-spent here.

## 2. Scope boundaries

### In scope

- chat-native `r7-commissioning-bridge` plus Task Studio handoff-receiver route clusters over explicit Commission, Contract, Authority Scope, Run, Proof Bundle, State Delta, Writeback Proposal, and Handoff objects,
- preflight admission, authority review, live monitoring, ledger/delta/writeback review, and handoff continuity seams that preserve shared IDs across chat and Task Studio,
- tests and fixtures for preflight, failure-state continuity, lane-separated decisions, shared-ID handoff payloads, and downstream Task Studio landing integrity.

### Out of scope

- Phase 5 proof/evaluation/governance deepening beyond the already accepted reusable-semantics packs,
- Task Studio rewrite or app-private task semantics beyond the preserved handoff payload,
- bridge-private run classes, lane-collapsing writeback convenience, or second truth models in monitor/ledger/delta views.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r7-commissioning-bridge-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
| `rel.chat-native-maturity-matrix.v1` | Fixes the package-maturity floor and stage-by-stage substrate expectations that the blueprint may not undercut. |
| `rel.chat-native-milestone-architecture-plan.v1` | Fixes the release focus, explicit deferrals, and anti-overbuild rules for this stage. |
| `surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1` | Maps release work onto accepted workspace roots, route naming rules, package seams, and service/worker boundaries. |
| `surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1` | Provides the accepted documentation-plane, manifest, current-state, and packet/navigation rules for implementation-facing work. |
| `cp.phase6-workspace-manifest-index-data.v1` | Provides the accepted workspace-root map used to keep blueprint scope inside the reserved repo layout. |
| `cp.phase6-codebase-current-state-data.v1` | States which roots are materialized versus still reserved so the blueprint stays honest about current repo posture. |
| `cp.phase6-module-test-contracts-data.v1` | Defines workspace-family dependency and naming rules that the blueprint must preserve. |
| `cp.phase6-fixture-rules-data.v1` | Defines the frozen fixture-family vocabulary and validation posture that the blueprint should cite. |
| `surf.phase6-task-studio-surface-contract-pack.v1` | Defines the accepted Task Studio route-contract landings and R7 -> Task Studio continuity surface mapping. |
| `reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1` | Defines the accepted preserved handoff payload and shared-ID continuity requirements from R7 into Task Studio. |

## 4. Implementation blueprint

### 4.1 Workspace roots and module clusters

| Workspace root | Planned module clusters | Why touched in this release |
| --- | --- | --- |
| `apps/chat-native/` | `apps/chat-native/r7-commissioning-bridge/`<br>`apps/chat-native/r7-live-monitor/`<br>`apps/chat-native/r7-chat-to-run-handoff/` | Implements commission cards, contract drafts, run preflight, live monitor, acceptance stack, and handoff affordances promised by R7. |
| `apps/task-studio/` | `apps/task-studio/ts-sc-01-task-home/`<br>`apps/task-studio/ts-sc-03-task-contract-panel/`<br>`apps/task-studio/ts-sc-05-context-inspector/`<br>`apps/task-studio/ts-sc-07-authority-panel/`<br>`apps/task-studio/ts-sc-08-live-run-view/`<br>`apps/task-studio/ts-sc-10-proof-ledger/`<br>`apps/task-studio/ts-sc-11-delta-inspector/`<br>`apps/task-studio/ts-sc-12-writeback-panel/` | Implements the Task Studio handoff landings required to preserve shared IDs and review continuity after R7 chat commissioning. |
| `packages/` | `packages/projection-grammar/commissioning-projection/`<br>`packages/shared-object-schemas/commissioning/`<br>`packages/shared-object-api/commissioning/`<br>`packages/environment-control-contracts/commission-preflight/`<br>`packages/review-writeback-contracts/acceptance-stack/`<br>`packages/replay-compare-contracts/contract-diff/`<br>`packages/tool-gateway-contracts/commissioned-side-effects/`<br>`packages/monitor-inspect/commissioning-monitor/` | Provides commissioning, preflight, review, compare, tool-preview, and inspect seams for explicit serious-work governance. |
| `services/` | `services/environment-shell-api/commission-preflight/`<br>`services/execution-control/contract-launch/`<br>`services/review-writeback/acceptance-stack/`<br>`services/event-provenance/commission-lineage/`<br>`services/model-gateway/commissioned-run-execution/`<br>`services/tool-gateway/commissioned-tool-preview/` | Coordinates commissioning preflight, consequential run launch, acceptance-stack review, and append-only commissioning lineage. |
| `workers/` | `workers/context-compiler/preflight-basis-freeze/`<br>`workers/replay-compare/contract-delta-compare/`<br>`workers/apply-writeback/commission-writeback-apply/`<br>`workers/tool-sandbox/commissioned-side-effect-preview/` | Executes frozen-basis preflight, contract-delta compare, lane-separated writeback apply, and side-effect previews for commissioned work. |
| `tests/` | `tests/contracts/r7-commissioning-bridge/`<br>`tests/fixtures/r7-commissioning-bridge/` | Covers Commission -> Contract -> Run continuity, preflight/monitor/ledger/delta behavior, lane-separated review, and Task Studio-safe handoff continuity. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Commissioning substrate | `Commission`, `Contract`, `Run Class`, `Authority Scope`, `Run`, `Proof Bundle`, `State Delta`, `Writeback Proposal`, `Review`, `Approval Decision`, and `Handoff` remain explicit shared objects with stable shared IDs. | Do not let commission cards, acceptance stacks, or handoff surfaces become replacement truth models. |
| Task Studio-safe handoff | Task Studio route landings remain projections over the same shared commissioning payload and reusable-execution lineage. | Do not recreate objects, translate ontology, or collapse lane separation during handoff. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Preflight and execution flow | Route Commission -> Contract -> Run preflight through environment-control, execution-control, compiler freeze, and review/writeback seams. | Scope widening or consequential execution must remain blocked until explicit authority scope and contract review exist. |
| Monitoring, review, and handoff flow | Serve live monitor, proof ledger, delta inspector, acceptance stack, and handoff payload through monitor/inspect, review-writeback, provenance, and compare seams. | Failed and blocked runs must keep proof/delta visibility, and Task Studio handoff must preserve shared IDs unchanged. |

### 4.4 Storage, provenance, and migration posture

1. Persist commission, contract amendment, preflight, run, review, approval, writeback, and handoff lineage as append-only records tied to stable shared IDs.
2. Keep Task Studio handoff payloads as preserved shared-object continuity rather than export/import blobs or app-private task metadata.
3. Do not hide authority or side-effect previews in chat-only state, monitor-only state, or Task Studio-only metadata.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Chat-side commissioning | commission card, contract draft, run preflight, acceptance stack, chat-to-run handoff | R7 commissioning and preflight promise inside chat. |
| Live monitor and review | live monitor, proof ledger, delta inspector, lane-by-lane writeback review, failure-state continuity | R7 monitor/ledger/delta/writeback review obligations. |
| Task Studio landing continuity | TS-SC-01/03/05/07/08/10/11/12 preserved-object landing paths | Accepted R7 -> Task Studio handoff and P6.1 Task Studio surface contract mapping. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression`<br>`handoff_continuity` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for Commission -> Contract -> Run identity, authority preflight, and preserved shared IDs across handoff.<br>Edge coverage for blocked/failing commissioned work, lane-separated review, and refusal of bridge-private taxonomy or silent escalation.<br>Regression and handoff-continuity coverage for Task Studio route landing, proof/delta visibility, and writeback continuity after handoff. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize bridge-private task objects, silent writeback convenience, or hidden authority escalation inside chat or Task Studio surfaces.
- Do not recreate commissioning payloads as Task Studio-only metadata or translate them into a new ontology.
- Do not collapse proof, delta, review, approval, or handoff continuity into persuasive monitor prose or UI-local state.

## 5. Acceptance notes

- This blueprint remains a bounded build plan for explicit commissioning and Task Studio-safe continuity; it must preserve the R6 governed-reuse substrate unchanged beneath it.
- Human implementation review should confirm that every handoff preserves shared IDs, lane separation, and preflight/monitor/ledger/delta continuity end to end.
