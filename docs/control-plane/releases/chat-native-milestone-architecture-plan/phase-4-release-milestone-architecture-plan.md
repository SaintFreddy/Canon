# Phase 4 release / milestone architecture plan
Version: 1.0
Status: Accepted
Task: P4.2 — Release / milestone architecture plan
Artifact ID: rel.chat-native-milestone-architecture-plan.v1
Release ID: chat-native-milestone-architecture-plan
Release scope: Accepted human-owned milestone architecture plan covering what each stage exposes, what is deferred, and what overbuilding is intentionally refused

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This plan was accepted as P4.2 following the completed P3.6 architecture
synchronization pass (`arch.phase3-architecture-sync-pass.v1`), which
confirmed no substrate drift before Phase 4 release-contract work began.

As of Phase 4+ convergence:

- P4.3-P4.9 (R1-R7 contract packs) are accepted and downstream of this plan.
- Phase 5 semantics packs (P5.1-P5.7) have absorbed the reusable-execution
  and commissioning seams named in §5.4-§5.5 and §8.
- Phase 6 implementation packets (P6.1-P6.6) have mapped §6 package-maturity
  postures to concrete execution packets.
- Phase 7 automation (P7.1-P7.4) now enforces the anti-drift locks this plan
  established.

This plan remains the milestone architecture authority. Sections below are
kept verbatim as the accepted human-owned record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This plan turns the accepted release topology, Platform Gate, and package-maturity matrix into one milestone architecture story.

It exists to:

- state what each stage is allowed to expose,
- name what each stage must deliberately defer,
- prevent later release packs from overbuilding ahead of the fixed path.

## 2. Planning rules

### 2.1 Inherit accepted substrate rule

This plan inherits the accepted P3.1-P3.6 architecture baseline and the accepted P4.1 maturity matrix.
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

## 4. Stage inheritance and protected seams

| Stage | Continuity center foregrounded here | Protected seams / scenarios that this stage must inherit | Package-maturity posture already fixed before the stage contract is written | Why the next contract pack must stay narrow |
| --- | --- | --- | --- | --- |
| Platform Gate | Frozen context + source/run/provenance identity | `SS-01`, `SS-02`, `SS-10`, `GS-03`, `EC-10` | All package areas must already be real at `M1` | Keeps later public releases from debating whether the substrate exists |
| R1 | Thread-assisted run continuity | `SS-01`, `SS-02`, `GS-01` | `pkg.environment-control` and `pkg.context-compiler` are already forced to `M3`; `pkg.shared-object-api`, `pkg.model-gateway`, `pkg.event-provenance-spine`, and `pkg.monitor-inspect` are already forced to `M2` | Keeps R1 limited to bounded familiar chat instead of leaking later-stage context or artifact claims |
| R2 | Run continuity with explicit pack control | `SS-01`, `GS-02`, `GS-03` | `pkg.context-compiler` is already forced to `M4`; `pkg.shared-object-api` is already forced to `M3`; `pkg.replay-compare` is already forced to `M2` | Keeps R2 focused on real evidence/context control rather than early branching or artifact governance |
| R3 | Branch/replay continuity around checkpoints | `SS-07`, `SS-11`, `GS-04`, `GS-05`, `EC-01`, `EC-09` | `pkg.event-provenance-spine` and `pkg.replay-compare` are already forced to `M4`; `pkg.review-writeback` is already forced to `M2` | Keeps semantic branching separate from artifact review and prevents mode-private backends |
| R4 | Artifact-centered continuity over run history | `SS-02`, `SS-03`, `SS-04`, `GS-06`, `GS-07`, `EC-03` | `pkg.shared-object-api` and `pkg.review-writeback` are already forced to `M4` | Protects the bridge out of transcript gravity and keeps proposal/writeback governance explicit |
| R5 | Prompt artifact lineage continuity | `SS-13`, `GS-08`, `GS-09`, `EC-04` | `pkg.model-gateway` is already forced to `M4` | Keeps prompt assets governed and lineage-bearing without spending Protocol/Applet semantics early |
| R6 | Reusable execution continuity through Protocol/Applet/Workflow objects | `SS-08`, `SS-12`, `GS-10`, `GS-11`, `EC-05` | `pkg.tool-gateway-sandbox` is already forced to `M4` and all earlier bridge-stage floors remain inherited | Keeps governed reuse real while refusing hidden autonomy widening or second-stack drift |
| R7 | Commission/Contract continuity into explicit run governance and Task Studio handoff | `SS-04`, `SS-05`, `SS-09`, `GS-12`, `GS-13`, `GS-14`, `EC-06` | `pkg.environment-control` and `pkg.monitor-inspect` are already forced to `M4` and all earlier carry-forward floors remain inherited | Keeps commissioning explicit enough that Task Studio can be a projection change rather than a rewrite |

