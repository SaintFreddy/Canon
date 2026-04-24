# Canon Phase 4+ Plan

## Plan Contract

- status: active authority
- scope: Platform Gate through `R7`, with the knowledgebase architecture absorbed into the main Canon release path
- execution_shape: bounded step plan
- step_budget: each active step should fit within a fresh-session working budget of roughly 50k tokens and must stay below about 75k tokens before handoff or rebasing
- ledger_rule: after each completed step, append the carry-forward ledger in the same session
- replaces_as_active_authority:
  - `canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan`
- preserves_as_historical_support:
  - `canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan`
  - `canon-ref:dev/kb/canon-phase-4-plus-plan-completed-steps-history`
  - `canon-ref:dev/kb/p00-architecture-delta`
  - `canon-ref:dev/kb/p01-shared-environment-knowledge-objects`
  - `canon-ref:dev/kb/p02-storage-and-query-lanes`
  - `canon-ref:dev/kb/p03-governance-and-event-spine-integration`
  - `canon-ref:dev/kb/p04-engine-seam-tightening`
  - `canon-ref:dev/kb/p05-compiler-injection-and-replay-basis`
- primary_source_basis:
  - `canon-ref:dev/ref/original-papers/chat-native-release-plan`
  - `https://github.com/SaintFreddy/Canon/blob/main/docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md`
  - `https://github.com/SaintFreddy/Canon/blob/main/docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md`
  - `canon-ref:dev/kb/canon-native-self-learning-knowledgebase-layer`
  - `canon-ref:dev/kb/p00-architecture-delta`
  - `canon-ref:dev/kb/p01-shared-environment-knowledge-objects`
  - `canon-ref:dev/kb/p02-storage-and-query-lanes`
  - `canon-ref:dev/kb/p03-governance-and-event-spine-integration`
  - `canon-ref:dev/kb/p04-engine-seam-tightening`
  - `canon-ref:dev/kb/p05-compiler-injection-and-replay-basis`
- local_term_and_fact_registry:
  - `canon-ref:dev/kb/identity/canon-canon-registry`
- out_of_scope:
  - rewriting Phases 1-3
  - reopening the `P00-P05` convergence baseline
  - running `P06-P13` as a second packet track beside this plan
  - making chat the durable owner of memory or canon truth
  - silent promotion of learned material into accepted truth
  - inventing a Task Studio-private knowledge ontology

## Purpose

This file restores one active Canon Phase 4+ authority after pre-phase-4 convergence.

The rollout plan did its job by bringing Canon to a new substrate baseline through `P00-P05`.
From this point on, Canon should execute release work through one integrated release story rather than through a side-plan of later packets.

`P00-P05` are now inherited baseline decisions.
`P06-P13` survive only as migration labels that help map old packet thinking into the release stages below.

Fresh sessions using this plan should also read `canon-ref:dev/kb/identity/canon-canon-registry` when workspace terminology, workflow labels, or durable local planning facts matter.
The registry normalizes local Canon language, but it does not override higher-authority Canon architecture or release sources.

## Current Plan Steps

All 20 bounded steps are `complete`. The compact step-status table below is the live recovery surface; the full `Objective` / `Completion signal` / (where applicable) `Closure` narrative for each step lives in `canon-ref:dev/kb/canon-phase-4-plus-plan-completed-steps-history`.

