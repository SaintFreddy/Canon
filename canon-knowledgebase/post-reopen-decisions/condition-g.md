# Accepted Decision: Condition (g) — Intra-workspace peerDependency carve-out

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule.

## Plan-owner authority

SaintFreddy (delegated recommendation).

## Accepted option

**Option A (Section 6 row 8 default)** — amend `phase-6-repo-package-architecture.md §6.1` to distinguish third-party peer-dependencies from intra-workspace peer-dependencies; intra-workspace carve-out is permitted.

## Decision statement

- The "zero external runtime dependencies" invariant is preserved in spirit: the engine still ships no third-party runtime peers.
- Intra-workspace peer-dependencies (`@canon/*` packages depending on other `@canon/*` packages as peers) are explicitly permitted because they are structurally equivalent to imports within the engine boundary.
- `phase-6-repo-package-architecture.md §6.1` gets a new paragraph:

  > "Third-party runtime peer-dependencies are forbidden; intra-workspace peer-dependencies between `@canon/*` packages are permitted because they are structurally equivalent to intra-engine imports and do not expand the runtime surface beyond `@canon/*`."

- No engine code change is required by this decision alone; the decision authorizes existing intra-workspace peer-dep shapes rather than rewriting them away.

## Rationale summary

- Section 6 row 8 default is Option A.
- Option B (rewrite engine to eliminate peer-deps entirely) would require significant refactoring across `packages/*` with no architectural benefit — the "zero external deps" property is what matters, not the peer-dep syntactic shape.
- Matches accepted Canon authority: engine is monorepo-structured and intra-workspace dependencies are implementation detail, not release-surface expansion.

## What this unblocks

- `pkt.remediate-peerdep-carveout.v1` (new packet scaffold authored on this pass; Canon doc amendment only).

## New constraints accepted

1. The amendment to `§6.1` is append-preserving: the prior paragraph stays as historical context, the new paragraph adds the carve-out.
2. Any future third-party peer-dep addition still requires an explicit plan-owner decision.
3. Lint or workspace-integrity check to detect accidental third-party peer-dep creep.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 8; finding `X-029`; Section 4 theme rollup.

## Execution posture

- Packet: `pkt.remediate-peerdep-carveout.v1` on SaintFreddy/Canon (control-plane doc-only).
- Model: `claude-opus-4-7 -r high`.
- Verification: amendment landed in `phase-6-repo-package-architecture.md §6.1`; registry + graph in sync; `python3 scripts/validators/validate_control_plane_integrity.py` green.
- Human review required on resulting PR before merge.
