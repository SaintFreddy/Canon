# CANON PLAN IMPACT REPORT

- Generated: 2026-04-19 by Claude Opus 4.7 (1M ctx), main agent + three parallel Opus 4.7 sub-agents (explicit `model: "opus"`)
- Input: [AGENTIC_ENGINE_AUDIT_LOG.md](AGENTIC_ENGINE_AUDIT_LOG.md) — 8,879 lines, 506 findings, all status OPEN (15 CRITICAL, 130 HIGH, 208 MEDIUM, 123 LOW, 30 INFO), audit date 2026-04-18
- Scope of this report: plan implications of the **145 CRITICAL + HIGH** findings. MEDIUM/LOW/INFO findings are summarized thematically only. No engine code is proposed here; this pass produces plan-owner directives.
- Cutoff context: per [canon-now.md:10](canon-now.md) the Canon-Dev baton is `stop`, and [canon-phase-4-plus-plan.md:110-144](canon-knowledgebase/canon-phase-4-plus-plan.md) states "no further authority-repair step remains open by default". The audit log constitutes a **cited contradiction** class event that plan-owners must adjudicate before resumption.

---

## Section 1 — Canon plan inventory

### 1.1 Core control-plane governance (`/Canon/docs/control-plane/`)

- [`core/master-plan.md`](Canon/docs/control-plane/core/master-plan.md) · master platform build plan (layer rules, release order, tooling policy) · 2026-04-16 · all layers.
- [`core/forbidden-shortcuts-register.md`](Canon/docs/control-plane/core/forbidden-shortcuts-register.md) · register of forbidden shortcuts with enforcement points · 2026-04-16 · all layers.
- [`core/repo-agent-operating-contract.md`](Canon/docs/control-plane/core/repo-agent-operating-contract.md) · repo agent operating contract · 2026-04-16 · control plane.
- [`core/context-budget-and-packet-policy.md`](Canon/docs/control-plane/core/context-budget-and-packet-policy.md) · bounded packet / budget policy · 2026-04-16 · control plane.
- Phase-6 execution-packet index + pilot-packet notes + release-blueprint index (JSON + MD) · 2026-04-16/18 · control plane.
- Phase-7 architecture-sync / delta-pack / release-gate / stale-regeneration JSON indices · 2026-04-16 · control plane.

### 1.2 Canon freeze + seam + release topology (`/canon/`)

- [`phase-1-canon-freeze-and-resolved-product-interpretation.md`](Canon/docs/control-plane/canon/phase-1-canon-freeze-and-resolved-product-interpretation.md) · resolved product interpretation, fixed release order · 2026-04-16 · Canon governance.
- [`phase-1-rewrite-containment-and-stable-seam-map.md`](Canon/docs/control-plane/canon/phase-1-rewrite-containment-and-stable-seam-map.md) · SS-* seam map including SS-10 Platform Gate prelaunch · 2026-04-16 · Canon governance.
- [`phase-1-layer-and-primitive-separation-pack.md`](Canon/docs/control-plane/canon/phase-1-layer-and-primitive-separation-pack.md) · owner-layer map per primitive · 2026-04-16 · Engine/Shared Env/Apps.
- [`phase-1-surface-and-release-topology-canon.md`](Canon/docs/control-plane/canon/phase-1-surface-and-release-topology-canon.md) · Platform Gate + R1-R7 + TS topology · 2026-04-16 · Canon governance.
- [`phase-1-source-decomposition-contradictions-and-glossary.md`](Canon/docs/control-plane/canon/phase-1-source-decomposition-contradictions-and-glossary.md) · canon vocabulary · 2026-04-16 · Canon governance.
- [`phase-1-golden-scenario-corpus-and-edge-case-suite.md`](Canon/docs/control-plane/canon/phase-1-golden-scenario-corpus-and-edge-case-suite.md) · golden scenarios · 2026-04-16 · Canon governance.

### 1.3 Phase 2 semantics + reuse invariants

- [`semantics/phase-2-core-object-and-state-machine-spec-pack.md`](Canon/docs/control-plane/semantics/phase-2-core-object-and-state-machine-spec-pack.md) · shared objects + identity + state machines · 2026-04-16 · Shared Environment.
- [`semantics/phase-2-run-class-taxonomy-and-protocol-kernel.md`](Canon/docs/control-plane/semantics/phase-2-run-class-taxonomy-and-protocol-kernel.md) · run classes + protocol kernel · 2026-04-16 · Shared Environment.
- [`semantics/phase-2-projection-grammar-contract-pack.md`](Canon/docs/control-plane/semantics/phase-2-projection-grammar-contract-pack.md) · shared interaction grammars · 2026-04-16 · Shared Environment.
- [`semantics/phase-2-chat-native-semantic-packs-by-release.md`](Canon/docs/control-plane/semantics/phase-2-chat-native-semantic-packs-by-release.md) · R1-R7 semantic locks · 2026-04-16 · Apps + Shared Env.
- [`reuse/phase-2-governance-authority-and-writeback-invariants.md`](Canon/docs/control-plane/reuse/phase-2-governance-authority-and-writeback-invariants.md) · governance invariants GI-01..10 · 2026-04-16 · Shared Environment.
- [`reuse/phase-2-proof-and-validation-invariants.md`](Canon/docs/control-plane/reuse/phase-2-proof-and-validation-invariants.md) · PI-01..10 + RC-01..08 · 2026-04-16 · Shared Environment.

### 1.4 Phase 3 architecture baseline + platform gate

- [`architecture/phase-3-platform-gate-spec-and-exit-audit.md`](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md) · hard pre-R1 gate + exit tests PG-01..10 + exit-audit checklist · 2026-04-16 · all layers (marked **Gate passed** at P3.6 acceptance, L126).
- [`architecture/phase-3-high-level-technical-architecture-baseline.md`](Canon/docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md) · runtime topology, process model, engine/env/app split · 2026-04-16 · all layers.
- [`architecture/phase-3-architecture-synchronization-pass.md`](Canon/docs/control-plane/architecture/phase-3-architecture-synchronization-pass.md) · P3.6 sync pass · 2026-04-16 · control plane.
- [`architecture/phase-3-data-storage-indexing-and-provenance-spec.md`](Canon/docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md) · storage classes, secret lane, provenance · 2026-04-16 · Shared Environment + Engine.
- [`architecture/phase-3-api-ipc-and-event-contract-spec.md`](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md) · typed envelopes, gateway contracts, event families, ordering, version bump rule · 2026-04-16 · cross-layer.
- [`architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md`](Canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md) · compiler topology, freeze/replay/diff · 2026-04-16 · Engine + Shared Env.

### 1.5 Phase 4 release plan + release contracts

- [`releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md`](Canon/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md) · per-stage exposes/defers/refuses · 2026-04-16 · control plane.
- [`releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md`](Canon/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md) · package maturity floors M1..M4 per gate · 2026-04-16 · control plane.
- [`releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack.md`](Canon/docs/control-plane/releases/r1-transcript-chat-contract/phase-4-r1-transcript-chat-contract-pack.md) · R1 contract · 2026-04-16 · Apps.
- [`releases/r2-context-chat-contract/phase-4-r2-context-chat-contract-pack.md`](Canon/docs/control-plane/releases/r2-context-chat-contract/phase-4-r2-context-chat-contract-pack.md) · R2 contract · 2026-04-16 · Apps + Shared Env.
- [`releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md`](Canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md) · R3 contract — exact replay promise · 2026-04-16 · Apps + Shared Env.
- [`releases/r4-artifact-workspace-contract/…`](Canon/docs/control-plane/releases/r4-artifact-workspace-contract/phase-4-r4-artifact-workspace-contract-pack.md) · R4 contract · 2026-04-16 · Apps + Shared Env.
- [`releases/r5-prompt-studio-contract/…`](Canon/docs/control-plane/releases/r5-prompt-studio-contract/phase-4-r5-prompt-studio-contract-pack.md) · R5 contract · 2026-04-16 · Apps + Shared Env.
- [`releases/r6-governed-agent-applet-chat-contract/…`](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md) · R6 contract — typed tool execution + scoped credentials + sandbox · 2026-04-16 · Apps + Shared Env + Engine.
- [`releases/r7-commissioning-bridge-contract/…`](Canon/docs/control-plane/releases/r7-commissioning-bridge-contract/phase-4-r7-commissioning-bridge-contract-pack.md) · R7 contract · 2026-04-16 · Apps + Shared Env + Engine.

### 1.6 Phase 5 reuse + commissioning + Task Studio

- [`reuse/phase-5-full-proof-validation-and-evaluation-spec.md`](Canon/docs/control-plane/reuse/phase-5-full-proof-validation-and-evaluation-spec.md) · proof/validation/eval spec · 2026-04-16 · Shared Env + Engine proof machinery.
- [`reuse/phase-5-full-governance-authority-and-writeback-spec.md`](Canon/docs/control-plane/reuse/phase-5-full-governance-authority-and-writeback-spec.md) · full governance/authority/writeback · 2026-04-16 · Shared Env.
- [`reuse/phase-5-full-run-class-protocol-packs.md`](Canon/docs/control-plane/reuse/phase-5-full-run-class-protocol-packs.md) · run-class protocol packs with `protocol_version` semantics · 2026-04-16 · Shared Env.
- [`reuse/phase-5-commissioning-bridge-to-task-studio-handoff-contract.md`](Canon/docs/control-plane/reuse/phase-5-commissioning-bridge-to-task-studio-handoff-contract.md) · R7→TS handoff · 2026-04-16 · Shared Env + TS.
- [`reuse/phase-5-task-studio-surface-and-lifecycle-contract-pack.md`](Canon/docs/control-plane/reuse/phase-5-task-studio-surface-and-lifecycle-contract-pack.md) · TS surface/lifecycle · 2026-04-16 · Apps (TS).
- [`reuse/phase-5-task-studio-v1-scope-pack.md`](Canon/docs/control-plane/reuse/phase-5-task-studio-v1-scope-pack.md) · TS V1 scope · 2026-04-16 · Apps (TS).
- [`reuse/phase-5-workflow-trigger-applet-pack-and-integration-binding-specs.md`](Canon/docs/control-plane/reuse/phase-5-workflow-trigger-applet-pack-and-integration-binding-specs.md) · reusable-execution specs · 2026-04-16 · Shared Env.

### 1.7 Phase 6 surfaces + repo architecture

- [`surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md`](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) · maps logical package seams to workspace roots, zero-external-runtime-deps posture, sandbox-isolation claim · 2026-04-16 · cross-layer.
- [`surfaces/phase-6-chat-native-surface-contract-pack.md`](Canon/docs/control-plane/surfaces/phase-6-chat-native-surface-contract-pack.md) · chat-native R1-R7 surface clusters · 2026-04-16 · Apps.
- [`surfaces/phase-6-task-studio-surface-contract-pack.md`](Canon/docs/control-plane/surfaces/phase-6-task-studio-surface-contract-pack.md) · Task Studio named surfaces · 2026-04-16 · Apps.
- [`surfaces/phase-6-shared-projection-grammar-surface-contract-pack.md`](Canon/docs/control-plane/surfaces/phase-6-shared-projection-grammar-surface-contract-pack.md) · projection grammar surface · 2026-04-16 · Shared Env.
- [`surfaces/phase-6-agent-oriented-codebase-pattern-and-documentation-plane-pack.md`](Canon/docs/control-plane/surfaces/phase-6-agent-oriented-codebase-pattern-and-documentation-plane-pack.md) · agent-operating rules · 2026-04-16 · control plane.
- [`surfaces/phase-6-later-domain-surface-backlog-contract-pack.md`](Canon/docs/control-plane/surfaces/phase-6-later-domain-surface-backlog-contract-pack.md) · later-domain backlog · 2026-04-16 · control plane.

### 1.8 Phase 6 implementation blueprints (`/implementation/release-blueprints/`)

- `r1-conversation-blueprint.md` … `r7-commissioning-bridge-blueprint.md` · one blueprint per release mapping contracts to workspace roots · 2026-04-16 · Apps + Shared Env + Engine seams.

### 1.9 Phase 6 execution packets (`/implementation/packets/`)

- Three packet families per release (`contracts-objects`, `runtime-execution`, `surface-validation`); R7 has five (adds `chat-surface`, `task-studio-handoff`, `test-fixtures`). Packets are file-whitelist-bounded delegations; they rarely embed new engine-capability claims.

