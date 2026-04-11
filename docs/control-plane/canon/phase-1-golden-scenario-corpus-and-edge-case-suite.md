# Phase 1 golden scenario corpus and edge-case suite
Version: 1.0
Status: Accepted
Task: P1.6 — Golden scenario corpus + edge-case suite
Artifact ID: canon.phase1-scenario-corpus.v1
Canon scope: Accepted scenario corpus covering major semantic pathways and known edge cases from chat-native wedge through Task Studio handoff

## 1. Purpose

This artifact defines the scenario corpus used to test whether the accepted canon actually hangs together.

It exists to:

- cover the major semantic pathways across the chat-native path and Task Studio handoff,
- make edge cases explicit before later semantic and architecture work,
- give later release, architecture, and repo work one accepted scenario baseline.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- golden-path scenarios,
- continuity-preservation scenarios,
- bridge-stage scenarios,
- edge-case and failure-pattern scenarios,
- scenario-to-seam coverage mapping.

### Out of scope

- executable test harnesses,
- fixture data files,
- UI copy tests,
- implementation-specific regression tests.

## 3. Coverage model

The corpus must cover all of the following:

1. transcript-native entry without transcript-native truth,
2. explicit context control,
3. semantic branching and replay,
4. artifact-centered continuity,
5. prompt asset lineage,
6. governed reusable execution,
7. explicit commissioning,
8. Task Studio handoff,
9. high-blast-radius edge cases that would reveal ontology drift.

## 4. Golden scenario corpus

| Scenario ID | Path | Core objects | What must stay true | Protected canon / seam |
| --- | --- | --- | --- | --- |
| `GS-01` | R1 attached-source question -> bounded answer | Thread/Line, Run, Source Reference, context snapshot | Assistant output is a run result with source grounding, not transcript truth | P1.2, P1.4, `SS-01`, `SS-02` |
| `GS-02` | R2 user edits an Evidence Pack before rerun | Run, Evidence Pack, Context Pack | Evidence/context remain separate and inspectable; rerun uses the edited pack | P1.1, P1.2, P1.4, `SS-01` |
| `GS-03` | R2 user freezes a pack and replays later | Context Pack, Run, replay input | Frozen context preserves replayability independent of later transcript state | P1.2, P1.4, `SS-01`, `SS-10` |
| `GS-04` | R3 branch from checkpoint with narrower evidence | Run, Checkpoint, Branch, Evidence Pack | Branch forks semantic state rather than cloning transcript only | P1.3, P1.4, `SS-07` |
| `GS-05` | R3 mode switch from research to debate | Branch, Mode Projection, Compare View | Mode change is a projection swap over the same branch/object graph | P1.3, P1.4, `SS-11`, `SS-15` |
| `GS-06` | R4 run against a focal artifact emits proposals | Artifact, Run, Proof Bundle, State Delta, Writeback Proposal | Artifact becomes continuity anchor while run remains the consequential unit | P1.2, P1.4, `SS-02`, `SS-03`, `SS-04` |
| `GS-07` | R4 reviewer accepts artifact writeback but rejects canon promotion | Artifact lane, Canon lane, Writeback Proposal, Approval Decision | Lane separation remains explicit and partial acceptance works | P1.2, P1.4, `SS-04`, `SS-08` |
| `GS-08` | R5 canonical prompt creates model-specific adaptations | Prompt artifact lineage, Artifact derivation links | Prompt assets remain governed artifacts with lineage, not hidden provider lore | P1.1, P1.4, `SS-13` |
| `GS-09` | R5 prompt asset reused later by governed execution | Prompt Artifact, Protocol/Applet input, Run | Prompt asset reuse does not replace Protocol/Applet ownership | P1.3, P1.4, `SS-12`, `SS-13` |
| `GS-10` | R6 successful flow saved as Protocol and installed as Applet | Protocol, Context Recipe, Strategy Preset, Verifier Pack, Applet | Reusable execution stays composed from run semantics rather than inventing a new ontology | P1.3, P1.4, `SS-12` |
| `GS-11` | R6 background run requires review in Queue/Inbox | Applet, Run, Proof Bundle, State Delta, Queue/Inbox | Background execution preserves the same governed run/proof/delta model as interactive work | P1.4, `SS-02`, `SS-08`, `SS-12` |
| `GS-12` | R7 casual request escalates into explicit Commission/Contract | Commission, Contract, Run Class, Authority Scope | Serious work becomes explicit commissioning before execution | P1.2, P1.4, `SS-05`, `SS-08` |
| `GS-13` | R7 writeback reviewed lane-by-lane before persistence | Commission, Run, Proof Bundle, State Delta, Writeback Proposal | Commissioning bridge exposes proof/delta/writeback as governable objects inside chat | P1.2, P1.4, `SS-04`, `SS-05`, `SS-08` |
| `GS-14` | R7 accepted commission opens in Task Studio | Commission, Contract, Run, Artifact, Proof Bundle | Task Studio receives an existing semantic object set; no ontology translation occurs | P1.2, P1.4, `SS-05`, `SS-09` |
| `GS-15` | Task Studio compare task from multiple sources | Commission, Contract, Evidence Pack, Run, Proof Bundle | Task Studio specializes commissioned work without owning the shared primitives underneath | P1.3, P1.4, `SS-02`, `SS-05`, `SS-09` |
| `GS-16` | Task Studio plan task branched under alternate assumptions | Contract, Branch, Strategy, Proof, Delta | Task Studio app surfaces preserve shared branch/proof semantics | P1.3, P1.4, `SS-07`, `SS-09` |

