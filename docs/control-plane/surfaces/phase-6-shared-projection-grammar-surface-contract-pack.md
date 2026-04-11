# Phase 6 shared projection grammar surface contract pack
Version: 1.0
Status: Accepted
Task: P6.1 — Surface contract packs
Artifact ID: surf.phase6-shared-projection-grammar-surface-contract-pack.v1
Surface scope: Accepted Phase 6 surface-contract deepening of the shared projection grammar for route clusters, alias resolution, companion-surface rules, and cross-app surface composition

This artifact is accepted for downstream use.
It deepens the accepted P2.6 grammar pack into Phase 6 surface contracts without changing grammar names or meanings.

## 1. Purpose

This pack turns the shared projection grammar into a reusable surface-contract layer for later release, Task Studio, and domain packs.

It exists to:

- define route-cluster and companion-surface expectations for the twelve accepted grammars,
- lock alias resolution rules so later packs reuse one grammar instead of inventing private metaphors,
- keep surface contracts below semantic ownership and above implementation detail.

## 2. Scope boundaries

### In scope

- shared grammar route-cluster contracts,
- alias-to-grammar resolution rules,
- companion-surface expectations,
- cross-grammar composition constraints that later packs must inherit.

### Out of scope

- release-specific product promises,
- Task Studio V1 inclusion/exclusion policy,
- repo/package/module layout,
- component-level UI design,
- domain-specific object semantics.

## 3. Surface-contract interpretation rules

### 3.1 Grammar-first rule

Every Phase 6 surface contract begins from the accepted grammar set `PG-01` through `PG-12`.
No later pack may treat a release-local or app-local alias as a replacement for the shared grammar it resolves to.

### 3.2 No-new-grammar rule

`P6.1` may deepen contract detail, but it may not add a thirteenth shared grammar family.
If a later pack appears to need one, that is a semantic review issue rather than a surface-contract shortcut.

### 3.3 Stable-selection rule

Route changes, pane swaps, tabs, and modal/detail expansions must preserve the same shared-object selection and stable refs.
Surface contracts may organize work differently, but they may not mint substitute identities.

### 3.4 Companion-not-override rule

Companion surfaces may enrich the current focal work, but they may not replace the primary grammar that owns the current consequential cluster.
`Console` may diagnose; it may not become the only source of proof, authority, delta, or approval truth.

### 3.5 Consequence-cluster visibility rule

Where `Run`, `Proof Bundle`, `State Delta`, `Writeback Proposal`, `Review`, or `Approval Decision` materially matter, the surface contract must keep them within the primary or companion cluster rather than pushing them into hidden logs or generic summaries.

## 4. Shared contract summary

| Grammar | Route-contract role | Required companions when materially relevant | Example aliases |
| --- | --- | --- | --- |
| `Composer` | Entry and shaping surface for new work or amendments | `Inspector`, `Browser / Library` | conversation composer, `New Commission Sheet`, contract draft entry |
| `Canvas` | Focal work or result surface | `Inspector`, `Ledger` | conversation canvas, focal artifact lens, `Result Canvas` |
| `Inspector` | Semantic detail and governing metadata surface | `Canvas`, `Live Monitor`, `Browser / Library` | context drawer, `Authority Panel`, `Task Contract Panel`, `Delta Inspector` |
| `Browser / Library` | Search, browse, filter, and resume surface | `Canvas`, `Inspector`, `Queue / Inbox` | thread library, artifact library, prompt browser |
| `Timeline` | Chronology and lifecycle surface | `Live Monitor`, `Compare View` | run history, checkpoint timeline, approval history |
| `Ledger` | Structured proof, validation, and decision surface | `Canvas`, `Queue / Inbox`, `Diff / Merge View` | `Proof Ledger`, validation ledger, writeback audit |
| `Compare View` | Explicit comparison surface | `Timeline`, `Diff / Merge View` | branch compare, pack diff, adaptation compare |
| `Queue / Inbox` | Pending governance and routed work surface | `Inspector`, `Ledger` | proposal inbox, review queue, failure inbox |
| `Board` | Grouped progression surface over accepted objects | `Browser / Library`, `Queue / Inbox` | workflow board, multi-run board |
| `Diff / Merge View` | Before/after and selective-acceptance surface | `Compare View`, `Ledger` | proposal review, merge view, revision diff |
| `Live Monitor` | Active execution supervision surface | `Timeline`, `Inspector`, `Console` | `Live Run View`, background-run monitor |
| `Console` | Low-level diagnostic surface | `Live Monitor`, `Inspector` | trace console, tool log console |

