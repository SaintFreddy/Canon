const refField = Object.freeze({ type: "ref", nullable: false })
const optionalRefField = Object.freeze({ type: "ref", nullable: true })
const stringField = Object.freeze({ type: "string", nullable: false })
const optionalStringField = Object.freeze({ type: "string", nullable: true })
const booleanField = Object.freeze({ type: "boolean", nullable: false })
const refArrayField = Object.freeze({ type: "array", items: { type: "ref" }, default: [] })
const stringArrayField = Object.freeze({ type: "array", items: { type: "string" }, default: [] })

export const RUN_AND_SOURCE_SCHEMA_VERSION = "1.0.0"

export const runAndSourceRefs = Object.freeze({
  threadLine: "schema.shared-object.thread-line.v1",
  runInputSnapshot: "schema.shared-object.run-input-snapshot.v1",
  run: "schema.shared-object.run.v1",
  sourceReference: "schema.shared-object.source-reference.v1",
  contextPackSnapshot: "schema.shared-object.context-pack-snapshot.v1",
  proofBundleSummary: "schema.shared-object.proof-bundle-summary.v1",
})

export const threadLineSchema = Object.freeze({
  schema_ref: runAndSourceRefs.threadLine,
  object_family: "thread_line",
  description:
    "Continuity lane for familiar chat that links runs, artifacts, and branch overlays without becoming the consequential truth anchor.",
  required_fields: [
    "thread_id",
    "scope_ref",
    "participant_refs",
    "related_run_refs",
    "related_branch_refs",
    "related_artifact_refs",
    "status",
    "continuity_metadata",
  ],
  fields: Object.freeze({
    thread_id: stringField,
    line_id: optionalStringField,
    scope_ref: refField,
    participant_refs: Object.freeze({ type: "array", items: { type: "ref" }, min_items: 1 }),
    related_run_refs: refArrayField,
    related_branch_refs: refArrayField,
    related_artifact_refs: refArrayField,
    status: stringField,
    continuity_metadata: Object.freeze({
      type: "object",
      required_fields: [
        "latest_run_ref",
        "latest_resume_basis_ref",
        "since_last_run_ref",
        "provider_continuity_required",
      ],
      fields: Object.freeze({
        latest_run_ref: optionalRefField,
        latest_resume_basis_ref: optionalRefField,
        since_last_run_ref: optionalRefField,
        provider_continuity_required: Object.freeze({ ...booleanField, const: false }),
      }),
    }),
  }),
  invariants: Object.freeze([
    "Thread continuity may assist familiar chat UX but does not replace run identity.",
    "Provider-managed conversation state may not be the only continuity mechanism.",
    "Branch overlays stay linked explicitly rather than being inferred from transcript copies.",
  ]),
})

export const runInputSnapshotSchema = Object.freeze({
  schema_ref: runAndSourceRefs.runInputSnapshot,
  object_family: "run_input_snapshot",
  description:
    "Frozen request-side admission basis captured before execution so replay and audit do not depend on hidden transcript state.",
  required_fields: [
    "input_snapshot_ref",
    "thread_ref",
    "line_ref",
    "source_ref_ids",
    "user_turn_text",
    "captured_at",
  ],
  fields: Object.freeze({
    input_snapshot_ref: refField,
    thread_ref: refField,
    line_ref: optionalRefField,
    source_ref_ids: refArrayField,
    attachment_ref_ids: refArrayField,
    user_turn_text: stringField,
    objective_summary: optionalStringField,
    captured_at: stringField,
  }),
  invariants: Object.freeze([
    "The input snapshot is the durable launch basis for a later run.",
    "Rerun and resume flows keep the snapshot explicit instead of rebuilding it from provider transcript continuity.",
  ]),
})

export const runSchema = Object.freeze({
  schema_ref: runAndSourceRefs.run,
  object_family: "run",
  description:
    "Primary consequential execution unit behind every R1 assistant answer, with stable identity, frozen input basis, and explicit proof and delta links.",
  required_fields: [
    "run_id",
    "run_class",
    "thread_ref",
    "objective_spec",
    "input_snapshot_ref",
    "status",
    "proof_bundle_ref",
    "state_delta_ref",
  ],
  fields: Object.freeze({
    run_id: stringField,
    run_class: Object.freeze({
      type: "string",
      enum: ["synthesize", "extract"],
    }),
    thread_ref: refField,
    objective_spec: Object.freeze({ type: "object", allow_additional_fields: true }),
    input_snapshot_ref: refField,
    evidence_pack_ref: optionalRefField,
    context_pack_ref: optionalRefField,
    branch_ref: optionalRefField,
    contract_ref: optionalRefField,
    authority_scope_ref: optionalRefField,
    status: Object.freeze({
      type: "string",
      enum: ["prepared", "admitted", "executing", "completed", "failed", "cancelled"],
    }),
    proof_bundle_ref: refField,
    state_delta_ref: refField,
  }),
  invariants: Object.freeze([
    "Every consequential assistant answer resolves back to one run.",
    "Retry, replay, and rerun behavior creates a new run_id instead of mutating prior run truth in place.",
    "Terminal runs always retain proof and delta links even when the delta is empty.",
  ]),
})

