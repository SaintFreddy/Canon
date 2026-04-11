# Phase 2 projection grammar contract pack
Version: 1.0
Status: Accepted
Task: P2.6 — Projection grammar contract pack
Artifact ID: sem.phase2-projection-grammar-contracts.v1
Semantic scope: Accepted shared interaction-grammar contracts for Composer, Canvas, Inspector, Browser / Library, Timeline, Ledger, Compare View, Queue / Inbox, Board, Diff / Merge View, Live Monitor, and Console

## 1. Purpose

This pack defines the reusable interaction grammar shared across chat-native releases and Task Studio.

It exists to:

- give apps one reusable surface grammar instead of private metaphors,
- keep projection choices below the semantic object layer and above implementation detail,
- map release-local surface names back to a stable shared grammar.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- the twelve shared projection grammars,
- required jobs and allowed object families for each grammar,
- reuse constraints, alias rules, and cross-grammar composition rules,
- stage-fit alignment to accepted release topology and semantic packs.

### Out of scope

- component-level UI design,
- route trees or layout composition,
- runtime/view-model implementation details,
- package/module boundaries,
- later domain-specific surface additions beyond the shared grammar baseline.

## 3. Grammar-wide interpretation rules

### 3.1 Projection-not-ownership rule

Projection grammar shapes how shared objects are entered, viewed, inspected, compared, monitored, or governed.
It does not transfer semantic ownership away from the shared object layer.

### 3.2 Stable-reference rule

Every grammar must round-trip stable shared-object refs.
A route change, pane change, or alias change must not create substitute identities.

### 3.3 Alias-must-resolve rule

Release-local names such as `Conversation Surface`, `Proposal Inbox`, `Proof Ledger`, `Result Canvas`, or `Authority Panel` are allowed only when they resolve back to one or more shared grammar contracts in this pack.

### 3.4 Composition-not-ontology rule

Apps may compose grammars, nest them, or foreground different ones by stage.
They may not invent incompatible replacements for these grammars when the shared grammar already fits.

### 3.5 Governance-visibility rule

Any grammar that exposes consequential work must preserve visibility of Run, Proof Bundle, State Delta, Writeback Proposal, Review, and Approval Decision objects where those objects are materially in play.

## 4. Contract template

Every projection grammar contract in this pack is defined using the same dimensions.

| Dimension | Meaning |
| --- | --- |
| Primary job | What the grammar is for |
| Admitted shared objects | Which shared objects or accepted drafts it may foreground |
| Required behaviors | Minimum interaction or inspectability behavior |
| Boundary locks | What the grammar must not collapse into or replace |
| Common compositions and stage fit | How the grammar is typically paired and where it is foregrounded |

## 5. Projection grammar summary

| Grammar ID | Grammar | Primary job | Typical shared objects | Example aliases / stage fits |
| --- | --- | --- | --- | --- |
| `PG-01` | Composer | Enter or shape new work | Commission, Contract, Template, Protocol, Source Reference, Run draft inputs | conversation composer, contract draft entry, new commission sheet |
| `PG-02` | Canvas | Primary work or result surface | Run, Artifact, Branch, Commission, Contract, Applet context | conversation canvas, focal artifact lens, result canvas |
| `PG-03` | Inspector | Detail rail or semantic inspection surface | Evidence Pack, Context Pack, Authority Scope, Proof Bundle, State Delta, metadata-bearing objects | context drawer, authority panel, delta inspector |
| `PG-04` | Browser / Library | Search, browse, and resume stored objects | Runs, Artifacts, Memory, Canon, Templates, Protocols, Applets, Packs | thread library, artifact library, prompt browser |
| `PG-05` | Timeline | Chronology and lifecycle view | Runs, Checkpoints, Branches, Reviews, Approval Decisions, replay history | run history, checkpoint timeline, approval history |
| `PG-06` | Ledger | Structured proof, validation, decision, and audit view | Proof Bundle, validator results, Writeback Proposal, Review, Approval Decision | proof ledger, validation ledger, writeback ledger |
| `PG-07` | Compare View | Explicit comparison of two or more targets | Branches, packs, artifacts, proofs, versions, options | branch compare, pack diff, adaptation compare |
| `PG-08` | Queue / Inbox | Routed pending work and governance actions | Assignment, Review, Approval Decision, failing Runs, escalations | proposal inbox, review queue, failure inbox |
| `PG-09` | Board | Grouped progression across states or stages | Runs, Workflows, Applets, Assignments, stage clusters | workflow board, multi-run board |
| `PG-10` | Diff / Merge View | Before/after and selective-acceptance surface | Artifact revisions, State Delta, Writeback Proposal, merge proposals | proposal review, merge view, revision diff |
| `PG-11` | Live Monitor | Supervise active execution | Run, Workflow, Checkpoint, pending approvals, child runs | run monitor, background-run monitor |
| `PG-12` | Console | Diagnostic and low-level inspection | tool outputs, traces, validator logs, execution diagnostics | trace console, tool log console |

