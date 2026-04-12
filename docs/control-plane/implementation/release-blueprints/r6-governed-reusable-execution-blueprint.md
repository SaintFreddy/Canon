# Phase 6 R6 governed reusable execution implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r6-governed-reusable-execution-blueprint.v1
Release ref: rel.r6-governed-agent-applet-chat-contract.v1
Implementation scope: Accepted R6 governed reusable-execution blueprint mapping protocol/applet/workflow objects, queue governance, tool hardening, and background parity seams onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R6 Governed Agent / Applet Chat contract into bounded implementation guidance for reusable execution objects, bounded background runs, queue/inbox governance, and tool-execution hardening.
It does not create runtime code or widen accepted release semantics.

## 1. Purpose

- map governed reusable execution onto concrete app, package, service, worker, and test clusters without inventing a second execution ontology,
- name the protocol, workflow, trigger, applet, queue, verifier, and tool-execution seams needed to keep bounded autonomy explicit and reviewable,
- preserve the accepted R6 non-goals so commissioning preflight and Task Studio handoff remain later-stage work.

## 2. Scope boundaries

### In scope

- chat-native `r6-governed-reusable-execution` and chatlet-projection route clusters over explicit protocol, workflow, trigger, applet, assignment, and queue objects,
- background-run admission, queue/inbox review, typed tool execution, sandbox hardening, and reusable-execution lineage seams,
- tests and fixtures for protocol/applet identity, queue state, authority narrowing, tool side-effect previews, and background parity.

### Out of scope

- explicit Commission/Contract preflight as the primary interaction loop,
- Task Studio handoff completion or app-private commissioning semantics,
- hidden autonomy widening, applet-private runtime semantics, or prompt assets replacing protocol/applet identity.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r6-governed-agent-applet-chat-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
| `rel.chat-native-maturity-matrix.v1` | Fixes the package-maturity floor and stage-by-stage substrate expectations that the blueprint may not undercut. |
| `rel.chat-native-milestone-architecture-plan.v1` | Fixes the release focus, explicit deferrals, and anti-overbuild rules for this stage. |
| `surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1` | Maps release work onto accepted workspace roots, route naming rules, package seams, and service/worker boundaries. |
| `surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1` | Provides the accepted documentation-plane, manifest, current-state, and packet/navigation rules for implementation-facing work. |
| `cp.phase6-workspace-manifest-index-data.v1` | Provides the accepted workspace-root map used to keep blueprint scope inside the reserved repo layout. |
| `cp.phase6-codebase-current-state-data.v1` | States which roots are materialized versus still reserved so the blueprint stays honest about current repo posture. |
| `cp.phase6-module-test-contracts-data.v1` | Defines workspace-family dependency and naming rules that the blueprint must preserve. |
| `cp.phase6-fixture-rules-data.v1` | Defines the frozen fixture-family vocabulary and validation posture that the blueprint should cite. |

## 4. Implementation blueprint

### 4.1 Workspace roots and module clusters

| Workspace root | Planned module clusters | Why touched in this release |
| --- | --- | --- |
| `apps/chat-native/` | `apps/chat-native/r6-governed-reusable-execution/`<br>`apps/chat-native/r6-chatlet-projection/` | Implements governed reusable execution, queue/inbox governance, chatlet projections, and bounded background-run affordances promised by R6. |
| `packages/` | `packages/projection-grammar/reusable-execution-projection/`<br>`packages/shared-object-schemas/reusable-execution/`<br>`packages/shared-object-api/governed-execution/`<br>`packages/model-gateway-contracts/reusable-run-execution/`<br>`packages/tool-gateway-contracts/tool-execution-policy/`<br>`packages/review-writeback-contracts/queue-review/`<br>`packages/event-provenance-contracts/reusable-execution-lineage/`<br>`packages/monitor-inspect/queue-inbox/` | Provides protocol/applet/workflow, model/tool gateway, queue/review, provenance, and inspect seams for bounded reusable execution. |
| `services/` | `services/execution-control/background-run-admission/`<br>`services/model-gateway/reusable-run-execution/`<br>`services/tool-gateway/typed-tool-execution/`<br>`services/review-writeback/queue-review/`<br>`services/event-provenance/applet-lineage/` | Coordinates reusable execution launches, typed provider/tool execution, queue review, and append-only lineage. |
| `workers/` | `workers/tool-sandbox/policy-bounded-run/`<br>`workers/apply-writeback/background-proposal-apply/`<br>`workers/replay-compare/protocol-version-compare/` | Executes sandboxed tool work, background proposal apply, and version compare over reusable execution refs. |
| `tests/` | `tests/contracts/r6-governed-reusable-execution/`<br>`tests/fixtures/r6-governed-reusable-execution/` | Covers protocol/applet identity, queue governance, authority narrowing, tool side-effect previews, and interactive/background parity. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Reusable execution substrate | `Protocol`, `Context Recipe`, `Strategy Preset`, `Verifier Pack`, `Workflow`, `Trigger`, `Applet`, and `Assignment` remain explicit shared objects over accepted run semantics. | Do not let agent profiles, chatlets, or applet settings become a second execution ontology. |
| Queue and tool hardening | Queue review, typed tool execution, side-effect classification, and sandbox policy remain explicit contracts and lineage-bearing objects. | Do not hide authority or tool consequences in notifications, prompt text, or surface arrangement. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Reusable execution launch flow | Route protocol/applet launches through execution-control, model-gateway, and review/writeback seams with explicit queue state. | Interactive and background launches must emit the same run/proof/delta/writeback object families. |
| Tool execution and queue review | Serve side-effect-classified tool execution through typed tool-gateway and sandbox workers, with queue review surfacing proof and delta context. | Background work may narrow behavior only through explicit policy; never widen authority silently. |

### 4.4 Storage, provenance, and migration posture

1. Persist protocol/applet/workflow versions, queue transitions, verifier outcomes, and tool events as append-only lineage linked to the same shared run objects.
2. Keep prompt assets as upstream inputs referenced by lineage rather than execution identity replacements.
3. Do not introduce commissioning-specific contract/amendment storage or Task Studio-only metadata in this release.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Reusable execution browser | protocol/app browsing, version pins, applet details, reusable-input inspection | R6 reusable-execution continuity promise. |
| Queue and inbox governance | queue board, inbox next actions, approval/failure surfacing, contradiction guard visibility | R6 queue/inbox and governance requirements. |
| Chatlet and tool supervision | chatlet projection, background-run status, typed tool result/failure inspection, side-effect previews | R6 tool-hardening and bounded background-run obligations. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression`<br>`background_parity` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for protocol/applet identity, queue object continuity, and explicit verifier/tool-policy bindings.<br>Edge coverage for authority narrowing, tool side-effect previews, and refusal of hidden autonomy widening.<br>Regression and background-parity coverage for interactive/background equivalence over run, proof, delta, and writeback objects. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize Commission/Contract preflight, Task Studio handoff routes, or bridge-private task taxonomy inside the R6 cluster.
- Do not allow applet settings, triggers, or chatlets to bypass verifier slots, queue review, or lane-separated writeback.
- Do not treat prompt cards or prompt assets as substitutes for protocol, workflow, trigger, or applet identity.

## 5. Acceptance notes

- This blueprint remains a bounded build plan for governed reusable execution and must preserve the R5 prompt-asset substrate unchanged beneath it.
- Human implementation review should confirm that every reusable-execution flow stays composed from accepted run semantics with explicit governance.
