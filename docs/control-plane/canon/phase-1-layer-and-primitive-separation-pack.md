# Phase 1 layer and primitive separation pack
Version: 1.0
Status: Accepted
Task: P1.3 — Layer and primitive separation pack
Artifact ID: canon.phase1-layer-primitive-separation.v1
Canon scope: Owner-layer map for engine, shared environment, chat-domain, Task Studio, and later domain-pack primitives

## 1. Purpose

This artifact fixes the owner layer for the major primitive families used by the platform plan.

It exists to:

- give each major object family one owner layer,
- make clear which layers do **not** own each family,
- stop projection language from turning into ontology drift,
- give later semantic, architecture, release, and repo work one clear boundary map.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- owner-layer assignment for major primitive families,
- explicit non-owner statements,
- engine-to-environment projection pair rules,
- Task Studio and chat-domain boundary rules,
- later domain-pack boundary rules.

### Out of scope

- detailed field-level schema design,
- state-machine design,
- release topology details,
- technical runtime topology,
- repo/package layout,
- code-domain schema details beyond owner-layer placement.

## 3. Boundary rules

### 3.1 One-owner rule

Each major primitive family has exactly one owner layer.
Other layers may project, specialize, package, or visualize that family, but they do not become the owner by doing so.

### 3.2 Projection-does-not-transfer-ownership rule

If a chat view or Task Studio view exposes a shared primitive, the owner still remains the shared environment or engine layer that defines it.

### 3.3 Environment-over-app rule

If an object must preserve identity across more than one app, it belongs to the shared environment, not to one app projection.

### 3.4 App-over-view rule

If an object exists only to support one app’s workflow or one release view’s UX, it belongs to that app or view/domain pack, not to the shared environment.

### 3.5 Domain-pack extension rule

Later domain packs may add domain-specific primitives, but they may not redefine shared-environment primitives as if those shared objects belonged to the domain pack.

## 4. Owner-layer map

| Primitive family | Owner layer | Included primitives / examples | Clear non-owners |
| --- | --- | --- | --- |
| Engine substrate primitives | Engine | Execution Unit, Objective Spec, Source Object, Evidence Item, Evidence Set, Compiled Context Package, Memory classes, Accepted Knowledge object, engine Strategy Graph form, Tool Invocation Record, Validation Record, engine Proof Bundle form, engine State Delta form, Variant, Policy object, Event object | Shared environment, chat-domain packs, Task Studio, later domain packs |
| Shared operating primitives | Shared environment | Scope, Workspace, Project, App, Surface, Thread/Line, Branch, Actor, Role Binding, Assignment, Commission, Contract, Run Class, Run, Checkpoint, Handoff, Source Reference, Evidence Pack, Context Pack, Authority Scope, Memory Object, Canon Object, Artifact, Proof Bundle, State Delta, Writeback Proposal, Provenance Graph, Template, Protocol, Context Recipe, Strategy Preset, Verifier Pack, Workflow, Trigger, Applet, Pack/Extension, Integration Binding, Review, Approval Decision, Annotation | Chat-domain packs, Task Studio, later domain packs as owners |
| Chat-domain primitives | Chat-domain / release-view layer | Message Block, Conversation Surface, Source Chip, Resume Packet, Span, Span Set, Lens, Context Operation, Pack Diff, Pack Freeze, Starter Pack, Fork Policy, Mode Projection, Off-chain Job, Merge Proposal, Consensus Branch, Root Artifact, Focal Artifact, Proposal, Canon Strip, Review Anchor, Prompt Artifact, Prompt Card, Model Profile, Adaptation, Agent Profile, Chatlet Projection, Commission Card, Contract Draft, Run Preflight, Acceptance Stack | Engine, shared environment, Task Studio, later domain packs as owners of these view-specific primitives |
| Task Studio app primitives | Task Studio app/domain layer | Task Home, New Commission Sheet, Task Contract Panel, Evidence Pack Builder, Context Inspector arrangement, Strategy Board, Authority Panel, Live Run View, Result Canvas, Delta Inspector, Writeback Panel, Task Studio task-family framing, commissioning lifecycle projection, progressive disclosure model | Engine, shared environment, chat-domain packs, later domain packs as owners of these app-specific constructs |
| Later domain-pack primitives | Later domain packs | Repository, Repo Snapshot, Working Copy, Code Surface Map, Symbol Graph, Dependency Graph, Diagnostic Set, Edit Contract, Change Set, Verification Contract, Verification Result, Scaffold Blueprint, Apply/Merge Proposal, Runtime Target, and equivalent future domain nouns | Engine, shared environment, chat-domain packs, Task Studio as owners of these domain-specific primitives |

