# Phase 4 R3 Branch / Visual Thinker contract pack
Version: 1.0
Status: Accepted
Task: P4.5 — R3 Branch / Visual Thinker contract pack
Artifact ID: rel.r3-branch-visual-thinker-contract.v1
Release ID: r3-branch-visual-thinker-contract
Release scope: Accepted R3 contract pack covering semantic branch/replay continuity, mode projections, off-chain jobs, merge proposals, inherited package floors, exit criteria, and explicit non-goals

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This contract pack was accepted as P4.5 under the accepted Phase 4 milestone
architecture plan (`rel.chat-native-milestone-architecture-plan.v1`) and the
accepted release-to-SDK maturity matrix
(`rel.chat-native-maturity-matrix.v1`).

As of Phase 4+ convergence:

- P4.4 remains the accepted upstream contract for explicit pack control,
  freeze/diff lineage, and inspectable memory/canon participation that R3
  inherits rather than replaces.
- P4.6 (R4 Artifact Workspace) is accepted as the direct downstream
  inheritance of the R3 handoff described in §5.
- Phase 6 package planning has mapped the R3 `M4`/`M3`/`M2` maturity floor in
  §4.4 to concrete execution packets without inventing an R3-private backend.
- Later accepted release packs inherit the R3 locks on semantic branch truth,
  explicit merge proposals, and proof/delta-aware replay rather than reopening
  transcript-clone shortcuts.

This pack remains the accepted R3 contract authority. Sections below are kept
verbatim as the accepted human-owned contract record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R3 Branch / Visual Thinker.

It exists to:

- define what semantic branching and replay must mean for the third public release,
- make branch/checkpoint/proof/delta continuity explicit before artifact-centered work becomes primary,
- lock the package-maturity floor, exit criteria, and anti-theater constraints for the R3 boundary.

## 2. Scope boundaries

### In scope

- the R3 user-facing product promise,
- the R3 branch/replay continuity center and shared primitives,
- the R3 projection-only additions for fork policies, mode projections, off-chain jobs, and merge proposals,
- the R3 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R3 exit criteria and explicit non-goals.

### Out of scope

- artifact-centered continuity as the primary visible center,
- proposal inbox and review/approval loops as the main user-facing bridge,
- prompt-asset governance,
- reusable Protocol/Applet execution packaging,
- commissioning preflight and Task Studio handoff depth,
- transcript cloning presented as semantic branch behavior.

## 3. Inherited stage rules

### 3.1 R2 pack-control substrate remains binding

R3 inherits the accepted Platform Gate baseline, the accepted R1 Transcript Chat contract, and the accepted R2 Context Chat contract.
R3 may deepen into branching and replay, but it may not replace bounded runs, frozen pack lineage, or explicit evidence/context inspection with transcript-local shortcuts.

### 3.2 Semantic-branch-not-transcript-clone rule

R3 branches fork semantic state from explicit checkpoints, packs, strategy inputs, assumptions, or outputs.
Transcript duplication alone is never sufficient branch identity, replay basis, or compare truth.

### 3.3 Mode-projection-and-explicit-merge rule

Mode switches remain projections over the same branch/object graph.
Off-chain jobs, branch merges, or consensus views may summarize or compare state, but they must return through explicit Runs, Proof Bundles, State Deltas, and Merge Proposals rather than silently collapsing lineage.

## 4. R3 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | The user can branch assumptions, packs, strategy, model choice, and execution mode through real branch/replay/compare flows rather than transcript clones |
| Continuity center | Branch/replay continuity around runs and checkpoints |
| Shared primitives foregrounded | Run, Branch, Checkpoint, Evidence Pack, Context Pack, Proof Bundle, State Delta |
| Projection-only additions | Fork Policy, Mode Projection, Off-chain Job, Merge Proposal, Consensus Branch, Branch Overlay |
| Protected seams and scenarios | `SS-07`, `SS-11`, `GS-04`, `GS-05`, `EC-01`, `EC-09`, plus Platform Gate tests `PG-01` and `PG-04` as inherited blockers |
| Handoff obligation | R3 -> R4 preserves run outputs, branch lineage, artifact proposals, and proof/delta identity so accepted artifacts can become the next visible continuity anchor |

### 4.2 Shared-object contract

| Object family | R3 contract |
| --- | --- |
| Run | Replay, compare, and branch exploration still resolve through distinct Runs rather than mutating prior run truth in place |
| Branch | Every alternate line has stable branch identity, parentage, continuity anchors, overlay state, and explicit merge/abandon/freeze posture |
| Checkpoint | Branching and replay anchor on explicit append-only checkpoints instead of transcript history or UI-local snapshots |
| Evidence Pack | Branches may narrow or widen evidence only through explicit pack lineage and basis diffs |
| Context Pack | Each replay or branch carries a frozen or explicitly diffed admitted basis rather than hidden prompt recomputation |
| Proof Bundle | Compare and mode surfaces must preserve task-shaped proof, omissions, contradictions, and uncertainty rather than relying on visual diff alone |
| State Delta | Off-chain jobs, replay outcomes, and merge candidates emit explicit delta-bearing state that later review surfaces can inherit |

