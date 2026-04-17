# Phase 3 context compiler / retrieval / memory / canon topology
Version: 1.0
Status: Accepted
Task: P3.2 — Context compiler / retrieval / memory / canon topology
Artifact ID: arch.phase3-context-compiler-topology.v1
Architecture scope: Accepted subsystem topology for spans, ingestion, evidence-vs-context distinction, staged retrieval, memory/canon injection, freeze/replay/diff, and recovery/compaction behavior

## 0. Convergence status (Phase 4+ update)

This topology was accepted as P3.2 and defines the context compiler as the
authoritative subsystem for evidence/context separation, memory/canon injection,
freeze/replay/diff, and recovery behavior.

As of Phase 4+ convergence:
- P3.3 (data storage/provenance) and P3.4 (API/event contracts) are accepted
  and map their storage, index, and event shapes directly to the §4 component
  topology and §5 object model.
- P3.5 (Platform Gate) exit tests PG-01 and PG-02 are the executable gate
  proofs for §8 freeze/replay behavior and §6 stage 4-9 (evidence assembly
  through freeze).
- P4.4 (R2 Context Chat), P4.5 (R3 Branch / Visual Thinker), and P4.9
  (R7 Commissioning Bridge) contract packs are accepted and reference this
  topology as their context-control authority rather than inventing view-local
  compiler behavior.
- P5.5 (Task Studio surface and lifecycle) and P5.6 (Task Studio V1 scope)
  treat §8 exact-freeze and §7 canon-injection order as substrate assumptions
  rather than Task Studio-private behavior.
- Phase 6 context-control and branch-replay packets (P6.2 R2, P6.3 R3) have
  grounded the §4 retrieval planner, evidence assembler, and pack freezer
  components in concrete execution packets.

The §3-§9 subsystem specification below is kept verbatim as the accepted
authority. §10 downstream implications are kept as the original intent record;
convergence outcomes are noted here.

## 1. Purpose

This pack defines the context compiler as a first-class subsystem.

It exists to:

- make source ingestion, evidence assembly, and context compilation explicit runtime stages,
- define how memory and canon enter compiled context without becoming hidden sludge,
- define how freeze, replay, diff, and recovery work without relying on transcript continuity.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- source ingestion and normalization topology,
- span and region addressing,
- evidence vs context separation,
- staged retrieval and injection order,
- freeze, replay, diff, recovery, and compaction behavior.

### Out of scope

- concrete storage schemas and index layouts,
- event payload formats,
- UI composition for context-editing surfaces,
- provider-specific parsing implementations,
- benchmark thresholds and scoring rules.

## 3. Subsystem rules

### 3.1 Source / evidence / context separation rule

Sources are ingested and normalized first.
Evidence Packs select admissible support material from those sources.
Context Packs compile the full runtime package, which may include evidence, memory, canon, policy, authority, and runtime constraints.

### 3.2 Staged-retrieval rule

Retrieval is staged rather than one-shot.
The compiler must distinguish candidate retrieval, evidence admission, and final context packing.

### 3.3 Explicit-injection rule

Memory and canon enter only through explicit scoped injection stages.
They may influence context, but they do not silently rewrite Evidence Packs or frozen replay bases.

### 3.4 Freeze-first replay rule

Replay and compare operate on frozen snapshots, pack lineage, and versioned source bases.
Transcript similarity is never sufficient replay evidence.

### 3.5 User-pin and exclusion preservation rule

Pinned evidence, explicit exclusions, and frozen pack bases survive compaction, replay, and diff unless the user or a new governing object changes them explicitly.

## 4. Subsystem topology

