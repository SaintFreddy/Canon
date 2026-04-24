# Canon Knowledgebase Layer Carry-Forward Ledger

## Purpose

This file is the machine-readable carry-forward ledger for the knowledgebase rollout.

Use it to record durable decisions, newly discovered constraints, packet outcomes, blockers, and explicit next-step unlocks that future sessions must know.

Do not use this file for narrative summaries.
Do not use this file for brainstorming.
Do not use this file for speculative ideas unless they are explicitly marked as provisional and tied to a concrete packet or blocker.

## Write Rules

1. Append new entries. Do not rewrite history unless correcting a factual mistake.
2. One durable change or decision per entry.
3. Keep `summary`, `impact`, and `next_action` to blunt operational language.
4. Always fill every required field.
5. Use stable IDs.
6. If an older entry is superseded, do not delete it. Add a new entry with `kind: supersession` and point back using `supersedes`.
7. If an entry only matters temporarily, still write it here if a future fresh session could waste time or make a wrong decision without it.

## Read Rules

Fresh sessions should:

1. read the newest entries first
2. filter first by `status: active`
3. then filter by the current `stage` and `packet`
4. then apply any `supersession` entries before acting

## Entry Schema

Every entry must use exactly this key set and order.

```yaml
- id: CF-0001
  date: 2026-04-16
  status: active
  kind: decision
  stage: pre-phase-4-convergence
  packet: P00
  topic: ownership
  summary: Shared environment owns durable memory and canon truth.
  impact: Engine work must stay at the injection seam and must not create a durable workspace memory store.
  source:
    - file:///absolute/path/or/url
  supersedes: []
  related:
    - P01
    - P04
  next_action: Use this as a hard constraint in object-model and engine-boundary packets.
```

## Allowed Values

### `status`

- `active`
- `superseded`
- `blocked`
- `done`
- `provisional`

### `kind`

- `decision`
- `constraint`
- `outcome`
- `blocker`
- `unlock`
- `supersession`
- `handoff`

### `stage`

- `pre-phase-4-convergence`
- `canonical-rewrite`
- `phase-4-execution`
- `historical`

### `packet`

- `P00`
- `P01`
- `P02`
- `P03`
- `P04`
- `P05`
- `P06`
- `P07`
- `P08`
- `P09`
- `P10`
- `P11`
- `P12`
- `P13`
- `none`

### `topic`

Use one of these when possible:

- `ownership`
- `governance`
- `storage`
- `query`
- `compiler`
- `replay`
- `passive-learning`
- `artifact-governance`
- `prompt-integration`
- `applet-policy`
- `commissioning`
- `historical-boundary`
- `process`
- `tracker`

If none fits, use a short lowercase hyphenated term.

## Query Tips

Useful manual filters:

- current active constraints for a packet: search `status: active` plus `packet: PX`
- current blockers: search `kind: blocker` plus `status: blocked`
- latest handoff facts: search `kind: handoff`
- outdated decisions: search `status: superseded`
- rewrite-stage guidance: search `stage: canonical-rewrite`

## Required Entry Triggers

Write a new entry when any of these happen:

1. a packet closes with a durable decision
2. a packet reveals a blocker that changes execution order
3. an older assumption is rejected or narrowed
4. a new read boundary becomes the standard for later packets
5. the current active packet changes
6. the canonical merge point moves or gets refined
7. Wiki or other historical materials are explicitly reclassified for a specific use
8. a future session would otherwise need chat memory to understand why a choice was made

## Anti-Patterns

Do not write entries like these:

- "Did a bunch of investigation"
- "Read many files"
- "Probably should maybe"
- "This seems important"
- long narrative paragraphs
- entries without source refs
- entries without a concrete impact on future work

## Active Ledger

