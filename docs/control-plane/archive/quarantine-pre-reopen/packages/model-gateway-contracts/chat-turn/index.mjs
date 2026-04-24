import { runAndSourceRefs } from "../../shared-object-schemas/run-and-source/index.mjs"

const refField = Object.freeze({ type: "ref", nullable: false })
const optionalRefField = Object.freeze({ type: "ref", nullable: true })
const stringField = Object.freeze({ type: "string", nullable: false })
const optionalStringField = Object.freeze({ type: "string", nullable: true })
const refArrayField = Object.freeze({ type: "array", items: { type: "ref" }, default: [] })

export const CHAT_TURN_CONTRACT_VERSION = "1.0.0"

export const chatTurnRefs = Object.freeze({
  chatTurnRequest: "contract.model-gateway.chat-turn.request.v1",
  sourceAttribution: "contract.model-gateway.chat-turn.source-attribution.v1",
  chatTurnResult: "contract.model-gateway.chat-turn.result.v1",
  chatTurnFailure: "contract.model-gateway.chat-turn.failure.v1",
})

export const chatTurnRequest = Object.freeze({
  contract_ref: chatTurnRefs.chatTurnRequest,
  kind: "gateway_request_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.run,
    runAndSourceRefs.contextPackSnapshot,
    runAndSourceRefs.sourceReference,
  ]),
  description:
    "Typed provider-facing request for one bounded R1 assistant answer built over an already frozen admitted basis.",
  required_fields: ["run_ref", "thread_ref", "context_pack_ref", "turn_messages"],
  fields: Object.freeze({
    run_ref: refField,
    thread_ref: refField,
    context_pack_ref: refField,
    turn_messages: Object.freeze({ type: "array", items: { type: "object" }, min_items: 1 }),
    allowed_source_ref_ids: refArrayField,
    output_mode: Object.freeze({ type: "string", enum: ["assistant_message"] }),
    citation_mode: Object.freeze({ type: "string", enum: ["source_chip_required"] }),
    provider_session_hint: Object.freeze({ type: "string", nullable: true }),
    model_profile_ref: optionalRefField,
  }),
  invariants: Object.freeze([
    "The gateway consumes frozen admitted basis and may not rebuild truth from transcript continuity.",
    "Provider session hints may assist UX but do not become durable run truth.",
  ]),
})

export const sourceAttribution = Object.freeze({
  contract_ref: chatTurnRefs.sourceAttribution,
  kind: "gateway_result_component",
  shared_object_refs: Object.freeze([runAndSourceRefs.sourceReference]),
  description:
    "Normalized source-bearing attribution used for R1 source chips and compact inspection.",
  required_fields: ["source_ref", "message_segment_id", "attribution_role"],
  fields: Object.freeze({
    source_ref: refField,
    source_region_ref: optionalRefField,
    message_segment_id: stringField,
    attribution_role: stringField,
  }),
})

export const chatTurnResult = Object.freeze({
  contract_ref: chatTurnRefs.chatTurnResult,
  kind: "gateway_result_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.sourceReference]),
  description:
    "Normalized model-gateway result for a bounded chat turn, carrying output blocks, usage accounting, and source-bearing attribution.",
  required_fields: ["run_ref", "gateway_execution_ref", "output_blocks", "source_attributions"],
  fields: Object.freeze({
    run_ref: refField,
    gateway_execution_ref: refField,
    output_blocks: Object.freeze({ type: "array", items: { type: "object" }, min_items: 1 }),
    source_attributions: Object.freeze({ type: "array", items: { type: "ref" }, default: [] }),
    finish_reason: stringField,
    usage_accounting: Object.freeze({ type: "object", allow_additional_fields: true }),
    provider_session_receipt: optionalRefField,
  }),
  invariants: Object.freeze([
    "Gateway output remains a bounded run result candidate, not durable product truth by itself.",
  ]),
})

export const chatTurnFailure = Object.freeze({
  contract_ref: chatTurnRefs.chatTurnFailure,
  kind: "gateway_failure_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.run]),
  description:
    "Typed failure mapping for provider/model execution, including continuity-loss posture that still preserves run identity.",
  required_fields: ["run_ref", "failure_class", "retryable"],
  fields: Object.freeze({
    run_ref: refField,
    failure_class: stringField,
    retryable: Object.freeze({ type: "boolean", nullable: false }),
    provider_session_lost: Object.freeze({ type: "boolean", nullable: false }),
    normalized_message: stringField,
    provider_error_code: optionalStringField,
  }),
})

export const chatTurnContractCatalog = Object.freeze({
  package_id: "pkg.model-gateway-contracts.chat-turn",
  package_version: CHAT_TURN_CONTRACT_VERSION,
  contracts: Object.freeze({
    chat_turn_request: chatTurnRequest,
    source_attribution: sourceAttribution,
    chat_turn_result: chatTurnResult,
    chat_turn_failure: chatTurnFailure,
  }),
})

export default chatTurnContractCatalog
