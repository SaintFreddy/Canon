# Phase 6 repo/package architecture and agent execution rules pack
Version: 1.0
Status: Accepted
Task: P6.2 — Repo/package architecture and agent execution rules
Artifact ID: surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1
Surface scope: Accepted Phase 6 repo/package architecture and agent execution rules pack mapping accepted runtime planes, package seams, route contracts, and Factory execution discipline onto one implementation-facing repo layout

This artifact is accepted for downstream use.
It turns the accepted architecture, release, handoff, and surface-contract baseline into one repo/package and execution plan for later implementation-facing work.
It does not create release blueprints, packet manifests, or runtime code.

## 1. Purpose

This pack exists to:

- map the accepted logical package seams and runtime planes onto one concrete repo layout and workspace family map,
- define the concrete package, service, worker, app, and reserved-domain boundaries that later implementation work must follow,
- state the module contract requirements that keep chat-native releases, Task Studio, gateways, workers, and later domains aligned to accepted semantics,
- define the additive agent execution rules that later Factory-first packets, blueprints, and scaffolding work must inherit.

## 2. Scope boundaries

### In scope

- the implementation-facing top-level repo layout for app, package, service, worker, test, and script roots,
- the concrete mapping from accepted logical package seams to workspace roots,
- module-family dependency and ownership rules,
- additive agent execution rules for future bounded implementation work,
- boundary locks that downstream documentation-plane, benchmark, blueprint, and packet work must inherit.

### Out of scope

- changing accepted semantic ownership, release doctrine, Task Studio meaning, or R7 handoff meaning,
- concrete URL paths, component trees, or release-by-release implementation blueprints,
- generated manifests, current-state views, or packet context manifests that belong to `P6.3`,
- pilot packet sets, benchmark harnesses, skills/adapters, or tuning notes that belong to `P6.4`,
- packet templates and file whitelists that belong to `P6.6`,
- P0.5 packet-budget or context-budget policy changes.

## 3. Repo/package interpretation rules

### 3.1 Architecture-before-layout rule

Repo shape follows accepted runtime planes, typed boundaries, release maturity, and handoff truth.
File placement may express those seams; it may not invent them.

### 3.2 Logical-seam-preservation rule

The accepted `P4.1` logical package areas remain the mandatory seam baseline.
Concrete workspaces may split a logical seam into contract and runtime roots, but they may not silently collapse two accepted seams into one convenience package.

### 3.3 One-control-plane-and-event-spine rule

Concrete repo layout must preserve one shared control plane and one shared event/provenance spine.
No package boundary may reintroduce direct UI-to-worker execution, per-view backends, or a second orchestration stack.

### 3.4 Surface-modules-are-projections rule

Chat-native clusters and Task Studio route modules remain projections over the accepted shared object model and shared grammar.
They may compose, alias, and arrange shared semantics, but they may not create app-private truth or route-local replacements for shared objects such as `Run`, `Proof Bundle`, `State Delta`, `Writeback Proposal`, or `Commission`.

### 3.5 Additive-agent-rules rule

This pack extends accepted `P0.2` and `P0.3` execution discipline into later implementation work.
It may add workspace-targeting and module-boundary rules, but it may not smuggle P0.5 packet-budget policy, release-private semantics, or human-owned product decisions into repo automation.

### 3.6 Reserved-root-not-scaffolded rule

`P6.2` reserves the root families and boundary rules below.
Later work may create those roots gradually, but it should not invent alternate top-level roots for the same concerns without a new accepted delta.

## 4. Top-level repo layout contract

