import { runAndSourceRefs } from "../../shared-object-schemas/run-and-source/index.mjs"

const refField = Object.freeze({ type: "ref", nullable: false })
const optionalRefField = Object.freeze({ type: "ref", nullable: true })
const stringField = Object.freeze({ type: "string", nullable: false })
const optionalStringField = Object.freeze({ type: "string", nullable: true })
const refArrayField = Object.freeze({ type: "array", items: { type: "ref" }, default: [] })

export const ADMITTED_BASIS_CONTRACT_VERSION = "1.0.0"

export const admittedBasisRefs = Object.freeze({
  compileRunContextCommand: "contract.context-compiler.admitted-basis.compile-run-context.v1",
  admittedBasisRecord: "contract.context-compiler.admitted-basis.record.v1",
  compileRunContextResult: "contract.context-compiler.admitted-basis.result.v1",
})

export const compileRunContextCommand = Object.freeze({
  contract_ref: admittedBasisRefs.compileRunContextCommand,
  kind: "job_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.run,
    runAndSourceRefs.runInputSnapshot,
    runAndSourceRefs.sourceReference,
  ]),
  description:
    "Compiler request for freezing the R1 admitted basis from explicit inputs before model invocation.",
  required_fields: [
    "run_ref",
    "thread_ref",
    "input_snapshot_ref",
    "requested_source_ref_ids",
  ],
  fields: Object.freeze({
    run_ref: refField,
    thread_ref: refField,
    input_snapshot_ref: refField,
    requested_source_ref_ids: refArrayField,
    evidence_pack_ref: optionalRefField,
    explicit_memory_refs: refArrayField,
    explicit_canon_refs: refArrayField,
    authority_scope_ref: optionalRefField,
    branch_ref: optionalRefField,
    provider_session_hint: Object.freeze({ type: "string", nullable: true }),
    compaction_policy: optionalStringField,
  }),
  invariants: Object.freeze([
    "Explicit admitted inputs take precedence over fallback lane selection.",
    "Provider continuity hints are advisory only and never become the replay basis.",
  ]),
})

export const admittedBasisRecord = Object.freeze({
  contract_ref: admittedBasisRefs.admittedBasisRecord,
  kind: "record_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.contextPackSnapshot,
    runAndSourceRefs.sourceReference,
  ]),
  description:
    "Frozen admitted-basis record kept behind compact inspection and exact replay for one R1 run.",
  required_fields: [
    "admitted_basis_ref",
    "run_ref",
    "input_snapshot_ref",
    "context_pack_ref",
    "memory_lane",
    "canon_lane",
    "authority_scope_ref",
  ],
  fields: Object.freeze({
    admitted_basis_ref: refField,
    run_ref: refField,
    input_snapshot_ref: refField,
    context_pack_ref: refField,
    evidence_pack_ref: optionalRefField,
    included_source_ref_ids: refArrayField,
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
    compaction_notes: Object.freeze({ type: "array", items: { type: "string" }, default: [] }),
  }),
})

export const compileRunContextResult = Object.freeze({
  contract_ref: admittedBasisRefs.compileRunContextResult,
  kind: "job_result_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.contextPackSnapshot,
    runAndSourceRefs.proofBundleSummary,
  ]),
  description:
    "Compiler result exposing the frozen context-pack ref and compact admitted-basis summary needed by R1 inspection and replay.",
  required_fields: ["run_ref", "context_pack_ref", "admitted_basis_ref", "frozen"],
  fields: Object.freeze({
    run_ref: refField,
    context_pack_ref: refField,
    admitted_basis_ref: refField,
    frozen: Object.freeze({ type: "boolean", const: true }),
    compact_summary_sections: Object.freeze({
      type: "array",
      items: { type: "string" },
      default: ["sources", "memory", "canon", "authority"],
    }),
  }),
})

export const admittedBasisContractCatalog = Object.freeze({
  package_id: "pkg.context-compiler-contracts.admitted-basis",
  package_version: ADMITTED_BASIS_CONTRACT_VERSION,
  contracts: Object.freeze({
    compile_run_context: compileRunContextCommand,
    admitted_basis_record: admittedBasisRecord,
    compile_run_context_result: compileRunContextResult,
  }),
})

export default admittedBasisContractCatalog
