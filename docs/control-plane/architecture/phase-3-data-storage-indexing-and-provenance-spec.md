# Phase 3 data / storage / indexing / provenance spec
Version: 1.0
Status: Accepted
Task: P3.3 — Data / storage / indexing / provenance spec
Artifact ID: arch.phase3-data-storage-provenance-spec.v1
Architecture scope: Accepted storage-class, event-stream, indexing, provenance, migration, invalidation, and rebuild baseline for the platform

## 1. Purpose

This pack defines the persistent data and provenance lanes required by the accepted runtime and compiler baselines.

It exists to:

- separate authoritative state from derived indexes and operational caches,
- make provenance and replay queryable without collapsing them into one generic store,
- define migration, invalidation, and rebuild rules before detailed API and gate work.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- storage-class catalog,
- authoritative vs derived state separation,
- event-stream families,
- graph/provenance rules,
- migration, invalidation, and rebuild behavior.

### Out of scope

- physical vendor choices,
- exact table or index schemas,
- queue implementation detail,
- backup/DR runbooks,
- benchmark thresholds.

## 3. Storage and provenance rules

### 3.1 Authoritative-vs-derived rule

Object truth lives in authoritative stores.
Search indexes, vector indexes, caches, and materialized provenance views are derived and rebuildable.

### 3.2 Lane-separation rule

Metadata, blobs, events, provenance, indexes, and secrets are distinct storage lanes.
One store may host multiple logical tables or collections, but the lanes remain explicit in the architecture.

### 3.3 Append-only lineage rule

Event history, proof lineage, approval history, and replay/branch lineage are append-only.
Corrections create new records and lineage edges rather than rewriting prior accepted history.

### 3.4 Tenant-and-scope rule

Every authoritative and derived lane is tenant-aware and scope-aware.
Cross-tenant leakage through caches, embeddings, or provenance lookups is forbidden.

### 3.5 Rebuildability rule

Any derived lane must declare its authoritative upstream basis and rebuild path.
If a derived lane becomes stale or corrupted, the system rebuilds from authoritative metadata, blobs, and events rather than inventing replacement truth.

## 4. Storage-class catalog

| Storage class | Truth status | Primary contents | Mutation model | Notes |
| --- | --- | --- | --- | --- |
| Relational metadata store | Authoritative | First-class object metadata, refs, lifecycle state, scope bindings, approvals, contracts, run headers, pack headers | Versioned row updates plus append-only history where required | Primary lookup plane for object identity and scoped queries |
| Object / blob store | Authoritative for large payloads | Normalized source payloads, artifact bodies, frozen pack snapshots, prompt assets, exported bundles, proof attachments | Immutable or revisioned objects; replacement by new object/version ref | Payloads are referenced from metadata, not treated as free-floating truth |
| Event store | Authoritative | Run lifecycle events, review/approval events, replay/branch events, writeback/apply events, ingestion/compiler events | Append-only | Backbone for replay, audit, and materialized provenance rebuilds |
| Provenance graph store | Derived-but-queryable materialization | Source->evidence, evidence->proof, run->artifact, branch/replay, delta->writeback lineage | Rebuilt from authoritative objects and events when necessary | May be backed by graph DB or equivalent indexed projection |
| Search index | Derived | Lexical and field-aware search over sources, artifacts, memory, canon, and object metadata | Reindexed from authoritative stores | Supports browse/query, never sole source of truth |
| Vector index | Derived | Embeddings for semantic retrieval over sources, artifacts, memory, and canon | Re-embedded / rebuilt from authoritative payloads | Tenant- and scope-filtered before retrieval use |
| Cache layer | Derived / ephemeral | Query caches, compilation caches, model-response caches where policy allows | Expiring, invalidatable | Never the only copy of accepted state |
| Secret / credential store | Authoritative for secrets only | Provider keys, integration credentials, token material, rotation metadata | Scoped create/rotate/revoke | Stores secret references for gateways; secrets do not live in metadata or blobs |

## 5. Authoritative and derived lane map

| Lane | Authoritative upstream | Typical consumers | Rebuild / invalidation trigger |
| --- | --- | --- | --- |
| Object metadata | Relational metadata store | Environment shell API, control service, workers, approval flows | Migrated in place with versioned backfills |
| Payload bodies | Object / blob store | Workers, artifact viewers, export flows, indexing jobs | New revision/object ref on payload change |
| Lifecycle and audit history | Event store | Replay, audit, live monitor, sync, provenance rebuild | Append-only; consumers checkpoint positions |
| Provenance queries | Metadata + blobs + event store | Proof views, artifact lineage, replay/diff tools | Rebuild when upstream events or lineage rules change |
| Lexical retrieval | Metadata + blobs | Browser / Library, retrieval planner, audit queries | Reindex when source/artifact payload or search schema changes |
| Semantic retrieval | Metadata + blobs | Retrieval planner, context compiler | Re-embed when payload, embedding model, or tenant policy changes |
| Ephemeral acceleration | Any allowed authoritative lane | Control service, workers | Invalidate on upstream change or policy/tenant boundary change |