| # | Label | Status |
| --- | --- | --- |
| 1 | cross-repo search and impact map | `complete` |
| 2 | local authority and terminology sync | `complete` |
| 3 | upstream Canon Tier 1 authority sync | `complete` |
| 4 | upstream Canon downstream surface sync | `complete` |
| 5 | local recovery recheck after upstream sync | `complete` |
| 6 | post-sync execution-plan commitment | `complete` |
| 7 | `PG-1` Platform Gate engine seam checkpoint and gap map | `complete` |
| 8 | `PG-2` frozen knowledge participation basis contract and wiring | `complete` |
| 9 | `PG-3` authoritative knowledge-lane ref passthrough | `complete` |
| 10 | `PG-4` knowledge-lane admission projection seam | `complete` |
| 11 | `PG-5` memory-before-canon compiler staging | `complete` |
| 12 | `PG-6` legacy knowledge-lane fallback isolation | `complete` |
| 13 | post-evidence compiler stage-order correction | `complete` |
| 14 | post-reopen host-projection lane-authority checkpoint | `complete` |
| 15 | post-reopen lane-level host-projection authority implementation | `complete` |
| 16 | post-reopen ref-first host-projection consumption | `complete` |
| 17 | post-reopen accepted-knowledge lane metadata passthrough | `complete` |
| 18 | post-reopen frozen-posture replay/audit sufficiency checkpoint | `complete` |
| 19 | post-forensic Phase 6 boundary correction | `complete` |
| 20 | audit-cited-contradiction reopen gate (closed 2026-04-24 via `CF-0097`; downstream propagation via `CF-0098`..`CF-0100`; live closure evidence duplicated in `Committed Post-Sync Execution Boundary` below) | `complete` |

Post-`PG-6` correction closure note: the bounded stage-order correction is now landed locally. `ContextCompilerPipeline` budgets optional evidence before memory and accepted knowledge, targeted regression coverage proves the inherited `evidence -> memory -> canon -> freeze` order under tight budget pressure, and broad lifecycle-fallback retirement remains deferred until accepted explicit host-projection contract authority exists.

## Committed Post-Sync Execution Boundary

- status: active post-sync boundary authority
- satisfied preconditions:
  - Step 3 Tier 1 upstream authority sync is locally complete in `Canon`
  - Step 4 downstream surface sync is locally complete in `Canon`
  - Step 5 recovery recheck is complete in this workspace
  - the language-query memo is complete in `canon-ref:dev/archive/agentic-engine-language-query-memo`
  - the `PG-1` seam checkpoint is complete in `canon-ref:dev/kb/platform-gate-engine-seam-checkpoint`
  - the `PG-2` knowledge participation basis slice is complete in `agentic-engine`
  - the `PG-3` authoritative knowledge-lane ref passthrough slice is complete in `agentic-engine`
  - the `PG-4` knowledge-lane admission projection seam is complete in `agentic-engine`
  - the `PG-5` memory-before-canon compiler staging slice is complete in `agentic-engine`
  - the `PG-6` legacy knowledge-lane fallback isolation slice is complete in `agentic-engine`
  - the post-evidence compiler stage-order correction is complete in `agentic-engine`
  - the validated engine seam pack is published on `agentic-engine` `origin/main`, and the Canon promotion pack is published on `Canon` `origin/main`
  - the host-projection contract wording is published on Canon `origin/main` at `fafd681`, the reopen checklist passes against published authority, and the first post-reopen seam decision is recorded in `canon-ref:dev/kb/post-reopen-host-projection-lane-authority-checkpoint`
- the first post-reopen lane-level authoritative host-projection implementation slice is complete locally in `agentic-engine`, and `corepack pnpm typecheck` plus `corepack pnpm test` both passed for that slice
- the second post-reopen ref-first host-projection consumption slice is complete locally in `agentic-engine`, and the accepted-knowledge lane metadata checkpoint selected the next bounded seam step honestly
- the third post-reopen accepted-knowledge lane metadata passthrough slice is complete locally in `agentic-engine`, and the frozen-posture replay/audit sufficiency checkpoint was selected honestly from published Canon authority
- the frozen-posture replay/audit sufficiency checkpoint is complete locally: direct inspection of published Canon wording plus the current compiled-context, deterministic snapshot, replay-contract, and replay-compare surfaces shows that the frozen context seam already preserves authoritative candidate refs, explicit lane input state, inclusion or exclusion decisions, explicit-vs-fallback admission basis, optional canon-lane `mode`, and optional validity summary for later replay or audit consumers
- corrective classification:
  - accepted Phase 6 materials in `Canon` model future roots under `apps/`, `packages/`, `services/`, and `workers/`, and they define future packet order for those roots
  - accepted Canon README plus the accepted repo/package pack, current-state view, and execution-packet index now state explicitly that this modeling is not itself a new higher-authority reopen event and does not authorize local implementation by default
  - the local `canon-ref:dev/kb/phase-6-r1-conversation-entry-checkpoint`, `canon-ref:dev/kb/phase-6-r1-conversation-contracts-objects-packet-checkpoint`, and `canon-ref:dev/kb/phase-6-r1-conversation-runtime-execution-packet-checkpoint` are preserved as evidence of the 2026-04-18 local inference chain, not as live next-step authority
  - Canon remains the accepted authority/control-plane repo for now, and the local code currently present under `Canon/packages/`, `Canon/services/`, and `Canon/workers/` remains on disk only as quarantined draft state for possible later ratification or reuse; do not delete it, but do not treat it as published landing or the active next step
  - the 2026-04-18 engine audit (`AGENTIC_ENGINE_AUDIT_LOG.md` plus `CANON_PLAN_IMPACT_REPORT.md`) constitutes a cited-contradiction reopen event per §157, reopening an authority-repair step (step 20) without invalidating earlier baseline decisions; Inherited Baseline items 1-10 and the completed step 1-19 record remain carry-forward substrate truth
