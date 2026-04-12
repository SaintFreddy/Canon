# Phase 6 Factory benchmark harness
Version: 1.0
Status: Accepted
Task: P6.4 — Pilot packet set + Factory benchmark harness + internal skills/adapters
Artifact ID: cp.phase6-factory-benchmark-harness.v1
Topic key: phase6-factory-benchmark-harness

This spec is accepted for downstream use.
It defines the Phase 6 dry-run benchmark harness for validating pilot execution packets, additive Factory skills, and thin repo-local wrappers before wider packet scaling.
It does not benchmark runtime product behavior or replace the accepted P0.3 Factory contract.

## 1. Purpose

This harness exists to:

- validate a first-wave pilot packet set against accepted packet, manifest, current-state, boundary, and fixture rules,
- exercise real repo-scoped skills and thin wrappers before broader packet rollout,
- freeze benchmark matrix inputs and benchmark result outputs in machine-readable datasets,
- turn packet-quality findings into explicit tuning notes instead of silent prompt drift.

## 2. Scope boundaries

### In scope

- dry-run structural validation of accepted pilot execution packets,
- benchmark matrix and result datasets,
- repo-scoped Factory skills that author packets or run the harness,
- thin wrappers that validate packets and emit benchmark results,
- tuning-note capture from benchmark findings.

### Out of scope

- runtime model/tool benchmarking,
- implementation code generation in `apps/`, `packages/`, `services/`, or `workers/`,
- widening the accepted P0.3 authority model,
- replacing packet briefs or execution packets with a second orchestration layer.

## 3. Harness interpretation rules

### 3.1 Dry-run structural benchmark rule

Phase 6 benchmarking is dry-run and structure-first because the repo still lacks runtime implementation roots.
The harness therefore evaluates real packet types, real file whitelists, accepted refs, validation coverage, and budget fit without pretending to run product code that does not yet exist.

### 3.2 Accepted-artifact-first rule

The harness reads accepted manifests, current-state data, packet-context rules, module-boundary contracts, fixture rules, run-class contracts, and current Factory skills before it evaluates any pilot packet.
It may not use drafts or unregistered notes as default truth.

### 3.3 Packet-class coverage rule

The first benchmark wave must cover at least:

- one read-heavy planning packet,
- one audit/review packet,
- one bounded write-path transform packet.

This ensures the harness tests both non-mutating and mutating packet shapes before `P6.5` and `P6.6`.

### 3.4 Thin-wrapper rule

Repo-local wrappers under `scripts/` remain thin validators and emitters around accepted packet and benchmark rules.
They may automate structural checks; they may not become a second task planner or alternate execution ontology.

## 4. Harness inputs

The harness consumes:

1. accepted pilot packets under `docs/control-plane/implementation/packets/`,
2. the accepted benchmark matrix dataset under `tests/benchmark-datasets/`,
3. accepted documentation-plane datasets from `P6.3`,
4. accepted run-class and proof/fixture baselines from `P2.2`, `P5.2`, and `P5.3`,
5. accepted repo-scoped Factory skill contracts and the two P6.4 skills below.

## 5. Benchmark stages

### 5.1 Packet-brief validation

Each pilot packet must:

- expose the accepted execution-packet header fields,
- embed one packet brief matching the accepted P0.2 schema baseline,
- declare one bounded file-whitelist ref,
- name a valid run class and selected packet-budget band.

### 5.2 Accepted-ref and whitelist mapping

For each pilot packet the harness must verify:

- source-authority refs and accepted-artifact refs resolve in the registry,
- file-whitelist paths map to accepted workspace roots from the manifest index,
- whitelisted control-plane children fit the accepted documentation-plane structure,
- the packet remains inside the named root families without silent widening.

### 5.3 Budget and validation coverage

For each pilot packet the harness must verify:

- the selected budget band exists in the accepted packet-context rules,
- the packet's governing-ref count fits the selected band,
- validation hooks align to the accepted execution-packet hook family,
- fixture expectations align to the accepted run-class fixture binding.

### 5.4 Frozen benchmark outputs

The harness emits:

- one benchmark results dataset under `tests/benchmark-datasets/`,
- one tuning-notes artifact under `docs/control-plane/core/`,
- console JSON output suitable for CI-style or headless review evidence.

Benchmark results remain frozen versioned outputs for the current packet wave rather than mutable scratch notes.

## 6. Pilot packet wave

The first accepted pilot wave is:

| Packet | Run class | Why it is in wave one |
| --- | --- | --- |
| `pkt.phase6-pilot-plan-release-blueprint-packet.v1` | `plan` | exercises blueprint-shaping scope and accepted-root targeting |
| `pkt.phase6-pilot-audit-doc-plane-consistency-packet.v1` | `audit` | exercises review-style packet scope and control-plane consistency checks |
| `pkt.phase6-pilot-transform-factory-skill-harness-packet.v1` | `transform` | exercises bounded write-path scope across `.factory/`, `scripts/`, and harness assets |

## 7. Skills and wrappers

### 7.1 Accepted P6.4 skills

| Asset | Role |
| --- | --- |
| `/.factory/skills/pilot-packet-authoring/SKILL.md` | Builds or refines pilot packets from accepted manifests, packet rules, and run-class baselines |
| `/.factory/skills/benchmark-harness/SKILL.md` | Runs the Phase 6 harness, freezes results, and updates tuning notes |

### 7.2 Thin wrappers

| Wrapper | Role |
| --- | --- |
| `scripts/validators/validate_pilot_packets.py` | Structural packet validator over headers, packet brief JSON, whitelist roots, and accepted refs |
| `scripts/wrappers/run_phase6_benchmarks.py` | Matrix-driven harness runner that executes validation and writes frozen results JSON |

These wrappers are support assets, not accepted truth artifacts on their own.

## 8. Output contract

The benchmark results dataset should record at least:

- benchmark case ID,
- packet ref,
- run class,
- pass/fail status,
- governing-ref count,
- file-whitelist root coverage,
- validation-hook coverage,
- fixture-family alignment,
- findings or missing conditions.

The tuning-notes artifact should record:

- packet types that benchmarked cleanly,
- packet shapes or roots that pushed scope or validator limits,
- current adapter or wrapper gaps,
- recommended next-wave packet additions.

## 9. Boundary locks

1. This harness validates execution-packet readiness; it does not replace human acceptance.
2. The harness may automate structural checks and result freezing, but it may not auto-promote meaning or status.
3. Skills and wrappers must stay additive to the accepted P0.3 Factory contract and the accepted P6.3 documentation plane.
4. Benchmark results may highlight gaps, but they may not widen packet scope or invent new roots without explicit accepted changes.

## 10. Review notes

Human review should confirm that this harness:

- tests real packet types before broader packet scaling,
- keeps packet benchmarking additive to accepted documentation-plane and Factory rules,
- uses thin wrappers rather than a second orchestration stack,
- produces frozen benchmark results and explicit tuning notes instead of silent packet drift.
