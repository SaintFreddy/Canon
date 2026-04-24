# Phase 6 R1 conversation implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r1-conversation-blueprint.v1
Release ref: rel.r1-transcript-chat-contract.v1
Implementation scope: Accepted R1 conversation blueprint mapping bounded chat-native conversation modules, run/context substrate seams, tests, fixtures, and explicit exclusions onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R1 Transcript Chat contract into bounded implementation guidance for familiar conversation entry, bounded run execution, compact inspection, and resume continuity.
It does not create runtime code or widen accepted release semantics.

> **Platform Gate reopen notice (2026-04-23).** This blueprint transitively depends on `arch.phase3-platform-gate-spec.v1`. On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the Platform Gate P3.6 acceptance marker against the 2026-04-18 agentic-engine audit-cited contradiction event per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A). Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`. This blueprint itself remains `accepted` for downstream use — the implementation guidance below is unchanged and the release doctrine is not reopened. Consumers reading this blueprint should, however, be aware that PG-01.1 (Clock + stableStringify + localeCompare + frozenAt), PG-07.1 (credentialScope enforcement), and PG-10.1 (spawnToolSandboxWorker + IPC export) are remediation sub-gates still closing. Engine sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (see `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0089..CF-0096); the sub-gates formally close after PG-R3 (maturity-matrix + milestone-plan sync) lands. See `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 for the full gate reopen markup and successor-checkpoint reference.

## 1. Purpose

- map the R1 familiar-chat promise onto concrete app, package, service, worker, and test clusters without reintroducing transcript truth,
- name the minimum shared-object and control-plane seams needed for run identity, source traceability, compact inspection, and resume behavior,
- preserve the accepted R1 non-goals so later context, branch, artifact, reuse, and commissioning work are not pre-spent early.

## 2. Scope boundaries

### In scope

- chat-native `r1-conversation` and compact-inspect route clusters over shared objects and projection grammar,
- bounded run admission, context compilation, provider invocation, and event/provenance trace seams for first-release chat turns,
- tests and fixtures for run identity, source-chip resolution, rerun behavior, and transcript-continuity loss edge cases.

### Out of scope

- full evidence/context editing or pack-freeze UX,
- semantic branching, artifact workspace governance, or prompt-asset lineage,
- governed reusable execution, commissioning preflight, or Task Studio handoff.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r1-transcript-chat-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
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
| `apps/chat-native/` | `apps/chat-native/r1-conversation/`<br>`apps/chat-native/r1-compact-inspect/` | Implements the bounded conversation surface, source chips, compact proof/context drawer, and resume affordances promised by R1. |
| `packages/` | `packages/projection-grammar/chat-thread-projection/`<br>`packages/shared-object-schemas/run-and-source/`<br>`packages/shared-object-api/run-continuity/`<br>`packages/environment-control-contracts/run-launch/`<br>`packages/context-compiler-contracts/admitted-basis/`<br>`packages/model-gateway-contracts/chat-turn/`<br>`packages/event-provenance-contracts/run-lineage/`<br>`packages/monitor-inspect/compact-run-inspect/` | Provides the shared-object, compiler, gateway, provenance, and inspect contracts that keep R1 chat projection-only over the accepted substrate. |
| `services/` | `services/environment-shell-api/conversation-entry/`<br>`services/execution-control/run-dispatch/`<br>`services/model-gateway/chat-turn-execution/`<br>`services/event-provenance/run-trace/` | Provides typed entry, dispatch, model execution, and append-only trace seams behind R1 conversation turns. |
| `workers/` | `workers/context-compiler/compile-run-context/` | Compiles the frozen admitted basis behind each R1 assistant answer without moving truth back into transcript state. |
| `tests/` | `tests/contracts/r1-conversation/`<br>`tests/fixtures/r1-conversation/` | Covers run identity, source-bearing inspection, rerun identity, and compact-inspection continuity. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Shared object substrate | `Run`, `Thread / Line`, `Source Reference`, `Context Pack` snapshot, and `Proof Bundle` summary remain explicit shared objects with stable refs. | Do not let `Message Block` or transcript surfaces become the consequential truth anchor. |
| Projection grammar and UI helpers | `chat-thread-projection` and compact-inspect helpers may compose shared objects into R1 chat surfaces and source-chip affordances. | Keep all projection helpers below shared-object and contract seams; no app-private truth models. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Run admission and execution | Route conversation entry through typed environment-control contracts into execution-control dispatch and context compilation. | Every consequential answer must remain a distinct bounded run with a stable `run_id`. |
| Source and proof inspection | Serve compact inspection from monitor/inspect plus event-provenance reads instead of transcript-local guesses. | Source chips must resolve to source-bearing objects or stable source regions. |

### 4.4 Storage, provenance, and migration posture

1. Persist run/result/source lineage through append-only event/provenance records; do not treat provider transcript continuity as durable state.
2. Keep resume continuity tied to shared thread and run refs rather than provider-managed conversation state.
3. No artifact-centered revision or branch/checkpoint storage lands in this release.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Conversation surface | new-thread, continue-thread, bounded-run result, regenerate-to-new-run | R1 familiar chat promise with run truth preserved under the surface. |
| Compact inspection | source chips, compact proof summary, compact admitted-basis drawer | R1 compact-inspection rule and exit criteria. |
| Resume continuity | resume packet, since-last-run indicators, loss-of-provider-continuity fallback | R1 handoff obligation into R2 without transcript-truth shortcuts. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for run identity, source-chip resolution, and rerun-as-new-run behavior.<br>Edge coverage for provider-transcript loss and compact-inspection fallback paths.<br>Regression coverage for thread resume continuity over stable shared-object refs. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize pack-editing, branch-map, artifact-governance, or applet-builder modules inside the R1 cluster.
- Do not add direct UI-to-worker RPC or provider-specific transcript state as the only resume mechanism.
- Do not collapse source, proof, or context inspection into decorative chat chrome.

## 5. Acceptance notes

- This blueprint remains a bounded build plan over currently reserved runtime roots; it does not claim those roots are already implemented.
- Human implementation review should confirm that R1 stays familiar at the surface while remaining fully run-backed beneath it.
