import {
  runLaunchRefs,
} from "../../../packages/environment-control-contracts/run-launch/index.mjs"
import {
  admittedBasisRefs,
} from "../../../packages/context-compiler-contracts/admitted-basis/index.mjs"
import {
  chatTurnRefs,
} from "../../../packages/model-gateway-contracts/chat-turn/index.mjs"
import {
  runLineageRefs,
} from "../../../packages/event-provenance-contracts/run-lineage/index.mjs"

export const RUN_DISPATCH_SERVICE_VERSION = "1.0.0"

export const runDispatchRefs = Object.freeze({
  prepareRun: "svc.execution-control.run-dispatch.prepare-run.v1",
  resumeRun: "svc.execution-control.run-dispatch.resume-run.v1",
  rerunRun: "svc.execution-control.run-dispatch.rerun-run.v1",
  admitCompiledRun: "svc.execution-control.run-dispatch.admit-compiled-run.v1",
  completeGatewayRun: "svc.execution-control.run-dispatch.complete-gateway-run.v1",
})

export const prepareRunDispatch = Object.freeze({
  dispatch_ref: runDispatchRefs.prepareRun,
  kind: "dispatch_route",
  accepts_contract_ref: runLaunchRefs.runLaunchAccepted,
  emits_job_ref: admittedBasisRefs.compileRunContextCommand,
  publishes_lineage_ref: runLineageRefs.runLifecycleEvent,
  next_worker_ref: "worker.context-compiler.compile-run-context.execute.v1",
  description:
    "Dispatch route for a newly prepared R1 run that freezes the admitted basis before any model execution starts.",
  invariants: Object.freeze([
    "Prepared runs must compile the admitted basis before gateway execution.",
    "Lifecycle publication stays append-only and run-scoped.",
  ]),
})

export const resumeRunDispatch = Object.freeze({
  dispatch_ref: runDispatchRefs.resumeRun,
  kind: "dispatch_route",
  accepts_contract_ref: runLaunchRefs.runLaunchAccepted,
  emits_job_ref: admittedBasisRefs.compileRunContextCommand,
  publishes_lineage_ref: runLineageRefs.resumeContinuityEvent,
  next_worker_ref: "worker.context-compiler.compile-run-context.execute.v1",
  description:
    "Dispatch route for explicit-resume launches that keeps provider-loss posture visible while reusing the same admitted-basis compiler seam.",
  invariants: Object.freeze([
    "Resume dispatch preserves explicit continuity events rather than hiding them in provider-local state.",
  ]),
})

export const rerunRunDispatch = Object.freeze({
  dispatch_ref: runDispatchRefs.rerunRun,
  kind: "dispatch_route",
  accepts_contract_ref: runLaunchRefs.runLaunchAccepted,
  emits_job_ref: admittedBasisRefs.compileRunContextCommand,
  publishes_lineage_ref: runLineageRefs.runLifecycleEvent,
  next_worker_ref: "worker.context-compiler.compile-run-context.execute.v1",
  description:
    "Dispatch route for regenerate-as-new-run behavior that preserves rerun lineage while still recompiling a fresh admitted basis.",
  invariants: Object.freeze([
    "Rerun dispatch never reuses a prior run identity.",
  ]),
})

export const admitCompiledRunDispatch = Object.freeze({
  dispatch_ref: runDispatchRefs.admitCompiledRun,
  kind: "dispatch_route",
  accepts_contract_ref: admittedBasisRefs.compileRunContextResult,
  emits_gateway_ref: chatTurnRefs.chatTurnRequest,
  publishes_lineage_ref: runLineageRefs.runLifecycleEvent,
  next_service_ref: "svc.model-gateway.chat-turn-execution.execute.v1",
  description:
    "Dispatch route that turns a frozen admitted basis into one bounded provider-facing chat-turn request.",
  invariants: Object.freeze([
    "Gateway execution starts only after the admitted basis is frozen.",
  ]),
})

export const completeGatewayRunDispatch = Object.freeze({
  dispatch_ref: runDispatchRefs.completeGatewayRun,
  kind: "dispatch_route",
  accepts_contract_refs: Object.freeze([
    chatTurnRefs.chatTurnResult,
    chatTurnRefs.chatTurnFailure,
  ]),
  publishes_lineage_refs: Object.freeze([
    runLineageRefs.runLifecycleEvent,
    runLineageRefs.sourceResolutionEvent,
  ]),
  trace_service_ref: "svc.event-provenance.run-trace.publish-run-lifecycle.v1",
  description:
    "Dispatch route that closes the bounded R1 run by publishing lifecycle and source-resolution trace facts from the normalized gateway outcome.",
  invariants: Object.freeze([
    "Completion remains reconstructable from append-only run and source events.",
  ]),
})

export const runDispatchServiceCatalog = Object.freeze({
  service_id: "svc.execution-control.run-dispatch",
  service_version: RUN_DISPATCH_SERVICE_VERSION,
  workspace_root: "services/execution-control/run-dispatch/",
  package_dependencies: Object.freeze({
    run_launch_contracts: runLaunchRefs,
    admitted_basis_contracts: admittedBasisRefs,
    chat_turn_contracts: chatTurnRefs,
    run_lineage_contracts: runLineageRefs,
  }),
  dispatch_routes: Object.freeze({
    prepare_run: prepareRunDispatch,
    resume_run: resumeRunDispatch,
    rerun_run: rerunRunDispatch,
    admit_compiled_run: admitCompiledRunDispatch,
    complete_gateway_run: completeGatewayRunDispatch,
  }),
  notes: Object.freeze([
    "This service stays inside execution-control orchestration and does not own provider logic, app projections, or shared-object authorship.",
  ]),
})

export default runDispatchServiceCatalog
