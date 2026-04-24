# Phase 3 Platform Gate spec and exit audit
Version: 1.0
Status: Accepted
Task: P3.5 — Platform Gate spec + exit audit
Artifact ID: arch.phase3-platform-gate-spec.v1
Architecture scope: Accepted internal pre-R1 gate defining required primitives, forced package areas, exit tests, audit checklist, and blocking failure conditions

## 0. Gate status (Phase 4+ update)

This gate spec was accepted as P3.5. It defines the hard pre-R1 blocking
criteria that were proven before Phase 4 release work proceeded.

Gate passage confirmation:
- `arch.phase3-architecture-sync-pass.v1` (P3.6) confirmed all §6 exit tests
  and §7 checklist items were met and declared no substrate drift before P4.1.
- `rel.chat-native-maturity-matrix.v1` (P4.1) inherited the §5 forced package
  areas without downgrade, confirming the substrate was real enough to bear
  the Phase 4 maturity floors.
- Phase 7 automation (`docs/control-plane/sync/`) now provides recurring
  gate-recheck automation (P7.4) that treats §6 and §8 as its regression basis.

The §6 exit-test catalog, §7 audit checklist, and §8 failure classes below
are kept verbatim as the authoritative gate record. They are now historical
proof criteria rather than open blockers.

## 0.1 Gate status (Phase 4+ reopen event, 2026-04-23)

On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the
Platform Gate acceptance marker against the 2026-04-18 agentic-engine
audit-cited contradiction event. The governing decision is
`canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A).

Authority-preservation rule: §0 above and §7 below remain verbatim. The
prior `Gate passed` state is preserved as append-only history and is not
deleted.

Reopen marker:

- `Gate reopened — audit-cited contradiction event 2026-04-18.`
- Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1` (all three sub-gates closed 2026-04-24 via the engine-side remediation PRs referenced in §0.1.1; the reopen event itself is preserved as append-only history per DEC-RO-0f Option A, so this spec does NOT revert the §7 audit-checklist header to the prior `Gate passed` line).
- Successor checkpoint: `post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint`
  is formally superseded by `post-reopen-audit-cited-contradiction-checkpoint`.

### 0.1.1 Remediation sub-gates

Three remediation sub-gates close the reopen. All three landed on `SaintFreddy/agentic-engine` main on 2026-04-24. The Platform Gate acceptance marker does NOT automatically revert to `passed` — DEC-RO-0f Option A keeps `Gate passed` as append-only history in §7 and keeps this reopen event recorded alongside it as the new substrate-truth. The sub-gate table below records the closure status and citation evidence for each sub-gate.

| Sub-gate | Status | Closes when | Closure evidence |
| --- | --- | --- | --- |
| `PG-01.1` | closed 2026-04-24 | engine `Clock` abstraction landed in `@canon/engine-core` with Shared Env production impl; `stableStringify` unified in `@canon/engine-core`; `localeCompare` purged from replay-sensitive sort paths; `frozenAt` placement decision recorded and implemented (condition (a), condition (d), and the `frozenAt` hash-inclusion sub-decision). | `SaintFreddy/agentic-engine` PRs for Clock, thaw-timestamp, localeCompare, frozenAt-in-hashed-doc, stableStringify (see CF-0089..CF-0096 in `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md`). |
| `PG-07.1` | closed 2026-04-24 | engine-owned `CredentialProvider` and hardened `validateCredentialScope` landed per condition (b) sub-decision B-1 Option A. | `SaintFreddy/agentic-engine` credentialScope-enforcement PR (see CF-0089..CF-0096). |
| `PG-10.1` | closed 2026-04-24 | `spawnToolSandboxWorker` forks a real Node child and `attachToolSandboxWorkerIpc` is shipped on `contracts/exports.json` per condition (b) sub-decisions B-2 and B-3 Option A. | `SaintFreddy/agentic-engine` toolSandboxWorker-fork PR (see CF-0089..CF-0096). |

### 0.1.2 Downstream posture

- Every Inherited Baseline item that cites Platform Gate as `passed` now
  reads against a reopened acceptance marker. Downstream Canon doc
  synchronization is handled by subsequent packets `PG-R2`
  (blueprint/footnote sync) and `PG-R3` (maturity-matrix / high-level
  architecture footnote sync); this packet is bounded to the Platform
  Gate spec itself plus the registry/graph/master-plan synchronization.
- The `PG-01` through `PG-10` exit-test catalog in §6 and the §7
  checklist continue to define the gate's pass conditions. The reopen
  does not redefine them; it reopens the P3.6 passage claim.
- Ordinary baton continuation was paused under `canon-now.md`
  `Baton state: stop — audit-reopen hold` while PG-01.1, PG-07.1, and
  PG-10.1 were open; all three sub-gates closed 2026-04-24 alongside
  the remaining reopen-resolution conditions (see CF-0089..CF-0099 in
  `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md`),
  so the baton is now in `Baton state: ready` pending plan-owner
  selection of the next bounded step.