## 6. Grammar contracts

### 6.1 `PG-01` — Composer

| Dimension | Contract |
| --- | --- |
| Primary job | Enter a Commission, shape a Contract, attach sources, or instantiate a Template, Protocol, Workflow, or Applet entry flow |
| Admitted shared objects | Draft Commission, draft Contract, Template, Protocol, Applet, Source Reference attachments, intake refs for a Run |
| Required behaviors | Capture raw request plus structured parameters; attach explicit sources; name the instantiation target; hand off into shared draft/governing objects instead of hidden execution |
| Boundary locks | Composer is not allowed to remain the sole source of truth once consequential work starts; it must not collapse serious work back into a prompt-only blob |
| Common compositions and stage fit | Commonly paired with Inspector and Browser / Library; foregrounded in R1 entry, R7 preflight, and Task Studio New Commission Sheet |

### 6.2 `PG-02` — Canvas

| Dimension | Contract |
| --- | --- |
| Primary job | Present the primary work or result surface for the currently foregrounded continuity center |
| Admitted shared objects | Run, Artifact, Branch, Commission, Contract, Protocol/Applet context, derived result artifacts |
| Required behaviors | Show the current focal object clearly; render structured result state when it exists; link out to supporting Inspector, Ledger, Compare, or Diff/Merge views as needed |
| Boundary locks | Canvas must not reduce structured work into transcript-only prose when a Run, Artifact, Proof Bundle, or Delta already exists |
| Common compositions and stage fit | Commonly paired with Inspector and Ledger; foregrounded as Conversation Surface, Focal Artifact Lens, and Result Canvas |

### 6.3 `PG-03` — Inspector

| Dimension | Contract |
| --- | --- |
| Primary job | Inspect semantic detail, metadata, and frozen basis for the currently selected object |
| Admitted shared objects | Evidence Pack, Context Pack, Authority Scope, Proof Bundle, State Delta, Contract, Commission, Artifact metadata, review state |
| Required behaviors | Expose frozen refs, inclusion/exclusion reasoning, policy or authority boundaries, and other decision-relevant semantics one click away from the main canvas |
| Boundary locks | Inspector is not a debug-only drawer; critical governance, context, or delta semantics must not live only in Console or hidden logs |
| Common compositions and stage fit | Commonly paired with Canvas, Queue / Inbox, and Live Monitor; foregrounded in R2 context control, R7 preflight, and Task Studio panels such as Authority Panel and Delta Inspector |

### 6.4 `PG-04` — Browser / Library

| Dimension | Contract |
| --- | --- |
| Primary job | Browse, search, filter, sort, and resume first-class objects |
| Admitted shared objects | Runs, Artifacts, Memory Objects, Canon Objects, Templates, Protocols, Applets, Packs, and related durable objects |
| Required behaviors | Preserve stable IDs in listing and filter state; support deep-linking into other grammars; keep object-family labels tied to accepted shared objects |
| Boundary locks | Browser / Library is not allowed to invent app-private object taxonomies that break cross-app continuity |
| Common compositions and stage fit | Commonly paired with Canvas and Inspector; foregrounded as Thread Library, Artifact Library, Prompt Browser, and Applet browser |

