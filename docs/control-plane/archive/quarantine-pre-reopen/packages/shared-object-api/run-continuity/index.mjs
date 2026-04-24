import { runAndSourceRefs } from "../../shared-object-schemas/run-and-source/index.mjs"

const refField = Object.freeze({ type: "ref", nullable: false })
const optionalRefField = Object.freeze({ type: "ref", nullable: true })
const stringField = Object.freeze({ type: "string", nullable: false })
const refArrayField = Object.freeze({ type: "array", items: { type: "ref" }, default: [] })

export const RUN_CONTINUITY_API_VERSION = "1.0.0"

export const runContinuityRefs = Object.freeze({
  threadContinuityView: "api.run-continuity.thread-view.v1",
  runInspectionView: "api.run-continuity.run-inspection-view.v1",
  resumeContinuityView: "api.run-continuity.resume-view.v1",
  rerunPlanView: "api.run-continuity.rerun-plan.v1",
})

export const threadContinuityView = Object.freeze({
  view_ref: runContinuityRefs.threadContinuityView,
  kind: "shared_object_query_model",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.threadLine,
    runAndSourceRefs.run,
    runAndSourceRefs.sourceReference,
  ]),
  description:
    "Identity-preserving continuity view for a conversation thread that keeps run history, source history, and provider-loss posture explicit.",
  required_fields: [
    "thread_ref",
    "latest_run_ref",
    "run_history_refs",
    "source_ref_ids",
    "continuity_state",
    "provider_continuity_required",
  ],
  fields: Object.freeze({
    thread_ref: refField,
    latest_run_ref: optionalRefField,
    run_history_refs: refArrayField,
    source_ref_ids: refArrayField,
    continuity_state: stringField,
    provider_continuity_required: Object.freeze({ type: "boolean", const: false }),
  }),
  invariants: Object.freeze([
    "Thread continuity is queryable without treating the thread itself as the consequential truth object.",
    "Continuity survives model swaps and provider changes through shared refs.",
  ]),
})

export const runInspectionView = Object.freeze({
  view_ref: runContinuityRefs.runInspectionView,
  kind: "shared_object_query_model",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.run,
    runAndSourceRefs.contextPackSnapshot,
    runAndSourceRefs.proofBundleSummary,
    runAndSourceRefs.sourceReference,
  ]),
  description:
    "Compact inspection view that resolves one assistant answer back to the run, admitted-basis snapshot, proof summary, and cited sources behind it.",
  required_fields: [
    "run_ref",
    "context_pack_ref",
    "proof_bundle_ref",
    "source_ref_ids",
    "status",
  ],
  fields: Object.freeze({
    run_ref: refField,
    context_pack_ref: optionalRefField,
    proof_bundle_ref: optionalRefField,
    source_ref_ids: refArrayField,
    status: stringField,
    compact_sections: Object.freeze({
      type: "array",
      items: { type: "string" },
      default: ["sources", "admitted_basis", "proof"],
    }),
  }),
  invariants: Object.freeze([
    "Compact inspection stays anchored to authoritative shared-object refs.",
    "The view may stay compact, but it may not hide run identity or grounding.",
  ]),
})

export const resumeContinuityView = Object.freeze({
  view_ref: runContinuityRefs.resumeContinuityView,
  kind: "shared_object_query_model",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.threadLine,
    runAndSourceRefs.run,
    runAndSourceRefs.contextPackSnapshot,
  ]),
  description:
    "Resume basis for familiar chat continuation without requiring hidden provider transcript continuity.",
  required_fields: [
    "thread_ref",
    "latest_run_ref",
    "since_last_run_ref",
    "latest_context_pack_ref",
    "provider_continuity_required",
  ],
  fields: Object.freeze({
    thread_ref: refField,
    latest_run_ref: optionalRefField,
    since_last_run_ref: optionalRefField,
    latest_context_pack_ref: optionalRefField,
    provider_continuity_required: Object.freeze({ type: "boolean", const: false }),
    continuity_notes: Object.freeze({ type: "array", items: { type: "string" }, default: [] }),
  }),
  invariants: Object.freeze([
    "Resume continuity derives from thread, run, and context refs rather than one provider session token.",
  ]),
})

export const rerunPlanView = Object.freeze({
  view_ref: runContinuityRefs.rerunPlanView,
  kind: "shared_object_query_model",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.run,
    runAndSourceRefs.runInputSnapshot,
    runAndSourceRefs.contextPackSnapshot,
  ]),
  description:
    "Rerun plan showing how a new run will inherit prior frozen basis links while producing a new run identity.",
  required_fields: [
    "prior_run_ref",
    "input_snapshot_ref",
    "will_create_new_run_id",
  ],
  fields: Object.freeze({
    prior_run_ref: refField,
    input_snapshot_ref: refField,
    prior_context_pack_ref: optionalRefField,
    will_create_new_run_id: Object.freeze({ type: "boolean", const: true }),
    carried_source_ref_ids: refArrayField,
    rerun_reason: stringField,
  }),
  invariants: Object.freeze([
    "Regenerate or rerun behavior always creates a new run rather than mutating prior run truth in place.",
  ]),
})

export const runContinuityApiCatalog = Object.freeze({
  package_id: "pkg.shared-object-api.run-continuity",
  package_version: RUN_CONTINUITY_API_VERSION,
  shared_object_dependencies: Object.freeze(Object.values(runAndSourceRefs)),
  operations: Object.freeze({
    load_thread_continuity: threadContinuityView.view_ref,
    load_run_inspection: runInspectionView.view_ref,
    load_resume_continuity: resumeContinuityView.view_ref,
    plan_rerun_as_new_run: rerunPlanView.view_ref,
  }),
  views: Object.freeze({
    thread_continuity: threadContinuityView,
    run_inspection: runInspectionView,
    resume_continuity: resumeContinuityView,
    rerun_plan: rerunPlanView,
  }),
})

export default runContinuityApiCatalog
