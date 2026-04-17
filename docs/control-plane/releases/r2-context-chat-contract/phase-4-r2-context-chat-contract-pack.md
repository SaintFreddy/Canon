# Phase 4 R2 Context Chat contract pack
Version: 1.0
Status: Accepted
Task: P4.4 — R2 Context Chat contract pack
Artifact ID: rel.r2-context-chat-contract.v1
Release ID: r2-context-chat-contract
Release scope: Accepted R2 contract pack covering explicit evidence/context control, pack operations, inherited package floors, exit criteria, and explicit non-goals

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This contract pack was accepted as P4.4 under the accepted Phase 4 milestone
architecture plan (`rel.chat-native-milestone-architecture-plan.v1`) and the
accepted release-to-SDK maturity matrix
(`rel.chat-native-maturity-matrix.v1`).

As of Phase 4+ convergence:

- P4.3 remains the accepted upstream contract for bounded runs,
  source-bearing identity, and transcript-as-truth refusal boundaries that R2
  inherits rather than replaces.
- P4.5 (R3 Branch / Visual Thinker) is accepted as the direct downstream
  inheritance of the R2 handoff described in §5.
- Phase 6 package planning has mapped the R2 `M4`/`M3`/`M2` maturity floor in
  §4.4 to concrete execution packets without inventing an R2-private pack
  backend.
- Later accepted release packs inherit the R2 locks on explicit pack control,
  freeze/diff lineage, and inspectable memory/canon participation rather than
  reopening hidden-context shortcuts.

This pack remains the accepted R2 contract authority. Sections below are kept
verbatim as the accepted human-owned contract record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R2 Context Chat.

It exists to:

- define what “real context control” means for the second public release,
- make the Evidence Pack / Context Pack / Memory / Canon surface contract explicit,
- lock the package-maturity floor, exit criteria, and anti-theater constraints for the R2 boundary.

## 2. Scope boundaries

### In scope

- the R2 user-facing product promise,
- the R2 continuity center and shared primitives,
- the R2 pack-editing projection additions,
- the R2 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R2 exit criteria and explicit non-goals.

### Out of scope

- semantic branch maps or checkpoint-first exploration,
- artifact-centered continuity as the primary visible center,
- reusable Protocol/Applet execution packaging,
- commissioning preflight and Task Studio handoff depth,
- hidden memory behavior presented as “smart defaults” without inspection or removal control.

## 3. Inherited stage rules

### 3.1 Platform Gate and R1 substrate remain binding

R2 inherits the accepted Platform Gate baseline and the accepted R1 Transcript Chat contract.
R2 may deepen context control, but it may not replace bounded runs, frozen context, or stable source-bearing identity with transcript-local shortcuts.

### 3.2 Evidence-vs-context distinction rule

R2 must keep Evidence Pack and Context Pack semantics separate.
Evidence is the admitted grounding basis; Context is the full runtime package compiled from evidence, memory, canon, branch overlays where applicable, authority, policy, tools, and runtime constraints.

### 3.3 Explicit-memory-and-canon rule

Memory and canon may become visible in R2, but only through explicit scoped injection and pack inspection.
R2 must not reintroduce hidden memory sludge or allow memory/canon to silently rewrite admitted evidence.

## 4. R2 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | The user can directly inspect and shape what the model sees through real Evidence Pack and Context Pack controls rather than hidden assembly |
| Continuity center | Run continuity with explicit pack control |
| Shared primitives foregrounded | Thread / Line, Run, Evidence Pack, Context Pack, Memory Object, Canon Object |
| Projection-only additions | Span, Span Set, Lens, Context Operation, Pack Diff, Pack Freeze, Starter Pack |
| Protected seams and scenarios | `SS-01`, `GS-02`, `GS-03`, `EC-02`, plus Platform Gate tests `PG-01` and `PG-02` as inherited blockers |
| Handoff obligation | R2 -> R3 preserves Run identity, pack lineage, replay basis, and proof basis so later branching can fork semantic state instead of transcript history |

### 4.2 Shared-object contract

| Object family | R2 contract |
| --- | --- |
| Run | Pack editing and rerun behavior still resolve through bounded Runs rather than transcript mutation |
| Evidence Pack | The user can inspect includes, exclusions, pins, and role labels as the admitted grounding basis for the run |
| Context Pack | The user can inspect the compiled runtime package and distinguish summarized vs verbatim or injected material where surfaced |
| Memory Object | Active memory must be attributable, inspectable, and removable for the current run where policy allows |
| Canon Object | Active canon must show scope and consume/challenge posture rather than acting as hidden lore |
| Thread / Line | May still hold continuity where present, but pack state moves with the run instead of remaining transcript-only |

