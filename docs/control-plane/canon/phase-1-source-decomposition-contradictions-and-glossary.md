# Phase 1 source decomposition, contradiction register, and glossary pack
Version: 1.0
Status: Accepted
Task: P1.1 — Source decomposition / contradiction register / glossary
Artifact ID: canon.phase1-source-decomposition.v1
Canon scope: Cross-source product canon normalization for Phase 1

## 1. Purpose

This artifact decomposes the accepted source-authority set into one reviewable Phase 1 working pack.

It exists to:

- extract the major governing claims from the three source-authority documents,
- make cross-source tensions explicit instead of leaving them implicit,
- normalize the major terms that downstream semantic and architecture work will reuse,
- name the still-unresolved terms that later tasks must formalize rather than hand-wave.

This artifact is accepted for downstream use.
It prepares P1.2.
It does not by itself freeze the final Phase 1 product interpretation.

## 2. Scope boundaries

### In scope

- claim decomposition from the accepted source-authority set,
- contradiction and tension extraction,
- major-term normalization for downstream control-plane use,
- explicit unresolved-term capture for later semantic work.

### Out of scope

- accepting final product canon,
- changing the fixed release order,
- changing the accepted layer boundary,
- introducing new shared primitives,
- writing semantic state machines or architecture topology,
- reopening accepted forbidden shortcuts.

## 3. Source decomposition basis

### 3.1 Source roles

| Source | Role in this pack | Primary contribution |
| --- | --- | --- |
| `sa.all-prims.v1` | Layer and primitive authority | Defines engine, shared environment, app/domain boundaries and the canonical primitive families |
| `sa.chat-native-release-plan.v1` | Release doctrine authority | Fixes Platform Gate, R1-R7 order, release-specific exposure, and forbidden implementation shortcuts |
| `sa.task-studio-north-star.v1` | North-star app authority | Defines commissioned-work UX, run-native operation, Task Studio surfaces, task families, proof, and writeback expectations |

### 3.2 Claim inventory

#### 3.2.1 Primitive-set and layer claims (`sa.all-prims.v1`)

| Claim ID | Claim | Downstream implication |
| --- | --- | --- |
| `AP-01` | The architecture has three layers: engine, shared environment, and app/domain layer. | Later semantic and architecture packs must assign each major object family to one owner layer. |
| `AP-02` | The engine is a universal SDK/execution substrate, not a host application or transcript wrapper. | Runtime and repo work must not treat chat or any app shell as engine truth. |
| `AP-03` | The shared environment standardizes the human-facing operating model, shared object model, governance model, reuse model, and projection grammar across apps. | Cross-app handoff and reuse must happen on shared primitives instead of app-private ontologies. |
| `AP-04` | Runs, compiled context, evidence, memory, accepted knowledge, validation, proof, authority, persistence, provenance, replay, and variants are first-class engine concerns. | Later semantics and architecture packs must preserve these as explicit objects, not hidden transcript residue. |
| `AP-05` | The canonical environment primitive set includes Scope, Workspace, Project, App, Surface, Thread/Line, Branch, Commission, Contract, Run, Strategy Graph, Checkpoint, Handoff, Source Reference, Evidence Pack, Context Pack, Authority Scope, Memory Object, Canon Object, Artifact, Proof Bundle, State Delta, Writeback Proposal, Protocol, Workflow, Applet, Review, Approval Decision, and Annotation. | P2 semantic contracts should start from this set instead of inventing substitute nouns. |
| `AP-06` | The later code/repo wedge is a domain pack built on the shared environment, not part of the environment primitive set itself. | Repo/package work must not let code-domain storage or tooling redefine platform ownership. |

#### 3.2.2 Release-doctrine claims (`sa.chat-native-release-plan.v1`)