## 5. Edge-case suite

| Edge ID | Edge case | Failure pattern to catch | Protected canon / seam |
| --- | --- | --- | --- |
| `EC-01` | Transcript clone presented as branch | Transcript copy masquerades as semantic branch/replay state | P1.2, P1.4, `SS-07` |
| `EC-02` | Hidden memory changes answer after pack freeze | Frozen context is not actually frozen or memory injection is opaque | P1.1, P1.2, `SS-01` |
| `EC-03` | Artifact Workspace silently mutates durable state | Proposal/delta/writeback separation collapses into implicit mutation | P1.2, P1.4, `SS-03`, `SS-04` |
| `EC-04` | Prompt asset treated as Protocol substitute | Prompt lineage is confused with reusable execution semantics | P1.1, P1.3, `SS-12`, `SS-13` |
| `EC-05` | Applet introduces its own execution ontology | Reusable execution no longer composes from the run model | P1.3, P1.4, `SS-12` |
| `EC-06` | Commissioning Bridge omits authority or proof preflight | Serious work is still opaque inside chat | P1.2, P1.4, `SS-05`, `SS-08` |
| `EC-07` | Task Studio handoff recreates objects instead of preserving them | Task Studio becomes a rewrite destination | P1.2, P1.4, `SS-09` |
| `EC-08` | Repo/package layout is used to argue layer ownership | Storage conventions override semantic ownership | P1.3, P1.5 |
| `EC-09` | Mode-specific backend appears for one R3 mode | Projection becomes backend fragmentation | P1.2, P1.4, `SS-11` |
| `EC-10` | Run truth is attached to provider transcript state | Platform Gate assumptions fail and later replay becomes impossible | P1.4, P1.5, `SS-10` |

## 6. Coverage summary

### 6.1 By stage

- Platform Gate: `GS-03`, `EC-10`
- R1: `GS-01`
- R2: `GS-02`, `GS-03`
- R3: `GS-04`, `GS-05`, `EC-01`, `EC-09`
- R4: `GS-06`, `GS-07`, `EC-03`
- R5: `GS-08`, `GS-09`, `EC-04`
- R6: `GS-10`, `GS-11`, `EC-05`
- R7: `GS-12`, `GS-13`, `EC-06`
- Task Studio: `GS-14`, `GS-15`, `GS-16`, `EC-07`

### 6.2 By high-blast-radius seam

- `SS-01`: `GS-01`, `GS-02`, `GS-03`, `EC-02`
- `SS-02`: `GS-01`, `GS-06`, `GS-11`, `GS-15`
- `SS-03`: `GS-06`, `GS-07`, `EC-03`
- `SS-04`: `GS-07`, `GS-13`
- `SS-05`: `GS-12`, `GS-13`, `GS-14`, `GS-15`
- `SS-07`: `GS-04`, `GS-16`, `EC-01`
- `SS-09`: `GS-14`, `GS-15`, `GS-16`, `EC-07`
- `SS-10`: `GS-03`, `EC-10`

## 7. Usage rules for later work

1. Later semantic and architecture work should use this corpus to check whether a proposal preserves accepted object continuity.
2. Later release-contract work should map release requirements back to these scenarios.
3. Later repo/package work should not treat a passing implementation detail as sufficient if it breaks any protected scenario truth.

## 8. Review notes

Human review should confirm that this corpus:

- covers the major semantic pathways from the chat-native wedge through Task Studio,
- includes the key bridge stages and high-blast-radius seams,
- makes edge cases explicit rather than leaving them implicit.
