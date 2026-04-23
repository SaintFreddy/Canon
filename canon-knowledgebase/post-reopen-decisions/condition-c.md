# Accepted Decision: Condition (c) — Policy-matcher pattern vs strict-equals

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule (canon-now.md "Plan-owner delegation rule"). Recommended option accepted automatically because this is a technical seam decision without project-direction implications.

## Plan-owner authority

SaintFreddy (delegated: "always choose recommended unless project-direction implications").

## Accepted option

**Option A (Section 6 row 4 default)** — engine ships typed `RulePattern` with glob/regex and explicit matcher at Platform Gate.

## Decision statement

- Engine introduces `RulePattern` as a tagged union in `packages/policy/src/rule-pattern.ts`:

  ```ts
  export type RulePattern =
    | { kind: "exact"; value: string }
    | { kind: "glob"; pattern: string }
    | { kind: "regex"; source: string; flags?: string };
  export function matches(pattern: RulePattern, candidate: string): boolean;
  ```

- `packages/policy/src/policy-matcher.ts` replaces every strict-equals check with `matches(pattern, candidate)`. Platform Gate spec §6 clause documenting policy matching is updated to reference `RulePattern`.
- Regex compilation is cached per `RulePattern` instance; compilation failures become typed `PolicyPatternCompileError` results (inspectable per PG-07).
- New regression tests cover exact + glob + regex paths, edge cases (empty candidate, regex with flags, glob with `**`), and failure surfaces.

## Rationale summary

- Section 6 row 4 default is Option A for SECURITY severity (`PKG-POL-001..005`, `PKG-POL-009`, `PKG-POL-014` — CRITICAL bucket).
- Option B (R6 ships pattern matcher with audit caveat) is allowed as fallback but defers a security fix and extends the window during which policies silently permit too much.
- Option C (defer to domain packs) scatters policy logic and makes cross-pack consistency impossible to audit.
- Option A matches the accepted three-layer architecture — engine owns the seam, domain packs supply rules via the typed surface.

## What this unblocks

- `pkt.remediate-policy-matcher.v1` (new packet scaffold authored on this pass).
- Closes PG-07 policy-matching sub-claim.

## New constraints accepted

1. Every policy rule in the repo must migrate to `RulePattern`. Strict-equals is expressible as `{ kind: "exact" }`.
2. Adapter/domain packs that ship rules must use the typed surface; ad-hoc string comparisons in policy paths become lint errors.
3. `contracts/exports.json` adds `RulePattern` and `matches` additively.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 4; findings `PKG-POL-001..005`, `PKG-POL-009`, `PKG-POL-014`; Platform Gate PG-07 §6 clause.

## Execution posture

- Packet: `pkt.remediate-policy-matcher.v1`.
- Model: `claude-opus-4-7 -r high`.
- Verification: `pnpm typecheck` + `pnpm test` green; regression matrix covering exact/glob/regex/compile-failure paths green; no remaining strict-equals in `packages/policy/src/`.
- Human review required on resulting PR before merge.
