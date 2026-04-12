# Platform Build Master Plan Record
Version: 1.0  
Last updated: 2026-04-11  
Status: Active planning artifact  
Primary execution tool: Factory.ai  
Secondary orchestration layer: Not part of the base plan  
Optional later branch: CrewAI only if a separate always-on, event-driven automation layer becomes necessary

---

## 1. Purpose of this file

This file is the master planning record for the platform program.

It exists to do five jobs at once:

1. Preserve the accepted product and architecture baseline.
2. Track what is done and what is not done.
3. Give fresh sessions enough context to expand any phase or task into a full execution prompt.
4. Preserve carry-forward information in one append-only place.
5. Keep downstream work from silently drifting away from accepted truth.

This file is meant to be attachable to fresh sessions. A fresh session should be able to read this file and then:
- explain any phase or task,
- expand any phase or task into a full prompt,
- execute bounded work for a selected task,
- update status markers,
- append new carry-forward information without rewriting history.

This file is not just a summary. It is the working control document.

---

## 2. How to use this file in fresh sessions

### 2.1 Mandatory reading rule

Any fresh session that receives this file must read the entire file before doing any of the following:
- suggesting plan changes,
- expanding a phase,
- expanding a task into a prompt,
- executing a task,
- marking something done,
- appending carry-forward information.

### 2.2 Fixed-context rule

Any fresh session using this file must treat the following sections as mandatory context:
- Section 4: Source authority and accepted baseline decisions
- Section 5: Current completion snapshot
- Section 6: Tooling and automation policy
- Section 8: Phase-by-phase execution plan
- Section 9: Append-only carry-forward log

These sections are not optional background. They are binding context for prompt generation and execution.

### 2.3 Prompt-generation rule

If a fresh session is asked to turn a phase or task into a prompt, the generated prompt must include all of the following:

- the selected phase or task ID and title,
- the purpose of the selected work,
- all relevant source authority and accepted baseline decisions,
- the current completion state,
- the dependencies of the selected work,
- the assigned execution mode for the selected work,
- the required deliverables,
- the acceptance criteria,
- the explicit non-goals or forbidden shortcuts that matter,
- the full append-only carry-forward log, either inline or as an appendix,
- the required status updates to apply after completion,
- the carry-forward topics that must be logged if new information is discovered.

If the carry-forward log becomes large, include it as an appendix. Do not silently omit entries.

### 2.4 Execution rule

If a fresh session is asked to execute a selected task:
- it must stay inside the selected task’s scope unless explicitly told otherwise,
- it must honor the automation mode for that task,
- it must not reopen fixed baseline decisions unless explicitly told to,
- it must propose status changes only after deliverables and validation exist,
- it must append new carry-forward information instead of rewriting earlier entries.

### 2.5 Minimal copy-paste requests for fresh sessions

Use one of these patterns.

**Expand a task into a prompt**
> Read the attached master plan file fully. Expand task `<TASK_ID>` into a full execution prompt. Follow the file’s prompt-generation rules exactly.

**Expand a phase into a prompt**
> Read the attached master plan file fully. Expand phase `<PHASE_ID>` into a full execution prompt. Follow the file’s prompt-generation rules exactly.

**Execute a task**
> Read the attached master plan file fully. Execute task `<TASK_ID>` within scope. Use the automation mode assigned in the file. Return deliverables, validation results, status updates, and an append-only carry-forward log entry draft.

---

## 3. Status legend and update rules

### 3.1 Status legend

- `[x]` Done and accepted
- `[ ]` Not done
- `[~]` In progress
- `[!]` Blocked
- `[>]` Stale and needs regeneration because an upstream accepted artifact changed

### 3.2 Update rules

Only mark a task `[x]` when:
- its stated deliverables exist,
- its acceptance criteria have been checked,
- the output is accepted for downstream use.

If a task is partially worked but not accepted, use `[~]`.

If an upstream artifact changes and a downstream artifact is no longer trustworthy, mark the downstream item `[>]`.

If a task cannot proceed because a dependency is missing or unresolved, use `[!]`.

### 3.3 Append-only rule for carry-forward information

The carry-forward log in Section 9 is append-only.

Do not delete old entries.  
Do not rewrite old entries.  
Do not silently “clean up” old entries.

If an earlier entry needs correction, add a new correction entry that references the earlier entry.

---

## 4. Source authority and accepted baseline decisions

### 4.1 Source authority

The current source authority is:

1. **All Prims / Agentic Stack — Engine + Shared Environment Primitive Set**  
   Role: defines the engine layer, the shared environment layer, the layer boundary, the canonical primitive set, reuse model, governance model, and projection grammar.

2. **Chat-Native Release Plan**  
   Role: defines the fixed chat-native release doctrine, the mandatory Platform Gate, the public release order from R1 through R7, what each release exposes, and the forbidden shortcuts during the chat-native phase.

3. **Task Studio — North Star Commissioned-Work App**  
   Role: defines the north-star app model, run-native commissioned work, the commissioning lifecycle, the primary Task Studio surfaces, task families, proof expectations, and the handoff target that the chat-native phase must build toward.

### 4.2 Accepted baseline decisions

The following baseline decisions are accepted and should not be reopened unless explicitly requested.

- [x] The architecture has three layers: engine, shared environment, and app/domain layer.
- [x] The engine is not the product shell.
- [x] The shared environment is not one app.
- [x] The first wedge is the chat-native phase.
- [x] Task Studio is the north-star commissioned-work app.
- [x] The chat-native phase is a proving ground for the substrate, not throwaway UI logic.
- [x] The release order is fixed: Platform Gate -> R1 Transcript Chat -> R2 Context Chat -> R3 Branch / Visual Thinker -> R4 Artifact Workspace -> R5 Prompt Studio -> R6 Governed Agent / Applet Chat -> R7 Commissioning Bridge -> Task Studio.
- [x] No release is allowed to invent a private competing truth model.
- [x] Chat is a projection over shared primitives, not the source of truth.
- [x] Task Studio must arrive as a projection change over existing primitives, not as a rewrite to a new ontology.
- [x] Artifact Workspace is the bridge release out of transcript gravity.
- [x] Prompt Studio and Governed Agent / Applet Chat are not optional side quests.
- [x] Commissioning Bridge is the terminal chat release.
- [x] Product truth remains human-owned.
- [x] Factory.ai is the primary execution and automation tool for repo/spec/code work in the base plan.
- [x] CrewAI is removed from the base plan.
- [x] CrewAI is only a later optional branch if a separate always-on, event-driven automation layer becomes necessary outside the normal repo/CI execution loop.

### 4.3 Forbidden shortcut baseline

These are accepted as forbidden shortcuts.

- [x] No master chat truth.
- [x] No fake fine-grained context control without real spans.
- [x] No chat-session-attached runs as the long-term model.
- [x] No hidden memory sludge.
- [x] No silent proposal application.
- [x] No separate backend per view.
- [x] No agent-builder-first approach before authority and verifier semantics exist.
- [x] No transcript-first rewrite trap.
- [x] No letting repo shape dictate platform architecture.
- [x] No second orchestration stack by default.

---

## 5. Current completion snapshot

This section answers, in plain terms, what is already done and what is not.

### 5.1 Already done

- [x] The current source authority has been identified and recorded in this file.
- [x] The accepted baseline product decisions have been recorded in this file.
- [x] The base tooling policy has been decided: Factory.ai is in the core plan; CrewAI is not.
- [x] This master plan file exists and is ready to be attached to fresh sessions.
- [x] The status system and append-only carry-forward mechanism are defined in this file.
- [x] The repo-level artifact registry and dependency graph have been implemented.
- [x] The lightweight repo/agent operating contract has been implemented.
- [x] The Factory operating contract has been implemented in the repo.
- [x] The forbidden-shortcuts register has been implemented and accepted.
- [x] The context-budget and packet policy has been implemented and accepted.
- [x] The Phase 1 source decomposition / contradiction register / glossary pack has been produced and accepted.
- [x] The Phase 1 canon freeze / resolved product interpretation note has been produced and accepted.
- [x] The Phase 1 layer and primitive separation pack has been produced and accepted.
- [x] The Phase 1 surface and release topology canon has been produced and accepted.
- [x] The Phase 1 rewrite-containment / stable seam map has been produced and accepted.
- [x] The Phase 1 golden scenario corpus and edge-case suite has been produced and accepted.
- [x] The Phase 2 core object and state-machine spec pack has been produced and accepted.
- [x] The Phase 2 run-class taxonomy and protocol-kernel pack has been produced and accepted.
- [x] The Phase 2 governance, authority, and writeback invariants have been produced and accepted.
- [x] The Phase 2 proof and validation invariants have been produced and accepted.
- [x] The Phase 2 chat-native semantic packs by release have been produced and accepted.
- [x] The Phase 2 projection grammar contract pack has been produced and accepted.
- [x] The Phase 3 high-level technical architecture baseline has been produced and accepted.
- [x] The Phase 3 context compiler / retrieval / memory / canon topology has been produced and accepted.
- [x] The Phase 3 data / storage / indexing / provenance spec has been produced and accepted.
- [x] The Phase 3 API / IPC / event contract spec has been produced and accepted.
- [x] The Phase 3 Platform Gate spec and exit audit have been produced and accepted.
- [x] The Phase 3 architecture synchronization pass has been produced and accepted.
- [x] The Phase 4 release-to-SDK maturity matrix has been produced and accepted.
- [x] The Phase 4 release / milestone architecture plan has been produced and accepted.
- [x] The Phase 4 R1 Transcript Chat contract pack has been produced and accepted.
- [x] The Phase 4 R2 Context Chat contract pack has been produced and accepted.
- [x] The Phase 4 R3 Branch / Visual Thinker contract pack has been produced and accepted.
- [x] The Phase 4 R4 Artifact Workspace contract pack has been produced and accepted.
- [x] The Phase 4 R5 Prompt Studio contract pack has been produced and accepted.
- [x] The Phase 4 R6 Governed Agent / Applet Chat contract pack has been produced and accepted.
- [x] The Phase 4 R7 Commissioning Bridge contract pack has been produced and accepted.
- [x] The Phase 5 full governance, authority, and writeback spec has been produced and accepted.
- [x] The Phase 5 full proof, validation, and evaluation spec has been produced and accepted.
- [x] The Phase 5 full run-class protocol packs have been produced and accepted.
- [x] The Phase 5 Workflow / Trigger / Applet / Pack / Integration Binding specs have been produced and accepted.
- [x] The Phase 5 Task Studio surface and lifecycle contract pack has been produced and accepted.
- [x] The Phase 5 Task Studio V1 scope pack has been produced and accepted.
- [x] The Phase 5 Commissioning Bridge -> Task Studio handoff contract has been produced and accepted.
- [x] The Phase 6 surface contract packs have been produced and accepted.
- [x] The Phase 7 delta-pack operating rule and coverage index have been produced and accepted.

### 5.2 High-level milestone snapshot

- [x] The release contract packs for Platform Gate through R7 have been produced and accepted.
- [x] The full reusable semantics and Task Studio readiness packs have been produced and accepted.
- [x] The repo/package architecture, documentation plane, and agent execution system have been implemented.
- [x] The pilot packet set, benchmark harness, and internal Factory skills/adapters have been implemented and benchmarked.
- [x] The release implementation blueprints have been produced and accepted.
- [x] The broader bounded execution packets have been generated and accepted.
- [ ] The continuous stale-detection, carry-forward, and sync loop is operational.

### 5.3 Phase status summary

- [x] Phase 0 — done in the repo
- [x] Phase 1 — done in the repo
- [x] Phase 2 — done in the repo
- [x] Phase 3 — done in the repo
- [x] Phase 4 — done in the repo
- [x] Phase 5 — done in the repo
- [x] Phase 6 — done in the repo
- [ ] Phase 7 — not done

---

## 6. Tooling and automation policy

### 6.1 Human-only work

These areas remain human-owned, with agent assistance allowed only for drafting, extraction, formatting, or comparison support:

- product canon decisions,
- layer ownership decisions,
- primitive ownership decisions,
- release doctrine interpretation,
- forbidden-shortcut decisions,
- proof/governance/authority meaning,
- acceptance of major architecture artifacts.

### 6.2 Human + Factory work

These areas are collaborative:

- contradiction extraction,
- glossary drafting,
- schema drafting,
- state-machine skeletons,
- consistency checks,
- architecture scaffolding,
- release gate templates,
- protocol/verifier/context recipe templates,
- validation harness scaffolding,
- blueprint drafting.

In these areas, humans define meaning and acceptance; Factory helps formalize and execute.

### 6.3 Factory-first work

These areas should default to Factory once upstream truth is accepted:

- package and module scaffolding,
- contract linting,
- replay/regression harnesses,
- test generation,
- bounded implementation packets,
- refactors and migrations,
- doc/code consistency checks,
- CI/CD headless execution,
- stale-dependency checks,
- carry-forward delta generation,
- release gate re-checks.

### 6.4 CrewAI rule

CrewAI is not part of the base plan.

Only reintroduce it if all of the following become true:
- you need a distinct automation runtime outside normal repo/CI execution,
- you need always-on or event-driven cross-system flows,
- Factory-based repo execution is not sufficient for that need,
- adding a second orchestration layer is worth the added complexity.

Until then, do not design around CrewAI.

---

## 7. Universal prompt assembly template

Use this template whenever a fresh session is asked to expand a phase or task into a full prompt.

