# Phase 3 high-level technical architecture baseline
Version: 1.0
Status: Accepted
Task: P3.1 — High-level technical architecture baseline
Artifact ID: arch.phase3-technical-architecture-baseline.v1
Architecture scope: Accepted runtime topology, process model, local/cloud split, layer boundaries, and identity/tenancy touchpoints for the platform baseline

## 1. Purpose

This pack turns the accepted semantic contracts into one explicit technical baseline.

It exists to:

- define the major runtime planes and process boundaries,
- choose a default local/cloud split without breaking later portability,
- keep engine, shared-environment, and app responsibilities explicit before deeper subsystem specs arrive.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- high-level runtime topology,
- process-family baseline,
- default local/cloud split,
- engine/environment/app boundary map,
- identity, scope, and tenancy touchpoints.

### Out of scope

- detailed compiler pipeline design,
- storage schema and indexing detail,
- event payload definitions,
- package/module layout,
- release-specific implementation blueprints.

## 3. Architecture baseline rules

### 3.1 Semantics-first boundary rule

Technical boundaries must preserve the accepted P2 object model.
Client views, workers, and storage may distribute responsibility, but they may not relocate truth into transcript state or app-private objects.

### 3.2 Hosted-default, portable-seam rule

The baseline product deployment is cloud-hosted for authoritative state and execution.
Local runtime remains a supported seam for later SDK, air-gapped, or BYOK-heavy variants, but it is not the default truth location.

### 3.3 Logical-boundary-over-microservice-count rule

The baseline defines logical runtime planes and process families first.
Initial deployment may begin as a modular control service plus worker pools, provided the logical boundaries stay explicit and splittable later.

### 3.4 Bounded-worker rule

Consequential execution, context compilation, replay, validation, and tool use run in bounded worker contexts rather than inside client views or ad hoc backend handlers.

### 3.5 One-event-spine rule

The platform uses one shared event and provenance spine for runs, approvals, branches, replays, and writeback.
This is not permission to add a second orchestration stack.

## 4. Runtime topology baseline

| Runtime plane | Primary layer owner | Responsibilities | Key inputs / outputs | Must not own |
| --- | --- | --- | --- | --- |
| Client projection runtime | App/domain projections over shared grammar | Render projection grammar, hold ephemeral UI state, collect user input, upload attachments, subscribe to run/event updates | Inputs: user actions, server state streams. Outputs: draft mutations, run/approval commands, file uploads | Authoritative run state, durable object truth, hidden transcript context |
| Environment shell API | Shared environment | Workspace/project/app/surface routing, search entry points, assignment/review inbox queries, integration-binding lookup, session bootstrap | Inputs: authenticated client requests. Outputs: scoped object queries, routing metadata, environment-level commands | Run execution, proof assembly, provider-managed transcript state |
| Execution control plane | Engine + shared-environment boundary | Commission/contract normalization, run admission, orchestration kickoff, replay/branch initiation, approval wait states, delta/writeback proposal creation | Inputs: run requests, contract/authority refs, trigger events. Outputs: run lifecycle events, proof/delta refs, review/apply requests | UI rendering, app-private semantics, direct object-store blobs as business truth |
| Worker plane | Engine | Bounded run workers, context compilation workers, validation/proof workers, replay/compare workers, apply workers | Inputs: frozen run snapshots, queue jobs, policy context. Outputs: proof, deltas, validator results, writeback side effects | Persistent UI session state, unbounded ambient authority |
| Model gateway | Engine | Provider adapters, capability negotiation, routing/fallback, token/cost accounting, normalized structured output | Inputs: compiled prompts/context packages. Outputs: normalized model responses, usage metrics, errors | Durable product state, view-specific semantics |
| Tool gateway and sandboxes | Engine | Typed tool adapter execution, side-effect classification, sandboxing, credential scoping, job tracking | Inputs: approved tool invocations. Outputs: typed tool results, side-effect previews, execution logs | Policy authorship, cross-tenant credential sharing |
| Data and provenance plane | Shared environment + engine persistence substrate | Relational metadata, object/blob storage, search/vector indexes, event store, provenance graph, caches | Inputs: accepted object writes and event append operations. Outputs: queryable object state, lineage, replay basis | UI-owned truth, provider transcript continuity |

## 5. Process model baseline

| Process family | Initial deployment bias | Responsibilities | Scaling posture |
| --- | --- | --- | --- |
| Client process | Browser or desktop shell per user session | Projection rendering, local drafts, upload preparation, event subscription | Scales with users; never authoritative |
| Control service | One modular server tier exposing environment and execution APIs | Auth/session handling, query composition, admission/preflight, orchestration dispatch, approval routing | Scales statelessly behind shared stores and queues |
| Worker pools | Separate bounded worker families by concern | Run execution, context compilation, validation/proof, replay/compare, writeback/apply | Scale independently by job class and latency/rigor profile |
| Gateway services | Model and tool adapter services or isolated worker classes | Provider normalization, tool execution, sandboxing, adapter retries, usage accounting | Scale independently; isolate failures and credentials |
| Data services | Managed stateful stores | Metadata, blobs, search/vector, event/provenance, caches | Scale by data class; durability and isolation prioritized over low-latency UI coupling |

Additional process rules:

