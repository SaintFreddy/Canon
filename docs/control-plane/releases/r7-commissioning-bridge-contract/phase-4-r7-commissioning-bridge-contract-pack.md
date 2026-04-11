# Phase 4 R7 Commissioning Bridge contract pack
Version: 1.0
Status: Accepted
Task: P4.9 — R7 Commissioning Bridge contract pack
Artifact ID: rel.r7-commissioning-bridge-contract.v1
Release ID: r7-commissioning-bridge-contract
Release scope: Accepted R7 contract pack covering Commission/Contract preflight, live monitoring, proof ledger, delta inspection, lane-by-lane writeback review, inherited package floors, exit criteria, and Task Studio-safe handoff constraints

This artifact is accepted for downstream use.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R7 Commissioning Bridge.

It exists to:

- define how explicit commissioning inside chat becomes real through Commission, Contract, Authority Scope, preflight, monitoring, proof, delta, and handoff objects,
- make serious work stop being chat convenience by escalating governed reusable execution into explicit commissioned-work semantics,
- lock the package-maturity floor, exit criteria, and anti-drift constraints for the R7 boundary and Task Studio-safe handoff.

## 2. Scope boundaries

### In scope

- the R7 user-facing product promise,
- the R7 commissioning continuity center and shared primitives,
- the R7 projection-only additions for commission cards, contract drafts, run preflight, acceptance stacks, and chat-to-run handoff,
- the R7 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R7 exit criteria and explicit non-goals.

### Out of scope

- Phase 5 proof, evaluation, and governance deepening,
- Task Studio rewrite or app-private task semantics beyond preserving the handoff payload,
- treating `triage` as a bridge-only ontology instead of the accepted intake run class,
- lane-collapsing writeback convenience or skipped authority/proof preflight,
- second truth models inside monitor, ledger, delta-inspection, or handoff views.

## 3. Inherited stage rules

### 3.1 R6 governed-reuse substrate remains binding

R7 inherits the accepted Platform Gate baseline plus the accepted R1-R6 release contracts.
Commissioning may escalate reusable execution into serious work, but it may not replace accepted protocol/applet context, governance state, prompt lineage, or run truth with chat-private bridge semantics.

### 3.2 Serious work resolves through Commission -> Contract -> Run

Commission is the request continuity anchor, Contract is the executable narrowing of that request, and Run remains the consequential execution unit.
`triage` is the intake class for the commissioning bridge; it is not a private R7 taxonomy.

### 3.3 Preflight, proof, writeback, and handoff stay explicit

Run Preflight, Live Monitor, Proof Ledger, Delta Inspector, Acceptance Stack, and Chat-to-Run Handoff are projections over shared Authority Scope, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision, and handoff continuity.
They may not become a second truth model, and they may not erase lane separation or object identity during the Task Studio handoff.

## 4. R7 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | Explicit commissioning inside chat becomes real through Commission/Contract preflight, live monitoring, proof ledger, delta/writeback inspection, and chat-to-run handoff without ontology translation into Task Studio |
| Continuity center | Commission/Contract continuity into explicit run governance and Task Studio handoff |
| Shared primitives foregrounded | Commission, Contract, Run Class, Authority Scope, Run, Proof Bundle, State Delta, Writeback Proposal, Review, Approval Decision, Handoff |
| Projection-only additions | Commission Card, Contract Draft, Run Preflight, Acceptance Stack, Chat-to-Run Handoff |
| Protected seams and scenarios | `SS-04`, `SS-05`, `SS-09`, `GS-12`, `GS-13`, `GS-14`, `EC-06`, `EC-07`, plus Platform Gate tests `PG-05`, `PG-06`, `PG-08`, and `PG-09` as inherited blockers |
| Handoff obligation | R7 -> Task Studio preserves Commission, Contract, Run, Authority Scope, Proof Bundle, State Delta, Writeback Proposal, and Artifact links as the exact handoff payload with shared IDs unchanged |

### 4.2 Shared-object contract

