# Forbidden-Shortcuts Register
Version: 1.0
Status: Accepted
Task: P0.4 — Forbidden-shortcuts register

## 1. Purpose

This artifact turns the already accepted forbidden-shortcut baseline into one explicit, reviewable register.

It exists to:

- preserve the accepted shortcut prohibitions without reopening them,
- make each shortcut human-legible and reusable in downstream review,
- identify concrete current enforcement points already present in the repo,
- name future lint/review points without pretending they already exist,
- reduce drift across later control-plane, release, architecture, and execution artifacts.

This register formalizes accepted baseline constraints.
It does not silently create new accepted shortcut semantics.

## 2. Scope boundaries

### In scope

- the accepted forbidden-shortcut baseline already recorded in `docs/control-plane/core/master-plan.md`
- shortcut definitions and reasons
- affected scope/layer mapping
- current enforcement-point mapping against accepted P0.0–P0.3 artifacts
- named future lint/review points for downstream work

### Out of scope

- redefining the accepted-artifact-only rule
- redefining the packet-brief baseline
- redefining the accepted P0.3 Factory operating contract
- packet-budget, context-budget, local-doc-first, or subagent exploration policy from P0.5
- source-authority changes
- acceptance of materially new shortcut categories without explicit human approval

## 3. Design constraints carried forward

- The three-layer architecture remains fixed: engine, shared environment, app/domain layer.
- Chat is a projection over shared primitives, not the source of truth.
- Task Studio remains the north-star commissioned-work app.
- The chat-native release order remains fixed.
- No release or repo artifact may invent a private competing truth model.
- Repo layout is a storage convention, not the platform architecture.
- Product truth remains human-owned.
- Factory.ai remains the base execution tool.
- CrewAI is not part of the base plan.
- The accepted-artifact-only default remains in force.
- The accepted packet-brief baseline remains in force.
- The accepted P0.3 Factory operating contract remains additive and must not be contradicted.

## 4. Register interpretation rules

### 4.1 Baseline status

The shortcut prohibitions in Section 7 are already accepted as baseline product truth through `docs/control-plane/core/master-plan.md` Section 4.3.

This artifact does not reopen that baseline.
It only structures it.

### 4.2 Artifact acceptance boundary

The structure, wording, enforcement-point mapping, and any future-point naming in this artifact remain reviewable until the artifact is explicitly accepted by a human.

Before explicit human acceptance:

- the artifact status must remain `review_ready`,
- P0.4 must remain open in `docs/control-plane/core/master-plan.md`,
- no new shortcut meaning should be treated as accepted unless it was already fixed upstream.

After explicit human acceptance and passing validation:

- the artifact may move to `accepted`,
- P0.4 may be marked done in `docs/control-plane/core/master-plan.md`,
- the carry-forward log may record the result as accepted downstream truth.

### 4.3 Proposed additions rule

If a later session discovers a materially new shortcut risk not already fixed by accepted artifacts:

- record it in a clearly labeled proposed-addition section,
- keep it non-accepted until explicit human approval,
- do not silently fold it into the accepted baseline list.

## 5. Current enforcement-point catalog

These enforcement points exist now.
They are current because the governing artifacts or skills already exist in the repo.

### CEP-001 — Master-plan baseline lock

- Artifact: `docs/control-plane/core/master-plan.md`
- Current role:
  - fixes the accepted baseline decisions in Section 4.2,
  - fixes the forbidden-shortcut baseline in Section 4.3,
  - keeps forbidden-shortcut decisions human-owned in Section 6.1,
  - requires P0.4 to define enforcement or lint points in Section 8.

### CEP-002 — Repo truth and precedence contract

- Artifact: `docs/control-plane/core/repo-agent-operating-contract.md`
- Current role:
  - preserves accepted-artifact-only truth handling,
  - preserves truth/instruction precedence,
  - blocks packet briefs from overriding accepted repo truth,
  - prevents repo artifacts from inventing private competing truth models.

### CEP-003 — Control-plane subtree boundary

- Artifact: `docs/control-plane/AGENTS.md`
- Current role:
  - treats `docs/control-plane/` as a storage convention for control-plane artifacts,
  - requires reuse of accepted P0.1 metadata and dependency semantics,
  - blocks repo-placement drift into layer ownership or runtime architecture claims.