### 6.5 `PG-05` — Timeline

| Dimension | Contract |
| --- | --- |
| Primary job | Show lifecycle chronology and causal ordering for consequential work |
| Admitted shared objects | Runs, Checkpoints, Branches, Reviews, Approval Decisions, replay attempts, major events |
| Required behaviors | Preserve chronological and causal order; expose branch points, replay attempts, checkpoint boundaries, and review/approval milestones as linked shared objects |
| Boundary locks | Timeline must not treat transcript message order as the substitute for lifecycle truth when explicit Run/Checkpoint/Decision records exist |
| Common compositions and stage fit | Commonly paired with Live Monitor and Compare View; foregrounded in R3 branch/replay work, R7 review history, and Task Studio run history |

### 6.6 `PG-06` — Ledger

| Dimension | Contract |
| --- | --- |
| Primary job | Present structured proof, validation, decisions, and audit state |
| Admitted shared objects | Proof Bundle, validator results, Writeback Proposal, Review, Approval Decision, audit-oriented Artifact refs |
| Required behaviors | Keep claims, evidence, validator outcomes, approval history, and lane-specific decisions inspectable as structured records rather than prose summaries |
| Boundary locks | Ledger must not collapse proof, delta, review, and approval into one persuasive narrative blob |
| Common compositions and stage fit | Commonly paired with Canvas, Inspector, and Queue / Inbox; foregrounded as Proof Ledger, validation ledger, and writeback audit view in R4, R7, and Task Studio |

### 6.7 `PG-07` — Compare View

| Dimension | Contract |
| --- | --- |
| Primary job | Compare two or more explicit targets and surface material differences |
| Admitted shared objects | Branches, Evidence/Context Packs, Artifacts, Proof Bundles, protocol or prompt versions, ranked options |
| Required behaviors | Name compared targets and axes explicitly; preserve target identity; surface material differences, omissions, and recommendation basis when present |
| Boundary locks | Compare View is not satisfied by a generic side-by-side visual arrangement without explicit targets and difference semantics |
| Common compositions and stage fit | Commonly paired with Timeline and Diff / Merge View; foregrounded as Branch Compare, Pack Diff, and Adaptation Compare |

### 6.8 `PG-08` — Queue / Inbox

| Dimension | Contract |
| --- | --- |
| Primary job | Route pending work, approvals, review items, failures, and escalations |
| Admitted shared objects | Assignment, Review, Approval Decision, pending Writeback Proposal, failing Run, escalation items |
| Required behaviors | Each item must resolve to concrete target objects, urgency, state, and next action; queue state must remain attributable and inspectable |
| Boundary locks | Queue / Inbox is not a generic notification feed disconnected from shared objects and decision state |
| Common compositions and stage fit | Commonly paired with Inspector and Ledger; foregrounded as Proposal Inbox in R4 and Queue / Inbox in R6 and later governance-heavy flows |

### 6.9 `PG-09` — Board

| Dimension | Contract |
| --- | --- |
| Primary job | Group existing work into staged progression clusters without replacing the underlying objects |
| Admitted shared objects | Runs, Workflows, Applets, Assignments, stage/state clusters over accepted objects |
| Required behaviors | Group or swimlane objects by explicit state or workflow stage; preserve direct links to underlying Run, Workflow, or Assignment identities |
| Boundary locks | Board may not invent a second workflow ontology or replace Workflow/Run objects with stage-private cards that lose provenance |
| Common compositions and stage fit | Commonly paired with Queue / Inbox and Browser / Library; foregrounded in reusable execution and later multi-run orchestration views |

### 6.10 `PG-10` — Diff / Merge View