```text
You are working from an attached master plan file.

Read the entire file first.

Selected item:
- ID: <PHASE_OR_TASK_ID>
- Title: <TITLE>

Your job:
Expand the selected item into a full execution prompt without reopening fixed baseline decisions.

Mandatory context to carry forward from the file:
1. Source authority and accepted baseline decisions
2. Current completion snapshot
3. Tooling and automation policy
4. Dependencies of the selected item
5. Deliverables of the selected item
6. Acceptance criteria of the selected item
7. Relevant forbidden shortcuts
8. The full append-only carry-forward log

Constraints:
- Stay within the scope of the selected item unless explicitly told otherwise.
- Honor the assigned execution mode.
- Do not silently omit carry-forward information.
- Do not change the meaning of accepted baseline decisions.
- If an upstream dependency is missing, say so and do not invent it.

Return:
1. Restated objective
2. Scope and non-scope
3. Required context carried forward
4. Dependencies and prerequisites
5. Step-by-step execution instructions
6. Deliverables to produce
7. Validation and acceptance checklist
8. Status updates to apply after completion
9. Draft append-only carry-forward log entry to add if the work completes
10. Any stale downstream items that would need to be marked if the work changes accepted truth
```

---

## 8. Phase-by-phase execution plan

## Phase 0 — Anti-drift and operating scaffold `[x]`

### Goal

Create the control plane that governs the rest of the work so later artifacts do not drift or poison downstream work.

### Exit condition

This phase is done when the repo has a real artifact registry, dependency model, packet policy, Factory operating contract, and forbidden-shortcut register that downstream tasks can rely on.

#### [x] P0.0 — Master execution plan record
- **Mode:** Human-only
- **Depends on:** current source authority
- **Deliverable:** this file
- **Acceptance:** this file exists, is self-contained, has status markers, has prompt-generation rules, and has an append-only carry-forward log
- **Carry-forward topics if updated later:** file version changes, structural rule changes

#### [x] P0.1 — Artifact registry, dependency graph, and promotion model
- **Mode:** Human + Factory
- **Depends on:** P0.0
- **Deliverable:** artifact registry spec, dependency graph format, promotion statuses, stale-marking rules
- **Acceptance:** every major artifact type has an ID pattern, owner, status field, dependency field, validation hook field, and stale propagation rule
- **Carry-forward topics:** artifact types added, status model refinements, stale propagation rules, validation hook standards

#### [x] P0.2 — Lightweight repo / agent operating contract
- **Mode:** Human + Factory
- **Depends on:** P0.1
- **Deliverable:** root AGENTS.md policy, module-local instruction convention, packet brief schema, accepted-artifact-only rule
- **Acceptance:** the repo has a minimal but explicit operating contract that agents and humans both follow
- **Carry-forward topics:** packet schema changes, repo-wide rules, module-local override rules

#### [x] P0.3 — Factory operating contract
- **Mode:** Human + Factory
- **Depends on:** P0.2
- **Deliverable:** Factory-specific AGENTS.md guidance, skills layout, headless execution conventions, review/approval rules for automated runs
- **Acceptance:** Factory can execute bounded packets consistently without inventing architecture or skipping review gates
- **Carry-forward topics:** skills created, droid/headless execution patterns, review/approval rules, failure-handling rules

#### [x] P0.4 — Forbidden-shortcuts register
- **Mode:** Human-only
- **Depends on:** P0.0
- **Deliverable:** explicit register of prohibited implementation shortcuts and their enforcement points
- **Acceptance:** each forbidden shortcut has a definition, a reason, and an enforcement or lint point
- **Carry-forward topics:** new shortcut risks discovered, enforcement points added, lint rules added

#### [x] P0.5 — Context-budget and packet policy
- **Mode:** Human-only
- **Depends on:** P0.2
- **Deliverable:** packet size targets, packet composition rules, local-doc-first read policy, subagent exploration rule
- **Acceptance:** packet creation has explicit bounds and escalation rules
- **Carry-forward topics:** packet size changes, escalation thresholds, context-compilation rules for packets

---

## Phase 1 — Product canon, layer separation, and topology `[x]`

### Goal

Turn the source docs into one coherent product truth with explicit layer boundaries, surface topology, and rewrite containment.

### Exit condition

This phase is done when there is one accepted canon for what belongs in engine, shared environment, chat-domain packs, and Task Studio, plus a stable seam map and scenario corpus.

#### [x] P1.1 — Source decomposition / contradiction register / glossary
- **Mode:** Human + Factory
- **Depends on:** P0.1
- **Deliverable:** claim inventory, contradiction register, glossary, unresolved-term list
- **Acceptance:** major terms are normalized, contradictions are explicit, and unresolved questions are named rather than buried
- **Carry-forward topics:** resolved contradictions, glossary lock-ins, unresolved terms that affect downstream specs

#### [x] P1.2 — Canon freeze / resolved product interpretation
- **Mode:** Human-only
- **Depends on:** P1.1
- **Deliverable:** accepted product interpretation note covering first wedge, north star, release order, and non-negotiable constraints
- **Acceptance:** no open ambiguity remains about wedge, north star, release order, or projection-vs-ontology rules
- **Carry-forward topics:** canon clarifications, explicit non-goals, confirmed interpretations that downstream work must not reopen

#### [x] P1.3 — Layer and primitive separation pack
- **Mode:** Human-only
- **Depends on:** P1.2
- **Deliverable:** explicit ownership map for engine primitives, environment primitives, chat-domain primitives, Task Studio primitives, later domain-pack primitives
- **Acceptance:** each major object family has one owner layer and clear non-owners
- **Carry-forward topics:** ownership clarifications, moved boundaries, downstream implications of any boundary changes

#### [x] P1.4 — Surface and release topology canon
- **Mode:** Human-only
- **Depends on:** P1.2
- **Deliverable:** topology artifact covering Platform Gate, R1-R7, Task Studio handoff, surfaces, modes, and cross-app handoff rules
- **Acceptance:** the platform has one accepted topology story and one accepted release-path story
- **Carry-forward topics:** topology corrections, surface vocabulary, handoff rules, mode/projection clarifications

#### [x] P1.5 — Rewrite-containment / stable seam map
- **Mode:** Human-only
- **Depends on:** P1.3 and P1.4
- **Deliverable:** stable seam map showing what must be stable now, what can change later, and what would be catastrophic to rewrite
- **Acceptance:** all high-blast-radius semantics are explicitly identified and placed below chat-specific UI logic
- **Carry-forward topics:** high-blast-radius seams, low-blast-radius seams, rewrite risks, stable interface rules

#### [x] P1.6 — Golden scenario corpus + edge-case suite
- **Mode:** Human + Factory
- **Depends on:** P1.2 and P1.4
- **Deliverable:** scenario corpus and edge-case suite spanning chat flows, artifact flows, branching, prompt assets, applets, commissioning, and Task Studio flows
- **Acceptance:** the corpus covers the major semantic pathways and known edge cases
- **Carry-forward topics:** newly discovered scenarios, edge cases that break assumptions, scenario-based validation rules

---

## Phase 2 — Shared semantic contracts before architecture `[x]`

### Goal

Lock the machine-grade nouns, transitions, governance rules, and proof rules before engineering architecture expands.

### Exit condition

This phase is done when the core object model, run classes, invariants, release-specific semantic packs, and projection grammar are accepted.

#### [x] P2.1 — Core object and state-machine spec pack
- **Mode:** Human + Factory
- **Depends on:** P1.3 and P1.5
- **Deliverable:** schemas and state transitions for Run, Artifact, Branch, Proof Bundle, State Delta, Writeback Proposal, Memory, Canon, Commission, Contract, Protocol, Applet, Review, Approval Decision, and related core objects
- **Acceptance:** major first-class objects have fields, transitions, and identity rules that downstream work can code against
- **Carry-forward topics:** field additions, transition rules, identity rules, lifecycle clarifications

#### [x] P2.2 — Run-class taxonomy + protocol kernel
- **Mode:** Human + Factory
- **Depends on:** P2.1
- **Deliverable:** base run classes, Task Studio task-family mappings, intake/result/proof schema skeletons, authority defaults, verifier slots, writeback defaults
- **Acceptance:** run classes are typed and no longer treated as vague generic tasks
- **Carry-forward topics:** run-class additions, schema changes, task-family mappings, protocol kernel rules

#### [x] P2.3 — Governance / authority / writeback invariants
- **Mode:** Human-only
- **Depends on:** P2.1
- **Deliverable:** invariant layer for scope widening, lane separation, approval points, policy boundaries, and authority semantics
- **Acceptance:** governance rules exist as explicit invariants, not as UI hopes
- **Carry-forward topics:** new invariants, clarified authority classes, writeback lane rules, policy edge cases

#### [x] P2.4 — Proof / validation invariants
- **Mode:** Human-only
- **Depends on:** P2.2
- **Deliverable:** invariant layer for proof expectations, uncertainty labeling, omission handling, contradiction handling, replay comparison expectations, and failure taxonomy
- **Acceptance:** proof is task-shaped and not one generic explanation blob
- **Carry-forward topics:** proof rules by task family, failure classes, validation expectations, uncertainty policies

#### [x] P2.5 — Chat-native semantic packs by release
- **Mode:** Human + Factory
- **Depends on:** P2.1 through P2.4
- **Deliverable:** semantic packs for Transcript Chat, Context Chat, Branch / Visual Thinker, Artifact Workspace, Prompt Studio, Governed Agent / Applet Chat, and Commissioning Bridge
- **Acceptance:** each release has an explicit semantic pack that sits on shared primitives instead of replacing them
- **Carry-forward topics:** release-specific object additions, semantic constraints, projection-specific vocabulary

#### [x] P2.6 — Projection grammar contract pack
- **Mode:** Human + Factory
- **Depends on:** P1.4 and P2.1
- **Deliverable:** contract pack for Composer, Canvas, Inspector, Browser/Library, Timeline, Ledger, Compare View, Queue/Inbox, Board, Diff/Merge View, Live Monitor, Console
- **Acceptance:** all apps can reuse one interaction grammar instead of inventing incompatible private metaphors
- **Carry-forward topics:** projection grammar rules, added projections, deprecations, reuse constraints

---

## Phase 3 — Technical baseline and Platform Gate `[x]`

### Goal

Turn accepted semantics into a real technical architecture and define the internal Platform Gate that must exist before public release work starts.

### Exit condition

This phase is done when the technical baseline, compiler topology, data/storage/provenance spec, API contracts, Platform Gate, and architecture sync pass are accepted.

#### [x] P3.1 — High-level technical architecture baseline
- **Mode:** Human + Factory
- **Depends on:** P2.1 through P2.6
- **Deliverable:** runtime topology, process model, local/cloud split, engine/environment/app boundaries, identity/tenancy touchpoints
- **Acceptance:** the platform has one accepted technical architecture baseline
- **Carry-forward topics:** runtime boundary changes, process model clarifications, identity/policy implications

#### [x] P3.2 — Context compiler / retrieval / memory / canon topology
- **Mode:** Human + Factory
- **Depends on:** P3.1
- **Deliverable:** topology for spans, ingestion, evidence-vs-context distinction, staged retrieval, memory/canon injection, freeze/replay/diff, recovery/compaction behavior
- **Acceptance:** the compiler is defined as a first-class subsystem rather than buried in prose
- **Carry-forward topics:** compiler pipeline changes, retrieval rules, memory/canon injection rules, replay constraints

#### [x] P3.3 — Data / storage / indexing / provenance spec
- **Mode:** Human + Factory
- **Depends on:** P3.1
- **Deliverable:** storage classes, relational metadata, event streams, object/blob storage, vector/search index, graph/provenance rules, migration/invalidation/rebuild rules
- **Acceptance:** storage and provenance lanes are explicit and separable
- **Carry-forward topics:** storage-class decisions, provenance model changes, rebuild rules, migration implications

#### [x] P3.4 — API / IPC / event contract spec
- **Mode:** Human + Factory
- **Depends on:** P3.1 and P3.3
- **Deliverable:** contracts for environment shell <-> engine, app <-> engine, UI <-> workers, runtime <-> model gateway, runtime <-> tool adapters, approvals/branching/replay/writeback/live-monitor events
- **Acceptance:** major process boundaries and message contracts are typed and explicit
- **Carry-forward topics:** event types, IPC rules, adapter contracts, compatibility constraints

#### [x] P3.5 — Platform Gate spec + exit audit
- **Mode:** Human + Factory
- **Depends on:** P3.1 through P3.4
- **Deliverable:** internal gate spec, required primitives, forced packages, exit tests, audit checklist
- **Acceptance:** there is a hard pre-R1 gate and a concrete way to test it
- **Carry-forward topics:** forced packages, gate test changes, missing prerequisites, audit failures and fixes

#### [x] P3.6 — Architecture synchronization pass
- **Mode:** Human-only
- **Depends on:** P3.1 through P3.5
- **Deliverable:** hard sync review across canon, seam map, scenario corpus, projection grammar, forbidden shortcuts, and Platform Gate
- **Acceptance:** no silent reintroduction of transcript-first or app-private ontology drift
- **Carry-forward topics:** sync findings, contradictions resolved, stale downstream items, architecture corrections

---

## Phase 4 — Fixed chat-native release doctrine `[x]`

### Goal

Convert the release roadmap into concrete release architecture contracts that drive implementation and SDK hardening.

### Exit condition

This phase is done when the release-to-SDK matrix, milestone architecture, and contract packs for Platform Gate through R7 are accepted.

#### [x] P4.1 — Release-to-SDK maturity matrix
- **Mode:** Human + Factory
- **Depends on:** P3.5
- **Deliverable:** matrix mapping Platform Gate and each release to the SDK/package areas that must become real
- **Acceptance:** every release forces explicit substrate maturity and nothing is hand-waved
- **Carry-forward topics:** package maturity changes, forced-package corrections, matrix implications

#### [x] P4.2 — Release / milestone architecture plan
- **Mode:** Human-only
- **Depends on:** P4.1 and P3.6
- **Deliverable:** milestone architecture plan covering what is exposed, what is deferred, and where overbuilding is intentionally refused
- **Acceptance:** there is one accepted release architecture story distinct from implementation blueprints
- **Carry-forward topics:** milestone boundary changes, deferrals, conscious non-goals, sequencing clarifications

