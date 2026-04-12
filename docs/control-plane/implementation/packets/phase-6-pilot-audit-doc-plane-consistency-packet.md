# Phase 6 pilot audit packet — documentation-plane consistency
Version: 1.0
Status: Accepted
Task: P6.4 — Pilot packet set + Factory benchmark harness + internal skills/adapters
Artifact ID: pkt.phase6-pilot-audit-doc-plane-consistency-packet.v1
Packet scope: First-wave `audit` packet for reviewing documentation-plane, manifest, current-state, contract, and fixture consistency inside accepted control-plane roots
File whitelist ref: wl.phase6-pilot-audit-doc-plane-consistency.v1

This packet is accepted for downstream use.
It pilot-tests the `audit` run class against accepted documentation-plane and validation assets.
It does not authorize packet drift, runtime code, or cross-root scope widening.

## Packet brief

```json
{
  "packet_id": "pkt.phase6-pilot-audit-doc-plane-consistency-packet.v1",
  "title": "Phase 6 pilot audit packet — documentation-plane consistency",
  "task_id": "P6.4",
  "objective": "Audit accepted manifest, current-state, packet-context, contract, and fixture assets for cross-pack consistency and bounded packet readiness.",
  "scope": [
    "Review accepted documentation-plane datasets and test-contract or fixture assets against their governing Phase 6 packs.",
    "Emit explicit audit findings or a structurally clean result without widening packet scope."
  ],
  "out_of_scope": [
    "Runtime code changes.",
    "Reopening accepted Phase 6 semantics or packet-budget policy.",
    "Introducing new roots, new packet schemas, or a second orchestration stack."
  ],
  "source_authority_refs": [
    "surf.phase6-repo-package-architecture-and-agent-execution-rules-pack.v1",
    "surf.phase6-agent-oriented-codebase-pattern-and-documentation-plane-pack.v1"
  ],
  "accepted_artifact_refs": [
    "cp.phase6-workspace-manifest-index-data.v1",
    "cp.phase6-codebase-current-state-data.v1",
    "cp.phase6-agent-packet-context-pack-rules-data.v1",
    "cp.phase6-module-test-contracts-data.v1",
    "cp.phase6-fixture-rules-data.v1",
    "cp.factory-review-guidelines-skill.v1"
  ],
  "file_whitelist_ref": "wl.phase6-pilot-audit-doc-plane-consistency.v1",
  "deliverables": [
    "An explicit audit result over accepted documentation-plane and validation assets.",
    "Tuning-note updates if the audit reveals packet or harness gaps."
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
    "Create a new corrective packet instead of widening this audit packet if material drift requires edits outside the whitelist."
  ],
  "execution_mode": "factory_first",
  "carry_forward_topics": [
    "audit-packet tuning",
    "documentation-plane drift findings",
    "validator coverage"
  ],
  "notes": [
    "Selected budget band: standard.",
    "Run class: audit.",
    "This packet is expected to stay read-heavy and to produce explicit findings even when structurally clean."
  ]
}
```

## File whitelist `wl.phase6-pilot-audit-doc-plane-consistency.v1`

- `docs/control-plane/core/workspace-manifest-index.json`
- `docs/control-plane/core/codebase-current-state.json`
- `docs/control-plane/core/agent-packet-context-pack-rules.json`
- `tests/contracts/module-boundary.contracts.json`
- `tests/fixtures/fixture-rules.json`
- `docs/control-plane/core/phase-6-pilot-packet-tuning-notes.md`

## Run-class and benchmark posture

- Run class: `audit`
- Selected budget band: `standard`
- Benchmark focus: documentation-plane coherence, fixture-policy alignment, review-output clarity

## Packet rationale

- This packet exercises the audit path against already materialized accepted assets.
- The whitelist stays inside existing control-plane and tests roots, which makes it a strong structural benchmark for review-style packets.
- The packet requires explicit findings even when no corrective action is needed, preserving inspectable audit output.
