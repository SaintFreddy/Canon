# Remediation packet — Clock / TimeProvider abstraction
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-clock-timeprovider.v1
Prerequisite condition: (a) Clock / TimeProvider abstraction ownership
Target repo: `agentic-engine`

This packet is a scaffold. It is not authorized for execution until the plan-owner records a decision for condition (a) in `canon-knowledgebase/post-reopen-decisions/condition-a.md`. The packet body below assumes Option A (engine owns `Clock` interface, Shared Env supplies production impl); if the recorded decision chooses another option, regenerate the packet before executing.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-clock-timeprovider.v1",
  "title": "Introduce Clock interface + systemClock default in @canon/engine-core",
  "task_id": "P4p.step20.remediation.a",
  "objective": "Create the single Clock seam in @canon/engine-core so every packages/core factory accepts an optional injected clock and defaults to systemClock. Unblocks Platform Gate PG-01 and R3 exact-replay claims.",
  "scope": [
    "Add packages/core/src/clock.ts with Clock interface, systemClock default, and DeterministicClock test utility.",
    "Thread optional clock parameter through every create()/freeze()/capture()/assemble() factory in packages/core.",
    "Update contracts/exports.json to export Clock, systemClock, and DeterministicClock.",
    "Add a lint rule forbidding Date.now / new Date() / performance.now outside packages/core/src/clock.ts.",
    "Add packages/core/src/__tests__/clock-injection.test.ts covering every factory."
  ],
  "out_of_scope": [
    "packages/context-compiler wiring (follow-on packet CLK-2).",
    "packages/provenance wiring (follow-on CLK-3).",
    "workers/run-executor wiring (follow-on CLK-4).",
    "Shared Environment Clock implementation details.",
    "Canon/ quarantined draft state."
  ],
  "source_authority_refs": [
    "canon-now.md condition (a)",
    "canon-knowledgebase/post-reopen-decisions/condition-a.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6 row 1",
    "CANON_PLAN_IMPACT_REPORT.md Section 4 theme T1",
    "AGENTIC_ENGINE_AUDIT_LOG.md findings OWN-001, PKG-CORE-THEME-001, PKG-CC-001/002/003"
  ],
  "file_whitelist_ref": "wl.remediate-clock-timeprovider.v1",
  "deliverables": [
    "packages/core/src/clock.ts with Clock interface + systemClock + DeterministicClock.",
    "Modified factories in packages/core (every create/freeze/capture/assemble site).",
    "Updated contracts/exports.json.",
    "New clock-injection test.",
    "Lint rule in repo config forbidding wall-clock calls outside clock.ts.",
    "Draft carry-forward entry for human acceptance."
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.lint.no-wall-clock" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "approval_requirements": [
    "Plan-owner acceptance of condition (a) recorded before execution starts.",
    "Human review of the resulting PR before merge.",
    "Split or escalate if the Clock seam cannot be introduced without reopening engine boundary rules."
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high",
  "carry_forward_topics": [
    "Clock seam placement",
    "factory signature widening",
    "lint rule coverage",
    "deterministic replay regression baseline"
  ],
  "notes": [
    "Pair with the follow-on CLK-2/3/4 packets before claiming PG-01 reachable.",
    "Do not move frozenAt inside the hashed document in this packet; that is a coupled PROV decision handled by pkt.remediate-frozenat-in-hashed-doc.v1."
  ]
}
```

## File whitelist `wl.remediate-clock-timeprovider.v1`

- `packages/core/src/clock.ts` (new)
- `packages/core/src/*.ts` (factories only; no test files outside __tests__)
- `packages/core/src/__tests__/clock-injection.test.ts` (new)
- `contracts/exports.json`
- Root lint configuration file (e.g., `.eslintrc.cjs` or `eslint.config.js`)

## Completion signal

- `packages/core/src/clock.ts` exists with `Clock`, `systemClock`, `DeterministicClock`.
- No `packages/core/src/*.ts` (outside `clock.ts`) contains `Date.now` / `new Date()` / `performance.now`.
- Every core factory accepts `clock?: Clock` and uses it when present.
- `contracts/exports.json` lists the new symbols.
- `corepack pnpm typecheck` green.
- `corepack pnpm test` green including the new clock-injection test.
- Lint rule rejects `Date.now` outside `clock.ts`.
