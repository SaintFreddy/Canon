# Phase 6 R4 artifact workspace implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r4-artifact-workspace-blueprint.v1
Release ref: rel.r4-artifact-workspace-contract.v1
Implementation scope: Accepted R4 artifact-workspace blueprint mapping focal-artifact, proposal/review, lineage, and writeback seams onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R4 Artifact Workspace contract into bounded implementation guidance for focal artifacts, proposal inbox review, historical truth per run, and lane-separated writeback.
It does not create runtime code or widen accepted release semantics.

> **Platform Gate reopen notice (2026-04-23).** This blueprint transitively depends on `arch.phase3-platform-gate-spec.v1`. On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the Platform Gate P3.6 acceptance marker against the 2026-04-18 agentic-engine audit-cited contradiction event per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A). Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`. This blueprint itself remains `accepted` for downstream use — the implementation guidance below is unchanged and the release doctrine is not reopened. Consumers reading this blueprint should, however, be aware that PG-01.1 (Clock + stableStringify + localeCompare + frozenAt), PG-07.1 (credentialScope enforcement), and PG-10.1 (spawnToolSandboxWorker + IPC export) are remediation sub-gates still closing. Engine sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (see `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0089..CF-0096); the sub-gates formally close after PG-R3 (maturity-matrix + milestone-plan sync) lands. See `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 for the full gate reopen markup and successor-checkpoint reference.

## 1. Purpose

- map artifact-centered continuity onto concrete app, package, service, worker, and test clusters without erasing run/proof/delta truth,
- name the proposal, review, approval, and writeback seams needed to keep durable mutation explicit and lane-separated,
- preserve the accepted R4 non-goals so prompt assets, reusable execution, and commissioning remain later-stage work.

## 2. Scope boundaries

### In scope

- chat-native `r4-artifact-workspace` and proposal-inbox route clusters over explicit artifact, proposal, review, and approval objects,
- artifact-targeted run dispatch, proposal/review storage, lane-separated apply flows, and artifact-lineage inspection seams,
- tests and fixtures for focal-artifact targeting, partial acceptance, historical truth, and alternative/objection lineage.

### Out of scope

- prompt-asset specialization or model-profile behavior,
- reusable execution packaging, background autonomy, or commissioning preflight,
- silent artifact mutation, generic save behavior, or treating artifacts as replacements for runs.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r4-artifact-workspace-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
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
| `apps/chat-native/` | `apps/chat-native/r4-artifact-workspace/`<br>`apps/chat-native/r4-proposal-inbox/` | Implements focal-artifact browsing, proposal inbox review, review anchors, and artifact resume flows promised by R4. |
| `packages/` | `packages/projection-grammar/artifact-workspace-projection/`<br>`packages/shared-object-schemas/artifact-governance/`<br>`packages/shared-object-api/artifact-lineage/`<br>`packages/environment-control-contracts/artifact-run-targeting/`<br>`packages/review-writeback-contracts/artifact-review/`<br>`packages/event-provenance-contracts/artifact-lineage/`<br>`packages/monitor-inspect/artifact-workspace/` | Provides artifact identity, proposal/review/writeback, provenance, and inspect seams for artifact-centered continuity. |
| `services/` | `services/environment-shell-api/artifact-run-targeting/`<br>`services/review-writeback/proposal-inbox/`<br>`services/review-writeback/review-anchor/`<br>`services/event-provenance/artifact-history/` | Coordinates artifact-targeted runs, proposal inbox materialization, review anchors, and append-only artifact lineage. |
| `workers/` | `workers/apply-writeback/artifact-lane-apply/`<br>`workers/replay-compare/artifact-revision-compare/` | Executes lane-separated apply and revision compare flows without mutating artifact truth silently. |
| `tests/` | `tests/contracts/r4-artifact-workspace/`<br>`tests/fixtures/r4-artifact-workspace/` | Covers focal-artifact targeting, proposal/review identity, partial acceptance, and artifact historical truth. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Artifact governance substrate | `Artifact`, `Writeback Proposal`, `Review`, `Approval Decision`, `Alternative Artifact`, and `Objection Artifact` remain first-class shared objects linked back to producing runs. | Do not let comments, drafts, or one-click save behaviors replace artifact lineage and governance. |
| Artifact-centered projection layer | `Root Artifact`, `Focal Artifact`, `Proposal`, and `Review Anchor` remain projection-layer affordances over the same underlying governance objects. | Do not collapse artifact-centered continuity into transcript history or UI-local state. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Artifact-targeted run flow | Route artifact-targeted transform/audit/synthesize launches through environment-control and review-writeback seams. | Every artifact-facing run must emit explicit proof, delta, and writeback proposal state. |
| Proposal and apply flow | Serve proposal inbox, review anchors, and lane-separated apply paths from review-writeback plus provenance reads. | Artifact acceptance may be partial by lane; never collapse canon, memory, workflow, and artifact writes into one save action. |

### 4.4 Storage, provenance, and migration posture

1. Persist artifact revisions, alternatives, objections, reviews, approvals, and apply records as append-only lineage linked to source runs.
2. Keep historical truth per artifact-facing run replayable even after later revisions or objections appear.
3. Do not treat artifact history as a replacement for proof, delta, or review lineage.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Artifact workspace | root artifact browser, focal artifact canvas, artifact resume, linked source run navigation | R4 artifact-centered continuity promise. |
| Proposal and review | proposal inbox, review anchors, approval decisions, partial-accept lane controls | R4 proposal-first and historical-truth rule. |
| Artifact alternatives | alternative artifact compare, objection artifact surfacing, revision history | R4 explicit alternative/objection artifact contract. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for artifact identity, focal-artifact run targeting, and proposal/review object continuity.<br>Edge coverage for lane-specific partial acceptance and refusal of silent artifact mutation.<br>Regression coverage for historical truth, alternative artifacts, and objection lineage. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize prompt-asset adaptation, protocol/applet packaging, or commissioning preflight modules inside the R4 cluster.
- Do not allow artifact save flows that bypass proof, delta, review, or lane-local decisions.
- Do not use artifact history or comments as substitutes for explicit review and approval records.

## 5. Acceptance notes

- This blueprint remains a bounded build plan for artifact-centered continuity and must preserve the R3 branch/replay substrate unchanged beneath it.
- Human implementation review should confirm that every durable artifact change remains proposal-first and fully lineage-bearing.