## 5. Milestone boundary notes

### 5.1 Platform Gate

- Architecture goal: prove the substrate is real enough that later release contracts can talk about user-visible scope instead of existential runtime gaps.
- Consequence: nothing public may bypass it.

### 5.2 R1 and R2

- R1 proves familiarity without transcript truth.
- R2 proves context control without pretending branching or artifacts already anchor continuity.

### 5.3 R3 and R4

- R3 is the semantic-branch bridge.
- R4 is the artifact-continuity bridge.
- These must stay distinct so branching does not collapse into artifact review and artifacts do not swallow replay semantics.

### 5.4 R5 and R6

- R5 hardens governed prompt assets as lineage-bearing artifacts.
- R6 hardens governed reusable execution as Protocol/Applet/Workflow reality.
- R5 must not pre-spend applet semantics, and R6 must not treat prompt assets as execution ontology.

### 5.5 R7

- R7 is the last chat-native milestone because it must expose explicit commissioning rather than more chat convenience layers.
- Architecture should treat R7 as the handoff-grade release, not as “chat plus a little more governance.”

## 6. Package-maturity posture by milestone

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

## 7. Planned non-goals by milestone

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

## 8. Downstream contract-pack handoff

> All P4.3-P4.9 contract packs listed below are accepted. This table remains
> the inheritance record; the accepted packs are the downstream proof.

| Contract pack (all accepted) | Must inherit from this milestone plan | Must not reopen |
| --- | --- | --- |
| `P4.3` — R1 Transcript Chat contract pack | Platform Gate as the mandatory substrate proof plus the R1 bounded-run/chat familiarity boundary | Full context editing, branching, artifact-centered continuity, or transcript-truth shortcuts |
| `P4.4` — R2 Context Chat contract pack | R1 bounded-run continuity plus the R2 requirement that evidence/context control becomes explicit and replayable | Branch-map semantics, artifact governance, or fake sidebar-only context control |
| `P4.5` — R3 Branch / Visual Thinker contract pack | R2 pack-control reality plus R3 semantic branch/replay continuity and mode-projection rules | Artifact workspace governance, transcript cloning presented as branching, or mode-private backends |
| `P4.6` — R4 Artifact Workspace contract pack | R3 branch/replay substrate plus the R4 artifact-centered continuity and lane-separated proposal/review bridge | Silent artifact mutation, artifact-centered rewrites of run truth, or reopening lane separation |
| `P4.7` — R5 Prompt Studio contract pack | R4 governed artifact lineage plus the R5 rule that prompt assets are governed artifacts backed by `pkg.model-gateway` maturity | Treating prompt cards as Protocol/Applet substitutes or hiding model adaptation lore off-substrate |
| `P4.8` — R6 Governed Agent / Applet Chat contract pack | R5 prompt-asset boundaries plus the R6 rule that reusable execution stays composed from shared run semantics with governed background runs | Agent theater, hidden autonomy widening, or a second execution ontology |
| `P4.9` — R7 Commissioning Bridge contract pack | R6 governed reuse plus the R7 requirement for explicit commission/contract/authority/proof/delta/writeback objects and Task Studio-safe handoff | Chat-private commissioning semantics, skipped preflight/authority review, or lane-collapsing writeback convenience |

## 9. Guidance for later release packs

1. Each R1-R7 pack should cite this milestone plan plus the accepted maturity matrix.
2. Each release contract should include an explicit “what this stage refuses to overbuild” section.
3. If a later pack appears to need a capability from a future bridge stage, that should be treated as an architecture review issue rather than solved by sneaking the capability earlier.

## 10. Accepted milestone decisions

1. The milestone boundaries above match the intended release doctrine interpretation.
2. The deferrals and non-goals are strict enough to stop overbuilding.
3. R4 and R7 remain the only semantic bridge releases in the public path.

## 11. Downstream implications

- P4.2 closes with one accepted milestone architecture story.
- P4.3-P4.9 have each become a narrower release contract. *(Resolved - all accepted.)*
- Phase 6 package planning has mapped concrete modules and services to the
  already-agreed milestone maturity posture. *(Resolved - P6.2 repo/package
  execution baseline accepted.)*

## 12. Acceptance notes

- This accepted artifact remains a milestone architecture plan rather than an implementation blueprint.
- This accepted artifact keeps deferrals intentional and explicit.
- This accepted artifact preserves the fixed chat-native path and its bridge releases for downstream release packs.
