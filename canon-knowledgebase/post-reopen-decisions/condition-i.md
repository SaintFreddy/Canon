# Accepted Decision: Condition (i) — Successor checkpoint for sufficiency claim

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule.

## Plan-owner authority

SaintFreddy (delegated recommendation).

## Accepted option

**Option A (Section 6 row 12 default)** — supersede `post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md` with the new checkpoint naming stableStringify + Clock + localeCompare + PROV-002/004 as open. Keeps append-only posture.

## Decision statement

- `canon-knowledgebase/post-reopen-audit-cited-contradiction-checkpoint.md` (already exists on disk as of 2026-04-19) is the durable successor.
- `canon-knowledgebase/post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md` is formally marked `SUPERSEDED by post-reopen-audit-cited-contradiction-checkpoint` in its header. The file is NOT deleted (append-only history preserved).
- `canon-now.md` fresh-session handoff reflects the successor relationship (already done in the 2026-04-19 edit recorded in `canon-now.md`).
- No code changes required.

## Rationale summary

- The successor checkpoint file already exists, so Option A is mechanically complete; this record just closes the plan-owner decision formally.
- Option B (retain and add inline corrective notes) creates two live checkpoints with inconsistent authority — bad for fresh-session recovery.

## What this unblocks

- Condition (i) tracking closes. No remediation packet needed beyond the header-markup edit.
- Fresh sessions reading the old checkpoint file immediately see `SUPERSEDED` and redirect to the current authority.

## New constraints accepted

1. `post-reopen-frozen-posture-replay-audit-sufficiency-checkpoint.md` header must contain an explicit `SUPERSEDED` stanza naming the successor. To be added in a micro-edit alongside the Platform Gate reopen packet (control-plane wave).
2. No content from the superseded file is deleted.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 12.

## Execution posture

- Packet: absorbed into `pkt.remediate-platform-gate-truth-status.v1` as a micro-edit (header markup on the superseded file). No standalone packet.
- Verification: old checkpoint file header contains `SUPERSEDED by post-reopen-audit-cited-contradiction-checkpoint`; `canon-now.md` fresh-session handoff references the successor.
