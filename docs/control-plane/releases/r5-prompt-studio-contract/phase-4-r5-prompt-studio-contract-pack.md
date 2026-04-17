# Phase 4 R5 Prompt Studio contract pack
Version: 1.0
Status: Accepted
Task: P4.7 — R5 Prompt Studio contract pack
Artifact ID: rel.r5-prompt-studio-contract.v1
Release ID: r5-prompt-studio-contract
Release scope: Accepted R5 contract pack covering governed prompt assets, prompt cards, model profiles, adaptations, lineage, staleness, inherited package floors, exit criteria, and explicit non-goals

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This contract pack was accepted as P4.7 under the accepted Phase 4 milestone
architecture plan (`rel.chat-native-milestone-architecture-plan.v1`) and the
accepted release-to-SDK maturity matrix
(`rel.chat-native-maturity-matrix.v1`).

As of Phase 4+ convergence:

- P4.6 remains the accepted upstream contract for artifact-governance
  continuity, proposal-first durability, and lineage-bearing prompt inputs that
  R5 inherits rather than replaces.
- P4.8 (R6 Governed Agent / Applet Chat) is accepted as the direct downstream
  inheritance of the R5 handoff described in §5.
- Phase 6 package planning has mapped the R5 `M4`/`M3` maturity floor in §4.4
  to concrete execution packets without inventing an R5-private prompt backend.
- Later accepted release packs inherit the R5 locks on governed prompt assets,
  adaptation lineage, and explicit no-hidden-prompt-lore boundaries rather than
  reopening prompt-side shadow-memory shortcuts.

This pack remains the accepted R5 contract authority. Sections below are kept
verbatim as the accepted human-owned contract record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R5 Prompt Studio.

It exists to:

- define how prompt assets become governed artifacts rather than hidden provider lore,
- make canonical-prompt generation, model-specific adaptation lineage, and staleness behavior explicit before reusable execution packaging appears,
- lock the package-maturity floor, exit criteria, and anti-substitution constraints for the R5 boundary.

## 2. Scope boundaries

### In scope

- the R5 user-facing product promise,
- the R5 prompt-asset continuity center and shared primitives,
- the R5 projection-only additions for prompt cards, model profiles, adaptations, lineage, and output targets,
- the R5 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R5 exit criteria and explicit non-goals.

### Out of scope

- reusable Protocol/Applet or Workflow execution UX,
- bounded background-run governance,
- commissioning preflight and Task Studio handoff depth,
- treating prompt cards as reusable execution identity,
- hidden provider adaptation lore or provider-side prompt mutation outside governed artifact flows.

## 3. Inherited stage rules

### 3.1 R4 artifact/governance substrate remains binding

R5 inherits the accepted Platform Gate baseline plus the accepted R1-R4 release contracts.
R5 may specialize prompt assets, but it may not replace artifact lineage, proposal-first durability, or frozen historical truth with provider-local prompt state.

### 3.2 Prompt-assets-are-governed-artifacts rule

Canonical prompts and model-specific adaptations remain governed artifacts with stable identity, revision lineage, proof, delta, and writeback behavior.
They do not become a parallel truth model or a hidden provider-specific store.

### 3.3 Adaptation-lineage-not-execution-identity rule

Model profiles, output targets, and adaptations may specialize prompt assets for later use, but they may not replace Protocol, Workflow, Trigger, or Applet ownership.
Provider-specific prompting behavior must stay explicit, versioned, and reviewable rather than undocumented lore.

## 4. R5 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | Canonical prompts and model-specific adaptations become governed, versioned prompt artifacts with explicit lineage, staleness, and reusable inputs rather than hidden provider lore |
| Continuity center | Prompt artifact lineage continuity |
| Shared primitives foregrounded | Artifact, Run, Proof Bundle, State Delta, Writeback Proposal |
| Projection-only additions | Prompt Artifact, Prompt Card, Model Profile, Adaptation, Adaptation Lineage, Output Target |
| Protected seams and scenarios | `SS-13`, `GS-08`, `GS-09`, `EC-04`, plus Platform Gate tests `PG-06` and `PG-07` as inherited blockers |
| Handoff obligation | R5 -> R6 preserves prompt-asset lineage, reusable execution inputs, and validation context without collapsing prompt assets into reusable execution identity |

### 4.2 Shared-object contract

| Object family | R5 contract |
| --- | --- |
| Artifact | Canonical prompts and model-specific adaptations remain artifact-level derivatives with stable identity, revision lineage, and reuse eligibility |
| Run | Prompt generation and adaptation work still resolves through bounded Runs rather than hidden provider-side prompt mutation |
| Proof Bundle | Prompt adaptation work must surface transform-style lineage basis, validation notes, compatibility/staleness notes, and uncertainty rather than prose-only rationale |
| State Delta | Prompt-generation and adaptation runs emit explicit created, revised, or stale-marked artifact state instead of hiding consequences in cards or provider settings |
| Writeback Proposal | Saving or updating prompt assets remains an explicit artifact-lane proposal flow rather than an ambient provider-side save action |

### 4.3 Projection-only additions

