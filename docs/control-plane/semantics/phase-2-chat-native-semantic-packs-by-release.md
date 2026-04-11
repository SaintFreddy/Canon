# Phase 2 chat-native semantic packs by release
Version: 1.0
Status: Accepted
Task: P2.5 — Chat-native semantic packs by release
Artifact ID: sem.phase2-chat-native-semantic-packs.v1
Semantic scope: Accepted release-specific semantic packs for R1 Transcript Chat through R7 Commissioning Bridge

## 1. Purpose

This pack defines the semantic overlay for each public chat-native release.

It exists to:

- map each release to the shared objects it must project,
- name the release-local vocabulary that may appear without becoming a second ontology,
- lock the semantic constraints each release must preserve before Phase 4 contract packs add fuller release detail.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- semantic packs for R1 through R7,
- shared-object substrate per release,
- release-local projection vocabulary,
- per-release semantic constraints, governance/proof exposure, and handoff obligations.

### Out of scope

- Platform Gate technical gate detail,
- full release contract packs and exit criteria,
- UI copy, motion, or layout detail,
- runtime/storage/API architecture,
- Task Studio surface contracts beyond the R7 handoff seam.

## 3. Pack-wide interpretation rules

### 3.1 Shared-substrate rule

Every release pack is a projection overlay on the accepted P2.1 object model.
No release pack owns a private truth model.

### 3.2 Run-class inheritance rule

Release packs expose work through the accepted P2.2 run classes.
They may foreground some classes, but they do not add release-private execution classes.

### 3.3 Invariant inheritance rule

The accepted P2.3 governance invariants and P2.4 proof invariants bind every pack.
Release-local affordances may expose those rules differently, but they may not bypass them.

### 3.4 Projection-vocabulary rule

Release-local terms such as `Message Block`, `Span`, `Prompt Card`, or `Commission Card` are projection vocabulary only.
They may point at shared objects or object regions, but they do not replace Run, Artifact, Branch, Protocol, Commission, Proof Bundle, State Delta, or Writeback Proposal.

### 3.5 Handoff-preservation rule

Each pack must hand off shared objects to the next stage without recreating them under new identities.
Release progression is a projection shift, not an ontology translation.

## 4. Cross-pack summary

| Pack ID | Release | Continuity center | Shared-object substrate | Projection-only additions | Run-class emphasis | Protected scenarios |
| --- | --- | --- | --- | --- | --- | --- |
| `SP-R1` | Transcript Chat | Thread-assisted run continuity | Thread / Line, Run, Source Reference, Artifact, Context Pack snapshot, Proof Bundle summary | Message Block, Conversation Surface, Source Chip, Resume Packet | `synthesize`, `extract` | `GS-01`, `EC-10` |
| `SP-R2` | Context Chat | Run continuity with explicit pack control | Thread / Line, Run, Evidence Pack, Context Pack, Memory Object, Canon Object | Span, Span Set, Lens, Context Operation, Pack Diff, Pack Freeze, Starter Pack | `synthesize`, `extract`, `compare` | `GS-02`, `GS-03`, `EC-02` |
| `SP-R3` | Branch / Visual Thinker | Branch and checkpoint continuity | Run, Branch, Checkpoint, Evidence Pack, Context Pack, Proof Bundle, State Delta | Fork Policy, Mode Projection, Off-chain Job, Merge Proposal, Consensus Branch, Branch Overlay | `compare`, `plan` plus replay over all run classes | `GS-04`, `GS-05`, `EC-01`, `EC-09` |
| `SP-R4` | Artifact Workspace | Artifact-centered continuity over run history | Artifact, Run, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision | Root Artifact, Focal Artifact, Proposal, Canon Strip, Review Anchor, Alternative Artifact, Objection Artifact, Artifact Resume Packet | `transform`, `audit`, `synthesize` | `GS-06`, `GS-07`, `EC-03` |
| `SP-R5` | Prompt Studio | Prompt artifact lineage continuity | Artifact, Run, Proof Bundle, State Delta, Writeback Proposal | Prompt Artifact, Prompt Card, Model Profile, Adaptation, Adaptation Lineage, Output Target | `transform` over prompt assets | `GS-08`, `GS-09`, `EC-04` |
| `SP-R6` | Governed Agent / Applet Chat | Reusable execution continuity | Protocol, Context Recipe, Strategy Preset, Verifier Pack, Workflow, Trigger, Applet, Run, Proof Bundle, State Delta, Writeback Proposal, Assignment | Agent Profile, Starter Context Pack, Memory Policy, Contradiction Guard, Chatlet Projection | packaged use of all accepted run classes | `GS-10`, `GS-11`, `EC-05` |
| `SP-R7` | Commissioning Bridge | Commission and Contract continuity | Commission, Contract, Run Class, Authority Scope, Run, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision, Handoff | Commission Card, Contract Draft, Run Preflight, Acceptance Stack, Chat-to-Run Handoff | `triage` for intake plus contracted downstream run classes | `GS-12`, `GS-13`, `GS-14`, `EC-06`, `EC-07` |

