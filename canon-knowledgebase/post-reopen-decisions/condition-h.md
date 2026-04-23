# Accepted Decision: Condition (h) — Replay-compare diff-semantics

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule.

## Plan-owner authority

SaintFreddy (delegated recommendation).

## Accepted option

**Option A (Section 6 row 9 default)** — add an explicit id-aligned diff variant; document positional-index semantics as dangerous but retained for backwards compatibility.

## Decision statement

- `workers/replay-compare/src/diff.ts` adds a new `diffByStableId()` function alongside the existing positional-index diff.
- `diffByStableId()` keys on each object's stable identity (e.g., `AgentIdentity.id`, `ArtifactObject.id`, etc.) to align entries across the two sides of the comparison; the diff reports added / removed / modified with the stable id as the anchor.
- The positional-index diff is preserved but its JSDoc gains an explicit warning: "positional diff compares entries at the same array index; reordering produces false positives. Prefer `diffByStableId` when comparing collections whose entries have stable ids."
- Platform Gate spec and R3 blueprint add a note referencing the id-aligned variant as the production path for exact-replay evaluation; positional diff is documented as "development / historical" only.

## Rationale summary

- Section 6 row 9 default is Option A: id-aligned diff matches the hashed-context invariant and avoids false-positive churn from reorderings.
- Option B (deprecate positional-index diff entirely) is cleaner but breaks any existing consumer without a migration. Option A keeps both paths alive with clear preference ordering.
- Matches R3 blueprint's implicit assumption: replay-compare produces id-keyed deltas.

## What this unblocks

- `pkt.remediate-replay-compare-diff-semantics.v1` (new packet scaffold authored on this pass).
- Precondition for R3 exact-replay acceptance: PG-01.1 sub-gate closure requires id-aligned diff to be the production path.

## New constraints accepted

1. Every core object that participates in replay-compare must expose a stable `id` field. This is already the case for accepted objects; the constraint formalizes it.
2. `contracts/exports.json` exports `diffByStableId` additively.
3. Positional diff usage in docs and code examples must be annotated with the warning JSDoc.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 9; finding `WRK-RC-002`.

## Execution posture

- Packet: `pkt.remediate-replay-compare-diff-semantics.v1`.
- Model: `claude-opus-4-7 -r high`.
- Verification: new `diffByStableId()` tested against fixtures that exercise add/remove/modify/reorder; positional diff still passes existing tests; R3 blueprint references the new variant.
- Human review required on resulting PR before merge.