| Root family | Role in the repo | Current posture and boundary |
| --- | --- | --- |
| `docs/control-plane/` | Accepted planning/spec control plane | Already present; remains the accepted truth plane for planning and architecture artifacts |
| `/.factory/` | Repo-scoped Factory execution assets | Already present; remains additive execution tooling, not product architecture |
| `apps/` | First-party app projection workspaces | Reserved for `chat-native` and `task-studio` app implementations over shared grammar and shared objects |
| `packages/` | Shared contracts, schemas, object APIs, grammar/runtime support packages | Reserved for reusable code that must stay below app projections and above service/worker implementations |
| `services/` | Environment shell, control plane, gateways, review/writeback, event/provenance entrypoints | Reserved for request/query/dispatch seams and adapter services |
| `workers/` | Bounded execution worker families | Reserved for run, compiler, replay, validation, and apply workers |
| `domains/` | Later domain-pack implementation roots | Reserved only after the accepted later-domain semantic gates are satisfied; not pre-approved implementation scope today |
| `tests/` | Contract tests, replay/regression suites, fixtures, and benchmark datasets | Reserved for test and fixture assets that validate accepted seams rather than redefining them |
| `scripts/` | Repo-local validator and generation wrappers | Reserved for thin wrappers around accepted validators and generators; not a second control plane |

Top-level layout rules:

1. No new top-level runtime root should be introduced for an already-owned concern without a new accepted delta.
2. First-party app projections land under `apps/`; future domain packs land under `domains/` only after their semantic gates are satisfied.
3. A workspace root may be empty until later implementation work lands, but its reserved ownership boundary begins here.
4. `docs/control-plane/` and `/.factory/` remain special: they govern repo truth and execution discipline, not runtime product ownership.

## 5. Concrete package and service seam map

### 5.1 Logical package areas -> concrete workspace roots

| Accepted logical seam | Concrete workspace roots to preserve it | Minimum responsibility | Must not absorb |
| --- | --- | --- | --- |
| `pkg.shared-object-api` | `packages/shared-object-schemas/`, `packages/shared-object-api/` | Stable shared refs, typed object APIs, identity-preserving query models | App-private aliases, worker orchestration, gateway adapters |
| `pkg.environment-control` | `packages/environment-control-contracts/`, `services/environment-shell-api/`, `services/execution-control/` | Admission, scoped queries, replay/branch requests, monitor subscriptions, orchestration dispatch | UI rendering, provider transcript continuity, worker-local semantics |
| `pkg.context-compiler` | `packages/context-compiler-contracts/`, `workers/context-compiler/` | Evidence/context lifecycle, compiler diagnostics, frozen admitted-basis handling | App-specific context stories, silent memory/canon injection |
| `pkg.event-provenance-spine` | `packages/event-provenance-contracts/`, `services/event-provenance/` | Event envelopes, lineage queries, replay cursors, provenance materialization | View-owned truth, stage-private audit history |
| `pkg.review-writeback` | `packages/review-writeback-contracts/`, `services/review-writeback/`, `workers/apply-writeback/` | Lane-local proposal, review, approval, apply, and compensation orchestration | Generic save behavior, mixed-lane mutation shortcuts |
| `pkg.replay-compare` | `packages/replay-compare-contracts/`, `workers/replay-compare/` | Checkpoint, replay, compare, basis-diff, and branch lineage work | Transcript cloning, mode-private replay logic |
| `pkg.model-gateway` | `packages/model-gateway-contracts/`, `services/model-gateway/` | Typed provider invocation, normalization, usage/failure accounting | Durable product truth, app/private route semantics |
| `pkg.tool-gateway-sandbox` | `packages/tool-gateway-contracts/`, `services/tool-gateway/`, `workers/tool-sandbox/` | Typed tool execution, side-effect previews, scoped credentials, sandbox isolation | Policy authorship, cross-tenant credential reuse, direct app coupling |
| `pkg.monitor-inspect` | `packages/monitor-inspect/` | Inspect-query models, monitor summaries, ledger-facing and inspector-facing view models over authoritative refs | Alternate truth stores, console-only semantics |

### 5.2 Cross-cutting app and grammar workspaces

| Workspace root | Role | Governing accepted baseline |
| --- | --- | --- |
| `packages/projection-grammar/` | Shared grammar primitives, alias resolution, companion composition, and route-cluster helpers used by all apps | `sem.phase2-projection-grammar-contracts.v1` and accepted `surf.phase6-*` packs |
| `apps/chat-native/` | R1-R7 release-cluster projections over shared objects and shared grammar | `surf.phase6-chat-native-surface-contract-pack.v1` |
| `apps/task-studio/` | `TS-SC-01` through `TS-SC-12` route modules and lifecycle-primary Task Studio projections | `surf.phase6-task-studio-surface-contract-pack.v1` |
| `domains/<domain-slug>/` | Future domain-pack implementation roots after semantic gates are accepted | `surf.phase6-later-domain-surface-backlog-contract-pack.v1` plus future domain object packs |

