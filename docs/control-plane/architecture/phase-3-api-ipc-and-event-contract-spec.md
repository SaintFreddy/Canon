# Phase 3 API / IPC / event contract spec
Version: 1.0
Status: Accepted
Task: P3.4 — API / IPC / event contract spec
Artifact ID: arch.phase3-api-ipc-event-contracts.v1
Architecture scope: Accepted boundary-contract baseline for APIs, internal IPC, gateway adapters, and shared event families across the platform

## 1. Purpose

This pack defines the typed message contracts across the accepted runtime boundaries.

It exists to:

- make the major process boundaries explicit before implementation and gate work,
- force query, command, job, adapter, and event traffic to carry first-class refs instead of transcript residue,
- keep live monitor, replay, approval, and writeback traffic on one coherent event spine.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- common message-envelope rules,
- boundary contracts across environment, control, workers, gateways, and UI subscriptions,
- shared event-family baseline,
- compatibility and failure semantics.

### Out of scope

- public SDK ergonomics,
- transport/vendor choices,
- exact protobuf/OpenAPI/JSON-schema files,
- queue and broker implementation choices,
- UI layout for event presentation.

## 3. Contract rules

### 3.1 Typed-envelope rule

Every API, IPC, gateway, and event message is versioned and typed.
Untyped prompt blobs or transcript snippets are not valid boundary contracts.

### 3.2 Command-query-event separation rule

Queries read scoped state.
Commands request admission, mutation, or lifecycle progress.
Events record append-only history and status transitions.

### 3.3 Ref-first rule

Cross-boundary messages carry object refs, pack refs, blob refs, and policy refs as the primary basis.
Large payload bodies may be attached only as explicit payload refs or bounded preview fields.

### 3.4 No-direct-UI-worker-RPC rule

Client projections do not call worker endpoints directly.
UI initiates work through environment/control APIs and observes worker progress through typed event or inspect-query contracts.

### 3.5 Compatibility rule

Additive fields are allowed within a schema version.
Breaking field, enum, or semantic changes require a new message type or a new major schema version.

## 4. Common envelope baseline

| Envelope type | Required fields | Used for |
| --- | --- | --- |
| Query envelope | `message_type`, `schema_version`, `correlation_id`, `actor_ref`, `workspace_ref`, `scope_ref`, `subject_refs?`, `query_payload` | Scoped reads and projections |
| Command envelope | `message_type`, `schema_version`, `correlation_id`, `actor_ref`, `workspace_ref`, `scope_ref`, `authority_scope_ref?`, `contract_ref?`, `idempotency_key`, `command_payload` | Admission, branching, approval, and writeback requests |
| Job envelope | `message_type`, `schema_version`, `job_id`, `causation_ref`, `priority`, `workspace_ref`, `frozen_input_refs`, `policy_refs?`, `deadline_hint?` | Control-service to worker-plane IPC |
| Gateway envelope | `message_type`, `schema_version`, `invocation_id`, `run_ref`, `workspace_ref`, `authority_scope_ref`, `payload_or_pack_refs`, `budget_policy_ref?`, `adapter_policy_ref?` | Worker-plane calls into model and tool gateways |
| Event envelope | `event_id`, `event_family`, `event_type`, `schema_version`, `emitted_at`, `workspace_ref`, `subject_refs`, `actor_ref?`, `causation_ref?`, `payload_ref?`, `sequence_ref` | Shared append-only event spine |

## 5. Boundary contract matrix

### 5.1 Client/app projection <-> environment shell API

| Contract family | Direction | Required refs / fields | Returns / effects |
| --- | --- | --- | --- |
| `ProjectionBootstrapQuery` | Client -> environment shell | actor/workspace/surface/app refs | Session bootstrap, routing, visible scopes, subscription cursors |
| `ScopedObjectQuery` | Client/app -> environment shell | typed object refs, scope filters, pagination | Object summaries, typed refs, projection-safe detail |
| `SearchBrowseQuery` | Client/app -> environment shell | workspace/scope refs, search text, retrieval mode | Search results, provenance-safe previews, continuation cursor |
| `AdmissionCommand` | Client/app -> control via environment shell | run-class intent, objective, pack refs, contract/authority refs when required | Accepted run/job refs plus initial events |
| `ReviewActionCommand` | Client/app -> review services via environment shell | review/proposal refs, decision payload, actor/role refs | Review/approval event emission and updated review state |

