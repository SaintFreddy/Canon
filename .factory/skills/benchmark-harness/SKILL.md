---
name: benchmark-harness
description: Run the Canon Phase 6 dry-run benchmark harness over accepted pilot packets, freeze matrix-driven benchmark results, and update tuning notes. Use when validating pilot packet readiness before broader packet rollout.
---

# Benchmark harness

## Required inputs

- accepted benchmark matrix dataset
- accepted pilot packet set
- output path for frozen benchmark results

## Instructions

1. Read `/AGENTS.md`, `docs/control-plane/AGENTS.md`, and `/.factory/AGENTS.md`.
2. Read the accepted harness contract at `cp.phase6-factory-benchmark-harness.v1`.
3. Read the accepted documentation-plane, run-class, and fixture assets that the benchmark matrix cites.
4. Run `python3 scripts/wrappers/run_phase6_benchmarks.py --matrix <matrix-path> --write <results-path>`.
5. Review the emitted results and carry forward the important findings into the accepted tuning-notes artifact.
6. Keep the harness dry-run and structure-first until runtime implementation roots and executable fixtures materially exist.

## Verification

- every benchmark case resolves to an accepted packet artifact and real packet file
- packet validation passes before results are frozen
- result JSON is reproducible from the matrix and the packet files
- findings remain explicit instead of hidden in logs only

## Never do

- treat the harness as a new execution planner
- widen packet scope automatically because a case fails
- claim runtime product behavior was benchmarked when only structural packet readiness was checked
- bypass human acceptance for new packet meaning or status changes