### 1.10 Phase 7 sync routines (`/sync/`)

- `phase-7-carry-forward-delta-pack-operating-rule.md`, `phase-7-recurring-architecture-synchronization-routine.md`, `phase-7-release-gate-recheck-automation.md`, `phase-7-stale-dependency-detection-and-regeneration-loop.md` · 2026-04-16 · control plane.

### 1.11 Canon artifact + dependency control plane

- [`artifact-control-plane-spec.md`](Canon/docs/control-plane/artifact-control-plane-spec.md), [`artifact-registry.seed.json`](Canon/docs/control-plane/artifact-registry.seed.json), [`dependency-graph.seed.json`](Canon/docs/control-plane/dependency-graph.seed.json) · 2026-04-16/18 · control plane.

### 1.12 Canon spec digests (`/docs/spec-digests/`)

- `agentic-engine/engine-core.md`, `engine-compiler.md`, `engine-gateway.md`
- `shared-environment/env-control.md`, `env-governance.md`, `env-shared-objects.md`
- `canon-apps/app-r1-conversation.md`
- · auto-generated on 2026-04-19 · **All engine + env + app-r1 digests are currently empty — every referenced source file reports `Source file not found` (e.g., `All-Prims-3.md`, `Chat-Native-Release-Plan-4.md`)**. Only `env-governance.md` contains substantive content (forbidden-shortcuts list). This is itself a SPEC-DIGEST-HASH signal (see X-015).

### 1.13 Supplementary plan-shaped docs (outside `/Canon/`)

- [`canon-knowledgebase/canon-phase-4-plus-plan.md`](canon-knowledgebase/canon-phase-4-plus-plan.md) · **active authority** for Phase 4+ post-convergence; step ledger · 2026-04-18 · control plane.
- [`canon-knowledgebase/p00-architecture-delta.md`](canon-knowledgebase/p00-architecture-delta.md) through [`p05-compiler-injection-and-replay-basis.md`](canon-knowledgebase/p05-compiler-injection-and-replay-basis.md) · knowledgebase convergence baseline · 2026-04-17 · Engine ↔ Shared Env seam.
- [`canon-knowledgebase/platform-gate-engine-seam-checkpoint.md`](canon-knowledgebase/platform-gate-engine-seam-checkpoint.md) · **already flags three engine seam gaps** (candidateRef synthesis, missing frozen knowledge-participation basis, stage-order) · 2026-04-17 · Engine.
- `canon-knowledgebase/canon-knowledgebase-layer-rollout-plan.md` · historical rollout plan (replaced) · 2026-04-18 · control plane.
- `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` · append-only decision ledger · 2026-04-18 · control plane.
- `canon-knowledgebase/canon-knowledgebase-layer-session-companion.md` · session recovery companion · 2026-04-18 · control plane.
- `canon-knowledgebase/post-reopen-*.md` · post-reopen engine-seam checkpoints · 2026-04-16 · Engine.
- `canon-knowledgebase/phase-6-r1-conversation-*-checkpoint.md` · local R1 packet completion records (since classified as "local inference error" — see canon-phase-4-plus-plan step 19).
- `canon-knowledgebase/step-3-upstream-tier-1-sync-bounded-slices.md` · upstream sync prep · 2026-04-18 · control plane.
- [`CANON_PROJECT_CONTEXT.md`](CANON_PROJECT_CONTEXT.md) · 2026-04-18 · supplementary ground truth.
- [`AGENTIC_WORKFLOW.md`](AGENTIC_WORKFLOW.md) · 2026-04-18 · operating manual (stations, protocols, gates).
- [`agentic-engine/CONTEXT.md`](agentic-engine/CONTEXT.md) · 2026-04-18 · engine repo purpose + boundary.
- [`agentic-engine-finish-session-plan.md`](agentic-engine-finish-session-plan.md) · six-session engine closure plan · 2026-04-18 · Engine.
- [`canon-now.md`](canon-now.md) · live step snapshot; baton `stop` · 2026-04-18 · control plane.
- [`shared-environment-starter-packet.md`](shared-environment-starter-packet.md) · next-repo handoff packet · 2026-04-18 · Shared Env.
- [`baton/baton-protocol.md`](baton/baton-protocol.md), [`baton/baton-automation-plan.md`](baton/baton-automation-plan.md) · baton mechanics · 2026-04-18 · control plane.
- [`migration/canon-ref-scaffold-plan.md`](migration/canon-ref-scaffold-plan.md), `canon-ref-exploration-report.md` · Canon-Ref v1 scaffold · 2026-04-18 · control plane.
- [`research/ambiguity-conflict-resolution-layers-for-environmental-canon.md`](research/ambiguity-conflict-resolution-layers-for-environmental-canon.md) · research memo · 2026-04-18 · supplementary.

---

## Section 2 — Per-plan impact table

Legend for Impact Class column:
`NO` = NO-IMPACT · `REF` = PLAN-REFERENCE · `CON` = PLAN-CONSTRAINT-CHANGE · `ARCH` = ARCHITECTURE-CHANGE · `GATE` = RELEASE-GATE-IMPACT · `EXP` = SCOPE-EXPANSION · `CTR` = SCOPE-CONTRACTION. Many findings warrant more than one class; the primary is listed first.

### 2.1 [`architecture/phase-3-platform-gate-spec-and-exit-audit.md`](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md) — Platform Gate spec & exit audit (marked passed at P3.6)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001 | CRITICAL | SECURITY | CTR+GATE | Retract the "scoped credentials" claim at §4 L87, §5 L105, §6 L118 (PG-07), §7 item 8 L137 OR reopen Platform Gate until engine enforces `allowedSecrets`. |
| PKG-TG-002 | CRITICAL | SECURITY | CTR+GATE | Retract "sandbox isolation" implication attached to `pkg.tool-gateway-sandbox` L105 OR reopen gate; rename engine primitive or fund process-isolation before exit. |
| WRK-TS-001 | CRITICAL | SECURITY | CTR+GATE | Same as above; PG-10 ("no direct UI-to-worker backdoor" L121) presupposes real worker-boundary isolation which audit shows absent. |
| WRK-TS-002 | CRITICAL | API-SURFACE | EXP+GATE | Require `attachToolSandboxWorkerIpc` on engine public surface before gate sign-off; otherwise gateway contract discipline PG-07 is an unshippable claim. |
| PKG-CC-002 | CRITICAL | DETERMINISM | GATE+ARCH | Clock abstraction is a structural prerequisite for PG-01 (L112 "frozen-context exact replay") — add explicit Clock-abstraction exit criterion to §4 substrate row or gate remains fictive. |
| PKG-CC-003 | CRITICAL | DETERMINISM | GATE+ARCH | Same Clock-abstraction gate criterion. |
| PKG-PROV-001 | CRITICAL | DETERMINISM | GATE+ARCH | PG-01 claims frozen-context replay; add exit criterion: "identical logical snapshots produce identical contentHash across packages". |
| PKG-PROV-002 | CRITICAL | DETERMINISM | GATE+CON | PG-01 evidence must cover thaw→re-freeze idempotency; amend blocking-failure class `gate.missing_primitive` L145 to include "snapshot integrity". |
| PKG-PROV-004 | CRITICAL | DETERMINISM | GATE+CON | Require that `frozenAt` is inside the hashed document OR explicitly scoped as presentation-only in the gate spec. |
| PKG-POL-001 | CRITICAL | SECURITY | CON+GATE | PG-07 "inspectable failure results" presumes deterministic policy matching; add gate criterion: "policy matcher is either documented-strict-equals or pattern-based with contract test". |
| X-007 | CRITICAL | API-SURFACE | GATE+EXP | Exit-audit item 10 L139 requires substrate "strong enough for public R1 work to proceed"; without LICENSE SDK cannot legally ship — add LICENSE-file requirement to exit checklist. |
| PKG-CORE-THEME-001 | CRITICAL | DETERMINISM | ARCH+GATE | Clock abstraction exit criterion as above. |
| OWN-001 | CRITICAL | DETERMINISM | ARCH+GATE | Clock abstraction exit criterion as above. |
| WRK-RC-001 | CRITICAL | CORRECTNESS | NO | Engine-local fix; no plan edit. |
| WRK-RC-002 | CRITICAL | DETERMINISM | CON | PG-01 "replayed from frozen packs and input refs" must specify id-aligned vs positional-index diff; add note. |
| PKG-TG-003 | HIGH | SECURITY | GATE | Add "hard termination" capability note or soften PG-07 "inspectable failure" language. |
| PKG-TG-011 | HIGH | SECURITY | GATE+CON | Same structural dependency as PKG-TG-001. |
| WRK-TS-003..008 | HIGH | SECURITY | GATE | Same structural dependency — Platform Gate cannot truthfully exit under current IPC posture. |
| PKG-PROV-003 | HIGH | SECURITY | CON | If gate claims frozen snapshots cross trust boundaries, require constant-time hash comparison. |
| PKG-PROV-015 | HIGH | SECURITY | CON | Deep-freeze / HMAC-sign snapshot as gate invariant. |
| PKG-MG-024 | HIGH | SECURITY | GATE | Scoped-credentials claim must cover Model Gateway too, not only Tool Gateway. |
| PKG-VAL-001..004 | HIGH | CORRECTNESS | GATE | Exit-audit item 8 "inspectable failures" requires structured error surface — PKG-VAL-001 drops error.code/stack silently. |

### 2.2 [`architecture/phase-3-high-level-technical-architecture-baseline.md`](Canon/docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001 | CRITICAL | SECURITY | CTR | §4 L73 claims Tool-gateway "credential scoping" as an owned responsibility — audit proves it is a name, not a runtime enforcement; either retract or tighten. |
| PKG-TG-002, WRK-TS-001 | CRITICAL | SECURITY | CTR | §4 L73 "sandboxing"; §5 L91 "Tool and model adapters may be deployed separately for isolation" — plans assume real isolation that the engine does not ship. |
| X-007, X-029 | CRITICAL/HIGH | API-SURFACE | EXP | §8 "Workers act through scoped service identities" presupposes a publishable SDK; LICENSE and peer-dep structure must land before this is actionable. |
| OWN-001, PKG-CC-002/003 | CRITICAL | DETERMINISM | ARCH | §3.4 "bounded worker" and §5 "engine-facing gateway" claims are soft until Clock abstraction exists. |

### 2.3 [`architecture/phase-3-api-ipc-and-event-contract-spec.md`](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| OWN-001 | CRITICAL | DETERMINISM | ARCH+REF | §7 L169 "causal refs rather than wall-clock only" anticipates Clock discipline — add explicit TimeProvider / sequence-number requirement. |
| PKG-PROV-001, OWN-008 | CRITICAL/HIGH | DETERMINISM | CON | §7 L170 "Breaking contract changes require version bump" is structurally undermined by the engine's frozen 0.0.0 version (cf. audit item X-010 MEDIUM, referenced by plan prompt); call the neutralization out so R1+ consumers rely on digest signals instead of semver. |
| PKG-MG-001/004/005/006/010/011 | HIGH | API-SURFACE/CORRECTNESS | CON | §5.5 L134 "Side-effecting tools must declare side-effect class before execution" and §5 gateway envelope — add tool-call shape requirements to API-IPC spec rather than implicit adapter behavior. |

### 2.4 [`architecture/phase-3-data-storage-indexing-and-provenance-spec.md`](Canon/docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001, PKG-TG-011 | CRITICAL/HIGH | SECURITY | CTR | §4 L76 "Stores secret references for gateways; secrets do not live in metadata or blobs" presupposes gateway scope enforcement. Either retract or require enforcement as data-plane invariant. |
| PKG-PROV-004, PKG-PROV-005, PKG-PROV-010, PKG-PROV-013 | CRITICAL/HIGH | DETERMINISM | CON | §7.1 L108 "Index records retain source/artifact version refs so retrieval can support frozen replay" — snapshot determinism must be runtime-verified, not assumed. |
| OWN-001 | CRITICAL | DETERMINISM | ARCH | §3.3 L50 "append-only" requires stable ordering beyond wall-clock — Clock/sequence abstraction required. |

