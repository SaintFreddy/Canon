# Phase 4 release / milestone architecture plan
Version: 0.1
Status: Review Ready
Task: P4.2 — Release / milestone architecture plan
Artifact ID: rel.chat-native-milestone-architecture-plan.v1
Release ID: chat-native-milestone-architecture-plan
Release scope: Review-ready human-only milestone architecture plan covering what each stage exposes, what is deferred, and what overbuilding is intentionally refused

This file is drafting support for a human-only task.
It is not accepted repo truth and is intentionally not registered in the accepted artifact datasets yet.

## 1. Purpose

This plan turns the accepted release topology, Platform Gate, and package-maturity matrix into one milestone architecture story.

It exists to:

- state what each stage is allowed to expose,
- name what each stage must deliberately defer,
- prevent later release packs from overbuilding ahead of the fixed path.

## 2. Planning rules

### 2.1 Inherit accepted substrate rule

This plan inherits the accepted P3.1-P3.5 architecture baseline and the accepted P4.1 maturity matrix.
It does not reopen substrate meaning that Platform Gate already fixed.

### 2.2 Stage-focus-not-totality rule

Each milestone foregrounds one continuity center or capability shift.
It does not attempt to expose every future surface or every mature package seam at once.

### 2.3 Defer-on-purpose rule

Deferral is architectural discipline, not missing work.
If a capability belongs to a later bridge stage, earlier milestones should refuse to fake it.

### 2.4 No-overbuild rule

When a later stage owns a semantic seam, earlier stages must not pre-spend that seam through hidden backend complexity, UI theater, or stage-private object models.

## 3. Milestone architecture summary

| Stage | What is intentionally exposed | What is intentionally deferred | What is intentionally refused |
| --- | --- | --- | --- |
| Platform Gate | Internal gate surfaces, audit evidence, replay/source/provenance checks, monitor/console support | Public release UX, polished release-specific flows, stage-specific product promises | Any claim that chat-native release work may proceed without proving the substrate |
| R1 Transcript Chat | Familiar conversation entry, bounded run execution, compact source/run inspection, thread-assisted continuity | Full context editing, semantic branching, artifact-centered continuity, governed reuse, commissioning | Transcript-as-truth behavior, hidden provider continuity, fake “simple chat” backend shortcuts |
| R2 Context Chat | Explicit evidence/context inspection, inclusion/exclusion visibility, freeze/diff/replay controls | Branch map semantics, artifact workspace, reusable execution packaging, commissioning bridge | Sidebar-only “context theater” without real pack control |
| R3 Branch / Visual Thinker | Semantic branch/replay/compare work, mode projections over shared branch state, checkpoint-centered exploration | Artifact-centered continuity, prompt asset governance, applet packaging, commissioning UI | Transcript cloning presented as branching, mode-private backends |
| R4 Artifact Workspace | Artifact-centered continuity, proposal inbox, review/approval loop, historical truth per run | Prompt asset specialization, governed reusable execution, commissioning preflight | Silent artifact mutation, treating artifacts as replacements for runs |
| R5 Prompt Studio | Prompt assets as governed artifacts, model-profile/adaptation lineage, reusable prompt inputs | Applet/workflow execution UX, background-run governance, commissioning bridge | Prompt cards as substitutes for Protocol/Applet semantics or hidden provider lore |
| R6 Governed Agent / Applet Chat | Protocol/Applet/Workflow/Trigger surfaces, bounded background runs, queue/inbox governance, tool execution hardening | Explicit commissioning/contract preflight as the primary interaction loop, Task Studio handoff | Agent theater, hidden autonomy widening, second-stack orchestration drift |
| R7 Commissioning Bridge | Commission/Contract preflight, live monitor, proof ledger, delta/writeback inspection, chat-to-run handoff | Task Studio-only surface depth, full reusable semantics deepening from Phase 5 | Treating chat commissioning as a private ontology or skipping explicit authority/proof/writeback objects |

## 4. Milestone boundary notes

### 4.1 Platform Gate

