# Remediation packet — Platform Gate downstream maturity/milestone sync (PG-R3)
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ post-step-20 — Platform Gate reopen downstream propagation (PG-R3)
Artifact ID: pkt.platform-gate-downstream-maturity-milestone-sync.v1
Prerequisite: `pkt.platform-gate-downstream-blueprint-sync.v1` (PG-R2) landed on `SaintFreddy/Canon` main (Canon PR #35, merged 2026-04-24)
Target repo: `SaintFreddy/Canon` (control-plane only, doc sync)

Scaffold authored after PG-R2 landing per CF-0098. Executes the "maturity-matrix + milestone-architecture-plan footnote sync" path explicitly named in `canon-knowledgebase/post-reopen-decisions/condition-f.md` as PG-R3 and flagged in PG-R2's "What unblocks next" section.

This packet is control-plane-only — no `agentic-engine` code changes. It propagates the Platform Gate reopen acknowledgement from the gate spec (PG-R1) through to the last two Phase 4 accepted release authorities that transitively depend on it, so downstream consumers reading either authority cannot miss the reopen context.

## Packet brief

```json
{
  "packet_id": "pkt.platform-gate-downstream-maturity-milestone-sync.v1",
  "title": "Propagate Platform Gate reopen status into the Phase 4 maturity matrix and milestone architecture plan",
  "task_id": "P4p.post-step-20.pg-r3",
  "objective": "The two accepted Phase 4 release authorities (rel.chat-native-maturity-matrix.v1 and rel.chat-native-milestone-architecture-plan.v1) each receive a uniformly-formatted 'Platform Gate reopen notice' block placed immediately before their `## 1. Purpose` header, plus a corresponding registry note appended to each artifact's entry in docs/control-plane/artifact-registry.seed.json. After this packet, no accepted Phase 4 release authority can be read in isolation without the reopen context being surfaced. Authority guidance itself is not rewritten; downstream consumers retain the accepted release doctrine and package-maturity floors.",
  "scope": [
    "Add a uniform 'Platform Gate reopen notice (2026-04-23)' block to the 2 target .md files under docs/control-plane/releases/",
    "Append one new note string to each of the 2 corresponding artifact-registry.seed.json entries",
    "No changes to any other file"
  ],
  "out_of_scope": [
    "Any agentic-engine code change",
    "Release blueprints (bp.phase6-r1..r7) — those were PG-R2 scope and already landed (Canon PR #35)",
    "Platform Gate spec itself (PG-R1 already landed)",
    "Release contract packs (9 rel.release_contract_pack artifacts with rel.r1..r7 lineage) — not in PG-R3 scope",
    "Phase 6 execution packets (26 pkt.execution_packet artifacts) — not in PG-R3 scope",
    "Surface packs, control-plane datasets, reuse packs — not in PG-R3 scope",
    "Editing AGENTIC_ENGINE_AUDIT_LOG.md, CANON_PLAN_IMPACT_REPORT.md, AGENTIC_WORKFLOW.md, or any canon-knowledgebase/ record",
    "Changing artifact_status on either target (both remain 'accepted' — reopen is surfaced via a new note, not a status flip)",
    "Flipping Platform Gate spec §0.1.1 sub-gates (PG-01.1 / PG-07.1 / PG-10.1) from pending to closed — that is a separate sub-gate-closure packet that is hard-gated on this packet landing",
    "Rewriting existing §0 Convergence status prose in either target",
    "Rewriting any body section (§1 Purpose and below) in either target"
  ],
  "source_authority_refs": [
    "canon-knowledgebase/post-reopen-decisions/condition-f.md (DEC-RO-0f, Option A)",
    "docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md §0.1 (PG-R1 landed markup)",
    "docs/control-plane/implementation/packets/remediation/pkt.platform-gate-downstream-blueprint-sync.v1.md (PG-R2 landed scaffold — structural template)",
    "docs/control-plane/artifact-registry.seed.json (rel.chat-native-maturity-matrix.v1 and rel.chat-native-milestone-architecture-plan.v1 entries; bp.phase6-r1-conversation-blueprint.v1 note for precedent format)",
    "canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md CF-0097 (step 20 closure) and CF-0098 (PG-R2 landing + PG-R3 unblock)",
    "canon-now.md (baton: ready)"
  ],
  "file_whitelist": [
    "docs/control-plane/releases/chat-native-maturity-matrix/phase-4-release-to-sdk-maturity-matrix.md",
    "docs/control-plane/releases/chat-native-milestone-architecture-plan/phase-4-release-milestone-architecture-plan.md",
    "docs/control-plane/artifact-registry.seed.json"
  ],
  "deliverables": [
    "2 release-authority .md files each with identical structural reopen-notice block inserted at the same logical position (immediately before `## 1. Purpose`)",
    "2 registry entries each with one new notes[] string appended (position: after existing notes, not inserted in between)",
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
  "reasoning_effort": "high",
  "model_rationale": "PG-R3 is uniform-template coordinated edits across 2 authority .md files + 1 JSON registry, with strict byte-identical text discipline and multi-authority citation requirements. Opus 4.7 high-reasoning is preferred over GPT-5 tight-instruction-following because the correctness gate is 'reopen notice must land at the same logical position in two structurally-similar-but-not-identical files, with authority-citation text exactly mirroring PG-R2's landed block, without rewriting any existing §0 Convergence status prose.' That class of work benefits from Opus's long-context rigor over 15-20 tool calls; GPT-5's advantage on bounded-template scope is marginal here since PG-R2 (same task shape) was already executed on Opus successfully."
}
```

## Uniform reopen-notice block (exact template to insert into each target .md)

The block MUST be inserted immediately before the existing `## 1. Purpose` header in each of the 2 target files. This places the notice AFTER the top artifact-ID header block AND the existing `## 0. Convergence status (Phase 4+ update)` section, and BEFORE the `## 1. Purpose` header. This position is the same "structurally parallel to PG-R2" position: reopen context is surfaced as the last thing a reader sees before entering the artifact's §1 body.

Use the SAME text verbatim in both files — only the file-path context differs; the content of the notice is identical.

```markdown
> **Platform Gate reopen notice (2026-04-23).** This artifact transitively depends on `arch.phase3-platform-gate-spec.v1`. On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the Platform Gate P3.6 acceptance marker against the 2026-04-18 agentic-engine audit-cited contradiction event per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A). Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`. This artifact itself remains `accepted` for downstream use — the release doctrine and package-maturity guidance below are unchanged and are not reopened. Consumers reading this artifact should, however, be aware that PG-01.1 (Clock + stableStringify + localeCompare + frozenAt), PG-07.1 (credentialScope enforcement), and PG-10.1 (spawnToolSandboxWorker + IPC export) are remediation sub-gates still closing. Engine sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (see `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0089..CF-0096); downstream blueprint propagation landed via Canon PR #35 (PG-R2, see CF-0098). The sub-gates formally close after the small sub-gate-closure packet flips PG-01.1 / PG-07.1 / PG-10.1 from pending to closed in the Platform Gate spec §0.1.1, which is hard-gated on this packet (PG-R3) landing. See `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 for the full gate reopen markup and successor-checkpoint reference.
```

## Uniform registry notes[] append (exact template to add to each target's entry)

Append — DO NOT replace — the existing `notes` array with this new string. Position: final element of the notes array for that entry.

```
Phase 4+ reopen awareness (2026-04-24): the artifact remains 'accepted' for downstream use; a Platform Gate reopen notice has been added to the artifact markdown header per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A, DEC-RO-0f). Transitive upstream dependency on `arch.phase3-platform-gate-spec.v1` now carries PG-01.1/PG-07.1/PG-10.1 as remediation sub-gates. Engine sub-gate remediation landed via 8 agentic-engine PRs on 2026-04-24; downstream blueprint propagation landed via Canon PR #35 (PG-R2). Release doctrine and package-maturity/milestone guidance are NOT reopened.
```

## Ordering

1. Apply the markdown block to each of the 2 target files using identical text. Each insertion is immediately before the `## 1. Purpose` header (i.e., at the end of the existing `## 0. Convergence status (Phase 4+ update)` section, separated by one blank line above and one blank line below the blockquote). Do not reflow existing prose.
2. Open `docs/control-plane/artifact-registry.seed.json`, find each of the 2 release-authority artifact entries by `artifact_id`, append the notes[] string to each.
3. Single commit; single PR against `SaintFreddy/Canon:main`.

## Forbidden

- Do NOT modify any file outside `file_whitelist`.
- Do NOT change either target's `artifact_status` (both remain `accepted`).
- Do NOT rewrite, reorder, or trim existing prose in either target. Only insert the reopen-notice block and the registry note.
- Do NOT rewrite or edit the existing `## 0. Convergence status (Phase 4+ update)` sections — those record prior P3.6/P4/P5/P6/P7 convergence context and are preserved verbatim.
- Do NOT change target dependency_refs, source_authority_refs, or validation_hooks arrays in the registry.
- Do NOT touch Platform Gate spec markdown — it already carries the §0.1 + §7 reopen markup from PG-R1.
- Do NOT touch any of the 7 Phase 6 release blueprints — those already carry the PG-R2 notice.
- Do NOT touch the Platform Gate spec §0.1.1 sub-gates (PG-01.1 / PG-07.1 / PG-10.1) status — that is the next packet after this one.
- Do NOT run a registry-apply or stale-propagation flag — this packet does NOT call `--apply-registry` on the stale-detection script. The downstream-impacted artifacts remain with their existing `accepted` status; only the 2 targets gain a reopen note.

## Verification

- `git diff --stat` shows exactly 3 files changed (2 .md + 1 .json).
- `git diff docs/control-plane/releases/` shows the same structural block inserted at the same logical location (immediately before `## 1. Purpose`) in each of the 2 target files.
- `git diff docs/control-plane/artifact-registry.seed.json` shows only 2 notes[] array appends — no other JSON fields touched.
- `python3 scripts/validators/validate_control_plane_integrity.py` remains green (or passes identically to before this PR) — must report `status: pass` with same artifact count and same graph-edge count as the pre-PR baseline.
- PR body includes: (i) byte-level diff confirmation that both reopen-notice blocks are identical text, (ii) byte-level diff confirmation that both registry notes appends are identical text, (iii) confirmation that no other file was touched, (iv) confirmation that §0 Convergence status prose was NOT modified in either file.

## What unblocks next

- **Sub-gate closure packet** (`pkt.platform-gate-subgate-closure.v1`, to be authored after this lands) — flips `arch.phase3-platform-gate-spec.v1` §0.1.1 sub-gates PG-01.1 / PG-07.1 / PG-10.1 from `pending` to `closed`, retires the "pending sub-gates" clause from `canon-now.md` Recommendation and from the `canon-phase-4-plus-plan.md` step 20 closure note, and appends a carry-forward entry. After that packet lands, the engine-closure "locally closed" supersession is formally lifted and the three-packet Platform Gate remediation sequence (PG-R1 → PG-R2 → PG-R3 → sub-gate-closure) is complete.
- **Phase 6 materialization packets** (P06.x) — can open for satellite-repo runtime work once plan-owner names the first bounded materialization step; this packet does not prerequisite or block that path.
- **Second-model review pass** — optional review of the 25 PRs merged 2026-04-24 using the model not chosen for original authoring; can run in parallel with or after this packet.
