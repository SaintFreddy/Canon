# Accepted Decision: Condition (a) — Clock / TimeProvider abstraction ownership

## Status

ACCEPTED. Recorded durably by plan-owner on 2026-04-23.

## Plan-owner

SaintFreddy (repo owner, Canon plan authority).

## Accepted option

**Option A** — Engine owns `Clock` interface in `@canon/engine-core`; Shared Environment supplies the production implementation.

## Decision statement

The engine defines a single `Clock` interface in `packages/core/src/clock.ts`:

```ts
export interface Clock {
  now(): Date;
  nowIso(): string;
  monotonicMs(): number;
}
export const systemClock: Clock = { /* production default */ };
export class DeterministicClock implements Clock { /* test utility */ }
```

Every factory in `packages/core` (`create*`, `freeze*`, `capture*`, `assemble*`) accepts an optional `clock?: Clock` parameter and uses it when present. Defaults to `systemClock`. Same pattern threads through `packages/context-compiler`, `packages/provenance`, `packages/policy`, `packages/model-gateway`, and `workers/run-executor`. A lint rule forbids `Date.now()`, `new Date()`, and `performance.now()` outside `packages/core/src/clock.ts`. Shared Environment wires its authoritative Clock into every engine factory it instantiates.

## Rationale summary

- Option B (Shared Env owns Clock, engine imports its contract) violates the `agentic-engine/AGENTS.md` engine-is-universal rule and destroys SDK-independence.
- Option C (retract determinism claim) publicly surrenders Canon's exact-replay promise, which is load-bearing for PG-01, R3 exact replay, R4 artifact replay, and R7 commissioning audit — a scope contraction larger than it appears.
- Option A is the only option consistent with the accepted three-layer architecture: engine owns seam shape, Shared Env owns runtime identity.

## What this unblocks

- `pkt.remediate-clock-timeprovider.v1` (wave A.1) — authorized for execution.
- `pkt.remediate-thaw-timestamp-authority.v1` (wave A.2) — authorized, runs after A.1.
- `pkt.remediate-localecompare-sort-paths.v1` (wave A.3) — authorized (coupled with condition (a)).
- Partial authorization for `pkt.remediate-frozenat-in-hashed-doc.v1` (wave A.4) — still requires the separate frozenAt hash-inclusion sub-decision before execution.

## New constraints accepted with this decision

1. Engine must never call `Date.now()` / `new Date()` / `performance.now()` in `src/`. Lint rule is mandatory and ships with the remediation packet.
2. Shared Env must document that its Clock is deterministic per run, monotonic within a run, and suitable as replay basis.
3. Every engine factory API widens by an optional `clock?: Clock` parameter. This is backwards-compatible but contractual.
4. `contracts/exports.json` must export `Clock`, `systemClock`, and `DeterministicClock` additively.

## Coupled open items (not resolved by this decision)

- Whether `frozenAt` moves **inside** the hashed compiled-context document. This is a separate PROV-002/PROV-004 sub-decision that must be recorded before `pkt.remediate-frozenat-in-hashed-doc.v1` executes.
- Exact shape of `Clock.monotonicMs()` default: counter-based deterministic default in engine vs. `performance.now()` passthrough in production. Remediation packet will propose the concrete default; plan-owner accepts that default on PR review.

## Reference to draft options analysis

Full option analysis and cited-evidence ledger at `/Users/fredericksaintmaximus/Desktop/Canon Dev/decisions/condition-a.md` (draft, preserved as historical record). Accept cites the same audit findings: `OWN-001`, `PKG-CORE-THEME-001`, `PKG-CC-001/002/003`, `PKG-MG-002`, theme `T1` in `CANON_PLAN_IMPACT_REPORT.md` Section 4.

## Execution posture

- First remediation packet to land: `pkt.remediate-clock-timeprovider.v1` on `SaintFreddy/agentic-engine`, tagged `@droid` on issue.
- Model: `claude-opus-4-7`, reasoning effort `high`.
- Verification: `corepack pnpm typecheck && corepack pnpm test` green, new `clock-injection.test.ts` asserts every factory accepts and uses an injected Clock, lint rule blocks wall-clock regressions.
- Human review required on the resulting PR before merge.
