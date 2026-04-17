# Phase 4 R1 Transcript Chat contract pack
Version: 1.0
Status: Accepted
Task: P4.3 — R1 Transcript Chat contract pack
Artifact ID: rel.r1-transcript-chat-contract.v1
Release ID: r1-transcript-chat-contract
Release scope: Accepted R1 contract pack covering the first public chat-native release promise, shared primitives, projection-only additions, package floors, exit criteria, and explicit non-goals

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This contract pack was accepted as P4.3 under the accepted Phase 4 milestone
architecture plan (`rel.chat-native-milestone-architecture-plan.v1`) and the
accepted release-to-SDK maturity matrix
(`rel.chat-native-maturity-matrix.v1`).

As of Phase 4+ convergence:

- P4.2 now records P4.3-P4.9 as accepted downstream contract packs, and this
  pack remains the accepted R1 authority for the bounded familiar-chat release
  boundary.
- P4.4 (R2 Context Chat) is accepted as the direct downstream inheritance of
  the R1 handoff described in §5.
- Phase 6 package planning has mapped the R1 `M3`/`M2` maturity floor in §4.4
  to concrete execution packets without inventing an R1-private backend.
- Later accepted release packs inherit the R1 refusals on transcript-as-truth
  and hidden provider continuity rather than reopening those shortcuts.

This pack remains the accepted R1 contract authority. Sections below are kept
verbatim as the accepted human-owned contract record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R1 Transcript Chat.

It exists to:

- define exactly what the first public release is allowed to promise,
- make the shared-object substrate and projection-only additions explicit,
- lock the package-maturity floor, exit criteria, and forbidden shortcuts for the R1 boundary.

## 2. Scope boundaries

### In scope

- the R1 user-facing product promise,
- the R1 continuity center and shared primitives,
- the R1 chat-domain projection additions,
- the R1 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R1 exit criteria and explicit non-goals.

### Out of scope

- full evidence/context editing,
- semantic branching or replay-first exploration,
- artifact-centered continuity as the primary visible center,
- reusable Protocol/Applet execution packaging,
- explicit commissioning preflight and Task Studio handoff depth.

## 3. Inherited stage rules

### 3.1 Platform Gate remains blocking

R1 may ship only on top of the accepted Platform Gate baseline.
No R1 implementation or contract interpretation may bypass the substrate proof required by `arch.phase3-platform-gate-spec.v1`.

### 3.2 Familiar-chat-not-transcript-truth rule

R1 may foreground a familiar conversation surface, but assistant turns remain outputs of bounded Runs.
Provider transcript continuity may assist UX or retrieval, but it must never become product truth, replay truth, or run identity.

### 3.3 Compact-inspection rule

R1 is allowed to keep inspection compact, but not hidden.
Every assistant answer must still resolve back to the same Run, frozen Context Pack snapshot, source-bearing objects or source regions, and proof basis that later stages inherit.

## 4. R1 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | The product feels like familiar AI chat, but each assistant answer is already a bounded run with compact source/run inspection and frozen context behind it |
| Continuity center | Thread-assisted run continuity |
| Shared primitives foregrounded | Thread / Line, Run, Source Reference, Artifact, Context Pack snapshot, Proof Bundle summary |
| Projection-only additions | Message Block, Conversation Surface, Source Chip, Resume Packet |
| Protected seams and scenarios | `SS-01`, `SS-02`, `SS-10`, `GS-01`, `EC-10`, plus Platform Gate tests `PG-01`, `PG-02`, and `PG-03` as inherited blockers |
| Handoff obligation | R1 -> R2 preserves Thread / Line continuity, Run identity, Source Reference identity, and evidence/context lineage instead of rehydrating provider transcript state |

### 4.2 Shared-object contract

| Object family | R1 contract |
| --- | --- |
| Thread / Line | Holds conversational continuity only; it is not the consequential truth object |
| Run | Every assistant answer that matters is the output of a distinct Run with stable identity and lifecycle state |
| Source Reference | Attached files, URLs, and cited material resolve to stable source-bearing objects rather than transcript-only blobs |
| Context Pack snapshot | Every answer has a frozen admitted basis even when only a compact drawer is shown |
| Proof Bundle summary | R1 exposes a compact proof basis sufficient to show that source grounding and run identity are real |
| Artifact | R1 may emit durable artifacts from answers, but artifact-centered continuity is not yet the primary visible center |

