---
name: control-plane-packet-execution
description: Execute bounded Canon control-plane packets using accepted artifacts, synchronized registry and graph updates, real validators, and carry-forward/status output. Use when a task includes a packet brief or explicit P-task scope touching accepted artifacts.
---

# Control-plane packet execution

## Required inputs

- selected task ID or packet brief
- governing accepted artifact refs
- explicit task scope, file targets, or file whitelist

## Instructions

1. Read `/AGENTS.md` and the nearest descendant `AGENTS.md` files for the touched paths.
2. Read the governing accepted artifacts named by the task or packet, including the relevant sections of `docs/control-plane/core/master-plan.md`.
3. Treat the packet brief or explicit task scope as the execution boundary.
4. Use accepted artifacts by default; do not treat drafts, notes, stale artifacts, or superseded artifacts as repo truth unless the task explicitly targets them.
5. If you create or change an accepted artifact, update both:
   - `docs/control-plane/artifact-registry.seed.json`
   - `docs/control-plane/dependency-graph.seed.json`
6. Reuse accepted artifact IDs, edge types, validation hooks, and stale rules. Do not invent task-local control-plane metadata.
7. Run the real validators that exist for the touched files before claiming completion.
8. Do not mark status done or append carry-forward entries until deliverables exist and validators pass.
9. If scope, acceptance state, or authority is ambiguous, stop and report the gap instead of widening scope.

## Verification

- JSON-parse every edited `.json` file.
- Verify every new graph artifact ID resolves in the registry.
- Verify validation hooks, edge types, and stale rules match the accepted P0.1 catalogs.
- Run any task-specific validators already required by the selected task or packet.

## Output

Return:

- restated objective
- files changed
- deliverables produced
- validation results
- proposed status updates
- draft carry-forward entry

## Never do

- reopen accepted baseline decisions without explicit task instruction
- pull P0.5-only packet-budget or context-policy behavior into execution
- treat repo layout as platform architecture
- introduce a second orchestration stack