### CEP-004 — Factory bounded-execution and additive-contract rule

- Artifact: `.factory/factory-operating-contract.md`
- Current role:
  - keeps P0.3 additive to accepted P0.2 truth,
  - blocks silent scope widening,
  - blocks a second orchestration stack,
  - blocks P0.5-only policy leakage into P0.3,
  - preserves human acceptance authority over meaning and status changes.

### CEP-005 — Packet-execution verification discipline

- Artifact: `.factory/skills/control-plane-packet-execution/SKILL.md`
- Current role:
  - requires governing accepted artifacts to be read,
  - requires synchronized registry and graph updates for accepted-artifact changes,
  - blocks task-local metadata invention,
  - blocks scope widening when authority or acceptance is unclear.

### CEP-006 — Automated review baseline-preservation check

- Artifact: `.factory/skills/review-guidelines/SKILL.md`
- Current role:
  - checks baseline preservation,
  - checks control-plane integrity,
  - checks scope discipline,
  - flags second-stack drift, repo-shape drift, and premature acceptance behavior.

## 6. Future lint/review-point catalog

These points are named now for downstream use, but they do not yet exist as implemented automation.
They are future review/lint targets only.

### FEP-001 — Architecture synchronization shortcut sweep

- Planned use: P3.6 and later recurring sync work
- Purpose: re-check accepted artifacts for shortcut regressions across canon, semantics, architecture, release packs, and execution rules.

### FEP-002 — Release-contract shortcut preservation review

- Planned use: P4.3 through P4.9
- Purpose: ensure each release contract pack shows how it preserves relevant shortcut prohibitions instead of reintroducing them through view-specific wording or scope shortcuts.

### FEP-003 — Context realism and span-integrity review

- Planned use: P3.2 and P4.4
- Purpose: reject fake context-control claims when real addressable spans, evidence boundaries, or compiled-context behavior are missing.

### FEP-004 — Memory/canon visibility and governance review

- Planned use: P3.2, P5.1, and P5.2
- Purpose: reject hidden memory behavior and require explicit visibility, scope, and challenge/promotion handling.

### FEP-005 — Proposal/writeback governance review

- Planned use: P4.6, P4.9, and P5.1
- Purpose: reject silent durable mutation and require explicit proposal, delta, approval, and lane-by-lane writeback semantics.

### FEP-006 — Execution-stack drift review

- Planned use: P6.2, P6.4, and P7.3
- Purpose: flag default introduction of a second orchestration stack or repo-execution machinery that bypasses accepted Factory-first base tooling.

### FEP-007 — Artifact-over-transcript continuity review

- Planned use: P4.6, P5.5, and P5.7
- Purpose: ensure continuity and handoff center on runs, artifacts, proof, and writeback rather than transcript continuity alone.

## 7. Shortcut register

Each entry below uses the following minimum fields:

- stable shortcut key
- shortcut name
- definition
- why forbidden
- affected scope/layer
- current enforcement points
- future lint/review points
- related accepted artifacts

### 7.1 `fs.no-master-chat-truth` — No master chat truth

- Shortcut name: Master chat truth
- Definition:
  - Treating chat or transcript continuity as the primary truth object for consequential work instead of shared primitives such as runs, evidence/context packs, artifacts, proof, deltas, and writeback proposals.
- Why forbidden:
  - This would collapse the shared substrate back into transcript logic, break cross-app continuity, and directly contradict the accepted baseline that chat is only a projection.
- Affected scope/layer:
  - source-authority interpretation
  - chat-native release doctrine
  - shared environment continuity model
  - repo control-plane artifacts that describe chat behavior
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-002`
  - `FEP-007`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.repo-agent-operating-contract.v1`
  - `cp.factory-operating-contract.v1`

### 7.2 `fs.no-fake-fine-grained-context-control` — No fake fine-grained context control without real spans

- Shortcut name: Fake fine-grained context control
- Definition:
  - Claiming fine-grained context control, pack editing, or source-region selection when the system does not have real addressable spans, explicit inclusion/exclusion semantics, or compiled-context inspection to support those claims.