### 5.2 Environment shell API <-> execution control plane

| Contract family | Direction | Required refs / fields | Returns / effects |
| --- | --- | --- | --- |
| `RunAdmissionRequest` | Environment shell -> control plane | run class, objective, frozen input refs or upload handles, authority/contract refs as required | `run_ref`, `job_ref`, lifecycle events |
| `ReplayOrCompareRequest` | Environment shell -> control plane | prior run/pack/checkpoint refs, replay mode, target refs | New `run_ref` plus branch/replay events |
| `BranchForkRequest` | Environment shell -> control plane | parent branch ref, fork checkpoint ref, continuity anchors | New `branch_ref`, emitted branch events |
| `WritebackGovernanceRequest` | Environment shell -> control plane | `state_delta_ref`, lane target, review policy refs | Lane-specific `writeback_proposal_ref` plus review events |
| `MonitorSubscriptionRequest` | Environment shell -> event spine | cursor, subject filters, workspace/scope filters | Ordered event stream or resumable cursor |

### 5.3 Control service <-> worker plane IPC

| Contract family | Direction | Required refs / fields | Returns / effects |
| --- | --- | --- | --- |
| `RunExecutionJob` | Control service -> workers | frozen run/input refs, protocol/policy refs, deadline/priority | Terminal run result refs and lifecycle events |
| `ContextCompileJob` | Control service -> compiler workers | admitted source/evidence refs, memory/canon mode, optional memory/canon admission inputs or explicit lane-absence markers, runtime budget | Frozen pack refs plus compiler events |
| `ReplayDiffJob` | Control service -> replay workers | pack lineage refs, checkpoint refs, replay/diff mode | Replay result refs, basis-diff refs, lineage events |
| `ProofValidationJob` | Control service -> validation workers | run/proof/delta refs, verifier-slot refs | Validator result refs, proof update events |
| `ApplyProposalJob` | Review/apply services -> apply workers | writeback proposal ref, approval refs, lane policy refs | Apply result refs and writeback events |

Rules:

1. Control service may send explicit memory/canon admission inputs when environment-control admission supplies them.
2. Compiler workers consume supplied lane inputs; they do not author them.
3. When a lane input is not supplied, the job marks that lane absent explicitly.

### 5.4 Worker plane <-> model gateway

| Contract family | Direction | Required refs / fields | Returns / effects |
| --- | --- | --- | --- |
| `ModelInvocationRequest` | Worker -> model gateway | `run_ref`, `context_pack_ref`, output-schema ref, budget policy, provider capability preferences | Normalized structured output, usage metrics, adapter diagnostics |
| `ModelInvocationResult` | Model gateway -> worker | invocation id, normalized content/result refs, token/cost metrics, safety notes, failure code | Proof/delta assembly inputs and gateway events |

Rules:

1. Workers send compiled context-pack refs or bounded payload refs, not hidden conversation state.
2. Provider-specific transcript state is adapter-private and may not become product truth.
3. Gateway failures still return inspectable failure codes and diagnostics refs.

### 5.5 Worker plane <-> tool gateway and sandboxes

| Contract family | Direction | Required refs / fields | Returns / effects |
| --- | --- | --- | --- |
| `ToolInvocationRequest` | Worker -> tool gateway | `run_ref`, tool contract id, argument payload ref, side-effect class, authority scope, credential binding ref, dry-run flag | Typed tool result refs, side-effect preview refs, execution logs |
| `ToolInvocationResult` | Tool gateway -> worker | invocation id, exit/result code, typed outputs, side-effect report, retryability flag | Worker continuation inputs and gateway events |

Rules:

1. Side-effecting tools must declare side-effect class before execution.
2. Credential bindings are passed by scoped refs, never inline secrets.
3. Tool results remain typed outputs, not free-form transcript narration.

