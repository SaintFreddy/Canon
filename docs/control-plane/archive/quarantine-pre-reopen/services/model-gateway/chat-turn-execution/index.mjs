import {
  chatTurnRefs,
} from "../../../packages/model-gateway-contracts/chat-turn/index.mjs"

export const CHAT_TURN_EXECUTION_SERVICE_VERSION = "1.0.0"

export const chatTurnExecutionRefs = Object.freeze({
  executeChatTurn: "svc.model-gateway.chat-turn-execution.execute.v1",
  normalizeChatTurnFailure: "svc.model-gateway.chat-turn-execution.normalize-failure.v1",
})

export const executeChatTurn = Object.freeze({
  entrypoint_ref: chatTurnExecutionRefs.executeChatTurn,
  kind: "gateway_execution_route",
  accepts_contract_ref: chatTurnRefs.chatTurnRequest,
  success_contract_ref: chatTurnRefs.chatTurnResult,
  failure_contract_ref: chatTurnRefs.chatTurnFailure,
  description:
    "Typed model-gateway execution route for one bounded R1 assistant answer over a frozen admitted basis.",
  invariants: Object.freeze([
    "Gateway execution consumes frozen admitted-basis inputs and may not rebuild truth from transcript continuity.",
    "Provider session hints remain optional UX aids and do not become durable run truth.",
  ]),
})

export const normalizeChatTurnFailure = Object.freeze({
  entrypoint_ref: chatTurnExecutionRefs.normalizeChatTurnFailure,
  kind: "gateway_failure_route",
  accepts_contract_ref: chatTurnRefs.chatTurnFailure,
  emits_contract_ref: chatTurnRefs.chatTurnFailure,
  description:
    "Normalization route for provider/model failures that preserves run identity and provider-continuity-loss posture as typed gateway output.",
  invariants: Object.freeze([
    "Failure normalization does not erase the run or collapse provider loss into generic transcript noise.",
  ]),
})

export const chatTurnExecutionServiceCatalog = Object.freeze({
  service_id: "svc.model-gateway.chat-turn-execution",
  service_version: CHAT_TURN_EXECUTION_SERVICE_VERSION,
  workspace_root: "services/model-gateway/chat-turn-execution/",
  package_dependencies: Object.freeze({
    chat_turn_contracts: chatTurnRefs,
  }),
  routes: Object.freeze({
    execute_chat_turn: executeChatTurn,
    normalize_chat_turn_failure: normalizeChatTurnFailure,
  }),
  notes: Object.freeze([
    "This gateway module stays inside typed provider execution and normalization only.",
    "Shared-object authorship, review semantics, and app projection logic remain outside this service boundary.",
  ]),
})

export default chatTurnExecutionServiceCatalog
