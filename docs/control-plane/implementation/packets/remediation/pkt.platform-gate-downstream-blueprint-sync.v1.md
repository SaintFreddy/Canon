# Remediation packet — Platform Gate downstream blueprint sync (PG-R2)
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ post-step-20 — Platform Gate reopen downstream propagation (PG-R2)
Artifact ID: pkt.platform-gate-downstream-blueprint-sync.v1
Prerequisite: `pkt.remediate-platform-gate-truth-status.v1` (PG-R1) landed on `SaintFreddy/Canon` main (Canon PR #17, merged 2026-04-24)
Target repo: `SaintFreddy/Canon` (control-plane only, doc sync)

Scaffold authored after step 20 closure per CF-0097. Executes the "downstream blueprint footnote sync" path explicitly named in `canon-knowledgebase/post-reopen-decisions/condition-f.md` as PG-R2.

This packet is control-plane-only — no `agentic-engine` code changes. It propagates the Platform Gate reopen acknowledgement from the gate spec itself (already landed via PG-R1) into every accepted release blueprint that transitively depends on it, so downstream consumers reading any individual blueprint cannot miss the reopen context.

## Packet brief

```json
{
  "packet_id": "pkt.platform-gate-downstream-blueprint-sync.v1",
  "title": "Propagate Platform Gate reopen status into 7 Phase 6 release blueprints",
  "task_id": "P4p.post-step-20.pg-r2",
  "objective": "Every accepted Phase 6 release blueprint (R1..R7) receives a uniformly-formatted 'Platform Gate reopen notice' footnote placed between the file's Status header and its §1 Purpose section, plus a corresponding registry note appended to each blueprint's entry in docs/control-plane/artifact-registry.seed.json. After this packet, no accepted blueprint can be read in isolation without the reopen context being surfaced. Blueprint guidance itself is not rewritten; downstream consumers retain the accepted implementation map.",
  "scope": [
    "Add a uniform 'Platform Gate reopen notice (2026-04-23)' block to each of the 7 blueprint .md files under docs/control-plane/implementation/release-blueprints/",
    "Append one new note string to each of those 7 blueprints' artifact-registry.seed.json entries",
    "No changes to any other file"
  ],
  "out_of_scope": [
    "Any agentic-engine code change",
    "Maturity matrix (rel.chat-native-maturity-matrix.v1) — that is PG-R3 scope",
    "Milestone architecture plan (rel.chat-native-milestone-architecture-plan.v1) — that is PG-R3 scope",
    "Release contract packs (9 rel.release_contract_pack artifacts) — not in PG-R2/R3 at all; deferred to a separate packet if needed",
    "Phase 6 execution packets (26 pkt.execution_packet artifacts) — not in PG-R2/R3 scope",
    "Surface packs, control-plane datasets, reuse packs — not in PG-R2/R3 scope",
    "Editing AGENTIC_ENGINE_AUDIT_LOG.md, CANON_PLAN_IMPACT_REPORT.md, AGENTIC_WORKFLOW.md, or any canon-knowledgebase/ record",
    "Changing artifact_status on any blueprint (all remain 'accepted' — reopen is surfaced via a new note, not a status flip)",
    "Retouching Platform Gate spec itself (PG-R1 already landed)",
    "Rewriting blueprint content — only header-level footnote additions and one registry note per entry"
  ],
  "source_authority_refs": [
    "canon-knowledgebase/post-reopen-decisions/condition-f.md (DEC-RO-0f, Option A)",
    "docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md §0.1 (PG-R1 landed markup)",
    "docs/control-plane/artifact-registry.seed.json (arch.phase3-platform-gate-spec.v1 entry for precedent note format)",
    "canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md CF-0097 (step 20 closure + downstream unblock)",
    "canon-now.md (baton: ready)"
  ],
  "file_whitelist": [
    "docs/control-plane/implementation/release-blueprints/r1-conversation-blueprint.md",
    "docs/control-plane/implementation/release-blueprints/r2-context-control-blueprint.md",
    "docs/control-plane/implementation/release-blueprints/r3-branch-replay-blueprint.md",
    "docs/control-plane/implementation/release-blueprints/r4-artifact-workspace-blueprint.md",
    "docs/control-plane/implementation/release-blueprints/r5-prompt-assets-blueprint.md",
    "docs/control-plane/implementation/release-blueprints/r6-governed-reusable-execution-blueprint.md",
    "docs/control-plane/implementation/release-blueprints/r7-commissioning-bridge-blueprint.md",
    "docs/control-plane/artifact-registry.seed.json"
  ],
  "deliverables": [
    "7 blueprint .md files each with identical structural reopen-notice block inserted at the same logical position",
    "7 registry entries each with one new notes[] string appended (position: after existing notes, not inserted in between)",
    "Single PR against SaintFreddy/Canon:main",
    "No other file changes"
  ],
  "validation_hooks": [
    { "hook_id": "vh.dependency.integrity" },
    { "hook_id": "vh.consistency.cross-pack-review" },
    { "hook_id": "vh.manual.acceptance" }
  ],
  "execution_mode": "factory_first",
  "runtime": "cli_session_preferred",
  "model": "claude-opus-4-7",
  "reasoning_effort": "high"
}
```

## Uniform reopen-notice block (exact template to insert into each blueprint .md)

The block MUST be inserted between the existing "This artifact is accepted for downstream use." line (or equivalent lead-in sentence right after the status/release-ref header) AND the next logical paragraph. Insert as a dedicated section using the blockquote format below. Use the SAME text verbatim in all 7 files — only the file-path context differs; the content of the notice is identical.

```markdown
> **Platform Gate reopen notice (2026-04-23).** This blueprint transitively depends on `arch.phase3-platform-gate-spec.v1`. On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the Platform Gate P3.6 acceptance marker against the 2026-04-18 agentic-engine audit-cited contradiction event per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A). Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`. This blueprint itself remains `accepted` for downstream use — the implementation guidance below is unchanged and the release doctrine is not reopened. Consumers reading this blueprint should, however, be aware that PG-01.1 (Clock + stableStringify + localeCompare + frozenAt), PG-07.1 (credentialScope enforcement), and PG-10.1 (spawnToolSandboxWorker + IPC export) are remediation sub-gates still closing. Engine sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (see `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0089..CF-0096); the sub-gates formally close after PG-R3 (maturity-matrix + milestone-plan sync) lands. See `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 for the full gate reopen markup and successor-checkpoint reference.
```

## Uniform registry notes[] append (exact template to add to each blueprint's entry)

Append — DO NOT replace — the existing `notes` array with this new string. Position: final element of the notes array for that entry.

```
Phase 4+ reopen awareness (2026-04-24): the artifact remains 'accepted' for downstream use; a Platform Gate reopen notice has been added to the blueprint markdown header per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A, DEC-RO-0f). Transitive upstream dependency on `arch.phase3-platform-gate-spec.v1` now carries PG-01.1/PG-07.1/PG-10.1 as remediation sub-gates. Engine sub-gate remediation landed via 8 agentic-engine PRs on 2026-04-24. Blueprint guidance and release doctrine are NOT reopened.
```

## Ordering

1. Apply the markdown block to each of the 7 blueprint files using identical text. Each insertion is at the same logical position (between the `## 1. Purpose` preceding paragraph and the §1 header). Do not reflow existing prose.
2. Open `docs/control-plane/artifact-registry.seed.json`, find each of the 7 blueprint artifact entries by `artifact_id`, append the notes[] string to each.
3. Single commit; single PR against `SaintFreddy/Canon:main`.

## Forbidden

- Do NOT modify any file outside `file_whitelist`.
- Do NOT change any blueprint's `artifact_status` (remains `accepted`).
- Do NOT rewrite, reorder, or trim existing prose in any blueprint. Only insert the reopen-notice block and the registry note.
- Do NOT change blueprint dependency_refs, source_authority_refs, or validation_hooks arrays.
- Do NOT touch Platform Gate spec markdown — it already carries the §0.1 + §7 reopen markup from PG-R1.
- Do NOT touch the maturity matrix or milestone architecture plan — those are PG-R3.
- Do NOT run a registry-apply or stale-propagation flag — this packet does NOT call `--apply-registry` on the stale-detection script. The 77 downstream-impacted artifacts remain with their existing `accepted` status; only the 7 blueprints gain a reopen note.

## Verification

- `git diff --stat` shows exactly 8 files changed (7 .md + 1 .json).
- `git diff docs/control-plane/implementation/release-blueprints/` shows the same structural block inserted at the same logical location in each of the 7 files.
- `git diff docs/control-plane/artifact-registry.seed.json` shows only 7 notes[] array appends — no other JSON fields touched.
- `python3 scripts/validators/validate_control_plane_integrity.py` remains green (or passes identically to before this PR).
- `python3 scripts/wrappers/run_phase7_stale_detection.py --changed-artifact arch.phase3-platform-gate-spec.v1` reports the same 77-artifact impact map with 7 blueprints visibly updated (not `stale`, but with notes indicating reopen awareness).
- PR body includes: (i) byte-level diff confirmation that all 7 blueprint reopen-notice blocks are identical text, (ii) byte-level diff confirmation that all 7 registry notes appends are identical text, (iii) confirmation that no other file was touched.

## What unblocks next

- **PG-R3** — maturity matrix (rel.chat-native-maturity-matrix.v1) + milestone architecture plan (rel.chat-native-milestone-architecture-plan.v1) receive the same reopen footnote pattern; after PG-R3 lands, the PG-01.1/PG-07.1/PG-10.1 sub-gates can be formally marked closed in the Platform Gate spec since all engine remediation has already landed.
- **Phase 6 materialization packets** (P06.x) — can open for satellite-repo runtime work once plan-owner names the first bounded materialization step; this packet does not prerequisite or block that path.
- **Engine-closure supersession lift** — the "locally closed" engine claim still formally superseded per canon-now.md Recommendation; PG-R3 closes that supersession by landing the last of the gate-reopen downstream sync.