#### [x] P4.3 — R1 Transcript Chat contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** product promise, shared primitives, chat-domain primitives, packages forced to mature, exit criteria, non-goals
- **Acceptance:** R1 is an explicit contract, not just a name on a roadmap
- **Carry-forward topics:** R1 surface clarifications, exit criteria changes, hidden assumptions uncovered

#### [x] P4.4 — R2 Context Chat contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** contract pack for packs, spans, memory/canon visibility, inclusion/exclusion explainability, save/diff/merge/freeze behavior
- **Acceptance:** R2 is defined as real context control rather than fake sidebar behavior
- **Carry-forward topics:** pack semantics, span rules, inclusion/exclusion policies, diff/freeze behavior

#### [x] P4.5 — R3 Branch / Visual Thinker contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** contract pack for branching, replay, compare, off-chain jobs, merge proposals, mode projections
- **Acceptance:** branching is semantic and replayable, not transcript cloning
- **Carry-forward topics:** branch types, replay semantics, compare rules, off-chain merge behavior

#### [x] P4.6 — R4 Artifact Workspace contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** contract pack for focal artifacts, proposal inbox, root canon strip, review/approval loop, historical truth per run
- **Acceptance:** continuity moves from transcript gravity to artifact-centered work
- **Carry-forward topics:** artifact roles, proposal behavior, review/approval rules, historical truth rules

#### [x] P4.7 — R5 Prompt Studio contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** contract pack for canonical prompts, prompt cards, model profiles, adaptations, lineage, staleness
- **Acceptance:** prompt assets are governed, versioned, and reusable
- **Carry-forward topics:** adaptation rules, staleness logic, model-profile behavior, reuse rules

#### [x] P4.8 — R6 Governed Agent / Applet Chat contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** contract pack for Protocols, Context Recipes, Strategy Presets, Verifier Packs, Workflows, Triggers, Applets, bounded background runs
- **Acceptance:** reusable governed execution becomes real without collapsing into agent theater
- **Carry-forward topics:** protocol creation rules, applet boundaries, background-run rules, memory/contradiction policies

#### [x] P4.9 — R7 Commissioning Bridge contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.2
- **Deliverable:** contract pack for Commission, Contract, Run Class, Authority Scope, Live Monitor, Proof Ledger, Delta Inspector, lane-by-lane writeback, chat-to-run handoff
- **Acceptance:** chat-native work reaches explicit commissioning semantics and can hand into Task Studio without ontology translation
- **Carry-forward topics:** commissioning rules, authority/preflight rules, handoff semantics, writeback-lane controls

---

## Phase 5 — Full reusable semantics and Task Studio readiness `[x]`

### Goal

Complete the reusable semantics stack and make the R7 -> Task Studio handoff structurally real before Task Studio becomes the primary app surface.

### Exit condition

This phase is done when governance, proof, protocol packs, reusable execution objects, Task Studio surfaces, V1 scope, and the commissioning-bridge handoff contract are accepted.

#### [x] P5.1 — Full governance / authority / writeback spec
- **Mode:** Human + Factory
- **Depends on:** P2.3 and P4.9
- **Deliverable:** complete policy, approval, side-effect preview, partial acceptance, rollback/compensation, scope-aware writeback model
- **Acceptance:** governance is machine-usable and reviewable, not only conceptual
- **Carry-forward topics:** approval-routing rules, compensation rules, partial-accept rules, governance edge cases

#### [x] P5.2 — Full proof / validation / evaluation spec
- **Mode:** Human + Factory
- **Depends on:** P2.4 and P4.9
- **Deliverable:** verifier packs, proof assemblers, evaluation fixtures, replay/regression suites, task-family proof sections
- **Acceptance:** proof and evaluation are explicit enough to drive implementation and review
- **Carry-forward topics:** proof pack changes, evaluation fixture additions, task-family proof refinements

#### [x] P5.3 — Full run-class protocol packs
- **Mode:** Human + Factory
- **Depends on:** P2.2 and P5.1 and P5.2
- **Deliverable:** protocol packs with intake schema, contract schema, result schema, proof schema, context recipe, strategy preset, verifier pack, authority defaults, writeback defaults, failure classes, fixtures
- **Acceptance:** reusable execution is typed and versionable
- **Carry-forward topics:** protocol versioning rules, defaults by run class, fixture changes, failure-class refinements

#### [x] P5.4 — Workflow / Trigger / Applet / Pack / Integration Binding specs
- **Mode:** Human + Factory
- **Depends on:** P5.3
- **Deliverable:** reusable execution composition specs and packaging specs
- **Acceptance:** recurring and packaged work composes from the run model rather than inventing a separate ontology
- **Carry-forward topics:** trigger types, packaging rules, integration binding rules, composition constraints

#### [x] P5.5 — Task Studio surface and lifecycle contract pack
- **Mode:** Human + Factory
- **Depends on:** P4.9 and P5.1 through P5.4
- **Deliverable:** Task Studio surfaces, lifecycle stages, layout rule, progressive disclosure model
- **Acceptance:** Task Studio is specified as a real app model, not just a future idea
- **Carry-forward topics:** surface changes, lifecycle clarifications, layout rules, progressive-disclosure refinements

#### [x] P5.6 — Task Studio V1 scope pack
- **Mode:** Human-only
- **Depends on:** P5.5
- **Deliverable:** V1 task families, result/proof expectations, non-goals, initial build scope, onboarding/category-teaching constraints
- **Acceptance:** V1 scope is explicit and protected from uncontrolled sprawl
- **Carry-forward topics:** V1 inclusions/exclusions, onboarding insights, scope boundary changes

#### [x] P5.7 — Commissioning Bridge -> Task Studio handoff contract
- **Mode:** Human-only
- **Depends on:** P4.9 and P5.5 and P5.6
- **Deliverable:** exact object and surface mapping from R7 semantics into Task Studio surfaces
- **Acceptance:** Task Studio is a projection change, not a semantic translation or rewrite
- **Carry-forward topics:** handoff mappings, incompatibilities found, bridge corrections, stale downstream items if mapping changes

---

## Phase 6 — Surface/codebase substrate and execution machinery `[x]`

### Goal

Turn accepted specs into a repo, package map, implementation system, and bounded execution packets that Factory and humans can use safely.

### Exit condition

This phase is done when the package map, documentation plane, Factory operating system, pilot packets, blueprints, and execution packets are in place.

#### [x] P6.1 — Surface contract packs
- **Mode:** Human + Factory
- **Depends on:** P2.6 and P5.5
- **Deliverable:** shared projection grammar packs, chat-native surface contracts, Task Studio surface contracts, later domain-surface backlog contracts
- **Acceptance:** surfaces reuse one grammar and remain aligned to accepted semantics
- **Carry-forward topics:** surface contract changes, shared grammar overrides, later-domain implications

#### [x] P6.2 — Repo/package architecture and agent execution rules
- **Mode:** Human + Factory
- **Depends on:** P3.6 and P4.1 and P5.7
- **Deliverable:** full package map, repo layout, package boundaries, agent execution rules, module contract requirements
- **Acceptance:** the repo shape follows architecture and release truth rather than dictating it
- **Carry-forward topics:** package additions, package boundary moves, module contract rules, agent execution rule changes

#### [x] P6.3 — Agent-oriented codebase pattern and documentation plane
- **Mode:** Human + Factory
- **Depends on:** P6.2
- **Deliverable:** documentation plane, generated current-state view, manifests, test-contract files, fixture rules, compiled context-pack rules for agent packets
- **Acceptance:** agents can navigate and execute safely from accepted artifacts
- **Carry-forward topics:** manifest rules, documentation-generation rules, fixture policies, packet compilation changes

#### [x] P6.4 — Pilot packet set + Factory benchmark harness + internal skills/adapters
- **Mode:** Factory-first
- **Depends on:** P0.3 and P6.2 and P6.3
- **Deliverable:** pilot packet set, benchmark results, internal Factory skills/adapters, tuning notes
- **Acceptance:** the execution environment is tested on real packet types before scaling up
- **Carry-forward topics:** packet performance findings, skill improvements, adapter gaps, benchmark outcomes

#### [x] P6.5 — Release implementation blueprints
- **Mode:** Human + Factory
- **Depends on:** P4.2 through P4.9 and P6.2
- **Deliverable:** release-by-release blueprints with touched modules, schemas, migrations, APIs/events, UI states, tests, fixtures, exclusions
- **Acceptance:** each release has a real blueprint that can be handed to implementers
- **Carry-forward topics:** blueprint corrections, module touch changes, migration updates, test coverage changes

#### [x] P6.6 — Agent execution packets
- **Mode:** Factory-first
- **Depends on:** P6.5
- **Deliverable:** bounded packets with scope, file whitelist, dependencies, deliverables, validation hooks, approval rules
- **Acceptance:** implementation work can be delegated safely in bounded units
- **Carry-forward topics:** packet template changes, validation hook changes, common failure modes, execution guardrail refinements

---

## Phase 7 — Continuous sync and deltas `[~]`

### Goal

Keep the whole program coherent after work starts landing by making stale detection, delta capture, and recurring sync part of the operating model.

### Exit condition

This phase is done when every accepted change triggers delta capture, stale detection, sync checks, and regeneration where needed.

#### [x] P7.1 — Carry-forward delta pack after every packet/release
- **Mode:** Factory-first
- **Depends on:** P6.6
- **Deliverable:** delta pack template and operating rule for every accepted packet/release
- **Acceptance:** each accepted change leaves a durable, reviewable record of what changed and what that change affects
- **Carry-forward topics:** delta template changes, recurring omissions, better downstream impact capture

#### [ ] P7.2 — Recurring architecture synchronization after every accepted delta
- **Mode:** Human + Factory
- **Depends on:** P7.1
- **Deliverable:** recurring sync checklist and execution routine
- **Acceptance:** accepted changes do not silently diverge from canon, semantics, or architecture
- **Carry-forward topics:** recurring contradictions, sync failure patterns, architecture pressure points

#### [ ] P7.3 — Stale dependency detection and regeneration loop
- **Mode:** Factory-first
- **Depends on:** P7.1 and P7.2
- **Deliverable:** stale detection rules, regeneration workflow, stale-marker updates
- **Acceptance:** downstream artifacts are marked stale and regenerated when upstream truth changes
- **Carry-forward topics:** stale-detection failures, regeneration rules, dependency graph corrections

#### [ ] P7.4 — Release gate re-check automation
- **Mode:** Factory-first
- **Depends on:** P7.3
- **Deliverable:** automated re-check routines for release gates after accepted changes
- **Acceptance:** changes that affect release readiness automatically trigger the right checks
- **Carry-forward topics:** gate automation changes, noisy checks, missing checks, release-readiness drift

---

## 9. Append-only carry-forward log

### Rules

- Append only.
- New entries go at the end.
- Never delete or rewrite old entries.
- If a prior entry is wrong, add a correction entry that references it.

### Entry template

Use this format for new entries:

```text
CF-XXXX | YYYY-MM-DD | Source: <PHASE/TASK/DECISION>

New information:
- ...

Impact:
- ...

Status changes:
- ...

Stale items:
- ...

Notes for future prompts:
- ...
```

### Current entries

#### CF-0001 | 2026-04-10 | Source: Baseline planning update

New information:
- The current source authority is fixed to three documents: the engine/shared-environment primitive set, the chat-native release plan, and the Task Studio north-star app spec.

Impact:
- All future expansion, architecture, and prompt work must treat those three documents as the canonical basis for this plan.

Status changes:
- Source authority recorded as done in this file.

Stale items:
- None.

Notes for future prompts:
- Prompts must carry forward the layer split, release doctrine, and Task Studio north-star role.

#### CF-0002 | 2026-04-10 | Source: Baseline planning update

New information:
- Accepted baseline decisions are now explicit: three-layer architecture, chat-native wedge first, Task Studio north star, fixed release order, no transcript truth, no private competing ontology per release.

Impact:
- Fresh sessions should not reopen these decisions unless explicitly told to do so.

Status changes:
- Baseline product truth recorded as done in this file.

Stale items:
- None.

Notes for future prompts:
- Generated prompts must treat these as fixed context, not optional discussion points.

#### CF-0003 | 2026-04-10 | Source: Tooling policy update

New information:
- Factory.ai is the primary execution and automation layer for this program.
- CrewAI is removed from the base plan.
- CrewAI remains only an optional later branch if an always-on, event-driven automation layer outside normal repo/CI execution becomes necessary.

Impact:
- The default plan should not add a second orchestration stack.
- Factory-specific operating contracts, skills, and headless execution become part of the plan.

Status changes:
- Tooling policy recorded as done in this file.

Stale items:
- Any earlier assumption that CrewAI belongs in the base plan.

Notes for future prompts:
- Prompts must default to human-owned product truth plus Factory-executed bounded work.

#### CF-0004 | 2026-04-10 | Source: Master planning artifact creation

New information:
- This master plan file is now the working control document for fresh sessions.
- It includes status markers, a universal prompt template, and an append-only carry-forward log.

Impact:
- Fresh sessions can use this file directly to expand phases/tasks into prompts and to record completion state.

Status changes:
- P0.0 marked done.
- Phase 0 marked in progress.

Stale items:
- None.

Notes for future prompts:
- Any prompt generated from this file must include the current completion snapshot and the full carry-forward log.

#### CF-0005 | 2026-04-11 | Source: P0.1 — Artifact registry, dependency graph, and promotion model

New information:
- A repo-level control-plane artifact model now exists under `docs/control-plane/`.
- The control plane defines major artifact families, semantic ID patterns, acceptance/stewardship fields, dependency edge semantics, promotion statuses, stale rules, and validation-hook standards.
- The master plan is now mirrored in-repo as the canonical control-plane record, and the P0.1 artifacts are accepted for downstream use.