- Why forbidden:
  - It would create false trust, make Context Chat semantics fake, and undermine the accepted evidence-versus-context distinction.
- Affected scope/layer:
  - source ingestion and normalization
  - evidence/context pack semantics
  - Context Chat release scope
  - future compiler and retrieval topology
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-005`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-003`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.repo-agent-operating-contract.v1`

### 7.3 `fs.no-chat-session-attached-runs` — No chat-session-attached runs as the long-term model

- Shortcut name: Chat-session-attached runs
- Definition:
  - Modeling runs as long-term objects that live primarily inside chat sessions or message history rather than as first-class bounded work units that can later anchor artifacts, proofs, branches, checkpoints, and Task Studio handoff.
- Why forbidden:
  - It would trap the platform in transcript gravity, increase rewrite risk, and break the accepted requirement that Task Studio arrive as a projection change rather than a new ontology.
- Affected scope/layer:
  - run model
  - transcript chat implementation
  - artifact workspace bridge
  - commissioning bridge and Task Studio handoff
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-002`
  - `FEP-007`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.repo-agent-operating-contract.v1`
  - `cp.factory-operating-contract.v1`

### 7.4 `fs.no-hidden-memory-sludge` — No hidden memory sludge

- Shortcut name: Hidden memory sludge
- Definition:
  - Allowing memory or canon influence to accumulate as opaque background behavior without explicit visibility, scope, provenance, challenge/demotion handling, or run-time inclusion/exclusion review where serious work requires it.
- Why forbidden:
  - It would make context compilation uninspectable, weaken trust, and conflict with the accepted distinction between memory, canon, evidence, and context.
- Affected scope/layer:
  - memory system
  - canon/stable truth handling
  - compiled-context behavior
  - governance and review semantics
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-004`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.all-prims.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.factory-operating-contract.v1`

### 7.5 `fs.no-silent-proposal-application` — No silent proposal application

- Shortcut name: Silent proposal application
- Definition:
  - Applying model-generated durable mutations as automatic state changes instead of returning explicit proposals, deltas, approvals, and lane-specific writeback decisions.
- Why forbidden:
  - It collapses computation into commitment, hides consequential state changes, and violates the accepted artifact/memory/canon/workflow/export lane separation.
- Affected scope/layer:
  - artifact governance
  - proof/delta/writeback model
  - review and approval flow
  - later Task Studio writeback control
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-004`
  - `CEP-005`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-005`
  - `FEP-007`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.all-prims.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.repo-agent-operating-contract.v1`
  - `cp.factory-operating-contract.v1`

### 7.6 `fs.no-separate-backend-per-view` — No separate backend per view

- Shortcut name: Separate backend per view
- Definition:
  - Building transcript, context, branch, artifact, prompt, agent, or commissioning views on different private backend models or incompatible truth ontologies rather than shared primitives and shared execution/state semantics.
- Why forbidden:
  - It would make the shared environment fake, break reuse and handoff, and undermine the accepted claim that releases are projections over one substrate.
