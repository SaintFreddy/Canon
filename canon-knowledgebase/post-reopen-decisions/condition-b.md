# Accepted Decision: Condition (b) — Tool-gateway honesty reconciliation

## Status

ACCEPTED. Recorded durably by plan-owner on 2026-04-23.

## Plan-owner

SaintFreddy (repo owner, Canon plan authority).

## Accepted options (three sub-decisions)

- **B-1 credentialScope enforcement path**: **Option A** — Engine owns `CredentialProvider` interface + enforcement wrapper; `validateCredentialScope` hardened against prototype pollution and the X-057 undefined coercion.
- **B-2 sandbox process-boundary isolation**: **Option A** — Engine ships `spawnToolSandboxWorker` that forks a real Node child, and renames the in-process primitive to `InProcessToolRunner`. Platform Gate §6 PG-10 gets an explicit process-boundary clause.
- **B-3 `ToolSandboxWorker` IPC export**: **Option A** — `attachToolSandboxWorkerIpc` and IPC message types are re-exported from `workers/tool-sandbox/src/index.ts` and added to `contracts/exports.json`.

## Decision statement

### B-1 — CredentialProvider

New file `packages/tool-gateway/src/credential-provider.ts`:

```ts
export interface CredentialProvider {
  resolve(scope: CredentialScope): Record<string, string>;
}
export class EnvBackedCredentialProvider implements CredentialProvider {
  // returns ONLY keys in scope.allowedSecrets from process.env
}
```

`ToolSandbox.execute` accepts a `CredentialProvider` (defaulted to `EnvBackedCredentialProvider`). Adapters receive a frozen execution context `{ secrets: provider.resolve(scope) }` with `process.env` stripped at the lexical boundary via an execution wrapper.

`validateCredentialScope` extended to enforce: `Array.isArray(scope.allowedSecrets)` with every element a non-empty string; `scope.toolId === toolId`; `scope.expiresAt` is a valid ISO or `null`. X-057 fixed by normalizing `undefined` → `null` at construction.

### B-2 — spawnToolSandboxWorker

- `packages/tool-gateway/src/tool-sandbox.ts` `ToolSandbox` renamed `InProcessToolRunner` (or equivalent; final name chosen on PR review). Documented as "in-process runner; development and testing only."
- New `workers/tool-sandbox/src/spawn-tool-sandbox-worker.ts` providing `spawnToolSandboxWorker(options): ParentSideHandle` which forks a Node child and marshals `execute` requests through the existing IPC protocol in `src/ipc.ts`.
- Platform Gate spec `§6 PG-10` gains the explicit clause: "tool execution runs in a forked Node child when the host opts into `spawnToolSandboxWorker`; in-process runner is documented as development/testing only." This is a condition (f) linked doc edit (see `post-reopen-decisions/condition-f.md`).
- Regression test: `workers/tool-sandbox/src/__tests__/spawn.test.ts` round-trips an `execute` request, asserts `process.pid` differs between parent and worker, and asserts a worker-side throw does not crash the parent.

### B-3 — IPC export

`workers/tool-sandbox/src/index.ts` re-exports `attachToolSandboxWorkerIpc`, `ParentMessage`, `WorkerMessage`, `ExecuteRequestMessage`, `ExecuteResultMessage`. `contracts/exports.json` lists the same additively.

## Rationale summary

- B-1 Option B would import a Shared-Env contract into engine and break engine-universality.
- B-1 Option C (CredentialScopeHint rename) publicly retracts PG-07's scoped-credential promise.
- B-2 Option B (defer fork to R6) pushes a Platform Gate substrate promise two releases forward and weakens the "gate-is-real-bridge-seam" discipline.
- B-2 Option C (delete PG-10 worker-boundary clause) conflicts with R6 and R7 blueprints that both assume sandboxing.
- B-3 Option B (subpath exports) is a minor ergonomic alternative; Option A is trivially cleaner.
- **Coupling accepted**: B-1 provides defense-in-depth; B-2 provides the hard contract. Together they deliver honest PG-07 + PG-10. The plan-owner has accepted the full A+A+A package rather than the "staged fork" alternative (a=A, b=A+B+A, f=B).

## What this unblocks

- `pkt.remediate-credentialscope-enforcement.v1` (wave B.1) — authorized for execution.
- `pkt.remediate-toolsandboxworker-fork.v1` (wave B.2) — authorized, can parallel B.1.

## New constraints accepted with this decision

1. Engine publishes `CredentialProvider` + `EnvBackedCredentialProvider` as public contract surface.
2. Adapters that reach around the provider (direct `process.env` access) are deprecated. A lint rule or adapter-contract test is recommended and will ship with the remediation packet.
3. `spawnToolSandboxWorker` becomes the required production pattern. In-process runner is explicitly labeled development/testing only.
4. Platform Gate spec §6 PG-10 prose is updated in the same reopen transaction as condition (f) acceptance.
5. IPC message contracts become part of the public engine API; breaking changes require typed migration.

## Reference to draft options analysis

Full option analysis, cited-evidence ledger, and coupling discussion at `/Users/fredericksaintmaximus/Desktop/Canon Dev/decisions/condition-b.md` (draft, preserved as historical record). Cited audit findings: `PKG-TG-001`, `PKG-TG-002`, `PKG-TG-011`, `PKG-MG-024`, `X-057`, `WRK-TS-001/002/003/004/005/006`; themes T2 and T3 in `CANON_PLAN_IMPACT_REPORT.md` Section 4.

## Execution posture

- First B-packet: `pkt.remediate-credentialscope-enforcement.v1`, then `pkt.remediate-toolsandboxworker-fork.v1` in parallel.
- Model: `claude-opus-4-7`, reasoning effort `high`.
- Verification matrix — credential gate: in-scope granted, out-of-scope denied, prototype-poisoned scope rejected, undefined expiresAt normalized, wildcard handling per the resolver's documented rules.
- Verification matrix — sandbox fork: parent PID ≠ child PID in live test, child crash does not propagate, child cannot access parent's non-allowed env, stdout from child cannot inject messages into IPC channel.
- Human review required on both resulting PRs before merge.