## 1. Purpose

This pack defines the hard internal gate that must pass before public R1 release work is considered launchable.

It exists to:

- turn the accepted Platform Gate seam into a concrete blocking architecture gate,
- name the minimum primitives and package areas that must exist before transcript-native UX is allowed to ship,
- define executable exit tests and a human audit checklist for proving the substrate is real.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- Platform Gate pass/fail rules,
- required primitive set,
- forced package/service areas,
- exit-test catalog,
- human exit-audit checklist.

### Out of scope

- public release UX polish,
- exact repo-directory layout,
- vendor-specific infrastructure choices,
- Phase 4 release-by-release product contracts,
- recurring sync automation detail.

## 3. Gate rules

### 3.1 Hard-blocking rule

Platform Gate is a release blocker, not a milestone suggestion.
No public R1 work is considered releasable until this gate passes.

### 3.2 Substrate-proof rule

Passing the gate means the platform proves frozen context, source tracing, run identity, proof/delta/writeback semantics, and provenance continuity on real execution paths.
Mock-only demonstrations do not satisfy the gate.

### 3.3 One-path rule

The gate must be passed on the same shared substrate that later chat-native releases and Task Studio will use.
View-local backdoors, transcript-only shortcuts, or mode-private backends do not count.

### 3.4 Human-owned exit rule

Factory may prepare the artifact set, test matrix, and evidence, but final gate passage remains a human architecture/release decision recorded through the audit checklist.

## 4. Required primitive set

| Primitive | Must exist before gate pass | Why it is required |
| --- | --- | --- |
| Run substrate | First-class `Run` identity with frozen admission basis, lifecycle state, proof ref, and delta ref | Prevents answer-first or transcript-first execution truth |
| Evidence / context substrate | Explicit Evidence Pack and Context Pack freeze, inspect, and replay basis behavior | Proves compiled context is real and inspectable |
| Source-region tracing | Stable source refs plus addressable spans/regions reaching proof and result fields | Proves grounding is not summary theater |
| Branch / replay substrate | Checkpoints, branches, replay requests, replay lineage, and basis diffs | Proves alternate work lines are semantic, not transcript clones |
| Governance substrate | Authority Scope, Review, Approval Decision, and lane-local Writeback Proposal flow | Proves serious work is governable before public release |
| Provenance / event spine | Append-only event and lineage basis queryable by run, review, replay, and writeback refs | Proves continuity survives beyond transient UI state |
| Gateway substrate | Typed model and tool gateway contracts with scoped credentials and inspectable failures | Proves external adapters are governed and replaceable |
| Failure / audit substrate | Failed runs still emit inspectable failure basis, diagnostics refs, and terminal events | Proves the system remains debuggable under failure |
| Tenant / scope enforcement | Workspace and scope filters enforced on reads, execution, events, retrieval, and writeback | Proves shared substrate is safe enough to expose publicly |

## 5. Forced package / service areas

These are logical package areas that must become real before gate passage.
They do not prescribe final repo layout, but they do prescribe mandatory implementation seams.

| Forced area | Minimum responsibility | Must expose |
| --- | --- | --- |
| `pkg.shared-object-api` | Typed shared-environment object contracts and scoped object APIs | Run/Branch/Artifact/Proof/Delta/Review/Writeback refs and queries |
| `pkg.environment-control` | Admission, replay, branch, review, and monitor entrypoints | Query + command envelopes and control-plane dispatch |
| `pkg.context-compiler` | Ingestion, spanization, evidence assembly, memory/canon injection, freeze/replay basis | Evidence/Context pack lifecycle and compiler diagnostics |
| `pkg.event-provenance-spine` | Append-only event store and provenance materialization | Event publication, replayable cursors, lineage queries |
| `pkg.review-writeback` | Lane-local proposals, review flows, approval capture, apply orchestration | Review objects, approval decisions, writeback application results |
| `pkg.replay-compare` | Checkpoint capture, replay execution, compare/basis diff handling | Replay requests, basis diffs, replay lineage |
| `pkg.model-gateway` | Typed provider invocation normalization and usage/failure accounting | Model invocation request/result contracts |
| `pkg.tool-gateway-sandbox` | Typed tool execution, side-effect classification, scoped credentials, logs | Tool invocation request/result contracts and side-effect previews |
| `pkg.monitor-inspect` | Live monitor and inspector projections over authoritative objects/events | Event subscriptions, inspect queries, monitor summaries |

## 6. Exit-test catalog