| Component | P3.1 runtime plane | Responsibilities | Emits / persists |
| --- | --- | --- | --- |
| Source ingest coordinator | Control service + worker plane | Admit uploaded or linked sources, assign source identity, queue normalization work, track version/freshness state | Source admission jobs, source identity records |
| Parser and normalizer pipeline | Worker plane | Parse documents/files/URLs, extract structure and metadata, normalize content for downstream indexing and region addressing | Normalized source payloads, parse status, structural metadata |
| Span and region mapper | Worker plane + data plane | Create stable addressable spans/regions over normalized sources, preserve source-region lineage, support excerpt references | Region maps, span indexes, citation anchors |
| Retrieval indexes | Data plane | Maintain lexical, semantic, metadata, and version-aware lookup structures over sources, artifacts, memory, and canon | Search/vector/materialized retrieval indexes |
| Retrieval planner | Worker plane | Decide which retrieval stages to run from objective, contract, branch state, packs, and policy | Retrieval plan, candidate sets, retrieval diagnostics |
| Evidence assembler | Worker plane | Build or refresh Evidence Packs from pinned items, retrieved candidates, role labels, and exclusions | Evidence Pack drafts, inclusion/exclusion report |
| Memory injector | Worker plane | Retrieve active Memory Objects by scope, freshness, and relevance after evidence assembly | Selected memory refs plus inclusion reasons |
| Canon injector | Worker plane | Retrieve Canon Objects by scope and mode (`consume-only`, `challenge-allowed`, or `propose-only`) after memory selection | Selected canon refs plus constraint notes |
| Context compiler coordinator | Worker plane | Compile the final Context Pack from contract/objective, evidence, memory, canon, branch overlays, authority, policy, tools, and runtime parameters | Context Pack draft plus compilation report |
| Pack freezer and versioner | Control service + data plane | Freeze admitted Context Packs and Evidence Packs, persist pack lineage, attach input snapshots for runs and replay | Frozen pack snapshots, lineage refs, input snapshot refs |
| Replay / diff service | Worker plane | Reconstruct exact or updated-basis runs, compare pack variants, surface basis deltas | Replay requests, pack diffs, basis-comparison reports |
| Recovery and compaction jobs | Worker plane | Compact oversized packs, recover from partial ingest/index failures, and preserve usable frozen basis on failure | Compaction results, recovery reports, blocked-stage diagnostics |

## 5. Object separation and compiler outputs

| Object | Contains | Explicitly excludes | Produced by |
| --- | --- | --- | --- |
| Source Reference | Source identity, locator, version/freshness, trust metadata | Retrieval decisions, memory/canon injection, policy snapshot | Source ingest coordinator |
| Span / region map | Addressable source regions and lineage anchors | Evidence admission, summary prose, context policy | Span and region mapper |
| Evidence Pack | Admitted evidence items, source roles, pinned items, exclusions, selection policy | Hidden memory, canon, tool budget, authority grants | Evidence assembler |
| Context Pack | Contract/objective snapshot, Evidence Pack snapshot, selected memory, selected canon, branch overlays, authority/policy/tool/runtime parameters, inclusion/exclusion report | Transcript-only residue, hidden provider state, implicit write authority | Context compiler coordinator |
| Memory selection set | Active Memory Object refs plus inclusion reasons | Accepted truth claims, writeback decisions | Memory injector |
| Canon selection set | Active Canon Object refs plus consume/challenge notes | General memory, hidden writeback, transcript lore | Canon injector |
| Compilation report | Token/fit diagnostics, inclusion/exclusion reasons, blocked stages, compaction notes | Durable object truth on its own | Context compiler coordinator |

## 6. Staged compilation pipeline

| Stage | Inputs | Operation | Outputs |
| --- | --- | --- | --- |
| 1. Admission | objective, contract, branch ref, explicit sources, user pins/exclusions, authority seed | Validate minimum inputs and create a compiler request | Compiler request record |
| 2. Ingestion and normalization | admitted source refs or uploads | Parse, normalize, version, and attach structural metadata | Normalized source set |
| 3. Spanization | normalized source set | Build stable region IDs and excerpt anchors | Span / region map |
| 4. Candidate retrieval | objective, contract, branch state, retrieval policy, normalized indexes | Gather candidate source/artifact/memory/canon refs before admission into packs | Candidate sets plus retrieval diagnostics |
| 5. Evidence assembly | candidate sources, pinned items, exclusions, source-role rules | Produce or refresh the Evidence Pack and inclusion/exclusion report | Evidence Pack draft |
| 6. Memory injection | Evidence Pack, scope rules, freshness/status filters | Select explicit Memory Objects and record why they were included or rejected | Memory selection set |
| 7. Canon injection | Evidence Pack, Memory selection set, canon mode, scope rules | Select Canon Objects and record consume/challenge constraints | Canon selection set |
| 8. Context compilation | contract/objective snapshot, Evidence Pack, memory, canon, authority, policy, tools, runtime budget | Assemble the final Context Pack and report token fit / overflow / blocked reasons | Context Pack draft + compilation report |
| 9. Freeze and admission | Context Pack draft, Evidence Pack draft, input snapshot policy | Freeze pack snapshots, attach lineage refs, and hand back admitted inputs for the Run | Frozen pack refs and input snapshot refs |

