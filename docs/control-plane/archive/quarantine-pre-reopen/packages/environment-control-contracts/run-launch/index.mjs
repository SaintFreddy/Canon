import { runAndSourceRefs } from "../../shared-object-schemas/run-and-source/index.mjs"

const refField = Object.freeze({ type: "ref", nullable: false })
const optionalRefField = Object.freeze({ type: "ref", nullable: true })
const stringField = Object.freeze({ type: "string", nullable: false })
const refArrayField = Object.freeze({ type: "array", items: { type: "ref" }, default: [] })

export const RUN_LAUNCH_CONTRACT_VERSION = "1.0.0"

export const runLaunchRefs = Object.freeze({
  startConversationRunCommand: "contract.environment-control.run-launch.start-conversation.v1",
  resumeConversationRunCommand: "contract.environment-control.run-launch.resume-conversation.v1",
  rerunConversationRunCommand: "contract.environment-control.run-launch.rerun-conversation.v1",
  runLaunchAccepted: "contract.environment-control.run-launch.accepted.v1",
  runLaunchRejected: "contract.environment-control.run-launch.rejected.v1",
})

export const startConversationRunCommand = Object.freeze({
  contract_ref: runLaunchRefs.startConversationRunCommand,
  kind: "command_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.threadLine,
    runAndSourceRefs.runInputSnapshot,
    runAndSourceRefs.sourceReference,
  ]),
  description:
    "Typed request for starting a new or continuing R1 chat turn as a bounded run without relying on ambient provider-managed transcript state.",
  required_fields: [
    "launch_mode",
    "run_class",
    "input_snapshot_ref",
    "thread_ref",
    "user_turn_text",
  ],
  fields: Object.freeze({
    launch_mode: Object.freeze({ type: "string", enum: ["new_thread", "continue_thread"] }),
    run_class: Object.freeze({ type: "string", enum: ["synthesize", "extract"] }),
    thread_ref: refField,
    input_snapshot_ref: refField,
    requested_source_ref_ids: refArrayField,
    user_turn_text: stringField,
    objective_spec: Object.freeze({ type: "object", allow_additional_fields: true }),
    authority_scope_ref: optionalRefField,
    contract_ref: optionalRefField,
    provider_session_hint: Object.freeze({ type: "string", nullable: true }),
  }),
  invariants: Object.freeze([
    "The provider session hint is optional and non-durable.",
    "Every accepted launch routes into a new run identity rather than mutating prior assistant truth.",
  ]),
})

export const resumeConversationRunCommand = Object.freeze({
  contract_ref: runLaunchRefs.resumeConversationRunCommand,
  kind: "command_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.threadLine,
    runAndSourceRefs.run,
    runAndSourceRefs.contextPackSnapshot,
  ]),
  description:
    "Typed request for continuing a thread from explicit shared refs after provider continuity is lost or intentionally absent.",
  required_fields: [
    "thread_ref",
    "prior_run_ref",
    "input_snapshot_ref",
    "since_last_run_ref",
  ],
  fields: Object.freeze({
    thread_ref: refField,
    prior_run_ref: refField,
    input_snapshot_ref: refField,
    since_last_run_ref: optionalRefField,
    latest_context_pack_ref: optionalRefField,
    requested_source_ref_ids: refArrayField,
    provider_session_hint: Object.freeze({ type: "string", nullable: true }),
  }),
  invariants: Object.freeze([
    "Resume behavior remains valid even when provider continuity is unavailable.",
  ]),
})

export const rerunConversationRunCommand = Object.freeze({
  contract_ref: runLaunchRefs.rerunConversationRunCommand,
  kind: "command_contract",
  shared_object_refs: Object.freeze([
    runAndSourceRefs.run,
    runAndSourceRefs.runInputSnapshot,
    runAndSourceRefs.contextPackSnapshot,
  ]),
  description:
    "Typed request for regenerate-or-rerun behavior that carries forward explicit frozen basis links while creating a new run identity.",
  required_fields: ["thread_ref", "prior_run_ref", "input_snapshot_ref", "rerun_reason"],
  fields: Object.freeze({
    thread_ref: refField,
    prior_run_ref: refField,
    input_snapshot_ref: refField,
    prior_context_pack_ref: optionalRefField,
    rerun_reason: stringField,
    requested_source_ref_ids: refArrayField,
  }),
  invariants: Object.freeze([
    "Rerun never reuses the prior run_id.",
  ]),
})

export const runLaunchAccepted = Object.freeze({
  contract_ref: runLaunchRefs.runLaunchAccepted,
  kind: "event_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.run, runAndSourceRefs.threadLine]),
  description:
    "Accepted launch receipt returned once the environment-control layer allocates a new run and dispatch path.",
  required_fields: ["run_ref", "thread_ref", "status", "dispatch_ref"],
  fields: Object.freeze({
    run_ref: refField,
    thread_ref: refField,
    status: Object.freeze({ type: "string", enum: ["prepared", "admitted"] }),
    dispatch_ref: refField,
    provider_session_hint_consumed: Object.freeze({ type: "boolean", nullable: false }),
  }),
})

export const runLaunchRejected = Object.freeze({
  contract_ref: runLaunchRefs.runLaunchRejected,
  kind: "event_contract",
  shared_object_refs: Object.freeze([runAndSourceRefs.threadLine]),
  description:
    "Explicit blocked launch result used when the request cannot be admitted without widening scope or violating the R1 continuity contract.",
  required_fields: ["thread_ref", "blocked_reason", "provider_session_required"],
  fields: Object.freeze({
    thread_ref: refField,
    blocked_reason: stringField,
    provider_session_required: Object.freeze({ type: "boolean", const: false }),
    missing_ref_ids: refArrayField,
  }),
})

export const runLaunchContractCatalog = Object.freeze({
  package_id: "pkg.environment-control-contracts.run-launch",
  package_version: RUN_LAUNCH_CONTRACT_VERSION,
  command_refs: Object.freeze({
    start_conversation_run: startConversationRunCommand.contract_ref,
    resume_conversation_run: resumeConversationRunCommand.contract_ref,
    rerun_conversation_run: rerunConversationRunCommand.contract_ref,
  }),
  result_refs: Object.freeze({
    accepted: runLaunchAccepted.contract_ref,
    rejected: runLaunchRejected.contract_ref,
  }),
  contracts: Object.freeze({
    start_conversation_run: startConversationRunCommand,
    resume_conversation_run: resumeConversationRunCommand,
    rerun_conversation_run: rerunConversationRunCommand,
    launch_accepted: runLaunchAccepted,
    launch_rejected: runLaunchRejected,
  }),
})

export default runLaunchContractCatalog