Impact:
- Downstream tasks can register artifacts against one control-plane model instead of inventing ad hoc metadata.
- P0.2 and P1.1 can rely on explicit dependency and stale-propagation semantics.
- Repo placement is now standardized for control-plane artifacts without making repo layout the platform architecture.

Status changes:
- P0.1 marked done.
- The completion snapshot line for the repo-level artifact registry and dependency graph has been updated to done.
- Phase 0 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Preserve the distinction between control-plane artifact types and runtime product primitives.
- Preserve the separation of semantic owner, stewardship mode, and acceptance authority.
- Reuse the defined stale rules and validation-hook standards rather than inventing task-local alternatives.

#### CF-0006 | 2026-04-11 | Source: P0.2 — Lightweight repo / agent operating contract

New information:
- Root `AGENTS.md`, `docs/control-plane/AGENTS.md`, `docs/control-plane/core/repo-agent-operating-contract.md`, and `docs/control-plane/core/packet-brief.schema.json` now exist and are registered as accepted control-plane artifacts.
- The repo now has an accepted-artifact-only default, explicit root and subtree instruction layering, and a lightweight packet-brief baseline for bounded work.

Impact:
- P0.3 can extend repo execution behavior without redefining baseline truth or instruction precedence.
- P0.5 can build packet policy on top of an accepted minimum packet-brief schema instead of inventing one.
- Downstream work can rely on AGENTS projections as execution guidance without treating them as a competing truth model.

Status changes:
- P0.2 marked done.
- The completion snapshot line for the lightweight repo/agent operating contract has been updated to done.
- Phase 0 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Preserve the accepted-artifact-only default unless an explicit task targets provisional material.
- Treat packet briefs as scope-narrowing execution artifacts, not source-of-truth replacements.
- Keep Factory-specific skills, headless execution rules, and automated-run review conventions deferred to P0.3.

#### CF-0007 | 2026-04-11 | Source: P0.3 — Factory operating contract

New information:
- Repo-scoped Factory execution assets now live under `/.factory/`, including `/.factory/factory-operating-contract.md`, `/.factory/AGENTS.md`, and initial shared skills for bounded packet execution and automated review guidance.
- Headless `droid exec` conventions, allowed autonomy bands, review gates, and failure handling are now explicit and registered as accepted control-plane artifacts.

Impact:
- Downstream packets and headless automation can rely on one accepted Factory-specific execution contract instead of inventing repo-local conventions.
- P6.4 now has a concrete repo baseline for project skills and headless execution behavior.
- P0.5 can layer packet-budget and context-policy work on top of an accepted Factory execution contract rather than bundling those concerns into P0.3.

Status changes:
- P0.3 marked done.
- The completion snapshot line for the Factory operating contract has been updated to done.
- Phase 0 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Use `/.factory/factory-operating-contract.md` plus the shared `/.factory/skills/` assets as the default Factory execution basis for repo-scoped packets and headless runs.
- Keep custom droids and hooks optional and additive; do not use them to bypass human acceptance or to smuggle P0.5-only packet policy into execution.

#### CF-0008 | 2026-04-11 | Source: P0.4 — Forbidden-shortcuts register

New information:
- An accepted forbidden-shortcuts register now exists at `docs/control-plane/core/forbidden-shortcuts-register.md`.
- The register formalizes the accepted shortcut baseline from `docs/control-plane/core/master-plan.md` Section 4.3 and maps current enforcement points plus named future review/lint points.
- New artifact `cp.forbidden-shortcuts-register.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Downstream control-plane, architecture, release, and execution work can now reference one accepted anti-drift register instead of restating shortcut prohibitions ad hoc.
- Phase 0 now has the accepted P0.4 shortcut artifact it needed; only P0.5 remains open in Phase 0.

Status changes:
- P0.4 marked done.
- The completion snapshot line for the forbidden-shortcuts register has been updated to done.
- Phase 0 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Preserve the distinction between current enforcement points and future named review/lint points.
- Keep P0.5 packet-budget and context-policy work separate from this accepted P0.4 register.

#### CF-0009 | 2026-04-11 | Source: P0.5 — Context-budget and packet policy

New information:
- An accepted P0.5 context-budget and packet policy now exists at `docs/control-plane/core/context-budget-and-packet-policy.md`.
- The policy defines packet budget bands, packet composition rules, local-doc-first reading, bounded subagent exploration, and escalation discipline on top of accepted P0.2, P0.3, and P0.4 artifacts.
- New artifact `cp.context-budget-and-packet-policy.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Downstream packet work can now rely on one accepted packet-budget and packet-composition policy instead of inventing task-local context-budget rules.
- Phase 0 now has its final accepted artifact and is complete.

Status changes:
- P0.5 marked done.
- The completion snapshot line for the context-budget and packet policy has been updated to done.
- Phase 0 marked done.

Stale items:
- None.

Notes for future prompts:
- Treat `cp.context-budget-and-packet-policy.v1` as the accepted control-plane basis for packet budget bands, local-doc-first reading, bounded subagent exploration, and escalation handling.
- Do not use this artifact to smuggle runtime context-compiler topology, repo/package architecture, or a second orchestration stack into later work.

#### CF-0010 | 2026-04-11 | Source: P1.1 — Source decomposition / contradiction register / glossary

New information:
- A review-ready P1.1 canon pack now exists at `docs/control-plane/canon/phase-1-source-decomposition-contradictions-and-glossary.md`.
- The pack extracts the major governing claims from the three source-authority documents, makes cross-source tensions explicit, normalizes major terms, and names unresolved terms for later tasks.
- New artifact `canon.phase1-source-decomposition.v1` is registered in the control-plane registry and dependency graph as `review_ready`.

Impact:
- P1.2 now has a concrete decomposition/glossary basis for human review and canon freeze work instead of re-deriving terminology from scratch.
- Downstream Phase 1 and Phase 2 work can reuse one review-ready normalization pack while preserving the human-owned acceptance boundary.

Status changes:
- P1.1 marked in progress with validated review-ready deliverables present and human acceptance still pending.
- Phase 1 marked in progress.

Stale items:
- None.

Notes for future prompts:
- Preserve the distinction between transcript continuity, run consequence, and artifact-centered continuity.
- Preserve the distinction between product canon in the control plane and runtime Canon Objects in the shared environment.
- Keep prompt assets distinct from execution assets when expanding Prompt Studio, Protocol, Workflow, and Applet work.

#### CF-0011 | 2026-04-11 | Source: P1.1 — Human acceptance and landing

New information:
- `docs/control-plane/canon/phase-1-source-decomposition-contradictions-and-glossary.md` is now accepted for downstream use.
- Artifact `canon.phase1-source-decomposition.v1` has been promoted from `review_ready` to `accepted`.

Impact:
- P1.2 is now unblocked on an accepted source decomposition/glossary basis.
- Downstream Phase 1 and Phase 2 work can reference one accepted terminology/tension pack instead of re-deriving these interpretations.

Status changes:
- P1.1 marked done.
- The completion snapshot now records the Phase 1 source decomposition / contradiction register / glossary pack as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `canon.phase1-source-decomposition.v1` as the accepted normalization basis for layer ownership, continuity semantics, projection-vs-ontology rules, and the product-canon vs runtime-canon distinction.

#### CF-0012 | 2026-04-11 | Source: P1.2 — Canon freeze / resolved product interpretation

New information:
- A review-ready P1.2 canon note now exists at `docs/control-plane/canon/phase-1-canon-freeze-and-resolved-product-interpretation.md`.
- The note resolves the first wedge, north-star app, fixed release order, projection-vs-ontology rule, and non-negotiable downstream constraints into one reviewable artifact.
- New artifact `canon.phase1-product-interpretation-freeze.v1` is registered in the control-plane registry and dependency graph as `review_ready`.

Impact:
- P1.3 through P1.6 now have a concrete review-ready interpretation note to review against while preserving the human-owned acceptance boundary.
- The accepted P1.1 normalization pack is now paired with a draft canon-freeze note instead of leaving P1.2 implicit.

Status changes:
- P1.2 marked in progress with validated review-ready deliverables present and human acceptance still pending.
- Phase 1 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Treat this P1.2 note as the review-ready basis for wedge, north star, release order, and projection-vs-ontology interpretation, but do not treat it as accepted canon until a human explicitly approves it.

#### CF-0013 | 2026-04-11 | Source: P1.2 — Human acceptance and landing

New information:
- `docs/control-plane/canon/phase-1-canon-freeze-and-resolved-product-interpretation.md` is now accepted for downstream use.
- Artifact `canon.phase1-product-interpretation-freeze.v1` has been promoted from `review_ready` to `accepted`.

Impact:
- P1.3 is now unblocked on an accepted canon-freeze basis.
- Downstream Phase 1 work can rely on one accepted interpretation note for wedge, north star, fixed release order, projection-vs-ontology rules, and non-negotiable constraints.

Status changes:
- P1.2 marked done.
- The completion snapshot now records the Phase 1 canon freeze / resolved product interpretation note as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `canon.phase1-product-interpretation-freeze.v1` together with `canon.phase1-source-decomposition.v1` as the accepted Phase 1 canon basis for P1.3 through P1.6.

#### CF-0014 | 2026-04-11 | Source: P1.3 — Layer and primitive separation pack

New information:
- A review-ready P1.3 owner-layer pack now exists at `docs/control-plane/canon/phase-1-layer-and-primitive-separation-pack.md`.
- The pack assigns one owner layer to the major primitive families across engine, shared environment, chat-domain, Task Studio, and later domain packs, and it explicitly names non-owners.
- New artifact `canon.phase1-layer-primitive-separation.v1` is registered in the control-plane registry and dependency graph as `review_ready`.

Impact:
- P1.4 and P1.5 now have a concrete review-ready layer-ownership basis instead of leaving projection language and owner boundaries implicit.
- Later semantic and architecture work now has one review-ready map for projection pairs, app-vs-shared ownership, and domain-pack containment.

Status changes:
- P1.3 marked in progress with validated review-ready deliverables present and human acceptance still pending.
- Phase 1 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Treat this pack as the review-ready owner-layer map, but do not treat it as accepted canon until a human explicitly approves it.
- Preserve the rule that Task Studio owns a commissioned-work app projection, not the underlying shared primitives it uses.

#### CF-0015 | 2026-04-11 | Source: P1.3 — Human acceptance and landing

New information:
- `docs/control-plane/canon/phase-1-layer-and-primitive-separation-pack.md` is now accepted for downstream use.
- Artifact `canon.phase1-layer-primitive-separation.v1` has been promoted from `review_ready` to `accepted`.

Impact:
- P1.4 and P1.5 are now grounded on one accepted owner-layer map instead of a review-ready draft.
- Later semantic and architecture work now has an accepted basis for owner-layer decisions, projection pairs, and non-owner boundaries.

Status changes:
- P1.3 marked done.
- The completion snapshot now records the Phase 1 layer and primitive separation pack as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `canon.phase1-layer-primitive-separation.v1` together with the accepted P1.1 and P1.2 canon packs as the Phase 1 owner-layer baseline for later topology, seam, and semantic work.

#### CF-0016 | 2026-04-11 | Source: P1.4 — Surface and release topology canon

New information:
- `docs/control-plane/canon/phase-1-surface-and-release-topology-canon.md` now defines the accepted topology story for Platform Gate, R1-R7, Task Studio handoff, surface emphasis, mode rules, and cross-app handoff rules.
- Artifact `canon.phase1-surface-release-topology.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 1 now has an accepted release-path and surface-topology basis for rewrite containment, scenario design, and later release-contract work.
- Downstream packs can now reuse one accepted continuity-and-handoff story instead of inventing local release topology narratives.

Status changes:
- P1.4 marked done.
- The completion snapshot now records the Phase 1 surface and release topology canon as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `canon.phase1-surface-release-topology.v1` together with the accepted P1.1-P1.3 canon artifacts as the Phase 1 topology baseline for P1.5, P1.6, and Phase 4 release packs.

#### CF-0017 | 2026-04-11 | Source: P1.5 — Rewrite-containment / stable seam map

New information:
- `docs/control-plane/canon/phase-1-rewrite-containment-and-stable-seam-map.md` now defines the accepted high-, medium-, and low-blast-radius seams for the substrate, bridge releases, and app projections.
- Artifact `canon.phase1-rewrite-containment-seams.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 1 now has an accepted rewrite-containment basis for architecture, scenario, and repo/package work.
- High-blast-radius seams are now explicit enough to guide later implementation without relying on hidden assumptions.

Status changes:
- P1.5 marked done.
- The completion snapshot now records the Phase 1 rewrite-containment / stable seam map as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `canon.phase1-rewrite-containment-seams.v1` together with the accepted P1.1-P1.4 canon artifacts as the Phase 1 rewrite-containment baseline for P1.6, Phase 3 architecture, and Phase 6 repo/package planning.

#### CF-0018 | 2026-04-11 | Source: P1.6 — Golden scenario corpus + edge-case suite

New information:
- `docs/control-plane/canon/phase-1-golden-scenario-corpus-and-edge-case-suite.md` now defines the accepted scenario corpus spanning the chat-native wedge, bridge releases, reusable execution, commissioning, and Task Studio handoff.
- Artifact `canon.phase1-scenario-corpus.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 1 now has an accepted scenario baseline for semantic, architecture, release-contract, and repo/package work.
- The major semantic pathways and edge cases are now explicit enough to drive later validation work.

Status changes:
- P1.6 marked done.
- Phase 1 marked done.
- The completion snapshot now records the Phase 1 golden scenario corpus and edge-case suite as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `canon.phase1-scenario-corpus.v1` together with the accepted P1.1-P1.5 canon artifacts as the full Phase 1 baseline for Phase 2 and later work.

#### CF-0019 | 2026-04-11 | Source: P2.1 — Core object and state-machine spec pack

New information:
- `docs/control-plane/semantics/phase-2-core-object-and-state-machine-spec-pack.md` now defines the accepted shared first-class object contracts, identity rules, and lifecycle/state-machine semantics for Run, Artifact, Branch, Proof Bundle, State Delta, Writeback Proposal, Memory, Canon, Commission, Contract, Protocol, Applet, Review, Approval Decision, and related support objects.
- Artifact `sem.phase2-core-object-state-machines.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 2 now has an accepted object-model baseline that later run-class, governance, release, and architecture work can build against.
- High-blast-radius continuity, lane separation, commissioned-work continuity, and Task Studio handoff semantics are now formalized as explicit shared object contracts.