| R5 addition | Contract |
| --- | --- |
| Prompt Artifact | Presents a canonical prompt asset or derived prompt adaptation as a governed artifact rather than a free-floating prompt blob |
| Prompt Card | Projects prompt-asset identity, version, compatibility, and staleness state without replacing the underlying artifact truth |
| Model Profile | Projects typed model/provider capability and adaptation constraints instead of hiding provider-specific behavior as undocumented lore |
| Adaptation | Represents a model-specific derived artifact linked back to a canonical prompt artifact and explicit output target |
| Adaptation Lineage | Makes canonical-prompt -> adaptation derivation, dependency, and staleness relationships inspectable and compareable |
| Output Target | Names the explicit target model profile or adaptation destination rather than assuming ambient provider state |

### 4.4 Package-maturity floor

| Package area | Required floor in R5 | Why R5 depends on it |
| --- | --- | --- |
| `pkg.model-gateway` | `M4` | R5 makes provider abstraction, model-profile behavior, typed failures, and adaptation constraints a governed substrate seam rather than hidden lore |
| `pkg.shared-object-api` | `M4` | Prompt assets and adaptations remain stable artifact refs with lineage, compare targets, and reusable downstream inputs |
| `pkg.review-writeback` | `M4` | Prompt assets remain governed artifacts saved and revised through explicit proposal/review/writeback behavior rather than direct provider mutation |
| `pkg.event-provenance-spine` | `M4` | Prompt derivation, staleness, validation, and reuse lineage must remain append-only and reconstructable |
| `pkg.replay-compare` | `M4` | Adaptation compare, lineage diff, and version-target comparison must operate on explicit targets rather than ad hoc side-by-side text |
| `pkg.monitor-inspect` | `M3` | Prompt browser, prompt cards, model-profile views, and adaptation compare surfaces must project authoritative lineage and validation state |

Inherited and still required in R5:

- `pkg.environment-control` remains at `M3`,
- `pkg.context-compiler` remains at `M4`,
- `pkg.tool-gateway-sandbox` remains at `M1`.

R5 must not overclaim reusable-execution, background-governance, or commissioning-depth capabilities that belong to later stages.

### 4.5 Exit criteria

R5 is contract-complete only when all of the following are true:

1. A canonical prompt can be created as a prompt artifact without binding product truth to one provider transcript or hidden provider state.
2. Model-specific adaptations are explicit derived artifacts linked back to the canonical prompt artifact and the target model profile.
3. Prompt cards, model profiles, and output targets resolve to explicit Artifact, Run, Proof Bundle, State Delta, and lineage state rather than undocumented provider lore.
4. Adaptation compare surfaces preserve explicit target identity, derivation lineage, and material differences rather than ad hoc side-by-side text.
5. Changes to a canonical prompt artifact or model profile can mark affected adaptations stale explicitly rather than leaving compatibility drift implicit.
6. Saving or updating prompt assets occurs through explicit artifact-governance flows instead of provider-side mutation or hidden overwrite.
7. Prompt assets can feed later runs, protocols, or applets without replacing Protocol/Applet identity or run-class ownership.

### 4.6 Explicit non-goals and refusals

R5 deliberately refuses to overbuild any of the following:

- prompt cards as substitutes for Protocol, Workflow, Trigger, or Applet semantics,
- hidden provider adaptation lore or undocumented prompt state,
- direct provider-side save behavior that bypasses artifact/proposal governance,
- collapsing prompt assets into reusable execution identity,
- background-run or governed-autonomy packaging as an R5 milestone,
- commissioning preflight or Task Studio handoff depth as primary R5 UX.

## 5. Downstream handoff to R6

R6 may turn successful prompt-backed flows into reusable execution, but it must inherit the R5 prompt-asset substrate rather than replace it.

> P4.8 is now accepted as the direct downstream realization of this handoff.
> The locks below remain the R5 -> R6 inheritance record.

The R5 contract therefore carries forward these locks:

- prompt assets already have stable artifact and adaptation lineage before Protocol/Applet packaging appears,
- model-specific behavior remains model-gateway-visible and versioned rather than becoming applet-local lore,
- prompt assets may feed reusable execution inputs, but they must not replace Protocol, Workflow, Trigger, or Applet identity,
- staleness, derivation, and validation context must survive when prompt assets are reused by governed execution.

## 6. Downstream implications

- P4.8 has narrowed into Protocol/Applet/Workflow/Trigger and background-run
  semantics rather than rediscovering whether prompt assets are governed
  artifacts with explicit lineage and staleness. *(Resolved - P4.8 accepted on
  inherited R5 prompt-asset substrate.)*
- Later releases must treat R5 as the proof that provider abstraction and
  prompt adaptation are governed substrate rather than hidden prompt lore.
  *(Resolved - inherited by accepted downstream release packs.)*
- Phase 6 package planning has mapped R5 UI and service work onto the
  `M4`/`M3` floors above rather than inventing an R5-private prompt backend.
  *(Resolved - Phase 6 repo/package execution baseline accepted.)*

## 7. Acceptance notes

- This accepted artifact defines the R5 boundary, not the whole release doctrine.
- This accepted artifact keeps R5 intentionally focused on governed prompt assets and adaptation lineage so later reusable-execution and commissioning stages can inherit one substrate story without rewrite drift.
