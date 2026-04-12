# Phase 6 R2 context control implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r2-context-control-blueprint.v1
Release ref: rel.r2-context-chat-contract.v1
Implementation scope: Accepted R2 context-control blueprint mapping explicit evidence/context operations, pack lineage seams, tests, fixtures, and deferrals onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R2 Context Chat contract into bounded implementation guidance for inspectable evidence/context control, pack operations, memory/canon visibility, and replayable pack lineage.
It does not create runtime code or widen accepted release semantics.

## 1. Purpose

- map real pack control onto concrete app, package, service, worker, and test clusters without reducing it to sidebar theater,
- keep Evidence Pack and Context Pack semantics explicit while naming the compiler, replay, and provenance seams required to make pack freeze and diff real,
- preserve the accepted R2 non-goals so branching, artifact governance, reusable execution, and commissioning are not pre-spent.

## 2. Scope boundaries

### In scope

- chat-native `r2-context-control` and pack-inspect route clusters over explicit evidence/context, memory, and canon objects,
- pack operations, freeze/diff handling, pack lineage, and context-operation execution seams,
- tests and fixtures for includes/exclusions, memory/canon visibility, pack freeze/diff, and replayable admitted bases.

### Out of scope

- semantic branch maps or checkpoint-first exploration,
- artifact-centered continuity as the visible center,
- reusable execution packaging, commissioning preflight, or hidden memory/canon influence.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r2-context-chat-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
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
| `apps/chat-native/` | `apps/chat-native/r2-context-control/`<br>`apps/chat-native/r2-pack-inspect/` | Implements evidence/context inspection, pack editing, freeze/diff views, and explicit memory/canon controls promised by R2. |
| `packages/` | `packages/projection-grammar/context-control-projection/`<br>`packages/shared-object-schemas/pack-lineage/`<br>`packages/shared-object-api/pack-control/`<br>`packages/context-compiler-contracts/context-operations/`<br>`packages/replay-compare-contracts/pack-basis-diff/`<br>`packages/event-provenance-contracts/pack-lineage/`<br>`packages/monitor-inspect/context-pack-inspect/` | Provides the shared pack lineage, context-operation, replay, provenance, and inspect seams required for real pack control. |
| `services/` | `services/environment-shell-api/context-operations/`<br>`services/execution-control/rerun-from-pack/`<br>`services/event-provenance/pack-lineage/` | Coordinates pack mutations, reruns, and append-only lineage over typed control contracts. |
| `workers/` | `workers/context-compiler/pack-freeze-diff/`<br>`workers/replay-compare/pack-basis-compare/` | Executes freeze/diff and replay-oriented basis comparison over explicit admitted-basis inputs. |
| `tests/` | `tests/contracts/r2-context-control/`<br>`tests/fixtures/r2-context-control/` | Covers pack include/exclude/pin, memory/canon attribution, pack freeze/diff, and replayable lineage. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Evidence vs. Context Pack substrate | `Evidence Pack`, `Context Pack`, `Memory Object`, `Canon Object`, and pack-lineage refs remain separate shared objects with explicit include/exclude semantics. | Do not let memory or canon silently rewrite admitted evidence or hide in prompt text. |
| Pack operations and basis diff | `Context Operation`, `Pack Diff`, `Pack Freeze`, and replay-basis diff seams remain typed compiler/replay contracts. | Do not reduce pack changes to prompt-string substitutions or UI-local diff state. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Pack control flow | Route include/exclude/pin and context operations through environment-control contracts into compiler and replay workers. | Pack changes must produce explicit pack-state lineage and rerunnable admitted bases. |
| Inspection and lineage | Serve evidence/context views, memory/canon attribution, and pack diffs from monitor/inspect plus event/provenance reads. | Pack state must follow the run and remain replayable beyond transcript or sidebar state. |

### 4.4 Storage, provenance, and migration posture

1. Persist pack freezes and diffs as append-only admitted-basis lineage, not mutable sidebar state.
2. Memory and canon injections remain attributable, removable, and scoped to explicit pack refs where policy allows.
3. No branch checkpoint or artifact revision storage lands in this release.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Evidence/context control | inspect evidence pack, inspect context pack, include/exclude/pin, memory/canon controls | R2 pack-control promise and explicit-memory rule. |
| Pack diff and freeze | freeze admitted basis, compare pack revisions, replay from frozen basis | R2 exit criteria around pack freeze and basis diff. |
| Context operations | span targeting, span-set operations, lens-driven summarize/extract/compact flows | R2 projection-only additions for span-based context work. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for pack include/exclude/pin semantics and explicit memory/canon attribution.<br>Edge coverage for hidden-memory refusal, pack-state replay, and freeze/diff gaps.<br>Regression coverage for pack lineage staying stable across reruns and diff views. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize branch graphs, artifact inboxes, or reusable execution builders inside the R2 cluster.
- Do not let pack controls become sidebar-only affordances without real compiler and provenance effects.
- Do not store memory/canon influence as opaque UI state or hidden provider lore.

## 5. Acceptance notes

- This blueprint remains a bounded build plan for explicit pack control and must preserve the R1 run-backed substrate unchanged.
- Human implementation review should confirm that every visible pack control maps back to real admitted-basis lineage.
