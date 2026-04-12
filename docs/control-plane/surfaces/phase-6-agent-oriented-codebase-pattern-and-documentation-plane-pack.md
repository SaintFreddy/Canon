# Phase 6 agent-oriented codebase pattern and documentation plane pack
Version: 1.0
Status: Accepted
Task: P6.3 — Agent-oriented codebase pattern and documentation plane
Artifact ID: surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1
Surface scope: Accepted Phase 6 documentation-plane pack defining workspace manifest views, generated current-state datasets, module-boundary test contracts, fixture rules, and packet context-pack compilation rules over the accepted repo/package baseline

This artifact is accepted for downstream use.
It turns the accepted `P6.2` repo/package baseline into one agent-navigation and documentation-plane layer for later implementation-facing work.
It does not create release blueprints, pilot packets, benchmark harnesses, runtime modules, or implementation code.

## 1. Purpose

This pack exists to:

- define the documentation-plane structure that mirrors the accepted Phase 6 root families,
- make workspace manifest views and the generated current-state view explicit and machine-usable,
- define where module-boundary test contracts and fixture-rule datasets live before executable harnesses arrive,
- define how later agent packets compile repo-local context packs from accepted artifacts, local docs, current-state data, and bounded file scope.

## 2. Scope boundaries

### In scope

- documentation-plane structure over the accepted root families from `P6.2`,
- workspace manifest index rules and generated current-state view rules,
- module-boundary test-contract datasets and fixture-rule datasets,
- packet context-pack compilation rules for later implementation-facing agent packets,
- boundary locks that `P6.4` through `P6.6` must inherit.

### Out of scope

- changing the accepted repo/package ownership map from `P6.2`,
- release-by-release touched-module blueprints that belong to `P6.5`,
- executable packet briefs, file whitelists, or approval templates that belong to `P6.6`,
- pilot benchmark harnesses, internal skills, or adapters that belong to `P6.4`,
- runtime context-compiler semantics beyond the accepted `P3.2` topology,
- implementation code, package scaffolding, services, workers, or UI modules.

## 3. Documentation-plane interpretation rules

### 3.1 Documentation-plane-over-layout rule

The documentation plane projects the accepted repo/package baseline into agent-readable manifests, current-state views, contract datasets, and packet-compilation rules.
It may describe current repo shape and reserved roots, but it may not redefine ownership or let file placement become architecture.

### 3.2 Normative-manifest plus derived-current-state rule

Workspace manifests are the normative documentation-plane view for the accepted root families.
The generated current-state view is derived from those manifest entries plus on-disk repo state.
Current-state data helps navigation and validation; it does not replace the accepted root-family baseline from `P6.2`.

### 3.3 Accepted-artifact navigation rule

Agents should navigate later implementation-facing work from:

1. accepted source-authority and accepted control-plane artifacts,
2. root and descendant `AGENTS.md` files,
3. the accepted workspace manifest index,
4. the generated current-state view,
5. the accepted module-boundary, fixture-rule, and packet-context datasets when they materially apply.

Unregistered notes, drafts, and stale material remain non-default inputs.

### 3.4 Reserved-root visibility rule

Reserved roots from `P6.2` appear in the documentation plane even before runtime code exists beneath them.
A reserved root may therefore be represented as `reserved_not_materialized` or `reserved_gated_not_materialized` in manifest and current-state data without implying implementation approval.

### 3.5 Test-contract-before-harness rule

`P6.3` introduces machine-usable module-boundary contracts and fixture rules before executable harnesses or benchmark wrappers exist.
Those datasets define expectations and placement; they do not claim that every later validator already exists.

### 3.6 Packet-context-is-execution-packaging rule

The packet context-pack rules in this pack are repo-execution packaging rules for later bounded agent work.
They reuse accepted `P0.2`, `P0.3`, `P0.5`, and `P3.2` truth, but they are not a second runtime context compiler and must not be read as product semantics.

## 4. Documentation-plane artifact set

