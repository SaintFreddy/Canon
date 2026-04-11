# Phase 6 chat-native surface contract pack
Version: 1.0
Status: Accepted
Task: P6.1 — Surface contract packs
Artifact ID: surf.phase6-chat-native-surface-contract-pack.v1
Surface scope: Accepted Phase 6 chat-native surface contract pack mapping R1-R7 surface clusters and aliases onto the shared projection grammar

This artifact is accepted for downstream use.
It fixes how the chat-native releases resolve their surface clusters back to the shared grammar instead of inventing release-private surface families.

## 1. Purpose

This pack turns the accepted R1-R7 release contracts into one cross-release surface-contract baseline.

It exists to:

- map each release's primary surface cluster onto the shared grammar,
- keep release-local aliases tied to stable grammar compositions,
- preserve the release-to-release handoff chain without view-local ontology drift.

## 2. Scope boundaries

### In scope

- chat-native release surface clusters for `R1` through `R7`,
- alias-to-grammar mapping for major release-local surfaces,
- release-to-release surface-handoff rules,
- release-local boundary locks against overbuild or second truth models.

### Out of scope

- Task Studio route contracts beyond the R7 handoff seam,
- repo/package/module layout,
- component-level UI detail,
- later domain surface families.

## 3. Chat-native interpretation rules

### 3.1 Release-surfaces-resolve-to-grammar rule

Every chat-native release surface must resolve to one or more shared grammars from the accepted projection grammar pack.
Release naming may change emphasis; it may not create new grammar families.

### 3.2 Continuity-center rule

Each release foregrounds one continuity center or capability shift.
The primary surface cluster for that release must match that center rather than spending future-stage grammar depth early.

### 3.3 Handoff-chain rule

Release-to-release handoffs remain transitions between grammar compositions over the same shared objects.
No release may smuggle a private backend, private task ontology, or surface-only object model into the next stage.

### 3.4 No-overbuild rule

When a later stage owns a semantic seam, earlier releases must not approximate it through hidden surface complexity, extra dashboard truth, or stage-private governable objects.

## 4. Cross-release summary

| Release | Primary surface cluster | Shared grammar composition | Continuity center | Explicit refusal |
| --- | --- | --- | --- | --- |
| `R1` | Conversation cluster | `Composer + Canvas` with `Inspector` companion | thread-assisted run continuity | transcript-as-truth shortcuts |
| `R2` | Context-control cluster | `Canvas + Inspector + Browser / Library + Compare View` | explicit evidence/context control | fake sidebar-only context control |
| `R3` | Branch/replay cluster | `Canvas + Timeline + Compare View + Board` | branch/replay continuity around checkpoints | transcript cloning as branching |
| `R4` | Artifact workspace cluster | `Canvas + Browser / Library + Queue / Inbox + Ledger + Diff / Merge View` | artifact-centered continuity | silent artifact mutation |
| `R5` | Prompt asset cluster | `Browser / Library + Canvas + Inspector + Compare View + Diff / Merge View` | prompt artifact lineage continuity | prompt cards as reusable execution ontology |
| `R6` | Governed reusable-execution cluster | `Composer + Canvas + Browser / Library + Queue / Inbox + Board + Live Monitor + Console` | protocol/applet/workflow continuity | agent theater and second execution ontology |
| `R7` | Commissioning bridge cluster | `Composer + Canvas + Inspector + Live Monitor + Ledger + Diff / Merge View + Queue / Inbox` | Commission/Contract continuity into explicit run governance and handoff | chat-private commissioning ontology |

## 5. Release surface contracts

### 5.1 `R1` and `R2`

1. `R1` `Conversation Surface` resolves to `Composer + Canvas`, with `Inspector` companion for source and run detail when expanded.
2. `R2` context control resolves to `Inspector`-led surfaces with `Browser / Library` and `Compare View` companions for pack browse/freeze/diff behavior.
3. Neither `R1` nor `R2` may create transcript-local truth that bypasses the shared run, evidence, or context substrate.

### 5.2 `R3`, `R4`, and `R5`

1. `R3` branch and replay surfaces resolve to `Timeline + Compare View`, optionally with `Board` and `Canvas` when focal work is foregrounded.
2. `R4` artifact workspace surfaces resolve to `Canvas` for focal artifacts, `Queue / Inbox` for proposal routing, `Ledger` for proof/review, and `Diff / Merge View` for selective acceptance.
3. `R5` prompt-asset browsing, model-profile inspection, and adaptation comparison stay within `Browser / Library`, `Inspector`, `Compare View`, and `Diff / Merge View` rather than inventing prompt-private grammars.

### 5.3 `R6` and `R7`

1. `Chatlet Projection` is normalized as a chat-facing composition over `Composer`, `Canvas`, `Browser / Library`, `Queue / Inbox`, `Board`, `Live Monitor`, and `Console`; it is not a new grammar family.
2. `R6` background runs and queue/inbox governance remain surface compositions over shared Protocol/Applet/Workflow/Run objects rather than a second execution ontology.
3. `R7` `Commission Card` resolves to `Canvas` or `Browser / Library` selection over the same `Commission` and linked `Contract`.
4. `R7` `Contract Draft` resolves to `Composer + Inspector`; `Run Preflight` resolves to `Inspector`-led governance/detail surfaces; `Proof Ledger` resolves to `Ledger`; `Delta Inspector` resolves to `Inspector` with `Diff / Merge View` companion.
5. `Acceptance Stack` remains a chat-domain projection over proof/review/delta/writeback surfaces; `Chat-to-Run Handoff` is a routing envelope rather than a new grammar or export/import artifact.

## 6. Boundary locks for downstream work

1. No chat-native release may invent a release-private grammar family.
2. `R6` may not treat governed reusable execution as a second ontology separate from the shared grammar and shared object model.
3. `R7` may not treat commissioning surfaces as a private ontology or as a substitute for the shared Commission/Contract/Run chain.
4. No release may hide proof, delta, review, approval, or writeback only in `Console` or narrative summaries when those objects materially exist.
5. Task Studio and later surface packs must inherit this release-cluster mapping rather than reinterpret the chat-native stages from scratch.

## 7. Downstream implications

### 7.1 For Task Studio surface contracts

- the Task Studio pack should treat R7 as a handoff from chat-native grammar compositions into Task Studio grammar compositions over the same shared objects,
- no Task Studio route contract should imply that chat-native releases used a different grammar substrate.

### 7.2 For later implementation work

- route/module/component planning should use these release clusters as the surface-contract baseline rather than rediscovering surface shape from copy or UI mockups.

## 8. Review notes

Human review should confirm that this pack:

- maps the accepted R1-R7 release surfaces onto one reusable grammar set,
- keeps release-local aliases and emphasis tied to shared grammar compositions,
- preserves the release-to-release handoff chain without second truth models,
- normalizes `Chatlet Projection`, `Acceptance Stack`, and `Chat-to-Run Handoff` as surface-level projections instead of new ontology.