These cross-cutting workspaces do not replace the accepted logical seams above.
They arrange those seams into projection or domain-facing implementation surfaces.

## 6. Module contract requirements

### 6.1 Workspace-family dependency matrix

| Workspace family | Allowed responsibilities | May depend on | Must not depend on |
| --- | --- | --- | --- |
| `apps/chat-native/` route/cluster modules | Release-cluster projections, local draft UX, shared grammar composition, deep-link routing | `packages/projection-grammar/`, `packages/shared-object-api/`, `packages/monitor-inspect/`, typed contracts from `packages/*-contracts/` | `workers/*`, gateway internals, storage internals, app-private truth stores |
| `apps/task-studio/` route modules | `TS-SC-*` surface composition, lifecycle routing, deep-link continuity, shared inspector/ledger composition | `packages/projection-grammar/`, `packages/shared-object-api/`, `packages/monitor-inspect/`, typed contracts from `packages/*-contracts/` | `workers/*`, gateway internals, Task-Studio-only shared-object replacements |
| `packages/*-contracts/` | Versioned schemas, envelopes, refs, query/command/job/gateway contracts | `packages/shared-object-schemas/` and other schema-only packages where required | `apps/*`, `services/*`, `workers/*` runtime code |
| `packages/projection-grammar/` and `packages/monitor-inspect/` | Shared projection/runtime helpers over accepted grammar and inspect semantics | `packages/shared-object-api/`, schema-only packages | Service dispatch, worker logic, gateway adapters, domain-private semantics |
| `services/environment-shell-api/`, `services/execution-control/`, `services/review-writeback/`, `services/event-provenance/` | Query composition, admission, review/apply routing, event publication, lineage queries | relevant `packages/*-contracts/`, `packages/shared-object-api/`, storage adapters behind service-local seams | `apps/*` route code, component trees, gateway-private adapters outside typed contracts |
| `services/model-gateway/` and `services/tool-gateway/` | Adapter execution, normalization, usage/failure accounting, sandbox routing | their own contract packages, adapter libraries, scoped credential helpers | App route code, shared object authorship, product review/approval semantics |
| `workers/*` | Bounded job execution over frozen refs, compiler/replay/validation/apply work | `packages/shared-object-api/`, relevant `packages/*-contracts/`, gateway contracts | App projections, UI-only helpers, route-local state |
| `domains/<domain-slug>/` | Future domain-specialized projections and packages after semantic gates pass | accepted shared packages and future domain-specific contracts | Re-owning shared commissioned-work objects or shared grammar families |

### 6.2 Route and cluster naming rules

1. Chat-native modules should align to accepted release clusters rather than inventing per-surface backends: e.g. `r1-conversation`, `r2-context-control`, `r3-branch-replay`, `r4-artifact-workspace`, `r5-prompt-assets`, `r6-governed-reusable-execution`, and `r7-commissioning-bridge`.
2. Task Studio route modules should align to accepted `TS-SC-01` through `TS-SC-12` route-contract IDs rather than ad hoc page names.
3. `Acceptance Stack` remains an alias/composition inside chat-native route code only; it may not become its own shared object package, service, or worker family.
4. `Chat-to-Run Handoff` remains a routing/deep-link envelope only; it may not become a new persistence package, import/export pipeline, or app-private transfer service.

### 6.3 Boundary-enforcement rules

1. Client/app code reaches consequential work through typed environment/control contracts only; no direct UI-to-worker RPC is allowed.
2. Control services dispatch typed job envelopes to workers and typed gateway envelopes to model/tool gateways; they do not import app route modules for business meaning.
3. Workers operate on frozen refs and typed contracts; they do not reach into app projection code, route-local state, or provider transcript continuity.
4. Gateway packages normalize model/tool execution and failures, but they do not own durable product truth, review state, or app semantics.
5. Any future implementation that needs to cross one of these rules requires a new accepted delta rather than a local convenience exception.

## 7. Agent execution rules for implementation-facing work

