# Phase 5 Workflow / Trigger / Applet / Pack / Integration Binding specs
Version: 1.0
Status: Accepted
Task: P5.4 — Workflow / Trigger / Applet / Pack / Integration Binding specs
Artifact ID: reuse.phase5-workflow-trigger-applet-pack-integration-binding-specs.v1
Reuse scope: Accepted reusable-execution composition pack covering workflow stage composition, trigger enablement, applet pinning, packaging/install rules, and scoped integration bindings

## 1. Purpose

This pack turns the accepted run-class protocol baseline into the full reusable-execution composition baseline.

It exists to:

- define how Workflow, Trigger, Applet, Pack / Extension, and Integration Binding objects compose accepted protocols instead of inventing a second execution stack,
- make version pinning, background enablement, packaging, install/export/update rules, and scoped external bindings machine-usable,
- lock the composition and binding rules that later Task Studio surface, V1 scope, and handoff packs must project unchanged.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- workflow stage composition and handoff rules,
- trigger kinds, enablement rules, and launch-target pinning,
- applet pinning, lifecycle, and background-run composition,
- Pack / Extension membership, install/import/export/update/retire rules,
- Integration Binding scope, capability, credential-binding, rotation, and rebinding rules,
- background parity, proof continuity, and Task Studio-safe handoff for composed reusable execution.

### Out of scope

- Task Studio layout, routing, or progressive-disclosure UI design,
- org-local connector catalogs or custom trigger taxonomies beyond the minimum kinds below,
- secret-store implementation details beyond scoped refs and rotation/rebinding rules,
- domain-specific packs or repo/code-domain packaging semantics,
- runtime implementation work beyond accepted architecture contracts.

## 3. Composition interpretation rules

### 3.1 Invariant-preservation rule

`reuse.phase5-run-class-protocol-packs.v1`, `reuse.phase5-governance-authority-writeback-spec.v1`, `reuse.phase5-proof-validation-evaluation-spec.v1`, `rel.r6-governed-agent-applet-chat-contract.v1`, and `rel.r7-commissioning-bridge-contract.v1` remain binding.
`GI-01` through `GI-10`, `PI-01` through `PI-10`, and `RC-07` remain the minimum floor for this deeper composition pack.
This pack deepens reusable-execution composition; it does not revise or bypass those accepted contracts.

### 3.2 Composition-not-ontology rule

Workflow, Trigger, Applet, Pack / Extension, and Integration Binding objects compose, route, install, or scope accepted run semantics.
They do not mint new run classes, replace Run / Proof Bundle / State Delta / Writeback Proposal objects, or create app-private substitutes for the shared substrate.

### 3.3 Exact-pinning and scoped-binding rule

Every reusable-execution composition object pins exact upstream versions and explicit binding refs.
There is no floating `protocol_version`, no hidden applet retargeting, no trigger retargeting by config convenience, and no inline secret material.
Integration Binding objects carry scoped capability and `credential_binding_ref` data, not authority on their own.

### 3.4 Background-parity and serious-work escalation rule

Triggered, workflow-driven, and applet-driven execution remains subject to the same proof, governance, and side-effect rules as interactive execution.
Composed background work still emits Run, Proof Bundle, State Delta, and Writeback Proposal objects where relevant, and serious work still resolves through `Commission -> Contract -> Run` rather than staying inside reusable-execution convenience wrappers.

### 3.5 Packaging-distinction rule

Pack / Extension is a reusable execution bundle distinct from Evidence Pack, Context Pack, prompt assets, and prompt adaptations.
Packaging may gather reusable execution objects and metadata together, but it does not replace the identity or lineage of the underlying Protocol, Workflow, Trigger, Applet, or Integration Binding objects.

## 4. Cross-object composition summary

| Object | Primary job | Must pin or bind | Default governance posture | Must not do |
| --- | --- | --- | --- | --- |
| Workflow | Compose ordered or staged protocol execution | Exact `protocol_id@protocol_version` stage refs, handoff rules, policy refs, optional context/strategy/integration refs | Inherits stage protocol defaults; may narrow only; no workflow-lane default writes | Invent a second workflow ontology or hide stage identity |
| Trigger | Start scheduled or event-driven reusable execution | Exact target `workflow` or `applet` version plus trigger policy and optional integration binding | Enablement remains explicit; writable/background use requires review | Widen authority or silently retarget to a newer version |
| Applet | Install governed reusable execution for manual or background launch | Exact entry protocol version, optional workflow version, context/strategy/trigger/policy refs | Install is inert until enablement; background parity remains binding | Float protocol versions or hide writes inside applet settings |
| Pack / Extension | Install, export, update, compare, or retire a reusable-execution bundle | Exact member versions, compatibility refs, lineage refs, binding-slot requirements | Packaging is explicit and attributable; install does not imply enablement | Become a second execution identity or masquerade as Evidence/Context Pack |
| Integration Binding | Scope external capability and credential binding for reusable execution | Explicit connector key, capability envelope, scope, and `credential_binding_ref` | Narrows what external access is possible; does not create authority | Carry inline secrets or cross-tenant credential reuse |