## 6. Event-stream catalog

| Stream family | Producers | Consumers | Required retention / semantics |
| --- | --- | --- | --- |
| Run lifecycle stream | Control service, worker plane | Live Monitor, Timeline, replay tools, audit | Append-only; ordered per run and causally linked across child runs |
| Review / approval / writeback stream | Review services, apply workers | Queue / Inbox, Ledger, audit, writeback application | Append-only; lane-local decisions remain attributable |
| Ingestion / compiler stream | Ingest coordinator, compiler workers | Context diagnostics, Platform Gate checks, rebuild automation | Records parse status, compaction, freeze, replay-basis creation, and failures |
| Branch / replay stream | Control service, replay workers | Timeline, Compare View, provenance graph | Captures fork, replay, compare, and merge lineage explicitly |
| Operational / observability stream | Gateways, workers, schedulers | Console, ops telemetry, sync automation | May be sampled for metrics, but object-linked diagnostics remain queryable |

## 7. Indexing and provenance rules

### 7.1 Search and vector indexing

| Rule | Requirement |
| --- | --- |
| Index source | Search and vector jobs read from authoritative payloads plus metadata, never from transcript residue |
| Scope filter | Tenant and scope filtering happens before ranking or embedding-based retrieval results are admitted |
| Version awareness | Index records retain source/artifact version refs so retrieval can support frozen replay or updated-source reruns |
| Rebuild path | Search and vector indexes must be rebuildable from metadata + blobs without semantic data loss |

### 7.2 Provenance graph

| Rule | Requirement |
| --- | --- |
| Node basis | Graph nodes correspond to authoritative object IDs or stable source-region IDs |
| Edge basis | Edges materialize source->evidence, evidence->proof, run->artifact, run->delta, delta->writeback, branch/replay, and approval lineage |
| Query posture | Provenance must be queryable directly for proof, artifact lineage, and replay inspection without requiring raw event replay every time |
| Rebuild path | The graph is rebuildable from authoritative object metadata, frozen pack refs, and append-only events |

## 8. Migration, invalidation, and rebuild rules

| Trigger | Required action | Affected lanes |
| --- | --- | --- |
| Object-schema version change | Migrate metadata with explicit version backfill; preserve old refs until consumers are upgraded | Relational metadata, event consumers, provenance materialization |
| Source or artifact payload revision | Write new blob/object ref, update metadata head refs, invalidate search/vector entries for affected payload | Object store, metadata, search, vector, provenance |
| Ingestion/parser change | Re-run normalization/spanization for affected sources, then rebuild dependent indexes and provenance edges | Blob derivatives, span maps, search/vector, provenance |
| Compiler-basis rule change | Invalidate derived compilation caches and regenerate affected materialized diagnostics; do not rewrite frozen historical packs | Cache layer, compiler diagnostics, optional derived views |
| Embedding-model or search-schema change | Rebuild affected vector/search indexes from authoritative payloads with tenant-aware batching | Vector index, search index |
| Provenance rule change | Rebuild graph materialization from metadata + event store; keep source events and object refs intact | Provenance graph store |
| Secret rotation or integration rebinding | Rotate secret material in secret store and invalidate gateway/session caches; no metadata or blob rewrite of secrets | Secret store, cache layer, gateway credentials |

## 9. Downstream implications

### 9.1 For P3.4 and P3.5

- API/event contracts and Platform Gate checks should map directly to these authoritative vs derived lanes and stream families.

### 9.2 For Phase 4 and later implementation work

- release and repo work should treat provenance, event history, metadata, blobs, and indexes as separable lanes rather than a generic backend bucket.

### 9.3 For sync and regeneration work

- stale detection and regeneration should key off these explicit rebuild paths instead of ad hoc manual judgment.

## 10. Review notes

Human review should confirm that this spec:

- gives the platform explicit storage and provenance lanes,
- keeps authoritative state separate from derived indexes and caches,
- preserves tenant/scope boundaries across all storage classes,
- gives migration, invalidation, and rebuild behavior one coherent baseline.
