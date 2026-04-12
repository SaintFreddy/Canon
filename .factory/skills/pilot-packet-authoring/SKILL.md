---
name: pilot-packet-authoring
description: Author or refine Canon Phase 6 pilot execution packets from accepted manifests, current-state data, packet-context rules, run-class contracts, and fixture bindings. Use when creating or updating `pkt.execution_packet` artifacts under `docs/control-plane/implementation/packets/`.
---

# Pilot packet authoring

## Required inputs

- target run class
- governing accepted artifact refs
- explicit packet objective and bounded file-whitelist

## Instructions

1. Read `/AGENTS.md`, `docs/control-plane/AGENTS.md`, and `/.factory/AGENTS.md` for the touched roots.
2. Read the accepted Phase 6 documentation-plane assets:
   - `cp.phase6-workspace-manifest-index-data.v1`
   - `cp.phase6-codebase-current-state-data.v1`
   - `cp.phase6-agent-packet-context-pack-rules-data.v1`
3. Read the accepted run-class and fixture baselines that govern the packet.
4. Keep the packet inside one explicit dominant objective and one explicit file-whitelist ref.
5. Use the accepted packet-brief schema for the embedded JSON brief.
6. Keep validation hooks aligned to accepted `pkt.execution_packet` defaults unless real fixtures or tests require more.
7. Point the packet back to accepted artifacts instead of restating their semantics locally.
8. Run `python3 scripts/validators/validate_pilot_packets.py <packet-path>` before claiming the packet is ready.

## Verification

- packet brief JSON parses and matches the accepted P0.2 schema shape
- whitelist paths map to accepted workspace roots
- run class and packet-budget band are explicit
- accepted refs resolve in the registry

## Never do

- widen packet scope beyond the named whitelist
- invent task-local packet metadata or a second packet schema
- treat repo layout as architecture ownership
- bypass accepted manifests, current-state data, or fixture rules
