# Remediation packet — Intra-workspace peerDependency carve-out
Version: 1.0
Status: Authorized
Task: Phase 4+ step 20 — post-reopen remediation wave D
Artifact ID: pkt.remediate-peerdep-carveout.v1
Prerequisite condition: (g) intra-workspace peerDependency carve-out
Target repo: `Canon` (control-plane doc-only)

Plan-owner decision recorded at `canon-knowledgebase/post-reopen-decisions/condition-g.md`.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-peerdep-carveout.v1",
  "title": "Amend phase-6-repo-package-architecture §6.1 to carve out intra-workspace peer-deps",
  "task_id": "P4p.step20.remediation.g",
  "objective": "Preserve the 'zero external runtime dependencies' invariant while explicitly permitting intra-workspace peer-dependencies between @canon/* packages.",
  "scope": [
    "Amend Canon/docs/control-plane/architecture/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md §6.1 to add the carve-out paragraph.",
    "Append carry-forward entry in master plan.",
    "Update docs/control-plane/artifact-registry.seed.json if §6.1 is a registered artifact surface.",
    "Update docs/control-plane/dependency-graph.seed.json if the amendment changes downstream artifact status."
  ],
  "out_of_scope": [
    "Any agentic-engine code change.",
    "Changing actual peer-dep declarations in agentic-engine packages.",
    "Broadening the carve-out to third-party peer-deps."
  ],
  "source_authority_refs": [
    "canon-now.md condition (g)",
    "canon-knowledgebase/post-reopen-decisions/condition-g.md",
    "CANON_PLAN_IMPACT_REPORT.md Section 6 row 8",
    "AGENTIC_ENGINE_AUDIT_LOG.md X-029"
  ],
  "file_whitelist_ref": "wl.remediate-peerdep-carveout.v1",
  "deliverables": [
    "Amended §6.1 paragraph",
    "Master-plan carry-forward entry",
    "Synchronized registry/graph entries"
  ],
  "validation_hooks": [
    { "hook_id": "vh.dependency.integrity" },
    { "hook_id": "vh.consistency.cross-pack-review" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "cli_session_preferred",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high",
  "notes": [
    "Control-plane only; no compiled code changes.",
    "Run scripts/validators/validate_control_plane_integrity.py after the edit."
  ]
}
```

## File whitelist `wl.remediate-peerdep-carveout.v1`

- `docs/control-plane/architecture/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md`
- `docs/control-plane/core/master-plan.md`
- `docs/control-plane/artifact-registry.seed.json`
- `docs/control-plane/dependency-graph.seed.json`

## Completion signal

- §6.1 contains the carve-out paragraph and preserves prior text.
- Master-plan carry-forward entry appended.
- `python3 scripts/validators/validate_control_plane_integrity.py` green.