### 4.3 Projection-only additions

| R3 addition | Contract |
| --- | --- |
| Fork Policy | Declares additive, subtractive, masked, frozen, live, model-swap, tool-swap, or off-chain branch posture without redefining the underlying Branch object |
| Mode Projection | Provides notebook, debate, research, architect, executive-summary, or graph views over the same branch/object graph |
| Off-chain Job | Runs detached exploration or research work that returns through explicit new Run/Proof/Delta records and merge proposals |
| Merge Proposal | Surfaces branch-to-branch or off-chain-to-parent reconciliation as an explicit proposal rather than silent branch collapse |
| Consensus Branch | Summarizes converged findings across branches without replacing source branch lineage or proposal history |
| Branch Overlay | Exposes branch-local pack, strategy, assumption, or output differences over a parent continuity line |

### 4.4 Package-maturity floor

| Package area | Required floor in R3 | Why R3 depends on it |
| --- | --- | --- |
| `pkg.replay-compare` | `M4` | R3 makes checkpoint capture, replay execution, basis diffing, and compare handling a carry-forward substrate seam rather than optional UX |
| `pkg.event-provenance-spine` | `M4` | Semantic branch lineage, replay history, off-chain returns, and merge proposals must remain append-only and reconstructable |
| `pkg.review-writeback` | `M2` | Merge proposals and proposal-bearing branch returns need explicit reviewable state before R4 deepens artifact governance |
| `pkg.context-compiler` | `M4` | Branching depends on inherited frozen pack lineage, explicit basis diffs, and replayable admitted context |
| `pkg.shared-object-api` | `M3` | R3 needs stable refs for runs, branches, checkpoints, packs, proof, and deltas across compare and mode surfaces |
| `pkg.monitor-inspect` | `M3` | R3 compare, timeline, and replay inspection surfaces must project authoritative branch/checkpoint/proof state rather than stage-local guesses |

Inherited and still required in R3:

- `pkg.environment-control` remains at `M3`,
- `pkg.model-gateway` remains at `M2`,
- `pkg.tool-gateway-sandbox` remains at `M1`.

R3 must not overclaim capabilities that belong to the later artifact, prompt, reusable-execution, or commissioning bridge stages.

### 4.5 Exit criteria

R3 is contract-complete only when all of the following are true:

1. A user can fork a branch from an explicit checkpoint or prior run basis without duplicating transcript history as the truth anchor.
2. Exact replay produces a new Run from frozen pack lineage and checkpoint state without relying on provider transcript continuity.
3. Pack, strategy, model-choice, or output differences across branches surface as explicit basis diffs and compare targets rather than hidden recomputation.
4. Mode switches preserve the same branch/object identities and do not create mode-private backends or duplicate truth objects.
5. Off-chain jobs return through explicit Run, Proof Bundle, State Delta, and Merge Proposal records rather than silently merging into the parent branch.
6. Compare and replay surfaces can inspect proof, omissions, contradictions, and delta state alongside output differences.

### 4.6 Explicit non-goals and refusals

R3 deliberately refuses to overbuild any of the following:

- transcript cloning presented as branching,
- mode-private backends or mode-local truth models,
- artifact workspace governance as the primary visible center,
- prompt-asset or reusable-execution packaging as an R3 milestone,
- silent off-chain merge or hidden branch collapse,
- branch UX that lacks proof, delta, or basis-diff awareness.

## 5. Downstream handoff to R4

R4 may shift visible continuity toward focal artifacts and proposal inbox review, but it must inherit the R3 branch substrate rather than replace it.

> P4.6 is now accepted as the direct downstream realization of this handoff.
> The locks below remain the R3 -> R4 inheritance record.

The R3 contract therefore carries forward these locks:

- branch and replay already operate on real checkpoints and pack lineage before artifacts become the visible continuity anchor,
- merge proposals already exist as explicit proposal-bearing state before artifact review deepens into lane-local governance,
- proof and delta identity survive branch exploration so later artifact proposals can trace back to the runs and branches that produced them,
- mode projections remain view-level compositions and must not leak into artifact ontology or durable truth.

## 6. Downstream implications

- P4.6 has narrowed into artifact-centered continuity and proposal/review
  behavior rather than rediscovering whether branch lineage, replay basis, and
  explicit proposals are already real. *(Resolved - P4.6 accepted on inherited
  R3 branch substrate.)*
- Later releases treat R3 as the proof that semantic branching is a
  shared-substrate capability rather than a fancy transcript UI. *(Resolved -
  inherited across accepted P4.7-P4.9 release packs.)*
- Phase 6 package planning has mapped R3 UI and service work onto the
  `M4`/`M3`/`M2` floors above rather than inventing an R3-private backend.
  *(Resolved - Phase 6 repo/package execution baseline accepted.)*

## 7. Acceptance notes

- This accepted artifact defines the R3 boundary, not the whole release doctrine.
- This accepted artifact keeps R3 intentionally focused on semantic branch/replay continuity so later artifact, prompt, reusable-execution, and commissioning stages can inherit one substrate story without rewrite drift.