| Claim ID | Claim | Downstream implication |
| --- | --- | --- |
| `RP-01` | The first public release may look transcript-native, but the product is never transcript-native underneath. | Chat surfaces must remain projections over the substrate. |
| `RP-02` | The public release order is fixed: Platform Gate -> R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> Task Studio. | Downstream work must preserve sequencing and dependency order. |
| `RP-03` | Platform Gate is a mandatory internal gate before R1. | P3.5 must exist as a hard prerequisite, not a soft milestone. |
| `RP-04` | Artifact Workspace is the bridge release out of transcript gravity. | Continuity must shift toward artifact-centered work by R4. |
| `RP-05` | Prompt Studio and Governed Agent / Applet Chat are in-scope chat-native releases because they harden substrate, model abstraction, packaging, policy, and reusable execution. | P4 and P5 must treat them as required contract packs, not optional side tracks. |
| `RP-06` | Commissioning Bridge is the terminal chat release and exposes commission, contract, evidence, context, strategy, authority, proof, delta, and writeback semantics inside chat. | R7 must make Task Studio a projection change rather than a semantic translation. |
| `RP-07` | Shared primitives are progressively revealed across releases; no view is allowed to introduce a private competing truth model. | Release packs must inherit from one substrate and preserve forbidden shortcuts. |

#### 3.2.3 North-star app claims (`sa.task-studio-north-star.v1`)

| Claim ID | Claim | Downstream implication |
| --- | --- | --- |
| `TS-01` | Task Studio is a general-purpose commissioned-task app for bounded, governable, proof-returning AI work. | Task Studio scope and later semantic packs must stay broad enough for general commissioned work, but typed and bounded. |
| `TS-02` | Task Studio is run-native, not prompt-centric. | Commissioning, contract, context, strategy, authority, proof, delta, and writeback objects must stay explicit. |
| `TS-03` | The core interaction loop is commissioning rather than prompting: commission -> interpret -> lock -> execute -> inspect -> accept/branch -> persist selectively. | Surface and lifecycle packs must expose this loop directly. |
| `TS-04` | Serious work requires explicit contract, inspectable evidence/context, visible strategy, visible authority, explicit proof, explicit state delta, and lane-separated writeback. | Governance, proof, and surface packs must not collapse these semantics into one answer blob. |
| `TS-05` | Task Studio V1 is bounded to typed task families such as Compare, Synthesize, Extract, Transform, Audit, Plan, and Triage. | P2.2 and P5.3 must map user-facing task families to run classes and proof schemas. |
| `TS-06` | Task Studio is not code-editing-first, not a generic chat app, and not a hidden orchestration toy. | Later architecture and repo work must preserve the general commissioned-work center of gravity. |

## 4. Contradiction and tension register

The source set is directionally aligned, but several tensions would create downstream drift if they remain implicit.

| ID | Tension / contradiction | Evidence | Working disposition | Status |
| --- | --- | --- | --- | --- |
| `CR-01` | Transcript continuity can appear primary in early chat releases even though the accepted baseline says chat is only a projection. | `AP-02`, `RP-01`, `TS-02` | Normalize truth locus as: transcript/message continuity is a projection; consequential truth lives in runs, context/evidence, artifacts, proof, deltas, and writeback objects. | Resolved baseline |
| `CR-02` | Different documents emphasize different continuity centers: thread continuity, run consequence, and artifact-centered continuity. | `AP-05` defines Thread/Line and Run separately; `RP-04` centers artifacts at R4; `TS-01` and `TS-02` center commissioned runs. | Normalize as: Thread/Line = continuity lane; Run = primary consequential unit; Artifact = primary continuity anchor from R4 onward; Task Studio commissions create runs that attach to and produce artifacts. | Resolved by normalization |
| `CR-03` | The docs use `app`, `surface`, `projection`, `mode`, and `view` with different levels of formality. | `AP-03` and environment primitives define App/Surface and projection grammar; `RP-07` says modes are projections; Task Studio defines concrete surfaces and layouts. | Normalize as: App = domain projection over shared substrate; Surface = routable work area; Projection grammar = reusable interaction shape; Mode/View = alternate projection of the same underlying objects. Formal surface contracts remain later work. | Partially resolved |
| `CR-04` | Engine-facing and environment-facing names differ for closely related concepts, which can look like ontology drift. | `AP-04` uses Accepted Knowledge, Compiled Context Package, Variant; `AP-05` uses Canon Object, Context Pack, Branch. | Normalize as engine-to-environment projection pairs: Accepted Knowledge -> Canon Object; Compiled Context Package -> Context Pack; Variant -> Branch. Downstream packs should preserve the pairing instead of inventing third names. | Resolved by glossary |
| `CR-05` | Prompt Studio introduces reusable prompt assets, while the environment primitives and Task Studio rely on Protocol/Applet/Workflow reuse objects. | `RP-05`; `AP-05`; Task Studio reuse expectations | Distinguish reusable content assets from reusable execution assets: Prompt Artifact/Prompt Card are governed prompt assets; Protocol/Applet/Workflow are executable specifications and compositions. They may connect later, but they are not substitutes. | Partially resolved |
| `CR-06` | Commission and Contract exist in the shared environment primitive set from the start, but the public chat release plan delays explicit commissioning UX until R7. | `AP-05`, `RP-06`, `TS-03` | Normalize as semantic-before-UX: Commission/Contract exist in substrate semantics earlier; explicit public chat preflight and commissioning UI appear at R7; Task Studio later becomes the primary projection of those existing semantics. | Resolved by release topology |
| `CR-07` | `Canon` can mean human-owned product truth in the control plane or scoped runtime accepted truth in the shared environment. | Control-plane usage in this repo; `AP-04`/`AP-05`; Task Studio memory/canon sections | Reserve `product canon` for accepted control-plane meaning owned by humans. Reserve `Canon Object` for scoped accepted runtime truth inside the environment. Do not use the terms interchangeably in later packs. | Partially resolved |
| `CR-08` | The source set is intentionally non-code-specific, but repo execution work can accidentally smuggle code/repo shape back into platform ownership. | `AP-06`; repo/storage warnings in P0 artifacts; `TS-06` | Preserve repo layout as storage/execution convention only. Code-domain primitives remain later domain-pack work and must not be promoted into shared-environment ownership because they happen to land in this repo. | Resolved baseline |
| `CR-09` | The engine supports multi-agent coordination, and R6 introduces governed agents/applets, but the accepted baseline forbids agent-builder-first behavior and a second orchestration stack by default. | `AP-04`; `RP-05`; accepted forbidden-shortcut baseline | Normalize as: multi-agent capability is allowed in the substrate, but governed reuse and autonomy only become product-facing after authority, verifier, and packaging semantics exist. Factory.ai remains the base execution tool; no second default orchestration layer is introduced. | Resolved baseline |