1. Interactive requests enter through the control service, not directly through worker endpoints.
2. Long-running or approval-gated work continues through worker jobs plus event updates rather than held-open request threads.
3. Replay, compare, and background execution use the same run/worker/event model as interactive execution.
4. Tool and model adapters may be deployed separately for isolation, but they remain behind one engine-facing gateway contract.

## 6. Default local/cloud split

| Concern | Default locus | Why this is the baseline | Stable portability seam |
| --- | --- | --- | --- |
| Projection rendering and local draft state | Local client | Keeps interaction responsive and lets users shape commissions, packs, and views without making the client authoritative | Same grammar can be hosted in browser, desktop shell, or local dev runtime |
| Attachment capture and pre-upload preprocessing | Local client, then cloud ingestion | Files originate locally, but durable source identity and normalization must become shared and replayable | Local adapters may later handle trusted local-only ingestion before handoff |
| Authoritative object graph and event history | Cloud data plane | Shared continuity, collaboration, approvals, replay, and provenance require one authoritative source of truth | Air-gapped/local deployments can swap the storage backend without changing object contracts |
| Run orchestration and policy enforcement | Cloud control plane + workers | Consequential work, approvals, writeback, and auditability need centralized enforcement in the default product mode | The execution plane is explicitly separable for local runtime or private-cloud deployment later |
| Model and tool gateway execution | Cloud gateway by default | Centralizes provider adapters, credential isolation, and usage accounting | Tenant-scoped local or BYOK gateways remain possible through the same gateway contract |
| Search, vector retrieval, provenance, and event storage | Cloud data plane | Cross-run retrieval, branch/replay, and cross-app continuity depend on shared indexed state | Storage adapters preserve replaceability for later local or regulated deployments |

## 7. Engine / environment / app boundary map

| Layer | Owns in runtime terms | Representative services or planes | Must not absorb |
| --- | --- | --- | --- |
| Engine | Model gateway, tool gateway, worker execution runtime, context compilation core, validation/proof core, replay/variant execution core, policy evaluation core | Worker plane, model gateway, tool gateway, engine-side portions of the control service | Workspace/app routing, app-private surface semantics, transcript-owned truth |
| Shared environment | Workspace/project/app/surface participation, shared object APIs, approvals, assignments, writeback governance, artifact/memory/canon/query surfaces, tenancy boundaries | Environment shell API, shared portions of the control service, data/provenance plane | Provider-specific reasoning, domain-pack semantics, UI-only aliases as truth |
| App/domain projections | Release-specific and Task Studio projection flows, aliases, arrangement of shared grammar, app-local draft UX | Client projection runtime, app route handlers, surface composition | Shared object ownership, run execution, approval/persistence semantics |

## 8. Identity and tenancy touchpoints

| Touchpoint | Enforcement point | Objects or state affected | Baseline rule |
| --- | --- | --- | --- |
| Session authentication | Environment shell API | Actor identity, workspace membership, visible scopes | Every request enters with authenticated actor and workspace context before object lookup |
| Scope resolution on read | Environment shell API + data plane filters | Workspace, project, branch, app, personal overlays, integration bindings | Read access is scope-filtered before compiled context or browsing results are assembled |
| Run admission | Execution control plane | Commission, Contract, Authority Scope, Run | Admission snapshots actor, workspace, branch, contract, and authority refs before worker dispatch |
| Worker execution credentials | Worker plane + gateways | Tool credentials, provider credentials, integration bindings | Workers act through scoped service identities and tenant-scoped bindings; no cross-tenant credential reuse |
| Durable writeback application | Apply workers + approval services | Artifact, memory, canon, workflow, export lanes | Apply paths require lane-local proposals, review, and approval inside the tenant/scope boundary |
| Event streaming and observability | Event/provenance plane | Run events, approvals, branch/replay lineage, audit logs | Streams and audit views are tenant-filtered and object-ref-based; diagnostics do not bypass scope rules |
| Search and retrieval | Data plane + context workers | Source refs, artifacts, memory, canon, prior runs | Retrieval is tenant-aware and scope-aware before ranking or context packing occurs |

## 9. Architecture locks and non-goals

1. The client is never the authoritative store for runs, packs, artifacts, or approvals.
2. No release gets its own backend truth model; all projections enter through the same shared control and data planes.
3. Provider transcript state is not required for continuity, replay, or context compilation.
4. Repo/package layout is deferred; this pack defines runtime boundaries only.
5. Dedicated compiler, storage, API, and gate specs arrive in P3.2 through P3.5; this pack does not preempt their detail.

## 10. Downstream implications

### 10.1 For P3.2 through P3.5

- compiler, storage, IPC/event, and Platform Gate specs should refine these runtime planes and process families rather than inventing new top-level ones.

### 10.2 For Phase 4 release packs

- release contracts should assume one shared control plane, one shared data/provenance plane, and reusable grammar/client projections over them.

### 10.3 For Phase 6 repo/package planning

- repo and package layout should follow these runtime boundaries and service seams instead of dictating them.

## 11. Review notes

Human review should confirm that this baseline:

- gives the platform one coherent technical architecture story,
- preserves the accepted semantic contracts and bridge seams,
- keeps local/cloud flexibility without making the default product architecture ambiguous,
- avoids transcript-first, app-private, or repo-shape-driven architecture drift.