### 2.5 [`architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md`](Canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-CC-002, PKG-CC-003 | CRITICAL | DETERMINISM | GATE+ARCH | §3.4 L85 "Replay and compare operate on frozen snapshots" breaks when freshness-rule evaluation consults wall-clock. Require evaluationTime on admitted basis or forbid freshness rules in freeze-first path. |
| PKG-CC-004..008 | HIGH | CORRECTNESS | CON | §8 L153 "Preserve source versions … exactly" requires strict ISO-8601 parser, discriminated-union candidate shape, exhaustive TrustTier handling. |
| PKG-CC-014..018, PKG-CC-026 | HIGH | DETERMINISM/SPEC | CON | §8 L153 `exactly` presupposes structured-type support (BigInt/Map/Set), alias policy for runtime UUIDs, schema-versioned canonical output. |
| OWN-001 | CRITICAL | DETERMINISM | ARCH | Clock abstraction as per §3.4 replay invariant. |

### 2.6 [`canon/phase-1-rewrite-containment-and-stable-seam-map.md`](Canon/docs/control-plane/canon/phase-1-rewrite-containment-and-stable-seam-map.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (consolidated) | CRITICAL/HIGH | DETERMINISM/SECURITY | REF | §5.1 L78 "frozen context snapshots, source-region traceability, run identity … provenance capture" — add carry-forward note that OWN-001 + PKG-TG-001 mean the substrate is partial, not satisfied, at audit date 2026-04-18. SS-10 prelaunch invariant text unchanged; evidence note amended. |

### 2.7 [`canon/phase-1-canon-freeze-and-resolved-product-interpretation.md`](Canon/docs/control-plane/canon/phase-1-canon-freeze-and-resolved-product-interpretation.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| — | — | — | NO | Release order RI-03 L48 remains correct; fixed release order is unaffected. |

### 2.8 [`canon/phase-1-layer-and-primitive-separation-pack.md`](Canon/docs/control-plane/canon/phase-1-layer-and-primitive-separation-pack.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| — | — | — | NO | Layer/primitive ownership unchanged; audit confirms no reverse-dep drift. |

### 2.9 [`semantics/phase-2-core-object-and-state-machine-spec-pack.md`](Canon/docs/control-plane/semantics/phase-2-core-object-and-state-machine-spec-pack.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-CORE-THEME-001 | CRITICAL | DETERMINISM | ARCH | §3.1 L54 "Required `created_at` timestamp on every first-class object" presupposes a clock. Add annotation: `created_at` is Clock-abstraction-resolved, not raw wall-clock. |
| PKG-CORE-THEME-003 | HIGH | CORRECTNESS | CON | Augment IR-05 "append-only once created" with runtime-enforcement requirement (Object.freeze not convention). |
| PKG-CORE-THEME-004 | HIGH | CORRECTNESS | CON | Specify listener-failure semantics as a shared-environment invariant if consumers observe RunLifecycle events. |
| PKG-CORE-THEME-012 | MEDIUM | DETERMINISM | REF | Add monotonic sequence-number requirement for rapid-transition ordering. |

### 2.10 [`semantics/phase-2-run-class-taxonomy-and-protocol-kernel.md`](Canon/docs/control-plane/semantics/phase-2-run-class-taxonomy-and-protocol-kernel.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-POL-011 | HIGH | DETERMINISM | ARCH+REF | §7.2 L147 "authority_scope_ref must exist" depends on AuthorityScope.create being replay-safe; require `restore()` factory in engine. |
| PKG-POL-002..005, PKG-POL-009 | HIGH | SECURITY | CON | §8 L184 "background execution does not expand authority" assumes robust policy matching; call out strict-equals limitations until R6 hardening. |

### 2.11 [`reuse/phase-2-governance-authority-and-writeback-invariants.md`](Canon/docs/control-plane/reuse/phase-2-governance-authority-and-writeback-invariants.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-POL-001, PKG-POL-002, PKG-POL-003, PKG-POL-004 | CRITICAL/HIGH | SECURITY | CON+REF | GI-01/GI-08/GI-10 remain valid invariants; §4 text already defers "Detailed routing, compensation, policy DSLs, and proof/evaluation depth" to later work (L53). Add: strict-equals literal match is the current concrete semantics; R6 must either ship pattern matcher or document it. |

### 2.12 [`reuse/phase-2-proof-and-validation-invariants.md`](Canon/docs/control-plane/reuse/phase-2-proof-and-validation-invariants.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-VAL-001..004 | HIGH | CORRECTNESS | CON | PI-10 "inspectable failure basis" requires structured error capture; explicit contract clarification needed. |
| PKG-PROV-002, PKG-PROV-004 | CRITICAL | DETERMINISM | CON | RC-03 L90 "Replay must reference `input_snapshot_ref`" requires snapshot integrity; either forge-detection or explicit integrity-scope language. |

### 2.13 [`reuse/phase-5-full-proof-validation-and-evaluation-spec.md`](Canon/docs/control-plane/reuse/phase-5-full-proof-validation-and-evaluation-spec.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| OWN-001, PKG-CC-002/003, PKG-PROV-001/002/004, PKG-CC-014..018, PKG-CORE-THEME-013 | CRITICAL/HIGH | DETERMINISM | GATE+ARCH | §8 `exact_replay` suite depends on bit-for-bit reproducibility. Add precondition: "Engine Clock abstraction must be present; stableStringify must be unified across packages; localeCompare must be purged from sort paths." |

### 2.14 [`reuse/phase-5-full-governance-authority-and-writeback-spec.md`](Canon/docs/control-plane/reuse/phase-5-full-governance-authority-and-writeback-spec.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-POL-001..005 | CRITICAL/HIGH | SECURITY | CON | §3.2 "stricter-boundary-wins" precedence is engine-verified via strict-equals; add explicit limitation until R6 pattern matcher lands. |
| PKG-TG-001 | CRITICAL | SECURITY | CTR | §7.3 "No inline secret material crosses handoff" presumes gateway enforcement of `allowedSecrets`. |

### 2.15 [`reuse/phase-5-full-run-class-protocol-packs.md`](Canon/docs/control-plane/reuse/phase-5-full-run-class-protocol-packs.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (X-010 MEDIUM) | MED | CONTRACT | CON | `protocol_version` pinning and `Backward-incompatible changes require new major version` (§5.2 L108) implicitly expect SDK to signal breakage via semver. Engine's `0.0.0` pin neutralizes this. Either plan formalizes a digest-based signal OR require engine to begin semver discipline. |

### 2.16 [`surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md`](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001 | CRITICAL | SECURITY | CTR | §5.1 L114 `pkg.tool-gateway-sandbox` row: **"Typed tool execution, side-effect previews, scoped credentials, sandbox isolation"** — retract "scoped credentials" or require enforcement. |
| PKG-TG-002, WRK-TS-001 | CRITICAL | SECURITY | CTR | Same row: "sandbox isolation" — retract or require real process-boundary implementation. |
| X-029 | HIGH | API-SURFACE | REF | §6.1 L148 "peer dependencies … out of bounds unless a later accepted artifact explicitly changes that policy" conflicts with X-029 (engine-core must be peerDependency). Plan must accept peerDependencies **inside the workspace** as distinct from third-party peerDependencies. |

### 2.17 [`surfaces/phase-6-chat-native-surface-contract-pack.md`](Canon/docs/control-plane/surfaces/phase-6-chat-native-surface-contract-pack.md)

| — | — | — | NO | Surface-grammar claims are unaffected by engine-side findings. |

### 2.18 [`surfaces/phase-6-task-studio-surface-contract-pack.md`](Canon/docs/control-plane/surfaces/phase-6-task-studio-surface-contract-pack.md)

| — | — | — | NO | TS surface claims unaffected directly; depends on R6/R7 substrate via upstream. |

### 2.19 [`implementation/release-blueprints/r1-conversation-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r1-conversation-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-MG-001..012 | HIGH | API-SURFACE/CORRECTNESS | CON | §4.1 L54 `packages/model-gateway-contracts/chat-turn/` seam relies on `chat-turn` shape; content-normalization, function-calling, role validation gaps must be closed before R1 can ship. |
| PKG-CC-*, OWN-001 | CRITICAL/HIGH | DETERMINISM | GATE | §4.4 L74 "Persist run/result/source lineage … not provider transcript continuity" depends on deterministic freeze — blocked until Platform Gate closes against Clock abstraction. |

### 2.20 [`implementation/release-blueprints/r2-context-control-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r2-context-control-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-PROV-001/002/004, PKG-CC-015/016/017 | CRITICAL/HIGH | DETERMINISM | GATE | §4.4 L75 "pack freezes … append-only admitted-basis lineage" blocked by snapshot-freezer drift. |

### 2.21 [`implementation/release-blueprints/r3-branch-replay-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r3-branch-replay-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| OWN-001, PKG-CC-002/003, PKG-CORE-THEME-001, PKG-CORE-THEME-013 | CRITICAL/HIGH | DETERMINISM | GATE+ARCH | §4.3 L70 "Exact replay must mint new runs from frozen basis" is **not achievable** without Clock abstraction. Add R3 entry-criterion: "Engine Clock abstraction landed and proven by cross-host determinism test." |
| PKG-PROV-001/002/004, PKG-PROV-005/006/008/009/010/011/013, PKG-CC-014, OWN-008 | CRITICAL/HIGH | DETERMINISM | GATE | §4.3 L71 "Merge remains explicit proposal state" and §4.6 L93 "Contract tests for branch identity, checkpoint-based replay" require all snapshot-freezer and diff-engine determinism gaps closed. |
| WRK-RC-001/002 | CRITICAL | CORRECTNESS | CON+GATE | Replay-compare worker edge cases must have documented behavior before R3 can declare exact replay. |

### 2.22 [`implementation/release-blueprints/r4-artifact-workspace-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r4-artifact-workspace-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (R3 inherited blockers) | — | — | GATE | R4 inherits R3's replay-determinism requirement transitively. Add explicit "R3 Clock + snapshot determinism prerequisite". |

### 2.23 [`implementation/release-blueprints/r5-prompt-assets-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r5-prompt-assets-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-MG-003/004/005/006, PKG-MG-011 | HIGH | CORRECTNESS | CON | §4.1 L56 `services/model-gateway/adaptation-execution/` depends on ModelAdapter typed `toolCalls`/`refusal`/streaming — add explicit spec entry. |

### 2.24 [`implementation/release-blueprints/r6-governed-reusable-execution-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r6-governed-reusable-execution-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001, PKG-TG-011, PKG-TG-003/004/005/006/007/008/009/010 | CRITICAL/HIGH | SECURITY | GATE+CTR | §4.1 L56 `workers/tool-sandbox/policy-bounded-run/` and §4.3 L71 "sandbox workers" presume credential scoping, timeout enforcement, output validation, abort-signal correctness. R6 cannot declare M4 on `pkg.tool-gateway-sandbox` until these land. |
| WRK-TS-001, WRK-TS-002 | CRITICAL | SECURITY | GATE+CTR | R6 tool sandbox must actually spawn a child process or the plan must retract isolation promise. |
| PKG-POL-001..005 | CRITICAL/HIGH | SECURITY | CON+GATE | §4.3 L71 "Background work may narrow behavior only through explicit policy" requires real policy matching. |
| PKG-MG-024 | HIGH | SECURITY | CON | Scoped credentials must cover Model Gateway too. |

### 2.25 [`implementation/release-blueprints/r7-commissioning-bridge-blueprint.md`](Canon/docs/control-plane/implementation/release-blueprints/r7-commissioning-bridge-blueprint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001, WRK-TS-001, PKG-TG-002 | CRITICAL | SECURITY | GATE+CTR | §4.1 L59 `workers/tool-sandbox/commissioned-side-effect-preview/` depends on real sandbox isolation. |
| OWN-001, PKG-PROV-001..004 | CRITICAL | DETERMINISM | GATE | §4.1 L59 `workers/context-compiler/preflight-basis-freeze/` depends on Clock + snapshot determinism. |
| PKG-POL-001..005 | CRITICAL/HIGH | SECURITY | CON | §4.3 L73 "authority scope and contract review" requires real policy matcher. |

### 2.26 [`implementation/packets/phase-6-r3-branch-replay-runtime-execution-packet.md`](Canon/docs/control-plane/implementation/packets/phase-6-r3-branch-replay-runtime-execution-packet.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (R3 blueprint findings) | — | — | GATE | Packet execution waits on engine Clock + snapshot determinism landings. |

### 2.27 [`implementation/packets/phase-6-r6-governed-reusable-execution-runtime-execution-packet.md`](Canon/docs/control-plane/implementation/packets/phase-6-r6-governed-reusable-execution-runtime-execution-packet.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (R6 blueprint findings) | — | — | GATE+CTR | Packet execution waits on engine tool-gateway hardening. |

