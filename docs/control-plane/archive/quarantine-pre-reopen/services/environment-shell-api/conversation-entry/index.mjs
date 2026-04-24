import {
  runContinuityRefs,
} from "../../../packages/shared-object-api/run-continuity/index.mjs"
import {
  runLaunchRefs,
} from "../../../packages/environment-control-contracts/run-launch/index.mjs"

export const CONVERSATION_ENTRY_SERVICE_VERSION = "1.0.0"

export const conversationEntryRefs = Object.freeze({
  startConversationEntry: "svc.environment-shell-api.conversation-entry.start.v1",
  resumeConversationEntry: "svc.environment-shell-api.conversation-entry.resume.v1",
  rerunConversationEntry: "svc.environment-shell-api.conversation-entry.rerun.v1",
})

export const startConversationEntry = Object.freeze({
  entrypoint_ref: conversationEntryRefs.startConversationEntry,
  kind: "service_entrypoint",
  accepts_contract_ref: runLaunchRefs.startConversationRunCommand,
  result_contract_refs: Object.freeze([
    runLaunchRefs.runLaunchAccepted,
    runLaunchRefs.runLaunchRejected,
  ]),
  continuity_view_ref: runContinuityRefs.threadContinuityView,
  dispatch_target_ref: "svc.execution-control.run-dispatch.prepare-run.v1",
  description:
    "Typed environment-shell entrypoint for starting a bounded R1 conversation run while preserving thread continuity as projection-only state.",
  invariants: Object.freeze([
    "Conversation entry may consult continuity views but may not treat the thread as the consequential truth anchor.",
    "Accepted launches always hand off to execution-control dispatch rather than reaching workers or gateways directly.",
  ]),
})

export const resumeConversationEntry = Object.freeze({
  entrypoint_ref: conversationEntryRefs.resumeConversationEntry,
  kind: "service_entrypoint",
  accepts_contract_ref: runLaunchRefs.resumeConversationRunCommand,
  result_contract_refs: Object.freeze([
    runLaunchRefs.runLaunchAccepted,
    runLaunchRefs.runLaunchRejected,
  ]),
  continuity_view_ref: runContinuityRefs.resumeContinuityView,
  dispatch_target_ref: "svc.execution-control.run-dispatch.resume-run.v1",
  description:
    "Typed environment-shell entrypoint for continuing a thread from explicit shared refs after provider continuity loss or absence.",
  invariants: Object.freeze([
    "Resume continuity remains reconstructable from shared refs even when provider continuity is unavailable.",
  ]),
})

export const rerunConversationEntry = Object.freeze({
  entrypoint_ref: conversationEntryRefs.rerunConversationEntry,
  kind: "service_entrypoint",
  accepts_contract_ref: runLaunchRefs.rerunConversationRunCommand,
  result_contract_refs: Object.freeze([
    runLaunchRefs.runLaunchAccepted,
    runLaunchRefs.runLaunchRejected,
  ]),
  continuity_view_ref: runContinuityRefs.rerunPlanView,
  dispatch_target_ref: "svc.execution-control.run-dispatch.rerun-run.v1",
  description:
    "Typed environment-shell entrypoint for regenerate-as-new-run behavior that preserves frozen basis links while creating a new run identity.",
  invariants: Object.freeze([
    "Rerun remains a new run dispatch and may not overwrite prior run truth.",
  ]),
})

export const conversationEntryServiceCatalog = Object.freeze({
  service_id: "svc.environment-shell-api.conversation-entry",
  service_version: CONVERSATION_ENTRY_SERVICE_VERSION,
  workspace_root: "services/environment-shell-api/conversation-entry/",
  package_dependencies: Object.freeze({
    continuity_api: runContinuityRefs,
    run_launch_contracts: runLaunchRefs,
  }),
  entrypoints: Object.freeze({
    start_conversation: startConversationEntry,
    resume_conversation: resumeConversationEntry,
    rerun_conversation: rerunConversationEntry,
  }),
  notes: Object.freeze([
    "This module materializes the R1 runtime_execution environment-shell entrypoint seam only.",
    "App routes remain out of scope for this packet and continue later under surface_validation.",
  ]),
})

export default conversationEntryServiceCatalog