Status changes:
- P2.1 marked done.
- Phase 2 marked in progress.
- The completion snapshot now records the Phase 2 core object and state-machine spec pack as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `sem.phase2-core-object-state-machines.v1` as the baseline semantic contract pack for P2.2 through P2.6 and for Phase 3 storage/API/runtime work.

#### CF-0020 | 2026-04-11 | Source: P2.2 — Run-class taxonomy + protocol kernel

New information:
- `docs/control-plane/semantics/phase-2-run-class-taxonomy-and-protocol-kernel.md` now defines the accepted base run classes, V1 Task Studio task-family mapping, protocol-kernel required fields, schema skeletons, authority defaults, verifier slots, and writeback defaults.
- Artifact `sem.phase2-run-class-taxonomy-protocol-kernel.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 2 now has an accepted execution-typing baseline that later governance, release, reusable-execution, and Task Studio work can build against.
- V1 task-family labels are now explicitly downstream projections over shared run classes instead of vague generic task buckets.

Status changes:
- P2.2 marked done.
- The completion snapshot now records the Phase 2 run-class taxonomy and protocol-kernel pack as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `sem.phase2-run-class-taxonomy-protocol-kernel.v1` together with `sem.phase2-core-object-state-machines.v1` as the Phase 2 execution-typing baseline for P2.3, P2.4, P2.5, P4.8, P4.9, and P5.3.

#### CF-0021 | 2026-04-11 | Source: P2.3 — Governance / authority / writeback invariants

New information:
- `docs/control-plane/reuse/phase-2-governance-authority-and-writeback-invariants.md` now defines the accepted invariant layer for scope widening, lane separation, approval points, policy boundaries, and authority semantics.
- Artifact `reuse.phase2-governance-authority-writeback-invariants.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 2 now has an accepted governance baseline that later release, applet, commissioning, and full governance specs can reuse.
- Approval points, lane separation, and authority non-self-expansion are now formalized as explicit shared invariants rather than UI assumptions.

Status changes:
- P2.3 marked done.
- The completion snapshot now records the Phase 2 governance, authority, and writeback invariants as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase2-governance-authority-writeback-invariants.v1` together with `sem.phase2-core-object-state-machines.v1` and `sem.phase2-run-class-taxonomy-protocol-kernel.v1` as the governance baseline for P2.4, P2.5, P4.8, P4.9, and P5.1.

#### CF-0022 | 2026-04-11 | Source: P2.4 — Proof / validation invariants

New information:
- `docs/control-plane/reuse/phase-2-proof-and-validation-invariants.md` now defines the accepted invariant layer for proof expectations, uncertainty labeling, omission handling, contradiction handling, replay/comparison expectations, and baseline failure classes.
- Artifact `reuse.phase2-proof-validation-invariants.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 2 now has an accepted proof baseline that later release packs, Task Studio proof surfaces, and full evaluation specs can reuse.
- Proof is now formalized as run-class-shaped, frozen-basis, inspectable support rather than a generic explanation blob.

Status changes:
- P2.4 marked done.
- The completion snapshot now records the Phase 2 proof and validation invariants as accepted.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase2-proof-validation-invariants.v1` together with the accepted P2.1-P2.3 artifacts as the proof baseline for P2.5, P4 release packs, and P5.2.

#### CF-0023 | 2026-04-11 | Source: P2.5 — Chat-native semantic packs by release

New information:
- `docs/control-plane/semantics/phase-2-chat-native-semantic-packs-by-release.md` now defines the accepted semantic overlay for each public chat-native release from R1 Transcript Chat through R7 Commissioning Bridge.
- Artifact `sem.phase2-chat-native-semantic-packs.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 2 now has an accepted release-semantics baseline that P2.6 and the later Phase 4 release contract packs can extend without inventing release-private ontologies.
- Each chat-native release now has one explicit mapping from shared objects to projection vocabulary, governance/proof exposure, and handoff obligations.

Status changes:
- P2.5 marked done.
- The completion snapshot now records the Phase 2 chat-native semantic packs by release as accepted.
- Phase 2 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Use `sem.phase2-chat-native-semantic-packs.v1` together with the accepted P2.1-P2.4 artifacts as the release-semantics baseline for P2.6, Phase 4 release packs, and the R7 -> Task Studio bridge.

#### CF-0024 | 2026-04-11 | Source: P2.6 — Projection grammar contract pack

New information:
- `docs/control-plane/semantics/phase-2-projection-grammar-contract-pack.md` now defines the accepted shared interaction grammar for Composer, Canvas, Inspector, Browser / Library, Timeline, Ledger, Compare View, Queue / Inbox, Board, Diff / Merge View, Live Monitor, and Console.
- Artifact `sem.phase2-projection-grammar-contracts.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 2 now has an accepted surface-grammar baseline that later architecture, release, and surface-contract work can extend without inventing private view metaphors.
- Chat-native aliases and Task Studio surface names now have one explicit mapping back to shared grammar contracts and compositions.

Status changes:
- P2.6 marked done.
- The completion snapshot now records the Phase 2 projection grammar contract pack as accepted.
- Phase 2 marked done.

Stale items:
- None.

Notes for future prompts:
- Use `sem.phase2-projection-grammar-contracts.v1` together with `canon.phase1-surface-release-topology.v1`, `sem.phase2-core-object-state-machines.v1`, and `sem.phase2-chat-native-semantic-packs.v1` as the surface-grammar baseline for Phase 3 architecture, Phase 4 release packs, and Phase 6 surface contracts.

#### CF-0025 | 2026-04-11 | Source: P3.1 — High-level technical architecture baseline

New information:
- `docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md` now defines the accepted runtime topology, process model, hosted-default local/cloud split, layer boundary map, and identity/tenancy touchpoints for the platform baseline.
- Artifact `arch.phase3-technical-architecture-baseline.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 3 now has an accepted top-level architecture story that P3.2 through P3.5 can refine without inventing new top-level runtime planes.
- The program now has one explicit technical baseline tying the accepted semantic objects to bounded workers, shared data/provenance planes, and projection-only clients.

Status changes:
- P3.1 marked done.
- The completion snapshot now records the Phase 3 high-level technical architecture baseline as accepted.
- Phase 3 marked in progress.

Stale items:
- None.

Notes for future prompts:
- Use `arch.phase3-technical-architecture-baseline.v1` together with the accepted P2.1-P2.6 artifacts as the architecture baseline for compiler, storage, API/event, Platform Gate, and later repo/package work.

#### CF-0026 | 2026-04-11 | Source: P3.2 — Context compiler / retrieval / memory / canon topology

New information:
- `docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md` now defines the accepted compiler subsystem topology for ingestion, spanization, evidence/context separation, staged retrieval, memory/canon injection, freeze/replay/diff, and recovery/compaction behavior.
- Artifact `arch.phase3-context-compiler-topology.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 3 now has an accepted compiler baseline that P3.3 through P3.5 can refine without burying context assembly inside generic orchestration prose.
- The program now has one explicit topology for R2 context control, R3 replay, R7 preflight, and Task Studio context inspection to project.

Status changes:
- P3.2 marked done.
- The completion snapshot now records the Phase 3 context compiler / retrieval / memory / canon topology as accepted.
- Phase 3 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Use `arch.phase3-context-compiler-topology.v1` together with `arch.phase3-technical-architecture-baseline.v1` and the accepted P2 artifacts as the compiler baseline for storage/index, API/event, Platform Gate, and later context-facing release work.

#### CF-0027 | 2026-04-11 | Source: P3.3 — Data / storage / indexing / provenance spec

New information:
- `docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md` now defines the accepted storage-class, event-stream, provenance, migration, invalidation, and rebuild baseline for the platform.
- Artifact `arch.phase3-data-storage-provenance-spec.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 3 now has an accepted data and provenance baseline that P3.4, P3.5, and later sync/regeneration work can extend without collapsing authoritative and derived lanes.
- The program now has one explicit separation between metadata, blobs, events, provenance, indexes, caches, and secrets.

Status changes:
- P3.3 marked done.
- The completion snapshot now records the Phase 3 data / storage / indexing / provenance spec as accepted.
- Phase 3 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Use `arch.phase3-data-storage-provenance-spec.v1` together with the accepted P3.1 and P3.2 architecture packs as the storage/provenance baseline for API/event contracts, Platform Gate, and later stale/regeneration automation.

#### CF-0028 | 2026-04-11 | Source: P3.4 — API / IPC / event contract spec

New information:
- `docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md` now defines the accepted boundary-contract baseline for APIs, internal IPC, gateway adapters, and shared event families.
- Artifact `arch.phase3-api-ipc-event-contracts.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 3 now has an accepted contract baseline covering environment/control boundaries, worker IPC, gateway adapters, and event-spine semantics for approvals, branching, replay, writeback, and live monitoring.
- The program now has one explicit rule set preventing direct UI-to-worker RPC and transcript-blob boundary contracts.

Status changes:
- P3.4 marked done.
- The completion snapshot now records the Phase 3 API / IPC / event contract spec as accepted.
- Phase 3 remains in progress pending Platform Gate and the final architecture sync pass.

Stale items:
- None.

Notes for future prompts:
- Use `arch.phase3-api-ipc-event-contracts.v1` together with the accepted P3.1-P3.3 architecture packs as the API/event baseline for Platform Gate, release contracts, and later service/package boundary planning.

#### CF-0029 | 2026-04-11 | Source: P3.5 — Platform Gate spec + exit audit

New information:
- `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` now defines the accepted internal Platform Gate, including required primitives, forced package/service areas, exit tests, audit checklist, and blocking failure classes.
- Artifact `arch.phase3-platform-gate-spec.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 3 now has an explicit hard pre-R1 gate proving frozen context, source tracing, run identity, provenance continuity, governance, typed boundaries, and scope enforcement before public release work.
- The program now has one concrete checklist for deciding whether the substrate is real enough to leave internal hardening and enter release-contract work.

Status changes:
- P3.5 marked done.
- The completion snapshot now records the Phase 3 Platform Gate spec and exit audit as accepted.
- Phase 3 remains in progress pending the final architecture synchronization pass.

Stale items:
- None.

Notes for future prompts:
- Use `arch.phase3-platform-gate-spec.v1` together with the accepted P3.1-P3.4 packs as the blocking pre-R1 baseline for P3.6 sync review, Phase 4 release contracts, and later repo/package concretization.

#### CF-0030 | 2026-04-11 | Source: P4.1 — Release-to-SDK maturity matrix

New information:
- `docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md` now defines the accepted cross-stage matrix mapping Platform Gate and R1-R7 to forced SDK/package maturity floors.
- Artifact `rel.chat-native-maturity-matrix.v1` is registered in the control-plane registry and dependency graph as `accepted`.

Impact:
- Phase 4 now has an explicit package-maturity baseline telling later release packs which substrate seams each stage forces to harden.
- The program now has one release-doctrine matrix that keeps Platform Gate, R4, and R7 bridge stages from hand-waving package maturity.

Status changes:
- P4.1 marked done.
- The completion snapshot now records the Phase 4 release-to-SDK maturity matrix as accepted.
- Phase 4 marked in progress.

Stale items:
- None.

Notes for future prompts:
- Use `rel.chat-native-maturity-matrix.v1` together with `arch.phase3-platform-gate-spec.v1`, `sem.phase2-chat-native-semantic-packs.v1`, and `canon.phase1-surface-release-topology.v1` as the release-maturity baseline for the human-only milestone architecture plan and the later R1-R7 contract packs.

#### CF-0031 | 2026-04-11 | Source: P3.6 — Architecture synchronization pass

New information:
- `docs/control-plane/architecture/phase-3-architecture-synchronization-pass.md` is now accepted for downstream use.
- Artifact `arch.phase3-architecture-sync-pass.v1` has been registered as `accepted`.
- The accepted sync pass records that no accepted Phase 3 artifact is stale at acceptance time and that the Phase 3 architecture stack remains aligned with the seam map, scenario corpus, projection grammar, forbidden shortcuts, Platform Gate, and accepted P4.1 maturity matrix.

Impact:
- Phase 3 is now complete.
- P4.2 and later Phase 4 release-contract work can inherit the accepted Phase 3 architecture stack without reopening bridge-stage locks or substrate-baseline questions.
- Later stale review can use `arch.phase3-architecture-sync-pass.v1` as the accepted sync baseline rather than a draft support note.

Status changes:
- P3.6 marked done.
- The completion snapshot now records the Phase 3 architecture synchronization pass as accepted.
- Phase 3 marked done.

Stale items:
- None.

Notes for future prompts:
- Use `arch.phase3-architecture-sync-pass.v1` together with the accepted P3.1-P3.5 artifacts and `rel.chat-native-maturity-matrix.v1` as the final accepted Phase 3 architecture-alignment lock for Phase 4 release work and later package planning.

#### CF-0032 | 2026-04-11 | Source: P4.2 — Release / milestone architecture plan

New information:
- `docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md` is now accepted for downstream use.
- Artifact `rel.chat-native-milestone-architecture-plan.v1` has been registered as `accepted`.
- The accepted milestone plan now fixes what Platform Gate and R1-R7 intentionally expose, defer, and refuse to overbuild, and it records the downstream contract-pack handoff constraints for P4.3-P4.9.

