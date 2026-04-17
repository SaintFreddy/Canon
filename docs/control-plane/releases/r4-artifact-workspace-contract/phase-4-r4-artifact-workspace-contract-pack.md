# Phase 4 R4 Artifact Workspace contract pack
Version: 1.0
Status: Accepted
Task: P4.6 — R4 Artifact Workspace contract pack
Artifact ID: rel.r4-artifact-workspace-contract.v1
Release ID: r4-artifact-workspace-contract
Release scope: Accepted R4 contract pack covering artifact-centered continuity, focal artifact runs, proposal/review loops, historical truth per run, inherited package floors, exit criteria, and explicit non-goals

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This contract pack was accepted as P4.6 under the accepted Phase 4 milestone
architecture plan (`rel.chat-native-milestone-architecture-plan.v1`) and the
accepted release-to-SDK maturity matrix
(`rel.chat-native-maturity-matrix.v1`).

As of Phase 4+ convergence:

- P4.5 remains the accepted upstream contract for semantic branch/replay
  continuity, merge-proposal lineage, and proof/delta-aware replay that R4
  inherits rather than replaces.
- P4.7 (R5 Prompt Studio) is accepted as the direct downstream inheritance of
  the R4 handoff described in §5.
- Phase 6 package planning has mapped the R4 `M4`/`M3`/`M2` maturity floor in
  §4.4 to concrete execution packets without inventing an R4-private backend.
- Later accepted release packs inherit the R4 locks on artifact-centered
  continuity, proposal-first durability, and historical truth per run rather
  than reopening silent artifact-mutation shortcuts.

This pack remains the accepted R4 contract authority. Sections below are kept
verbatim as the accepted human-owned contract record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R4 Artifact Workspace.

It exists to:

- define how continuity moves out of transcript gravity and into governed artifacts,
- make focal-artifact runs, proposal/review loops, and historical truth per run explicit before prompt-asset work appears,
- lock the package-maturity floor, exit criteria, and anti-mutation constraints for the R4 boundary.

## 2. Scope boundaries

### In scope

- the R4 user-facing product promise,
- the R4 artifact-centered continuity center and shared primitives,
- the R4 projection-only additions for focal artifacts, proposal/review affordances, canon strip behavior, and artifact alternatives,
- the R4 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R4 exit criteria and explicit non-goals.

### Out of scope

- prompt-asset specialization or model-profile behavior,
- reusable Protocol/Applet execution packaging,
- commissioning preflight and Task Studio handoff depth,
- silent artifact mutation or generic one-click save behavior,
- treating artifact history as a replacement for run/proof/delta truth.

## 3. Inherited stage rules

### 3.1 R3 branch/replay substrate remains binding

R4 inherits the accepted Platform Gate baseline plus the accepted R1-R3 release contracts.
R4 may foreground artifacts, but it may not replace bounded runs, frozen replay basis, or explicit branch lineage with artifact-local shortcuts.

### 3.2 Artifact-centered-but-run-consequential rule

Artifact becomes the visible continuity anchor in R4.
Run remains the primary consequential unit, and artifacts stay linked back to the runs, proof, deltas, and proposals that produced or revised them.

### 3.3 Proposal-first-and-historical-truth rule

Durable mutation remains proposal-first and lane-separated.
Historical truth for any artifact-facing run stays frozen and inspectable even after later artifact revisions, alternatives, objections, or canon decisions appear.

## 4. R4 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | Work centers on focal artifacts and governed proposals: runs attach to artifacts, emit explicit proof/delta/writeback state, and keep historical truth per run rather than silently mutating durable outputs |
| Continuity center | Artifact-centered continuity over run history |
| Shared primitives foregrounded | Artifact, Run, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision |
| Projection-only additions | Root Artifact, Focal Artifact, Proposal, Canon Strip, Review Anchor, Alternative Artifact, Objection Artifact, Artifact Resume Packet |
| Protected seams and scenarios | `SS-02`, `SS-03`, `SS-04`, `GS-06`, `GS-07`, `EC-03`, plus Platform Gate tests `PG-05` and `PG-06` as inherited blockers |
| Handoff obligation | R4 -> R5 preserves Artifact identity, derivation lineage, proof/delta basis, and prompt-oriented outputs as governed artifact derivatives rather than private prompt state |

### 4.2 Shared-object contract

| Object family | R4 contract |
| --- | --- |
| Artifact | Artifacts become the visible continuity anchor with stable identity and revision lineage linked back to producing runs, proof, deltas, and proposals |
| Run | Artifact-targeted transform, audit, or synthesize work still resolves through bounded Runs rather than direct artifact mutation |
| Proof Bundle | Artifact review, canon-strip decisions, and proposal acceptance must surface structured proof, omissions, contradictions, and validation basis rather than prose-only justification |
| State Delta | Every focal-artifact run emits an explicit summary of created, modified, or proposed state instead of hiding consequences in the canvas |
| Writeback Proposal | Artifact, canon, memory, workflow, and export consequences remain lane-separated, reviewable, and partially acceptable rather than collapsing into one save action |
| Review | Proposal inbox items and review anchors resolve to explicit Review objects linked to artifacts, proof, deltas, and proposal targets |
| Approval Decision | Artifact-facing acceptance, rejection, or partial acceptance remains attributable and bound to explicit proposal/review targets |

### 4.3 Projection-only additions