| Artifact or dataset | Repo path | Role |
| --- | --- | --- |
| Workspace manifest index | `docs/control-plane/core/workspace-manifest-index.json` | Accepted machine-readable manifest view over the Phase 6 root families |
| Generated current-state view | `docs/control-plane/core/codebase-current-state.json` | Derived repo-state snapshot naming which root families are materialized, reserved, or gated |
| Packet context-pack rules | `docs/control-plane/core/agent-packet-context-pack-rules.json` | Accepted compilation rules for later bounded agent packets |
| Module-boundary test contracts | `tests/contracts/module-boundary.contracts.json` | Machine-usable boundary rules over workspace families and cross-root refusals |
| Fixture rules | `tests/fixtures/fixture-rules.json` | Machine-usable fixture-family, storage-root, and protocol-binding rules |

The documentation plane therefore spans accepted control-plane data and repo-local contract roots without creating a second planning system.

## 5. Workspace manifest model

### 5.1 Root-family manifest coverage

The manifest index must cover the following root families from `P6.2`:

| Manifest root | Phase 6 role | Expected state in the current repo |
| --- | --- | --- |
| `docs/control-plane/` | accepted planning/spec control plane | materialized and active |
| `/.factory/` | repo-scoped Factory execution assets | materialized and active |
| `apps/` | first-party app projections | reserved until later implementation work |
| `packages/` | shared contracts, schemas, and reusable packages | reserved until later implementation work |
| `services/` | environment/control and gateway services | reserved until later implementation work |
| `workers/` | bounded worker families | reserved until later implementation work |
| `domains/` | later domain-pack roots | reserved and semantically gated |
| `tests/` | contracts, fixtures, regression, replay, and benchmark assets | materialized as documentation-plane contract and fixture roots in `P6.3` |
| `scripts/` | thin repo-local validator and generation wrappers | reserved until real wrappers land |

### 5.2 Required manifest fields

Each manifest entry should make the following explicit:

- root path,
- workspace family role,
- current materialization posture,
- allowed child roots or family patterns,
- governing accepted artifact refs,
- execution posture for agent navigation,
- notes when a root is gated or intentionally not yet materialized.

### 5.3 Manifest discipline

1. A manifest entry may describe a reserved root that is not yet present on disk.
2. A manifest entry may not smuggle new ownership, runtime meaning, or domain semantics into the repo.
3. `domains/` remains gated by future accepted domain packs and should stay visibly gated in documentation-plane data.
4. `tests/` may materialize contract and fixture roots before runtime packages or services exist because those files describe validation expectations rather than executable product modules.

## 6. Generated current-state view rules

### 6.1 Derivation basis

The generated current-state view should derive from:

- the accepted workspace manifest index,
- actual on-disk presence of the named root families,
- the accepted P6.3 contract/fixture files that materialize `tests/`,
- existing control-plane and Factory roots already present in the repo.

### 6.2 What the current-state view must show

For each root family the derived view should expose:

- whether the root currently exists on disk,
- whether the root is active, reserved, or gated,
- notable entries or child roots when materialized,
- the governing manifest or accepted artifact refs that explain its state.

### 6.3 Derived-view boundary

The current-state view may be regenerated when root materialization changes.
Regenerating the view updates derived data only; it does not, by itself, approve new roots or change accepted ownership rules.

## 7. Module-boundary contract and fixture-rule datasets

### 7.1 Module-boundary contract expectations

The module-boundary contract dataset should make machine-usable at least the following `P6.2` rules:

- allowed dependency roots per workspace family,
- forbidden dependency roots and direct-crossing shortcuts,
- chat-native route naming alignment to `R1` through `R7`,
- Task Studio route naming alignment to `TS-SC-01` through `TS-SC-12`,
- explicit refusal of direct UI-to-worker execution,
- explicit refusal of `Acceptance Stack` or `Chat-to-Run Handoff` as new packages, services, or workers.

### 7.2 Fixture-rule expectations

