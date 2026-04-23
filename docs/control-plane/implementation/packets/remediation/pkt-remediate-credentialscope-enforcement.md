# Remediation packet — credentialScope.allowedSecrets enforcement
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-credentialscope-enforcement.v1
Prerequisite condition: (b) tool-gateway honesty — credentialScope enforcement path
Target repo: `agentic-engine`

Scaffold only. Execution requires a recorded plan-owner decision at `canon-knowledgebase/post-reopen-decisions/condition-b.md` specifying the enforcement path.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-credentialscope-enforcement.v1",
  "title": "Enforce credentialScope.allowedSecrets at the tool gateway",
  "task_id": "P4p.step20.remediation.b-credentialscope",
  "objective": "Close the gap between declared credentialScope.allowedSecrets and actual gateway behavior. Every tool invocation must fail closed when a requested secret is outside the declared scope; every path that resolves secrets must go through the enforcement point.",
  "scope": [
    "Introduce or lift the single enforcement point (e.g., packages/model-gateway/src/credential-gate.ts).",
    "Route every tool-invocation credential resolution through the gate.",
    "Fail closed with a typed error when a requested secret is not in allowedSecrets.",
    "Add a regression test matrix: in-scope granted, out-of-scope denied, missing-declaration denied, wildcard handling if decision permits.",
    "Update contracts/exports.json if the gate becomes a public symbol."
  ],
  "out_of_scope": [
    "ToolSandboxWorker IPC isolation (separate packet).",
    "Policy-matcher pattern decisions (separate condition).",
    "Changing the credentialScope schema itself."
  ],
  "source_authority_refs": [
    "canon-now.md condition (b)",
    "canon-knowledgebase/post-reopen-decisions/condition-b.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6",
    "AGENTIC_ENGINE_AUDIT_LOG.md credentialScope findings"
  ],
  "file_whitelist_ref": "wl.remediate-credentialscope-enforcement.v1",
  "deliverables": [
    "Credential gate module with fail-closed semantics.",
    "Every tool invocation site routed through the gate.",
    "Test matrix covering in-scope / out-of-scope / missing / wildcard.",
    "Updated contracts/exports.json if applicable.",
    "Draft carry-forward entry."
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.security.fail-closed-matrix" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## File whitelist `wl.remediate-credentialscope-enforcement.v1`

- `packages/model-gateway/src/**/*.ts`
- `packages/policy/src/**/*.ts` (if the gate lives here per decision)
- `workers/run-executor/src/**/*.ts` (call-site updates only)
- `contracts/exports.json`
- `packages/*/src/__tests__/credential-scope.*.test.ts`

## Completion signal

- No tool-invocation path resolves a secret without going through the gate.
- Out-of-scope requests produce a typed `CredentialScopeViolation` error (or the type named by the decision).
- Full test matrix green.
- `pnpm typecheck` + `pnpm test` green.