## 5. Shared composition contract model

### 5.1 Required refs and bindings

| Element | Contract |
| --- | --- |
| `protocol_ref@version` | Exact `protocol_id` plus `protocol_version` pin for any composed run stage |
| `workflow_ref@version` | Exact `workflow_id` plus `workflow_version` pin when a Trigger or Applet targets a Workflow |
| `applet_ref@version` | Exact `applet_id` plus `applet_version` pin when a Trigger or Pack references an Applet |
| `context_recipe_ref` | Optional reusable context assembly ref; may narrow basis only |
| `strategy_preset_ref` | Optional reusable strategy ref; may narrow ordering/refusal only |
| `verifier_pack_ref` + `fixture_set_ref` | Explicit proof/evaluation attachments carried forward from the pinned protocol packs |
| `policy_binding_refs` | Explicit policy and reviewable constraint refs active for the composed object |
| `authority_scope_ref` | Required whenever composed execution reads or writes beyond the default wedge |
| `contract_ref` | Required whenever composed execution is commissioned or requests writable consequential behavior |
| `review_hook_set` | Explicit review-trigger vocabulary inherited from the pinned protocol packs plus any composition-specific background or export hooks |
| `integration_binding_ref` | Scoped reusable external-capability binding ref; never secret material |
| `credential_binding_ref` | Typed gateway/external credential ref resolved through Integration Binding or equivalent scoped binding path |
| `pack_membership_refs` | Exact member refs and version pins for Pack / Extension membership |
| `lineage_refs` | Install/import/export/update/rebind lineage required for pack, applet, trigger, and binding history |
| `handoff_context_refs` | Linked workflow/applet/trigger/pack/binding refs preserved into R7 and Task Studio handoff payloads |

### 5.2 Pinning, versioning, and lifecycle rules

1. Workflow stages, Trigger launch targets, Applet entry points, and Pack members pin exact upstream versions.
2. Material change to stage order, target refs, bound protocol versions, capability envelope, required binding slots, or exported manifest semantics creates a new semantic version or new revision record before later execution.
3. Enable/disable/pause/install/retire lifecycle transitions alone do not rewrite semantic version history.
4. Repointing a Trigger or Applet to a different protocol/workflow version is a material change, not a live toggle.
5. Pack install/import/export/update/retire events remain explicit lifecycle history; install never implies enablement or authority grant.
6. Secret rotation or integration rebinding creates a new binding revision or new secret ref and invalidates gateway/session caches without rewriting historical runs.

### 5.3 Governance, proof, and writeback binding rules

1. Workflow, Trigger, and Applet objects inherit the pinned protocol defaults and may narrow behavior only.
2. `background_enablement_review` is required before writable or consequential background execution becomes enabled.
3. Every launch created by a Workflow, Trigger, or Applet still emits Run, Proof Bundle, State Delta, and Writeback Proposal objects where the pinned protocol pack requires them.
4. No composition object may default to mixed-lane writeback; workflow, memory, canon, and export persistence remain separate lanes.
5. A composed object may not authorize scope widening on its own; widened reads or writes still require the accepted Authority Scope and Contract path.
6. Proof minima, evaluator thresholds, fixtures, and failure mappings from the pinned protocol packs remain binding in background, replay, and Task Studio projections.
7. Queue / Inbox, Board, Live Monitor, Ledger, and Browser / Library surfaces only project these objects and their linked runs; they do not become the semantic source of truth.

### 5.4 Scoped credential and secret-separation rules

1. Integration Binding records connector identity, scope boundary, capability envelope, policy refs, and `credential_binding_ref`; it does not store authority or acceptance policy.
2. Secret material lives only in the secret / credential store and is referenced through scoped refs; secrets never live in workflow, trigger, applet, or pack manifests.
3. Workers and gateways resolve `credential_binding_ref` at execution time through scoped service identities and tenant-aware binding lookup.
4. Pack import/export may carry required binding slots, compatibility requirements, and capability expectations, but never live secrets.
5. Cross-tenant or out-of-scope binding reuse is forbidden even if a connector key or pack identity matches.

### 5.5 Background parity and handoff continuity rules