| Object family | R7 contract |
| --- | --- |
| Commission | Becomes the request continuity anchor for serious work with explicit objective, scope summary, priority, and requested authority envelope instead of staying a transcript-level ask |
| Contract | Narrows a Commission into executable scope, run class, deliverable schemas, acceptance policy, and authority scope; material amendment creates a new contract record rather than mutating live scope in place |
| Run Class | Uses `triage` as the intake class for commissioning preflight and preserves downstream run-class meaning instead of inventing a bridge-private taxonomy |
| Authority Scope | Run preflight and consequential execution must expose explicit grants, limits, and policy refs while keeping authority separate from strategy |
| Run | Commissioned execution remains a bounded Run linked to explicit commission, contract, and authority refs; new attempts or escalations create new historical records |
| Proof Bundle | Proof Ledger and preflight expose verifier outcomes, uncertainty, omissions, contradictions, and failure basis as structured records rather than persuasive prose |
| State Delta | Delta Inspector presents explicit proposed or observed change state, including empty or failure-state deltas, instead of hiding consequences in chat summaries |
| Writeback Proposal | Durable effects remain lane-separated, review-gated, and partially acceptable inside chat rather than collapsing into one convenience action |
| Review | Acceptance Stack uses Review as the decision container for lane-by-lane evaluation rather than replacing it with one bridge-only verdict |
| Approval Decision | Attributable, append-only approval records remain visible through preflight, review, and Task Studio handoff |
| Handoff | Chat-to-Run Handoff preserves exact Commission, Contract, Run, Authority Scope, Proof Bundle, State Delta, Writeback Proposal, and Artifact link continuity rather than exporting and recreating task-local objects |

### 4.3 Projection-only additions

| R7 addition | Contract |
| --- | --- |
| Commission Card | Projects commission identity, priority, scope, and lifecycle state without replacing the underlying Commission and Contract objects |
| Contract Draft | Projects executable scope shaping and amendment work while preserving explicit contract records and acceptance policy |
| Run Preflight | Projects authority scope, acceptance basis, admitted/frozen inputs, and scope gaps before consequential execution instead of hiding them in confirmation prose |
| Acceptance Stack | Projects review, approval, and lane-specific acceptance state over proof, delta, and writeback objects rather than collapsing them into one persuasive verdict |
| Chat-to-Run Handoff | Projects the preserved Task Studio transfer payload with shared IDs rather than an export/import or rewrite step |

### 4.4 Package-maturity floor

| Package area | Required floor in R7 | Why R7 depends on it |
| --- | --- | --- |
| `pkg.environment-control` | `M4` | R7 makes commissioning-grade admission, authority/preflight routing, and handoff-safe scope enforcement first-class and unavoidable |
| `pkg.monitor-inspect` | `M4` | R7 makes live monitoring, proof ledger, delta inspection, and handoff-safe inspection commissioning-grade rather than view-local conveniences |
| `pkg.shared-object-api` | `M4` | Commission, Contract, Authority Scope, Review, Approval, Handoff, and writeback objects must remain stable across chat and Task Studio |
| `pkg.context-compiler` | `M4` | Run preflight and Task Studio handoff must preserve the same frozen admitted basis rather than rebuilding context from transcript state |
| `pkg.event-provenance-spine` | `M4` | Commission, contract, run, review, approval, writeback, and handoff lineage must remain append-only and reconstructable |
| `pkg.review-writeback` | `M4` | Lane-by-lane review, approval history, and writeback application stay explicit inside commissioning flows |
| `pkg.replay-compare` | `M4` | Contract amendments, proof comparisons, delta inspection, and handoff review must operate on explicit refs rather than bridge-local summaries |
| `pkg.model-gateway` | `M4` | Commissioned work still relies on typed provider invocation and inspectable failure accounting rather than hidden model lore |
| `pkg.tool-gateway-sandbox` | `M4` | Consequential commissioned work still depends on typed tool execution, side-effect previews, scoped credentials, and inspectable failures |