| Dimension | Contract |
| --- | --- |
| Primary job | Inspect explicit before/after changes and support selective acceptance where policy allows |
| Admitted shared objects | Artifact revisions, State Delta, Writeback Proposal, Branch merge proposals, adaptation deltas |
| Required behaviors | Preserve source and target identity; show change scope explicitly; support selective lane-local or operation-local acceptance when the underlying objects allow it |
| Boundary locks | Diff / Merge View must act on explicit revisions, deltas, or proposals rather than raw transcript blobs or implicit “latest text wins” behavior |
| Common compositions and stage fit | Commonly paired with Compare View and Ledger; foregrounded in R4 proposal review, R5 adaptation comparison, and R7 lane-by-lane writeback review |

### 6.11 `PG-11` — Live Monitor

| Dimension | Contract |
| --- | --- |
| Primary job | Supervise active consequential execution while it is happening |
| Admitted shared objects | Run, Workflow, Checkpoint, child-run linkage, pending approvals, warning state |
| Required behaviors | Surface current phase, completed phases, blocked phases, pending approvals, child runs, checkpoints, and expected next transitions in governance-relevant terms |
| Boundary locks | Live Monitor is not agent theater and not raw chain-of-thought output; it must prioritize governable execution state over spectacle |
| Common compositions and stage fit | Commonly paired with Timeline and Console; foregrounded in internal Platform Gate monitoring, R6 background runs, R7 live monitoring, and Task Studio live run supervision |

### 6.12 `PG-12` — Console

| Dimension | Contract |
| --- | --- |
| Primary job | Provide low-level diagnostics, trace data, tool outputs, and validation logs |
| Admitted shared objects | Tool invocation traces, validator logs, execution diagnostics, adapter failures, detailed runtime traces |
| Required behaviors | Keep low-level data linked back to the relevant Run, Tool, validator, or adapter identity; support deep inspection without becoming the primary semantic source of truth |
| Boundary locks | Console may reveal implementation detail, but it may not be the only place where proof, authority, delta, or approval semantics are available |
| Common compositions and stage fit | Commonly paired with Live Monitor and Inspector; foregrounded in internal gate/audit work, advanced background-run debugging, and later implementation-facing tooling |

## 7. Cross-grammar composition and alias rules

1. `Conversation Surface` resolves to a composition of Composer + Canvas, with Inspector as the companion when semantic detail is expanded.
2. `Context Drawer`, `Authority Panel`, `Task Contract Panel`, and `Delta Inspector` resolve to Inspector variants rather than new grammars.
3. `Proof Ledger` and writeback audit views resolve to Ledger; `Proposal Inbox` resolves to Queue / Inbox; `Result Canvas` and `Focal Artifact Lens` resolve to Canvas.
4. `Pack Diff`, `Branch Compare`, and `Adaptation Compare` resolve to Compare View; selective acceptance of those differences resolves to Diff / Merge View.
5. `Branch Map` and run-history views are compositions built from Timeline plus Compare View or Live Monitor, not separate grammar families.
6. `Live Run View` resolves to Live Monitor with companion Timeline, Inspector, and Console as needed.
7. When a stage needs a new alias, the alias must declare which shared grammar or grammar composition it resolves to.

## 8. Downstream implications

### 8.1 For Phase 3 architecture work

- route contracts, UI-worker boundaries, and event flows should map to these grammar contracts rather than to release-local one-offs.

### 8.2 For Phase 4 release contract packs

- each release contract should choose stage emphasis from this grammar set instead of inventing local metaphors that duplicate existing grammars.

### 8.3 For Phase 6 surface contracts

- later surface/repo packs should deepen these contracts into module and route plans without changing the shared grammar names or meanings.

## 9. Review notes

Human review should confirm that this pack:

- gives the platform one reusable interaction grammar across chat-native releases and Task Studio,
- keeps grammar aliases resolvable back to shared contracts,
- preserves the distinction between semantic objects and the surfaces that project them,
- avoids private view metaphors where the shared grammar already fits.