## 5. Release-pack contracts

### 5.1 `SP-R1` — Transcript Chat

| Dimension | Contract |
| --- | --- |
| Shared substrate | Thread / Line continuity, Run, Source Reference, compact Artifact output, frozen Context Pack snapshot, Proof Bundle summary |
| Projection additions | Message Block, Conversation Surface, Source Chip, Resume Packet |
| Semantic locks | Assistant turns are outputs of Runs; transcript continuity may assist retrieval but never becomes truth; each cited chip resolves to source-bearing objects or source regions; rerun/regenerate creates a new `run_id` |
| Governance/proof exposure | Compact drawers must still reference the same Run, Context Pack snapshot, and proof basis; no answer is accepted without frozen admitted context and source grounding |
| Handoff obligation | R1 -> R2 preserves Thread / Line continuity, Run identity, Source Reference identity, and pack lineage rather than rehydrating a provider transcript |

### 5.2 `SP-R2` — Context Chat

| Dimension | Contract |
| --- | --- |
| Shared substrate | Run, Evidence Pack, Context Pack, Memory Object, Canon Object, Thread / Line continuity where present |
| Projection additions | Span, Span Set, Lens, Context Operation, Pack Diff, Pack Freeze, Starter Pack |
| Semantic locks | Evidence Pack and Context Pack remain distinct; membership reasons, inclusion/exclusion, and summarized-vs-verbatim states stay inspectable; frozen packs replay independently of later transcript state; memory/canon injection is visible and removable per run |
| Governance/proof exposure | Proof and omission handling must point back to the actual pack basis used by the Run; hidden memory drift after pack freeze is forbidden |
| Handoff obligation | R2 -> R3 preserves Run identity, pack state, proof basis, and checkpoint lineage so semantic branching forks actual state rather than transcript copies |

### 5.3 `SP-R3` — Branch / Visual Thinker

| Dimension | Contract |
| --- | --- |
| Shared substrate | Run, Branch, Checkpoint, Evidence Pack, Context Pack, Proof Bundle, State Delta |
| Projection additions | Fork Policy, Mode Projection, Off-chain Job, Merge Proposal, Consensus Branch, Branch Overlay |
| Semantic locks | Branches fork checkpoints, packs, strategy, assumptions, or outputs rather than transcripts; mode switches do not create new object identities; off-chain jobs merge back only through explicit proposals or new runs; replay and compare always create new Run/Proof/Delta records |
| Governance/proof exposure | Replay and compare views must surface task-shaped proof, omissions, contradictions, and delta state; visual diff alone is insufficient |
| Handoff obligation | R3 -> R4 preserves run outputs, branch lineage, artifact proposals, and proof/delta identity so accepted artifacts can become the next visible continuity anchor |

### 5.4 `SP-R4` — Artifact Workspace

| Dimension | Contract |
| --- | --- |
| Shared substrate | Artifact, Run, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision |
| Projection additions | Root Artifact, Focal Artifact, Proposal, Canon Strip, Review Anchor, Alternative Artifact, Objection Artifact, Artifact Resume Packet |
| Semantic locks | Artifact becomes the visible continuity anchor while Run remains the consequential unit; durable mutation always flows through proposal and lane-specific writeback objects; historical truth remains frozen per run even if the artifact changes later; alternatives and objections remain first-class artifacts, not comments |
| Governance/proof exposure | Proposal Inbox, review anchors, and canon strips must map back to Review, Approval Decision, Proof Bundle, State Delta, and Writeback Proposal objects; silent mutation is forbidden |
| Handoff obligation | R4 -> R5 preserves Artifact identity, derivation lineage, proof/delta basis, and any prompt-oriented outputs as artifact derivatives rather than private prompt-state blobs |