### 4.3 Projection-only additions

| R2 addition | Contract |
| --- | --- |
| Span | Provides addressable selection targets over messages, files, artifacts, or source excerpts |
| Span Set | Groups selected spans into reusable pack-editing or context-operation inputs |
| Lens | Provides focused pack views such as goals, contradictions, or constraints without changing shared object ownership |
| Context Operation | Runs bounded pack transformations such as summarize, extract constraints, compact, or contradiction extraction over selected spans |
| Pack Diff | Shows pack-basis differences explicitly rather than hiding changes across reruns or replays |
| Pack Freeze | Freezes a reusable admitted basis for replay and later comparison |
| Starter Pack | Provides reusable pack seeds without replacing real pack objects or compilation rules |

### 4.4 Package-maturity floor

| Package area | Required floor in R2 | Why R2 depends on it |
| --- | --- | --- |
| `pkg.context-compiler` | `M4` | R2 turns context assembly into a permanent substrate commitment through inspectable pack control, freeze, diff, and replay |
| `pkg.shared-object-api` | `M3` | R2 needs stable pack, memory, canon, and run refs that can be edited, saved, merged, and replayed |
| `pkg.replay-compare` | `M2` | Freeze, diff, and later branching require an explicit basis-diff seam rather than hidden recomputation |
| `pkg.event-provenance-spine` | `M3` | Pack edits, freezes, and reruns must leave reconstructable lineage instead of transient sidebar state |
| `pkg.monitor-inspect` | `M3` | R2 inspectors must project authoritative inclusion/exclusion and pack-basis details rather than UI-local guesses |

Inherited and still required in R2:

- `pkg.environment-control` remains at `M3`,
- `pkg.model-gateway` remains at `M2`,
- `pkg.review-writeback` remains at `M1`,
- `pkg.tool-gateway-sandbox` remains at `M1`.

R2 must not overclaim capabilities that require later-stage branch, artifact, reuse, or commissioning floors.

### 4.5 Exit criteria

R2 is contract-complete only when all of the following are true:

1. The user can inspect the Evidence Pack and Context Pack for a serious run before rerunning it.
2. Included memory and canon objects are attributable and removable for the run where policy allows.
3. Pack include/exclude/pin operations produce real pack-state changes rather than prompt-text substitutions.
4. Pack freeze and pack diff operate on stable admitted bases that remain replayable beyond transcript state.
5. Context operations can target addressable spans rather than only whole files or whole messages.
6. Pack state follows the Run and remains available for later replay/compare instead of living only inside the transcript sidebar.

### 4.6 Explicit non-goals and refusals

R2 deliberately refuses to overbuild any of the following:

- sidebar-only “context theater” without real pack control,
- semantic branch map or checkpoint UX,
- artifact-centered continuity as the visible center,
- hidden memory/canon influence that cannot be inspected or removed,
- reusable execution packaging or agent-builder semantics,
- commissioning preflight or Task Studio handoff depth as primary R2 UX.

## 5. Downstream handoff to R3

R3 may deepen into branch, checkpoint, and replay exploration, but it must inherit the R2 pack substrate rather than replace it.

> P4.5 is now accepted as the direct downstream realization of this handoff.
> The locks below remain the R2 -> R3 inheritance record.

The R2 contract therefore carries forward these locks:

- packs already have stable lineage before branch maps appear,
- freeze and diff already operate on real admitted bases before branching extends them,
- memory and canon are explicit pack inputs rather than hidden side channels,
- later branching must fork semantic pack state rather than duplicate transcript history only.

## 6. Downstream implications

- P4.5 has narrowed into semantic branch/replay behavior rather than
  rediscovering whether pack freeze and basis diff are already real. *(Resolved
  - P4.5 accepted on inherited R2 pack substrate.)*
- Later releases treat R2 as the proof that context control is a
  shared-substrate capability instead of a sidebar illusion. *(Resolved -
  inherited across accepted P4.6-P4.9 release packs.)*
- Phase 6 package planning has mapped R2 UI and service work onto the
  `M4`/`M3`/`M2` floors above rather than inventing an R2-private pack backend.
  *(Resolved - Phase 6 repo/package execution baseline accepted.)*

## 7. Acceptance notes

- This accepted artifact defines the R2 boundary, not the whole release doctrine.
- This accepted artifact keeps R2 intentionally focused on real pack control so later branch, artifact, reuse, and commissioning stages can carry forward one substrate story without rewrite drift.