The fixture-rule dataset should define:

- the accepted fixture families from the Phase 5 proof baseline,
- expected storage roots under `tests/fixtures/`,
- versioned-and-frozen dataset discipline,
- protocol-pack binding rules through `fixture_set_ref`,
- continuity expectations for regression, background parity, and handoff continuity.

### 7.3 Non-claim about executability

These datasets define validation truth and storage posture only.
They do not claim that every fixture family is already populated or that `P6.4` benchmark harnesses already exist.

## 8. Agent packet context-pack rules

### 8.1 Required packet-context segments

Later bounded agent packets should compile context packs from the following segment classes when applicable:

1. instruction stack (`AGENTS.md`, nearest descendant `AGENTS.md`, packet brief or explicit task scope),
2. governing accepted artifact refs and relevant source-authority refs,
3. workspace manifest and current-state datasets,
4. touched files and nearby local docs,
5. module-boundary contracts and fixture rules when validation or proof semantics materially apply,
6. supporting reads and bounded subagent findings only when `P0.5` permits them.

### 8.2 Assembly order

Packet-context assembly should follow this order:

1. instructions and scope boundary,
2. governing accepted truth,
3. manifest and current-state navigation data,
4. touched-file and local-doc reads,
5. contract, fixture, and validator datasets,
6. optional supporting reads or bounded subagent findings.

This order preserves the accepted local-doc-first rule and prevents broad search from becoming the default first move.

### 8.3 Budget alignment

Packet-context compilation must preserve `P0.5` budget bands:

- `narrow`: no subagent findings and minimal supporting reads,
- `standard`: one bounded read-only subagent at most,
- `extended`: broader but still single-packet work with explicit rationale.

If packet context would exceed the selected band, the packet must split or escalate rather than silently widen.

### 8.4 Hard exclusions

Packet-context compilation may not:

- pull non-accepted artifacts as default truth,
- treat runtime transcript continuity as sufficient replay basis,
- hide proof, delta, review, or approval semantics only in logs,
- infer semantic ownership from repo adjacency alone,
- collapse direct UI-to-worker or app-to-gateway shortcuts back into the execution basis.

## 9. Boundary locks for downstream work

1. `P6.4` may use the documentation plane to build pilot packets, benchmark inputs, or internal skills, but it may not reinterpret the accepted root-family ownership map.
2. `P6.5` should map release blueprints to the workspace families and route contracts already named here rather than inventing new planning roots.
3. `P6.6` should derive bounded execution packets from these manifest, current-state, contract, fixture, and packet-context rules rather than rediscovering scope case by case.
4. Future executable validators or generation wrappers may refine how these datasets are produced, but they must remain additive to the accepted pack and should not replace it as the governing truth.
5. If later semantic work changes root ownership, protocol fixture meaning, or packet-budget semantics, this pack should be marked stale and regenerated rather than patched ad hoc.

## 10. Downstream implications

### 10.1 For `P6.4`

- pilot packet work can name workspace families, current-state materialization, and validation/fixture roots from one accepted documentation plane,
- benchmark or adapter work can stay additive to the accepted Factory contract instead of using implementation convenience as topology.

### 10.2 For `P6.5`

- release blueprints can cite concrete workspace families, route-contract IDs, module-boundary contracts, and validation roots without inventing their own package map.

### 10.3 For `P6.6`

- bounded execution packets can compile smaller, explicit context packs from accepted manifests and current-state data,
- packet file scope can stay aligned to accepted workspace roots instead of broad repo guesses.

## 11. Review notes

Human review should confirm that this pack:

- mirrors the accepted `P6.2` root families into one documentation-plane layer without letting documentation redefine architecture,
- keeps manifest truth separate from the derived current-state view,
- makes boundary contracts, fixture rules, and packet context-pack guidance machine-usable without claiming later harnesses already exist,
- gives `P6.4` through `P6.6` one accepted navigation baseline for bounded implementation-facing work.