## 7. Memory and canon injection order

| Injection stage | Selection basis | Hard rules | Result |
| --- | --- | --- | --- |
| Evidence before memory | Explicit sources, retrieval candidates, pins, exclusions | Evidence admission must not be silently rewritten by memory hits | Stable evidence basis |
| Memory before canon | Scope, freshness, status, relevance, contradiction/supersession state | Hidden memory injection after freeze is forbidden; suspended or retired memory does not inject | Explicit memory selection set |
| Canon after memory | Scope, acceptance state, consume/challenge mode, dependency notes | Canon constrains context only through explicit selected refs and mode notes; canon does not silently mutate memory | Explicit canon selection set |
| Policy and authority after canon | Authority Scope, policy bindings, tool/model availability, runtime budget | Authority is a separate injected boundary, not part of evidence or canon | Final compile constraints |

## 8. Freeze / replay / diff behavior

| Mode | Basis | Required behavior | Output |
| --- | --- | --- | --- |
| Exact freeze | Frozen Evidence Pack + Context Pack + input snapshot refs | Preserve source versions, selections, memory/canon refs, authority, and branch lineage exactly | Replayable admitted basis |
| Exact replay | Frozen pack refs and frozen source versions | Reconstruct a new Run over the same admitted basis without relying on transcript state | New Run/Proof/Delta with replay lineage |
| Updated-source replay | Prior pack refs plus refreshed source versions | Re-run retrieval/compile with the same pack policy but new source versions and explicit diff notes | New Run plus basis-diff report |
| Branch diff | Two pack or branch bases | Compare evidence, memory, canon, authority, and policy differences explicitly | Pack-diff / basis-diff report |
| Compile diff | Two Context Pack snapshots | Surface inclusion, exclusion, compaction, and budget differences at pack level | Context diff report |

## 9. Recovery and compaction behavior

| Condition | Required behavior | User-visible effect |
| --- | --- | --- |
| Source parse failure | Preserve source identity, mark parse status, and continue only if policy allows partial evidence assembly | Compilation report shows blocked or partial source basis explicitly |
| Missing or stale index | Rebuild or fall back to slower retrieval path; do not pretend coverage is unchanged | Retrieval diagnostics and possible degraded-confidence note |
| Token / budget overflow | Compact only non-pinned background material first; preserve pins, exclusions, and governing snapshots | Compilation report shows what was compacted, summarized, or dropped |
| Memory conflict or stale memory | Exclude conflicted/suspended memory from injection and surface the exclusion reason | Memory inclusion/exclusion report records the conflict |
| Canon challenge or contradiction | Keep accepted canon refs explicit and mark challenge mode; unresolved contradiction remains explicit | Canon constraint notes and contradiction items remain visible |
| Replay basis invalid | Refuse exact replay and require updated-basis replay or manual repair | Replay request returns blocked basis with explicit reason |
| Partial stage failure after freeze preparation | Preserve the last successful frozen objects and failure diagnostics instead of discarding all state | Recovery report plus resumable or branchable basis |

## 10. Downstream implications

### 10.1 For P3.3 and P3.4

*(Resolved - P3.3 data storage and P3.4 API/event spec accepted; both map
to §4 components and §5 objects.)*

- storage, index, provenance, and API/event specs should map directly to these compiler components, stages, and frozen outputs.

### 10.2 For P3.5 Platform Gate

*(Resolved - PG-01 through PG-04 gate tests confirm §8 freeze/replay and
§6 evidence assembly stages. Gate passed at P3.6.)*

- gate tests should verify frozen context reconstruction, source-region traceability, replay basis continuity, and explicit evidence/context separation.

### 10.3 For later release and Task Studio work

*(Resolved - P4.4 R2, P4.5 R3, P4.9 R7, P5.5-P5.6 Task Studio, and
P6.2-P6.3 implementation packets all accepted on this topology.)*

- R2 context control, R3 branching/replay, R7 preflight, and Task Studio context inspection should all project this subsystem rather than inventing view-local compiler behavior.

## 11. Review notes

> Review completed at acceptance (P3.2). The criteria below are kept as the
> original audit record; confirmed by P3.6 sync pass and downstream adoption.

Human review should confirm that this topology:

- makes the context compiler a real subsystem with explicit stages and outputs,
- preserves evidence/context separation and explicit memory/canon injection,
- gives freeze/replay/diff and recovery/compaction behavior one coherent baseline,
- avoids hidden context assembly and transcript-first continuity.