### 5.6 UI/live-monitor subscription contract

| Contract family | Direction | Required refs / fields | Returns / effects |
| --- | --- | --- | --- |
| `EventSubscriptionQuery` | Client -> environment/event spine | cursor, subject refs, event-family filters, visibility scope | Ordered event stream or snapshot + cursor |
| `InspectObjectQuery` | Client -> environment shell | run/proof/delta/review/proposal refs | Latest query-safe object state for inspectors and ledgers |
| `LiveMonitorProjectionEvent` | Event spine -> client projection | authoritative event ref plus monitor summary fields | Derived monitor update suitable for Timeline / Monitor views |

Live Monitor is a projection over the authoritative event spine.
It may summarize status, but it may not invent a second truth model separate from the stored events and objects.

## 6. Shared event-family baseline

| Event family | Representative event types | Required subject refs | Primary consumers |
| --- | --- | --- | --- |
| `run.lifecycle.v1` | `run.admitted`, `run.executing`, `run.completed`, `run.failed`, `run.cancelled` | `run_ref`, optionally `proof_bundle_ref`, `state_delta_ref` | Timeline, Live Monitor, audit, replay tools |
| `review.approval.v1` | `review.opened`, `review.partially_decided`, `review.resolved`, `approval.recorded`, `approval.superseded` | `review_ref`, `approval_decision_ref?`, `writeback_proposal_ref?` | Queue / Inbox, Ledger, audit |
| `branch.replay.v1` | `branch.forked`, `checkpoint.captured`, `replay.requested`, `replay.completed`, `compare.generated` | `branch_ref`, `checkpoint_ref?`, `run_ref?` | Timeline, Compare View, provenance graph |
| `writeback.proposal.v1` | `proposal.created`, `proposal.review_requested`, `proposal.approved`, `proposal.rejected`, `proposal.applied` | `writeback_proposal_ref`, `state_delta_ref`, `review_ref?` | Ledger, Queue / Inbox, apply workers |
| `compiler.context.v1` | `source.ingested`, `evidence.frozen`, `context.frozen`, `compaction.performed`, `compiler.blocked` | `evidence_pack_ref?`, `context_pack_ref?`, `source_ref?` | Context inspectors, Platform Gate, rebuild jobs |
| `gateway.execution.v1` | `model.invoked`, `model.failed`, `tool.started`, `tool.completed`, `tool.failed` | `run_ref`, gateway invocation refs | Console, Live Monitor, audit |
| `monitor.projection.v1` | `monitor.snapshot`, `monitor.stall_detected`, `monitor.recovered` | authoritative event refs plus `run_ref` | Live Monitor views only; derived, never sole truth |

## 7. Failure, cancellation, and compatibility semantics

| Concern | Required rule |
| --- | --- |
| Idempotency | Commands that may retry across network or queue boundaries carry an `idempotency_key` and must not create duplicate durable objects when retried safely |
| Cancellation | Cancellation is a typed command and terminal event, not the silent disappearance of a job or run |
| Partial failure | Gateway, worker, and apply failures emit explicit failure events and attach inspectable diagnostics refs |
| Ordering | Per-subject event order must be stable enough for replay/audit reconstruction; cross-subject consumers rely on causal refs rather than wall-clock only |
| Compatibility | Breaking contract changes require version bump and coexistence plan; consumers may not guess new semantics from old message types |

## 8. Downstream implications

### 8.1 For P3.5 Platform Gate

- gate checks should verify typed envelopes, no direct UI-to-worker RPC, explicit event families, and ref-first gateway/tool contracts.

### 8.2 For Phase 4 and later release work

- release packs should project these contracts into chat-native surfaces without inventing surface-private event or approval semantics.

### 8.3 For repo/package planning

- package and service seams should follow these boundary contracts instead of re-deriving architecture from file layout.

## 9. Review notes

Human review should confirm that this spec:

- makes the major API, IPC, adapter, and event boundaries explicit,
- keeps UI, workers, gateways, and approval flows on typed contracts,
- preserves one shared event spine without a second monitor-only truth model,
- prevents transcript blobs or app-private RPC from becoming the platform substrate.
