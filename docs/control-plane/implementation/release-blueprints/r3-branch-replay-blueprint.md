# Phase 6 R3 branch replay implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r3-branch-replay-blueprint.v1
Release ref: rel.r3-branch-visual-thinker-contract.v1
Implementation scope: Accepted R3 branch-replay blueprint mapping semantic branch, checkpoint, compare, and merge-proposal seams onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R3 Branch / Visual Thinker contract into bounded implementation guidance for branch identity, checkpointed replay, mode projections, off-chain returns, and merge proposals.
It does not create runtime code or widen accepted release semantics.

> **Platform Gate reopen notice (2026-04-23).** This blueprint transitively depends on `arch.phase3-platform-gate-spec.v1`. On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the Platform Gate P3.6 acceptance marker against the 2026-04-18 agentic-engine audit-cited contradiction event per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A). Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`. This blueprint itself remains `accepted` for downstream use — the implementation guidance below is unchanged and the release doctrine is not reopened. Consumers reading this blueprint should, however, be aware that PG-01.1 (Clock + stableStringify + localeCompare + frozenAt), PG-07.1 (credentialScope enforcement), and PG-10.1 (spawnToolSandboxWorker + IPC export) are remediation sub-gates still closing. Engine sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (see `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0089..CF-0096); the sub-gates formally close after PG-R3 (maturity-matrix + milestone-plan sync) lands. See `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 for the full gate reopen markup and successor-checkpoint reference.

## 1. Purpose

- map semantic branching and replay onto concrete app, package, service, worker, and test clusters without falling back to transcript clones,
- name the checkpoint, compare, provenance, and proposal seams needed to keep branch identity explicit and replayable,
- preserve the accepted R3 non-goals so artifact governance, prompt-asset lineage, reusable execution, and commissioning remain later-stage work.

## 2. Scope boundaries

### In scope

- chat-native `r3-branch-replay` and mode-projection route clusters over explicit branch, checkpoint, compare, and merge-proposal objects,
- checkpoint capture, replay execution, compare views, off-chain returns, and merge-proposal review seams,
- tests and fixtures for branch identity, checkpoint-based replay, mode projection continuity, and merge-proposal lineage.

### Out of scope

- artifact-centered continuity as the visible center,
- prompt-asset governance or reusable execution packaging,
- commissioning preflight, Task Studio handoff, or transcript cloning as branch truth.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r3-branch-visual-thinker-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
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
| `apps/chat-native/` | `apps/chat-native/r3-branch-replay/`<br>`apps/chat-native/r3-mode-projection/` | Implements branch graph, replay/compare, mode switches, and merge-proposal affordances promised by R3. |
| `packages/` | `packages/projection-grammar/branch-projection/`<br>`packages/shared-object-schemas/branch-checkpoint-delta/`<br>`packages/shared-object-api/branch-lineage/`<br>`packages/replay-compare-contracts/branch-replay/`<br>`packages/review-writeback-contracts/merge-review/`<br>`packages/event-provenance-contracts/branch-lineage/`<br>`packages/monitor-inspect/branch-compare/` | Provides branch, checkpoint, replay, proposal, provenance, and inspect seams for semantic branch work. |
| `services/` | `services/execution-control/checkpoint-launch/`<br>`services/review-writeback/merge-proposals/`<br>`services/event-provenance/branch-history/` | Coordinates replay launches, explicit merge proposals, and append-only branch/checkpoint lineage. |
| `workers/` | `workers/replay-compare/checkpoint-replay/`<br>`workers/replay-compare/branch-compare/` | Executes exact replay and branch compare against explicit checkpoint and pack lineage. |
| `tests/` | `tests/contracts/r3-branch-replay/`<br>`tests/fixtures/r3-branch-replay/` | Covers branch identity, checkpoint-based replay, compare stability, and explicit merge-proposal returns. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Branch and checkpoint substrate | `Branch`, `Checkpoint`, `State Delta`, and `Merge Proposal` remain explicit shared objects linked back to runs and pack lineage. | Do not let transcript duplication or mode-local state stand in for branch identity. |
| Mode projection and off-chain return | `Mode Projection`, off-chain returns, and consensus views remain projections over the same branch/object graph. | Do not create mode-private backends or silent branch collapse. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Checkpoint and replay flow | Route checkpoint capture and replay through execution-control and replay workers over explicit branch/checkpoint refs. | Exact replay must mint new runs from frozen basis rather than mutating earlier truth. |
| Compare and merge review | Serve branch compare and merge-proposal review from replay-compare plus review-writeback seams. | Merge remains explicit proposal state with proof/delta context; never silent reconciliation. |

### 4.4 Storage, provenance, and migration posture

1. Persist branch, checkpoint, and replay lineage as append-only provenance linked to explicit branch and run refs.
2. Keep branch overlays and basis diffs reconstructable from pack lineage instead of UI-local graph state.
3. Do not introduce artifact revision storage or prompt-asset derivation in this release.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Branch/replay exploration | branch from checkpoint, replay exact basis, compare outcomes, inspect basis diffs | R3 semantic-branch and replay continuity promise. |
| Mode projections | notebook/debate/research/architect projections over the same branch graph | R3 mode-projection rule and non-mode-private backend lock. |
| Merge proposals | off-chain return, merge proposal review, consensus branch view, abandon/freeze posture | R3 explicit-merge and off-chain return obligations. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for branch identity, checkpoint-based replay, and explicit basis-diff visibility.<br>Edge coverage for transcript-clone refusal and merge-proposal lineage preservation.<br>Regression coverage for compare results, branch overlays, and mode switches staying on one shared object graph. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize artifact workspace inboxes, prompt-asset browsers, or protocol/applet builders inside the R3 cluster.
- Do not let mode switches create separate backends, object graphs, or hidden merge behavior.
- Do not treat transcript duplication as checkpoint capture or replay truth.

## 5. Acceptance notes

- This blueprint remains a bounded build plan for semantic branch/replay work and must preserve the R2 pack substrate unchanged.
- Human implementation review should confirm that every branch affordance resolves back to explicit checkpoint, run, proof, and delta lineage.
