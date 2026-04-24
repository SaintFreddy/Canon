import {
  runLineageRefs,
} from "../../../packages/event-provenance-contracts/run-lineage/index.mjs"

export const RUN_TRACE_SERVICE_VERSION = "1.0.0"

export const runTraceRefs = Object.freeze({
  publishRunLifecycle: "svc.event-provenance.run-trace.publish-run-lifecycle.v1",
  publishSourceResolution: "svc.event-provenance.run-trace.publish-source-resolution.v1",
  publishResumeContinuity: "svc.event-provenance.run-trace.publish-resume-continuity.v1",
  queryRunTrace: "svc.event-provenance.run-trace.query.v1",
})

export const publishRunLifecycle = Object.freeze({
  entrypoint_ref: runTraceRefs.publishRunLifecycle,
  kind: "provenance_route",
  accepts_contract_ref: runLineageRefs.runLifecycleEvent,
  description:
    "Append-only provenance route for prepared, admitted, executing, and terminal R1 run lifecycle events.",
  invariants: Object.freeze([
    "Lifecycle facts stay append-only and reconstructable after provider continuity loss.",
  ]),
})

export const publishSourceResolution = Object.freeze({
  entrypoint_ref: runTraceRefs.publishSourceResolution,
  kind: "provenance_route",
  accepts_contract_ref: runLineageRefs.sourceResolutionEvent,
  description:
    "Append-only provenance route for source attachment, inclusion, exclusion, and citation facts used by compact R1 inspection.",
  invariants: Object.freeze([
    "Source chips and compact inspection derive from stable source lineage rather than transcript-local guesses.",
  ]),
})

export const publishResumeContinuity = Object.freeze({
  entrypoint_ref: runTraceRefs.publishResumeContinuity,
  kind: "provenance_route",
  accepts_contract_ref: runLineageRefs.resumeContinuityEvent,
  description:
    "Append-only provenance route for resume-basis creation and provider-continuity-loss handling.",
  invariants: Object.freeze([
    "Resume continuity remains explicit and queryable even when provider continuity is absent.",
  ]),
})

export const queryRunTrace = Object.freeze({
  entrypoint_ref: runTraceRefs.queryRunTrace,
  kind: "provenance_query_route",
  accepts_contract_ref: runLineageRefs.runLineageQuery,
  description:
    "Typed lineage query route over run lifecycle, source-resolution, and resume-continuity events for R1 continuity reads.",
  invariants: Object.freeze([
    "Queries reconstruct trace state from append-only events instead of ambient chat history.",
  ]),
})

export const runTraceServiceCatalog = Object.freeze({
  service_id: "svc.event-provenance.run-trace",
  service_version: RUN_TRACE_SERVICE_VERSION,
  workspace_root: "services/event-provenance/run-trace/",
  package_dependencies: Object.freeze({
    run_lineage_contracts: runLineageRefs,
  }),
  routes: Object.freeze({
    publish_run_lifecycle: publishRunLifecycle,
    publish_source_resolution: publishSourceResolution,
    publish_resume_continuity: publishResumeContinuity,
    query_run_trace: queryRunTrace,
  }),
  notes: Object.freeze([
    "This service materializes the append-only R1 run-trace seam and does not introduce alternate truth stores.",
  ]),
})

export default runTraceServiceCatalog