Impact:
- Phase 4 now has one accepted milestone architecture story distinct from implementation blueprints.
- P4.3 can proceed on an accepted R1 boundary instead of a review-ready milestone draft.
- Later release packs can narrow stage contracts without reopening stage ordering, bridge-stage ownership, or package-floor inheritance.

Status changes:
- P4.2 marked done.
- The completion snapshot now records the Phase 4 release / milestone architecture plan as accepted.
- Phase 4 remains in progress pending P4.3-P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.chat-native-milestone-architecture-plan.v1` together with `rel.chat-native-maturity-matrix.v1`, `arch.phase3-platform-gate-spec.v1`, and the accepted Phase 1 topology/seam/scenario artifacts as the milestone-architecture baseline for the R1-R7 contract packs.

#### CF-0033 | 2026-04-11 | Source: P4.3 — R1 Transcript Chat contract pack

New information:
- `docs/control-plane/releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r1-transcript-chat-contract.v1` has been registered as `accepted`.
- The accepted R1 contract now fixes the first public release promise, the shared primitives and chat-only additions it may expose, the package-maturity floor it inherits, the exit criteria it must satisfy, and the explicit R1 non-goals it must refuse.

Impact:
- Phase 4 now has its first stage-specific release contract pack after the milestone architecture plan.
- P4.4 can proceed on an accepted R1 boundary instead of inferring what Transcript Chat must preserve before explicit context control begins.
- Later release packs can treat R1 as the proof that familiar chat already runs on bounded runs, frozen context, and source grounding rather than on transcript-truth shortcuts.

Status changes:
- P4.3 marked done.
- The completion snapshot now records the Phase 4 R1 Transcript Chat contract pack as accepted.
- Phase 4 remains in progress pending P4.4-P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r1-transcript-chat-contract.v1` together with `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, `arch.phase3-platform-gate-spec.v1`, and `sem.phase2-chat-native-semantic-packs.v1` as the accepted R1 contract baseline for P4.4 and later release-pack work.

#### CF-0034 | 2026-04-11 | Source: P4.4 — R2 Context Chat contract pack

New information:
- `docs/control-plane/releases/r2-context-chat-contract/phase-4-r2-context-chat-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r2-context-chat-contract.v1` has been registered as `accepted`.
- The accepted R2 contract now fixes what real context control means: explicit Evidence Pack and Context Pack inspection, visible memory/canon injection, pack operations, the inherited package-floor raises, and the explicit non-goals that prevent context theater or hidden memory behavior.

Impact:
- Phase 4 now has accepted contracts for both R1 and R2.
- P4.5 can proceed on an accepted context-control boundary instead of inferring whether pack freeze, diff, and replay-basis semantics are already real before branch UX appears.
- Later release packs can treat R2 as the proof that context control is a shared-substrate capability rather than a transcript sidebar illusion.

Status changes:
- P4.4 marked done.
- The completion snapshot now records the Phase 4 R2 Context Chat contract pack as accepted.
- Phase 4 remains in progress pending P4.5-P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r2-context-chat-contract.v1` together with `rel.r1-transcript-chat-contract.v1`, `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, and `arch.phase3-context-compiler-topology.v1` as the accepted R2 contract baseline for P4.5 and later release-pack work.

#### CF-0035 | 2026-04-11 | Source: Repo-wide control-plane sync audit

New information:
- A repo-wide control-plane consistency check found two missing `depends_on` edges in `docs/control-plane/dependency-graph.seed.json` for existing accepted dataset artifacts:
  - `cp.artifact-registry-data.v1 -> cp.artifact-control-plane-spec.v1`
  - `cp.dependency-graph-data.v1 -> cp.artifact-control-plane-spec.v1`
- The dependency graph has been corrected so the graph now matches the accepted registry dependency refs for those artifacts.

Impact:
- Repo-wide registry/graph consistency validation now passes without the previously discovered mismatch.
- No accepted product, architecture, or release-contract meaning changed; this was a control-plane dataset integrity correction.

Status changes:
- No phase or packet status markers changed.

Stale items:
- None.

Notes for future prompts:
- Treat the current `cp.artifact-registry-data.v1` and `cp.dependency-graph-data.v1` pair as structurally aligned after the repo-wide sync correction.


#### CF-0036 | 2026-04-11 | Source: P4.5 — R3 Branch / Visual Thinker contract pack

New information:
- `docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r3-branch-visual-thinker-contract.v1` has been registered as `accepted`.
- The accepted R3 contract now fixes what semantic branching means: checkpoint-based branch identity, replay and compare over frozen pack lineage, mode projections over shared branch state, explicit off-chain return/merge behavior, the inherited package-floor raises, and the explicit non-goals that prevent transcript-clone or mode-private backend drift.

Impact:
- Phase 4 now has accepted contracts for R1 through R3.
- P4.6 can proceed on an accepted branch/replay boundary instead of inferring whether checkpoints, replay lineage, proof/delta compare surfaces, and proposal-bearing branch returns are already real before artifact-centered continuity becomes primary.
- Later release packs can treat R3 as the proof that semantic branching is a shared-substrate capability rather than transcript duplication with a branch map skin.

Status changes:
- P4.5 marked done.
- The completion snapshot now records the Phase 4 R3 Branch / Visual Thinker contract pack as accepted.
- Phase 4 remains in progress pending P4.6-P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r3-branch-visual-thinker-contract.v1` together with `rel.r2-context-chat-contract.v1`, `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, and `arch.phase3-api-ipc-event-contracts.v1` as the accepted R3 contract baseline for P4.6 and later release-pack work.


#### CF-0037 | 2026-04-11 | Source: P4.6 — R4 Artifact Workspace contract pack

New information:
- `docs/control-plane/releases/r4-artifact-workspace-contract/phase-4-r4-artifact-workspace-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r4-artifact-workspace-contract.v1` has been registered as `accepted`.
- The accepted R4 contract now fixes what artifact-centered continuity means: focal-artifact runs remain run-native, model outputs become explicit proposals with review and lane-local writeback behavior, historical truth stays frozen per run, and alternatives or objections remain first-class artifacts instead of comments or silent overwrites.

Impact:
- Phase 4 now has accepted contracts for R1 through R4.
- P4.7 can proceed on an accepted artifact-governance boundary instead of inferring whether proposal inbox behavior, historical truth per run, artifact lineage, and lane-local review/writeback semantics are already real before prompt assets appear.
- Later release packs can treat R4 as the bridge out of transcript gravity and the proof that durable mutation remains proposal-first and explicitly governed.

Status changes:
- P4.6 marked done.
- The completion snapshot now records the Phase 4 R4 Artifact Workspace contract pack as accepted.
- Phase 4 remains in progress pending P4.7-P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r4-artifact-workspace-contract.v1` together with `rel.r3-branch-visual-thinker-contract.v1`, `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, and `arch.phase3-data-storage-provenance-spec.v1` as the accepted R4 contract baseline for P4.7 and later release-pack work.


#### CF-0038 | 2026-04-11 | Source: P4.7 — R5 Prompt Studio contract pack

New information:
- `docs/control-plane/releases/r5-prompt-studio-contract/phase-4-r5-prompt-studio-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r5-prompt-studio-contract.v1` has been registered as `accepted`.
- The accepted R5 contract now fixes what governed prompt assets mean: canonical prompts and model-specific adaptations remain artifact-level derivatives with explicit model-profile/output-target lineage, staleness stays inspectable, and prompt assets can feed later runs without replacing reusable execution identity or hiding provider behavior as lore.

Impact:
- Phase 4 now has accepted contracts for R1 through R5.
- P4.8 can proceed on an accepted prompt-asset boundary instead of inferring whether model-profile behavior, adaptation lineage, staleness handling, and governed prompt reuse are already real before Protocol/Applet packaging appears.
- Later release packs can treat R5 as the proof that provider abstraction and prompt adaptation are governed substrate rather than hidden prompt-state conventions.

Status changes:
- P4.7 marked done.
- The completion snapshot now records the Phase 4 R5 Prompt Studio contract pack as accepted.
- Phase 4 remains in progress pending P4.8-P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r5-prompt-studio-contract.v1` together with `rel.r4-artifact-workspace-contract.v1`, `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, and `arch.phase3-api-ipc-event-contracts.v1` as the accepted R5 contract baseline for P4.8 and later release-pack work.


#### CF-0039 | 2026-04-11 | Source: P4.8 — R6 Governed Agent / Applet Chat contract pack

New information:
- `docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r6-governed-agent-applet-chat-contract.v1` has been registered as `accepted`.
- The accepted R6 contract now fixes governed reusable execution as Protocol, Workflow, Trigger, and Applet packaging over the accepted run model; background runs emit the same Run, Proof Bundle, State Delta, and Writeback Proposal objects as interactive work, and queue/inbox governance plus typed tool execution remain explicit.

Impact:
- Phase 4 now has accepted contracts for R1 through R6.
- P4.9 can proceed on an accepted governed-reuse boundary instead of inferring whether protocol/applet packaging, background-run governance, authority limits, and tool-execution gates are already real before explicit Commission/Contract semantics appear.
- Later release packs can treat R6 as the proof that bounded autonomy is governed substrate rather than agent theater or a second execution ontology.

Status changes:
- P4.8 marked done.
- The completion snapshot now records the Phase 4 R6 Governed Agent / Applet Chat contract pack as accepted.
- Phase 4 remains in progress pending P4.9.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r6-governed-agent-applet-chat-contract.v1` together with `rel.r5-prompt-studio-contract.v1`, `reuse.phase2-governance-authority-writeback-invariants.v1`, `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, and `arch.phase3-api-ipc-event-contracts.v1` as the accepted R6 contract baseline for P4.9 and later release-pack work.


#### CF-0040 | 2026-04-11 | Source: P4.9 — R7 Commissioning Bridge contract pack

New information:
- `docs/control-plane/releases/r7-commissioning-bridge-contract/phase-4-r7-commissioning-bridge-contract-pack.md` is now accepted for downstream use.
- Artifact `rel.r7-commissioning-bridge-contract.v1` has been registered as `accepted`.
- The accepted R7 contract now fixes explicit commissioning inside chat: Commission and Contract preflight, explicit Authority Scope, live monitoring, proof ledger, delta inspection, lane-by-lane writeback review, and chat-to-run handoff that preserves shared IDs into Task Studio.

Impact:
- Phase 4 now has accepted contracts for R1 through R7.
- Phase 5 can proceed on an accepted commissioning and handoff boundary instead of inferring whether explicit Commission/Contract semantics, scoped preflight, and Task Studio-safe continuity are already real.
- Later packets can treat R7 as the proof that Task Studio is a projection change over commissioned-work semantics rather than an ontology rewrite.

Status changes:
- P4.9 marked done.
- The completion snapshot now records the Phase 4 R7 Commissioning Bridge contract pack as accepted.
- Phase 5 is now the next active packet set.

Stale items:
- None.

Notes for future prompts:
- Use `rel.r7-commissioning-bridge-contract.v1` together with `rel.r6-governed-agent-applet-chat-contract.v1`, `reuse.phase2-governance-authority-writeback-invariants.v1`, `reuse.phase2-proof-validation-invariants.v1`, `rel.chat-native-milestone-architecture-plan.v1`, `rel.chat-native-maturity-matrix.v1`, `arch.phase3-api-ipc-event-contracts.v1`, and `sa.task-studio-north-star.v1` as the accepted R7 contract baseline for P5.1, P5.2, P5.5, and P5.7.


#### CF-0041 | 2026-04-11 | Source: P5.1 — Full governance / authority / writeback spec

New information:
- `docs/control-plane/reuse/phase-5-full-governance-authority-and-writeback-spec.md` is now accepted for downstream use.
- Artifact `reuse.phase5-governance-authority-writeback-spec.v1` has been registered as `accepted`.
- The accepted Phase 5 governance spec now makes policy composition, authority admission, approval routing, side-effect preview, scope-aware writeback, partial acceptance, and rollback/compensation machine-usable while preserving the accepted R7 commissioning and handoff boundary.

Impact:
- Phase 5 now has an accepted machine-usable governance baseline instead of only the Phase 2 invariant layer.
- P5.3, P5.4, P5.5, and P5.7 can build on explicit routing, preview, compensation, and append-only governance rules instead of inferring them from R7 release-contract language.
- Later work can treat governance continuity into Task Studio as an operational substrate, not a conceptual promise.

Status changes:
- P5.1 marked done.
- The completion snapshot now records the Phase 5 full governance, authority, and writeback spec as accepted.
- Phase 5 is in progress pending P5.2-P5.7.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase5-governance-authority-writeback-spec.v1` together with `rel.r7-commissioning-bridge-contract.v1`, `rel.r6-governed-agent-applet-chat-contract.v1`, `reuse.phase2-governance-authority-writeback-invariants.v1`, `reuse.phase2-proof-validation-invariants.v1`, `sem.phase2-core-object-state-machines.v1`, `sem.phase2-run-class-taxonomy-protocol-kernel.v1`, `sem.phase2-projection-grammar-contracts.v1`, and `arch.phase3-api-ipc-event-contracts.v1` as the governance baseline for P5.3, P5.4, P5.5, and P5.7.


#### CF-0042 | 2026-04-11 | Source: P5.2 — Full proof / validation / evaluation spec

New information:
- `docs/control-plane/reuse/phase-5-full-proof-validation-and-evaluation-spec.md` is now accepted for downstream use.
- Artifact `reuse.phase5-proof-validation-evaluation-spec.v1` has been registered as `accepted`.
- The accepted Phase 5 proof/evaluation spec now makes verifier-pack definitions, proof assembly, threshold profiles, evaluation fixtures, replay/regression suites, and task-family proof sections machine-usable while preserving accepted governance and R7 handoff boundaries.

Impact:
- Phase 5 now has an accepted full proof/evaluation baseline beyond the Phase 2 invariant layer.
- P5.3 can bind protocol packs to explicit verifier/evaluation contracts, failure mappings, and fixtures instead of relying only on proof skeletons.
- P5.4-P5.7 and Task Studio proof surfaces can project accepted evaluator, ledger, regression, and handoff semantics without redefining proof.

