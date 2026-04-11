# Phase 1 surface and release topology canon
Version: 1.0
Status: Accepted
Task: P1.4 — Surface and release topology canon
Artifact ID: canon.phase1-surface-release-topology.v1
Canon scope: Accepted topology story for Platform Gate, R1-R7, Task Studio handoff, surfaces, modes, and cross-app handoff rules

## 1. Purpose

This artifact fixes one accepted topology story for the platform.

It exists to:

- define how Platform Gate, R1-R7, and Task Studio relate as one path,
- clarify which surfaces matter at each stage,
- make continuity and handoff rules explicit,
- prevent release-by-release topology drift.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- Platform Gate placement,
- R1-R7 release topology,
- Task Studio handoff topology,
- surface roles,
- mode/projection rules,
- cross-app handoff rules.

### Out of scope

- detailed schema design,
- field-level surface contracts,
- runtime topology,
- repo/package layout,
- implementation sequencing inside one release.

## 3. Topology principles

### 3.1 One substrate, many projections

All public releases and Task Studio project the same underlying substrate.
No release owns a separate backend truth model.

### 3.2 Consequence stays run-native

Runs remain the primary consequential unit across the full path.
Threads, branches, artifacts, prompt assets, applets, and commissions may anchor continuity differently at different stages, but they do not replace run consequence.

### 3.3 Continuity shifts by stage

- Early chat releases foreground thread continuity.
- Branching releases foreground branch/replay continuity.
- Artifact Workspace shifts visible continuity toward artifacts.
- Commissioning Bridge foregrounds commission/contract preflight.
- Task Studio foregrounds commissioned-work surfaces.

### 3.4 Modes are projections, not products

Notebook, debate, research, architect, executive-summary, graph, and similar modes are alternate projections over shared objects.
They are not separate ontologies or separate backends.

### 3.5 Handoffs preserve identity

Cross-app movement must preserve the identity of runs, artifacts, branches, proof, deltas, and writeback proposals.
Handoffs change the surface, not the meaning-bearing object.

## 4. Release path topology

| Stage | Primary surface center | Continuity center | What the stage proves | Handoff rule |
| --- | --- | --- | --- | --- |
| Platform Gate | Internal gate and audit surfaces | Frozen context + source/run/provenance identity | The substrate is not transcript-dependent before public launch | No public launch work may bypass this gate |
| R1 Transcript Chat | Conversation Surface + compact run/source inspection | Thread-assisted run continuity | Chat can feel familiar while still returning bounded runs with context snapshots and source grounding | Assistant turns are outputs of runs, not truth anchors |
| R2 Context Chat | Conversation Surface + full context/evidence drawer | Run continuity with explicit pack control | Users can inspect and shape evidence/context instead of trusting hidden assembly | Packs move with the run rather than staying transcript-only |
| R3 Branch / Visual Thinker | Branch map, compare, replay, mode projections | Branch/replay continuity around runs and checkpoints | Alternate lines of work become semantic and replayable | Branching forks assumptions, packs, strategy, or outputs, not just transcripts |
| R4 Artifact Workspace | Artifact workspace, focal artifact lens, proposal inbox | Artifact-centered continuity over run history | Continuity moves out of transcript gravity and into governed artifacts | Runs attach to focal artifacts and emit proposals/deltas instead of silent mutation |
| R5 Prompt Studio | Prompt asset browser, prompt card/adaptation views | Prompt artifact lineage continuity | Prompt assets become governed, versioned artifacts on the same substrate | Prompt assets remain assets, not substitutes for Protocol/Applet semantics |
| R6 Governed Agent / Applet Chat | Chatlet/apply settings surfaces, queue/inbox | Reusable execution continuity via Protocol/Applet/Workflow objects | Governed reuse and bounded autonomy become real without replacing shared primitives | Applets and background runs preserve the same run/proof/delta/writeback semantics |
| R7 Commissioning Bridge | Commission card, contract draft, preflight, live monitor, ledger | Commission/Contract continuity into explicit run governance | Serious work inside chat becomes explicit commissioning | Chat-to-Run handoff must preserve commission, contract, authority, proof, delta, and writeback identity |
| Task Studio | Commissioning surfaces, result canvas, proof ledger, delta/writeback panels | Commissioned-work continuity centered on Commission -> Run -> Artifact | The north-star app becomes the primary commissioned-work projection | The move from R7 to Task Studio is a projection change, not an ontology translation |

## 5. Surface canon

### 5.1 Shared projection grammar surfaces

These shared surface grammars are reused across the topology:

- Composer
- Canvas
- Inspector
- Browser / Library
- Timeline
- Ledger
- Compare View
- Queue / Inbox
- Board
- Diff / Merge View
- Live Monitor
- Console

### 5.2 Stage-specific surface emphasis

| Stage | Surface emphasis |
| --- | --- |
| R1 | Conversation Surface, Source Chip, compact run/context inspection |
| R2 | Conversation Surface plus Context/Evidence editing surfaces |
| R3 | Branch Map, Compare View, replay views, mode projections |
| R4 | Artifact Workspace, Focal Artifact Lens, Proposal Inbox |
| R5 | Prompt artifact browser, adaptation compare, model-profile surfaces |
| R6 | Applet/agent configuration surfaces, Queue / Inbox, bounded background-run views |
| R7 | Commission preflight surfaces, Live Monitor, Proof Ledger, Delta Inspector |
| Task Studio | New Commission Sheet, Task Contract Panel, Evidence Pack Builder, Context Inspector, Strategy Board, Authority Panel, Result Canvas, Proof Ledger, Delta Inspector, Writeback Panel |

## 6. Mode and projection rules

1. Transcript Chat, Context Chat, Branch / Visual Thinker, Artifact Workspace, Prompt Studio, Governed Agent / Applet Chat, Commissioning Bridge, and Task Studio are all projections over shared primitives.
2. R3 modes such as notebook, debate, research, architect, executive-summary, and graph are alternate projections over the same branch/object graph.
3. Task Studio is an app-level projection over shared commissioned-work semantics, not a new semantic layer.
4. A surface may foreground one continuity center without taking ownership of the underlying object family.

## 7. Cross-app handoff rules

| From | To | Preserved objects | Rule |
| --- | --- | --- | --- |
| R1 Transcript Chat | R2 Context Chat | Thread/Line, Run, Source Reference, Evidence/Context state | Context control extends the same run-based work instead of starting a new ontology |
| R2 Context Chat | R3 Branch / Visual Thinker | Run, Checkpoint, Branch, Pack state, Proof basis | Branching and replay must fork semantic state, not duplicate transcript history only |
| R3 Branch / Visual Thinker | R4 Artifact Workspace | Run outputs, Branch lineage, Artifact proposals, Proof/Delta | Accepted or reviewed artifacts become the new visible continuity anchor |
| R4 Artifact Workspace | R5 Prompt Studio | Artifacts, derivation lineage, Prompt assets | Prompt assets derive from governed artifacts and preserve lineage |
| R5 Prompt Studio | R6 Governed Agent / Applet Chat | Prompt artifacts, Protocol/Applet inputs, validation context | Prompt assets may feed reusable execution but do not replace Protocol/Applet objects |
| R6 Governed Agent / Applet Chat | R7 Commissioning Bridge | Protocol/Applet context, Runs, governance state | Reusable execution must still flow into explicit commissioning semantics for serious work |
| R7 Commissioning Bridge | Task Studio | Commission, Contract, Run, Authority Scope, Proof Bundle, State Delta, Writeback Proposal, Artifact links | The handoff is a surface change into the dedicated commissioned-work app |

## 8. Topology constraints that must not drift

### 8.1 Platform Gate is mandatory

Platform Gate is not optional and is not a public release substitute.

### 8.2 Artifact Workspace is the bridge release

R4 is the point where visible continuity must move out of transcript gravity.
This is not optional.

### 8.3 Commissioning Bridge is the terminal chat release

R7 must expose explicit commissioning semantics before Task Studio becomes primary.

### 8.4 Task Studio is not a rewrite destination

Task Studio must receive the already-established semantics of commission, contract, run, proof, delta, and writeback.

## 9. Downstream implications

### 9.1 For P1.5 — Rewrite-containment / stable seam map

- Treat run/context/evidence/artifact/proof/delta/writeback identity as high-blast-radius seams.
- Treat surface swaps and mode projections as lower-blast-radius changes.

### 9.2 For P1.6 — Golden scenario corpus

- Include scenarios that walk the handoff chain from early chat through R7 into Task Studio.
- Include scenarios that verify identity preservation across branch, artifact, prompt, applet, and commissioning transitions.

### 9.3 For Phase 4 release packs

- Each release contract must fit this topology story instead of inventing a local one.

## 10. Review notes

Human review should confirm that this canon:

- gives the platform one accepted release-path story,
- keeps continuity and handoff rules explicit,
- keeps modes and releases as projections over shared primitives,
- preserves R4 and R7 as the key bridge stages,
- preserves Task Studio as the north-star handoff target rather than a rewrite destination.
