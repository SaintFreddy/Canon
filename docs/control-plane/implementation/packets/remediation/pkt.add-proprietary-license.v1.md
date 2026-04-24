# pkt.add-proprietary-license.v1

- **Packet ID**: `pkt.add-proprietary-license.v1`
- **Authority**: DEC-RO-04 recorded at `canon-knowledgebase/post-reopen-decisions/condition-e-license.md`
- **Carry-forward**: CF-0095
- **Scope**: All 5 repos (Canon, agentic-engine, canon-apps, shared-environment, agentic-engine-history) + 1 doc update in Canon repo only
- **Ordering**: Independent (no packet dependencies); safe to parallelize with wave-B packets after this lands
- **Execution mode**: Autonomous via `droid-issue-exec.yml` on each repo. For cross-repo consistency, a single coordinator issue on `SaintFreddy/Canon` kicks off, packet requires the droid to open 5 PRs (1 per repo) via `gh api` on each target. Alternative simpler execution: open 5 separate issues, one per repo, each with a narrower scope.

## Prerequisite

DEC-RO-04 recorded (confirmed via in-repo `canon-knowledgebase/post-reopen-decisions/condition-e-license.md` — landed 2026-04-24 per CF-0095).

## Goal

Install the Proprietary LICENSE file at the root of every repo and reconcile the public-SDK phrasing in `AGENTIC_WORKFLOW.md §9` so the documented posture matches the recorded decision.

## Exact LICENSE text

Both new LICENSE files and reconciled AGENTIC_WORKFLOW.md must use the text verbatim from `condition-e-license.md`:

```
Copyright (c) 2026 SaintFreddy. All rights reserved.

This source code and all associated files are proprietary and confidential.
No license, express or implied, is granted to any person or entity for use,
copy, modification, distribution, or creation of derivative works of this
source code, in whole or in part, except as expressly authorized in writing
by the copyright holder.
```

## File whitelist

### In `SaintFreddy/Canon`:
- `LICENSE` — create at repo root with exact text above. If a LICENSE file already exists, overwrite with the Proprietary text (any prior license was not accepted authority; the decision record is definitive).
- `AGENTIC_WORKFLOW.md` — reconcile §9 L426 "public SDK posture" phrasing. Options:
  - Variant A (preferred): mark the phrase as "aspirational, not current license posture under DEC-RO-04 (2026-04-24); see `canon-knowledgebase/post-reopen-decisions/condition-e-license.md` for the current posture and revisit conditions."
  - Variant B: remove the phrasing entirely.
  The packet executor must pick **Variant A** (preserves the aspiration for future revisit) unless §9 structure makes that awkward, in which case it picks Variant B and documents the choice in the PR body.

### In `SaintFreddy/agentic-engine`, `SaintFreddy/canon-apps`, `SaintFreddy/shared-environment`, `SaintFreddy/agentic-engine-history`:
- `LICENSE` — create at repo root with exact text above. Overwrite if present.

### Also in Canon only:
- `docs/control-plane/core/master-plan.md` — if it cites LICENSE status as "pending" or "aspirational public SDK", reconcile to reference DEC-RO-04 with the Proprietary posture.
- `CANON_PLAN_IMPACT_REPORT.md` — append a row to §6 row 6 noting DEC-RO-04 landed on Option 4. This file is marked read-only in `canon-now.md`, so this is the ONE exception authorized by the decision record. The append must be a single new row at the end of §6's decision ledger, not a modification of existing rows.

## Verification

- `cat LICENSE` in each repo returns the exact text above, byte-for-byte.
- `grep -c "public SDK posture" AGENTIC_WORKFLOW.md` in Canon either returns 0 (Variant B) or the remaining hits are inside the "aspirational / revisit" markup block (Variant A).
- All 5 repos' build / test / typecheck suites remain green after the LICENSE file is added (LICENSE files do not affect builds).
- Opens 5 separate PRs, 1 per repo. Canon's PR is the largest (LICENSE + AGENTIC_WORKFLOW + master-plan + impact-report). The other 4 are single-file PRs.

## Forbidden

- Do NOT license any file under any other posture.
- Do NOT commit a SPDX header ("SPDX-License-Identifier: ...") in source files — that would contradict the proprietary posture. If existing files have SPDX headers, DO NOT modify them in this packet; raise a future packet for that cleanup.
- Do NOT touch `canon-now.md`, `canon-knowledgebase/`, `AGENTIC_ENGINE_AUDIT_LOG.md`.