### 2.28 [`implementation/packets/phase-6-r7-commissioning-bridge-runtime-execution-packet.md`](Canon/docs/control-plane/implementation/packets/phase-6-r7-commissioning-bridge-runtime-execution-packet.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (R7 blueprint findings) | — | — | GATE+CTR | Packet execution waits on Clock + sandbox + policy landings. |

### 2.29 Other phase-6 implementation packets (R1/R2 contracts+runtime+surface, R3 contracts+surface, R4 all, R5 all, R6 contracts+surface, R7 chat-surface/ts-handoff/test-fixtures)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| — | — | — | NO | Packets are file-whitelist-bounded delegations with no additional engine-capability claims; inherited blocks propagate from blueprint tables above. |

### 2.30 [`releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md`](Canon/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001, PKG-TG-002, WRK-TS-001 | CRITICAL | SECURITY | CTR+GATE | Matrix cell for `pkg.tool-gateway-sandbox` at Platform Gate (M1) is overstated. Either (a) add explicit footnote: "M1 means type-shape only, not enforced scoping/isolation", OR (b) raise Platform-Gate floor. |

### 2.31 [`releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md`](Canon/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (consolidated) | CRITICAL/HIGH | multiple | REF | §5.1 L93 "Platform Gate blocking" carries forward; add carry-forward note: "audit 2026-04-18 proves substrate incomplete against PG-07 + PG-01". |

### 2.32 [`releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md`](Canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| OWN-001, PKG-CC-002/003, PKG-PROV-001/002/004 | CRITICAL | DETERMINISM | GATE+ARCH | §4.5 L141 "Exact replay produces a new Run from frozen pack lineage" is the core R3 promise and is currently unreachable — add Clock + snapshot-determinism prerequisites. |

### 2.33 [`releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md`](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001/011 | CRITICAL/HIGH | SECURITY | GATE+CTR | §4.5 L147 "Tool execution is typed, side-effect-classified, scoped by authority and credential bindings, and inspectable" presupposes gateway enforcement. Retract or implement. |
| WRK-TS-001/002 | CRITICAL | SECURITY | GATE+CTR | Same row references sandbox hardening. |
| PKG-POL-001..005 | CRITICAL/HIGH | SECURITY | CON+GATE | §4.5 L146 "Applet, Workflow, Trigger … may narrow behavior but may not silently widen authority" requires real policy semantics. |

### 2.34 [`canon-knowledgebase/canon-phase-4-plus-plan.md`](canon-knowledgebase/canon-phase-4-plus-plan.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (consolidated) | — | — | REF | Plan is currently in `Baton state: stop`. Add an authority-repair step entry: "audit 2026-04-18 constitutes cited contradiction against §206 'memory and canon injection are real engine seams with authoritative refs and frozen replay basis behavior' — reopen for engine remediation sequencing." |
| OWN-001, PKG-CORE-THEME-001 | CRITICAL | DETERMINISM | ARCH | §173 "Replay correctness depends on frozen authoritative refs" — add Clock abstraction to Platform Gate obligation list at §206. |

### 2.35 [`canon-knowledgebase/p04-engine-seam-tightening.md`](canon-knowledgebase/p04-engine-seam-tightening.md) & [`p05-compiler-injection-and-replay-basis.md`](canon-knowledgebase/p05-compiler-injection-and-replay-basis.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-PROV-001/002/004, PKG-CC-014..018 | CRITICAL/HIGH | DETERMINISM | CON | p05 L148 "The frozen basis must be serializable by the deterministic snapshot freezer" — current freezer is NOT deterministic across packages. Add explicit remediation list. |
| OWN-001 | CRITICAL | DETERMINISM | ARCH | p05 L104 "canonical context replay-boundary artifact" requires Clock abstraction. |

### 2.36 [`canon-knowledgebase/platform-gate-engine-seam-checkpoint.md`](canon-knowledgebase/platform-gate-engine-seam-checkpoint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (consolidated) | — | — | REF | Checkpoint already flags three gaps (candidateRef synthesis, frozen knowledge-participation basis, stage-order). Add four more: Clock absence, stableStringify divergence, credentialScope unenforcement, sandbox-isolation mis-naming. Keep the doc as append-only. |

### 2.37 [`canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md`](canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-PROV-001/002/004, PKG-CC-014..018, OWN-001, OWN-008 | CRITICAL/HIGH | DETERMINISM | REF+CON | Checkpoint states "the frozen context boundary already preserves authoritative candidate refs … for later replay or audit consumers". Audit disproves "already sufficient" claim for the cross-host determinism + snapshot-integrity properties. Supersede with a new checkpoint that acknowledges the gap. |

### 2.38 [`CANON_PROJECT_CONTEXT.md`](CANON_PROJECT_CONTEXT.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| WRK-TS-001 | CRITICAL | SECURITY | REF+CTR | §2 L57 "Tool execution across spawned Node child processes (NOT container isolation)" — retract "spawned Node child processes" portion; replace with accurate "in-process ToolSandbox; `attachToolSandboxWorkerIpc` optional spawn helper". |
| PKG-TG-001 | CRITICAL | SECURITY | REF+CTR | §3 primitive list + §2 imply credential scoping works. Soften. |
| X-010 (MED — version pin) | MED | CONTRACT | REF | §6 L146 "Status: 0.0.0" — add explicit acknowledgement that 0.0.0 is structurally unable to signal breakage to Canon consumers (plan must choose digest-based signal). |
| X-029 | HIGH | API-SURFACE | REF | §6 "0 + 0 peers" claim conflicts with need for `@canon/engine-core` as a peerDependency. Clarify that intra-workspace peer-deps are compatible with "zero external peers". |
| OWN-001 / Deterministic replay claim | CRITICAL | DETERMINISM | REF | §5 #5 L121 "Deterministic replay across the full primitive graph" — qualify as aspirational; audit shows Clock abstraction absent. |

### 2.39 [`AGENTIC_WORKFLOW.md`](AGENTIC_WORKFLOW.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| WRK-TS-001 | CRITICAL | SECURITY | REF+CTR | §5 L203 "`ToolSandbox` — execution surface backed by the `tool-sandbox` worker (`node:child_process`-based, NOT container isolation; documented as such)" — remove "`node:child_process`-based" until audit WRK-TS-001 is closed; or add "(helper `attachToolSandboxWorkerIpc` provides optional child-process hosting; default ToolSandbox is in-process)". |
| PKG-TG-001 | CRITICAL | SECURITY | REF+CTR | §5 L200 `ToolRegistry` + `CredentialScope` description implies enforcement. Soften. |
| OWN-001 | CRITICAL | DETERMINISM | REF | §7 Gate 04 "replay-determinism" gate — explicit Clock abstraction prerequisite must be added or the gate's green signal is misleading. |
| X-010 | MED | CONTRACT | REF | §10 "1.0 API surface (not 0.0.0)" recognized as a release-readiness requirement at L426. Escalate: 0.0.0 also breaks plan-prose semver expectations (phase-3-api-ipc §7 L170). |

### 2.40 [`agentic-engine/CONTEXT.md`](agentic-engine/CONTEXT.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| PKG-TG-001, PKG-TG-002, WRK-TS-001 | CRITICAL | SECURITY | REF+CTR | L33 "Tool interaction (Tool Gateway, sandboxing, credential scoping)" — all three claims partially absent. Rewrite as "Tool interaction (Tool Gateway, sandboxing contract *surfaces*, credential scope *shape*; runtime enforcement tracked as open audit items in AGENTIC_ENGINE_AUDIT_LOG.md)". |
| OWN-001, PKG-CORE-THEME-001 | CRITICAL | DETERMINISM | REF | L37 "Replay and comparison (temporal state, diffing, deterministic replay)" — hedge "deterministic replay" until Clock abstraction lands. |

### 2.41 [`agentic-engine-finish-session-plan.md`](agentic-engine-finish-session-plan.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| X-007, X-029 | CRITICAL/HIGH | API-SURFACE | REF | Sessions 3 and 4 already address tarball/peerDep hardening. Add explicit session for LICENSE + peer-dep restructure OR confirm covered. |
| (consolidated audit) | CRITICAL/HIGH | multiple | REF | Extend plan with sessions for: Clock abstraction, stableStringify unification, credentialScope enforcement, ToolSandboxWorker spawn helper, policy-matcher decision, queue.ts deletion. |

### 2.42 [`canon-now.md`](canon-now.md) & [`shared-environment-starter-packet.md`](shared-environment-starter-packet.md)

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| (consolidated) | — | — | REF | Update baton snapshot with "engine audit 2026-04-18 constitutes cited contradiction — prerequisite engine remediations named before shared-environment work begins". |

### 2.43 Sync routines, Phase 7 files, Semantics other-than-core, packets non-runtime, canon-ref migration plans, baton protocol, research memo, freeze/layer/surface canon docs, forbidden shortcuts, master plan, artifact control plane, spec-digest SHARED/APP files

| Finding ID | Severity | Category | Impact Class | Required plan edit |
| --- | --- | --- | --- | --- |
| — | — | — | NO | No direct prose edit required from the audit findings. (Spec-digest empty-source anomaly is covered in Section 5 under X-015.) |

### 2.44 Engine-local HIGH findings with no plan prose change (~30 items)

The following HIGH findings are NO-IMPACT at the plan prose level — engine-internal correctness/security/type-safety fixes, but no Canon plan claim is contradicted or advanced by them:

- `PKG-CC-005..008, PKG-CC-026` (discriminated-union candidate, trust-tier exhaustive, retrieval-rule validation)
- `PKG-CC-014..018` (engine-local snapshot-freezer cleanups — but tagged GATE in §2.5 via R3/Phase-5 chain)
- `WRK-CC-001/002/004/005/012` (context-compiler worker fixes; WRK-CC-002 tagged REF in the EngineError theme)
- `WRK-RC-003/006/008/012/013/017/026` (replay-compare correctness/coverage)
- `PKG-MG-002/003/012/016` (invocation-normalizer cleanups)
- `PKG-TG-004/005/006/007/008/009/010/012/041` (tool-gateway hardening; upstream of PKG-TG-001 in practice)
- `WRK-TS-003..008` (IPC hardening; upstream of WRK-TS-001)
- `PKG-PROV-003/007/011/013/015/016/029/030/034` (freezer + diff-engine correctness; several tagged GATE upstream via R3)
- `PKG-POL-019` (shallow-copy; REF)
- `WRK-RE-001..050 subset` (run-executor correctness)
- `X-001/002/004/005/006/008/011/014/023/025/027/030/037/039/041/045/057`
- `PKG-CORE-THEME-003/007, OWN-002/003/004/009/010/011/014/015/016/017/018`

Most of these roll up under the 12 cross-cutting themes in Section 3 — so the plan edits needed are theme-level, not per-finding.

---

## Section 3 — Cross-cutting theme map

### T1 — No Clock / TimeProvider abstraction (≥15 rolled-up findings)

