# Remediation packet — Platform Gate sub-gate closure
Version: 1.0
Status: Draft (scaffold)
Task: Phase 4+ post-step-20 — Platform Gate sub-gate closure and engine-closure supersession lift
Artifact ID: pkt.platform-gate-subgate-closure.v1
Prerequisite: `pkt.platform-gate-downstream-maturity-milestone-sync.v1` (PG-R3) landed on `SaintFreddy/Canon` main (Canon PR #39, merged 2026-04-24)
Target repo: `SaintFreddy/Canon` (control-plane + authority record, doc sync)

Scaffold authored after PG-R3 landing per CF-0099. Executes the final act in the DEC-RO-0f Option A remediation sequence: formally flip the Platform Gate §0.1.1 sub-gates PG-01.1 / PG-07.1 / PG-10.1 from `pending` to `closed`, retire the "pending sub-gates" clause from the authority record (`canon-now.md` + `canon-knowledgebase/canon-phase-4-plus-plan.md`), and lift the engine-closure "locally closed" supersession.

All engine-side sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (CF-0089..CF-0096). Downstream doc propagation landed via Canon PR #17 (PG-R1), Canon PR #35 (PG-R2), and Canon PR #39 (PG-R3). The remediation authority chain is complete — this packet is the final doc-sync act that closes the sub-gate triple.

## Packet brief

```json
{
  "packet_id": "pkt.platform-gate-subgate-closure.v1",
  "title": "Flip Platform Gate §0.1.1 sub-gates PG-01.1 / PG-07.1 / PG-10.1 from pending to closed and retire the 'pending sub-gates' authority-record clauses",
  "task_id": "P4p.post-step-20.pg-subgate-closure",
  "objective": "The Platform Gate spec §0.1.1 sub-gate table flips all three sub-gates from `pending` to `closed` with citations to the engine-side remediation PRs that landed 2026-04-24. Both authority records (`canon-now.md` Recommendation block and `canon-knowledgebase/canon-phase-4-plus-plan.md` step 20 closure note) have their 'pending sub-gates' / 'PG-R2 and PG-R3 land' language retired in favor of the now-landed wave closure. After this packet, the engine-closure 'locally closed' supersession is formally lifted; the Platform Gate acceptance marker still reads `reopened 2026-04-18 → closed via PG-R1/R2/R3/subgate-closure 2026-04-24`, not a full revert to the prior `passed` marker (per DEC-RO-0f Option A's append-only-history discipline).",
  "scope": [
    "Edit `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 reopen-marker line + §0.1.1 sub-gate table + §0.1.2 baton-continuation language + §7 checklist reopen marker to reflect closure",
    "Edit `canon-now.md` Recommendation block 'User-selected bounded task' bullet to retire the 'PG-R2 and PG-R3 land' clause and record the supersession lift",
    "Edit `canon-knowledgebase/canon-phase-4-plus-plan.md` step 20 'next bounded execution step' block to retire the 'Platform Gate follow-ups PG-R2 / PG-R3' clause now that both have landed",
    "No other file changes in this PR — CF-0100 landing entry is a separate PR"
  ],
  "out_of_scope": [
    "Any agentic-engine code change",
    "Reverting the Platform Gate acceptance marker to the prior `passed` line — DEC-RO-0f Option A preserves `Gate passed` as append-only history; sub-gate closure does NOT reactivate that marker",
    "Editing `AGENTIC_ENGINE_AUDIT_LOG.md`, `CANON_PLAN_IMPACT_REPORT.md`, `AGENTIC_WORKFLOW.md`, `canon-knowledgebase/post-reopen-decisions/`",
    "Editing CF ledger entries in this packet — CF-0100 is a separate landing-record PR",
    "Changing Platform Gate §0 or §7 core body text beyond the targeted reopen/checklist markers identified below",
    "Rewriting the §0.1.2 Downstream posture downstream-doc-sync narrative about PG-R2 / PG-R3 (those descriptions remain accurate historical records)",
    "Any registry (artifact-registry.seed.json) or graph (dependency-graph.seed.json) edit — Platform Gate artifact itself remains `accepted`",
    "Touching Phase 6 blueprints, maturity matrix, milestone architecture plan (all already carry the reopen notice from PG-R2 / PG-R3 and retain their current `accepted` status)"
  ],
  "source_authority_refs": [
    "canon-knowledgebase/post-reopen-decisions/condition-f.md (DEC-RO-0f, Option A — formal reopen with sub-gates PG-01.1 / PG-07.1 / PG-10.1; append-only-history discipline; sub-gate-closure is the final act)",
    "canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md CF-0089..CF-0096 (engine-side sub-gate remediation PRs 2026-04-24)",
    "canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md CF-0097 (step 20 closure), CF-0098 (PG-R2 landing), CF-0099 (PG-R3 landing + sub-gate-closure unblock + explicit scope enumeration)",
    "docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md (current §0.1 / §0.1.1 / §0.1.2 / §7 reopen markup — targets of this packet)",
    "canon-now.md (current Recommendation block 'User-selected bounded task' bullet — target of this packet)",
    "canon-knowledgebase/canon-phase-4-plus-plan.md (current step 20 'next bounded execution step' block — target of this packet)"
  ],
  "file_whitelist": [
    "docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md",
    "canon-now.md",
    "canon-knowledgebase/canon-phase-4-plus-plan.md"
  ],
  "deliverables": [
    "Platform Gate spec §0.1 + §0.1.1 + §0.1.2 + §7 text flipped from pending-sub-gate posture to closed-sub-gate posture using the exact target strings in §'Exact edit targets' below",
    "canon-now.md Recommendation 'User-selected bounded task' bullet reworded to reflect the lift",
    "canon-phase-4-plus-plan.md step 20 next-bounded-step block reworded to reflect the lift",
    "Single PR against SaintFreddy/Canon:main",
    "No other file changes in this PR"
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
  "model_rationale": "Sub-gate-closure is authority-record-sensitive: it flips the Platform Gate sub-gate table status and retires two separate 'pending' clauses in two authority files (canon-now.md + canon-phase-4-plus-plan.md) that must stay internally consistent. The correctness gate is 'every PG-01.1/PG-07.1/PG-10.1 reference flips to closed status in a mutually-consistent way, AND the DEC-RO-0f Option A append-only-history discipline is preserved (Gate passed line stays, reopen line stays, closure is recorded as a new state not a revert)'. That cross-file consistency + append-only-history nuance benefits from Opus's long-context rigor. GPT-5's bounded-template advantage is not well-matched here because the 3 files have 3 different editing patterns (table-cell flips + blockquote retirements + inline-bullet rewrites)."
}
```

## Exact edit targets

### File 1 — `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md`

Four surgical edits within the accepted Platform Gate spec:

#### Edit 1a — §0.1 reopen marker line

**Replace** (exact line 40):

```
- Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`.
```

