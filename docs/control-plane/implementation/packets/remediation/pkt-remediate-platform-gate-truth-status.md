# Remediation packet — Platform Gate truth-status reconciliation
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ step 20 — post-reopen remediation wave A
Artifact ID: pkt.remediate-platform-gate-truth-status.v1
Prerequisite condition: (f) Platform Gate truth-status decision
Target repo: `Canon` (control-plane only)

Scaffold only. Execution requires a recorded plan-owner decision at `canon-knowledgebase/post-reopen-decisions/condition-f.md` specifying either formal reopen or retention with audit-aware footnotes.

This packet is control-plane-only — no `agentic-engine` code changes. It reconciles Canon's Platform Gate authority record with the observed audit reality.

## Packet brief

```json
{
  "packet_id": "pkt.remediate-platform-gate-truth-status.v1",
  "title": "Reconcile Platform Gate truth-status with audit-cited reality",
  "task_id": "P4p.step20.remediation.f",
  "objective": "Bring the Platform Gate artifact into durable alignment with audit-cited reality. Either formally reopen (status: reopened) with enumerated failing invariants, or retain 'passed' with explicit audit-aware footnotes that cite the 12 conditions and link to the remediation packet queue.",
  "scope": [
    "Update Canon/docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md per the recorded decision.",
    "Append a new accepted artifact carry-forward entry to docs/control-plane/core/master-plan.md.",
    "Update docs/control-plane/artifact-registry.seed.json status and stale-fields per decision.",
    "Update docs/control-plane/dependency-graph.seed.json if the decision changes downstream artifact status (e.g., marking PG-dependent release contracts stale pending remediation)."
  ],
  "out_of_scope": [
    "Any agentic-engine code change.",
    "Reopening accepted baseline decisions beyond condition (f).",
    "Editing AGENTIC_ENGINE_AUDIT_LOG.md or CANON_PLAN_IMPACT_REPORT.md."
  ],
  "source_authority_refs": [
    "canon-now.md condition (f)",
    "canon-knowledgebase/post-reopen-decisions/condition-f.md",
    "canon-knowledgebase/post-reopen-audit-cited-contradiction-checkpoint.md",
    "arch.phase3-platform-gate-spec.v1",
    "AGENTIC_ENGINE_AUDIT_LOG.md",
    "CANON_PLAN_IMPACT_REPORT.md"
  ],
  "file_whitelist_ref": "wl.remediate-platform-gate-truth-status.v1",
  "deliverables": [
    "Updated Platform Gate artifact file.",
    "Synchronized registry/graph entries.",
    "New master-plan carry-forward entry.",
    "Stale-marker propagation if reopened."
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
    "This packet is control-plane only. No compiled code changes.",
    "Run scripts/validators/validate_control_plane_integrity.py after the edits.",
    "Run scripts/wrappers/run_phase7_stale_detection.py --changed-artifact arch.phase3-platform-gate-spec.v1 and record the impact map in the carry-forward entry.",
    "Pairs with all 6 other remediation packets. Whether this packet goes first or last depends on the recorded decision (formal reopen goes first; retain-with-footnotes goes after engine-side remediation lands).",
    "Under retention-with-footnotes, this packet depends on completion of packets 1-6 and annotates 'passed' with a remediation log citation."
  ]
}
```

## File whitelist `wl.remediate-platform-gate-truth-status.v1`

- `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md`
- `docs/control-plane/core/master-plan.md` (carry-forward append only)
- `docs/control-plane/artifact-registry.seed.json`
- `docs/control-plane/dependency-graph.seed.json`

## Completion signal

- Platform Gate artifact status matches the recorded decision exactly.
- Registry/graph in sync.
- `python3 scripts/validators/validate_control_plane_integrity.py` green.
- Master-plan carry-forward entry appended.