1. Triggered, workflow-driven, and applet-driven runs preserve `protocol_id`, `protocol_version`, `run_class`, `workflow_id`, `applet_id`, `trigger_id`, `pack_id`, and linked `integration_binding_ref` values as explicit refs where present.
2. Blocked background launches still emit inspectable failure basis, run-status history, and any required proof/delta state rather than disappearing into scheduler logs.
3. R7 and Task Studio handoff preserves workflow/applet/trigger/pack context as linked refs with shared IDs instead of recreating reusable execution as app-local state.
4. Rebinding, rotation, disablement, or superseding install actions append new history; they do not rewrite earlier launch or handoff lineage.

## 6. Object specs

### 6.1 Workflow

| Dimension | Contract |
| --- | --- |
| Object identity | `workflow_id` is stable; material composition changes create a new `workflow_version` or new workflow lineage record |
| Required bindings | Ordered `stage_protocol_refs@versions`, stage-local `context_recipe_ref?`, `strategy_preset_ref?`, `verifier_pack_ref?`, `integration_binding_ref?`, `policy_refs`, and explicit `handoff_rules` |
| Stage contract | Entry criteria, stage transitions, retry/replay posture, pause points, child-run linkage, and stage-local review hooks are explicit and inspectable |
| Governance posture | Workflow inherits pinned protocol defaults, may narrow only, never defaults workflow-lane writes, and still requires Authority Scope / Contract when serious or writable work is in play |
| Proof / continuity posture | Each stage launch emits its own Run / Proof Bundle / State Delta / Writeback Proposal objects as required; workflow Board and Live Monitor views are derived projections only |
| Packaging posture | Workflow may be a Pack / Extension member, but pack install does not auto-approve, auto-run, or auto-enable it |
| Fixture focus | Multi-stage handoff, blocked approval between stages, background parity, and R7 / Task Studio handoff continuity |

### 6.2 Trigger

| Dimension | Contract |
| --- | --- |
| Object identity | `trigger_id` is stable; material change to launch target, trigger kind, scope, or capability envelope creates a new `trigger_version` |
| Required bindings | `trigger_kind` is at minimum `schedule` or `event`; each trigger pins one `workflow_ref@version` or `applet_ref@version`, plus `policy_refs`, optional `integration_binding_ref`, and enablement history |
| Launch contract | A trigger launch instantiates the pinned target with explicit launch basis, trigger context, and frozen target version refs rather than resolving dynamically at fire time |
| Governance posture | Enable/disable is explicit; writable or consequential launches require `background_enablement_review`; hidden retries or backoff behavior may not widen authority or bypass review |
| Proof / continuity posture | Triggered runs keep the same proof/evaluator minima as interactive runs, and blocked launches remain inspectable through run or scheduler-linked records rather than silent drops |
| Packaging posture | Trigger may be packaged, but packaged triggers remain inert until the tenant installs the pack and explicitly enables the trigger |
| Fixture focus | Scheduled run, event-driven run, blocked scope, disabled trigger, and background parity scenarios |

### 6.3 Applet

| Dimension | Contract |
| --- | --- |
| Object identity | `applet_id` is stable; material change to pinned protocol/workflow version, bound context/strategy refs, or policy bindings creates a new `applet_version` |
| Required bindings | Exact entry `protocol_ref@version`, optional `workflow_ref@version`, optional `trigger_ref@version`, optional `context_recipe_ref`, optional `strategy_preset_ref`, `policy_binding_refs`, optional `integration_binding_refs`, optional `pack_ref` |
| Launch contract | Manual or triggered applet launches instantiate runs from the pinned protocol/workflow and explicit bound refs; applet settings may not retarget to a newer protocol behind the same applet state |
| Governance posture | Applets may narrow protocol defaults only; enabling writable background behavior requires `background_enablement_review`; no hidden memory, canon, workflow, or export write posture appears through applet config |
| Proof / continuity posture | Interactive and background applet runs emit the same Run / Proof Bundle / State Delta / Writeback Proposal objects, and R7 handoff preserves linked applet/protocol context |
| Packaging posture | Applets are installable and packageable, but pack membership or installation never bypasses enablement, review, or pinned version checks |
| Fixture focus | Installed vs enabled applet, paused applet, background-run parity, protocol-version pin stability, and Task Studio handoff continuity |

### 6.4 Pack / Extension

