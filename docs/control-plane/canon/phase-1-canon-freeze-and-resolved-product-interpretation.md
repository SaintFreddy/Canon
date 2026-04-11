# Phase 1 canon freeze and resolved product interpretation note
Version: 1.0
Status: Review-ready
Task: P1.2 — Canon freeze / resolved product interpretation
Artifact ID: canon.phase1-product-interpretation-freeze.v1
Canon scope: Resolved product interpretation for wedge, north star, release order, and non-negotiable constraints

## 1. Purpose

This artifact turns the accepted baseline plus the accepted P1.1 decomposition pack into one explicit resolved-interpretation note for downstream work.

It exists to:

- close remaining ambiguity around the first wedge, north star, release order, and projection-vs-ontology rules,
- restate the non-negotiable constraints that later semantic, architecture, release, and repo work must preserve,
- provide one reviewable canon note that later Phase 1 and Phase 2 tasks can reference directly.

This artifact is review-ready, not yet accepted.
It is intended to become the accepted P1.2 canon-freeze note after human review.

## 2. Scope boundaries

### In scope

- resolved interpretation of the first wedge,
- resolved interpretation of the north-star app,
- resolved interpretation of the fixed release order,
- resolved interpretation of projection-vs-ontology rules,
- explicit non-negotiable downstream constraints.

### Out of scope

- layer-by-layer ownership mapping for every primitive family,
- surface topology details per release,
- state-machine or schema design,
- technical architecture topology,
- repo/package layout,
- any reopening of accepted baseline decisions.

## 3. Resolved product interpretation

### 3.1 Decision table

| Decision ID | Resolved interpretation | Basis | Downstream rule |
| --- | --- | --- | --- |
| `RI-01` | The first wedge is the chat-native phase. | `sa.chat-native-release-plan.v1`, `cp.master-plan.v1` | Early product work may look chat-like, but must still harden the shared substrate underneath. |
| `RI-02` | Task Studio is the north-star commissioned-work app, not a side concept and not a code-first detour. | `sa.task-studio-north-star.v1`, `cp.master-plan.v1` | Later semantics, release work, and repo decisions must preserve Task Studio as the handoff target. |
| `RI-03` | The release order is fixed and non-reopenable inside normal execution: Platform Gate -> R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> Task Studio. | `sa.chat-native-release-plan.v1`, `cp.master-plan.v1` | Downstream release and architecture packs must preserve this sequence and its dependency logic. |
| `RI-04` | Chat-native releases are projections over shared primitives, not competing ontologies or transcript-owned truth models. | `sa.all-prims.v1`, `sa.chat-native-release-plan.v1`, `canon.phase1-source-decomposition.v1` | No release pack or implementation plan may relocate consequential truth into transcript/session state. |
| `RI-05` | Task Studio must arrive as a projection change over already-existing semantics, not as a rewrite to a new ontology. | `sa.task-studio-north-star.v1`, `sa.chat-native-release-plan.v1`, `canon.phase1-source-decomposition.v1` | R7 and Task Studio work must preserve object continuity across the handoff. |
| `RI-06` | Artifact Workspace is the bridge release out of transcript gravity. | `sa.chat-native-release-plan.v1`, `canon.phase1-source-decomposition.v1` | Continuity must move toward artifact-centered work by R4 without demoting runs as the primary consequential unit. |
| `RI-07` | Prompt Studio and Governed Agent / Applet Chat are mandatory chat-native releases because they harden reusable substrate, provider abstraction, governance, and packaging. | `sa.chat-native-release-plan.v1`, `cp.master-plan.v1` | These releases must be treated as required architecture work, not optional feature branches. |
| `RI-08` | Commissioning Bridge is the terminal chat release and must expose commissioning semantics explicitly enough that Task Studio becomes a surface shift, not a semantic migration. | `sa.chat-native-release-plan.v1`, `sa.task-studio-north-star.v1` | R7 contract work must make commission, contract, authority, proof, delta, and writeback semantics explicit in chat. |

