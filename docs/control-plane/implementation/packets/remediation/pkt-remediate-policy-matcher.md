# Remediation packet — Policy-matcher typed RulePattern
Version: 1.0
Status: Authorized (prerequisite decision recorded)
Task: Phase 4+ step 20 — post-reopen remediation wave D
Artifact ID: pkt.remediate-policy-matcher.v1
Prerequisite condition: (c) policy-matcher pattern vs strict-equals
Target repo: `agentic-engine`

Plan-owner decision recorded at `canon-knowledgebase/post-reopen-decisions/condition-c.md` — Option A accepted.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-policy-matcher.v1",
  "title": "Ship typed RulePattern with glob/regex and replace strict-equals in policy paths",
  "task_id": "P4p.step20.remediation.c",
  "objective": "Replace strict-equals policy matching with a typed RulePattern tagged union supporting exact/glob/regex, with cached compilation and typed failure results.",
  "scope": [
    "Add packages/policy/src/rule-pattern.ts with RulePattern tagged union, matches() function, and cached regex compilation.",
    "Update packages/policy/src/policy-matcher.ts to use matches() everywhere.",
    "Add typed PolicyPatternCompileError for regex compilation failures.",
    "Add packages/policy/src/__tests__/rule-pattern.test.ts covering exact + glob + regex + compile-failure paths.",
    "Update contracts/exports.json to export RulePattern and matches additively."
  ],
  "out_of_scope": [
    "Domain-pack rule definitions (they migrate later).",
    "AuthorityScope restore factory (PKG-POL-011 is a separate ARCHITECTURE-CHANGE).",
    "Canon/ quarantined draft state."
  ],
  "source_authority_refs": [
    "canon-now.md condition (c)",
    "canon-knowledgebase/post-reopen-decisions/condition-c.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6 row 4",
    "AGENTIC_ENGINE_AUDIT_LOG.md PKG-POL-001..005, PKG-POL-009, PKG-POL-014"
  ],
  "file_whitelist_ref": "wl.remediate-policy-matcher.v1",
  "deliverables": [
    "packages/policy/src/rule-pattern.ts (new)",
    "Updated packages/policy/src/policy-matcher.ts",
    "New regression test suite",
    "Updated contracts/exports.json",
    "Draft carry-forward entry"
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.lint.no-strict-equals-in-policy-matchers" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## File whitelist `wl.remediate-policy-matcher.v1`

- `packages/policy/src/rule-pattern.ts` (new)
- `packages/policy/src/policy-matcher.ts`
- `packages/policy/src/__tests__/rule-pattern.test.ts` (new)
- `packages/policy/src/__tests__/policy-matcher.test.ts`
- `contracts/exports.json`

## Completion signal

- `RulePattern` + `matches` exported additively.
- No strict-equals string comparisons in `packages/policy/src/` outside `RulePattern` `kind: "exact"` branch.
- Test matrix green across exact/glob/regex/compile-failure paths.
- `pnpm typecheck` + `pnpm test` green.