| Dimension | Contract |
| --- | --- |
| Object identity | `pack_id` is stable; member-set or compatibility changes create a new `pack_version` and explicit lineage record |
| Required bindings | Exact `member_refs@versions`, compatibility refs, install/update/import/export policy refs, lineage refs, optional required binding slots, and optional manifest refs |
| Packaging contract | Pack / Extension bundles Protocols, Workflows, Triggers, Applets, Context Recipes, Strategy Presets, Verifier Packs, and related reusable-execution metadata as an installable/exportable unit |
| Governance posture | Install, import, export, update, and retire events remain explicit history; install does not imply enablement; external export/import side effects require the appropriate lane-local review path |
| Proof / continuity posture | Pack compare/diff uses explicit member versions and lineage; exported manifests preserve refs and compatibility metadata without replacing the identity of the bundled objects |
| Boundary lock | Pack / Extension is not Evidence Pack, Context Pack, prompt asset, prompt card, or app-private ontology wrapper |
| Fixture focus | Install, update, pack diff, export/import lineage, and required-binding-slot validation |

### 6.5 Integration Binding

| Dimension | Contract |
| --- | --- |
| Object identity | `integration_binding_id` is stable; capability or target-scope changes create a new binding revision, while pure secret rotation creates a new linked secret ref and rotation history |
| Required bindings | `binding_scope`, `connector_key`, `capability_refs`, `credential_binding_ref`, `policy_refs`, `allowed_target_refs`, optional `secret_ref`, and optional `rotation_metadata_ref` |
| Binding contract | Integration Binding scopes external capability for tool or integration use through tenant/workspace-aware refs; it may narrow which protocols, workflows, triggers, or applets can invoke the binding |
| Governance posture | Integration Binding does not authorize execution on its own; widening capability envelope or target scope requires explicit reviewable change and may require a new Authority Scope / Contract path |
| Proof / continuity posture | Runs record binding refs and side-effect preview lineage; secret rotation, rebinding, disablement, or revocation append new history rather than rewriting prior run or handoff records |
| Packaging posture | Packs may declare required binding slots or compatible connector requirements, but pack transport never carries live secret material |
| Fixture focus | Binding resolution, secret rotation, rebinding, blocked missing binding, tenant leakage prevention, and inspectable external side-effect preview |

## 7. Scenario and shortcut grounding

| Composition area | Strongest scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| Workflow / Trigger / Applet composition and background parity | `SS-08`, `SS-12`, `GS-10`, `GS-11`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-separate-backend-per-view` |
| Commissioning continuity and Task Studio handoff for composed work | `SS-05`, `SS-09`, `GS-12`, `GS-13`, `GS-14`, `EC-06`, `EC-07` | `fs.no-master-chat-truth`, `fs.no-silent-proposal-application` |
| Pack / Extension lineage and prompt-identity separation | `GS-08`, `GS-09`, `GS-15`, `EC-04`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-separate-backend-per-view` |
| Scoped integration binding and external-tool discipline | `GS-11`, `GS-13`, `EC-05`, `EC-06`, `EC-07` plus inherited gate checks `PG-07` and `PG-09` | `fs.no-agent-builder-first`, `fs.no-silent-proposal-application` |

## 8. Boundary locks for downstream work

1. `P5.5` must project these exact Workflow, Trigger, Applet, Pack / Extension, and Integration Binding objects, refs, and pinned versions into Task Studio surfaces instead of inventing view-local substitutes.
2. `P5.6` may narrow V1 trigger kinds, pack exposure, or binding UX, but it may not redefine the semantic contracts in this pack.
3. `P5.7` must preserve linked workflow/applet/trigger/pack/binding context as shared refs through the commissioning-bridge handoff rather than recreating them as app-local metadata.
4. Future domain packs may add domain-specific connectors or package members, but they may not back-edit shared-environment ownership or introduce inline secrets, floating versions, or hidden authority.
5. Evidence Pack, Context Pack, prompt assets, and Pack / Extension remain distinct object families with distinct lineage and governance behavior.

## 9. Downstream implications

### 9.1 For P5.5

- Task Studio surface and lifecycle contracts should treat Board, Queue / Inbox, Browser / Library, Live Monitor, Ledger, and Inspector views as projections over these composition objects and their linked runs,
- Task Studio app flows should pin the same protocol/workflow/applet versions and binding refs defined here rather than deriving app-private execution state.

### 9.2 For P5.6 and P5.7

- V1 scope and commissioning-handoff work should use this pack as the reusable-execution composition baseline for trigger kinds, applet packaging, required binding slots, background parity, and handoff continuity,
- later handoff or scope packs may narrow exposure, but they should not reopen exact-version pinning, scoped binding, or pack-distinction rules.

## 10. Review notes

Human review should confirm that this pack:

- makes recurring and packaged work compose from the accepted run model instead of inventing a separate ontology,
- preserves exact protocol/workflow/applet/pack pinning and scoped integration binding semantics,
- keeps secrets and credential bindings separated from reusable-execution metadata,
- preserves background parity, governance continuity, and Task Studio-safe handoff for composed work.