## 5. Normalized glossary

| Term | Normalized meaning for downstream work | Source variants / notes |
| --- | --- | --- |
| **Engine** | The universal execution substrate and SDK for bounded, source-aware, policy-aware agentic work. | `sa.all-prims.v1` |
| **Shared environment** | The human-facing operating layer that standardizes shared objects, scope, governance, reuse, and projection grammar across apps. | `sa.all-prims.v1` |
| **App / domain pack** | A domain-specific projection built over the shared environment, not a private competing ontology. | `App`, `domain layer`, `later code wedge`, `Task Studio` |
| **Projection** | A user-facing way of exposing existing substrate objects without redefining their meaning. | Used across all three source docs |
| **Surface** | A routable work area inside an app. | Formal environment primitive in `sa.all-prims.v1`; concrete Task Studio surfaces later |
| **Run** | The bounded unit of consequential work and the primary consequential primitive. | Shared across all source docs |
| **Thread / Line** | A continuity lane for interaction, discussion, or evolving work; not the primary consequential primitive. | `Thread / Line` in environment primitives; transcript continuity in release plan |
| **Artifact** | A persistent output or persistent referenced object used across apps and later as a continuity anchor. | Shared across all source docs |
| **Evidence Pack** | The allowed grounding material for a run: sources and source regions that may support conclusions. | Environment-facing form of engine evidence structures |
| **Context Pack** | The compiled runtime package actually used by a run, including evidence plus memory, canon, policies, authority, tools, and parameters. | Environment-facing projection of `Compiled Context Package` |
| **Memory Object** | Durable remembered state available to future work, but distinct from canon. | Shared environment/runtime term |
| **Canon Object** | Scoped accepted runtime truth inside the shared environment. | Environment-facing projection of engine `Accepted Knowledge` |
| **Product canon** | Human-owned accepted control-plane meaning used to govern downstream planning/spec work in this repo. | Control-plane-specific distinction introduced by this pack |
| **Branch** | An alternate semantic line of work spanning assumptions, context, strategy, candidate knowledge, artifacts, or outcomes. | Environment-facing projection of engine `Variant` |
| **Proof Bundle** | The structured support package attached to a result, artifact, or decision. | Shared across release plan and Task Studio |
| **State Delta** | The explicit record of what changed or is proposed to change because of a run or merge. | Shared across source docs |
| **Writeback Proposal** | A lane-specific proposal to commit durable change. | Separates artifact, memory, canon, workflow, export/send, and integration writes |
| **Commission** | The raw delegated request before normalization into a formal contract. | Shared primitive; explicitly surfaced in R7 and Task Studio |
| **Contract** | The typed statement of what work is being commissioned, what success means, and what constraints/proof expectations apply. | `Contract`, `Task Contract`, `Contract Draft` |
| **Run Class** | The execution category that determines schemas, proof policy, authority defaults, and writeback defaults. | Shared-environment term |
| **Task Family** | The user-facing family of work inside Task Studio, typically mapped onto one or more run classes. | Task Studio-facing term; exact mapping deferred to P2.2 |
| **Authority Scope** | The explicit declaration of what a run may read, write, export, send, promote, or modify. | Shared across environment, release plan, and Task Studio |
| **Protocol** | A versioned executable specification for a class of work. | Successor to unstructured reuse prose |
| **Applet** | A packaged, user-facing projection over one or more Protocols with state, surfaces, roles, triggers, and writeback behavior. | Shared environment primitive; product-facing in R6 |
| **Platform Gate** | The mandatory internal pre-release gate that proves the substrate is not transcript-dependent before public launch. | `sa.chat-native-release-plan.v1` |
| **Task Studio** | The north-star commissioned-work app that makes consequential AI work run-native, inspectable, governable, and proof-returning. | `sa.task-studio-north-star.v1` |