**With**:

```
- Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1` (all three sub-gates closed 2026-04-24 via the engine-side remediation PRs referenced in §0.1.1; the reopen event itself is preserved as append-only history per DEC-RO-0f Option A, so this spec does NOT revert the §7 audit-checklist header to the prior `Gate passed` line).
```

#### Edit 1b — §0.1.1 Remediation sub-gates introductory paragraph

**Replace**:

```
Three remediation sub-gates close the reopen. They must each land before
the Platform Gate acceptance marker returns to `passed`.
```

**With**:

```
Three remediation sub-gates close the reopen. All three landed on `SaintFreddy/agentic-engine` main on 2026-04-24. The Platform Gate acceptance marker does NOT automatically revert to `passed` — DEC-RO-0f Option A keeps `Gate passed` as append-only history in §7 and keeps this reopen event recorded alongside it as the new substrate-truth. The sub-gate table below records the closure status and citation evidence for each sub-gate.
```

#### Edit 1c — §0.1.1 sub-gate table (add a Status column and flip all three to closed)

**Replace** (the 4-line table block — header + separator + 3 rows):

```
| Sub-gate | Closes when |
| --- | --- |
| `PG-01.1` | engine `Clock` abstraction landed in `@canon/engine-core` with Shared Env production impl; `stableStringify` unified in `@canon/engine-core`; `localeCompare` purged from replay-sensitive sort paths; `frozenAt` placement decision recorded and implemented (condition (a), condition (d), and the `frozenAt` hash-inclusion sub-decision). |
| `PG-07.1` | engine-owned `CredentialProvider` and hardened `validateCredentialScope` landed per condition (b) sub-decision B-1 Option A. |
| `PG-10.1` | `spawnToolSandboxWorker` forks a real Node child and `attachToolSandboxWorkerIpc` is shipped on `contracts/exports.json` per condition (b) sub-decisions B-2 and B-3 Option A. |
```

**With**:

```
| Sub-gate | Status | Closes when | Closure evidence |
| --- | --- | --- | --- |
| `PG-01.1` | closed 2026-04-24 | engine `Clock` abstraction landed in `@canon/engine-core` with Shared Env production impl; `stableStringify` unified in `@canon/engine-core`; `localeCompare` purged from replay-sensitive sort paths; `frozenAt` placement decision recorded and implemented (condition (a), condition (d), and the `frozenAt` hash-inclusion sub-decision). | `SaintFreddy/agentic-engine` PRs for Clock, thaw-timestamp, localeCompare, frozenAt-in-hashed-doc, stableStringify (see CF-0089..CF-0096 in `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md`). |
| `PG-07.1` | closed 2026-04-24 | engine-owned `CredentialProvider` and hardened `validateCredentialScope` landed per condition (b) sub-decision B-1 Option A. | `SaintFreddy/agentic-engine` credentialScope-enforcement PR (see CF-0089..CF-0096). |
| `PG-10.1` | closed 2026-04-24 | `spawnToolSandboxWorker` forks a real Node child and `attachToolSandboxWorkerIpc` is shipped on `contracts/exports.json` per condition (b) sub-decisions B-2 and B-3 Option A. | `SaintFreddy/agentic-engine` toolSandboxWorker-fork PR (see CF-0089..CF-0096). |
```

#### Edit 1d — §0.1.2 Downstream posture baton-continuation paragraph

**Replace**:

```
- Ordinary baton continuation remains paused under `canon-now.md`
  `Baton state: stop — audit-reopen hold` until PG-01.1, PG-07.1, and
  PG-10.1 close and the remaining reopen-resolution conditions are
  decided.
