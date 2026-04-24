# Canon Phase 4+ Plan — Stage Plan

## Purpose

This file preserves the full release-stage authority (Platform Gate + `R1`..`R7`) that was originally inline inside `canon-ref:dev/kb/canon-phase-4-plus-plan`.

The active plan file keeps only a compact pointer to this file on its hot recovery surface. Open this file only when a plan-owner-selected release stage becomes the active bounded step.

This file is forward-looking authority, not historical scaffolding. It defines what each release stage must honestly demonstrate for the knowledgebase architecture to inherit correctly. It is declared in the active plan's `preserves_as_stage_authority` list.

## Scope

One subsection per stage, in release order:

- Platform Gate
- `R1` Transcript Chat
- `R2` Context Chat
- `R3` Branch / Visual Thinker
- `R4` Artifact Workspace
- `R5` Prompt Studio
- `R6` Governed Agent / Applet Chat
- `R7` Commissioning Bridge

Every stage uses the same four-field shape:

- **Architecture or user promise** — what the release honestly communicates
- **Knowledgebase obligations at this stage** — what the substrate must support
- **Package-maturity posture that matters most here** — which maturity levels must be real
- **Intentional deferrals and refusals** — what this stage specifically does not claim
- **Exit signal** — the test that the stage has done enough

## Cross-Stage Guardrails reference

The authoritative `Cross-Stage Guardrails` block remains in `canon-ref:dev/kb/canon-phase-4-plus-plan` because it applies across every stage below. Read both files together whenever a stage section is active.

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