### 7.1 Truth and instruction precedence

1. Accepted source-authority artifacts and accepted control-plane artifacts remain the default repo truth.
2. Root `AGENTS.md` and nearest descendant `AGENTS.md` files remain the execution-projection layer for humans and agents.
3. New implementation roots should add descendant `AGENTS.md` files only when narrower local rules are actually needed; those files may narrow scope but may not widen accepted truth.

### 7.2 Bounded workspace targeting

1. Every future implementation packet or explicit task should name the governing accepted artifact refs plus the workspace roots or file whitelist it may touch.
2. Cross-root changes are allowed only when the packet or task scope names every touched root explicitly.
3. If work changes an accepted artifact or adds a new accepted artifact, it must synchronize `docs/control-plane/artifact-registry.seed.json`, `docs/control-plane/dependency-graph.seed.json`, and the relevant `master-plan.md` status/carry-forward entries.

### 7.3 Headless Factory defaults

1. Repo-scoped headless runs use `droid exec --cwd <repo-root>`.
2. Read-only/spec-first behavior remains the default for analysis, planning, and review work.
3. Mutating work should remain `--auto low` unless real validators require a reversible repo-local build/test/install path, in which case `--auto medium` may be used within scope.
4. `--auto high`, `--skip-permissions-unsafe`, push/deploy authority, and silent scope widening remain disallowed by default.

### 7.4 Validation and review discipline

1. Before completion, run the real validators that exist for the touched files.
2. Until `P6.3` introduces generated wrappers, the minimum validation baseline for control-plane and packet work remains:
   - JSON parse for edited `.json` files,
   - registry/graph integrity verification,
   - validation-hook, edge-type, and stale-rule catalog checks,
   - cross-pack consistency review against the accepted governing artifacts.
3. Do not mark status done, append carry-forward entries, or commit accepted-artifact changes until deliverables exist and validators pass.
4. Review git status and diffs before commit so scope drift, stale wording, or accidental changes are caught before landing.

### 7.5 Boundary refusals

Agents may not use repo/package convenience to:

- infer semantic ownership from file placement,
- bypass the control plane with direct UI-to-worker behavior,
- create a second orchestration stack in code or automation,
- hide proof, delta, review, or writeback semantics only in `Console` or logs,
- reinterpret accepted handoff or route contracts as import/export or app-private state shells.

## 8. Boundary locks for downstream work

1. `P6.3` may add manifests, generated current-state views, and documentation-plane structure inside these roots, but it may not redefine their ownership roles.
2. `P6.4` may add skills, adapters, and benchmark harnesses, but those assets must land under the root families above and preserve the same execution and boundary rules.
3. `P6.5` release blueprints should cite workspace roots and logical seams from this pack instead of inventing new top-level package families per release.
4. `P6.6` execution packets should whitelist these roots and module families explicitly rather than treating the repo as one undifferentiated write target.
5. Future domain work remains gated by accepted later-domain semantic packs; `domains/` is reserved, not pre-approved scope.

## 9. Downstream implications

### 9.1 For `P6.3`

- the documentation plane should mirror these workspace families and generate current-state/manifests against them,
- module contract files, fixture rules, and packet-compiled context guidance should assume this layout instead of rediscovering it.

### 9.2 For `P6.4`

- pilot packets and benchmark work should use this pack as the workspace-targeting and boundary baseline,
- any new Factory skill or adapter should remain additive to the accepted `/.factory/` contract and should not backfill product architecture from automation convenience.

### 9.3 For `P6.5` and `P6.6`

- release blueprints should map touched modules to the workspace roots named here,
- execution packets should package work against these roots, logical seams, and module-boundary rules rather than against ad hoc file trees.

## 10. Review notes

Human review should confirm that this pack:

- maps the accepted runtime planes and `P4.1` logical seams onto one concrete repo/package layout without letting layout dictate architecture,
- keeps chat-native clusters, Task Studio route modules, gateways, workers, and later-domain roots inside clear boundary lines,
- extends accepted P0.2/P0.3 execution discipline without importing P0.5-only packet-budget policy,
- gives `P6.3` through `P6.6` one accepted package and agent-execution baseline for later implementation-facing work.