## 6. Unresolved-term list

These terms should stay explicit and unresolved until later tasks formalize them.

| Term / phrase | Current working interpretation | Why still unresolved | Likely owner task |
| --- | --- | --- | --- |
| **Task family -> Run Class mapping** | Task Studio task families are user-facing groupings that will map onto formal run classes. | Exact one-to-one vs one-to-many mapping is not yet fixed. | `P2.2` |
| **Mode projection** | An alternate projection over the same branch/object graph. | Release plan names several modes, but their exact surface and grammar boundaries are not yet formalized. | `P1.4`, `P2.6`, `P4.5` |
| **Off-chain job** | A bounded research/exploration job that merges back through proposals. | The term appears in R3, but its precise execution and governance semantics are not yet specified. | `P4.5` |
| **Consensus branch** | A branch construct used in R3 mode work. | The release plan names it without fixing merge or approval semantics yet. | `P4.5` |
| **Chatlet projection** | A chat-facing projection of a governed applet/agent. | Named in R6, but not yet normalized against Applet, Surface, and Projection grammar. | `P4.8`, `P6.1` |
| **Acceptance Stack** | The R7 view-specific acceptance object grouping preflight/approval/writeback review. | Named in the release plan, but not yet mapped onto Review, Approval Decision, Delta, and Writeback Proposal surfaces. | `P4.9`, `P5.7` |
| **Root Artifact vs Focal Artifact** | Artifact Workspace differentiates workspace-root continuity from currently worked-on artifact focus. | The release plan names both, but their exact lifecycle and handoff semantics remain future work. | `P4.6` |
| **Contradiction Guard** | A reusable contradiction-checking control inside governed agent/applet work. | It is not yet clear whether it is a verifier-pack concern, a policy concern, or both. | `P4.8`, `P5.2` |

## 7. Working interpretation to carry into P1.2+

Until this pack is superseded or marked stale, downstream work should treat the following as the current working interpretation:

1. The three source-authority docs are directionally aligned; the main risk is term drift and emphasis drift, not a hard baseline split.
2. Runs remain the primary consequential primitive even when continuity later becomes artifact-centered.
3. Artifact-centered continuity is a later release/topology rule, not a replacement for run primacy.
4. Chat/public view sequencing is a projection problem, not an ontology problem.
5. Product canon and runtime canon must stay separate terms.
6. Prompt assets and execution assets must stay separate categories.
7. Code-domain work remains downstream domain-pack work and must not back-propagate into environment ownership during Phase 1.

## 8. Validation notes

This pack should be reviewed against the accepted P0.1 control-plane model and the accepted P0.4/P0.5 anti-drift baseline.

Manual review should confirm:

- the source-authority decomposition stays faithful to the accepted baseline,
- contradictions are explicit rather than buried,
- normalized terms do not silently reopen accepted decisions,
- unresolved items are named as future work instead of being smuggled in as fixed truth.