## 5. Alias and composition contract

### 5.1 Entry and focal-work aliases

1. `Conversation Surface` resolves to `Composer + Canvas`, with `Inspector` companion when semantic detail expands.
2. `New Commission Sheet` resolves to `Composer + Inspector` rather than a bespoke wizard grammar.
3. `Commission Card` and other resume cards remain projections over `Canvas` or `Browser / Library` selections rather than new shared objects.
4. `Focal Artifact Lens` and `Result Canvas` resolve to `Canvas` with supporting `Inspector` or `Ledger` companions when consequence state matters.

### 5.2 Inspect and govern aliases

1. `Context Drawer`, `Context Inspector`, `Authority Panel`, `Task Contract Panel`, and `Delta Inspector` resolve to `Inspector` variants or `Inspector` plus their accepted companions.
2. `Proof Ledger` and writeback audit surfaces resolve to `Ledger`.
3. `Proposal Inbox` and review queues resolve to `Queue / Inbox`.
4. No inspect/govern alias may hide critical semantics solely in `Console`.

### 5.3 Compare, diff, and progression aliases

1. `Pack Diff`, `Branch Compare`, and `Adaptation Compare` resolve to `Compare View`.
2. Selective acceptance over explicit diffs or proposals resolves to `Diff / Merge View`.
3. `Branch Map` and run-history views are compositions built from `Timeline` plus `Compare View` or `Live Monitor`, not separate grammar families.
4. Workflow and multi-run boards resolve to `Board` over accepted objects rather than stage-private cards.

### 5.4 Live supervision aliases

1. `Live Run View` resolves to `Live Monitor` with `Timeline`, `Inspector`, and `Console` companions as needed.
2. Background-run monitoring remains the same grammar family as live run supervision; it is not a second execution ontology.
3. Trace consoles and tool-log panes resolve to `Console` and stay diagnostic rather than semantic truth sources.

## 6. Boundary locks for downstream work

1. No later pack may introduce a new shared grammar family without upstream semantic change.
2. Every release, Task Studio, or domain alias must resolve back to one or more shared grammar contracts from this pack.
3. Route or pane changes must preserve stable shared-object refs instead of minting view-private identity.
4. `Console` must never become the only surface carrying proof, authority, delta, or approval semantics.
5. `P6.2` may map repo/package boundaries around these grammar contracts, but it may not reinterpret the grammar set itself.

## 7. Downstream implications

### 7.1 For chat-native surface contracts

- release-local surfaces should pick a primary grammar cluster by continuity center instead of inventing release-private surface families,
- release-to-release handoffs should remain transitions between grammar compositions over the same shared objects.

### 7.2 For Task Studio and later domain packs

- Task Studio and later domain surfaces should implement named surface aliases and route contracts as grammar compositions grounded here,
- later domain packs may add domain-specific nouns, but they must still reuse this grammar set and its boundary locks.

## 8. Review notes

Human review should confirm that this pack:

- gives Phase 6 one reusable surface-contract baseline over the accepted grammar set,
- keeps aliases resolvable back to shared grammar contracts,
- preserves the distinction between semantic ownership and the surfaces that project shared objects,
- avoids private view metaphors or new grammar families where the shared grammar already fits.