- next bounded execution step:
  - step 20 — audit-cited-contradiction reopen gate — `complete` as of 2026-04-24. Ordinary baton continuation is cleared to resume; the next bounded step is **unassigned** pending plan-owner selection from the stage plan below (any `R1`..`R7` stage entry). The Platform Gate three-packet downstream propagation sequence (PG-R1 Canon PR #17, PG-R2 Canon PR #35, PG-R3 Canon PR #39) has landed, and Platform Gate §0.1.1 sub-gates PG-01.1 / PG-07.1 / PG-10.1 all closed 2026-04-24 via `pkt.platform-gate-subgate-closure.v1`, lifting the prior engine-closure "locally closed" supersession. No step auto-activates under the audit-reopen hold lift; see `canon-ref:dev/canon-now` for the ready-state baton record and the CF-0089..CF-0100 carry-forward chain for the full wave-closure evidence.
- verification surface:
  - `archive/gpt5_browser_packet/_canon_registry/operator-final-verdict.md`
  - `archive/gpt5_browser_packet/_canon_registry/what-wait-means-now.md`
  - `CANON_PROJECT_CONTEXT.md`
  - `Canon/README.md`
  - `Canon/docs/control-plane/core/codebase-current-state.json`
  - `Canon/docs/control-plane/AGENTS.md`
  - `Canon/docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md`
  - `Canon/docs/control-plane/implementation/release-blueprints/r1-conversation-blueprint.md`
  - `Canon/docs/control-plane/core/phase-6-execution-packet-index.json`
  - `canon-ref:dev/kb/phase-6-r1-conversation-entry-checkpoint`
- reopen rule:
  - reopen Step 4 only if a later session finds a specific contradictory upstream Canon file rather than local wording drift
  - reopen the closed post-reopen engine seam or any post-Platform-Gate implementation continuation only if later accepted higher-authority Canon material explicitly names another bounded step or a cited contradiction proves the current boundary wrong
  - an explicit user choice of a different bounded task may proceed, but it is not automatic continuation of the invalid Phase 6 chain
  - do not resume `contracts_objects`, `runtime_execution`, or `surface_validation` by default from the local draft `Canon/packages/`, `Canon/services/`, or `Canon/workers/` roots
- durable-state rule:
  - update `canon-ref:dev/canon-now`, `canon-ref:dev/kb/canon-tasks`, `canon-ref:dev/kb/canon-knowledgebase-layer-session-companion`, and `canon-ref:dev/kb/canon-knowledgebase-layer-carry-forward` in the same session whenever a later authority change or contradiction reopens this seam

## Inherited Baseline

The following decisions are already settled and must be treated as carry-forward substrate truth for every later stage.

1. Durable memory and canon truth live in the shared environment, not in chat and not in the engine runtime.
2. The engine owns only the host-neutral injection, compilation-reporting, and replay-safe seam for memory and canon participation.
3. Durable learning stays proposal-first and review-gated on the route `event -> proposal -> review -> approved object -> explicit injection`.
4. Memory and canon stay separate lanes with immutable revisions, explicit scope, and provenance requirements.
5. The first storage posture is relational-first authoritative state plus append-only events plus blob payloads plus rebuildable lexical, vector, and provenance projections.
6. Compilation stays explicit-stage and freeze-first: evidence assembly first, then memory injection, then canon injection, then policy and authority freeze.
7. Replay correctness depends on frozen authoritative refs and visible inclusion or exclusion reasons, not on rerunning mutable retrieval.
8. Apps own projections, controls, review surfaces, and disclosure, but they do not own truth promotion or a second durable knowledge model.
9. The release order stays fixed: Platform Gate -> `R1` -> `R2` -> `R3` -> `R4` -> `R5` -> `R6` -> `R7` -> Task Studio.
10. The bridge stages remain Platform Gate, `R4`, and `R7`; they carry substrate decisions forward rather than reopening them locally.

## Legacy Packet Absorption Map

The rollout packet labels are preserved only so later sessions can translate old notes into the canonical release path.

| Legacy packet label | Canonical home in this plan | Current meaning |
| --- | --- | --- |
| `P00-P05` | inherited baseline | already absorbed substrate decisions; not active packets |
| `P06` | Platform Gate through `R2` | passive capture event model and scope discipline that keep early learning proposal-first |
| `P07` | Platform Gate through `R2` | internal distillation and review-queue substrate needed before later public governance surfaces widen |
| `P08` | `R1-R2` | honest chat and pack projections for knowledge participation |
| `P09` | `R3` | branch, replay, compare, and knowledge-basis correctness |
| `P10` | `R4` | artifact-centered knowledge governance and continuity |
| `P11` | `R5` | prompt-asset integration without prompt-side shadow memory |
| `P12` | `R6` | governed applet learning policies and reusable execution constraints |
| `P13` | `R7` | commissioning and handoff-safe knowledge lineage |

Do not activate those legacy labels as standalone plan authority.
Use them only to locate packet-era source material while executing the release stages below.
Use `canon-ref:dev/kb/identity/canon-canon-registry` to normalize those legacy packet labels against the current local workflow language when needed.

## Stage Plan

### Platform Gate

Architecture goal: prove the substrate is real enough that every public release can inherit knowledge participation without pretending transcript continuity is truth.

Knowledgebase obligations at this stage:

- memory and canon injection are real engine seams with authoritative refs and frozen replay basis behavior
- append-only knowledge observation, proposal, decision, and state-transition events are real shared-environment substrate
- proposal, review, approval, and apply paths for memory and canon are executable on real paths, even if still internal-facing
- passive capture starts as scoped observation intake and proposal substrate, not as user-facing autonomous memory magic
- operator and audit surfaces can show what knowledge participated in a run and why it was admitted or blocked

Package-maturity posture that matters most here:

- all package areas must already be real at `M1`
- `pkg.context-compiler`, `pkg.shared-object-api`, `pkg.event-provenance-spine`, and `pkg.review-writeback` must be real enough that later stages inherit them instead of debating their existence

Intentional deferrals and refusals:

- no public learning product promise yet
- no transcript-private memory behavior
- no branch, artifact, prompt, applet, or commissioning semantics smuggled in early
- no silent background promotion of candidate learning

Exit signal:

`R1` can honestly expose bounded runs with explicit knowledge participation because the substrate beneath that story is already real.

### R1 Transcript Chat

User promise: this still feels familiar, but each answer is a bounded run with explicit grounding rather than transcript-owned truth.

Knowledgebase obligations at this stage:

- disclose when memory or canon participated in a run
- preserve compact visibility into included and excluded knowledge basis records
- keep candidate learning internal or visibly marked as suggestion-only rather than injecting it by default
- keep early reviewer and operator surfaces honest even if full governance UX is not yet public-facing

Package-maturity posture that matters most here:

- `pkg.environment-control` -> `M3`
- `pkg.context-compiler` -> `M3`
- `pkg.shared-object-api`, `pkg.model-gateway`, `pkg.event-provenance-spine`, and `pkg.monitor-inspect` -> `M2`

Intentional deferrals and refusals:

- not full context editing
- not artifact-centered continuity
- not hidden memory accumulation
- not governed reusable execution

Exit signal:

Users can see that knowledge participation is real and explicit, while the product still avoids pretending that `R1` offers full memory governance.

### R2 Context Chat

User promise: context control becomes explicit and replayable instead of being tucked behind invisible defaults.

Knowledgebase obligations at this stage:

- include, exclude, pin, and challenge controls operate over active memory and canon participation
- the system can show why a memory or canon record was included, excluded, blocked, previewed, or constrained
- user corrections can open proposal-bearing flows without collapsing directly into accepted truth
- passive capture and early distillation stay proposal-first and visibly scoped

Package-maturity posture that matters most here:

- `pkg.context-compiler` -> `M4`
- `pkg.shared-object-api` -> `M3`
- `pkg.event-provenance-spine` -> `M3`
- `pkg.monitor-inspect` -> `M3`
- `pkg.replay-compare` -> `M2`

Intentional deferrals and refusals:

- not branch-map semantics yet
- not artifact-governance center of gravity yet
- not fake context control that only edits sidebars while hidden defaults continue elsewhere

Exit signal:

`R2` can expose real pack control over knowledge participation without widening into fake branching or early artifact governance.

### R3 Branch / Visual Thinker

User promise: branches, replay, compare, and mode projections can vary assumptions without breaking run truth.

Knowledgebase obligations at this stage:

- exact replay reuses frozen knowledge refs from the original basis
- altered replay and compare report explicit knowledge-basis diffs instead of silently rerunning mutable discovery
- suspensions, supersessions, and branch-local differences stay queryable and explainable
- merge and conflict surfaces treat knowledge disagreements as governed state, not transcript drift

Package-maturity posture that matters most here:

- `pkg.event-provenance-spine` -> `M4`
- `pkg.replay-compare` -> `M4`
- `pkg.review-writeback` -> `M2`

Intentional deferrals and refusals:

- not artifact review center yet
- not prompt or applet infrastructure milestone
- not transcript cloning presented as branching

Exit signal:

Canon can distinguish same-basis replay from changed-basis replay without hand-waving over knowledge lineage.

### R4 Artifact Workspace

User promise: continuity shifts from transcript gravity to artifacts, proposals, reviews, approvals, and durable run-linked work.

Knowledgebase obligations at this stage:

- artifact-linked knowledge proposals become the main durable promotion path
- objections, alternatives, suspensions, and supersessions stay first-class shared-environment governance records
- accepted memory and canon remain tied back to run, proof, delta, artifact, and approval lineage
- artifact-centered continuity inherits the same knowledgebase rather than inventing a new truth model

Package-maturity posture that matters most here:

- `pkg.shared-object-api` -> `M4`
- `pkg.review-writeback` -> `M4`

Intentional deferrals and refusals:

- not prompt-governance or reusable-execution milestone yet
- not silent artifact mutation
- not artifact-centered replacement of run truth

Exit signal:

`R4` becomes the bridge out of transcript gravity while preserving one governed knowledgebase and one proposal-first continuity model.

### R5 Prompt Studio

User promise: prompt artifacts and model adaptations become governed reusable assets with lineage.

Knowledgebase obligations at this stage:

- prompt assets read shared memory and canon through explicit lineage-bearing references
- staleness and dependency behavior are visible when accepted knowledge changes
- model-profile and adaptation behavior stays part of governed substrate rather than hidden provider lore
- prompt assets do not become a second memory store

Package-maturity posture that matters most here:

- `pkg.model-gateway` -> `M4`

Intentional deferrals and refusals:

- not governed applet execution yet
- not prompt-side shadow canon
- not prompt cards acting as substitutes for protocol or applet semantics

Exit signal:

Prompt artifacts can consume shared knowledge truth without replacing it or creating private prompt memory.

### R6 Governed Agent / Applet Chat

User promise: reusable execution can operate under explicit policy, verifier, and authority constraints instead of theater about autonomous agents.

Knowledgebase obligations at this stage:

- reusable execution receives explicit memory policy, contradiction guards, verifier packs, and queue routing
- background or triggered work may observe and propose knowledge changes, but may not silently apply them
- applets and workflows stay on shared truth and shared governance rather than inventing a private learning ontology

Package-maturity posture that matters most here:

- `pkg.tool-gateway-sandbox` -> `M4`

Intentional deferrals and refusals:

- not commissioning bridge yet
- not hidden autonomy widening
- not applet-private memory semantics

Exit signal:

Canon can safely let governed reusable execution participate in learning while preserving proposal-first mutation and shared truth ownership.

### R7 Commissioning Bridge

User promise: serious consequential work becomes explicit commissioning with authority, proof, delta, writeback, and handoff-grade continuity.

Knowledgebase obligations at this stage:

- preflight shows which memory and canon refs matter, under what authority they were accepted, and what review lineage governs them
- commissioned work preserves knowledge participation through proof ledger, delta inspection, and writeback review surfaces
- handoff payloads carry shared refs and authority lineage directly so Task Studio inherits meaning without ontology translation
- commissioning stays explicit enough that this remains the final chat-native bridge rather than a chat-private branch of the platform

Package-maturity posture that matters most here:

- `pkg.environment-control` -> `M4`
- `pkg.monitor-inspect` -> `M4`

Intentional deferrals and refusals:

- not a Task Studio rewrite
- not chat-private commissioning semantics
- not skipped preflight, authority review, or writeback lineage

Exit signal:

By `R7`, Canon can hand knowledge-bearing commissioned work into Task Studio as a projection change rather than a substrate rewrite.

## Cross-Stage Guardrails

These remain active across every milestone in this plan.

1. No master chat truth.
2. No hidden memory sludge.
3. No silent proposal application.
4. No engine-owned durable workspace memory store.
5. No index-as-truth shortcut.
6. No secrets in memory or canon lanes.
7. No prompt, applet, or commissioning-private competing truth layer.
8. No replay claim unless frozen refs and basis reporting are explicit.

## Immediate Next Checkpoint

Execution has completed the sync, the `PG-1` checkpoint, the `PG-2` knowledge participation basis slice, the `PG-3` authoritative knowledge-lane ref passthrough slice, the `PG-4` knowledge-lane admission projection seam, the `PG-5` memory-before-canon compiler staging slice, the `PG-6` legacy knowledge-lane fallback isolation slice, the bounded post-evidence compiler stage-order correction locally, the first post-reopen lane-authority implementation slice locally, the second post-reopen ref-first host-projection consumption slice locally, the third post-reopen accepted-knowledge lane metadata passthrough slice locally, and the frozen-posture replay/audit sufficiency checkpoint locally.

There is no active bounded local checkpoint after that closure.

The later local Phase 6 entry and packet continuation chain is preserved as historical evidence of a 2026-04-18 inference error from pre-existing Phase 6 modeling docs, not as live next-step authority. Accepted Canon authority now states that same boundary explicitly, so no residual source-level conflict remains open here.

The next concrete move is:

1. recover from the refreshed local authority state and confirm the frozen-posture replay/audit sufficiency closure still matches published Canon authority
2. stop unless a later higher-authority Canon checkpoint or a specific contradiction names one new bounded recoverable step, or the user explicitly chooses a different bounded task
3. do not treat accepted Phase 6 future-layout modeling or the local draft `Canon/packages/`, `Canon/services/`, and `Canon/workers/` roots as default authorization to resume implementation
4. do not reopen replay, diff, compact event redesign, broader lifecycle retirement, or a generalized multi-lane schema rewrite locally without that authority
5. keep published remote `main` state distinct from any historically non-authoritative local workspace checkouts while evaluating any future reopen signal

## Historical Boundary

The rollout file remains valuable, but only as migration support.

- `canon-ref:dev/kb/canon-knowledgebase-layer-rollout-plan` is now historical scaffolding, not active plan authority
- `P00-P05` remain durable convergence inputs, not active execution packets
- `P06-P13` remain useful migration labels, not standalone active planning packets
- Wiki remains historical prior art only