Status changes:
- P5.2 marked done.
- The completion snapshot now records the Phase 5 full proof, validation, and evaluation spec as accepted.
- Phase 5 remains in progress pending P5.3-P5.7.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase5-proof-validation-evaluation-spec.v1` together with `reuse.phase5-governance-authority-writeback-spec.v1`, `rel.r7-commissioning-bridge-contract.v1`, `rel.r6-governed-agent-applet-chat-contract.v1`, `reuse.phase2-proof-validation-invariants.v1`, `sem.phase2-run-class-taxonomy-protocol-kernel.v1`, `sem.phase2-projection-grammar-contracts.v1`, `arch.phase3-context-compiler-topology.v1`, `arch.phase3-api-ipc-event-contracts.v1`, and `arch.phase3-platform-gate-spec.v1` as the proof/evaluation baseline for P5.3-P5.7.


#### CF-0043 | 2026-04-11 | Source: P5.3 — Full run-class protocol packs

New information:
- `docs/control-plane/reuse/phase-5-full-run-class-protocol-packs.md` is now accepted for downstream use.
- Artifact `reuse.phase5-run-class-protocol-packs.v1` has been registered as `accepted`.
- The accepted Phase 5 protocol pack now makes versioned run-class schemas, Context Recipe and Strategy Preset bindings, verifier pack links, authority/writeback defaults, failure mappings, and fixture sets machine-usable across all seven base run classes.

Impact:
- Phase 5 now has an accepted operational protocol baseline on top of the accepted taxonomy, governance, and proof layers.
- P5.4 can compose Workflow / Trigger / Applet / Pack / Integration specs from accepted protocol-pack refs instead of inventing a separate reusable-execution model.
- P5.5-P5.7 and Task Studio can project protocol IDs/versions, verifier and fixture expectations, and review-hook/writeback posture without redefining run-class meaning.

Status changes:
- P5.3 marked done.
- The completion snapshot now records the Phase 5 full run-class protocol packs as accepted.
- Phase 5 remains in progress pending P5.4-P5.7.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase5-run-class-protocol-packs.v1` together with `reuse.phase5-governance-authority-writeback-spec.v1`, `reuse.phase5-proof-validation-evaluation-spec.v1`, `sem.phase2-run-class-taxonomy-protocol-kernel.v1`, `rel.r6-governed-agent-applet-chat-contract.v1`, `rel.r7-commissioning-bridge-contract.v1`, `reuse.phase2-governance-authority-writeback-invariants.v1`, `reuse.phase2-proof-validation-invariants.v1`, `arch.phase3-context-compiler-topology.v1`, and `arch.phase3-api-ipc-event-contracts.v1` as the protocol baseline for P5.4-P5.7.


#### CF-0044 | 2026-04-11 | Source: P5.4 — Workflow / Trigger / Applet / Pack / Integration Binding specs

New information:
- `docs/control-plane/reuse/phase-5-workflow-trigger-applet-pack-and-integration-binding-specs.md` is now accepted for downstream use.
- Artifact `reuse.phase5-workflow-trigger-applet-pack-integration-binding-specs.v1` has been registered as `accepted`.
- The accepted Phase 5 composition pack now makes workflow stages, trigger enablement, applet pinning, pack lifecycle, and scoped integration-binding rules machine-usable without inventing a second reusable-execution ontology.

Impact:
- Phase 5 now has an accepted reusable-execution composition baseline on top of the accepted protocol, governance, and proof layers.
- P5.5 can specify Task Studio surfaces and lifecycle stages against exact workflow/applet/trigger/pack/binding objects instead of app-local execution lore.
- P5.6-P5.7 can narrow V1 exposure and handoff behavior while preserving exact version pinning, scoped binding, and background-parity continuity.