## 5. Engine vs shared-environment projection pairs

These pairs are allowed and expected.
They do **not** mean ownership is ambiguous.

| Engine form | Shared-environment form | Ownership rule |
| --- | --- | --- |
| Execution Unit | Run | Engine owns the universal execution substrate contract; shared environment owns the user-facing operating object |
| Source Object | Source Reference | Engine owns source ingestion/normalization object shape; shared environment owns the cross-app operating reference |
| Evidence Set | Evidence Pack | Engine owns the substrate evidence machinery; shared environment owns the user-facing governed pack |
| Compiled Context Package | Context Pack | Engine owns runtime compilation substrate; shared environment owns the inspectable operating projection |
| Accepted Knowledge object | Canon Object | Engine owns the substrate truth-management capability; shared environment owns the scoped accepted operating truth object |
| Variant | Branch | Engine owns the alternate-state substrate; shared environment owns the cross-app governed branch object |
| Decision / approval event | Approval Decision | Engine owns generic decision events; shared environment owns the user-facing approval primitive |
| Persistence proposal | Writeback Proposal | Engine owns computation-vs-commit substrate separation; shared environment owns the lane-specific operating proposal |

## 6. Non-owner clarifications

### 6.1 What the engine does **not** own

The engine does not own:

- Workspace, Project, App, Surface, Thread/Line,
- cross-app user-facing governance objects such as Review or Approval Decision,
- release-view primitives,
- Task Studio’s app-specific surfaces and workflow composition.

### 6.2 What the shared environment does **not** own

The shared environment does not own:

- transcript-only or release-view-only chat primitives,
- Task Studio’s app-specific surface composition,
- later repo/code-domain primitives,
- repo/package layout decisions.

### 6.3 What chat-domain packs do **not** own

Chat-domain packs do not own:

- Run, Artifact, Branch, Evidence Pack, Context Pack, Proof Bundle, State Delta, Writeback Proposal,
- Protocol, Workflow, Applet, or other shared reusable execution objects,
- product truth or accepted canon.

Chat views may project these objects, summarize them, or stage them for interaction.
They do not replace them.

### 6.4 What Task Studio does **not** own

Task Studio does not own the underlying shared primitives it uses.

Task Studio does **not** own:

- Commission, Contract, Run, Evidence Pack, Context Pack, Strategy Graph, Authority Scope,
- Proof Bundle, State Delta, Writeback Proposal, Branch, Review, Approval Decision, Artifact.

Task Studio owns the commissioned-work app projection over those primitives:

- the commissioned-work surface set,
- the commissioning lifecycle rhythm,
- task-family framing,
- result presentation and progressive disclosure choices.

### 6.5 What later domain packs do **not** own

Later domain packs do not own the shared-environment substrate.
They may introduce domain-specific nouns, but they must not back-edit ownership of shared primitives such as Run, Artifact, Branch, Proof Bundle, or Writeback Proposal.

## 7. Boundary decisions to carry forward

1. Runs are shared-environment operating objects, not chat primitives and not Task Studio-owned primitives.
2. Chat-domain primitives are view-specific helpers and must remain replaceable projections over shared objects.
3. Task Studio is an app/domain projection that specializes commissioned work; it does not redefine the shared substrate.
4. Repo/code-domain nouns belong to later domain packs and must not be promoted into the shared environment merely because code work is important later.
5. Repo placement must never be used as evidence for layer ownership.

## 8. Downstream implications

### 8.1 For P1.4 — Surface and release topology canon

- Surface sequencing should be built on top of this owner map.
- Chat-native releases may foreground different objects, but they may not take ownership of shared ones.

### 8.2 For P1.5 — Rewrite-containment / stable seam map

- Engine and shared-environment owners define the high-blast-radius seams.
- Chat and Task Studio surface work should be placed above those seams, not inside them.

### 8.3 For P2 semantic work

- Field-level schemas and transitions should inherit this owner map rather than rediscover it.
- If a later schema implies a different owner layer, treat that as a contradiction to review, not as silent drift.

## 9. Review notes

Human review should confirm that this pack:

- gives each major primitive family one owner layer,
- clearly names non-owners,
- keeps Task Studio as an app/domain projection rather than a new substrate,
- keeps chat-domain primitives view-specific,
- keeps later repo/code-domain primitives out of the shared-environment core.
