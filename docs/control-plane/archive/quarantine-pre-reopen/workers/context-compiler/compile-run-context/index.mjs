import {
  runContinuityRefs,
} from "../../../packages/shared-object-api/run-continuity/index.mjs"
import {
  admittedBasisRefs,
} from "../../../packages/context-compiler-contracts/admitted-basis/index.mjs"

export const COMPILE_RUN_CONTEXT_WORKER_VERSION = "1.0.0"

export const compileRunContextWorkerRefs = Object.freeze({
  executeCompileRunContext: "worker.context-compiler.compile-run-context.execute.v1",
  publishCompiledBasis: "worker.context-compiler.compile-run-context.publish-basis.v1",
})

export const executeCompileRunContext = Object.freeze({
  worker_ref: compileRunContextWorkerRefs.executeCompileRunContext,
  kind: "worker_job_route",
  accepts_contract_ref: admittedBasisRefs.compileRunContextCommand,
  record_contract_ref: admittedBasisRefs.admittedBasisRecord,
  result_contract_ref: admittedBasisRefs.compileRunContextResult,
  inspection_view_refs: Object.freeze([
    runContinuityRefs.runInspectionView,
    runContinuityRefs.resumeContinuityView,
  ]),
  description:
    "Bounded context-compiler worker that freezes the admitted basis for one R1 run before provider invocation.",
  invariants: Object.freeze([
    "Explicit admitted inputs take precedence over fallback lane selection.",
    "Provider session hints remain advisory only and never become the replay basis.",
    "The worker emits a frozen admitted-basis record and compact inspection-ready result for the same run.",
  ]),
})

export const publishCompiledBasis = Object.freeze({
  worker_ref: compileRunContextWorkerRefs.publishCompiledBasis,
  kind: "worker_result_route",
  accepts_contract_ref: admittedBasisRefs.compileRunContextResult,
  next_dispatch_ref: "svc.execution-control.run-dispatch.admit-compiled-run.v1",
  description:
    "Worker result route that hands the frozen admitted-basis result back to execution-control for bounded chat-turn execution.",
  invariants: Object.freeze([
    "Context compilation remains a worker seam over frozen refs and returns control through typed dispatch rather than app-local shortcuts.",
  ]),
})

export const compileRunContextWorkerCatalog = Object.freeze({
  worker_id: "worker.context-compiler.compile-run-context",
  worker_version: COMPILE_RUN_CONTEXT_WORKER_VERSION,
  workspace_root: "workers/context-compiler/compile-run-context/",
  package_dependencies: Object.freeze({
    continuity_api: runContinuityRefs,
    admitted_basis_contracts: admittedBasisRefs,
  }),
  jobs: Object.freeze({
    execute_compile_run_context: executeCompileRunContext,
    publish_compiled_basis: publishCompiledBasis,
  }),
  notes: Object.freeze([
    "This worker materializes the R1 admitted-basis compiler seam only.",
    "Pack editing, replay/compare, and later-stage context controls remain outside this packet.",
  ]),
})

export default compileRunContextWorkerCatalog
