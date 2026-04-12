# Phase 6 R5 prompt assets implementation blueprint
Version: 1.0
Status: Accepted
Task: P6.5 — Release implementation blueprints
Artifact ID: bp.phase6-r5-prompt-assets-blueprint.v1
Release ref: rel.r5-prompt-studio-contract.v1
Implementation scope: Accepted R5 prompt-assets blueprint mapping governed prompt artifacts, model-profile lineage, validation, and staleness seams onto the Phase 6 repo/package layout.

This artifact is accepted for downstream use.
It translates the accepted R5 Prompt Studio contract into bounded implementation guidance for governed prompt artifacts, model profiles, adaptations, staleness, and reviewable provider abstraction.
It does not create runtime code or widen accepted release semantics.

## 1. Purpose

- map governed prompt assets onto concrete app, package, service, worker, and test clusters without collapsing them into provider-local lore,
- name the model-profile, adaptation-lineage, compare, and review seams needed to keep prompt assets explicit, versioned, and reusable,
- preserve the accepted R5 non-goals so reusable execution, background autonomy, and commissioning remain later-stage work.

## 2. Scope boundaries

### In scope

- chat-native `r5-prompt-assets` and model-profile browser route clusters over prompt artifacts, prompt cards, model profiles, and adaptations,
- prompt-asset derivation, model-profile compatibility, adaptation compare, staleness marking, and governed save/apply seams,
- tests and fixtures for canonical prompt lineage, adaptation derivation, profile compatibility, and explicit stale-mark behavior.

### Out of scope

- Protocol/Applet/Workflow execution UX or bounded background-run governance,
- commissioning preflight and Task Studio handoff depth,
- provider-local prompt mutation or prompt cards as reusable execution identity.

## 3. Governing baseline

| Baseline artifact ref | Why it governs this blueprint |
| --- | --- |
| `rel.r5-prompt-studio-contract.v1` | Defines the release-specific promise, exit criteria, inherited seams, and explicit non-goals that this blueprint must implement. |
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
| `apps/chat-native/` | `apps/chat-native/r5-prompt-assets/`<br>`apps/chat-native/r5-model-profile-browser/` | Implements prompt-asset browsing, prompt cards, model-profile views, adaptation compare, and staleness affordances promised by R5. |
| `packages/` | `packages/projection-grammar/prompt-asset-projection/`<br>`packages/shared-object-schemas/prompt-assets/`<br>`packages/shared-object-api/prompt-assets/`<br>`packages/model-gateway-contracts/model-profile-compat/`<br>`packages/review-writeback-contracts/prompt-asset-review/`<br>`packages/event-provenance-contracts/prompt-lineage/`<br>`packages/monitor-inspect/prompt-browser/` | Provides prompt artifact, adaptation, model-profile, review, provenance, and inspect seams for governed prompt assets. |
| `services/` | `services/model-gateway/adaptation-execution/`<br>`services/review-writeback/prompt-asset-review/`<br>`services/event-provenance/prompt-lineage/` | Coordinates model-profile compatibility, adaptation derivation, governed review/save, and append-only prompt lineage. |
| `workers/` | `workers/replay-compare/adaptation-compare/`<br>`workers/apply-writeback/prompt-asset-apply/` | Executes adaptation compare and lane-separated prompt-asset apply flows over explicit artifact lineage. |
| `tests/` | `tests/contracts/r5-prompt-assets/`<br>`tests/fixtures/r5-prompt-assets/` | Covers canonical prompt lineage, model-profile compatibility, adaptation compare, and stale-mark propagation. |

### 4.2 Shared schemas, contracts, and object seams

| Area | Planned work | Guardrails |
| --- | --- | --- |
| Prompt artifact substrate | `Prompt Artifact`, `Model Profile`, `Adaptation`, `Adaptation Lineage`, and `Output Target` remain governed artifact-layer facts with stable lineage. | Do not let prompt cards or provider settings become the primary truth model. |
| Provider abstraction and staleness | Model-profile compatibility, adaptation compare, and stale-mark rules remain explicit model-gateway and provenance seams. | Do not hide provider-specific prompt behavior or compatibility drift in undocumented lore. |

### 4.3 APIs, events, and execution seams

| Seam | Planned implementation focus | Must preserve |
| --- | --- | --- |
| Prompt derivation flow | Route canonical prompt generation and adaptation derivation through model-gateway and review-writeback seams. | Prompt changes must remain bounded runs with explicit proof, delta, and artifact-lane proposals. |
| Compatibility and compare flow | Serve model-profile compatibility, adaptation compare, and staleness state from model-gateway, replay-compare, and provenance reads. | Adaptation compare must preserve explicit target identity and lineage rather than ad hoc side-by-side text. |

### 4.4 Storage, provenance, and migration posture

1. Persist prompt derivations, model-profile compatibility records, and stale-mark propagation as append-only lineage linked to prompt artifacts and runs.
2. Keep provider abstraction visible through typed model-profile refs instead of ambient provider settings.
3. Do not introduce protocol/applet execution state or background-run queue state in this release.

### 4.5 UI states and surface projections

| Surface cluster | States to implement | Derived from |
| --- | --- | --- |
| Prompt asset browser | prompt cards, canonical prompt details, version history, reusable-input status | R5 governed prompt-artifact promise. |
| Model-profile and adaptation views | model-profile browser, output-target selection, adaptation compare, stale adaptation indicators | R5 adaptation-lineage and staleness rules. |
| Governed save/review | prompt-asset review flow, lineage-preserving save/apply, validation notes | R5 explicit artifact-governance requirement for prompt assets. |

### 4.6 Tests, fixtures, and validators

| Validation layer | Coverage target | Why it matters |
| --- | --- | --- |
| Validation hooks | `vh.dependency.integrity`<br>`vh.consistency.cross-pack-review`<br>`vh.fixture.or-test-when-applicable`<br>`vh.manual.acceptance` | Use the default implementation-blueprint validation hooks from the accepted artifact-type catalog. |
| Fixture families | `golden_scenario`<br>`edge_case`<br>`regression` | Exercise nominal, edge, and drift coverage relevant to this release boundary. |
| Coverage focus | Contract tests for prompt-artifact identity, model-profile compatibility, and adaptation lineage.<br>Edge coverage for stale adaptation propagation and refusal of provider-local prompt mutation.<br>Regression coverage for adaptation compare, output-target identity, and governed save/apply behavior. | Keep validation aligned to accepted boundary, lineage, and non-goal rules. |

### 4.7 Explicit exclusions and deferred work

- Do not materialize protocol/applet/workflow builders, queue/inbox governance, or commissioning panels inside the R5 cluster.
- Do not allow prompt cards or provider settings to bypass artifact review and writeback flows.
- Do not hide model-specific behavior or compatibility drift outside typed model-profile and lineage objects.

## 5. Acceptance notes

- This blueprint remains a bounded build plan for governed prompt assets and must preserve the R4 artifact/governance substrate unchanged beneath it.
- Human implementation review should confirm that prompt assets stay lineage-bearing artifacts rather than provider-local prompt state.
