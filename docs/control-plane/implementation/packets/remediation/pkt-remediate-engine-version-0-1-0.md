# Remediation packet — Engine semver start at 0.1.0
Version: 1.0
Status: Authorized
Task: Phase 4+ step 20 — post-reopen remediation wave D
Artifact ID: pkt.remediate-engine-version-0.1.0.v1
Prerequisite condition: (e.1) engine version direction
Target repo: `agentic-engine`

Plan-owner decision recorded at `canon-knowledgebase/post-reopen-decisions/condition-e-engine-version.md`.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-engine-version-0.1.0.v1",
  "title": "Bump agentic-engine workspace to 0.1.0 with spec-digest anchor",
  "task_id": "P4p.step20.remediation.e1",
  "objective": "Move every @canon/* workspace package from 0.0.0 to 0.1.0 and record the initial spec-digest anchor.",
  "scope": [
    "Update agentic-engine/package.json and every packages/*/package.json + workers/*/package.json to version 0.1.0.",
    "Update any internal workspace: references to match.",
    "Create docs/spec-digests/engine-0.1.0.md checkpoint with the content-hash anchor and the list of contracts/exports.json symbols at 0.1.0.",
    "Update any repo-level version references in README if present.",
    "Add CHANGELOG.md entry for 0.1.0 noting it as the first semver release after the audit-reopen remediation wave."
  ],
  "out_of_scope": [
    "Publishing to npm.",
    "Breaking-change introductions (this is a version-bump packet, not a breaking-change packet).",
    "Canon/ quarantined draft state."
  ],
  "source_authority_refs": [
    "canon-now.md condition (e)",
    "canon-knowledgebase/post-reopen-decisions/condition-e-engine-version.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6 row 7",
    "AGENTIC_ENGINE_AUDIT_LOG.md X-010, X-015"
  ],
  "file_whitelist_ref": "wl.remediate-engine-version-0.1.0.v1",
  "deliverables": [
    "All package.json files bumped to 0.1.0",
    "docs/spec-digests/engine-0.1.0.md",
    "CHANGELOG.md entry",
    "Draft carry-forward entry"
  ],
  "validation_hooks": [
    { "hook_id": "vh.typecheck.pnpm" },
    { "hook_id": "vh.test.pnpm" },
    { "hook_id": "vh.build.pnpm" },
    { "hook_id": "vh.spec-digest.present" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "github_actions_droid_or_cli_session",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## File whitelist `wl.remediate-engine-version-0.1.0.v1`

- `package.json` (root)
- `packages/*/package.json`
- `workers/*/package.json`
- `docs/spec-digests/engine-0.1.0.md` (new)
- `CHANGELOG.md`
- `README.md` (only if it cites the version literally)

## Completion signal

- `jq -r '.version' packages/*/package.json` all return `0.1.0`.
- `docs/spec-digests/engine-0.1.0.md` exists with content-hash anchor.
- `pnpm build` green.
