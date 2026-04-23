# Phase 3 Platform Gate spec and exit audit
Version: 1.1
Status: Reopened (formal reopen under Phase 4+ step 20, condition (f))
Task: P3.5 — Platform Gate spec + exit audit
Artifact ID: arch.phase3-platform-gate-spec.v1
Architecture scope: Accepted internal pre-R1 gate defining required primitives, forced package areas, exit tests, audit checklist, and blocking failure conditions

## 0. Gate status (Phase 4+ update)

### 0.1 Current status (post-reopen, Phase 4+ step 20)

The Platform Gate is formally **reopened** under Phase 4+ step 20 per the
recorded plan-owner decision for reopen condition (f) (Option A: formal
reopen with enumerated sub-gates). The prior P3.6 "Gate passed" state
recorded in §0.2 and §7 below is preserved as append-only history; it is
not being rewritten or removed.

Reopen scope (do not widen):
- Three enumerated sub-gates are open blockers pending remediation:
  - `PG-01.1` — frozen-context exact-replay sub-invariant (see §11.1).
  - `PG-07.1` — gateway contract discipline sub-invariant (see §11.2).
  - `PG-10.1` — no-direct-UI-to-worker backdoor sub-invariant (see §11.3).
- All other §6 exit tests and §7 checklist items remain on their prior
  P3.6-confirmed pass record; they are not reopened by this decision.
- Remediation packet queue:
  - `pkt.remediate-platform-gate-truth-status.v1` (this packet, control-plane
    alignment — goes first under Option A).
  - `pkt.remediate-*` engine-side packets for PG-01.1, PG-07.1, PG-10.1
    follow after this packet lands on main.
- Downstream artifacts (release contracts, sync passes, Phase 6/7 packs)
  remain accepted at their own acceptance time; a remediation-pending
  footnote is recorded in the registry/graph rather than cascading
  stale-markers across every PG-dependent artifact. Under Option A, the
  Platform Gate artifact itself carries the reopen marker; sub-gate
  remediation packets will drive any per-artifact stale propagation.

Authoritative references:
- `canon-now.md` condition (f).
- `canon-knowledgebase/post-reopen-decisions/condition-f.md` — Option A accepted.
- `AGENTIC_ENGINE_AUDIT_LOG.md` — cited failing invariants.
- `CANON_PLAN_IMPACT_REPORT.md` — governing rows for condition (f).

### 0.2 Prior P3.6 gate passage record (preserved, append-only)

This gate spec was accepted as P3.5. It defines the hard pre-R1 blocking
criteria that were proven before Phase 4 release work proceeded.

Gate passage confirmation (pre-reopen, historical record):
- `arch.phase3-architecture-sync-pass.v1` (P3.6) confirmed all §6 exit tests
  and §7 checklist items were met and declared no substrate drift before P4.1.
- `rel.chat-native-maturity-matrix.v1` (P4.1) inherited the §5 forced package
  areas without downgrade, confirming the substrate was real enough to bear
  the Phase 4 maturity floors.
- Phase 7 automation (`docs/control-plane/sync/`) now provides recurring
  gate-recheck automation (P7.4) that treats §6 and §8 as its regression basis.

The §6 exit-test catalog, §7 audit checklist, and §8 failure classes below
are kept verbatim as the authoritative gate record. The P3.6 "pass" state
recorded there is historical proof criteria as of P3.6 acceptance; the
enumerated sub-gates in §0.1 are the currently open blockers. The prior
checklist entries are not rewritten.

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

> Gate passed (historical, P3.6 acceptance — preserved append-only).
> The following checklist is kept as the human-owned audit record.
> Confirmed at P3.6 acceptance. Per §0.1, the gate is now formally
> reopened on the sub-gates PG-01.1, PG-07.1, and PG-10.1 enumerated
> in §11; the prior P3.6 "Gate passed" marker is not rewritten.

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
*(Post-reopen footnote — Phase 4+ step 20, condition (f), Option A: the
P3.6 "Gate passed" confirmation remains the historical sync record; the
sub-gates PG-01.1, PG-07.1, and PG-10.1 in §11 are the open blockers
that post-reopen remediation must clear. The P3.6 resolution is not
reopened — only the three enumerated sub-gates are.)*

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