```

**With**:

```
- Ordinary baton continuation was paused under `canon-now.md`
  `Baton state: stop — audit-reopen hold` while PG-01.1, PG-07.1, and
  PG-10.1 were open; all three sub-gates closed 2026-04-24 alongside
  the remaining reopen-resolution conditions (see CF-0089..CF-0099 in
  `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md`),
  so the baton is now in `Baton state: ready` pending plan-owner
  selection of the next bounded step.
```

#### Edit 1e — §7 Exit-audit checklist reopen marker footnote

**Replace**:

```
> Gate reopened — audit-cited contradiction event 2026-04-18. The prior
> `Gate passed` line above is preserved as append-only history per
> `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A,
> recorded 2026-04-23). Platform Gate's next status is
> `pending PG-01.1 + PG-07.1 + PG-10.1`. See §0.1 for the remediation
> sub-gates and successor-checkpoint reference.
```

**With**:

```
> Gate reopened — audit-cited contradiction event 2026-04-18. The prior
> `Gate passed` line above is preserved as append-only history per
> `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A,
> recorded 2026-04-23). Sub-gates PG-01.1 / PG-07.1 / PG-10.1 all
> closed 2026-04-24 (see §0.1.1 for closure evidence); under DEC-RO-0f
> Option A's append-only-history discipline, this §7 audit-checklist
> header preserves `Gate passed` as prior-state history and does NOT
> revert to that marker. See §0.1 for the full reopen record and
> successor-checkpoint reference.
```

### File 2 — `canon-now.md`

One surgical edit in the Recommendation block.

#### Edit 2a — 'User-selected bounded task' bullet

**Replace** (exact bullet paragraph, including the leading `- ` marker):

```
- User-selected bounded task: `agentic-engine-finish-session-plan.md` through Session 6 remains complete locally. The engine-closure posture reopened under cited-contradiction review is now resolved: the engine seam is restored to a more-rigorous closed state via the 8 agentic-engine remediation PRs landed today (credentialScope + toolSandboxWorker + Clock + stableStringify + policy-matcher + replay-compare + engine-version 0.1.0 + LICENSE). The "locally closed" claim is still formally superseded until Phase-4+ plan step 20 and Platform Gate follow-up packets PG-R2 and PG-R3 land; those are candidates for the next bounded step.
```

**With**:

```
- User-selected bounded task: `agentic-engine-finish-session-plan.md` through Session 6 remains complete locally. The engine-closure posture reopened under cited-contradiction review is now resolved: the engine seam is restored to a more-rigorous closed state via the 8 agentic-engine remediation PRs landed 2026-04-24 (credentialScope + toolSandboxWorker + Clock + stableStringify + policy-matcher + replay-compare + engine-version 0.1.0 + LICENSE). The prior "locally closed" supersession is now formally lifted: Phase-4+ plan step 20 closed 2026-04-24 (CF-0097), Platform Gate follow-ups PG-R2 (Canon PR #35, CF-0098) and PG-R3 (Canon PR #39, CF-0099) landed 2026-04-24, and Platform Gate §0.1.1 sub-gates PG-01.1 / PG-07.1 / PG-10.1 all closed 2026-04-24 via this packet. Plan-owner names the next bounded step.
```

### File 3 — `canon-knowledgebase/canon-phase-4-plus-plan.md`

One surgical edit in the step 20 next-bounded-step block.

#### Edit 3a — step 20 next-bounded-step line

**Replace** (exact line):

```
  - step 20 — audit-cited-contradiction reopen gate — `complete` as of 2026-04-24. Ordinary baton continuation is cleared to resume; the next bounded step is **unassigned** pending plan-owner selection from the stage plan below (Platform Gate follow-ups PG-R2 / PG-R3, or any `R1`..`R7` stage entry). No step auto-activates under the audit-reopen hold lift; see `canon-ref:dev/canon-now` for the ready-state baton record and the CF-0089..CF-0096 carry-forward chain for the full wave-closure evidence.
```

**With**:

```
  - step 20 — audit-cited-contradiction reopen gate — `complete` as of 2026-04-24. Ordinary baton continuation is cleared to resume; the next bounded step is **unassigned** pending plan-owner selection from the stage plan below (any `R1`..`R7` stage entry). The Platform Gate three-packet downstream propagation sequence (PG-R1 Canon PR #17, PG-R2 Canon PR #35, PG-R3 Canon PR #39) has landed, and Platform Gate §0.1.1 sub-gates PG-01.1 / PG-07.1 / PG-10.1 all closed 2026-04-24 via `pkt.platform-gate-subgate-closure.v1`, lifting the prior engine-closure "locally closed" supersession. No step auto-activates under the audit-reopen hold lift; see `canon-ref:dev/canon-now` for the ready-state baton record and the CF-0089..CF-0100 carry-forward chain for the full wave-closure evidence.
```

## Ordering

1. Apply Edit 1a → Edit 1b → Edit 1c → Edit 1d → Edit 1e in the Platform Gate spec file in a single pass.
2. Apply Edit 2a in `canon-now.md` in a single pass.
3. Apply Edit 3a in `canon-knowledgebase/canon-phase-4-plus-plan.md` in a single pass.
4. Single commit; single PR against `SaintFreddy/Canon:main`.
5. CF-0100 (packet landing + engine-closure supersession lift record) is a separate PR after this one merges.

## Forbidden

- Do NOT modify any file outside `file_whitelist`.
- Do NOT change `arch.phase3-platform-gate-spec.v1` artifact_status in the registry — it remains `accepted`.
- Do NOT revert the §7 `Gate passed` header to an active `passed` marker — DEC-RO-0f Option A keeps it as append-only history. Sub-gate closure does not revert the reopen event.
- Do NOT rewrite §0 core text (before `### 0.1 Reopen — audit-cited contradiction event 2026-04-18`), §2-§6 body text, or §8-§10 body text. Only touch the exact target strings in §'Exact edit targets'.
- Do NOT rewrite §0.1.2 downstream-posture paragraphs OTHER than the targeted baton-continuation paragraph (Edit 1d). The PG-R2 / PG-R3 descriptive sentences stay as historical record.
- Do NOT touch Platform Gate §0.1 `Authority-preservation rule` paragraph (the §0/§7 verbatim-preservation clause is still active — sub-gate closure does not touch §7 body, only the reopen-marker footnote at the top of §7).
- Do NOT edit CF ledger entries in this packet.
- Do NOT touch registry or graph seed JSON files.
- Do NOT touch blueprints or maturity matrix / milestone plan .md files — those already carry the PG-R2 / PG-R3 reopen notice and remain accurate.
- Do NOT delete any historical text; only targeted replacements are permitted.

## Verification

- `git diff --stat` shows exactly 3 files changed.
- `git diff docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` shows exactly the 5 targeted edits (1a..1e) and nothing else.
- `git diff canon-now.md` shows exactly Edit 2a and nothing else.
- `git diff canon-knowledgebase/canon-phase-4-plus-plan.md` shows exactly Edit 3a and nothing else.
- `python3 scripts/validators/validate_control_plane_integrity.py` returns `status: pass, issues: []` with 111 artifacts and 1424 graph edges (unchanged).
- The §7 `Gate passed` header line is still present verbatim as prior-state history (append-only discipline preserved).
- The `## 0.1 Reopen — audit-cited contradiction event 2026-04-18` header is still present verbatim.
- PR body includes: (i) confirmation that 5 Platform Gate edits land together and nothing else in that file, (ii) confirmation that canon-now.md and canon-phase-4-plus-plan.md each get exactly one targeted edit, (iii) confirmation that §7 append-only `Gate passed` line is preserved, (iv) explicit note that CF-0100 will land as a separate PR.

## What unblocks next

- **CF-0100 append** — single-file PR to `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` recording this packet's landing and the formal lift of the engine-closure "locally closed" supersession. After CF-0100 lands, the entire DEC-RO-0f Option A remediation sequence (PG-R1 → PG-R2 → PG-R3 → sub-gate closure) is complete.
- **Plan-owner next bounded step selection** — Canon is fully ready to accept any of: (a) Phase 6 materialization pilot packets against satellite repos, (b) second-model review pass over today's 25 merged PRs, (c) stop for the day.
- **No further Platform Gate reopen-related packets** are expected. The next reopen event would require a fresh cited-contradiction trigger per `canon-phase-4-plus-plan.md §157`.