```yaml
entries:
  - id: CF-0001
    date: 2026-04-16
    status: active
    kind: decision
    stage: pre-phase-4-convergence
    packet: none
    topic: ownership
    summary: Shared environment owns durable memory and canon truth; engine owns only the selection, injection, reporting, and replay-safe seam.
    impact: Object-model, storage, governance, and app projection work must stay out of the engine runtime.
    source:
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer#L7-L16
      - canon-ref:engine/docs/spec-digests/phase-2-context-chat-engine#L17-L23
      - canon-ref:engine/context#L13-L18
    supersedes: []
    related:
      - P00
      - P01
      - P04
      - P05
    next_action: Treat this as a hard constraint during pre-phase-4 convergence.

  - id: CF-0002
    date: 2026-04-16
    status: active
    kind: constraint
    stage: pre-phase-4-convergence
    packet: none
    topic: governance
    summary: Passive learning may create candidates and proposals but may not silently promote durable truth.
    impact: All learning flows must stay on the path event to proposal to review to approved object to explicit injection.
    source:
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer#L18-L22
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer#L147-L157
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
    supersedes: []
    related:
      - P03
      - P06
      - P07
      - P12
      - P13
    next_action: Enforce this in governance, event-spine, passive-capture, and applet-policy packets.

  - id: CF-0003
    date: 2026-04-16
    status: active
    kind: constraint
    stage: pre-phase-4-convergence
    packet: none
    topic: replay
    summary: Knowledge injection must stay freeze-first and replay-safe with explicit selected refs and inclusion or exclusion reasons.
    impact: Compiler and replay work cannot allow inline learning side effects or hidden mutable knowledge basis.
    source:
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer#L14-L19
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer#L92-L103
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
    supersedes: []
    related:
      - P04
      - P05
      - P09
    next_action: Keep this explicit in engine seam and compiler injection packets.

  - id: CF-0004
    date: 2026-04-16
    status: active
    kind: handoff
    stage: pre-phase-4-convergence
    packet: P00
    topic: process
    summary: The rollout plan is active only through P00 to P05; after P05 the next required move is a canonical Phase 4+ rewrite before P06 to P13 proceed.
    impact: Future sessions should not activate post-merge packets directly from the rollout plan.
    source:
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes: []
    related:
      - P05
      - P06
    next_action: Execute only convergence packets until a canonical rewrite artifact exists.

  - id: CF-0005
    date: 2026-04-16
    status: active
    kind: decision
    stage: historical
    packet: none
    topic: historical-boundary
    summary: Wiki is preserved as historical prior art and lesson record, not active architecture authority for the knowledgebase rollout.
    impact: Fresh sessions should not default to Wiki materials unless doing explicit historical comparison or contradiction review.
    source:
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P00
      - P01
      - P02
      - P03
      - P04
      - P05
    next_action: Use Wiki only when a packet explicitly needs historical comparison.

  - id: CF-0006
    date: 2026-04-16
    status: active
    kind: outcome
    stage: pre-phase-4-convergence
    packet: P00
    topic: process
    summary: P00 is now recorded in canon-knowledgebase/p00-architecture-delta.md as the durable architecture delta, release impact matrix, and forbidden-shortcuts addendum for the knowledgebase rollout.
    impact: Future sessions can use the P00 file as the single convergence baseline before object model, storage, governance, engine seam, and compiler packets.
    source:
      - canon-ref:dev/kb/p00-architecture-delta
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
    supersedes: []
    related:
      - P01
      - P02
      - P03
      - P04
      - P05
    next_action: Read canon-knowledgebase/p00-architecture-delta.md first, then execute P01 inside the shared-environment object-model boundary.

  - id: CF-0007
    date: 2026-04-16
    status: active
    kind: outcome
    stage: pre-phase-4-convergence
    packet: P01
    topic: object-model
    summary: P01 is now recorded in canon-knowledgebase/p01-shared-environment-knowledge-objects.md with separate MemoryObject and CanonObject lanes, immutable revisions, shared lifecycle states, and explicit scope and provenance requirements.
    impact: Later packets can assume one canonical shared-environment knowledge object model and no longer need to debate candidate injection, revision identity, or where supersession and challenge metadata live.
    source:
      - canon-ref:dev/kb/p01-shared-environment-knowledge-objects
      - canon-ref:dev/kb/p00-architecture-delta
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer
    supersedes: []
    related:
      - P02
      - P03
      - P04
      - P05
    next_action: Use the P01 object model as the shared-environment schema baseline, then execute P02 inside the storage and query-lane boundary.

  - id: CF-0008
    date: 2026-04-16
    status: active
    kind: outcome
    stage: pre-phase-4-convergence
    packet: P02
    topic: storage
    summary: P02 is now recorded in canon-knowledgebase/p02-storage-and-query-lanes.md with a relational-first authoritative store, append-only event spine, blob payload lane, separate secret lane, and rebuildable lexical, vector, and provenance projections.
    impact: Later packets can assume one storage/query baseline where scope admission happens before ranking, replay resolves exact revision refs from authoritative lanes, and derived indices never become Canon truth.
    source:
      - canon-ref:dev/kb/p02-storage-and-query-lanes
      - canon-ref:dev/kb/p01-shared-environment-knowledge-objects
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer
    supersedes: []
    related:
      - P03
      - P05
      - P06
    next_action: Use the P02 storage and query-lane note as the durable substrate baseline, then execute P03 within the governance and event-spine boundary.

  - id: CF-0009
    date: 2026-04-16
    status: active
    kind: outcome
    stage: pre-phase-4-convergence
    packet: P03
    topic: governance
    summary: P03 is now recorded in canon-knowledgebase/p03-governance-and-event-spine-integration.md with one proposal-first governance route, typed knowledge event families, separate approval versus application semantics, and mandatory provenance for every durable mutation.
    impact: Later packets can assume that memory and canon changes always travel through writeback proposals, reviews, approval decisions, and explicit applied state transitions, with no silent mutation path left for the shared-environment knowledgebase.
    source:
      - canon-ref:dev/kb/p03-governance-and-event-spine-integration
      - canon-ref:dev/kb/p02-storage-and-query-lanes
      - canon-ref:dev/kb/p01-shared-environment-knowledge-objects
      - canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer
    supersedes: []
    related:
      - P04
      - P05
      - P06
      - P07
    next_action: Use the P03 governance and event-spine note as the durable mutation baseline, then execute P04 inside the engine-seam boundary.

  - id: CF-0010
    date: 2026-04-16
    status: active
    kind: outcome
    stage: pre-phase-4-convergence
    packet: P04
    topic: compiler
    summary: P04 is now recorded in canon-knowledgebase/p04-engine-seam-tightening.md with a consumer-only engine seam where shared environment supplies authoritative memory and canon refs while the engine owns only injection candidates, compilation reporting, and replay-basis transport.
    impact: Later packets can assume the engine must not own durable memory or canon objects, must stop treating engine-authored MemoryObject and AcceptedKnowledgeObject shapes as the long-term host contract, and must carry host-provided candidate refs into compiler reports and frozen replay inputs.
    source:
      - canon-ref:dev/kb/p04-engine-seam-tightening
      - canon-ref:engine/packages/core/src/memory-object.ts
      - canon-ref:engine/packages/core/src/accepted-knowledge-object.ts
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/core/src/execution-unit.ts
    supersedes: []
    related:
      - P05
      - P06
    next_action: Use the P04 engine-seam note as the contract baseline, then execute P05 to wire explicit candidate refs, compilation reporting, and replay-safe frozen basis behavior through the narrowed seam.

  - id: CF-0011
    date: 2026-04-16
    status: active
    kind: outcome
    stage: pre-phase-4-convergence
    packet: P05
    topic: replay
    summary: P05 is now recorded in canon-knowledgebase/p05-compiler-injection-and-replay-basis.md with explicit post-evidence memory and canon stages, authoritative candidate refs, a first-class frozen knowledge basis, and the context compiler snapshot treated as the replay-safe context boundary.
    impact: The canonical rewrite can now assume one settled compiler and replay posture where exact replay reuses frozen knowledge refs, inclusion and exclusion reasons stay visible, and no inline learning side effects occur inside compilation.
    source:
      - canon-ref:dev/kb/p05-compiler-injection-and-replay-basis
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:engine/packages/provenance/src/replay-contract.ts
    supersedes: []
    related:
      - P06
      - P08
      - P09
    next_action: Use the P05 note as the final convergence baseline, then rewrite the canonical Phase 4+ plan before any later packet activates.

  - id: CF-0012
    date: 2026-04-16
    status: active
    kind: handoff
    stage: canonical-rewrite
    packet: none
    topic: process
    summary: Pre-Phase-4 convergence is complete through P05 and the rollout track must now pause for one canonical Phase 4+ rewrite that absorbs P00-P05 before P06-P13 resume.
    impact: Future sessions should treat the rewrite as the only active Canon step and should not execute later rollout packets directly from the migration plan.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/p05-compiler-injection-and-replay-basis
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
    supersedes: []
    related:
      - P05
      - P06
      - P13
    next_action: Rewrite the canonical Phase 4+ plan, update the tracker to the rewritten authority, and only then reactivate post-merge execution work.

  - id: CF-0013
    date: 2026-04-16
    status: active
    kind: decision
    stage: canonical-rewrite
    packet: none
    topic: process
    summary: `canon-ref:dev/kb/identity/canon-canon-registry` is now the root registry for canonized terms and durable planning facts, and `notes-flow` is the canon name for the file-first packet workflow used in this workspace.
    impact: Future sessions should add new canon terminology and durable workflow or planning facts there instead of relying on repeated chat phrasing.
    source:
      - canon-ref:dev/kb/identity/canon-canon-registry
      - canon-ref:desktop/canon-development-packet-workflow-scaffold
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P05
    next_action: Add new canon terms and facts to the registry as they are accepted, and keep workflow state files aligned when those additions change the active process.

  - id: CF-0014
    date: 2026-04-16
    status: active
    kind: decision
    stage: canonical-rewrite
    packet: none
    topic: process
    summary: The session companion now routes fresh sessions to `canon-ref:dev/kb/identity/canon-canon-registry` whenever workspace terminology, workflow labels, or durable planning facts matter.
    impact: Future sessions can recover canonized local language consistently without treating repeated chat phrasing as authority or rereading multiple status files to rediscover established terms.
    source:
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
      - canon-ref:dev/kb/identity/canon-canon-registry
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P05
    next_action: Keep the registry and session companion in sync whenever new canon terms or planning facts become part of the normal recovery flow.

  - id: CF-0015
    date: 2026-04-16
    status: active
    kind: outcome
    stage: canonical-rewrite
    packet: none
    topic: process
    summary: The canonical rewrite is now recorded in canon-knowledgebase/canon-phase-4-plus-plan.md, which absorbs P00-P05 into one active Phase 4+ authority and maps P06-P13 into release-stage execution rather than a second packet track.
    impact: Future sessions should reopen the canonical plan first, treat the rollout plan as historical migration support only, and execute Platform Gate through R7 from the rewritten release story.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P05
      - P06
      - P13
    next_action: Resume integrated Phase 4 execution from the Platform Gate checkpoint in the canonical plan.

  - id: CF-0016
    date: 2026-04-16
    status: active
    kind: unlock
    stage: phase-4-execution
    packet: P06
    topic: process
    summary: Stage C is now active again, with the earliest execution restart point at Platform Gate and the historical P06-P07 labels serving only as source markers for passive-capture and review-substrate work.
    impact: The next implementation session should start from the canonical plan's Platform Gate checkpoint and keep R1 disclosure-only plus R2 explicit-control boundaries intact while early learning substrate work hardens.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/p05-compiler-injection-and-replay-basis
    supersedes: []
    related:
      - P06
      - P07
      - P08
    next_action: Start the Platform Gate checkpoint and read the legacy P06-P07 packet artifacts only as bounded migration inputs.

  - id: CF-0017
    date: 2026-04-16
    status: active
    kind: decision
    stage: phase-4-execution
    packet: P06
    topic: process
    summary: Both plan authorities now include `canon-ref:dev/kb/identity/canon-canon-registry` as the local source for canonized terms and durable planning facts when terminology, workflow labels, or legacy packet translation matter.
    impact: Future sessions can recover both the active Phase 4+ execution language and the historical rollout vocabulary consistently without re-deriving local Canon terms from chat history.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan
      - canon-ref:dev/kb/identity/canon-canon-registry
    supersedes: []
    related:
      - P06
    next_action: Keep both plan files aligned with the registry whenever new canon terms or durable planning facts become part of execution recovery.

  - id: CF-0018
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: A thorough cross-repo search found no local old-plan authority references inside agentic-engine, but it did identify likely upstream Canon updates across the milestone architecture plan, maturity matrix, Platform Gate spec, context-compiler topology, and some downstream release surfaces.
    impact: Future sessions should treat upstream Canon authority sync as the current focus rather than assuming the local plan promotion is complete across both repos.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:engine/context
      - https://github.com/SaintFreddy/Canon/blob/main/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md
      - https://github.com/SaintFreddy/Canon/blob/main/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md
      - https://github.com/SaintFreddy/Canon/blob/main/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md
      - https://github.com/SaintFreddy/Canon/blob/main/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md
    supersedes: []
    related:
      - P06
      - P07
      - P13
    next_action: Execute Step 3 of the plan and update the upstream Tier 1 authority docs in bounded slices.

  - id: CF-0019
    date: 2026-04-16
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: process
    summary: In local shorthand, `the plan` now means `canon-ref:dev/kb/canon-phase-4-plus-plan`, and a plan must be step-bounded so a fresh session can usually finish one step in roughly 50k tokens and never exceed about 75k tokens without handoff or rebasing, with the append-only carry-forward ledger updated after each completed step.
    impact: Future sessions should organize active work as bounded plan steps, refer to the active authority simply as `the plan`, and update the ledger every time a step completes.
    source:
      - canon-ref:dev/kb/identity/canon-canon-registry
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
    next_action: Keep the plan, tracker, and recovery files aligned to bounded step execution and ledger updates.

  - id: CF-0020
    date: 2026-04-16
    status: active
    kind: unlock
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The current active checkpoint has shifted from direct Platform Gate implementation restart to Step 3 of the plan, which is the upstream Canon Tier 1 authority sync needed to stop cross-repo planning drift before deeper implementation resumes.
    impact: The next execution session should open the upstream Tier 1 docs first, preserve historical materials by demotion rather than deletion, and defer direct Platform Gate implementation slices until the authority sync is settled.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P06
      - P07
    next_action: Start the upstream Tier 1 authority sync in bounded steps and record each completed step in this ledger.

  - id: CF-0021
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Step 3 bounded-slice prep is now recorded in canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md, with additive per-file edits for the upstream milestone architecture plan, maturity matrix, Platform Gate spec, and context-compiler topology.
    impact: Future sessions can apply the Tier 1 sync one file at a time without re-reading or re-deriving the upstream authority edits from scratch.
    source:
      - canon-ref:dev/kb/step-3-upstream-tier-1-sync-bounded-slices
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the prepared slices in a writable upstream Canon checkout and verify that each edit preserves accepted body text while promoting the current authority.

  - id: CF-0022
    date: 2026-04-16
    status: active
    kind: blocker
    stage: phase-4-execution
    packet: none
    topic: process
    summary: This workspace does not currently contain a writable upstream Canon checkout; `Canon` is only an empty placeholder directory.
    impact: Step 3 can be prepared locally but cannot be fully landed or verified against upstream files from this workspace until a real Canon checkout is available.
    source:
      - canon-ref:dev/kb/step-3-upstream-tier-1-sync-bounded-slices
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Reopen Step 3 inside a real Canon checkout, apply the prepared Tier 1 slices, and then continue to Step 4 downstream surface sync.

  - id: CF-0023
    date: 2026-04-16
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Canon workspace now has a Deep-mode baton protocol at `canon-ref:dev/baton/amp-deep-baton` plus a durable packet helper at `canon-ref:dev/scripts/canon-baton-next.sh`, so ordinary `Do the next task` continuation can self-handoff until a real blocker appears.
    impact: Future sessions can own routine serialized continuation from durable files instead of making the user reopen each next mechanical step by hand.
    source:
      - canon-ref:dev/agents
      - canon-ref:dev/baton/amp-deep-baton
      - canon-ref:dev/scripts/canon-baton-next.sh
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P06
      - P07
    next_action: Use the Deep baton whenever the user asks for serialized continuation, and spawn exactly one Deep successor when the next step stays mechanical.

  - id: CF-0024
    date: 2026-04-16
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Deep-mode baton now explicitly makes the agent own routine continuation plus obvious self-service prerequisite work, and requires the chain to stop only after a true blocker is confirmed.
    impact: Future sessions should not bounce ordinary setup or next-step work back to the user; they should first attempt the smallest obvious mechanical actions that stay within current authority and tools.
    source:
      - canon-ref:dev/agents
      - canon-ref:dev/baton/amp-deep-baton
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P06
      - P07
    next_action: For serialized continuation commands, keep the baton moving through self-service mechanical steps and wait for the user only when the dependency or contradiction remains real after those attempts.

  - id: CF-0025
    date: 2026-04-16
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The `Canon` placeholder has been replaced with a real local Canon checkout on `main`, so the no-checkout blocker for local Step 3 execution is superseded.
    impact: Future sessions should apply the prepared Tier 1 slices directly in `Canon`; Step 3 is still unlanded upstream until those edits are made, verified, and pushed from that repo.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:canon/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan
    supersedes:
      - CF-0022
    related:
      - P06
      - P07
    next_action: Apply Slice 1A-1C from canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md to the milestone architecture plan in Canon, verify additive-only changes, and then hand off the next Tier 1 file.

  - id: CF-0026
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Slice 1A-1C is now applied locally to the upstream milestone architecture plan in `Canon`, adding convergence framing and resolved downstream status without rewriting the accepted body.
    impact: Future sessions can treat File 1 of Step 3 as locally synced and move directly to File 2; upstream promotion is still incomplete until the remaining Tier 1 files are edited, verified, and pushed.
    source:
      - canon-ref:dev/kb/step-3-upstream-tier-1-sync-bounded-slices
      - canon-ref:canon/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply Slice 2A-2C from canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md to the maturity matrix in Canon, verify additive-only changes, and then hand off the next Tier 1 file.

  - id: CF-0027
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The local File 1 Step 3 sync now also aligns the milestone plan's accepted-artifact metadata in `artifact-registry.seed.json` and `dependency-graph.seed.json`, and `validate_control_plane_integrity.py` still passes.
    impact: Future sessions can treat the milestone architecture plan slice as locally complete at both the document and control-plane metadata layers, then move directly to File 2 without reopening File 1 bookkeeping.
    source:
      - canon-ref:canon/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply Slice 2A-2C from canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md to the maturity matrix in Canon, verify additive-only changes, and then hand off the next Tier 1 file.

  - id: CF-0028
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Slice 2A-2C is now applied locally to the upstream maturity matrix in `Canon`, adding convergence framing, resolved downstream status, and accepted-review annotation without rewriting the accepted body.
    impact: Future sessions can treat Files 1-2 of Step 3 as locally synced and move directly to File 3; upstream promotion is still incomplete until the remaining Tier 1 files are edited, verified, and pushed.
    source:
      - canon-ref:dev/kb/step-3-upstream-tier-1-sync-bounded-slices
      - canon-ref:canon/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply Slice 3A-3C from canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md to the Platform Gate spec in Canon, verify additive-only changes, and then hand off the next Tier 1 file.

  - id: CF-0029
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Slice 3A-3C is now applied locally to the upstream Platform Gate spec in `Canon`, adding gate-status framing, passed-gate audit annotation, and resolved downstream status without rewriting the accepted body.
    impact: Future sessions can treat Files 1-3 of Step 3 as locally synced and move directly to File 4; upstream promotion is still incomplete until the remaining Tier 1 file is edited, verified, and pushed.
    source:
      - canon-ref:dev/kb/step-3-upstream-tier-1-sync-bounded-slices
      - canon-ref:canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply Slice 4A-4C from canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md to the context-compiler topology in Canon, verify additive-only changes, and then hand off the next Tier 1 file.

  - id: CF-0030
    date: 2026-04-16
    status: superseded
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Canon baton now requires Oracle-first bounded-step recovery and confirmation, defaults that reasoning pass to `deep3`, and reserves Deep `deep3` for execution successors unless a stronger supported mode is explicitly exposed to the session.
    impact: Future agents should not guess at unverified mode names; they should use Oracle first for baton reasoning, then run the actual bounded step in Deep `deep3`, while preferring a stronger mode only when the current session can really access it.
    source:
      - canon-ref:dev/baton/amp-deep-baton
      - canon-ref:dev/agents
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Continue Step 3 with the context-compiler topology slice under the Oracle-first and Deep `deep3` baton split, then hand off the next Tier 1 file if it stays mechanical.

  - id: CF-0031
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Slice 4A-4C is now applied locally to the upstream context-compiler topology in `Canon`, adding convergence framing, resolved downstream status, and accepted-review annotation without rewriting the accepted body.
    impact: Future sessions can treat all four Tier 1 Step 3 files as locally synced and move the active checkpoint to Step 4 downstream surface sync; upstream promotion is still incomplete until downstream surfaces are synced and the Canon repo changes are committed and pushed.
    source:
      - canon-ref:dev/kb/step-3-upstream-tier-1-sync-bounded-slices
      - canon-ref:canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Recover the first bounded Step 4 downstream surface in `Canon`, apply its sync, and verify the edit stays additive and compliant.

  - id: CF-0032
    date: 2026-04-16
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Automatic Deep baton continuation stops after local Step 3 completion because Step 4 is named only at the downstream-surface category level in durable files and is not yet reduced to one bounded file slice.
    impact: Future sessions can recover that Step 4 is next, but they should not auto-handoff into a mechanical execution step until the first downstream surface is explicitly selected and bounded.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
    supersedes: []
    related:
      - P06
      - P07
    next_action: Bound the first affected Step 4 downstream file in `Canon`, record that narrower checkpoint in durable state, and then resume the Deep baton.

  - id: CF-0033
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The first bounded Step 4 downstream surface is now fixed as `canon-ref:canon/docs/control-plane/releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack`, chosen as the earliest downstream release pack in the fixed release order that inherits the newly synced Tier 1 authority.
    impact: Future sessions no longer need to pause at Step 4 selection; they can start with one bounded R1 contract-pack sync before widening to R2, R3, R7, or broader control-plane carry-forward surfaces.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:canon/docs/control-plane/releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the Step 4 authority-sync edit to the R1 Transcript Chat contract pack in `Canon`, verify the change stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0034
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R1 Transcript Chat contract pack in `Canon`, adding convergence framing, accepted R1->R2 inheritance annotation, and resolved downstream status without rewriting the accepted contract body.
    impact: Future sessions can treat the first downstream Step 4 pack as locally synced and move directly to the R2 Context Chat contract pack; upstream promotion is still incomplete until the remaining downstream surfaces are edited, verified, and pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the next bounded Step 4 sync to the R2 Context Chat contract pack in `Canon`, verify the edit stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0035
    date: 2026-04-16
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R2 Context Chat contract pack in `Canon`, adding convergence framing, accepted R2 -> R3 inheritance annotation, and resolved downstream status without rewriting the accepted contract body.
    impact: Future sessions can treat the second downstream Step 4 pack as locally synced and move directly to the R3 Branch / Visual Thinker contract pack; upstream promotion is still incomplete until the remaining downstream surfaces are edited, verified, and pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r2-context-chat-contract/phase-4-r2-context-chat-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the next bounded Step 4 sync to the R3 Branch / Visual Thinker contract pack in `Canon`, verify the edit stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0036
    date: 2026-04-17
    status: superseded
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Canon baton execution default is rolled back from `deep3` to `deep2` because `deep3` is currently erroring in this workspace; `ampmax`, the baton protocol, and the workspace router now agree on `deep2` for manual launches, Oracle-first recovery, and `handoff` successors.
    impact: Future sessions should not continue launching or handing off Canon baton work in `deep3`; they should use `deep2` until a later durable update explicitly promotes a different supported mode.
    source:
      - canon-ref:home/zshrc
      - canon-ref:dev/agents
      - canon-ref:dev/baton/amp-deep-baton
      - canon-ref:dev/canon-now
    supersedes:
      - CF-0030
    related:
      - P06
      - P07
    next_action: Continue Canon baton work with `ampmax` and `handoff mode: deep2` until `deep3` is explicitly revalidated and re-promoted in durable state.

  - id: CF-0037
    date: 2026-04-17
    status: superseded
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The temporary `deep2` rollback is itself reverted because the installed Amp CLI does not support `deep2`; `ampmax`, the workspace router, and the Canon baton instructions now use the supported `deep` mode again.
    impact: Future sessions should launch `ampmax` and create Canon baton `handoff` successors with `mode: deep` until a newly supported alternative mode is verified in the local CLI help and then promoted in durable state.
    source:
      - canon-ref:home/zshrc
      - canon-ref:home/local/bin/ampmax
      - canon-ref:dev/agents
      - canon-ref:dev/baton/amp-deep-baton
      - canon-ref:dev/canon-now
    supersedes:
      - CF-0036
    related:
      - P06
      - P07
    next_action: Continue Canon baton work with `ampmax` and `handoff mode: deep`, and investigate the missing-name tool-use normalization warnings separately from mode selection.

  - id: CF-0038
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Local Canon baton mode naming is normalized: `deep3` and `deep2` are historical mistakes, `ampmax` is the manual deep-plus-xhigh launch, and every AMP `handoff` successor must keep using the supported `deep` mode name.
    impact: Future sessions should treat any old `deep3` or `deep2` durable text as superseded recovery history only, launch manual strongest-local sessions with `ampmax`, and never create new threads with unsupported mode names.
    source:
      - canon-ref:home/config/amp/settings.json
      - canon-ref:home/local/bin/ampmax
      - canon-ref:dev/agents
      - canon-ref:dev/baton/amp-deep-baton
    supersedes:
      - CF-0030
      - CF-0036
      - CF-0037
    related:
      - P06
      - P07
    next_action: Use `ampmax` for manual strongest-local execution, keep `handoff mode: deep`, and treat any future raw-tag or missing-name tool failures as separate parser or session-state defects rather than mode-selection guidance.

  - id: CF-0039
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: A distrustful recovery pass reconciled the contaminated baton range against disk, confirmed the R1 and R2 Step 4 syncs are truly present in `Canon`, repaired the `ampmax` launcher, and corrected the plan and ledger so only supported `deep` handoff guidance remains active.
    impact: Future sessions should recover Canon baton state from filesystem evidence first, treat the bad-thread range as non-authoritative unless disk agrees, use `ampmax` only for manual strongest-local launches, and keep every `handoff` on `mode: deep`.
    source:
      - canon-ref:home/config/amp/settings.json
      - canon-ref:home/local/bin/ampmax
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-carry-forward
      - canon-ref:canon/docs/control-plane/releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack
      - canon-ref:canon/docs/control-plane/releases/r2-context-chat-contract/phase-4-r2-context-chat-contract-pack
    supersedes: []
    related:
      - P06
      - P07
    next_action: Continue Step 4 at the R4 Artifact Workspace contract pack using filesystem-verified recovery rather than suspect thread claims.

  - id: CF-0040
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R3 Branch / Visual Thinker contract pack in `Canon`, adding convergence framing, accepted R3 -> R4 inheritance annotation, and resolved downstream status without rewriting the accepted contract body.
    impact: Future sessions can treat the third downstream Step 4 pack as locally synced and move directly to the R4 Artifact Workspace contract pack; upstream promotion is still incomplete until the remaining downstream surfaces are edited, verified, and pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the next bounded Step 4 sync to the R4 Artifact Workspace contract pack in `Canon`, verify the edit stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0041
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R4 Artifact Workspace contract pack in `Canon`, adding convergence framing, accepted R4 -> R5 inheritance annotation, and resolved downstream status without rewriting the accepted contract body.
    impact: Future sessions can treat the fourth downstream Step 4 pack as locally synced and move directly to the R5 Prompt Studio contract pack; upstream promotion is still incomplete until the remaining downstream surfaces are edited, verified, and pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r4-artifact-workspace-contract/phase-4-r4-artifact-workspace-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the next bounded Step 4 sync to the R5 Prompt Studio contract pack in `Canon`, verify the edit stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0042
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R5 Prompt Studio contract pack in `Canon`, adding convergence framing, accepted R5 -> R6 inheritance annotation, and resolved downstream status without rewriting the accepted contract body.
    impact: Future sessions can treat the fifth downstream Step 4 pack as locally synced and move directly to the R6 Governed Agent / Applet Chat contract pack; upstream promotion is still incomplete until the remaining downstream surfaces are edited, verified, and pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r5-prompt-studio-contract/phase-4-r5-prompt-studio-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the next bounded Step 4 sync to the R6 Governed Agent / Applet Chat contract pack in `Canon`, verify the edit stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0043
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R6 Governed Agent / Applet Chat contract pack in `Canon`, adding convergence framing, accepted R6 -> R7 inheritance annotation, resolved downstream status, and aligned accepted-artifact metadata without rewriting the accepted contract body.
    impact: Future sessions can treat the sixth downstream Step 4 pack as locally synced and move directly to the R7 Commissioning Bridge contract pack; upstream promotion is still incomplete until the remaining downstream surfaces are edited, verified, and pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Apply the next bounded Step 4 sync to the R7 Commissioning Bridge contract pack in `Canon`, verify the edit stays additive, then hand off the next downstream surface if it remains mechanical.

  - id: CF-0044
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 4 authority-sync edit is now applied locally to the upstream R7 Commissioning Bridge contract pack in `Canon`, adding convergence framing, accepted R7 -> Task Studio inheritance annotation, resolved downstream status, and aligned accepted-artifact metadata without rewriting the accepted contract body; a bounded follow-on check found the R7 blueprint and related downstream control-plane surfaces already aligned, so Step 4 is now locally complete.
    impact: Future sessions should move to Step 5 local recovery recheck and reopen Step 4 only if that distrustful recheck finds a specific contradictory upstream Canon file; upstream promotion is still incomplete until the local Canon changes are pushed.
    source:
      - canon-ref:canon/docs/control-plane/releases/r7-commissioning-bridge-contract/phase-4-r7-commissioning-bridge-contract-pack
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:canon/docs/control-plane/implementation/release-blueprints/r7-commissioning-bridge-blueprint
      - canon-ref:dev/canon-now
    supersedes: []
    related:
      - P06
      - P07
    next_action: Execute Step 5 by rechecking local recovery state against the promoted upstream authority and keeping the Canon Dev recovery files aligned unless a concrete contradiction reopens Step 4.

  - id: CF-0045
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Step 5 local recovery recheck is now locally complete; it found stale active-step routing only in `canon-phase-4-plus-plan.md` and `canon-knowledgebase-layer-session-companion.md`, aligned those recovery surfaces, and found no contradictory upstream Canon file during the bounded recheck.
    impact: Fresh sessions can recover the completed Step 5 state from the plan, session companion, ledger, task tracker, and baton helper without being sent back to Step 3 or Step 4; automatic baton continuation should stop until a post-sync execution step is explicitly bounded in durable files.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/scripts/canon-baton-next.sh
    supersedes: []
    related:
      - P06
      - P07
    next_action: Recover from the refreshed post-Step-5 authority surfaces, reopen Step 4 only if a specific contradictory upstream Canon file appears, and do not auto-handoff into a post-sync execution step until that next step is explicitly bounded in durable files.

  - id: CF-0046
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Post-Step-5 routing is now the active recovery story; earlier checkpoint-routing entries that pointed to Platform Gate or Step 3 as the current restart point are historical milestones, not live next-step guidance.
    impact: Fresh sessions should recover from canon-now, the task tracker, the refreshed session companion, and the completed-step plan state; they should not resume Platform Gate or Step 3 from older ledger routing unless a new durable update explicitly promotes that move again.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
      - canon-ref:dev/scripts/canon-baton-next.sh
    supersedes:
      - CF-0016
      - CF-0020
    related:
      - P06
      - P07
    next_action: Keep the baton paused after recovery until one bounded post-sync execution step is promoted in durable files, and treat older checkpoint-routing entries as historical route markers only.

  - id: CF-0047
    date: 2026-04-17
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The first post-Step-5 execution step is now explicitly bounded to a workspace `.md` memo answering whether `agentic-engine` should one day have its own language, with an Oracle-backed position that also states whether such a language should be Turing complete.
    impact: Fresh sessions no longer need to guess the first post-sync move; they should complete the language-query memo first, and only after that should the following agent commit one execution plan in durable files before baton continuation resumes. Deliberation may take multiple rounds before that plan commitment, but the commitment itself must be explicit.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes: []
    related:
      - P06
      - P07
    next_action: Hand off one Deep successor to write the language-query memo into a `.md` file in the workspace folder with Oracle support, then stop; the following agent should use that memo and any needed deliberation rounds to commit one explicit execution plan in durable files before further baton continuation.

  - id: CF-0048
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The Oracle-backed language-query memo now lives at `canon-ref:dev/archive/agentic-engine-language-query-memo`, concluding that `agentic-engine` should not pursue its own general-purpose language and that any future language-like layer should be a constrained declarative spec over existing engine contracts rather than a Turing-complete language.
    impact: Fresh sessions now have a durable architectural answer for the language question; the next bounded post-sync step is to commit one explicit execution plan in durable files before ordinary baton continuation resumes, with any needed deliberation happening before that commitment lands.
    source:
      - canon-ref:dev/archive/agentic-engine-language-query-memo
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes: []
    related:
      - P06
      - P07
    next_action: Recover the completed memo, deliberate as needed, and then commit one explicit execution plan in durable files before ordinary baton continuation resumes.

  - id: CF-0049
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The post-sync execution plan is now committed in `canon-ref:dev/kb/canon-phase-4-plus-plan`, and ordinary baton continuation resumes from `PG-1` — the Platform Gate engine seam checkpoint and gap map.
    impact: Fresh sessions should reopen the plan's committed post-sync execution section and execute only `PG-1` using the language-query memo plus the bounded `agentic-engine` seam files named there; they should not reopen Step 3, Step 4, Step 5, or the memo substance unless a concrete contradiction appears.
    source:
      - canon-ref:dev/archive/agentic-engine-language-query-memo
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0047
      - CF-0048
    related:
      - P06
      - P07
    next_action: Execute `PG-1` by producing `canon-ref:dev/kb/platform-gate-engine-seam-checkpoint`, verify its claims against the cited `agentic-engine` seam files, and then update durable state again before choosing the next implementation slice.

  - id: CF-0050
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `PG-1` is now complete in `canon-ref:dev/kb/platform-gate-engine-seam-checkpoint`, which confirms the engine-owned seam is real, keeps Step 4 closed, and advances ordinary baton continuation to `PG-2` — frozen knowledge participation basis contract and wiring.
    impact: Fresh sessions should recover the `PG-1` checkpoint note before editing code, then execute only `PG-2` inside the bounded `agentic-engine` seam files; they should not reopen Step 4, the language memo, or the broader convergence baseline unless a concrete contradiction appears.
    source:
      - canon-ref:dev/kb/platform-gate-engine-seam-checkpoint
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0049
    related:
      - P06
      - P07
    next_action: Execute `PG-2` by adding the first-class frozen knowledge participation basis surface to the bounded `agentic-engine` seam files named in the plan, then verify with `pnpm typecheck` and `pnpm test` before choosing the next seam-hardening slice.

  - id: CF-0051
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `PG-2` is now complete in `agentic-engine`, which lands a first-class frozen knowledge participation basis, keeps Step 4 closed, and advances ordinary baton continuation to `PG-3` — authoritative knowledge-lane ref passthrough.
    impact: Fresh sessions should recover the completed `PG-2` slice from the refreshed authority files, then execute only `PG-3` inside the bounded engine seam; they should not reopen Step 4, the language memo, or the broader convergence baseline unless a concrete contradiction appears.
    source:
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:engine/workers/run-executor/src/run-executor.ts
      - canon-ref:engine/contracts/exports.json
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0050
    related:
      - P06
      - P07
    next_action: Execute `PG-3` by adding optional opaque authoritative refs to `MemoryObject` and `AcceptedKnowledgeObject`, preserve them into compiler `candidateRef` outputs and frozen knowledge-participation artifacts, then verify with `pnpm typecheck` and `pnpm test` before choosing the next seam-hardening slice.

  - id: CF-0052
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `PG-3` is now complete in `agentic-engine`, which lands authoritative knowledge-lane ref passthrough, keeps Step 4 closed, and advances ordinary baton continuation to `PG-4` — knowledge-lane admission projection seam.
    impact: Fresh sessions should recover the completed `PG-3` slice from the refreshed authority files, then execute only `PG-4` inside the bounded engine seam; they should not reopen Step 4, the language memo, or the broader convergence baseline unless a concrete contradiction appears.
    source:
      - canon-ref:engine/packages/core/src/memory-object.ts
      - canon-ref:engine/packages/core/src/accepted-knowledge-object.ts
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0051
    related:
      - P06
      - P07
    next_action: Execute `PG-4` by adding optional explicit admission projections for memory and accepted-knowledge candidates, keep legacy lifecycle gating only as fallback, leave queue order unchanged in this slice, and verify with `pnpm typecheck` and `pnpm test` before choosing the next seam-hardening slice.

  - id: CF-0053
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `PG-4` is now complete in `agentic-engine`, which lands explicit knowledge-lane admission projections with explicit projection-versus-fallback reporting, keeps Step 4 closed, and advances ordinary baton continuation to `PG-5` — memory-before-canon compiler staging.
    impact: Fresh sessions should recover the completed `PG-4` slice from the refreshed authority files, then execute only `PG-5` inside the bounded engine seam; they should not reopen Step 4 or remove legacy lifecycle fallback semantics in the same slice unless a concrete contradiction appears.
    source:
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:engine/workers/run-executor/src/run-executor.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0052
    related:
      - P06
      - P07
    next_action: Execute `PG-5` by making compiler staging budget memory before accepted knowledge while keeping projection-first admission and legacy lifecycle fallback unchanged, then verify with `pnpm typecheck` and `pnpm test` before choosing the next seam-hardening slice.

  - id: CF-0054
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `PG-5` is now complete in `agentic-engine`, which lands explicit memory-before-canon compiler staging under tight budget pressure, keeps projection-first admission plus legacy fallback behavior unchanged, keeps Step 4 closed, and advances ordinary baton continuation to `PG-6` — legacy knowledge-lane fallback isolation.
    impact: Fresh sessions should recover the completed `PG-5` slice from the refreshed authority files, then execute only `PG-6` inside the bounded engine seam; they should not reopen Step 4 or widen this next slice into public contract, event, or broad lifecycle changes unless a concrete contradiction appears.
    source:
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0053
    related:
      - P06
      - P07
    next_action: Execute `PG-6` by isolating legacy knowledge-lane fallback behind explicit compiler-local helpers while keeping projection-first admission, memory-before-canon staging, and the existing compilation report plus knowledge-participation basis unchanged, then verify with `pnpm typecheck` and `pnpm test` before choosing the next seam-hardening slice.

  - id: CF-0055
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `PG-6` is now complete in `agentic-engine`, which localizes legacy knowledge-lane fallback behind explicit compiler-local helpers, keeps projection-first admission plus memory-before-canon staging intact, and exhausts the recorded `PG-1` seam gap map; ordinary baton continuation is now paused pending accepted explicit host-projection contract authority rather than advancing to an invented `PG-7`.
    impact: Fresh sessions should recover the completed `PG-6` slice from the refreshed authority files, keep Step 4 closed, and stop without inventing the next Platform Gate implementation slice unless higher-authority Canon material now defines the post-`PG-6` host-projection contract boundary.
    source:
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0054
    related:
      - P06
      - P07
    next_action: Resume only when accepted authority defines the explicit host-projection contract boundary for any post-`PG-6` lifecycle-fallback retirement slice; until then, keep the baton paused and do not invent `PG-7`.

  - id: CF-0056
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: A bounded post-`PG-6` contradiction audit found the prior paused-state closure was too strong: `PG-6` remains complete, but `ContextCompilerPipeline` still budgets optional evidence after memory and accepted knowledge, so the inherited `evidence -> memory -> canon -> freeze` stage model is not fully landed and the baton should reopen from that local seam correction rather than waiting only on host-projection authority.
    impact: Fresh sessions should recover the reopened local stage-order contradiction from the authority files, execute only the bounded compiler-stage-order correction inside `agentic-engine`, and return to the host-projection-authority pause only if that local contradiction is actually closed.
    source:
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/p05-compiler-injection-and-replay-basis
      - canon-ref:dev/kb/platform-gate-engine-seam-checkpoint
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0055
    related:
      - P05
      - P06
      - P07
    next_action: Land the smallest compiler-stage-order correction so optional evidence budgets before memory and accepted knowledge, add regression coverage, verify with `pnpm typecheck` plus `pnpm test`, then decide whether the baton can truthfully return to the host-projection-authority pause.

  - id: CF-0057
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The bounded post-evidence compiler stage-order correction is now complete in `agentic-engine`, which lands optional evidence before memory and accepted knowledge, keeps projection-first admission plus localized legacy fallback intact, and returns the baton to the host-projection-authority pause rather than inventing a new `PG-7`.
    impact: Fresh sessions should recover the closed local seam contradiction from the authority files, treat the inherited `evidence -> memory -> canon -> freeze` order as locally landed, and stop unless accepted higher-authority Canon material names another contract-bearing slice or a cited contradiction reopens the seam.
    source:
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
      - canon-ref:engine/workers/run-executor/src/tests/run-executor.test.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0056
    related:
      - P05
      - P06
      - P07
    next_action: Resume only if accepted higher-authority Canon material names another post-`PG-6` contract-bearing slice or a cited local seam contradiction reopens.

  - id: CF-0058
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The bounded publication audit is complete: the validated engine seam pack was published to `agentic-engine` `origin/main` from a clean clone at `f03ce3c`, the Canon control-plane sync pack was published to `Canon` `origin/main` at `ae196ae`, and the baton returns to the host-projection-authority pause.
    impact: Fresh sessions should treat remote `main` in both repos as the published authority, and they should not treat the original dirty `agentic-engine` checkout or its stray wiki history, junk files, and extra unpublished diffs as publication truth.
    source:
      - https://ampcode.com/threads/T-019d9912-c03c-71bf-a780-868c6bda8dad
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/workers/run-executor/src/run-executor.ts
      - canon-ref:canon/docs/control-plane/artifact-registry.seed.json
      - canon-ref:canon/docs/control-plane/dependency-graph.seed.json
      - canon-ref:canon/scripts/validators/validate-control-plane-integrity.py
    supersedes:
      - CF-0057
    related:
      - P05
      - P06
      - P07
    next_action: Resume only if accepted higher-authority Canon material names another post-`PG-6` contract-bearing slice, a cited local seam contradiction reopens, or a later session explicitly chooses to clean up the original dirty `agentic-engine` checkout.

  - id: CF-0059
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: A local-only Canon-style bounded slice note now exists at `canon-ref:dev/gpt5-packet/canon-registry/upstream-review-admission-projection-bounded-slices`, translating the raw admission-projection proposal into per-file upstream review slices without changing `Canon` or `agentic-engine`, and the host-projection-authority pause remains in force.
    impact: Future sessions can reuse the local review-prep artifacts for an explicitly chosen operator task, but ordinary baton continuation remains parked until accepted higher-authority Canon material names a contract-bearing slice or a cited contradiction reopens the seam.
    source:
      - canon-ref:dev/gpt5-packet/canon-registry/proposed-upstream-admission-projection-slice
      - canon-ref:dev/gpt5-packet/canon-registry/upstream-review-admission-projection-bounded-slices
      - canon-ref:dev/gpt5-packet/canon-registry/operator-final-verdict
      - canon-ref:dev/gpt5-packet/canon-registry/what-wait-means-now
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Stay parked by default; if another explicit local operator task is chosen, compare this review note against the exact wording of the three target Canon files or prepare a narrower minimum-acceptable-wording variant without treating that work as resumed implementation.

  - id: CF-0060
    date: 2026-04-17
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: A local-only pre-unblock runway now exists at `canon-ref:dev/gpt5-packet/canon-registry/host-projection-pre-unblock-local-runway`, which keeps implementation paused but defines three serialized operator steps; the next mechanical baton step is an exact wording/style compare against the three target Canon files.
    impact: Fresh sessions should keep the host-projection-authority pause for implementation, but they should continue the explicit local runway instead of stopping outright when the user wants serialized continuation.
    source:
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-pre-unblock-local-runway
      - canon-ref:dev/gpt5-packet/canon-registry/upstream-review-admission-projection-bounded-slices
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Execute Step 1 by creating `canon-ref:dev/gpt5-packet/canon-registry/admission-projection-target-file-wording-compare`, capturing exact insertion anchors, house vocabulary, wording likely to trigger pushback, safest additive phrasing, and whether each current slice should stay as written or be narrowed.

  - id: CF-0061
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Step 1 of the local-only pre-unblock runway is now complete: `canon-ref:dev/gpt5-packet/canon-registry/admission-projection-target-file-wording-compare` compares the bounded slices note against the three target Canon files, implementation remains paused, and the next mechanical baton step is Step 2.
    impact: Fresh sessions can recover the exact insertion anchors, house vocabulary, likely pushback wording, and narrowing guidance from the compare note instead of rereading the target files before preparing the minimum-acceptable wording variant.
    source:
      - canon-ref:dev/gpt5-packet/canon-registry/admission-projection-target-file-wording-compare
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-pre-unblock-local-runway
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Execute Step 2 by creating `canon-ref:dev/gpt5-packet/canon-registry/admission-projection-minimum-acceptable-wording`, preserving the six missing contract answers while cutting wording that feels schema-heavy, object-creating, or broader than needed.

  - id: CF-0062
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Step 2 of the local-only pre-unblock runway is now complete: `canon-ref:dev/gpt5-packet/canon-registry/admission-projection-minimum-acceptable-wording` preserves the six missing contract answers while narrowing the wider review note to target-file house style, implementation remains paused, and the next mechanical baton step is Step 3.
    impact: Fresh sessions can recover the narrowest acceptable wording variant without rereading the target Canon files, and they should continue with the local-only authority reopen checklist rather than revisiting implementation or widening the review-prep slice.
    source:
      - canon-ref:dev/gpt5-packet/canon-registry/admission-projection-minimum-acceptable-wording
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-pre-unblock-local-runway
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Execute Step 3 by creating `canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist`, using the contract scan report, pause verdict notes, and the completed minimum-acceptable wording variant to define the smallest honest authority combination that would reopen the seam.

  - id: CF-0063
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Step 3 of the local-only pre-unblock runway is now complete: `canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist` defines the six yes-or-no reopen checks, the smallest sufficient accepted-authority combination, and the insufficient evidence cases, so the runway is complete and the baton returns to parked-by-default state.
    impact: Fresh sessions should keep implementation paused, use the checklist only when accepted higher-authority Canon material changes or a cited contradiction appears, and otherwise stop instead of relitigating the same host-projection pause boundary.
    source:
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-pre-unblock-local-runway
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Stay parked by default; if accepted higher-authority Canon material changes or a cited contradiction appears, apply `canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist` before deciding whether the seam honestly reopens.

  - id: CF-0064
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The approved minimum host-projection contract wording is now promoted locally into Canon authority in `Canon`, control-plane integrity still passes, the reopen checklist now evaluates all six checks as yes locally, and the seam is reopened locally for a new bounded decision.
    impact: Fresh sessions should no longer route through the pre-unblock runway as the active checkpoint; they should distinguish local reopen from published authority and take only one bounded follow-on step such as publication or a tightly scoped post-reopen seam decision.
    source:
      - canon-ref:canon/docs/spec-digests/shared-environment/env-control
      - canon-ref:canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec
      - canon-ref:canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist
      - canon-ref:canon/scripts/validators/validate-control-plane-integrity.py
    supersedes:
      - CF-0063
    related:
      - P05
      - P06
      - P07
    next_action: Publish the local Canon authority promotion or use the reopened authority to choose one bounded post-reopen seam step without widening into broad implementation.

  - id: CF-0065
    date: 2026-04-17
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: process
    summary: `yalla` is now a canonized lexical term in the Canon Dev registry, meaning proceed now or let's go, and future sessions may treat it as an explicit prompt to continue without added ceremony.
    impact: Fresh sessions no longer need to infer whether `yalla` is casual chatter or an execution cue; in this workspace it is canon shorthand for immediate forward motion.
    source:
      - canon-ref:dev/kb/identity/canon-canon-registry
      - https://en.wiktionary.org/wiki/%D9%8A%D8%A7%D8%A7%D9%84%D9%84%D9%87
      - https://ampcode.com/threads/T-019d9af9-eef3-7429-bfbd-00f2cda0f126
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Use `yalla` consistently as workspace shorthand for proceed now, while still recovering the exact bounded step from durable Canon state.

  - id: CF-0066
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The host-projection Canon authority promotion is now published to `github.com/SaintFreddy/Canon` `main` at `fafd681`, the control-plane integrity validator passed before publication, and the reopen checklist now passes against published Canon authority.
    impact: Fresh sessions should treat the host-projection contract as present in published Canon authority and move to one bounded post-reopen seam decision rather than more pre-unblock prep or publication work.
    source:
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - https://github.com/SaintFreddy/Canon/commit/fafd681
      - canon-ref:canon/scripts/validators/validate-control-plane-integrity.py
    supersedes:
      - CF-0064
    related:
      - P05
      - P06
      - P07
    next_action: Use the reopened published Canon authority to choose one bounded post-reopen seam decision without widening into broad implementation.

  - id: CF-0067
    date: 2026-04-17
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: compiler
    summary: The first post-reopen seam decision now selects lane-level authoritative host-projection inputs as the next engine slice because published Canon says supplied lane inputs are authoritative and fallback is allowed only when a lane is absent, while the current compiler still falls back candidate-by-candidate inside supplied lane bags.
    impact: Future sessions should implement only this lane-authority slice in `agentic-engine`; they should not widen into replay, export, or broader lifecycle work in the same step.
    source:
      - canon-ref:dev/kb/post-reopen-host-projection-lane-authority-checkpoint
      - canon-ref:dev/gpt5-packet/canon-registry/host-projection-authority-reopen-checklist
      - canon-ref:canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec
      - canon-ref:canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Implement the selected lane-level authoritative host-projection slice in `agentic-engine`, verify it with `corepack pnpm typecheck` plus `corepack pnpm test`, and then update durable state again in the same session.

  - id: CF-0068
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: compiler
    summary: The post-reopen lane-authority implementation slice is now landed locally in `agentic-engine`: supplied memory/canon lane bags are authoritative per lane, omitted candidates inside a supplied lane are excluded under explicit-projection basis, frozen knowledge participation preserves lane `inputState`, and `corepack pnpm typecheck` plus `corepack pnpm test` both passed.
    impact: Fresh sessions should treat the selected post-reopen implementation slice as complete locally and return to a bounded next-step selection rather than widening automatically into replay, diff, export, or broader lifecycle retirement.
    source:
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:engine/workers/run-executor/src/run-executor.ts
      - canon-ref:engine/workers/run-executor/src/tests/run-executor.test.ts
      - https://ampcode.com/threads/T-019d9b56-0de9-7249-babf-3d474184382b
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Recover from updated durable state and choose exactly one next bounded post-reopen seam step before any further implementation or publication work.

  - id: CF-0069
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Canon baton continuation now uses bounded-step recoverability rather than the earlier narrow mechanical-handoff reading; if the next step has a clear start, clear end, and recoverable next start-point, baton flow should continue unless a true blocker, contradiction, missing dependency, or genuine human-judgment fork remains.
    impact: Future sessions should not stop serialized Canon continuation merely because the next bounded step still contains ordinary engineering judgment, and they should treat the older mechanical-only baton wording as superseded.
    source:
      - canon-ref:dev/agents
      - canon-ref:dev/baton/amp-deep-baton
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-knowledgebase-layer-session-companion
    supersedes:
      - CF-0023
      - CF-0024
    related:
      - P05
      - P06
      - P07
    next_action: Apply this baton rule to the next serialized Canon continuation and stop only if the next bounded step cannot be recovered cleanly or still needs real human judgment.

  - id: CF-0070
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: compiler
    summary: The second post-reopen host-projection consumption slice is now landed locally in `agentic-engine`: supplied memory and accepted-knowledge lane bags resolve by authoritative candidate ref first, engine-local IDs remain tolerated as compatibility fallback for the already-shipped projection seam, targeted compiler and run-executor regressions now use ref-keyed host projections, `contracts/exports.json` required no edit, and `corepack pnpm typecheck` plus `corepack pnpm test` both passed.
    impact: Fresh sessions should treat ref-first host-projection consumption as complete locally, should not reopen the earlier selection-only checkpoint, and should move directly to the next bounded authority-named seam gap.
    source:
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
      - canon-ref:engine/workers/run-executor/src/run-executor.ts
      - canon-ref:engine/workers/run-executor/src/tests/run-executor.test.ts
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-phase-4-plus-plan
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Treat the ref-first host-projection consumption slice as complete locally and use the accepted-knowledge lane metadata checkpoint as the next bounded recovery point.

  - id: CF-0071
    date: 2026-04-17
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: compiler
    summary: The next post-reopen seam step is accepted-knowledge lane metadata passthrough so canon-lane optional `mode` and validity summary survive the engine seam and frozen reporting surfaces without changing ref-first lookup, lane-authority semantics, stage order, replay or diff behavior, or broader lifecycle work.
    impact: Future sessions should implement only this bounded slice in `agentic-engine` and should not widen into memory-lane metadata, generalized lane-schema work, replay, diff, or export redesign unless the slice proves that is strictly required.
    source:
      - canon-ref:dev/kb/post-reopen-accepted-knowledge-lane-metadata-checkpoint
      - canon-ref:canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec
      - canon-ref:canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Implement the accepted-knowledge lane metadata passthrough slice, verify it with `corepack pnpm typecheck` plus `corepack pnpm test`, review `contracts/exports.json`, and update durable state again in the same session.

  - id: CF-0072
    date: 2026-04-17
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: compiler
    summary: The third post-reopen seam slice is now landed locally in `agentic-engine`: accepted-knowledge lane inputs preserve optional canon-lane `mode` and optional validity summary through compiler normalization, compiled context, and deterministic frozen snapshots, targeted core/compiler/snapshot/run-executor regressions prove the passthrough, `contracts/exports.json` required no edit, and `corepack pnpm typecheck` plus `corepack pnpm test` both passed.
    impact: Fresh sessions should treat the accepted-knowledge lane metadata passthrough slice as complete locally and should not reopen that implementation slice while the next bounded post-reopen seam decision remains audit-only.
    source:
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/core/src/tests/compiled-context-and-evidence.deep.test.ts
      - canon-ref:engine/packages/context-compiler/src/compiler-pipeline.ts
      - canon-ref:engine/packages/context-compiler/src/tests/compiler-pipeline.deep.test.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:engine/packages/context-compiler/src/tests/snapshot-freezer.deep.test.ts
      - canon-ref:engine/workers/run-executor/src/run-executor.ts
      - canon-ref:engine/workers/run-executor/src/tests/run-executor.test.ts
      - https://ampcode.com/threads/T-019d9b7c-4354-779c-9502-ae54eabf2ed4
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Treat the accepted-knowledge lane metadata passthrough slice as complete locally and use the frozen-posture replay/audit sufficiency checkpoint as the next bounded recovery point.

  - id: CF-0073
    date: 2026-04-17
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: compiler
    summary: The next post-reopen seam step is a frozen-posture replay/audit sufficiency checkpoint so durable state can decide whether the reopened engine seam is now locally closed or whether one more clearly named engine-owned reporting gap remains, without widening into replay, diff, or compact event redesign.
    impact: Future sessions should execute only this bounded audit/checkpoint next and should not start another engine implementation slice unless that checkpoint names it explicitly.
    source:
      - canon-ref:dev/kb/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint
      - canon-ref:canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec
      - canon-ref:canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology
      - canon-ref:engine/packages/core/src/compiled-context.ts
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts
      - canon-ref:engine/packages/provenance/src/replay-contract.ts
    supersedes: []
    related:
      - P05
      - P06
      - P07
    next_action: Execute the frozen-posture replay/audit sufficiency checkpoint, update durable state with either local seam closure or one more clearly bounded engine-owned step, and then hand off exactly one successor again only if the next start-point remains recoverable.

  - id: CF-0074
    date: 2026-04-17
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: replay
    summary: The frozen-posture replay/audit sufficiency checkpoint is complete and closes the reopened post-reopen engine seam locally because the frozen context boundary already preserves the Canon-named lane posture for later replay or audit consumers.
    impact: Future sessions should treat the reopened seam as locally closed and should not reopen another engine-owned reporting slice unless later higher-authority Canon wording or a specific replay or audit contradiction names a new bounded gap.
    source:
      - canon-ref:dev/kb/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint
      - canon-ref:canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology#L112-L153
      - canon-ref:engine/packages/core/src/compiled-context.ts#L139-L149
      - canon-ref:engine/packages/core/src/compiled-context.ts#L416-L446
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts#L100-L103
      - canon-ref:engine/packages/context-compiler/src/snapshot-freezer.ts#L176-L204
      - canon-ref:engine/packages/provenance/src/replay-contract.ts#L12-L15
      - canon-ref:engine/workers/replay-compare/src/index.ts#L39-L45
      - canon-ref:engine/workers/replay-compare/src/index.ts#L259-L307
      - https://ampcode.com/threads/T-019d9b8d-639e-7275-aecd-37244518c429
    supersedes:
      - CF-0073
    related:
      - P05
      - P06
      - P07
    next_action: Stop the Canon baton here unless a later higher-authority Canon checkpoint or a specific contradiction supplies one new bounded recoverable step.

  - id: CF-0075
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Canon Dev runner orchestration is now centralized through Model-Ref at `canon-ref:dev/kb/identity/model-ref-registry`, and the live baton contract is runner-neutral at `canon-ref:dev/baton/baton-protocol`.
    impact: Future sessions should use runner-neutral workflow language in live docs, read Model-Ref whenever launcher or baton behavior matters, and treat older AMP-specific baton wording in historical notes or superseded carry-forward entries as provenance rather than the current contract.
    source:
      - canon-ref:dev/kb/identity/model-ref-registry
      - canon-ref:dev/scripts/model-ref.py
      - canon-ref:dev/scripts/migrate-amp-coupling.py
      - canon-ref:dev/baton/baton-protocol
      - canon-ref:dev/agents
      - canon-ref:dev/canon-now
    supersedes:
      - CF-0023
      - CF-0024
      - CF-0038
      - CF-0039
    related:
      - P06
      - P07
    next_action: Use `scripts/migrate-amp-coupling.py report` after future live-scope edits, and update Model-Ref instead of scattering new runner or model wording through active docs.

  - id: CF-0076
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Canon baton flow is now explicitly defined as session-owned successor creation plus direct baton-packet injection when the current runner or host exposes one fresh same-runner successor path; it is not an unattended scheduler and it is not specific to AMP, Claude Code, or Codex.
    impact: Future sessions should treat the baton packet as exact text owned by the current session, inject it directly into one fresh successor when the host supports that path, and otherwise write the same packet explicitly in durable files before stopping.
    source:
      - canon-ref:dev/kb/identity/model-ref-registry
      - canon-ref:dev/baton/baton-protocol
      - canon-ref:dev/baton/baton-automation-plan
      - canon-ref:dev/agents
      - canon-ref:dev/scripts/canon-baton-next.sh
      - canon-ref:dev/canon-now
    supersedes:
      - CF-0075
    related:
      - P06
      - P07
    next_action: When future runner work reopens a bounded Canon step, prefer one same-runner successor with direct baton-packet injection over user-as-scheduler reopening, and fall back to the explicit durable packet only when the host cannot create that successor directly.

  - id: CF-0077
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Canon baton safety is now mechanically enforced: `canon-ref:dev/canon-now` carries an explicit `Baton state`, the helper at `canon-ref:dev/scripts/canon-baton-next.sh` emits an exact successor packet only when that state is `continue`, the live contract canonizes `same-runner successor`, and `canon-ref:dev/scripts/model-ref.py` now validates typed runner-adapter semantics instead of only checking field presence.
    impact: Future sessions should treat `Baton state` as the sole durable gate for successor creation, should not create any successor when it is `stop` even if a broader task row remains active, and should rely on Model-Ref validation plus the runner-coupling migration checker to keep live workflow surfaces aligned across AMP, Codex, and Claude Code.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/agents
      - canon-ref:dev/baton/baton-protocol
      - canon-ref:dev/baton/baton-automation-plan
      - canon-ref:dev/kb/identity/canon-canon-registry
      - canon-ref:dev/kb/identity/model-ref-registry
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/scripts/canon-baton-next.sh
      - canon-ref:dev/scripts/model-ref.py
      - canon-ref:dev/scripts/migrate-amp-coupling.py
    supersedes:
      - CF-0076
    related:
      - P06
      - P07
    next_action: Keep `Baton state` aligned with real next-step availability, extend the runner-coupling checker when new live authority files are added, and continue using one same-runner successor only when the durable state explicitly permits continuation.

  - id: CF-0078
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Codex and Claude Code runner adapters are now grounded in verified local CLI behavior rather than AMP-style projection: both expose host-invoked prompt-bearing startup or resume surfaces for same-runner baton continuation, while only AMP remains modeled as a native in-session baton handoff tool.
    impact: Future sessions should treat Codex and Claude Code successor creation as host-CLI baton paths, not as proof of native self-replacement or a built-in handoff primitive, and should continue to reserve the native baton label for AMP unless later verified local tooling proves otherwise.
    source:
      - canon-ref:dev/kb/identity/model-ref-registry
      - canon-ref:dev/scripts/model-ref.py
      - canon-ref:dev/baton/baton-protocol
      - canon-ref:dev/baton/baton-automation-plan
      - local `codex --help`
      - local `codex fork --help`
      - local `codex resume --help`
      - local `claude --help`
    supersedes:
      - CF-0077
    related:
      - P06
      - P07
    next_action: When a future same-runner baton step is reopened for Codex or Claude Code, prefer the verified local CLI startup or resume surface with injected packet text, and update Model-Ref again if either runner later exposes a true native in-session baton primitive.

  - id: CF-0079
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The prior Canon stop-state is now superseded operationally: the post-reopen engine seam remains locally closed, but accepted Phase 6 packet authority plus the new local entry checkpoint now select `pkt.phase6-r1-conversation-contracts-objects-packet.v1` as the first bounded post-Platform-Gate step.
    impact: Future sessions should keep the engine seam closed, recover `canon-ref:dev/kb/phase-6-r1-conversation-entry-checkpoint`, and execute only the accepted R1 `contracts_objects` packet in a writable `Canon` implementation session rather than waiting for another engine-owned seam gap or widening into later packet families.
    source:
      - canon-ref:dev/kb/phase-6-r1-conversation-entry-checkpoint
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:canon/docs/control-plane/core/phase-6-execution-packet-index.json
      - canon-ref:canon/docs/control-plane/implementation/packets/phase-6-r1-conversation-contracts-objects-packet
      - canon-ref:canon/docs/control-plane/core/codebase-current-state.json
    supersedes:
      - CF-0074
    related:
      - P08
    next_action: Recover the new entry checkpoint, then execute only `pkt.phase6-r1-conversation-contracts-objects-packet.v1` in a writable implementation session rooted at `Canon`; if that workspace boundary is still unavailable, record the blocker instead of widening.

  - id: CF-0080
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: P08
    topic: process
    summary: The accepted R1 `contracts_objects` packet is now complete locally in the writable `Canon` checkout as six whitelisted `packages/` schema and contract catalogs, so the next bounded Canon step is `pkt.phase6-r1-conversation-runtime-execution-packet.v1`.
    impact: Future sessions should recover `canon-ref:dev/kb/phase-6-r1-conversation-contracts-objects-packet-checkpoint`, treat the new `Canon/packages/` slice as local unpublished implementation state on top of published authority `fafd681`, and execute only the accepted R1 `runtime_execution` packet in the same or equivalent checkout that already carries that slice.
    source:
      - canon-ref:dev/kb/phase-6-r1-conversation-contracts-objects-packet-checkpoint
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:canon/docs/control-plane/implementation/packets/phase-6-r1-conversation-contracts-objects-packet
      - canon-ref:canon/docs/control-plane/core/phase-6-execution-packet-index.json
      - canon-ref:canon/packages/shared-object-schemas/run-and-source/index.mjs
      - canon-ref:canon/packages/shared-object-api/run-continuity/index.mjs
      - canon-ref:canon/packages/environment-control-contracts/run-launch/index.mjs
      - canon-ref:canon/packages/context-compiler-contracts/admitted-basis/index.mjs
      - canon-ref:canon/packages/model-gateway-contracts/chat-turn/index.mjs
      - canon-ref:canon/packages/event-provenance-contracts/run-lineage/index.mjs
    supersedes:
      - CF-0079
    related:
      - P08
    next_action: Execute only `pkt.phase6-r1-conversation-runtime-execution-packet.v1` in the same writable `Canon` checkout or an equivalent checkout that already carries the local `contracts_objects` slice; do not widen to `surface_validation`, `R2`, or renewed engine-seam work.

  - id: CF-0081
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: P08
    topic: process
    summary: The accepted R1 `runtime_execution` packet is now complete locally in the writable `Canon` checkout as five whitelisted `services/` and `workers/` runtime catalogs over the earlier local `contracts_objects` slice, so the next bounded Canon step is `pkt.phase6-r1-conversation-surface-validation-packet.v1`.
    impact: Future sessions should recover `canon-ref:dev/kb/phase-6-r1-conversation-runtime-execution-packet-checkpoint`, treat the local `Canon/packages/`, `Canon/services/`, and `Canon/workers/` roots as unpublished implementation state on top of published authority `fafd681`, and execute only the accepted R1 `surface_validation` packet in the same or equivalent checkout that already carries those slices.
    source:
      - canon-ref:dev/kb/phase-6-r1-conversation-runtime-execution-packet-checkpoint
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:canon/docs/control-plane/implementation/packets/phase-6-r1-conversation-runtime-execution-packet
      - canon-ref:canon/docs/control-plane/implementation/packets/phase-6-r1-conversation-surface-validation-packet
      - canon-ref:canon/docs/control-plane/implementation/release-blueprints/r1-conversation-blueprint
      - canon-ref:canon/tests/contracts/module-boundary.contracts.json
      - canon-ref:canon/services/environment-shell-api/conversation-entry/index.mjs
      - canon-ref:canon/services/execution-control/run-dispatch/index.mjs
      - canon-ref:canon/services/model-gateway/chat-turn-execution/index.mjs
      - canon-ref:canon/services/event-provenance/run-trace/index.mjs
      - canon-ref:canon/workers/context-compiler/compile-run-context/index.mjs
    supersedes:
      - CF-0080
    related:
      - P08
    next_action: Execute only `pkt.phase6-r1-conversation-surface-validation-packet.v1` in the same writable `Canon` checkout or an equivalent checkout that already carries the local `contracts_objects` plus `runtime_execution` slices; do not widen to `R2` or renewed engine-seam work.

  - id: CF-0082
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: P08
    topic: process
    summary: Baton continuation is intentionally stopped by explicit user instruction after local completion of the accepted R1 `runtime_execution` packet; the next bounded step remains `pkt.phase6-r1-conversation-surface-validation-packet.v1`, but no successor should start until the user explicitly resumes work.
    impact: Future sessions must treat the R1 `surface_validation` packet as the next bounded step while keeping the queue paused, leaving `Baton state` at `stop`, and refusing automatic same-runner continuation until an explicit user resume instruction is given.
    source:
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:dev/kb/phase-6-r1-conversation-runtime-execution-packet-checkpoint
      - canon-ref:dev/baton/baton-protocol
      - local thread instruction on 2026-04-18: "Stop the baton flow before anything else"
    supersedes:
      - CF-0081
    related:
      - P08
    next_action: Keep the baton stopped until the user explicitly resumes work; on resume, recover `canon-ref:dev/kb/phase-6-r1-conversation-runtime-execution-packet-checkpoint` and execute only `pkt.phase6-r1-conversation-surface-validation-packet.v1` in the same or equivalent writable implementation checkout.

  - id: CF-0083
    date: 2026-04-18
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The 2026-04-18 move from the closed post-reopen engine seam into Phase 6 implementation continuation was a local inference error from pre-existing Phase 6 modeling docs, not a new higher-authority Canon reopen event.
    impact: Future sessions must restore the live boundary to the closed post-reopen seam pause, treat accepted Phase 6 future-root modeling under `Canon` as non-authorizing by default while `Canon` remains the accepted authority/control-plane repo for now, and keep the local `Canon/packages/`, `Canon/services/`, and `Canon/workers/` code on disk only as quarantined draft state for possible later ratification or reuse outside the live next-step plan.
    source:
      - archive/gpt5_browser_packet/_canon_registry/operator-final-verdict.md
      - archive/gpt5_browser_packet/_canon_registry/what-wait-means-now.md
      - CANON_PROJECT_CONTEXT.md
      - Canon/README.md
      - Canon/docs/control-plane/core/codebase-current-state.json
      - Canon/docs/control-plane/AGENTS.md
      - Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md
      - Canon/docs/control-plane/implementation/release-blueprints/r1-conversation-blueprint.md
      - Canon/docs/control-plane/core/phase-6-execution-packet-index.json
      - canon-ref:dev/kb/phase-6-r1-conversation-entry-checkpoint
      - canon-ref:dev/canon-now
    supersedes:
      - CF-0079
      - CF-0080
      - CF-0081
      - CF-0082
    related:
      - P08
    next_action: Keep `Baton state` at `stop`, do not resume Phase 6 packet execution by default, and reopen work only if later accepted Canon authority or a cited contradiction actually reopens the boundary or the user explicitly chooses another bounded task.

  - id: CF-0084
    date: 2026-04-18
    status: active
    kind: outcome
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Accepted Canon authority now explicitly states that future-root modeling and packet order are non-authorizing until a later accepted artifact changes reserved roots to materialized, so the earlier Phase 6 boundary ambiguity is closed at the source.
    impact: Future sessions can recover the stop boundary directly from accepted Canon README plus the accepted repo/package pack, current-state view, and execution-packet index without relying on local corrective inference; no further authority-repair step remains open in Canon Dev, and the local `Canon/packages/`, `Canon/services/`, and `Canon/workers/` code remains quarantined draft state for possible later ratification or reuse.
    source:
      - Canon/README.md
      - Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md
      - Canon/docs/control-plane/core/codebase-current-state.json
      - Canon/docs/control-plane/core/phase-6-execution-packet-index.json
      - Canon/docs/control-plane/core/master-plan.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-phase-4-plus-plan
    supersedes: []
    related:
      - P08
    next_action: Choose only an explicit bounded task when work resumes; keep Phase 6 packet continuation stopped by default unless later accepted Canon authority or a cited contradiction changes the boundary.

  - id: CF-0085
    date: 2026-04-18
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The user explicitly chose a different bounded task: finish `agentic-engine` honestly and prepare the next-repo handoff through a one-step-per-session recovery plan rooted at `agentic-engine-finish-session-plan.md`.
    impact: Future sessions may work `agentic-engine` again without reopening the closed Canon Phase 6 seam, but they must execute exactly one numbered session from the root plan per thread, keep clean-room claims tied to fresh checkouts, and stop to ask the user whenever the plan marks a dependency as `User action required`.
    source:
      - agentic-engine-finish-session-plan.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
      - canon-ref:engine/CONTEXT.md
      - canon-ref:dev/kb/canon-phase-4-plus-plan
    supersedes: []
    related:
      - P08
    next_action: Execute Session 1 from `agentic-engine-finish-session-plan.md` and do not chain later sessions in the same thread.

  - id: CF-0086
    date: 2026-04-18
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Session 1 of the `agentic-engine` finish plan proved that current HEAD `06bc935` already closes the old Phase 3 branch-side blocker through the landed `8c1f4f2` variant-lineage and variant-diff slice, and the stale Prompt 8 note is now explicitly historical.
    impact: Future sessions should treat Phase 3 as closed for the engine-owned scope in `agentic-engine`, recover the current repo truth from the new current-HEAD checkpoint note, and move directly to clean-checkout CI honesty without reopening Canon Phase 6 work.
    source:
      - agentic-engine-finish-session-plan.md
      - agentic-engine/docs/phase-3-prompt-8-carry-forward.md
      - agentic-engine/docs/phase-3-current-head-checkpoint.md
      - agentic-engine/docs/spec-digests/phase-3-branch-replay.md
      - agentic-engine/README.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P08
    next_action: Execute Session 2 from `agentic-engine-finish-session-plan.md` in a clean copy or equivalent fresh checkout and make the CI path honest without widening into packaging.

  - id: CF-0087
    date: 2026-04-18
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Session 2 of the `agentic-engine` finish plan is complete: current HEAD now has an honest clean-checkout CI path, the README points local CI invocation at `pnpm run ci` instead of PNPM's reserved `ci` command, and `agentic-engine/docs/clean-checkout-ci-checkpoint.md` records the fresh-clone proof.
    impact: Future sessions should treat the clean-room CI contradiction as closed at current HEAD, recover the exact proof surface from the new checkpoint note, and move directly to Session 3 packaging truth without reopening Canon Phase 6 work.
    source:
      - agentic-engine-finish-session-plan.md
      - agentic-engine/package.json
      - agentic-engine/.github/workflows/ci.yml
      - agentic-engine/tests/cross-repo-contracts.test.ts
      - agentic-engine/README.md
      - agentic-engine/docs/clean-checkout-ci-checkpoint.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P08
    next_action: Execute Session 3 from `agentic-engine-finish-session-plan.md` and make packaging behavior explicit and reproducible without widening into boundary or release-closure work.

  - id: CF-0088
    date: 2026-04-18
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Session 3 of the `agentic-engine` finish plan is complete: current HEAD now proves an explicit self-building packaging rule via per-workspace `prepack`, representative copied unbuilt surface-package and worker pack probes pass cleanly, and `agentic-engine/docs/packaging-truth-checkpoint.md` records the repo-local proof.
    impact: Future sessions should treat the clean-pack contradiction as closed at current HEAD, recover the exact proof surface from the new checkpoint note, and move directly to Session 4 boundary and consumer proof without reopening Canon Phase 6 work.
    source:
      - agentic-engine-finish-session-plan.md
      - agentic-engine/packages/core/package.json
      - agentic-engine/workers/tool-sandbox/package.json
      - agentic-engine/tests/build-package-cleanliness.test.ts
      - agentic-engine/tests/packaging-test-utils.ts
      - agentic-engine/docs/packaging-truth-checkpoint.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P08
    next_action: Execute Session 4 from `agentic-engine-finish-session-plan.md` and tighten boundary and consumer proof without widening into broad downstream integration or release-closure work.

  - id: CF-0089
    date: 2026-04-18
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Session 4 of the `agentic-engine` finish plan is complete: current HEAD already proves the forbidden-dependency boundary guard across the root plus every public workspace manifest, and the packed external-consumer harness exercises representative runtime behavior for core, replay/provenance, and worker entry surfaces.
    impact: Future sessions should treat the two medium audit gaps as closed at current HEAD, recover the exact proof surface from the new checkpoint note, and move directly to Session 5 release-closure truth without reopening Canon Phase 6 work or widening into broad downstream integration.
    source:
      - agentic-engine-finish-session-plan.md
      - agentic-engine/tests/cross-repo-contracts.test.ts
      - agentic-engine/tests/external-consumer-packaging.test.ts
      - agentic-engine/docs/boundary-and-consumer-proof-checkpoint.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P08
    next_action: Execute Session 5 from `agentic-engine-finish-session-plan.md` and close release truth with one durable engine-closure checkpoint, explicit audit finding disposition, and honest remaining-limit wording.

  - id: CF-0090
    date: 2026-04-18
    status: active
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Session 5 of the `agentic-engine` finish plan is complete: current HEAD now has a durable engine-closure checkpoint that reconciles the deep release audit against the landed Session 2-4 proof surfaces, keeps the README wording aligned with that closure truth, and records the remaining limits honestly.
    impact: Future sessions should treat the five release-audit findings as closed at current HEAD, recover the exact repo-local closure truth from `agentic-engine/docs/engine-closure-checkpoint.md`, and move directly to Session 6 next-repo handoff work without reopening Canon Phase 6 or re-auditing already-closed engine findings.
    source:
      - agentic-engine-finish-session-plan.md
      - agentic-engine/docs/engine-closure-checkpoint.md
      - agentic-engine/README.md
      - agentic-engine/docs/clean-checkout-ci-checkpoint.md
      - agentic-engine/docs/packaging-truth-checkpoint.md
      - agentic-engine/docs/boundary-and-consumer-proof-checkpoint.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P08
    next_action: Execute Session 6 from `agentic-engine-finish-session-plan.md` and prepare the next repo handoff from `agentic-engine/docs/engine-closure-checkpoint.md`, including the bounded check for whether a local shared-environment checkout exists.

  - id: CF-0091
    date: 2026-04-18
    status: blocked
    kind: handoff
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Session 6 of the `agentic-engine` finish plan is complete: `shared-environment` is confirmed as the next Layer 2 repo above `agentic-engine`, `shared-environment-starter-packet.md` records the bounded starter handoff, and no local `shared-environment` checkout exists in this workspace yet.
    impact: Future sessions should keep the Canon baton stopped, use `shared-environment-starter-packet.md` as the next-repo recovery packet once a checkout exists, and not widen into Canon Phase 6 draft roots or abstract shared-environment planning without a real repo checkout.
    source:
      - agentic-engine-finish-session-plan.md
      - agentic-engine/CONTEXT.md
      - agentic-engine/docs/engine-closure-checkpoint.md
      - Canon/docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md
      - shared-environment-starter-packet.md
      - canon-ref:dev/canon-now
      - canon-ref:dev/kb/canon-tasks
    supersedes: []
    related:
      - P01
      - P02
      - P03
    next_action: Provide the next repo checkout path or clone the shared-environment repo into this workspace so the next bounded session can start from a real checkout instead of planning in the abstract.

  - id: CF-0092
    date: 2026-04-19
    status: active
    kind: supersession
    stage: phase-4-execution
    packet: none
    topic: process
    summary: The 2026-04-18 agentic-engine paranoia audit (`AGENTIC_ENGINE_AUDIT_LOG.md`, 506 findings: 15 CRITICAL, 130 HIGH, 208 MEDIUM, 123 LOW, 30 INFO) plus `CANON_PLAN_IMPACT_REPORT.md` (74 of 145 CRITICAL+HIGH findings require plan-owner action across 14 ARCHITECTURE-CHANGE, 25 RELEASE-GATE-IMPACT, 4 SCOPE-EXPANSION, 5 SCOPE-CONTRACTION, 26 PLAN-CONSTRAINT-CHANGE; 22 concrete plan over-claims in Section 5; 12 plan-owner decisions in Section 6) constitute a cited-contradiction reopen event under `canon-ref:dev/kb/canon-phase-4-plus-plan` §157 and open Phase-4+ plan step 20. This supersedes CF-0074's "reopened post-reopen engine seam locally closed" claim because the frozen context does not enforce cross-package determinism or snapshot integrity per audit findings PKG-PROV-001/002/004 and OWN-001/008; the event is a cited-contradiction reopen, not a baseline invalidation, so Inherited Baseline items 1-10 in the Phase-4+ plan remain carry-forward substrate truth.
    impact: Ordinary baton continuation is durably stopped. Future sessions must treat Phase-4+ plan step 20 as the live open step, must not emit a successor packet, must not resume Phase 6 packet execution from the quarantined `Canon/packages/`, `Canon/services/`, or `Canon/workers/` roots, and must not advance the reopened engine posture until the twelve plan-owner decisions from `CANON_PLAN_IMPACT_REPORT.md` Section 6 are recorded. The twelve pending decisions are (1) Clock/TimeProvider abstraction ownership, (2) credentialScope enforcement path, (3) ToolSandbox isolation reconciliation and `ToolSandboxWorker` IPC export, (4) policy matcher (pattern vs strict-equals), (5) `stableStringify` unification into `@canon/engine-core`, (6) LICENSE and engine version direction (0.0.0 vs 0.1.0 + semver), (7) Platform Gate truth-status (reopen vs retain `passed` with footnotes), (8) intra-workspace peerDependency carve-out, (9) replay-compare diff-semantics (id-aligned vs positional), (10) successor checkpoint for frozen-posture sufficiency acknowledged, (11) quarantined-draft fate under `Canon/packages/`, `Canon/services/`, and `Canon/workers/`, and (12) R3/R6/R7 prerequisite wording for Clock plus tool-gateway hardening. Minimum-next-step per `canon-ref:dev/kb/post-reopen-audit-cited-contradiction-checkpoint` is plan-owner decisions on items 1, 2, and 7.
    source:
      - AGENTIC_ENGINE_AUDIT_LOG.md
      - CANON_PLAN_IMPACT_REPORT.md
      - canon-ref:dev/kb/canon-phase-4-plus-plan
      - canon-ref:dev/kb/post-reopen-audit-cited-contradiction-checkpoint
      - canon-ref:dev/canon-now
    supersedes:
      - CF-0074
    related:
      - P04
      - P09
      - P12
      - P13
    next_action: No further execution inside this session. Baton stopped pending audit-cited-contradiction reopen at Phase-4+ plan step 20. Future sessions reading this ledger should consult `canon-ref:dev/kb/post-reopen-audit-cited-contradiction-checkpoint` before acting and should record plan-owner decisions for the twelve items in `CANON_PLAN_IMPACT_REPORT.md` Section 6 before attempting any bounded continuation.
```

  - id: CF-0093
    date: 2026-04-23
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Plan-owner recorded accepted decisions for the three minimum-next post-reopen conditions named in `canon-ref:dev/kb/post-reopen-audit-cited-contradiction-checkpoint`. Condition (a) = Option A (engine owns `Clock` interface in `packages/core/src/clock.ts`; Shared Env supplies production impl; `systemClock` default; `DeterministicClock` test utility; lint rule forbids wall-clock calls outside `clock.ts`). Condition (b) = Option A across all three sub-decisions (B-1 engine owns `CredentialProvider` + hardened `validateCredentialScope` against prototype pollution and X-057; B-2 `spawnToolSandboxWorker` forks a real Node child, in-process primitive renamed `InProcessToolRunner`, Platform Gate §6 PG-10 gains explicit process-boundary clause; B-3 `attachToolSandboxWorkerIpc` and IPC message types re-exported from `workers/tool-sandbox/src/index.ts` and added to `contracts/exports.json`). Condition (f) = Option A (formal reopen of Platform Gate acceptance; add sub-gates PG-01.1, PG-07.1, PG-10.1; preserve prior `passed` as append-only history; sync footnotes across downstream Canon docs; `post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint` formally superseded by `post-reopen-audit-cited-contradiction-checkpoint`). Decision records live at `canon-knowledgebase/post-reopen-decisions/condition-{a,b,f}.md`.
    impact: `pkt.remediate-clock-timeprovider.v1`, `pkt.remediate-thaw-timestamp-authority.v1`, `pkt.remediate-localecompare-sort-paths.v1`, `pkt.remediate-credentialscope-enforcement.v1`, `pkt.remediate-toolsandboxworker-fork.v1`, and `pkt.remediate-platform-gate-truth-status.v1` are authorized for execution. `pkt.remediate-frozenat-in-hashed-doc.v1` is partially authorized pending the separate frozenAt hash-inclusion sub-decision. Platform Gate remediation packet goes FIRST under Option A (documents the reopened posture before engine remediation lands). Baton state remains `stop — audit-reopen hold` at the global level because the other 9 reopen conditions ((c) policy-matcher, (d) stableStringify, (e) LICENSE + engine version, (g) intra-workspace peerDependency, (h) replay-compare diff-semantics, (i) successor checkpoint acknowledgement, (j) Canon quarantine status, plus frozenAt hash-inclusion sub-decision and LICENSE sub-decisions) remain open, but scope is now explicitly carved out for the six authorized remediation packets above. Remediation will execute autonomously via `@droid`-tagged issues on SaintFreddy/agentic-engine and SaintFreddy/Canon, pinned to `claude-opus-4-7 -r high`, with auto-review and human-merge gating. Platform Gate spec retains both `passed` (historical) and `reopened` (live) markers per Option A.
    source:
      - canon-knowledgebase/post-reopen-decisions/condition-a.md
      - canon-knowledgebase/post-reopen-decisions/condition-b.md
      - canon-knowledgebase/post-reopen-decisions/condition-f.md
      - canon-ref:dev/kb/post-reopen-audit-cited-contradiction-checkpoint
      - canon-ref:dev/canon-now
      - CANON_PLAN_IMPACT_REPORT.md
      - AGENTIC_ENGINE_AUDIT_LOG.md
    supersedes: []
    related:
      - P04
      - P09
    next_action: Open `[remediation]` issues tagged `@droid` on SaintFreddy/Canon for `pkt.remediate-platform-gate-truth-status.v1` (first; control-plane only) and on SaintFreddy/agentic-engine for `pkt.remediate-clock-timeprovider.v1`, `pkt.remediate-credentialscope-enforcement.v1`, and `pkt.remediate-toolsandboxworker-fork.v1` (parallel wave A.1 + B.1 + B.2) once the Platform Gate reopen markup has landed on main. Coupled follow-on packets (thaw, localeCompare, frozenAt) land after wave A.1 and their respective sub-decisions. Address the remaining 9 reopen conditions via `post-reopen-decision-brief` skill drafts in the next batch.

  - id: CF-0094
    date: 2026-04-23
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: process
    summary: Plan-owner set a standing delegation rule in `canon-now.md` ("always choose recommended unless project-direction implications") and under that rule the agent recorded accepted decisions for seven additional reopen conditions, leaving only (e.2) LICENSE and (j) Canon quarantined-draft fate as escalated. Recorded decisions (all Option A per `CANON_PLAN_IMPACT_REPORT.md` Section 6 defaults): (c) engine ships typed `RulePattern` with glob/regex and explicit matcher at Platform Gate; (d) canonical `stableStringify` in `@canon/engine-core` with cross-package determinism test, drift-detector not needed; (e.1) engine workspace bumps to `0.1.0` with breaking-change protocol tied to spec-digest regeneration; (g) `phase-6-repo-package-architecture §6.1` amended to carve out intra-workspace peer-dependencies while preserving "zero external runtime dependencies"; (h) replay-compare adds `diffByStableId()` as production path with positional diff retained and JSDoc-warned; (i) `post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint` formally superseded by `post-reopen-audit-cited-contradiction-checkpoint` via header markup (absorbed into Platform Gate packet); frozenAt hash-inclusion sub-decision accepted as "inside the hashed compiled-context document, sourced from injected Clock." Four new remediation packet scaffolds added to `SaintFreddy/Canon` on 2026-04-23 (merged PR #9): `pkt.remediate-policy-matcher.v1`, `pkt.remediate-engine-version-0.1.0.v1`, `pkt.remediate-peerdep-carveout.v1`, `pkt.remediate-replay-compare-diff-semantics.v1`.
    impact: Ten remediation packets are now authorized (see `canon-now.md` "Authorized remediation packets" list): six engine packets on `SaintFreddy/agentic-engine` (Clock, thaw, localeCompare, frozenAt, credentialScope, ToolSandboxWorker fork, stableStringify, policy-matcher, engine-version, replay-compare) and two Canon control-plane packets (Platform Gate truth-status, peerDependency carve-out). Only LICENSE and Canon-quarantine decisions remain gating. Baton state remains `stop — audit-reopen hold (scope-carved)` because (e.2) and (j) are still open and touch project-direction. Execution proceeds via `@droid`-tagged issues on the two GitHub repos pinned to Opus 4.7 high-reasoning; ordering gate: Platform Gate reopen PR (Canon #8) lands first, then engine and Canon wave-D packets parallelize; Clock-dependent packets (thaw, localeCompare, frozenAt) wait for Clock PR to land. This entry is a decision-class entry and does not supersede CF-0092 or CF-0093; it extends them.
    source:
      - canon-knowledgebase/post-reopen-decisions/condition-c.md
      - canon-knowledgebase/post-reopen-decisions/condition-d.md
      - canon-knowledgebase/post-reopen-decisions/condition-e-engine-version.md
      - canon-knowledgebase/post-reopen-decisions/condition-g.md
      - canon-knowledgebase/post-reopen-decisions/condition-h.md
      - canon-knowledgebase/post-reopen-decisions/condition-i.md
      - canon-knowledgebase/post-reopen-decisions/frozenat-hash-inclusion.md
      - canon-ref:dev/canon-now
      - CANON_PLAN_IMPACT_REPORT.md
      - AGENTIC_ENGINE_AUDIT_LOG.md
    supersedes: []
    related:
      - P04
      - P05
      - P09
    next_action: Open `@droid` remediation issues on `SaintFreddy/agentic-engine` for the four independently-executable engine packets (stableStringify, policy-matcher, engine-version-0.1.0, replay-compare-diff-semantics) and on `SaintFreddy/Canon` for peerDependency carve-out (doc-only). Leave Clock-dependent engine packets (thaw, localeCompare, frozenAt) queued until the Clock PR lands. Prompt plan-owner SaintFreddy for explicit decisions on (e.2) LICENSE choice and (j) Canon quarantined-draft fate.

  - id: CF-0095
    date: 2026-04-24
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: legal-posture
    summary: Plan-owner SaintFreddy recorded DEC-RO-04 for condition (e.2) LICENSE choice = Proprietary / All Rights Reserved across all 5 repos (Canon, agentic-engine, canon-apps, shared-environment, agentic-engine-history). Decision rejected Option 1 MIT, Option 2 Apache-2.0, and Option 3 BSL. Chose Option 4 because it maximises commercial flexibility during 0.1.0, preserves later reversal to any license, and avoids granting rights that must then be honored. Public-SDK aspiration phrased in `AGENTIC_WORKFLOW.md §9 L426` is withdrawn for 0.1.0 and must be reconciled by the LICENSE remediation packet. Full record at `canon-knowledgebase/post-reopen-decisions/condition-e-license.md`.
    impact: Authorizes `pkt.add-proprietary-license.v1` which will (i) add a Proprietary LICENSE file of the exact form specified in the decision record to each of the 5 repo roots, (ii) update `AGENTIC_WORKFLOW.md §9` to either mark public-SDK posture as aspirational / not current or remove that phrasing entirely (packet surfaces both variants for plan-owner selection), (iii) append a row to `CANON_PLAN_IMPACT_REPORT.md §6 row 6` noting DEC-RO-04 landed on Option 4. This is the last remaining LICENSE-gated action; no other packets were blocked purely on (e.2). Revisit conditions named in the decision record: 1.0 milestone, external partnership triggering specific license posture, or plan-owner electing OSS for community growth.
    source:
      - canon-knowledgebase/post-reopen-decisions/condition-e-license.md
      - canon-ref:dev/canon-now
      - CANON_PLAN_IMPACT_REPORT.md
      - AGENTIC_WORKFLOW.md
    supersedes: []
    related:
      - CF-0094
    next_action: Author packet scaffold `pkt.add-proprietary-license.v1` in `SaintFreddy/Canon/docs/control-plane/implementation/packets/remediation/`, open `@droid`-tagged remediation issue, and merge resulting PRs across all 5 repos.

  - id: CF-0096
    date: 2026-04-24
    status: active
    kind: decision
    stage: phase-4-execution
    packet: none
    topic: repo-structure
    summary: Plan-owner SaintFreddy recorded DEC-RO-05 for condition (j) Canon quarantined-draft fate = Delete, executed in two sequenced packets under correctness-first discipline. Packet A (`pkt.quarantine-invariant-sweep.v1`) extracts every `invariants: Object.freeze([...])` array from the 11 `.mjs` contract-as-code files under `Canon/packages/`, `Canon/services/`, `Canon/workers/` (1,369 total LOC, zero inbound imports, zero overlap with control-plane artifact-registry ref names), identifies the matching spec digest for each invariant's subject domain, and appends any NOT already captured as one-liners under a clearly-labelled "Invariants (from quarantined pre-reopen contract catalogs)" subsection with origin-file attribution. Packet A does no deletion. Packet B (`pkt.quarantine-delete.v1`) is hard-gated on Packet A landing; it `git rm -r`'s the 3 directories and reconciles `docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md` + `docs/control-plane/core/master-plan.md` prose that still expects Canon to host packages/services/workers. Decision rejected Preserve (slow rot) and Advance (weeks of redundant contract re-authoring in an abandoned mjs format). Full record at `canon-knowledgebase/post-reopen-decisions/condition-j.md`.
    impact: Unblocks the final two reopen-gating packets. All 12 reopen-resolution conditions are now RECORDED; no escalated decisions remain. Git history preserves the 1,369 LOC of contract-as-code for future archaeology. Canon repo becomes structurally control-plane + authority only, matching its post-reopen identity. `post-reopen-remediation` skill will enforce the two-packet ordering gate: Packet B's issue body cites Packet A's merged PR as a prerequisite and the skill blocks execution if Packet A hasn't landed.
    source:
      - canon-knowledgebase/post-reopen-decisions/condition-j.md
      - canon-ref:dev/canon-now
      - CANON_PLAN_IMPACT_REPORT.md
    supersedes: []
    related:
      - CF-0094
      - CF-0095
    next_action: Author packet scaffolds `pkt.quarantine-invariant-sweep.v1` and `pkt.quarantine-delete.v1` in `SaintFreddy/Canon/docs/control-plane/implementation/packets/remediation/`. Open Packet A's `@droid` issue first. Open Packet B's issue only after Packet A's PR has merged to main.
