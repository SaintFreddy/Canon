# Accepted Decision: frozenAt hash-inclusion (sub-decision of condition a)

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule.

## Plan-owner authority

SaintFreddy (delegated recommendation).

## Accepted option

**frozenAt moves INSIDE the hashed compiled-context document**, sourced from the injected `Clock` per the condition (a) decision.

## Decision statement

- `packages/core/src/compiled-context.ts` changes so `frozenAt` is a top-level field of the hashed document, populated by `clock.nowIso()` at freeze time.
- `packages/context-compiler/src/snapshot-freezer.ts` asserts `frozenAt` is present before computing the digest; absence is a typed `SnapshotIntegrityError`.
- Provenance emitters that previously read `frozenAt` from outside the hash are updated to read it from the hashed document instead.
- Two back-to-back freezes with an identical `DeterministicClock` produce byte-identical digests — this becomes a regression test.

## Rationale summary

- With condition (a) Option A accepted, `frozenAt` can be sourced deterministically from the injected Clock. Moving it inside the hash is the only placement that makes PG-01 "frozen-context exact replay" achievable.
- Leaving `frozenAt` outside the hash means two semantically-identical freezes produce different observable documents depending on wall-clock drift — directly falsifies R3 exact replay.
- No second option is rational once (a) Option A is accepted. Alternatives would either (i) re-introduce wall-clock non-determinism by accident, or (ii) split the document identity in a way that complicates downstream provenance.

## What this unblocks

- `pkt.remediate-frozenat-in-hashed-doc.v1` (already scaffolded; now fully authorized — previously partially blocked).
- Part of PG-01 evidence bundle (paired with Clock + stableStringify + localeCompare purge).

## New constraints accepted

1. Any future compiled-context schema change that affects `frozenAt` placement requires a spec-digest regen (see `condition-e-engine-version.md`).
2. Snapshot-freezer is not allowed to produce a digest without `frozenAt`.
3. Thawed documents must carry `frozenAt` forward in the hashed form so replay-compare can see it.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 1 coupling note; findings `PKG-PROV-002`, `PKG-PROV-004`, `PKG-CC-003`.

## Execution posture

- Packet: `pkt.remediate-frozenat-in-hashed-doc.v1` on SaintFreddy/agentic-engine.
- Depends on: `pkt.remediate-clock-timeprovider.v1` landing first.
- Verification: deterministic-replay regression test green; snapshot-freezer refuses to hash without `frozenAt`; provenance emitters read from the hashed document.
- Human review required on resulting PR before merge.
