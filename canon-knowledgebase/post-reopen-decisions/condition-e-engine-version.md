# Accepted Decision: Condition (e.1) — Engine semver direction and spec-digest regen protocol

## Status

ACCEPTED. Recorded 2026-04-23 under the plan-owner delegation rule.

## Plan-owner authority

SaintFreddy (delegated recommendation).

## Accepted option

**Option A (Section 6 row 7 default)** — engine starts at `0.1.0` with an explicit breaking-change protocol tied to spec-digest regeneration.

## Decision statement

- `agentic-engine/package.json` and every `@canon/*` package in the workspace move to `"version": "0.1.0"`.
- Breaking-change protocol: any change that modifies a type in `contracts/exports.json`, a hash-contributing field in a core object, or the IPC message contract requires:
  1. Minor bump (`0.1.0 → 0.2.0`) for additive-but-breaking changes during `0.x`.
  2. Spec-digest regeneration recorded at `docs/spec-digests/` with a dated checkpoint entry naming the breaking change.
  3. Carry-forward entry describing the break and migration path.
- `X-015` spec-digest anchoring: each minor bump produces a new content-hash anchor stored alongside the checkpoint.

## Rationale summary

- Section 6 row 7 default is Option A.
- Option B (stay `0.0.0` with content-hash-only channel) makes downstream semantic versioning impossible and muddies release messaging. Already rejected implicitly by Phase 4+ plan step 20 expectations.
- Option C (retract all semver prose) surrenders release-discipline tooling and public communicability.

## What this unblocks

- `pkt.remediate-engine-version-0.1.0.v1` (new packet scaffold authored on this pass).
- Release-cadence discipline from R1 onward.

## Coupled to condition (e.2)

The LICENSE sub-decision of condition (e) is a project-direction choice and is **escalated to the plan-owner** — not resolved here. The engine-version decision is independent of the LICENSE choice and can land on its own.

## New constraints accepted

1. Every `@canon/*` workspace package is `0.1.0` at minimum and subject to the breaking-change protocol above.
2. Spec-digest regeneration is mandatory on each minor bump; omission is a lint violation in repo hygiene.
3. Release messaging uses semver semantics consistently.

## Reference to audit authority

`CANON_PLAN_IMPACT_REPORT.md` Section 6 row 7; findings `X-010 (MED)` + `X-015`.

## Execution posture

- Packet: `pkt.remediate-engine-version-0.1.0.v1`.
- Model: `claude-opus-4-7 -r high`.
- Verification: every `@canon/*` `package.json` on `0.1.0`; `docs/spec-digests/engine-0.1.0.md` checkpoint exists; `pnpm build` green.
- Human review required on resulting PR before merge.