| Test ID | Test | Pass condition | Protected seam / scenario |
| --- | --- | --- | --- |
| `PG-01` | Frozen-context exact replay | A completed run can be replayed from frozen packs and input refs without provider transcript continuity | `SS-01`, `SS-10`, `GS-03`, `EC-10` |
| `PG-02` | Source-region traceability | Proof/result fields link to stable source-region refs that remain inspectable after execution | `SS-01`, `GS-01`, `GS-02` |
| `PG-03` | Run identity independence | Losing provider-side transcript continuity does not erase run/proof/delta identity or inspectability | `SS-02`, `SS-10`, `EC-10` |
| `PG-04` | Branch / replay semantic continuity | Forking from a checkpoint creates new branch/run records with explicit lineage and no transcript clone substitute | `SS-07`, `GS-04`, `EC-01` |
| `PG-05` | Lane-separated writeback governance | Artifact approval and canon rejection can happen separately without collapsing lanes or mutating durable state silently | `SS-04`, `SS-08`, `GS-07`, `GS-13`, `EC-03` |
| `PG-06` | Typed event-spine continuity | Run, review, approval, replay, and writeback events stream with stable refs and resumable cursors | `SS-02`, `SS-08`, `SS-10` |
| `PG-07` | Gateway contract discipline | Model and tool execution use typed contracts, scoped credentials, and inspectable failure results | P3.1-P3.4 boundary locks |
| `PG-08` | Failure inspectability | Failed execution still emits terminal run state, proof/failure basis, delta state, and diagnostics refs | `PI-10`, `RC-08` |
| `PG-09` | Scope and tenancy enforcement | Retrieval, inspect queries, monitor streams, and writeback actions reject out-of-scope access | P3.1 identity/tenancy baseline |
| `PG-10` | No direct UI-to-worker backdoor | User-initiated work only enters through environment/control APIs; direct worker RPC is absent or blocked | P3.4 no-direct-UI-worker-RPC rule |

## 7. Exit-audit checklist

> Gate passed. The following checklist is kept as the human-owned audit
> record. Confirmed at P3.6 acceptance.
>
> Gate reopened — audit-cited contradiction event 2026-04-18. The prior
> `Gate passed` line above is preserved as append-only history per
> `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A,
> recorded 2026-04-23). Sub-gates PG-01.1 / PG-07.1 / PG-10.1 all
> closed 2026-04-24 (see §0.1.1 for closure evidence); under DEC-RO-0f
> Option A's append-only-history discipline, this §7 audit-checklist
> header preserves `Gate passed` as prior-state history and does NOT
> revert to that marker. See §0.1 for the full reopen record and
> successor-checkpoint reference.

The gate may pass only when human review can answer every line below with “yes”.

1. The required primitive set in Section 4 exists on the shared substrate rather than in view-local stubs.
2. The forced package/service areas in Section 5 are implemented as real seams, even if final repo layout is still provisional.
3. `PG-01` through `PG-10` have executable evidence, not narrative claims only.
4. Evidence/context freeze and replay do not depend on provider transcript continuity.
5. Source-region tracing reaches proof and inspection surfaces.
6. Review, approval, and writeback remain lane-local and attributable.
7. Event/provenance queries are sufficient to reconstruct run, replay, review, and apply history.
8. Model and tool gateways use typed requests/results with scoped credentials and inspectable failures.
9. No forbidden shortcut has been knowingly reintroduced, especially transcript truth, silent proposal application, second-stack drift, or app-private ontology drift.
10. Human architecture/release owners agree the substrate is strong enough for public R1 work to proceed.

## 8. Blocking failure classes

| Failure class | Meaning |
| --- | --- |
| `gate.missing_primitive` | One or more required primitives from Section 4 does not exist or is only simulated |
| `gate.transcript_truth_dependency` | Run continuity, replay, or truth still depends on provider transcript state |
| `gate.untraceable_source_basis` | Source-region traceability does not reach proof or inspectable result fields |
| `gate.governance_bypass` | Review/approval/writeback can be bypassed or lane separation collapses |
| `gate.untyped_boundary` | API, IPC, gateway, or event boundaries still rely on ad hoc blobs or implicit semantics |
| `gate.provenance_gap` | Events or lineage are insufficient to reconstruct consequential history |
| `gate.scope_or_tenancy_leak` | Scope filtering or tenant isolation fails on reads, execution, or eventing |
| `gate.audit_incomplete` | Required tests or human audit evidence are missing |

## 9. Downstream implications

### 9.1 For P3.6 architecture sync

*(Resolved - P3.6 sync pass accepted; gate confirmed as final Phase 3 lock.)*

- the sync pass should treat this gate as the final Phase 3 lock and look for canon, seam, scenario, grammar, or shortcut regressions against it.

### 9.2 For Phase 4 release doctrine

*(Resolved - P4.1-P4.9 all inherit these primitives and package areas.)*

- Platform Gate and later release packs should assume these primitives and package areas already exist rather than reopening the pre-R1 substrate question.

### 9.3 For Phase 6 repo/package planning

*(Resolved - P6.2-P6.6 packets map forced areas to concrete execution packets.)*

- repo/package work should map these forced areas into concrete packages and services without collapsing them into transcript- or view-owned code.

## 10. Review notes

Human review should confirm that this gate:

- is truly blocking before R1,
- proves the substrate on real execution paths,
- makes required primitives, forced package areas, and tests concrete,
- leaves no ambiguity about what would fail the prelaunch gate.
