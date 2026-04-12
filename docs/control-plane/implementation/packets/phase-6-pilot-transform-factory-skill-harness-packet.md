# Phase 6 pilot transform packet — Factory skill and harness refinement
Version: 1.0
Status: Accepted
Task: P6.4 — Pilot packet set + Factory benchmark harness + internal skills/adapters
Artifact ID: pkt.phase6-pilot-transform-factory-skill-harness-packet.v1
Packet scope: First-wave `transform` packet for bounded write-path refinement of Factory packet-authoring or benchmark-harness assets
File whitelist ref: wl.phase6-pilot-transform-factory-skill-harness.v1

This packet is accepted for downstream use.
It pilot-tests the `transform` run class against a real write-path limited to `.factory/`, `scripts/`, and benchmark-harness assets.
It does not authorize runtime product writes, package scaffolding, or cross-lane writeback.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-pilot-transform-factory-skill-harness-packet.v1",
  "title": "Phase 6 pilot transform packet — Factory skill and harness refinement",
  "task_id": "P6.4",
  "objective": "Refine accepted Factory packet-authoring or benchmark-harness assets through one bounded write-path packet that stays inside additive execution tooling.",
  "scope": [
    "Touch only accepted Factory skill specs, thin packet-validation or benchmark wrappers, harness specs, tuning notes, and required registry or graph synchronization.",
    "Keep all changes additive to the accepted P0.3 Factory contract and the accepted Phase 6 documentation plane."
  ],
  "out_of_scope": [
    "Runtime product code or service or worker scaffolding.",
    "New authority models, new packet schemas, or hidden automation layers.",
    "Mixed-lane writeback beyond artifact-lane proposal behavior."
  ],
  "source_authority_refs": [
    "cp.factory-operating-contract.v1",
    "surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1"
  ],
  "accepted_artifact_refs": [
    "cp.factory-packet-execution-skill.v1",
    "cp.factory-review-guidelines-skill.v1",
    "cp.phase6-factory-benchmark-harness.v1",
    "cp.phase6-agent-packet-context-pack-rules-data.v1",
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1"
  ],
  "file_whitelist_ref": "wl.phase6-pilot-transform-factory-skill-harness.v1",
  "deliverables": [
    "Bounded refinements to accepted Factory skill or benchmark-harness assets.",
    "Updated tuning notes and synchronized registry or graph changes when accepted artifacts change."
  ],
  "validation_hooks": [
    {
      "hook_id": "vh.dependency.integrity"
    },
    {
      "hook_id": "vh.consistency.cross-pack-review"
    },
    {
      "hook_id": "vh.fixture.or-test-when-applicable"
    },
    {
      "hook_id": "vh.manual.acceptance"
    }
  ],
  "approval_requirements": [
    "Human implementation-owner acceptance before packet promotion or downstream use.",
    "Escalate or split if the change needs roots outside .factory/, scripts/, docs/control-plane/core/, or tests/benchmark-datasets/."
  ],
  "execution_mode": "factory_first",
  "carry_forward_topics": [
    "transform-packet tuning",
    "skill refinement",
    "wrapper gaps",
    "benchmark harness findings"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: transform.",
    "This packet is the first write-path pilot and therefore keeps the whitelist tightly bounded to additive execution assets."
  ]
}
```

## File whitelist `wl.phase6-pilot-transform-factory-skill-harness.v1`

- `.factory/skills/pilot-packet-authoring/SKILL.md`
- `.factory/skills/benchmark-harness/SKILL.md`
- `scripts/validators/validate_pilot_packets.py`
- `scripts/wrappers/run_phase6_benchmarks.py`
- `docs/control-plane/core/phase-6-factory-benchmark-harness.md`
- `docs/control-plane/core/phase-6-pilot-packet-tuning-notes.md`
- `docs/control-plane/artifact-registry.seed.json`
- `docs/control-plane/dependency-graph.seed.json`

## Run-class and benchmark posture

- Run class: `transform`
- Selected budget band: `standard`
- Benchmark focus: bounded write-path clarity, additive Factory-scope discipline, wrapper validation readiness

## Packet rationale

- This packet is the first write-path benchmark and therefore proves that bounded packet mutation can stay additive to accepted Factory tooling.
- The whitelist explicitly crosses `.factory/`, `scripts/`, and `docs/control-plane/` roots, which exercises multi-root scope discipline without touching runtime product roots.
- The packet remains artifact-lane only and never implies memory, canon, export, or workflow writes.
