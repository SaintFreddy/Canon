import { runAndSourceRefs } from "../../shared-object-schemas/run-and-source/index.mjs"

const refField = Object.freeze({ type: "ref", nullable: false })
const optionalRefField = Object.freeze({ type: "ref", nullable: true })
const stringField = Object.freeze({ type: "string", nullable: false })
const refArrayField = Object.freeze({ type: "array", items: { type: "ref" }, default: [] })

export const RUN_LINEAGE_CONTRACT_VERSION = "1.0.0"

export const runLineageRefs = Object.freeze({
  runLifecycleEvent: "contract.event-provenance.run-lineage.lifecycle-event.v1",
  sourceResolutionEvent: "contract.event-provenance.run-lineage.source-resolution-event.v1",
  resumeContinuityEvent: "contract.event-provenance.run-lineage.resume-event.v1",
  runLineageQuery: "contract.event-provenance.run-lineage.query.v1",
})

export const runLifecycleEvent = Object.freeze({
  contract_ref: runLineageRefs.runLifecycleEvent,
  kind: "event_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.run,
    runAndSourceRefs.contextPackSnapshot,
    runAndSourceRefs.proofBundleSummary,
  ]),
  description:
    "Append-only run lifecycle event envelope for prepared, admitted, executing, and terminal R1 run state transitions.",
  required_fields: ["event_ref", "event_type", "run_ref", "thread_ref", "occurred_at"],
  fields: Object.freeze({
    event_ref: refField,
    event_type: Object.freeze({
      type: "string",
      enum: ["run_prepared", "run_admitted", "run_executing", "run_completed", "run_failed", "run_cancelled"],
    }),
    run_ref: refField,
    thread_ref: refField,
    input_snapshot_ref: optionalRefField,
    context_pack_ref: optionalRefField,
    proof_bundle_ref: optionalRefField,
    state_delta_ref: optionalRefField,
    occurred_at: stringField,
  }),
  invariants: Object.freeze([
    "Lifecycle events are append-only and reconstructable after provider continuity loss.",
  ]),
})

export const sourceResolutionEvent = Object.freeze({
  contract_ref: runLineageRefs.sourceResolutionEvent,
  kind: "event_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.sourceReference, runAndSourceRefs.run]),
  description:
    "Append-only source lineage event for attachments, admissions, exclusions, and source-chip citations.",
  required_fields: ["event_ref", "event_type", "run_ref", "source_ref", "occurred_at"],
  fields: Object.freeze({
    event_ref: refField,
    event_type: Object.freeze({
      type: "string",
      enum: ["source_attached", "source_included", "source_excluded", "source_cited"],
    }),
    run_ref: refField,
    source_ref: refField,
    source_region_ref: optionalRefField,
    lineage_reason: stringField,
    occurred_at: stringField,
  }),
})

export const resumeContinuityEvent = Object.freeze({
  contract_ref: runLineageRefs.resumeContinuityEvent,
  kind: "event_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.threadLine, runAndSourceRefs.run]),
  description:
    "Append-only continuity event for resume-basis generation and provider-continuity loss handling.",
  required_fields: ["event_ref", "event_type", "thread_ref", "occurred_at"],
  fields: Object.freeze({
    event_ref: refField,
    event_type: Object.freeze({
      type: "string",
      enum: ["resume_basis_generated", "provider_continuity_lost", "thread_resumed"],
    }),
    thread_ref: refField,
    prior_run_ref: optionalRefField,
    next_run_ref: optionalRefField,
    since_last_run_ref: optionalRefField,
    provider_continuity_required: Object.freeze({ type: "boolean", const: false }),
    occurred_at: stringField,
  }),
})

export const runLineageQuery = Object.freeze({
  contract_ref: runLineageRefs.runLineageQuery,
  kind: "query_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.run, runAndSourceRefs.threadLine]),
  description:
    "Typed lineage query over run lifecycle, source resolution, and resume continuity events.",
  required_fields: [],
  fields: Object.freeze({
    thread_ref: optionalRefField,
    run_ref: optionalRefField,
    event_types: Object.freeze({ type: "array", items: { type: "string" }, default: [] }),
    since_event_ref: optionalRefField,
    limit: Object.freeze({ type: "number", minimum: 1, maximum: 200 }),
  }),
  invariants: Object.freeze([
    "Lineage queries reconstruct state from append-only events rather than implicit transcript history.",
  ]),
})

export const runLineageContractCatalog = Object.freeze({
  package_id: "pkg.event-provenance-contracts.run-lineage",
  package_version: RUN_LINEAGE_CONTRACT_VERSION,
  contracts: Object.freeze({
    run_lifecycle_event: runLifecycleEvent,
    source_resolution_event: sourceResolutionEvent,
    resume_continuity_event: resumeContinuityEvent,
    run_lineage_query: runLineageQuery,
  }),
  event_groups: Object.freeze({
    run_lifecycle: runLifecycleEvent.contract_ref,
    source_resolution: sourceResolutionEvent.contract_ref,
    resume_continuity: resumeContinuityEvent.contract_ref,
  }),
})

export default runLineageContractCatalog
