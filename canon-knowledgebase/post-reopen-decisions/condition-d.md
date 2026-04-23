# Accepted Decision: Condition (d) — stableStringify unification into @canon/engine-core

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule.

## Plan-owner authority

SaintFreddy (delegated recommendation).

## Accepted option

**Option A (Section 6 row 5 default)** — land the helper now in `@canon/engine-core`, add a cross-package determinism test, include it in PG-01 evidence.

## Decision statement

- Canonical `stableStringify` lives in `packages/core/src/stable-stringify.ts`. The implementation is the strict-deterministic variant: keys sorted with byte-deterministic comparator, arrays preserved in order, numbers/booleans/null handled explicitly, `undefined` skipped, NaN/Infinity rejected with typed error.
- Every other package (`packages/provenance`, `packages/context-compiler`, `packages/policy`, etc.) replaces its local copy with `import { stableStringify } from "@canon/engine-core"`.
- New test `packages/core/src/__tests__/stable-stringify.cross-package.test.ts` asserts byte-identical output for a fixture set that every prior caller was previously producing.
- `contracts/exports.json` adds `stableStringify` additively.
- A drift-detector is NOT added (Option B's concession is unnecessary once the single copy ships).

## Rationale summary

- Section 6 row 5 default is Option A: "a single helper is less code and objectively safer."
- Option B (freeze per-package copies with drift detector) preserves duplication and requires a running test suite to catch regressions that would never exist under Option A.
- Findings `PKG-PROV-001/002/004`, `PKG-CC-014..018`, `OWN-008` all point at the divergence as the root cause.

## What this unblocks

- `pkt.remediate-stablestringify-unification.v1` (already scaffolded; authorized now).
- Part of PG-01 evidence bundle (paired with Clock + localeCompare purge + frozenAt placement).

## New constraints accepted

1. No package may ship its own `stableStringify`. Lint rule or import-path restriction enforced.
2. `contracts/exports.json` exports are additive.
3. NaN/Infinity inputs throw typed `StableStringifyError`; callers must handle or propagate.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 5; findings `PKG-PROV-001/002/004`, `PKG-CC-014..018`, `OWN-008`; Section 4 theme rollup.

## Execution posture

- Packet: `pkt.remediate-stablestringify-unification.v1` on SaintFreddy/agentic-engine.
- Can parallel `pkt.remediate-clock-timeprovider.v1`.
- Verification: cross-package byte-identity fixture test; `grep -rE 'function +stableStringify|const +stableStringify' packages/ | grep -v __tests__` returns exactly one non-test match.
- Human review required on resulting PR before merge.