### 3.2 Interpretation notes

#### First wedge

The first wedge is deliberately chat-native because it is the lowest-friction adoption surface.
That does not authorize transcript-native truth underneath.
The wedge is visual and experiential, not ontological.

#### North star

Task Studio remains the north-star general-purpose commissioned-work app.
It proves the shared environment directly by making consequential work run-native, inspectable, governable, proof-returning, and writeback-aware.

#### Release order

The release order is fixed because it encodes dependency order:

- Platform Gate prevents transcript-first substrate shortcuts,
- R1-R3 expose runs, context, and branching,
- R4 moves continuity toward artifacts,
- R5-R6 harden reusable assets and governed execution,
- R7 exposes explicit commissioning semantics,
- Task Studio then becomes the dedicated commissioned-work projection over that established substrate.

#### Projection vs ontology

All chat-native releases, all mode projections, and Task Studio itself must reuse one shared substrate and one shared semantic base.
Different views may change what is foregrounded, but they may not invent private truth models.

## 4. Non-negotiable constraints

The following constraints are closed for downstream work unless an explicit future instruction reopens them.

### 4.1 Core baseline constraints

- The architecture has three layers: engine, shared environment, app/domain layer.
- The engine is not the product shell.
- The shared environment is not one app.
- Product truth remains human-owned.
- Chat is a projection over shared primitives, not the source of truth.
- Task Studio is the north-star commissioned-work app.
- The chat-native release order is fixed.
- Artifact Workspace is the bridge release out of transcript gravity.
- Prompt Studio and Governed Agent / Applet Chat are required releases, not optional side quests.
- Commissioning Bridge is the terminal chat release.

### 4.2 Forbidden-shortcut constraints

- No master chat truth.
- No fake fine-grained context control without real spans.
- No chat-session-attached runs as the long-term model.
- No hidden memory sludge.
- No silent proposal application.
- No separate backend per view.
- No agent-builder-first approach before authority and verifier semantics exist.
- No transcript-first rewrite trap.
- No letting repo shape dictate platform architecture.
- No second orchestration stack by default.

## 5. Explicitly closed ambiguity set

For the purposes of downstream planning/spec work, the following questions are considered closed by this note:

- Which public wedge comes first? `Chat-native phase`
- What is the north-star app model? `Task Studio`
- Is the release order still open to reshuffling? `No`
- Is chat allowed to own consequential truth? `No`
- Does Task Studio require a new ontology later? `No`
- Are Prompt Studio and R6 optional? `No`
- Is Artifact Workspace optional as the bridge out of transcript gravity? `No`

Remaining future work may still formalize schemas, ownership maps, surface contracts, and technical topology, but it should not reopen these resolved interpretations while doing so.

## 6. Downstream implications

### 6.1 For P1.3 — Layer and primitive separation pack

- Use this note plus `canon.phase1-source-decomposition.v1` as the fixed interpretation basis for assigning owner layers.
- Do not let view-specific wording smuggle truth back into transcript or app-private objects.

### 6.2 For P1.4 — Surface and release topology canon

- Treat release order and the R4/R7 bridge points as fixed.
- Express topology as projection sequencing over shared primitives, not as independent product stacks.

### 6.3 For P1.5 — Rewrite-containment / stable seam map

- Place run/context/evidence/artifact/proof/delta/writeback semantics below chat-specific UI logic.
- Treat transcript-owned state as a high-risk rewrite trap, not a viable substrate shortcut.

### 6.4 For P1.6 — Golden scenario corpus

- Include scenarios that explicitly test wedge-to-north-star continuity, artifact-centered continuity after R4, and chat-to-Task-Studio continuity after R7.

## 7. Review notes

Human review should specifically confirm that this note:

- does not reopen accepted baseline decisions,
- accurately freezes wedge/north-star/release-order/projection interpretation,
- preserves the accepted forbidden-shortcut register,
- does not smuggle later-phase architecture or schema decisions into product canon.