- Affected scope/layer:
  - runtime architecture
  - shared environment object model
  - release contract design
  - cross-app handoff
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-003`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-002`
  - `FEP-007`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.all-prims.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.control-plane-module-agents.v1`
  - `cp.factory-operating-contract.v1`

### 7.7 `fs.no-agent-builder-first` — No agent-builder-first approach before authority and verifier semantics exist

- Shortcut name: Agent-builder-first
- Definition:
  - Shipping reusable agent/applet builder flows before authority scopes, verifier packs, contradiction checks, proof expectations, and governance semantics are explicit enough to bound autonomy and trust.
- Why forbidden:
  - It would turn reusable execution into prompt theater, weaken governance, and violate the accepted release order that places governed agent/applet work after context, branch, artifact, and prompt hardening.
- Affected scope/layer:
  - reusable execution layer
  - protocol/applet/workflow semantics
  - governance and proof layer
  - background execution policy
- Current enforcement points:
  - `CEP-001`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-002`
  - `FEP-005`
  - `FEP-006`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.factory-operating-contract.v1`

### 7.8 `fs.no-transcript-first-rewrite-trap` — No transcript-first rewrite trap

- Shortcut name: Transcript-first rewrite trap
- Definition:
  - Taking implementation shortcuts that put transcript-specific state, semantics, or continuity above the substrate objects that later releases and Task Studio must reuse, thereby forcing costly rewrites when the product moves beyond transcript-dominant surfaces.
- Why forbidden:
  - It makes later release work brittle, increases blast radius, and directly contradicts the accepted rule that the chat-native phase hardens the substrate in public.
- Affected scope/layer:
  - architecture seams
  - run/context/artifact/provenance substrate
  - release sequencing
  - later Task Studio handoff
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-002`
  - `FEP-007`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.chat-native-release-plan.v1`
  - `sa.task-studio-north-star.v1`
  - `cp.repo-agent-operating-contract.v1`
  - `cp.factory-operating-contract.v1`

### 7.9 `fs.no-repo-shape-architecture-drift` — No letting repo shape dictate platform architecture

- Shortcut name: Repo-shape architecture drift
- Definition:
  - Inferring engine/shared-environment/app ownership, runtime topology, or product truth from file layout, package placement, or control-plane storage conventions rather than from accepted semantic and architecture artifacts.
- Why forbidden:
  - It would invert the intended dependency direction, making storage conventions define platform meaning and creating avoidable architecture drift.
- Affected scope/layer:
  - repo/package planning
  - control-plane artifact placement
  - later repo/package architecture work
  - surface/codebase substrate work
- Current enforcement points:
  - `CEP-001`
  - `CEP-002`
  - `CEP-003`
  - `CEP-004`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-006`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `sa.all-prims.v1`
  - `cp.control-plane-module-agents.v1`
  - `cp.repo-agent-operating-contract.v1`
  - `cp.factory-operating-contract.v1`

### 7.10 `fs.no-second-orchestration-stack-by-default` — No second orchestration stack by default

- Shortcut name: Second orchestration stack by default
- Definition:
  - Introducing an additional default orchestration/runtime layer alongside Factory.ai before an explicit accepted need justifies it, or designing later repo/program work around that extra stack as if it were already part of the base plan.
- Why forbidden:
  - It would add complexity, split execution truth, and directly contradict the accepted tooling baseline that Factory.ai is the base execution layer and CrewAI is only a later optional branch.
- Affected scope/layer:
  - repo execution policy
  - automation/runtime tooling
  - future package and execution-system work
- Current enforcement points:
  - `CEP-001`
  - `CEP-004`
  - `CEP-005`
  - `CEP-006`
- Future lint/review points:
  - `FEP-001`
  - `FEP-006`
- Related accepted artifacts:
  - `cp.master-plan.v1`
  - `cp.factory-operating-contract.v1`
  - `cp.factory-workspace-agents.v1`
  - `cp.factory-packet-execution-skill.v1`
  - `cp.factory-review-guidelines-skill.v1`

## 8. Proposed additions pending human approval

At the time of this P0.4 drafting pass, no materially new shortcut category is added beyond the already accepted baseline from `docs/control-plane/core/master-plan.md` Section 4.3.

Future sessions may append proposed additions here, but they must remain explicitly non-accepted until a human approves them.

## 9. Validation expectations for P0.4

P0.4 validation should use real checks that currently exist:

1. JSON parse for edited or created `.json` files.
2. Dependency-integrity verification that new graph references resolve to registry artifact IDs.
3. Verification that validation hooks, edge types, and stale rules come from accepted P0.1 catalogs.
4. Verification that this register preserves the accepted forbidden-shortcut baseline from `docs/control-plane/core/master-plan.md` Section 4.3 rather than reinterpreting it.
5. Verification that each shortcut entry includes a definition, reason, affected scope/layer, current enforcement points, future lint/review points, and related accepted artifacts.
6. Final scope review confirming no P0.5-only packet-budget or context-policy behavior was pulled into this artifact.

## 10. Why this preserves the baseline

This register does not:

- reopen accepted shortcut decisions,
- redefine the accepted-artifact-only rule,
- redefine the packet-brief baseline,
- redefine the accepted P0.3 Factory contract,
- claim future lint/review automation already exists,
- add a second orchestration stack,
- or let repo placement imply platform architecture ownership.

It makes the accepted forbidden-shortcut baseline explicit enough for downstream packs, reviews, and packets to reference without silently drifting.