| R4 addition | Contract |
| --- | --- |
| Root Artifact | Anchors the artifact workspace and artifact-library continuity without replacing the run model underneath it |
| Focal Artifact | Defines the currently foregrounded artifact lens and the default run target within the workspace |
| Proposal | Projects candidate artifact-facing changes or outputs backed by State Delta, Writeback Proposal, Review, and Approval Decision objects |
| Canon Strip | Surfaces canon-linked context or promotion candidates adjacent to the focal artifact while keeping canon as a separate durable lane |
| Review Anchor | Attaches review context to artifact regions or proposal elements and resolves back to Review, Approval Decision, Proof Bundle, and State Delta objects |
| Alternative Artifact | Preserves a competing artifact as a first-class lineage-bearing object rather than an overwritten draft |
| Objection Artifact | Preserves a challenge or objection as a first-class artifact rather than collapsing it into comments or hidden review prose |
| Artifact Resume Packet | Provides artifact-centered resume and since-last-visit state without relying on transcript history as the continuity anchor |

### 4.4 Package-maturity floor

| Package area | Required floor in R4 | Why R4 depends on it |
| --- | --- | --- |
| `pkg.shared-object-api` | `M4` | R4 makes Artifact, Proposal, Review, Approval, Proof, and Delta refs a carry-forward continuity seam that later stages must inherit unchanged |
| `pkg.review-writeback` | `M4` | Proposal inbox, lane-local review, partial acceptance, and apply behavior become a bridge-stage governance seam rather than optional support logic |
| `pkg.event-provenance-spine` | `M4` | Artifact lineage, proposal history, review history, and historical truth per run must remain append-only and reconstructable |
| `pkg.replay-compare` | `M4` | Artifact continuity still depends on inherited branch/replay lineage and explicit revision/proposal comparison rather than latest-text wins behavior |
| `pkg.context-compiler` | `M4` | Historical truth per artifact-facing run depends on frozen admitted basis and replayable context behind later revisions |
| `pkg.monitor-inspect` | `M3` | Artifact workspace, proposal inbox, proof ledger, delta inspector, and artifact resume views must project authoritative state rather than view-local guesses |

Inherited and still required in R4:

- `pkg.environment-control` remains at `M3`,
- `pkg.model-gateway` remains at `M2`,
- `pkg.tool-gateway-sandbox` remains at `M1`.

R4 must not overclaim prompt-governance, reusable-execution, or commissioning-depth capabilities that belong to later stages.

### 4.5 Exit criteria

R4 is contract-complete only when all of the following are true:

1. A user can target a focal artifact with a new run while preserving explicit run identity, frozen basis, and artifact linkage.
2. Runs against focal artifacts emit explicit Proof Bundle, State Delta, and Writeback Proposal objects instead of silently mutating artifact state.
3. Proposal inbox items and review anchors resolve to Review, Approval Decision, Proof Bundle, State Delta, and Writeback Proposal records rather than generic comments or notifications.
4. Lane-local partial acceptance works, including artifact-lane acceptance with canon-lane rejection, without collapsing proposals or mutating durable state silently.
5. Historical truth for any artifact-facing run remains inspectable even after later artifact revisions, alternatives, or objections exist.
6. Alternative and objection artifacts remain first-class artifacts with lineage instead of comments, overwritten drafts, or hidden review branches.
7. Artifact browse and resume flows can navigate from an artifact to the source run, proof, delta, and proposal history without relying on transcript history.

### 4.6 Explicit non-goals and refusals

R4 deliberately refuses to overbuild any of the following:

- silent artifact mutation,
- treating artifacts as replacements for runs,
- collapsing alternatives or objections into comments or versionless overwrites,
- one-click save behavior that collapses writeback lanes,
- prompt-governance or reusable-execution packaging as an R4 milestone,
- using artifact or transcript history as a substitute for proof/delta/review lineage.

## 5. Downstream handoff to R5

R5 may specialize governed prompt assets, but it must inherit the R4 artifact/governance substrate rather than replace it.

> P4.7 is now accepted as the direct downstream realization of this handoff.
> The locks below remain the R4 -> R5 inheritance record.

The R4 contract therefore carries forward these locks:

- artifact identity, revision lineage, and proposal review are already stable before prompt-specific derivatives appear,
- proof, delta, and writeback basis remain attached to artifact-producing runs so prompt adaptations inherit lineage rather than private prompt state,
- alternative and objection artifacts remain artifact-layer facts even when some artifacts become prompt assets,
- prompt assets may specialize governed artifacts, but they must not bypass artifact-lane governance or rewrite historical truth.

## 6. Downstream implications

- P4.7 has narrowed into prompt-asset lineage and adaptation behavior rather
  than rediscovering whether artifact-centered continuity and proposal
  governance are already real. *(Resolved - P4.7 accepted on inherited R4
  artifact/governance substrate.)*
- Later releases treat R4 as the bridge out of transcript gravity and the
  proof that durable mutation remains proposal-first and lane-separated.
  *(Resolved - inherited by accepted downstream release packs.)*
- Phase 6 package planning has mapped R4 UI and service work onto the
  `M4`/`M3`/`M2` floors above rather than inventing an R4-private backend.
  *(Resolved - Phase 6 repo/package execution baseline accepted.)*

## 7. Acceptance notes

- This accepted artifact defines the R4 boundary, not the whole release doctrine.
- This accepted artifact keeps R4 intentionally focused on artifact-centered continuity and explicit proposal/review behavior so later prompt, reusable-execution, and commissioning stages can inherit one substrate story without rewrite drift.