### 4.3 Projection-only additions

| R1 addition | Contract |
| --- | --- |
| Message Block | Presents a run result inside the conversation surface without becoming the truth anchor |
| Conversation Surface | Provides the familiar chat entry path while remaining a projection over shared substrate objects |
| Source Chip | Resolves to source-bearing objects or source regions, not to decorative citations |
| Resume Packet | Lets a thread resume without requiring hidden provider-managed transcript continuity |

### 4.4 Package-maturity floor

| Package area | Required floor in R1 | Why R1 depends on it |
| --- | --- | --- |
| `pkg.environment-control` | `M3` | Familiar chat still has to admit bounded runs, reruns, and monitorable execution on the shared substrate |
| `pkg.context-compiler` | `M3` | Every R1 answer requires frozen admitted context and source-grounded compilation rather than hidden transcript assembly |
| `pkg.shared-object-api` | `M2` | Compact R1 inspection still needs stable refs for runs, sources, artifacts, and snapshots |
| `pkg.model-gateway` | `M2` | Provider/model changes must not break continuity or push product truth back into one provider transcript |
| `pkg.event-provenance-spine` | `M2` | Run/result/source continuity must survive beyond the visible chat turn |
| `pkg.monitor-inspect` | `M2` | Compact drawers and inspectors must project authoritative run/context/proof state rather than stage-local UI guesses |

Inherited but not newly central in R1:

- `pkg.review-writeback` stays at `M1`,
- `pkg.replay-compare` stays at `M1`,
- `pkg.tool-gateway-sandbox` stays at `M1`.

R1 must not overclaim capabilities that require those later-stage floors.

### 4.5 Exit criteria

R1 is contract-complete only when all of the following are true:

1. Every assistant answer has a stable `run_id`, frozen Context Pack snapshot, and inspectable source list.
2. Source chips resolve to source-bearing objects or stable source regions.
3. Losing provider transcript continuity does not erase Run identity, proof basis, or source traceability.
4. Threads can resume through shared substrate objects rather than hidden provider conversation state alone.
5. Rerun or regenerate creates a new Run instead of mutating prior run truth in place.
6. Compact R1 inspection surfaces resolve back to authoritative Run, Context Pack snapshot, and proof-basis objects.

### 4.6 Explicit non-goals and refusals

R1 deliberately refuses to overbuild any of the following:

- transcript-as-truth behavior,
- hidden provider continuity as the only resume mechanism,
- full evidence/context editing,
- semantic branch/replay UX,
- artifact-centered continuity as the visible center,
- governed reusable execution or agent-builder semantics,
- commissioning preflight or lane-by-lane writeback review as primary R1 UX.

## 5. Downstream handoff to R2

> P4.4 is now accepted as the direct downstream realization of this handoff.
> The locks below remain the R1 -> R2 inheritance record.

R2 may deepen context control, but it must inherit the R1 substrate rather than replace it.

The R1 contract therefore carries forward these locks:

- the assistant answer is still a Run result, not a transcript truth anchor,
- source-bearing identity already exists before pack editing becomes user-visible,
- compact context inspection in R1 becomes fuller pack control in R2 without changing the underlying object model,
- any future context controls must remain real enough to preserve frozen replay and source traceability.

## 6. Downstream implications

- P4.4 has narrowed into real evidence/context control rather than
  rediscovering whether R1 already runs on frozen context and stable source
  refs. *(Resolved - P4.4 accepted on inherited R1 substrate.)*
- Later releases treat R1 as the proof that familiar chat can already run on
  the shared substrate without transcript-truth shortcuts. *(Resolved -
  inherited across accepted P4.5-P4.9 release packs.)*
- Phase 6 package planning has mapped R1 UI and service work onto the `M3`/`M2`
  floors above rather than inventing an R1-private backend. *(Resolved - Phase
  6 repo/package execution baseline accepted.)*

## 7. Acceptance notes

- This accepted artifact defines the first public release boundary, not the whole chat-native phase.
- This accepted artifact keeps R1 intentionally narrow so later stages can carry forward real context, branch, artifact, reuse, and commissioning seams without rewrite drift.