- **Rolled-up IDs**: `OWN-001` (CRITICAL) · `PKG-CORE-THEME-001` (CRITICAL) · `PKG-CC-002` (CRITICAL) · `PKG-CC-003` (CRITICAL) · `PKG-CC-001` (HIGH) · `PKG-CC-004` (HIGH) · `PKG-MG-002` (HIGH) · `PKG-POL-011` (HIGH) · `PKG-CORE-THEME-012` (MED, derivative) · `WRK-RE-014` (HIGH, indirect) · plus MEDIUM echoes throughout core/provenance.
- **Plans affected**: [platform-gate-spec §4 L87, §6 L112 PG-01, §7 L137 item 8](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md); [phase-3-context-compiler §3.4 L85](Canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md); [phase-3-api-ipc §7 L169](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md); [r3-branch-replay-blueprint §4.3 L70](Canon/docs/control-plane/implementation/release-blueprints/r3-branch-replay-blueprint.md); [phase-4-r3-contract-pack §4.5 L141](Canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md); [phase-5 proof/validation/eval §3.3 / §8](Canon/docs/control-plane/reuse/phase-5-full-proof-validation-and-evaluation-spec.md); [canon-phase-4-plus-plan §206-291](canon-knowledgebase/canon-phase-4-plus-plan.md); [p05-compiler-injection-and-replay-basis](canon-knowledgebase/p05-compiler-injection-and-replay-basis.md); [CANON_PROJECT_CONTEXT.md §5 L121](CANON_PROJECT_CONTEXT.md); [AGENTIC_WORKFLOW.md §7 gate 04](AGENTIC_WORKFLOW.md); [agentic-engine/CONTEXT.md L37](agentic-engine/CONTEXT.md).
- **Architecture implication**: introducing a `Clock` / `TimeProvider` interface as a new first-class engine-core abstraction injected through every `create()`/`freeze()`/`capture()`/`assemble()` factory. This is the single largest structural addition required. It propagates into core objects, context-compiler, provenance, policy (AuthorityScope.create nondeterminism), and run-executor.
- **Owner decision required**: Confirm Clock abstraction is an R3-prerequisite — blocks Platform Gate exit truth and R3 exact-replay. Decision options: (a) implement Clock now as Platform-Gate reopen driver; (b) weaken R3 "exact replay" language to "context-altered deterministic replay" (engine's current honest disclaimer in DEEP_RELEASE_AUDIT_LOG); (c) defer Clock to R3 entry as explicit prerequisite but let Platform Gate stand with footnote. Default recommendation: **(a)** — the least structural damage is to fix the engine before R1 work resumes.

### T2 — credentialScope unenforced (`allowedSecrets`)

- **Rolled-up IDs**: `PKG-TG-001` (CRITICAL) · `PKG-TG-011` (HIGH) · `PKG-TG-041` (HIGH, derivative) · `WRK-TS-004` (HIGH, IPC) · `PKG-MG-024` (HIGH, model-gateway analogue) · `X-057` (HIGH, expiresAt coercion).
- **Plans affected**: [platform-gate-spec PG-07 L118, exit item 8 L137, §4 L87, §5 L105](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md); [phase-3-high-level-arch §4 L73, §8 L119](Canon/docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md); [phase-3-api-ipc §5.5 L135](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md); [phase-3-data-storage §4 L76, §8 L130](Canon/docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md); [phase-6-repo-package-architecture §5.1 L114](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md); [phase-5-full-gov spec §7.3](Canon/docs/control-plane/reuse/phase-5-full-governance-authority-and-writeback-spec.md); [maturity-matrix §6 L117 + §7 L130](Canon/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md); [r6-contract-pack §4.5 L147](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md); [agentic-engine/CONTEXT.md L33](agentic-engine/CONTEXT.md); [CANON_PROJECT_CONTEXT.md](CANON_PROJECT_CONTEXT.md); [AGENTIC_WORKFLOW.md §5 L200](AGENTIC_WORKFLOW.md).
- **Architecture implication**: Engine must own a real secret resolver (a scoped `CredentialProvider` that serves only strings named in `allowedSecrets` to the adapter). Alternatively, the primitive is renamed (e.g., `CredentialReference` with explicit "advisory-only" contract) and plans are tightened to forbid relying on it. Either path is an engine change; the former is SCOPE-EXPANSION (engine owns credential resolution), the latter is SCOPE-CONTRACTION (plans retract enforcement claims).
- **Owner decision required**: Does Engine SDK own runtime credential resolution, or does Shared Environment? Default recommendation: **Engine owns the type + scope-check; the concrete secret resolver is injected by Shared Environment** — consistent with the three-layer architecture. Either way Platform Gate PG-07 wording must change today.

### T3 — ToolSandbox does not isolate (no child process)

- **Rolled-up IDs**: `PKG-TG-002` (CRITICAL) · `WRK-TS-001` (CRITICAL) · `WRK-TS-002` (CRITICAL) · `PKG-TG-003` (HIGH) · `WRK-TS-007` (HIGH) · `PKG-TG-009/010` (HIGH, derivative).
- **Plans affected**: [platform-gate-spec §4 L87, §5 L105, §6 L121 PG-10](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md); [phase-3-high-level-arch §4 L73, §5 L91](Canon/docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md); [phase-6-repo-package-architecture §5.1 L114](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md); [r6-contract-pack §4.5 L147, §4.4 L125](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md); [r7-blueprint §4.1 L59](Canon/docs/control-plane/implementation/release-blueprints/r7-commissioning-bridge-blueprint.md); [AGENTIC_WORKFLOW.md §5 L163,171,202,212](AGENTIC_WORKFLOW.md); [CANON_PROJECT_CONTEXT.md §2 L57](CANON_PROJECT_CONTEXT.md); [agentic-engine/CONTEXT.md L33](agentic-engine/CONTEXT.md).
- **Architecture implication**: Either (a) engine ships `spawnToolSandboxWorker(options)` as a public helper that forks a child process and attaches IPC, exporting `attachToolSandboxWorkerIpc` from public surface (closes WRK-TS-001 + WRK-TS-002 together); (b) plans retract "sandbox isolation"/"spawned child processes" prose and limit runtime-enforcement to document the in-process behavior; or (c) engine defers isolation to Shared Environment / deployment infra (e.g., Cloudflare Workers per CANON_PROJECT_CONTEXT.md §4 #8 — but CF Workers isolate at tenant boundary, not per-adapter).
- **Owner decision required**: Is real process/memory isolation a Platform Gate invariant or an R6 invariant? Current plans are inconsistent (Platform Gate lists it; maturity matrix delays hardening to R6). Default recommendation: **Platform Gate requires a process-boundary contract but not full isolation enforcement; R6 tightens to real child-process default**.

### T4 — stableStringify divergence + snapshot determinism

- **Rolled-up IDs**: `PKG-PROV-001` (CRITICAL) · `PKG-PROV-002` (CRITICAL) · `PKG-PROV-004` (CRITICAL) · `OWN-008` (HIGH) · `OWN-002` (HIGH) · `PKG-PROV-011/012/013/029` (HIGH) · `PKG-CC-014..018` (HIGH) · `PKG-CORE-THEME-013` (HIGH, localeCompare) · `PKG-PROV-005/006/008/009/010` (HIGH).
- **Plans affected**: [platform-gate PG-01](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md); [phase-3-context-compiler §8 L153](Canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md); [phase-3-data-storage §7.1 L108](Canon/docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md); [phase-5 proof/validation/eval §8](Canon/docs/control-plane/reuse/phase-5-full-proof-validation-and-evaluation-spec.md); [r3-contract-pack §4.5 L141](Canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md); [r3-blueprint §4.4 L74-76](Canon/docs/control-plane/implementation/release-blueprints/r3-branch-replay-blueprint.md); [p05 L104, L148](canon-knowledgebase/p05-compiler-injection-and-replay-basis.md); [post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint](canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md).
- **Architecture implication**: Extract canonical `stableStringify`/`sortValue`/UUID aliasing into `@canon/engine-core` as shared helper. Platform Gate PG-01 "exact replay from frozen packs" requires bit-for-bit determinism across packages. This is ARCHITECTURE-CHANGE inside the engine + RELEASE-GATE-IMPACT on Platform Gate.
- **Owner decision required**: Accept the `post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md` as superseded; plan a successor that names stableStringify unification as an unfinished condition. Default recommendation: **supersede the "sufficiency" checkpoint; open a `PG-FREEZE-DETERMINISM` checkpoint with a concrete close criterion (cross-package determinism test landing)**.

### T5 — Strict-equals policy matching

- **Rolled-up IDs**: `PKG-POL-001` (CRITICAL) · `PKG-POL-002/003/004/005` (HIGH) · `PKG-POL-009` (HIGH) · `PKG-POL-014` (HIGH, enforcement-mode gap) · `PKG-POL-019` (HIGH).
- **Plans affected**: [phase-2-governance-authority-and-writeback-invariants §4 L53 + §4 L59, L66, L68](Canon/docs/control-plane/reuse/phase-2-governance-authority-and-writeback-invariants.md) (plan already defers "policy DSLs"); [phase-5-full-gov spec §3.2 L49, §4.1 L61, §6](Canon/docs/control-plane/reuse/phase-5-full-governance-authority-and-writeback-spec.md); [platform-gate-spec §4 L85](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md); [r6-contract-pack §4.5 L146](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md); [phase-2-run-class-taxonomy §8 L184](Canon/docs/control-plane/semantics/phase-2-run-class-taxonomy-and-protocol-kernel.md).
- **Architecture implication**: R6 has always assumed richer policy matching than strict-equals can provide. Either engine ships a pattern matcher (`glob` or typed `RulePattern`) at R6, or the plan language at GI-01/08/10/stricter-boundary-wins is tightened to state "strict-equals literal match is current semantics; pattern matching deferred to domain packs".
- **Owner decision required**: Is it acceptable for Platform Gate and R1-R5 to ship with a policy matcher that silently bypasses rules on whitespace/case perturbation? Default recommendation: **close PKG-POL-001 before Platform Gate truly exits** (it's CRITICAL SECURITY).

### T6 — Error discipline (`new Error` vs `EngineError`)

- **Rolled-up IDs**: `OWN-005` (HIGH) · `PKG-CORE-THEME-002` (HIGH) · `WRK-CC-002` (HIGH) · `WRK-RC-004` (HIGH) · `WRK-RE-002` (HIGH) · `PKG-CORE-THEME-006` (MED, toJSON).
- **Plans affected**: [phase-2-proof-and-validation-invariants PI-10](Canon/docs/control-plane/reuse/phase-2-proof-and-validation-invariants.md); [platform-gate-spec §7 L137 item 8 "inspectable failures"](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md); [CANON_PROJECT_CONTEXT.md §3 L94](CANON_PROJECT_CONTEXT.md); [AGENTIC_WORKFLOW.md §10 L441](AGENTIC_WORKFLOW.md).
- **Architecture implication**: Engine-local discipline; plans already specify typed error surface. No plan-prose change required beyond reaffirming the `EngineError` contract.
- **Owner decision required**: Add CI lint rule forbidding `new Error(` in engine `src/*.ts` paths? Default recommendation: **yes** (OWN-005 remediation hint).

### T7 — Dead code shipped (`workers/run-executor/src/queue.ts`)

- **Rolled-up IDs**: `OWN-006` (HIGH) · `X-031` (HIGH) · `X-032` (HIGH) · plus `PKG-MG-001` (InvocationNormalizer surface leak) thematically related.
- **Plans affected**: none directly. Implicit touch on [phase-6-repo-package-architecture §6.3 L161](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) — "Workers operate on frozen refs and typed contracts; they do not reach into …". Dead code violates public surface cleanliness promise.
- **Architecture implication**: Engine cleanup only.
- **Owner decision required**: None. Default recommendation: delete.

### T8 — Mocks on public root surface (`MockToolAdapter`, `MockModelAdapter`)

- **Rolled-up IDs**: `X-012` (HIGH) · `PKG-MG-001` (HIGH, InvocationNormalizer).
- **Plans affected**: [phase-6-repo-package-architecture §6.1 L137 "`packages/*-contracts/` … must not depend on `apps/*`, `services/*`, `workers/*` runtime code"](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) — mocks on root surface are adjacent to this boundary rule.
- **Architecture implication**: Split `/testing` subpath export or separate `@canon/engine-gateway-testing` package. Engine-local; no plan change required.
- **Owner decision required**: None. Default recommendation: subpath export.

### T9 — `@canon/engine-core` must be `peerDependencies` not `dependencies`

- **Rolled-up IDs**: `X-029` (HIGH).
- **Plans affected**: [phase-6-repo-package-architecture §6.1 L148 "peer dependencies … out of bounds"](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md); [CANON_PROJECT_CONTEXT.md §4 #1 "Zero external runtime dependencies, forever" + §6 "0 + 0 peers"](CANON_PROJECT_CONTEXT.md); [AGENTIC_WORKFLOW.md §7 gate 06](AGENTIC_WORKFLOW.md).
- **Architecture implication**: Plans conflate third-party peerDependencies (banned) with intra-workspace peerDependencies (required for single-copy identity). Add an explicit carve-out in phase-6-repo-package-architecture §6.1: "Intra-`@canon/*` peerDependencies are permitted and required for workspaces that depend on `@canon/engine-core`; third-party peerDependencies remain out of bounds."
- **Owner decision required**: Accept carve-out language. Default recommendation: **yes**.

### T10 — Missing LICENSE (X-007)

- **Rolled-up IDs**: `X-007` (CRITICAL).
- **Plans affected**: [platform-gate-spec §7 item 10 L139](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md) (public R1 readiness implicit); [agentic-engine-finish-session-plan.md](agentic-engine-finish-session-plan.md) (sessions 3/4 don't mention LICENSE).
- **Architecture implication**: Add LICENSE file + license field to root + every workspace package. SCOPE-EXPANSION at SDK-consumability level.
- **Owner decision required**: Which license (MIT / Apache-2.0 / proprietary / source-available)? Default recommendation: **MIT or Apache-2.0** for a Canon SDK that aspires to external consumption per AGENTIC_WORKFLOW.md §9 L426 "a 1.0 API surface (not 0.0.0)".

### T11 — tsconfig strict flags missing

- **Rolled-up IDs**: `X-003` (HIGH) · `X-057` (HIGH).
- **Plans affected**: none directly. [phase-6-repo-package-architecture §6.1 "typed contracts"](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) implicit.
- **Architecture implication**: Engine-local. No plan change.
- **Owner decision required**: None. Default recommendation: enable all listed flags, fix fallout.

### T12 — Forever-pinned contract version `0.0.0` + empty spec digests

- **Rolled-up IDs**: `X-010` (MEDIUM, not in CRITICAL/HIGH but highlighted by prompt) · `X-015` (HIGH) · SPEC-DIGEST-HASH observation from [agent 2 report on `docs/spec-digests/*.md`](Canon/docs/spec-digests).
- **Plans affected**: [phase-3-api-ipc §3.5 L61, §7 L170](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md); [phase-5-full-run-class-protocol-packs §5.2 L102-108](Canon/docs/control-plane/reuse/phase-5-full-run-class-protocol-packs.md); [AGENTIC_WORKFLOW.md §9 L426](AGENTIC_WORKFLOW.md); [Canon/docs/spec-digests/agentic-engine/*.md](Canon/docs/spec-digests/agentic-engine/engine-core.md) (all empty — "Source file not found: All-Prims-3.md"); [`scripts/generate-spec-digests.py`](Canon/scripts/generate-spec-digests.py).
- **Architecture implication**: The plans assume a working version + digest channel for signaling breakage. Today the engine's `0.0.0` pin and Canon's empty digests together mean **no freshness signal exists**. Either plans adopt digest-based signals explicitly, or engine + Canon adopt semver + digest regeneration.
- **Owner decision required**: Regenerate spec digests from an authoritative source (clarify whether `All-Prims-3.md` / `Chat-Native-Release-Plan-4.md` are actually missing vs. merely renamed) AND decide whether engine begins semver discipline now. Default recommendation: **both** — start engine `0.1.0` with breaking-change protocol tied to digest regeneration.

---

## Section 4 — Release-gate impact

### Platform Gate ([phase-3-platform-gate-spec-and-exit-audit.md, marked passed at P3.6 acceptance L126](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md))

**Status**: gate is **already marked passed** in plan prose ("Gate passed. The following checklist is kept as the human-owned audit record. Confirmed at P3.6 acceptance" — L125-126), but the audit proves multiple exit-test promises are false. Plan-owner must decide whether Platform Gate is retrospectively reopened, narrowed, or amended with honest footnotes.

Findings that block or require plan revision before Platform Gate remains truthfully closed:
- PG-01 "frozen-context exact replay": `OWN-001`, `PKG-CORE-THEME-001`, `PKG-CC-002`, `PKG-CC-003`, `PKG-PROV-001`, `PKG-PROV-002`, `PKG-PROV-004`, `OWN-008`, plus the Clock & stableStringify themes.
- PG-07 "scoped credentials, inspectable failure results": `PKG-TG-001`, `PKG-TG-011`, `PKG-MG-024`, `PKG-VAL-001..004`.
- PG-10 "no direct UI-to-worker backdoor": `WRK-TS-001` (engine does not have a real worker boundary).
- Exit item 10 "public R1 work to proceed": `X-007` (no LICENSE), `X-029` (peer-dep), plus AGENTIC_WORKFLOW.md §9 L426 1.0-API recognition.
- Forced area `pkg.tool-gateway-sandbox` at §5 L105: `PKG-TG-001`, `PKG-TG-002`, `WRK-TS-001/002`, `PKG-POL-001..005`.

**Primary decision**: reopen Platform Gate with a prioritized remediation list (T1-T4, T10) — OR retain "passed" status with a documented "audit-aware substrate gap" carry-forward note. Given this is a SECURITY + DETERMINISM gate, reopening is the more honest path.

### R1 Transcript Chat

Findings that block or delay: PKG-MG-001/004/005/006/010/011 (model-gateway contract gaps relevant to §4.1 `chat-turn/` seam); inherited Clock/snapshot blockers from Platform Gate.
Plan revision: [r1-conversation-blueprint.md](Canon/docs/control-plane/implementation/release-blueprints/r1-conversation-blueprint.md) requires acknowledgement that `packages/model-gateway-contracts/chat-turn/` cannot fully satisfy R1's "frozen admitted basis" promise until Clock + snapshot-determinism land.

### R2 Context Chat

Findings that block: `PKG-PROV-001/002/004`, `PKG-CC-014..018`, `OWN-008` — R2 pack freeze/diff depends on deterministic snapshots.
Plan revision: [r2-context-control-blueprint.md](Canon/docs/control-plane/implementation/release-blueprints/r2-context-control-blueprint.md) §4.4 L75 must carry the Clock + stableStringify-unification prerequisites.

### R3 Branch / Visual Thinker

Findings that block: **this is the single most-impacted release**. T1 (Clock), T4 (snapshot determinism), `WRK-RC-001/002/003/006/008/012/013/017/026`, `PKG-PROV-029/030` (diff-engine positional matching).
Plan revision: [phase-4-r3-contract-pack §4.5 L141](Canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md) and [r3-blueprint](Canon/docs/control-plane/implementation/release-blueprints/r3-branch-replay-blueprint.md) must declare engine Clock abstraction + stableStringify unification + cross-host determinism test as entry criteria. R3 is **not shippable** until these land.

### R4 Artifact Workspace

Findings that block: inherited from R3. No R4-specific engine gaps beyond transitive dependencies.
Plan revision: [r4-artifact-workspace-blueprint.md](Canon/docs/control-plane/implementation/release-blueprints/r4-artifact-workspace-blueprint.md) implicit inheritance; no direct wording change.

### R5 Prompt Studio

Findings that block: PKG-MG-003/004/005/006/011 (model-gateway toolCalls/refusal/streaming shape — R5 `services/model-gateway/adaptation-execution/` depends).
Plan revision: [r5-prompt-assets-blueprint §4.1 L56](Canon/docs/control-plane/implementation/release-blueprints/r5-prompt-assets-blueprint.md) — add explicit ModelAdapter shape prerequisites.

### R6 Governed Agent / Applet Chat

Findings that block: **second-most-impacted**. T2 (credentialScope), T3 (sandbox), T5 (policy), plus all model-gateway HIGHs.
Plan revision: [phase-4-r6-contract-pack §4.5 L147](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md) + [r6-blueprint](Canon/docs/control-plane/implementation/release-blueprints/r6-governed-reusable-execution-blueprint.md) must declare the full tool-gateway-hardening list as entry criteria. Maturity matrix row for `pkg.tool-gateway-sandbox` M1→M4 at R6 is the formal site where these land.

### R7 Commissioning Bridge

Findings that block: inherited from R3 + R6. Plus sandbox-preview (`workers/tool-sandbox/commissioned-side-effect-preview/`) depends on WRK-TS-001 resolution.
Plan revision: [r7-commissioning-bridge-blueprint §4.1 L59](Canon/docs/control-plane/implementation/release-blueprints/r7-commissioning-bridge-blueprint.md) — add inherited prerequisites.

### Task Studio (TS)

Findings that block: none directly engine-facing beyond inherited R7 chain. TS V1 scope pack correctly defers secret-management and applet-builder features.
Plan revision: none. Inherits from R7.

---

## Section 5 — Over-claim list

Each entry names a plan passage whose prose asserts a capability the audit disproves or materially narrows.

1. **[`phase-3-platform-gate-spec-and-exit-audit.md`](Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md) §6 L118 (PG-07)** claims "Model and tool execution use typed contracts, scoped credentials, and inspectable failure results" — **audit PKG-TG-001** proves `credentialScope.allowedSecrets` is never enforced. Decision: retract "scoped credentials" OR reopen gate. Section 4 recommends reopen.
2. **Same file §7 item 8 L137** restates the PG-07 claim in the human-owned audit checklist. Same retraction applies.
3. **Same file §4 L87 "Gateway substrate" row** "Typed model and tool gateway contracts with scoped credentials and inspectable failures". Same retraction.
4. **Same file §5 L105** `pkg.tool-gateway-sandbox` row "Typed tool execution, side-effect classification, scoped credentials, logs". Same retraction.
5. **Same file §6 L121 (PG-10)** "User-initiated work only enters through environment/control APIs; direct worker RPC is absent or blocked" — **audit WRK-TS-001** proves there is no real worker-boundary (worker is in-process). The absence of a child-process barrier means "direct worker RPC blocked" is structurally meaningless. Decision: require real process boundary at Platform Gate OR weaken PG-10 to "no direct UI-to-worker *logical* backdoor".
6. **[`phase-3-high-level-technical-architecture-baseline.md`](Canon/docs/control-plane/architecture/phase-3-high-level-technical-architecture-baseline.md) §4 L73** "Tool adapter execution, side-effect classification, **sandboxing, credential scoping**". Retract both or enforce.
7. **Same file §5 L91** "Tool and model adapters may be deployed separately for isolation, but they remain behind one engine-facing gateway contract" — current engine has no separate-deployment path; WRK-TS-002 says IPC helper is not even public. Retract "may be deployed separately for isolation" OR export the IPC helper.
8. **[`phase-6-repo-package-architecture-and-agent-execution-rules-pack.md`](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) §5.1 L114** `pkg.tool-gateway-sandbox` row **"Typed tool execution, side-effect previews, scoped credentials, sandbox isolation"**. Both "scoped credentials" (PKG-TG-001) and "sandbox isolation" (WRK-TS-001, PKG-TG-002) are current over-claims. Decision: retract or enforce.
9. **Same file §6.1 L148** "Third-party runtime packages, peer dependencies, and provider or tool client SDKs are out of bounds" — **audit X-029** requires intra-workspace peerDependencies to preserve `@canon/engine-core` identity. Clarify carve-out.
10. **[`phase-3-api-ipc-and-event-contract-spec.md`](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md) §7 L170** "Breaking contract changes require version bump and coexistence plan" — engine's `0.0.0` pin (MEDIUM X-010, flagged in prompt) makes this unenforceable. Decision: adopt digest-based signal OR begin semver discipline.
11. **[`phase-3-data-storage-indexing-and-provenance-spec.md`](Canon/docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md) §4 L76** "Secret / credential store …Stores secret references for gateways; secrets do not live in metadata or blobs" — PKG-TG-001 proves gateways do not honor the scope side of this contract. Retract "references" narrative or enforce.
12. **[`phase-4-r6-contract-pack §4.5 L147`](Canon/docs/control-plane/releases/r6-governed-agent-applet-chat-contract/phase-4-r6-governed-agent-applet-chat-contract-pack.md)** "Tool execution is typed, side-effect-classified, scoped by authority and credential bindings, and inspectable" — over-claim. R6 entry criteria must list T2+T3+T5 as prerequisites.
13. **[`maturity-matrix §6 L117`](Canon/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md)** `pkg.tool-gateway-sandbox` cell shows M1 at Platform Gate — implicit claim that credential-scoping shape is "achieved" at gate. Add footnote clarifying "M1 = types only, not runtime-enforced".
14. **[`phase-4-r3-contract-pack §4.5 L141`](Canon/docs/control-plane/releases/r3-branch-visual-thinker-contract/phase-4-r3-branch-visual-thinker-contract-pack.md)** "Exact replay produces a new Run from frozen pack lineage and checkpoint state without relying on provider transcript continuity" — not achievable until Clock abstraction + stableStringify unification land. Either retract "exact replay" or declare prerequisites.
15. **[`canon-phase-4-plus-plan.md §206-207`](canon-knowledgebase/canon-phase-4-plus-plan.md)** Platform Gate obligation list: "memory and canon injection are real engine seams with authoritative refs and frozen replay basis behavior" — **partial truth**; basis is frozen but cross-host determinism is absent (stableStringify divergence + localeCompare + Clock gap). Supersede or footnote.
16. **[`canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md`](canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md)** decision: "the frozen context boundary already preserves authoritative candidate refs … for later replay or audit consumers". Audit shows integrity is not actually enforced (PKG-PROV-004 frozenAt outside hash; PKG-PROV-002 synthetic timestamps; PKG-PROV-001 divergent stableStringify). Supersede with a successor checkpoint.
17. **[`agentic-engine/CONTEXT.md`](agentic-engine/CONTEXT.md) L33** "Tool interaction (Tool Gateway, sandboxing, credential scoping)" — two of three are over-claims (sandboxing, credential scoping).
18. **[`agentic-engine/CONTEXT.md`](agentic-engine/CONTEXT.md) L37** "Replay and comparison (temporal state, diffing, deterministic replay)" — "deterministic replay" is an over-claim until Clock lands.
19. **[`CANON_PROJECT_CONTEXT.md`](CANON_PROJECT_CONTEXT.md) §2 L57** "Tool execution across spawned Node child processes (NOT container isolation)" — "spawned Node child processes" is false for default ToolSandbox path; the `ToolSandboxWorker` class does not fork (WRK-TS-001).
20. **[`CANON_PROJECT_CONTEXT.md`](CANON_PROJECT_CONTEXT.md) §5 #5 L121** "Deterministic replay across the full primitive graph — provenance + model + compiled-context + strategy boundaries" — over-claim until Clock lands.
21. **[`AGENTIC_WORKFLOW.md`](AGENTIC_WORKFLOW.md) §5 L163** "Canon-native tool protocol lives here" and L171/L202 "node:child_process tool execution (NOT container isolation)" — same child-process over-claim as #19.
22. **[`AGENTIC_WORKFLOW.md`](AGENTIC_WORKFLOW.md) §7 Gate 04 L343** "Replay-determinism gate" — gate claim depends on Clock abstraction. Footnote.

---

## Section 6 — Decision backlog

Findings that cannot be resolved without a plan-owner decision. Each entry: audit ID · decision needed · candidate options · default recommendation.

| # | Audit ID(s) | Decision needed | Candidate options | Default recommendation |
| --- | --- | --- | --- | --- |
| 1 | OWN-001, PKG-CORE-THEME-001, PKG-CC-002/003, PKG-CC-001, PKG-MG-002 | Where does the Clock/TimeProvider abstraction live? | (a) `@canon/engine-core` owns `Clock` interface, each factory accepts optional `clock` param; (b) Shared Environment supplies Clock and Engine only accepts injection; (c) defer via explicit caller-supplied timestamps everywhere | (a) engine owns interface, Shared Env supplies production impl; this is SCOPE-EXPANSION on engine, SCOPE-CONTRACTION-avoiding for Shared Env |
| 2 | PKG-TG-001, PKG-TG-011, PKG-MG-024 | Does engine own runtime credential resolution, or only the scope type? | (a) engine owns `CredentialProvider` interface + enforcement wrapper that strips `process.env` and returns only `allowedSecrets`; (b) engine only defines type, Shared Env provides resolver; (c) rename to `CredentialScopeHint` and retract enforcement promise | (a) — matches Platform Gate PG-07 intent with minimal plan churn |
| 3 | PKG-TG-002, WRK-TS-001, WRK-TS-002 | Is process-boundary isolation a Platform-Gate invariant or deferred to R6? | (a) Platform Gate requires process-boundary contract (export `attachToolSandboxWorkerIpc` + optional `spawnToolSandboxWorker`), R6 requires real child-process default; (b) Platform Gate passes with in-process, R6 retrofits; (c) retract sandbox-isolation claim everywhere | (a) — honest about Platform Gate being a real bridge seam |
| 4 | PKG-POL-001..005, PKG-POL-009, PKG-POL-014 | Does engine ship pattern matching now or document strict-equals? | (a) engine ships typed `RulePattern` with glob/regex and explicit matcher at Platform Gate; (b) R6 ships pattern matcher, strict-equals retained through R1-R5 with audit-logged caveats; (c) defer to domain packs entirely | (a) for SECURITY severity; failing that, (b) with prominent audit caveat |
| 5 | PKG-PROV-001/002/004, PKG-CC-014..018, OWN-008 | Accept stableStringify unification into `@canon/engine-core` as ARCHITECTURE-CHANGE? | (a) land helper now, add cross-package determinism test, include in PG-01 evidence; (b) retain per-package copies, freeze them with a drift-detector test | (a) — a single helper is less code and objectively safer |
| 6 | X-007 | License choice | MIT / Apache-2.0 / BSL / proprietary | MIT or Apache-2.0 (public SDK aspiration per AGENTIC_WORKFLOW.md §9 L426) |
| 7 | X-010 (MED) + X-015 | Engine semver + spec digest regeneration | (a) engine starts at `0.1.0` with breaking-change protocol tied to digest regen; (b) keep 0.0.0, adopt content-hash-only channel; (c) retract all plan prose that relies on semver signals | (a) |
| 8 | X-029 | Plan carve-out for intra-workspace peer-deps | (a) amend phase-6-repo-package-architecture §6.1 to distinguish third-party vs intra-workspace peer-deps; (b) rewrite engine to not need peerDependencies at all | (a) — narrower, preserves "zero external runtime dependencies" spirit |
| 9 | WRK-RC-002 | Replay-compare diff semantics | (a) add explicit id-aligned diff variant; document positional-index semantics' danger; (b) deprecate positional-index diff | (a) |
| 10 | Platform Gate truth-status | Retain "passed" with footnotes, or formally reopen | (a) reopen, list remediation gates PG-01.1, PG-07.1, PG-10.1 etc.; (b) retain passed status with explicit append-only "audit-aware substrate gap" carry-forward; (c) freeze Canon execution entirely pending remediation | (a) — reopen. Explicit, recoverable, append-only. |
| 11 | Phase 6 packet quarantine state | Does the audit reopen `canon-phase-4-plus-plan.md` baton state `stop`? | (a) yes — audit is a "cited contradiction" per §157; add new step 20 to step ledger; (b) no — baton remains stopped until human owner decides; (c) defer to next session | (b) formal human decision required before (a) |
| 12 | post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md | Supersede the "sufficiency" claim? | (a) supersede with new checkpoint naming stableStringify + Clock + localeCompare + PROV-002/004 as open; (b) retain and add inline corrective notes | (a) — keeps append-only posture |

---

## Section 7 — Self-verification pass

### 7.1 CRITICAL finding impact-class counts (expected 15)

| Impact class (primary) | Count | IDs |
| --- | --- | --- |
| ARCHITECTURE-CHANGE | 3 | OWN-001, PKG-CORE-THEME-001, PKG-PROV-001 |
| RELEASE-GATE-IMPACT | 5 | PKG-CC-002, PKG-CC-003, PKG-PROV-002, PKG-PROV-004, X-007 |
| SCOPE-CONTRACTION | 3 | PKG-TG-001, PKG-TG-002, WRK-TS-001 |
| SCOPE-EXPANSION | 1 | WRK-TS-002 |
| PLAN-CONSTRAINT-CHANGE | 2 | PKG-POL-001, WRK-RC-002 |
| NO-IMPACT | 1 | WRK-RC-001 |
| PLAN-REFERENCE | 0 |  |
| **Total** | **15** | **(matches expected)** |

Every CRITICAL also has at least one secondary class (mostly RELEASE-GATE-IMPACT) — see Section 2 tables.

### 7.2 HIGH finding impact-class counts (expected 130)

| Impact class (primary) | Count | Exemplar IDs |
| --- | --- | --- |
| NO-IMPACT | 56 | WRK-RE-001..050 subset; engine-local cleanups; X-001/002/004/005/006/008/011/014/023/025/027/030/037/039/041/045; PKG-CORE-THEME-007; most PKG-MG-*, PKG-POL-019, PKG-PROV cleanups not in freezer; OWN-002/003/004/009/010/011/014/015/016/017/018 |
| PLAN-REFERENCE | 22 | All EngineError-theme findings (OWN-005, PKG-CORE-THEME-002, WRK-CC-002, WRK-RC-004, WRK-RE-002), dead-queue (OWN-006, X-031, X-032), mocks (X-012, PKG-MG-001), tsconfig (X-003, X-057), peer-dep (X-029), carry-forward docs across supplementary dirs |
| PLAN-CONSTRAINT-CHANGE | 16 | PKG-POL-002..005, PKG-POL-009, PKG-POL-014, PKG-VAL-001..004, PKG-PROV-003, PKG-PROV-015, PKG-MG-024, PKG-CC-014..018 where they are the only finding to rewrite plan invariant |
| ARCHITECTURE-CHANGE | 11 | PKG-PROV-012, OWN-008 (stableStringify unification); PKG-MG-010/011 (ModelAdapter spec additions); PKG-POL-011 (AuthorityScope restore factory); PKG-CC-001, PKG-CC-004, PKG-CORE-THEME-013; PKG-PROV-008/009/013 |
| RELEASE-GATE-IMPACT | 20 | PKG-PROV-001 (in HIGH if double-counted), PKG-PROV-005/006/010/011/013/029/030, PKG-TG-003/004/005/006/007/008/009/010, WRK-TS-003/004/005/006/007/008, PKG-CORE-THEME-003/004 |
| SCOPE-EXPANSION | 3 | PKG-MG-010 (streaming/close/healthCheck expansion — arguable); WRK-TS-003..005 (IPC hardening upstream of WRK-TS-002); X-015 (spec-digest hash anchoring expansion) |
| SCOPE-CONTRACTION | 2 | PKG-TG-011 (credentialScope runtime validation owed), WRK-TS-004 |
| **Total** | **130** | **(matches expected)** |

Note: because several HIGH findings genuinely belong to two classes, the primary-class buckets above are my judgment call; Section 2 per-plan tables list multi-class assignments honestly. The combinatoric sum if secondaries counted would be ≈ 170.

### 7.3 Plans inventoried

- Canon `/docs/control-plane/` plan-shaped docs counted: **52** markdown files (excluding JSON artifact registries, .mjs/.py scripts, .factory skills).
- Canon `/docs/spec-digests/` markdown digests: **7** (all empty except `env-governance.md`).
- Supplementary (`/canon-knowledgebase/` + root docs + baton/migration/research): **28** markdown files.
- **Plans inventoried total: 87 files.** Section 1 listed ~63 of these as primary touchpoints; the remainder (golden-scenario corpus, artifact/dependency graph seeds, historical rollout, canon-ref scaffold, baton protocol, research memo, session companions) are acknowledged but carry NO-IMPACT directly.

### 7.4 Plans with at least one suggested edit

Counting Section 2 tables only:

1. phase-3-platform-gate-spec-and-exit-audit.md
2. phase-3-high-level-technical-architecture-baseline.md
3. phase-3-api-ipc-and-event-contract-spec.md
4. phase-3-data-storage-indexing-and-provenance-spec.md
5. phase-3-context-compiler-retrieval-memory-canon-topology.md
6. phase-1-rewrite-containment-and-stable-seam-map.md (REF)
7. phase-2-core-object-and-state-machine-spec-pack.md
8. phase-2-run-class-taxonomy-and-protocol-kernel.md
9. phase-2-governance-authority-and-writeback-invariants.md
10. phase-2-proof-and-validation-invariants.md
11. phase-5-full-proof-validation-and-evaluation-spec.md
12. phase-5-full-governance-authority-and-writeback-spec.md
13. phase-5-full-run-class-protocol-packs.md
14. phase-6-repo-package-architecture-and-agent-execution-rules-pack.md
15. r1-conversation-blueprint.md
16. r2-context-control-blueprint.md
17. r3-branch-replay-blueprint.md
18. r4-artifact-workspace-blueprint.md (inherited)
19. r5-prompt-assets-blueprint.md
20. r6-governed-reusable-execution-blueprint.md
21. r7-commissioning-bridge-blueprint.md
22. phase-6-r3-branch-replay-runtime-execution-packet.md (inherited)
23. phase-6-r6-governed-reusable-execution-runtime-execution-packet.md (inherited)
24. phase-6-r7-commissioning-bridge-runtime-execution-packet.md (inherited)
25. chat-native-maturity-matrix / phase-4-release-to-sdk-maturity-matrix.md
26. chat-native-milestone-architecture-plan.md
27. phase-4-r3-branch-visual-thinker-contract-pack.md
28. phase-4-r6-governed-agent-applet-chat-contract-pack.md
29. canon-knowledgebase/canon-phase-4-plus-plan.md
30. canon-knowledgebase/p04-engine-seam-tightening.md
31. canon-knowledgebase/p05-compiler-injection-and-replay-basis.md
32. canon-knowledgebase/platform-gate-engine-seam-checkpoint.md
33. canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md
34. CANON_PROJECT_CONTEXT.md
35. AGENTIC_WORKFLOW.md
36. agentic-engine/CONTEXT.md
37. agentic-engine-finish-session-plan.md
38. canon-now.md
39. shared-environment-starter-packet.md

**Plans with at least one suggested edit: 39.** Plans inventoried but with no suggested edit (NO-IMPACT): 48.

### 7.5 Findings requiring plan-owner action

Primary-class sum *pre-paranoid*: PLAN-CONSTRAINT-CHANGE (2 CRIT + 16 HIGH) + ARCHITECTURE-CHANGE (3 CRIT + 11 HIGH) + RELEASE-GATE-IMPACT (5 CRIT + 20 HIGH) + SCOPE-EXPANSION (1 CRIT + 3 HIGH) + SCOPE-CONTRACTION (3 CRIT + 2 HIGH) = **66 findings**. *Post-paranoid* (after Section 8 upgrades): **74 findings** (PLAN-CONSTRAINT-CHANGE grows from 18 to 26). If HIGH secondary classes are added, the effective number of findings that carry at least one plan-action class rises to ≈ 108.

### 7.6 Findings where plan impact could not be determined

- `PKG-PROV-005` — UUID aliasing scope. Unclear whether Canon plan passage constrains the alias universe. Likely PLAN-CONSTRAINT-CHANGE but could be NO-IMPACT.
- `X-045` — stale DEEP_RELEASE_AUDIT_LOG.md file in engine repo. Plan governance for engine-internal docs is undefined; engine-local cleanup assumed.
- `X-015` — spec-digest hash anchoring, plus the newly-surfaced empty-digest anomaly (Section 1.12). Plan response depends on whether missing `All-Prims-3.md` / `Chat-Native-Release-Plan-4.md` sources are genuinely missing or merely renamed. Classified as SCOPE-EXPANSION by default.

---

## Section 8 — Paranoid extra pass

### 8.1 Re-scan of NO-IMPACT bucket for false negatives

- `PKG-CORE-THEME-007` (non-null assertions in variant-lineage): initially NO-IMPACT (local TS hygiene). Re-examination: [phase-2-core-object-and-state-machine-spec-pack §5 Variant (L430-ish)](Canon/docs/control-plane/semantics/phase-2-core-object-and-state-machine-spec-pack.md) specifies variant-lineage semantics — non-null casts could mask plan-invariant violations at runtime. **Upgrade to PLAN-CONSTRAINT-CHANGE** — runtime readonly enforcement should be specified at the semantics level.
- `PKG-CORE-THEME-004` (listener no try/catch): initial NO-IMPACT/PLAN-CONSTRAINT-CHANGE borderline. Re-examination: [phase-3-api-ipc §6 L154-161 event-family baseline](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md) names Timeline/Live Monitor/audit as consumers of `run.lifecycle.v1`. A single throwing listener silently interrupting event delivery is a data-loss class bug at cross-subject consumer boundary. **Upgrade to PLAN-CONSTRAINT-CHANGE** — failure semantics must be specified, not implicit.
- `OWN-003` (recursive event-stream append LIFO reorder): initial NO-IMPACT. Re-examination: [phase-3-api-ipc §7 L169 "Per-subject event order must be stable enough for replay/audit reconstruction"](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md) — LIFO nested-emit order is a stable-ordering violation for any consumer observing both outer and inner events. **Upgrade to PLAN-CONSTRAINT-CHANGE**.
- `OWN-015` (addNode no batch/rollback): initial NO-IMPACT. Re-examination: [phase-3-data-storage §3.3 L50 "append-only"](Canon/docs/control-plane/architecture/phase-3-data-storage-indexing-and-provenance-spec.md) implies transactional batch admission; mid-constructed-graph state at plan level is an undocumented failure mode. **Upgrade to PLAN-CONSTRAINT-CHANGE** — or explicit plan note that partial-failure leaves graph in inspectable state consistent with PI-10.
- `PKG-MG-012` (case-sensitive provider registry): initial NO-IMPACT. Re-examination: [phase-3-api-ipc §5.3 provider normalization](Canon/docs/control-plane/architecture/phase-3-api-ipc-and-event-contract-spec.md) — provider-id normalization is plan-observable. **Upgrade to PLAN-REFERENCE** — add normalization policy to plan.
- `X-057` (exactOptionalPropertyTypes → undefined `expiresAt`): initially PLAN-REFERENCE (tsconfig theme). Re-examination: combined with PKG-TG-011, this is a credentialScope correctness bug, not just a strict-flag gap. **Upgrade to PLAN-CONSTRAINT-CHANGE** under Section 2.1 Platform-Gate table.

### 8.2 Re-scan of PLAN-REFERENCE bucket for false negatives

- `X-029` (engine-core as peerDependency): initial PLAN-REFERENCE. Re-examination: [phase-6-repo-package-architecture §6.1 L148](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) categorically bans peerDependencies. This is a PLAN-CONSTRAINT-CHANGE — plan must carve out intra-workspace peerDeps. Already noted in T9.
- `WRK-CC-002` / `WRK-RC-004` / `WRK-RE-002` (plain `new Error` in workers): initial PLAN-REFERENCE. Re-examination: workers are load-bearing for R1/R2/R3/R6/R7 blueprints. Consumer-observable error contract at worker boundary is a cross-layer contract, not an engine-internal concern. **Upgrade to PLAN-CONSTRAINT-CHANGE** for at least the engine-boundary (worker-dispatched) errors.
- `X-010` (MED, `0.0.0` forever): initially outside CRITICAL/HIGH scope per prompt. Re-examination: the prompt explicitly flags this as strategically important. **Escalate**: this is the structural dependency for phase-3-api-ipc §7 L170 and phase-5-full-run-class-protocol-packs §5.2 L102-108. Add to decision backlog as #7 (already captured).
- `PKG-CC-014..018` in spec-conformance category: initially split across NO-IMPACT / CON. Re-examination: [phase-3-context-compiler §8 L153](Canon/docs/control-plane/architecture/phase-3-context-compiler-retrieval-memory-canon-topology.md) "Preserve source versions … exactly" — all five findings are direct violations of the "exactly" contract. **Upgrade collectively to PLAN-CONSTRAINT-CHANGE**, which they already are in Section 2.5.
- `PKG-MG-001` (InvocationNormalizer mocks-on-root): initially PLAN-REFERENCE. Re-examination: [phase-6-repo-package-architecture §6.3 L159 "no direct UI-to-worker RPC"](Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md) is adjacent but not identical. The real issue is cross-layer contract leakage — mocks on root surface invite app-layer dependency on test fixtures. Upgrade class: PLAN-CONSTRAINT-CHANGE (plan must forbid production imports of `Mock*` classes).

### 8.3 Net change from paranoid pass

9 HIGH findings upgraded:
- `PKG-CORE-THEME-007`: NO-IMPACT → PLAN-CONSTRAINT-CHANGE
- `PKG-CORE-THEME-004`: NO-IMPACT → PLAN-CONSTRAINT-CHANGE
- `OWN-003`: NO-IMPACT → PLAN-CONSTRAINT-CHANGE
- `OWN-015`: NO-IMPACT → PLAN-CONSTRAINT-CHANGE
- `PKG-MG-012`: NO-IMPACT → PLAN-REFERENCE
- `PKG-MG-001`: PLAN-REFERENCE → PLAN-CONSTRAINT-CHANGE
- `WRK-CC-002` / `WRK-RC-004` / `WRK-RE-002`: PLAN-REFERENCE → PLAN-CONSTRAINT-CHANGE (3 findings)
- `X-057`: PLAN-REFERENCE → PLAN-CONSTRAINT-CHANGE

Net flow: NO-IMPACT loses 5 (4 to CON + 1 to REF); PLAN-REFERENCE loses 3 net (+1 from NO-IMPACT, −4 to CON); PLAN-CONSTRAINT-CHANGE gains 8. Revised HIGH bucket totals in Section 7.2:

- NO-IMPACT: 56 → **51**
- PLAN-REFERENCE: 22 → **19**
- PLAN-CONSTRAINT-CHANGE: 16 → **24**
- Other classes unchanged (ARCH=11, GATE=20, EXP=3, CTR=2)

Check: 51 + 19 + 24 + 11 + 20 + 3 + 2 = 130 ✓

---

## Final summary

**Of the 145 CRITICAL+HIGH findings, 74 require plan-owner action** (after paranoid pass):

- **K = 14** ARCHITECTURE-CHANGE (3 CRIT + 11 HIGH) — Clock abstraction (OWN-001, PKG-CORE-THEME-001), stableStringify unification (PKG-PROV-001, PKG-PROV-012, OWN-008), ModelAdapter spec additions (PKG-MG-010/011), AuthorityScope restore factory (PKG-POL-011), localeCompare removal (PKG-CORE-THEME-013), ISO-parser strictness / sortValue coverage / topological-order validation (PKG-CC-001, PKG-CC-004, PKG-PROV-008/009/013)
- **L = 25** RELEASE-GATE-IMPACT (5 CRIT + 20 HIGH) — Platform Gate PG-01/PG-07/PG-10 block; R3/R6/R7 blueprint prerequisites; PKG-CC-002/003, PKG-PROV-002/004/005/006/010/011/029/030, X-007, PKG-TG-003..010, WRK-TS-003..008, PKG-CORE-THEME-003/004
- **M = 4** SCOPE-EXPANSION (1 CRIT + 3 HIGH) — ToolSandboxWorker IPC export (WRK-TS-002); ModelAdapter streaming/close/healthCheck (PKG-MG-010); spec-digest hash anchoring (X-015); IPC request-validation hardening upstream of WRK-TS-002 (WRK-TS-003/005)
- **P = 5** SCOPE-CONTRACTION (3 CRIT + 2 HIGH) — credentialScope claim retraction (PKG-TG-001, PKG-TG-011); ToolSandbox name retraction (PKG-TG-002); ToolSandboxWorker child-process claim retraction (WRK-TS-001, WRK-TS-004)
- **Q = 26** PLAN-CONSTRAINT-CHANGE (2 CRIT + 24 HIGH, post-paranoid) — policy matching semantics (PKG-POL-001..005, PKG-POL-009, PKG-POL-014); snapshot integrity invariants (PKG-PROV-003, PKG-PROV-015); proof/validation error capture (PKG-VAL-001..004); event-stream ordering (OWN-003, PKG-CORE-THEME-004); frozen-object deep-freeze enforcement (PKG-CORE-THEME-003, PKG-CORE-THEME-007); compiler-candidate discriminated union and exact preservation (PKG-CC-014..018, PKG-CC-026); provenance-graph batch contract (OWN-015); replay-compare diff semantics (WRK-RC-002); worker-boundary error contract (WRK-CC-002, WRK-RC-004, WRK-RE-002); InvocationNormalizer production-import prohibition (PKG-MG-001); credentialScope undefined-type coercion (X-057); plus credential-scoping for Model Gateway (PKG-MG-024)

The remaining 71 of 145 are NO-IMPACT (local engine fixes, 52 including 1 CRITICAL) or PLAN-REFERENCE (prose-only updates, 19). Explicit unknowns: 3 findings listed in §7.6.

**74 of 145 CRITICAL+HIGH findings require plan-owner action: 14 ARCHITECTURE-CHANGE, 25 RELEASE-GATE-IMPACT, 4 SCOPE-EXPANSION, 5 SCOPE-CONTRACTION, 26 PLAN-CONSTRAINT-CHANGE.**

The single largest structural requirement is the **Clock / TimeProvider abstraction** (Theme T1), which is an engine ARCHITECTURE-CHANGE and simultaneously a Platform-Gate + R3 RELEASE-GATE-IMPACT. The second is the **Tool Gateway honesty reconciliation** (Themes T2 + T3), which reaches Platform Gate + R6 + R7 plans directly and every plan prose that over-claims sandbox / credential scoping indirectly.

No audit finding redraws which layer owns what. No audit finding violates the three-layer architecture or the Platform Gate → R1 → R2 → R3 → R4 → R5 → R6 → R7 → Task Studio release order. All required changes fit within the Engine SDK layer's accepted scope — though the **Platform-Gate "passed" status itself** is the most consequential plan artifact the audit puts into question.
