# pkt.quarantine-delete.v1

- **Packet ID**: `pkt.quarantine-delete.v1`
- **Authority**: DEC-RO-05 recorded at `canon-knowledgebase/post-reopen-decisions/condition-j.md`
- **Carry-forward**: CF-0096
- **Scope**: `SaintFreddy/Canon` control-plane only
- **Ordering**: HARD-GATED on `pkt.quarantine-invariant-sweep.v1`'s PR merging to main. This packet MUST NOT execute before Packet A has landed.
- **Execution mode**: Autonomous via `droid-issue-exec.yml`

## Gating check (first step in execution, before any file modification)

The executing droid MUST verify ALL of the following before proceeding:

1. The file `canon-knowledgebase/post-reopen-decisions/condition-j.md` exists on current `main` and names this packet as "Packet B."
2. A merged PR exists in `SaintFreddy/Canon` with title matching `Droid: [remediation] pkt.remediate-quarantine-invariant-sweep.v1` OR a PR whose body cites `pkt.quarantine-invariant-sweep.v1` and is in `merged` state. Use `gh pr list --repo SaintFreddy/Canon --state merged --search "quarantine-invariant-sweep"` to verify.
3. The invariant-sweep PR's diff touched `docs/spec-digests/` files (confirming the sweep actually ran) and did NOT touch `Canon/packages`, `Canon/services`, or `Canon/workers` (confirming Packet A respected its scope).

If ANY of these checks fail, the droid MUST stop, write `/tmp/droid-blocker.md` explaining which check failed, and exit cleanly per workflow rule 7.

## Goal

Physically remove the quarantined `Canon/packages/`, `Canon/services/`, `Canon/workers/` directories and reconcile phase-6 plan prose that still expects these directories to materialize in the Canon repo.

## Execution steps

1. **Pre-flight gate** (above). Stop if any check fails.

2. **Remove directories**:
   ```
   git rm -rf Canon/packages
   git rm -rf Canon/services
   git rm -rf Canon/workers
   ```
   Note: the paths above are relative to the repo root. If the repo root does not have a top-level `Canon/` directory (i.e., the Canon repo's own root IS the Canon workspace), adjust to `git rm -rf packages services workers`. Detect correctly at execution time: check if a top-level `packages/` exists in the repo vs a nested `Canon/packages/`.

3. **Reconcile phase-6 prose**. For each of the files below, grep for patterns that expect Canon to host packages/services/workers and reconcile with a statement referencing DEC-RO-05:
   - `docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md`
   - `docs/control-plane/core/master-plan.md`
   - `docs/control-plane/implementation/packets/**/*.md` (any that reference `Canon/packages|Canon/services|Canon/workers`)

   Reconciliation format: replace the "will materialize in Canon under apps/packages/services/workers" phrasing with:
   > *DEC-RO-05 (2026-04-24): Canon is control-plane + authority only; runtime lives in `agentic-engine`, `canon-apps`, `shared-environment`, `agentic-engine-history`. The quarantined draft roots (`Canon/packages/`, `Canon/services/`, `Canon/workers/`) were removed in `pkt.quarantine-delete.v1`. Git history preserves the 1,369 LOC for archaeology. See `canon-knowledgebase/post-reopen-decisions/condition-j.md`.*

4. **Sanity checks** (must all pass):
   - `ls Canon/packages Canon/services Canon/workers` returns "No such file or directory" (or equivalent for the chosen path).
   - `git log --oneline -- Canon/packages` still returns non-empty output (confirms history is preserved).
   - `grep -r "Canon/packages\|Canon/services\|Canon/workers" docs/ --exclude-dir=control-plane/implementation/packets/remediation` returns only the reconciliation-language additions from step 3 (no leftover expectations).
   - `pnpm typecheck` remains green (nothing depended on these directories).

5. **PR body must include**:
   - List of files removed (count, not full enumeration).
   - List of files reconciled (with quoted before/after snippets for the most important phase-6 prose changes).
   - Confirmation that Packet A's PR is cited as prerequisite and is merged.
   - Link to `canon-knowledgebase/post-reopen-decisions/condition-j.md`.

## Forbidden

- Do NOT execute before Packet A's PR is merged. The gating check at step 1 is hard-fail.
- Do NOT delete any file outside the 3 quarantined directories.
- Do NOT touch `canon-now.md`, `canon-knowledgebase/`, `AGENTIC_ENGINE_AUDIT_LOG.md`, `CANON_PLAN_IMPACT_REPORT.md`.
- Do NOT modify `.gitignore` to hide the removal. The removal must be visible in git history.
- Do NOT squash-force-push. Standard squash merge via auto-workflow is expected.

## Post-merge follow-ups (outside this packet's scope)

- Append CF-0098 to `canon-knowledgebase-layer-carry-forward.md` noting deletion complete + link to this PR. (Plan-owner or follow-up packet.)
- Update `canon-now.md` "Constraint" paragraph: remove the clause that says "quarantined code must stay on disk" — replace with "quarantined code was removed 2026-04-XX per DEC-RO-05." (Plan-owner, since canon-now.md is human-owned.)
- Verify no other repo has stale references to `Canon/packages|Canon/services|Canon/workers` (spot-check `agentic-engine`, `canon-apps`, `shared-environment`, `agentic-engine-history`).