### 5.5 `SP-R5` — Prompt Studio

| Dimension | Contract |
| --- | --- |
| Shared substrate | Artifact lineage, Run, Proof Bundle, State Delta, Writeback Proposal |
| Projection additions | Prompt Artifact, Prompt Card, Model Profile, Adaptation, Adaptation Lineage, Output Target |
| Semantic locks | Canonical prompts and model-specific adaptations remain artifact-level derivatives with lineage and staleness state; prompt assets may feed later runs, protocols, or applets but do not replace Protocol/Applet semantics; provider-specific prompting behavior is never hidden as undocumented lore |
| Governance/proof exposure | Adaptation work follows transform-style lineage and validation expectations; staleness and derivation status remain explicit and reviewable |
| Handoff obligation | R5 -> R6 preserves prompt-asset lineage, reusable execution inputs, and validation context without collapsing prompt assets into reusable execution identity |

### 5.6 `SP-R6` — Governed Agent / Applet Chat

| Dimension | Contract |
| --- | --- |
| Shared substrate | Protocol, Context Recipe, Strategy Preset, Verifier Pack, Workflow, Trigger, Applet, Run, Proof Bundle, State Delta, Writeback Proposal, Assignment |
| Projection additions | Agent Profile, Starter Context Pack, Memory Policy, Contradiction Guard, Chatlet Projection |
| Semantic locks | Reusable execution composes from accepted run classes and Protocol/Applet objects; background runs emit the same Run/Proof/Delta/Writeback objects as interactive work; memory and contradiction policies constrain reuse but do not create new truth objects; applet settings may narrow behavior but may not widen authority silently |
| Governance/proof exposure | Queue / Inbox, approval gates, and failure handling must surface the same proof, delta, and writeback semantics required elsewhere; applets cannot bypass verifier slots or lane separation |
| Handoff obligation | R6 -> R7 preserves protocol/applet context, governance state, and run lineage while escalating serious work into explicit Commission and Contract objects |

### 5.7 `SP-R7` — Commissioning Bridge

| Dimension | Contract |
| --- | --- |
| Shared substrate | Commission, Contract, Run Class, Authority Scope, Run, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision, Handoff |
| Projection additions | Commission Card, Contract Draft, Run Preflight, Acceptance Stack, Chat-to-Run Handoff |
| Semantic locks | Serious work escalates into explicit Commission/Contract semantics before consequential execution; authority remains separate from strategy; lane-by-lane writeback remains explicit inside chat; `triage` is the intake class, not a private bridge ontology; chat-to-run handoff preserves shared IDs into Task Studio |
| Governance/proof exposure | Preflight, live monitoring, proof ledger, and delta inspection must expose shared Authority Scope, Proof Bundle, State Delta, and Writeback Proposal objects directly; no serious run may bypass proof or authority preflight |
| Handoff obligation | R7 -> Task Studio preserves Commission, Contract, Run, Authority Scope, Proof Bundle, State Delta, Writeback Proposal, and Artifact links as the exact handoff payload |

## 6. Cross-pack anti-drift rules

1. No pack may replace shared objects with view-local equivalents.
2. No pack may hide authority, proof, delta, or writeback behind transcript, artifact, prompt, or applet convenience language.
3. Prompt assets, Applets, and Commission Cards are additive projections over accepted objects, not substitute roots of truth.
4. A release may foreground a new continuity center without demoting Runs as the primary consequential unit.
5. The R4 and R7 bridge points remain mandatory semantic seam changes and may not be optimized away.

## 7. Downstream implications

### 7.1 For P2.6

- projection grammar contracts should map shared surfaces onto these semantic packs rather than inventing per-release metaphors from scratch.

### 7.2 For Phase 4 release contract packs

- each release contract should extend exactly one semantic pack from this artifact and add release promise, package maturity, and exit criteria without revising the underlying semantics.

### 7.3 For Phase 5 and Task Studio

- reusable execution, proof surfaces, and the R7 -> Task Studio bridge should deepen these pack contracts rather than redefining them.

## 8. Review notes

Human review should confirm that this pack:

- gives each chat-native release an explicit semantic overlay on the shared substrate,
- preserves accepted run classes, governance invariants, and proof invariants,
- keeps projection vocabulary additive instead of ontological,
- preserves R4 and R7 as the required bridge seams into artifact-centered work and explicit commissioning.