export const sourceReferenceSchema = Object.freeze({
  schema_ref: runAndSourceRefs.sourceReference,
  object_family: "source_reference",
  description:
    "Stable environment-level source identity used for attachments, URLs, and cited source regions across provider changes and reruns.",
  required_fields: [
    "source_ref_id",
    "source_type",
    "locator",
    "scope_visibility",
    "freshness_state",
    "trust_state",
    "version_state",
    "provenance_summary",
  ],
  fields: Object.freeze({
    source_ref_id: stringField,
    source_type: stringField,
    locator: Object.freeze({ type: "object", allow_additional_fields: true }),
    scope_visibility: stringField,
    freshness_state: stringField,
    trust_state: stringField,
    version_state: stringField,
    provenance_summary: Object.freeze({ type: "object", allow_additional_fields: true }),
    source_region_refs: refArrayField,
  }),
  invariants: Object.freeze([
    "Source identity stays stable independently of any one thread or provider session.",
    "Source chips and citations must resolve to this substrate rather than decorative transcript-only references.",
  ]),
})

export const contextPackSnapshotSchema = Object.freeze({
  schema_ref: runAndSourceRefs.contextPackSnapshot,
  object_family: "context_pack_snapshot",
  description:
    "Frozen admitted-basis snapshot for an R1 answer, preserving explicit evidence, memory, canon, and authority inputs behind compact inspection.",
  required_fields: [
    "context_pack_id",
    "input_snapshot_ref",
    "frozen",
    "included_source_refs",
    "memory_lane",
    "canon_lane",
    "authority_scope_ref",
  ],
  fields: Object.freeze({
    context_pack_id: stringField,
    input_snapshot_ref: refField,
    evidence_pack_ref: optionalRefField,
    frozen: Object.freeze({ ...booleanField, const: true }),
    included_source_refs: refArrayField,
    excluded_source_items: Object.freeze({ type: "array", items: { type: "object" }, default: [] }),
    memory_lane: Object.freeze({
      type: "object",
      required_fields: ["basis_origin", "included_refs", "excluded_items"],
      fields: Object.freeze({
        basis_origin: Object.freeze({ type: "string", enum: ["explicit", "fallback", "absent"] }),
        included_refs: refArrayField,
        excluded_items: Object.freeze({ type: "array", items: { type: "object" }, default: [] }),
      }),
    }),
    canon_lane: Object.freeze({
      type: "object",
      required_fields: ["basis_origin", "mode", "included_refs", "excluded_items"],
      fields: Object.freeze({
        basis_origin: Object.freeze({ type: "string", enum: ["explicit", "fallback", "absent"] }),
        mode: optionalStringField,
        included_refs: refArrayField,
        excluded_items: Object.freeze({ type: "array", items: { type: "object" }, default: [] }),
      }),
    }),
    authority_scope_ref: refField,
    branch_ref: optionalRefField,
    compaction_notes: stringArrayField,
  }),
  invariants: Object.freeze([
    "Exact replay depends on this snapshot rather than hidden transcript state.",
    "Explicit-vs-fallback lane origin stays visible for later replay, audit, and R2 inheritance.",
  ]),
})

export const proofBundleSummarySchema = Object.freeze({
  schema_ref: runAndSourceRefs.proofBundleSummary,
  object_family: "proof_bundle_summary",
  description:
    "Compact proof substrate for R1 answers, preserving evidence, omissions, contradictions, and validator outcomes without collapsing into persuasive prose.",
  required_fields: [
    "proof_bundle_id",
    "run_ref",
    "evidence_refs",
    "uncertainty_items",
    "omission_items",
    "contradiction_items",
    "summary_sections",
    "lifecycle_state",
  ],
  fields: Object.freeze({
    proof_bundle_id: stringField,
    run_ref: refField,
    evidence_refs: refArrayField,
    uncertainty_items: Object.freeze({ type: "array", items: { type: "object" }, default: [] }),
    omission_items: Object.freeze({ type: "array", items: { type: "object" }, default: [] }),
    contradiction_items: Object.freeze({ type: "array", items: { type: "object" }, default: [] }),
    validator_result_refs: refArrayField,
    summary_sections: Object.freeze({ type: "array", items: { type: "string" }, min_items: 1 }),
    lifecycle_state: Object.freeze({
      type: "string",
      enum: ["collected", "reviewed", "accepted", "challenged"],
    }),
  }),
  invariants: Object.freeze([
    "Compact inspection remains traceable back to the same proof substrate later stages inherit.",
    "Proof payload stays distinct from UI narration and transcript convenience text.",
  ]),
})

export const runAndSourceSchemaCatalog = Object.freeze({
  package_id: "pkg.shared-object-schemas.run-and-source",
  package_version: RUN_AND_SOURCE_SCHEMA_VERSION,
  schema_refs: runAndSourceRefs,
  objects: Object.freeze({
    thread_line: threadLineSchema,
    run_input_snapshot: runInputSnapshotSchema,
    run: runSchema,
    source_reference: sourceReferenceSchema,
    context_pack_snapshot: contextPackSnapshotSchema,
    proof_bundle_summary: proofBundleSummarySchema,
  }),
  notes: Object.freeze([
    "This package is additive shared-object substrate for the R1 contracts_objects packet.",
    "Projection-only additions such as Message Block, Conversation Surface, Source Chip, and Resume Packet remain outside this schema-only package.",
  ]),
})

export default runAndSourceSchemaCatalog
