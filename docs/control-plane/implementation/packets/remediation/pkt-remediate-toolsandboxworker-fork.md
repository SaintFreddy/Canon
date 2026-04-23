# Remediation packet — ToolSandboxWorker child-process fork
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-toolsandboxworker-fork.v1
Prerequisite condition: (b) tool-gateway honesty — sandbox isolation claim
Target repo: `agentic-engine`

Scaffold only. Execution requires a recorded plan-owner decision at `canon-knowledgebase/post-reopen-decisions/condition-b.md` specifying the IPC export and isolation model.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-toolsandboxworker-fork.v1",
  "title": "Make ToolSandboxWorker actually fork a child process",
  "task_id": "P4p.step20.remediation.b-sandbox-fork",
  "objective": "Replace the current in-process pseudo-sandbox with a real child-process fork so tool-invocation isolation claims are truthful. Bound stdin/stdout/stderr, enforce a strict capability envelope, and surface child-process errors as typed results.",
  "scope": [
    "Rewrite ToolSandboxWorker to spawn a child Node/Bun process via node:child_process fork (or the equivalent decision-named mechanism).",
    "Define the parent<->child IPC contract (message types, request/response shape, error propagation).",
    "Bound the child's environment: no network by default, no access to the parent process's file descriptors beyond the declared channel.",
    "Add integration tests that prove: (i) sandbox crash does not take down the parent; (ii) sandbox cannot access parent-process secrets; (iii) stdout from the sandbox cannot inject messages into the IPC channel."
  ],
  "out_of_scope": [
    "credentialScope.allowedSecrets enforcement (paired packet).",
    "ToolSandboxWorker public API changes beyond the IPC contract.",
    "Host-level network restrictions (those belong to the shell, not the sandbox worker)."
  ],
  "source_authority_refs": [
    "canon-now.md condition (b)",
    "canon-knowledgebase/post-reopen-decisions/condition-b.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6",
    "AGENTIC_ENGINE_AUDIT_LOG.md ToolSandboxWorker findings"
  ],
  "file_whitelist_ref": "wl.remediate-toolsandboxworker-fork.v1",
  "deliverables": [
    "Rewritten ToolSandboxWorker.",
    "IPC contract module (types + serializer).",
    "Child-process bootstrap entry.",
    "Integration test suite proving real isolation.",
    "Draft carry-forward entry."
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.security.sandbox-isolation-matrix" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## File whitelist `wl.remediate-toolsandboxworker-fork.v1`

- `workers/tool-sandbox/src/**/*.ts` (or wherever ToolSandboxWorker currently lives)
- `packages/model-gateway/src/sandbox-ipc.ts` (new, if the contract lives here)
- `workers/tool-sandbox/src/__tests__/*.test.ts`
- `contracts/exports.json` if the sandbox types become public

## Completion signal

- `ps -ef` during a live test shows an actual forked child process.
- Isolation matrix green: crash, secret access, stdout injection all produce the expected controlled outcomes.
- `pnpm typecheck` + `pnpm test` green.