By R7, every package area in the accepted Phase 4 maturity matrix is at `M4`.
R7 must not overclaim Phase 5 proof/governance deepening or Task Studio surface completion.

### 4.5 Exit criteria

R7 is contract-complete only when all of the following are true:

1. Serious work in chat resolves through explicit Commission -> Contract -> Run semantics, with `triage` as the intake class rather than a private bridge taxonomy.
2. Commissions, Contracts, Authority Scopes, and Runs resolve to explicit shared objects with inspectable identity, lifecycle, and scope boundaries; material amendment creates a new contract record rather than mutating scope in place.
3. Run Preflight exposes authority scope, acceptance basis, frozen admitted basis, scope gaps, and downstream run-class intent before consequential execution begins.
4. Live Monitor, Proof Ledger, and Delta Inspector project authoritative Run, Proof Bundle, State Delta, Writeback Proposal, Review, and Approval objects rather than monitor-only or chat-only truth.
5. Proof, delta, review, approval, and writeback remain lane-separated and inspectable inside chat, including partial acceptance behavior and lane-local decisions.
6. Failed or blocked commissioned work still emits inspectable proof or failure basis and delta state; monitor and ledger views do not disappear on failure.
7. Handoff to Task Studio preserves shared IDs and object continuity (`commission_id`, `contract_id`, `run_id`, `proof_bundle_id`, `state_delta_id`, `writeback_proposal_id`, and linked artifacts) rather than recreating objects or translating ontology.
8. R7 inherits R6 governed-reuse context, protocol/applet lineage, and approval state rather than replacing them with chat-private commissioning semantics.
9. Scope widening or writable consequential work requires explicit authority scope and accepted contract before the next run; no silent escalation happens from prompts, monitor actions, or approval surfaces.

### 4.6 Explicit non-goals and refusals

R7 deliberately refuses to overbuild any of the following:

- chat-private commissioning ontology or bridge-only task taxonomy,
- skipping explicit Commission, Contract, Authority Scope, proof, or preflight semantics for serious work,
- lane-collapsing or silent writeback convenience inside chat,
- Task Studio rewrite or object recreation at the handoff boundary,
- treating `triage` as an app-private class or reclassifying work into a separate Task Studio-only taxonomy,
- second truth models in Live Monitor, Proof Ledger, Delta Inspector, or Acceptance Stack views,
- commission cards, contract drafts, or acceptance stacks as substitutes for underlying shared objects,
- claiming that Phase 5 proof, evaluation, or governance deepening is already complete in R7.

## 5. Downstream handoff to Task Studio

Task Studio may become the primary commissioned-work projection, but it must inherit the R7 commissioning payload exactly rather than rewriting object meaning.

The R7 contract therefore carries forward these locks:

- shared Commission, Contract, Authority Scope, Run, Proof Bundle, State Delta, Writeback Proposal, and Artifact link identities stay stable across the handoff,
- preflight, ledger, and acceptance context remain inspectable after handoff instead of collapsing into task metadata,
- lane-separated review and approval history remains attributable and append-only,
- R6 protocol/applet context plus prompt-lineage inputs remain linked wherever commissioned work depends on them,
- Task Studio is a projection change over the same commissioned-work semantics, not a separate ontology.

## 6. Downstream implications

- Phase 5 packs should deepen governance/authority/writeback, proof/validation/evaluation, run-class protocol packs, reusable execution objects, and Task Studio surfaces on top of this accepted commissioning and handoff boundary rather than reopening it.
- Later releases must treat R7 as the proof that explicit commissioning and Task Studio-safe continuity are real rather than future-only intent.
- Phase 6 surface and package planning should map onto the all-`M4` package posture above rather than inventing an R7-private control plane.

## 7. Acceptance notes

- This accepted artifact defines the R7 boundary, not the whole reusable-semantics doctrine.
- This accepted artifact keeps R7 intentionally focused on explicit commissioning, lane-separated governance, and Task Studio-safe handoff so later work can deepen the shared substrate without ontology drift.