## 11. Reopen sub-gates (Phase 4+ step 20, condition (f), Option A)

These sub-gates are the only §6/§7 invariants formally reopened under the
recorded plan-owner decision for condition (f). They narrow the prior
`PG-01`, `PG-07`, and `PG-10` exit tests; they do not widen scope to
additional invariants. Sub-gate pass criteria must be re-proven on the
same shared substrate required by §3.2 and §3.3.

| Sub-gate | Parent test | Reopened invariant | Pass condition | Remediation packet |
| --- | --- | --- | --- | --- |
| `PG-01.1` | `PG-01` | Frozen-context exact replay on the specific code paths cited by the audit log | A completed run on the cited paths replays from frozen packs and input refs with no dependency on provider transcript continuity and no non-deterministic fallback | `pkt.remediate-*` (engine-side, scheduled after this packet lands) |
| `PG-07.1` | `PG-07` | Gateway contract discipline on the specific gateway boundaries cited by the audit log | Model and tool invocations on the cited boundaries use typed contracts with scoped credentials; failure results are inspectable and reach the failure-audit substrate defined in §4 | `pkt.remediate-*` (engine-side, scheduled after this packet lands) |
| `PG-10.1` | `PG-10` | No direct UI-to-worker backdoor on the specific ingress paths cited by the audit log | User-initiated work on the cited ingress paths only enters through environment/control APIs; any direct worker RPC is absent or blocked and regression-tested | `pkt.remediate-*` (engine-side, scheduled after this packet lands) |

### 11.1 `PG-01.1` — frozen-context exact replay (reopened sub-invariant)

- Parent §6 test: `PG-01`.
- Parent §8 failure class: `gate.transcript_truth_dependency`.
- Audit-cited finding: see the audit log entry referenced by condition (f)
  in `AGENTIC_ENGINE_AUDIT_LOG.md`.
- Re-pass requires the cited run paths to replay from frozen `Evidence Pack`
  and `Context Pack` refs alone, without any implicit fallback to provider
  transcript state or to non-frozen inputs.

### 11.2 `PG-07.1` — gateway contract discipline (reopened sub-invariant)

- Parent §6 test: `PG-07`.
- Parent §8 failure class: `gate.untyped_boundary`.
- Audit-cited finding: see the audit log entry referenced by condition (f)
  in `AGENTIC_ENGINE_AUDIT_LOG.md`.
- Re-pass requires the cited gateway calls to go through typed
  request/result contracts with scoped credentials and to produce
  inspectable failure results that reach the §4 failure/audit substrate.

### 11.3 `PG-10.1` — no direct UI-to-worker backdoor (reopened sub-invariant)

- Parent §6 test: `PG-10`.
- Parent §8 failure class: `gate.governance_bypass`.
- Audit-cited finding: see the audit log entry referenced by condition (f)
  in `AGENTIC_ENGINE_AUDIT_LOG.md`.
- Re-pass requires the cited ingress paths to route only through
  environment/control APIs; any direct worker RPC path must be removed or
  blocked with a regression test that demonstrates the block.

### 11.4 Reopen procedural rules

- This reopen is bounded to sub-gates §11.1–§11.3. It does not reopen any
  other §6/§7 entries or any accepted Phase 4+ baseline decision.
- The prior P3.6 "Gate passed" state in §0.2 and §7 is preserved
  append-only; it must not be deleted or rewritten.
- Sub-gate clearance is recorded by append-only history in this file
  (additional §11.x entries noting the packet that cleared each sub-gate)
  together with downstream registry/graph updates.
- Until all three sub-gates clear, downstream work that relies on the
  cited invariants must treat the relevant paths as remediation-pending
  rather than assuming the prior P3.6 pass still covers them.
