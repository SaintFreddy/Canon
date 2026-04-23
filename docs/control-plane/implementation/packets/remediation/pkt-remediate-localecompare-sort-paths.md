# Remediation packet — localeCompare purge from sort paths
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-localecompare-sort-paths.v1
Prerequisite condition: coupled with (a) Clock decision
Target repo: `agentic-engine`

Scaffold only. `localeCompare` in replay-sensitive sort paths is non-deterministic across locales; this packet purges those call sites in favor of byte-deterministic comparators.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-localecompare-sort-paths.v1",
  "title": "Replace localeCompare with byte-deterministic comparators in replay-sensitive sort paths",
  "task_id": "P4p.step20.remediation.localecompare",
  "objective": "Every sort path that feeds into a hashed document, a compiled context digest, or a replay-order invariant must use a locale-independent string comparator. Purge localeCompare from those paths and add a lint rule.",
  "scope": [
    "Grep for localeCompare in packages/ and workers/; enumerate every replay-sensitive call site.",
    "Replace with a byte-deterministic comparator (e.g., strict < / > comparison, or a shared packages/core/src/ordering.ts utility).",
    "Keep localeCompare allowed in user-facing display sorting only (document the permitted scope).",
    "Add lint rule forbidding localeCompare in replay-sensitive paths (via file-path-based restriction)."
  ],
  "out_of_scope": [
    "Changing display-layer sort behavior.",
    "Redesigning the ordering contract."
  ],
  "source_authority_refs": [
    "canon-now.md condition (a) coupling",
    "CANON_PLAN_IMPACT_REPORT.md Section 6",
    "AGENTIC_ENGINE_AUDIT_LOG.md localeCompare findings"
  ],
  "file_whitelist_ref": "wl.remediate-localecompare-sort-paths.v1",
  "deliverables": [
    "Replay-sensitive sort paths converted.",
    "packages/core/src/ordering.ts byte-deterministic comparator utility (if one is needed).",
    "Updated lint configuration.",
    "Regression test proving identical input produces identical sorted output across locales.",
    "Draft carry-forward entry."
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.lint.no-localecompare-in-replay-paths" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## File whitelist `wl.remediate-localecompare-sort-paths.v1`

- Every file matching `grep -rn "localeCompare" packages/ workers/` outside test and display-only subdirectories (enumerated at planning time).
- `packages/core/src/ordering.ts` (new, if introduced)
- Root lint configuration

## Completion signal

- `grep -rn "localeCompare" packages/ workers/ | grep -v __tests__ | grep -v display` returns zero replay-sensitive matches.
- Lint rule enforces the purge going forward.
- `pnpm typecheck` + `pnpm test` green.