- Architecture goal: prove the substrate is real enough that later release contracts can talk about user-visible scope instead of existential runtime gaps.
- Consequence: nothing public may bypass it.

### 4.2 R1 and R2

- R1 proves familiarity without transcript truth.
- R2 proves context control without pretending branching or artifacts already anchor continuity.

### 4.3 R3 and R4

- R3 is the semantic-branch bridge.
- R4 is the artifact-continuity bridge.
- These must stay distinct so branching does not collapse into artifact review and artifacts do not swallow replay semantics.

### 4.4 R5 and R6

- R5 hardens governed prompt assets as lineage-bearing artifacts.
- R6 hardens governed reusable execution as Protocol/Applet/Workflow reality.
- R5 must not pre-spend applet semantics, and R6 must not treat prompt assets as execution ontology.

### 4.5 R7

- R7 is the last chat-native milestone because it must expose explicit commissioning rather than more chat convenience layers.
- Architecture should treat R7 as the handoff-grade release, not as “chat plus a little more governance.”

## 5. Package-maturity posture by milestone

| Stage | Package areas that are newly central to the milestone architecture |
| --- | --- |
| Platform Gate | All `M1` package areas from `rel.chat-native-maturity-matrix.v1` |
| R1 | `pkg.environment-control`, `pkg.context-compiler`, plus compact `pkg.shared-object-api`, `pkg.event-provenance-spine`, `pkg.monitor-inspect`, and `pkg.model-gateway` visibility |
| R2 | `pkg.context-compiler`, `pkg.shared-object-api`, `pkg.event-provenance-spine`, `pkg.monitor-inspect`, and entry-level `pkg.replay-compare` |
| R3 | `pkg.replay-compare` and `pkg.event-provenance-spine` as carry-forward branch substrate, with proposal-bearing `pkg.review-writeback` entry |
| R4 | `pkg.shared-object-api` and `pkg.review-writeback` as carry-forward artifact/governance bridge seams |
| R5 | `pkg.model-gateway` as governed substrate rather than hidden adaptation lore |
| R6 | `pkg.tool-gateway-sandbox` as the reusable-execution hardening seam |
| R7 | `pkg.environment-control` and `pkg.monitor-inspect` at commissioning-grade maturity |

## 6. Planned non-goals by milestone

| Stage | Non-goals that should remain explicit |
| --- | --- |
| Platform Gate | Not a public release substitute; not a UX milestone |
| R1 | Not full context control; not artifact workspace; not reusable agents |
| R2 | Not branch map; not artifact-centered continuity; not hidden memory magic |
| R3 | Not artifact review center; not prompt/app infrastructure milestone |
| R4 | Not prompt-governance or reusable execution milestone |
| R5 | Not applet/governed-autonomy milestone |
| R6 | Not commissioning bridge; not Task Studio handoff completion |
| R7 | Not Task Studio rewrite; not Phase 5 proof/governance deepening completion |

## 7. Draft guidance for later release packs

1. Each R1-R7 pack should cite this milestone plan plus the accepted maturity matrix.
2. Each release contract should include an explicit “what this stage refuses to overbuild” section.
3. If a later pack appears to need a capability from a future bridge stage, that should be treated as an architecture review issue rather than solved by sneaking the capability earlier.

## 8. Human review decisions still required

1. Confirm that the milestone boundaries above match the intended release doctrine interpretation.
2. Confirm that the deferrals and non-goals are strict enough to stop overbuilding.
3. Confirm that R4 and R7 remain the only semantic bridge releases in the public path.

## 9. Draft recommendation for downstream work

If human review agrees with this plan:

- P4.2 can close with one accepted milestone architecture story,
- P4.3-P4.9 can each become a narrower release contract rather than reopening stage ordering,
- Phase 6 package planning can map concrete modules/services to already-agreed milestone maturity.

## 10. Review notes

Human review should confirm that this draft:

- is a milestone architecture plan rather than a disguised implementation blueprint,
- keeps deferrals intentional and explicit,
- preserves the fixed chat-native path and its bridge releases,
- is suitable to promote or revise as the formal P4.2 result.