Status changes:
- P5.4 marked done.
- The completion snapshot now records the Phase 5 Workflow / Trigger / Applet / Pack / Integration Binding specs as accepted.
- Phase 5 remains in progress pending P5.5-P5.7.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase5-workflow-trigger-applet-pack-integration-binding-specs.v1` together with `reuse.phase5-run-class-protocol-packs.v1`, `reuse.phase5-governance-authority-writeback-spec.v1`, `reuse.phase5-proof-validation-evaluation-spec.v1`, `rel.r6-governed-agent-applet-chat-contract.v1`, `rel.r7-commissioning-bridge-contract.v1`, `sem.phase2-projection-grammar-contracts.v1`, `arch.phase3-context-compiler-topology.v1`, and `arch.phase3-api-ipc-event-contracts.v1` as the reusable-execution composition baseline for P5.5-P5.7.


#### CF-0045 | 2026-04-11 | Source: P5.5 — Task Studio surface and lifecycle contract pack

New information:
- `docs/control-plane/reuse/phase-5-task-studio-surface-and-lifecycle-contract-pack.md` is now accepted for downstream use.
- Artifact `reuse.phase5-task-studio-surface-lifecycle-contract-pack.v1` has been registered as `accepted`.
- The accepted Phase 5 Task Studio pack now makes named surfaces, lifecycle stages, layout rules, and progressive-disclosure behavior machine-usable while preserving shared IDs, reusable-execution lineage, and lane-separated governance semantics.

Impact:
- Phase 5 now has an accepted Task Studio app-model baseline on top of the accepted R7 handoff, governance, proof, protocol, and reusable-execution composition layers.
- P5.6 can narrow V1 scope and exposure choices against an explicit Task Studio lifecycle and surface contract instead of relying on future-only intent.
- P5.7 and later surface-contract work can preserve exact handoff continuity and grammar mapping without inventing app-private state machines.

Status changes:
- P5.5 marked done.
- The completion snapshot now records the Phase 5 Task Studio surface and lifecycle contract pack as accepted.
- Phase 5 remains in progress pending P5.6-P5.7.

Stale items:
- None.

Notes for future prompts:
- Use `reuse.phase5-task-studio-surface-lifecycle-contract-pack.v1` together with `reuse.phase5-workflow-trigger-applet-pack-integration-binding-specs.v1`, `reuse.phase5-run-class-protocol-packs.v1`, `reuse.phase5-governance-authority-writeback-spec.v1`, `reuse.phase5-proof-validation-evaluation-spec.v1`, `rel.r7-commissioning-bridge-contract.v1`, `sem.phase2-projection-grammar-contracts.v1`, `canon.phase1-source-decomposition.v1`, and `sa.task-studio-north-star.v1` as the Task Studio app-model baseline for P5.6, P5.7, and P6.1.

---

## 10. End state this plan is aiming at

If the plan is followed correctly, the result should be:

- one stable product truth,
- one stable shared substrate below all app projections,
- one fixed chat-native release path that hardens the SDKs in public,
- one clean handoff from R7 into Task Studio without ontology rewrite,
- one repo/package/execution system that lets Factory handle bounded implementation work safely,
- one operating model where every accepted change carries forward its impact instead of silently breaking downstream work.

That is the target state.

#### CF-0046 | 2026-04-11 | Source: P5.6 — Task Studio V1 scope pack

New information:
- A review-ready P5.6 support pack now exists at `docs/control-plane/reuse/phase-5-task-studio-v1-scope-pack.md`.
- Artifact `reuse.phase5-task-studio-v1-scope-pack.v1` is registered in the control-plane registry and dependency graph as `review_ready`.
- The pack narrows V1 to the accepted seven task families, stage-centered named surfaces, governable result/proof/delta floors, artifact-lane-first persistence, and conservative onboarding/reusable-execution exposure constraints without reopening accepted semantics.

Impact:
- P5.6 now has a concrete review-ready scope basis for human approval instead of re-deriving V1 boundaries from P5.5 and R7.
- P5.7 and P6.1 can draft against an explicit V1 exposure floor while preserving the human-owned acceptance boundary.

Status changes:
- P5.6 remains pending in the master plan, with validated review-ready deliverables present and human acceptance still pending.
- Phase 5 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Treat `reuse.phase5-task-studio-v1-scope-pack.v1` as the review-ready V1 exposure and non-goal basis for task-family vocabulary, primary-vs-companion surface exposure, artifact-lane-first persistence, and onboarding/category-teaching constraints.
- Do not treat it as accepted until a human explicitly approves it; preserve the rule that V1 narrows exposure/defaults only and does not redefine lifecycle, task-family mapping, proof, governance, or handoff meaning.

#### CF-0047 | 2026-04-11 | Source: P5.7 — Commissioning Bridge -> Task Studio handoff contract

New information:
- A review-ready P5.7 support pack now exists at `docs/control-plane/reuse/phase-5-commissioning-bridge-to-task-studio-handoff-contract.md`.
- Artifact `reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1` is registered in the control-plane registry and dependency graph as `review_ready`.
- The pack maps the accepted R7 commissioning payload, `Acceptance Stack`, and `Chat-to-Run Handoff` onto Task Studio surfaces, lifecycle landings, proof/delta/writeback continuity, and reusable-execution lineage without ontology translation.

Impact:
- P5.7 now has a concrete review-ready handoff basis for human approval instead of re-deriving exact surface mappings from R7 and P5.5.
- P6.1 can treat the R7 -> Task Studio projection and lifecycle landing matrix as explicit while preserving the human-owned acceptance boundary.

Status changes:
- P5.7 remains pending in the master plan, with validated review-ready deliverables present and human acceptance still pending.
- Phase 5 remains in progress pending human acceptance of P5.6-P5.7.

Stale items:
- None.

Notes for future prompts:
- Treat `reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1` together with `reuse.phase5-task-studio-v1-scope-pack.v1` as the review-ready R7 -> Task Studio projection baseline for exact payload preservation, `Acceptance Stack` decomposition, default landings, and reusable-execution continuity.
- Do not treat it as accepted until a human explicitly approves it; preserve the rule that Task Studio is a projection change, not a semantic translation or rewrite destination.

#### CF-0048 | 2026-04-11 | Source: P6.1 — Surface contract packs

New information:
- Accepted surface-contract packs now exist at `docs/control-plane/surfaces/phase-6-shared-projection-grammar-surface-contract-pack.md`, `docs/control-plane/surfaces/phase-6-chat-native-surface-contract-pack.md`, and `docs/control-plane/surfaces/phase-6-later-domain-surface-backlog-contract-pack.md`.
- A review-ready Task Studio surface contract pack now exists at `docs/control-plane/surfaces/phase-6-task-studio-surface-contract-pack.md`.
- Artifacts `surf.phase6-shared-projection-grammar-surface-contract-pack.v1`, `surf.phase6-chat-native-surface-contract-pack.v1`, and `surf.phase6-later-domain-surface-backlog-contract-pack.v1` are registered as `accepted`, while `surf.phase6-task-studio-surface-contract-pack.v1` is registered as `review_ready` pending human acceptance of P5.6/P5.7.

Impact:
- Phase 6 now has an accepted shared grammar surface baseline, an accepted chat-native surface-contract baseline, and an accepted later-domain backlog boundary pack instead of leaving surface contracts implicit.
- P6.1 now has a concrete review-ready Task Studio route-contract pack that can be promoted after human acceptance of the review-ready P5.6/P5.7 support packs.
- Later route/module work can plan against explicit surface contracts without inventing new grammar families or app-private handoff state.

Status changes:
- P6.1 remains pending in the master plan, with validated surface-contract packs present and the Task Studio pack awaiting upstream human acceptance.
- Phase 6 marked in progress.

Stale items:
- None.

Notes for future prompts:
- Treat `surf.phase6-shared-projection-grammar-surface-contract-pack.v1`, `surf.phase6-chat-native-surface-contract-pack.v1`, and `surf.phase6-later-domain-surface-backlog-contract-pack.v1` as the accepted Phase 6 surface-contract baseline.
- Treat `surf.phase6-task-studio-surface-contract-pack.v1` as review-ready only until `reuse.phase5-task-studio-v1-scope-pack.v1` and `reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1` are human-accepted.
- Keep `P6.1` out of repo/package/module architecture detail; that belongs to `P6.2`.

#### CF-0049 | 2026-04-12 | Source: P5.6 — Human acceptance and landing

New information:
- `docs/control-plane/reuse/phase-5-task-studio-v1-scope-pack.md` is now accepted for downstream use.
- Artifact `reuse.phase5-task-studio-v1-scope-pack.v1` has been promoted from `review_ready` to `accepted`.

Impact:
- P5.7, P6.1, and later route/module work now have an accepted V1 exposure baseline instead of a review-ready support note.
- V1 family scope, surface exposure, artifact-lane-first persistence posture, and onboarding constraints are now fixed for downstream use.

Status changes:
- P5.6 marked done.
- The completion snapshot now records the Phase 5 Task Studio V1 scope pack as accepted.

Stale items:
- None.

Notes for future prompts:
- Treat `reuse.phase5-task-studio-v1-scope-pack.v1` as the accepted V1 scope baseline for Task Studio family exposure, primary-vs-companion surface emphasis, persistence posture, and onboarding/category-teaching constraints.
- Downstream work may narrow presentation, but it may not reopen the accepted V1 scope decisions without a new accepted delta.

#### CF-0050 | 2026-04-12 | Source: P5.7 — Human acceptance and landing

New information:
- `docs/control-plane/reuse/phase-5-commissioning-bridge-to-task-studio-handoff-contract.md` is now accepted for downstream use.
- Artifact `reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1` has been promoted from `review_ready` to `accepted`.

Impact:
- Phase 5 now has an accepted R7 -> Task Studio handoff baseline instead of a review-ready support note.
- P6.1 and P6.2 can rely on exact payload preservation, `Acceptance Stack` decomposition, and lifecycle landing continuity without re-deriving them from R7 and P5.5.

Status changes:
- P5.7 marked done.
- The completion snapshot now records the Phase 5 Commissioning Bridge -> Task Studio handoff contract as accepted.
- Phase 5 marked done.

Stale items:
- None.

Notes for future prompts:
- Treat `reuse.phase5-commissioning-bridge-task-studio-handoff-contract.v1` together with `reuse.phase5-task-studio-v1-scope-pack.v1` as the accepted R7 -> Task Studio projection baseline for exact payload preservation, default landings, and reusable-execution continuity.
- Downstream work may not reinterpret the handoff as export/import, app-local metadata, or ontology translation.

#### CF-0051 | 2026-04-12 | Source: P6.1 — Task Studio surface contract acceptance

New information:
- `docs/control-plane/surfaces/phase-6-task-studio-surface-contract-pack.md` is now accepted for downstream use.
- Artifact `surf.phase6-task-studio-surface-contract-pack.v1` has been promoted from `review_ready` to `accepted`.
- All four P6.1 surface-contract packs are now accepted.

Impact:
- P6.2 can plan repo/package architecture against fully accepted shared grammar, chat-native, Task Studio, and later-domain surface contracts.
- Later route/module work no longer needs a provisional Task Studio surface-contract layer.

Status changes:
- P6.1 marked done.
- The completion snapshot now records the Phase 6 surface contract packs as accepted.
- Phase 6 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Treat `surf.phase6-task-studio-surface-contract-pack.v1` together with the other accepted `surf.phase6-*` artifacts as the accepted Phase 6 surface-contract baseline.
- If accepted V1 scope or handoff semantics change later, mark the Task Studio surface contract pack stale and regenerate it rather than patching around drift.

#### CF-0052 | 2026-04-12 | Source: P6.2 — Repo/package architecture and agent execution rules

New information:
- `docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md` now defines the accepted Phase 6 repo/package architecture and agent execution baseline.
- Artifact `surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1` is registered in the control-plane registry and dependency graph as `accepted`.
- The pack maps accepted runtime planes and logical package seams onto concrete repo roots, workspace families, module-boundary rules, and additive agent execution discipline without letting repo shape dictate platform meaning.

Impact:
- `P6.3` now has an accepted workspace/root and module-boundary baseline for documentation-plane, manifests, and generated current-state work.
- `P6.4` through `P6.6` can benchmark, blueprint, and packetize work against one accepted repo/package and agent-execution system instead of inventing task-local layout or execution rules.
- Later implementation work now has explicit first-party app roots, shared package families, service/worker roots, reserved later-domain roots, and preserved no-direct-UI-to-worker / no-second-stack constraints.

Status changes:
- P6.2 marked done.
- The completion snapshot now records the repo/package architecture and agent execution system as implemented.
- Phase 6 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Treat `surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1` as the accepted package-map and execution baseline for `apps/`, `packages/`, `services/`, `workers/`, `domains/`, `tests/`, and `scripts/` roots.
- Preserve the rule that repo layout follows accepted architecture, release, and handoff truth; do not use file placement to re-own shared objects or to create direct UI-to-worker execution paths.
- Keep later implementation-facing work additive to accepted P0.2/P0.3 execution rules and do not import P0.5-only packet-budget policy into package or automation semantics.

#### CF-0053 | 2026-04-12 | Source: P6.3 — Agent-oriented codebase pattern and documentation plane

New information:
- `docs/control-plane/surfaces/phase-6-agent-oriented-codebase-pattern-and-documentation-plane-pack.md` now defines the accepted Phase 6 documentation-plane and agent-navigation baseline over the accepted repo/package map.
- Artifacts `surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1`, `cp.phase6-workspace-manifest-index-data.v1`, `cp.phase6-codebase-current-state-data.v1`, `cp.phase6-module-test-contracts-data.v1`, `cp.phase6-fixture-rules-data.v1`, and `cp.phase6-agent-packet-context-pack-rules-data.v1` are registered in the control-plane registry and dependency graph as `accepted`.
- `tests/contracts/module-boundary.contracts.json` and `tests/fixtures/fixture-rules.json` now materialize the `tests/` root as accepted contract/fixture assets, while `apps/`, `packages/`, `services/`, `workers/`, `domains/`, and `scripts/` remain reserved in the generated current-state view.

Impact:
- `P6.4` can compile pilot packets, benchmark inputs, and internal execution support against accepted manifests, current-state data, module-boundary contracts, and packet context-pack rules instead of rediscovering repo scope.
- `P6.5` and `P6.6` can map release blueprints and execution packets to accepted workspace families, validation roots, fixture policies, and bounded context-compilation guidance.
- Agents now have one accepted documentation-plane layer for navigating current repo posture without turning derived current-state data into new architecture truth.

Status changes:
- P6.3 marked done.
- The completion snapshot now records the repo/package architecture, documentation plane, and agent execution system as implemented.
- Phase 6 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Use `cp.phase6-workspace-manifest-index-data.v1` and `cp.phase6-codebase-current-state-data.v1` together as the accepted repo-navigation baseline for later implementation-facing work.
- Use `cp.phase6-module-test-contracts-data.v1` and `cp.phase6-fixture-rules-data.v1` when blueprinting or packetizing module, validation, replay, or benchmark work.
- Compile later bounded packet context from accepted manifests/current-state plus accepted P0.5 packet-budget rules; do not reinterpret runtime context-compiler topology as a packet-only invention.

#### CF-0054 | 2026-04-12 | Source: P6.4 — Pilot packet set + Factory benchmark harness + internal skills/adapters

New information:
- `docs/control-plane/core/phase-6-factory-benchmark-harness.md` now defines the accepted dry-run benchmark contract for the first-wave pilot packet set.
- Artifacts `cp.phase6-factory-benchmark-harness.v1`, `cp.factory-pilot-packet-authoring-skill.v1`, `cp.factory-benchmark-harness-skill.v1`, `cp.phase6-pilot-benchmark-matrix-data.v1`, `cp.phase6-pilot-benchmark-results-data.v1`, `cp.phase6-pilot-packet-tuning-notes.v1`, `pkt.phase6-pilot-plan-release-blueprint-packet.v1`, `pkt.phase6-pilot-audit-doc-plane-consistency-packet.v1`, and `pkt.phase6-pilot-transform-factory-skill-harness-packet.v1` are registered in the control-plane registry and dependency graph as `accepted`.
- `docs/control-plane/implementation/packets/`, `.factory/skills/`, `scripts/validators/`, `scripts/wrappers/`, and `tests/benchmark-datasets/` now materialize the accepted pilot-packet, benchmark, and additive Factory-execution support lane.
- The frozen benchmark results record all three first-wave pilot packets passing the dry-run structural harness, and the tuning notes lock in the initial budget, whitelist-root, and run-class observations.

Impact:
- `P6.5` can shape release blueprints against an accepted plan-packet archetype and a tested benchmark harness instead of inventing packet structure ad hoc.
- `P6.6` can expand bounded execution packets from accepted `plan`, `audit`, and `transform` pilot shapes, shared packet-authoring skill guidance, and frozen benchmark expectations.
- Later Factory execution work now has one accepted validator and one accepted benchmark wrapper for checking packet briefs, whitelist-root mapping, fixture bindings, and budget-band ceilings before scale-out.

Status changes:
- P6.4 marked done.
- The completion snapshot now records the pilot packet set, benchmark harness, and internal Factory skills/adapters as implemented and benchmarked.
- Phase 6 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Start from the accepted pilot packet archetypes before creating broader execution packets; split scope instead of widening the current standard-band packets by default.
- Run `scripts/validators/validate_pilot_packets.py` and `scripts/wrappers/run_phase6_benchmarks.py` when packet briefs, whitelist roots, fixture bindings, or packet-context rules change.
- Keep transform-style packet writes additive to `.factory/`, `scripts/`, `docs/control-plane/`, and other explicitly accepted roots unless a new packet family is accepted.

#### CF-0055 | 2026-04-12 | Source: P6.5 — Release implementation blueprints

New information:
- Seven accepted release blueprints now live under `docs/control-plane/implementation/release-blueprints/`, covering `R1` conversation, `R2` context control, `R3` branch replay, `R4` artifact workspace, `R5` prompt assets, `R6` governed reusable execution, and `R7` commissioning bridge.
- Artifact `cp.phase6-release-blueprint-index-data.v1` now freezes the machine-readable release-blueprint index, while artifacts `bp.phase6-r1-conversation-blueprint.v1` through `bp.phase6-r7-commissioning-bridge-blueprint.v1` are registered in the control-plane registry and dependency graph as `accepted`.
- `scripts/validators/validate_release_blueprints.py` now provides a thin repo-local validator for blueprint headers, required sections, workspace-root mapping, fixture-family citations, and cross-pack registry references.
- The accepted blueprints map each release to bounded app/package/service/worker/test module clusters, fixture families, validation hooks, and explicit exclusions without pretending reserved runtime roots are already implemented.

Impact:
- `P6.6` can derive bounded execution packets from one accepted per-release blueprint set plus the shared blueprint index instead of reconstructing release scope ad hoc.
- Later implementation work now has a stable release-by-release map of touched modules, shared-object seams, API/event boundaries, storage posture, UI states, test posture, and deferred work.
- The commissioning bridge blueprint now connects accepted chat-native and Task Studio route landings through preserved handoff continuity rather than a future-only narrative.

Status changes:
- P6.5 marked done.
- The completion snapshot now records the release implementation blueprints as produced and accepted.
- Phase 6 remains in progress.

Stale items:
- None.

Notes for future prompts:
- Start `P6.6` packetization from the accepted blueprint files and `cp.phase6-release-blueprint-index-data.v1` rather than re-deriving release scope from the Phase 4 packs alone.
- Run `scripts/validators/validate_release_blueprints.py` whenever blueprint sections, module clusters, fixture families, or governing refs change.
- Treat the blueprint files as bounded build guidance over reserved roots; do not interpret them as proof that runtime code or directories already exist.

#### CF-0056 | 2026-04-12 | Source: P6.6 — Agent execution packets

New information:
- Artifact `cp.phase6-execution-packet-index-data.v1` now freezes the machine-readable Phase 6 execution-packet map, and twenty-three bounded execution packets now live under `docs/control-plane/implementation/packets/` as accepted `pkt.execution_packet` artifacts.
- The accepted packet set covers `R1` through `R6` with `contracts_objects`, `runtime_execution`, and `surface_validation` packet families, while `R7` additionally splits into `chat_surface`, `task_studio_handoff`, and `test_fixtures` packets to preserve handoff-specific scope discipline.
- `scripts/validators/validate_execution_packets.py` now provides a thin repo-local validator for packet/index alignment, blueprint-subset whitelists, packet-family prefix rules, prerequisite ordering, and budget-band ceilings.
- All accepted Phase 6 packet assets validate cleanly together with the pilot packets, benchmark harness/results, release blueprints, registry, and dependency graph.

Impact:
- Phase 6 now has a complete accepted delegation layer: pilot packet archetypes, benchmark evidence, release blueprints, and bounded execution packets can all be handed to implementers without re-deriving scope.
- `P7.1` can build delta-pack and sync rules against one explicit packet inventory rather than against ad hoc packet patterns.
- The R7 packet family now preserves a separate Task Studio handoff packet, which protects shared-ID continuity and avoids collapsing chat-side commissioning scope into Task Studio landing work.

Status changes:
- P6.6 marked done.
- The completion snapshot now records the broader bounded execution packets as generated and accepted.
- Phase 6 marked done in the repo.

Stale items:
- None.

Notes for future prompts:
- Start later execution work from `cp.phase6-execution-packet-index-data.v1` and the accepted per-release packet families instead of inventing new packet breakdowns by convenience.
- Run `scripts/validators/validate_execution_packets.py` whenever packet briefs, packet-family splits, whitelist paths, prerequisite chains, or packet-budget choices change.
- Preserve the accepted family split and standard-band posture; split packets further instead of widening them, especially around R7 handoff scope.

#### CF-0057 | 2026-04-12 | Source: P7.1 — Carry-forward delta pack after every packet/release

New information:
- Artifact `sync.phase7-carry-forward-delta-pack.v1` now defines the accepted delta-pack template and operating loop that every accepted release, packet, or sync change must follow before downstream work continues.
- Artifact `cp.phase7-delta-pack-index-data.v1` now freezes the machine-readable Phase 7 delta-trigger inventory over every accepted Phase 6 release blueprint and execution packet.
- `scripts/validators/validate_control_plane_integrity.py` now provides a thin repo-local integrity check for registry/graph node, edge, status, hook, and dependency-ref alignment, while `scripts/validators/validate_phase7_sync_artifacts.py` validates sync-pack structure plus delta-index coverage.
- The documentation-plane manifest and current-state datasets now materialize `docs/control-plane/sync/` as an accepted sync/delta/stale artifact root.

Impact:
- `P7.2` can drive recurring architecture sync from one accepted delta baseline instead of recreating change scope from ad hoc packet or release lists.
- Later stale-detection and gate-recheck work can read one explicit release/packet trigger inventory and one explicit sync artifact root instead of inferring control-plane coverage from free-form docs.
- Registry and dependency-graph changes now have a reusable integrity check before downstream sync automation relies on them.

Status changes:
- P7.1 marked done.
- The completion snapshot now records the Phase 7 delta-pack operating rule and coverage index as accepted.
- Phase 7 marked in progress.

Stale items:
- None.

Notes for future prompts:
- Treat `sync.phase7-carry-forward-delta-pack.v1` and `cp.phase7-delta-pack-index-data.v1` as the default delta-capture baseline for later accepted release, packet, or sync changes.
- Run `python3 scripts/validators/validate_control_plane_integrity.py` and `python3 scripts/validators/validate_phase7_sync_artifacts.py` whenever sync artifacts, manifest/current-state sync placement, or the delta-trigger inventory changes.
- Preserve the durable pair of sync-pack update plus append-only carry-forward entry; do not collapse accepted delta capture into ad hoc commit commentary.
