# Phase 6 pilot packet tuning notes
Version: 1.0
Status: Accepted
Task: P6.4 — Pilot packet set + Factory benchmark harness + internal skills/adapters
Artifact ID: cp.phase6-pilot-packet-tuning-notes.v1

This note freezes the first dry-run benchmark observations for the accepted Phase 6 pilot packet wave.
It records packet-shape and harness findings only.
It does not widen packet scope or redefine accepted Phase 6 authority.

## Benchmark snapshot

- Benchmark harness: `cp.phase6-factory-benchmark-harness.v1`
- Benchmark matrix: `cp.phase6-pilot-benchmark-matrix-data.v1`
- Benchmark results: `cp.phase6-pilot-benchmark-results-data.v1`
- Cases executed: `3`
- Passing cases: `3`
- Failing cases: `0`
- Benchmark posture: `dry_run_structural`

## Packet-shape findings

1. The first-wave `plan`, `audit`, and `transform` packets all pass the packet-brief, whitelist-root, validation-hook, and budget-band checks.
2. Every pilot packet currently uses the `standard` budget band and lands exactly at the governing-ref ceiling of `8`, so future packet growth should prefer splitting scope over widening the band by default.
3. The audit packet proves that mixed `docs/control-plane/` and `tests/` review scope remains structurally valid when fixture and contract datasets stay frozen.
4. The transform packet proves that a bounded write path can cross `.factory/`, `scripts/`, and `docs/control-plane/` without touching runtime implementation roots.

## Harness findings

- The thin validator and wrapper approach is sufficient for dry-run structural benchmarking in P6.4.
- Root-file whitelist handling must preserve both child directories and accepted root files under `docs/control-plane/`.
- Benchmark output should remain frozen under `tests/benchmark-datasets/` and should be regenerated only when pilot packets, fixture bindings, or packet-context rules materially change.

## Carry-forward guidance

- Prefer keeping future pilot packets at or below the current governing-ref count unless a new benchmark case proves a wider band is necessary.
- Preserve explicit validation-hook lists in packet briefs; the harness depends on set equality rather than implied defaults.
- If future transform packets need runtime roots, split them into a new packet family instead of widening the current additive Factory tooling packet.
