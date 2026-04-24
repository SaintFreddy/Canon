# Quarantine archive — pre-reopen contract-as-code (DEC-RO-05)

This directory preserves 11 `.mjs` contract-as-code files (1,369 LOC) from the
pre-reopen Canon workspace that were never committed to the remote `main`
branch. They lived only in the plan-owner's local workspace as "quarantined
draft state" and were archived here as a one-time preservation commit before
local deletion under DEC-RO-05 (2026-04-24).

See:
- `canon-knowledgebase/post-reopen-decisions/condition-j.md` — the decision record
- `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0096 — carry-forward entry
- `docs/control-plane/implementation/packets/remediation/pkt.quarantine-invariant-sweep.v1.md` — the invariant-sweep packet that reads from this archive and ports invariants into spec-digests

## Structure

- `packages/` — 6 contract-package catalogs (each under its own subdirectory with `index.mjs`)
- `services/` — 4 service execution catalogs
- `workers/` — 1 worker execution catalog

## Nature of the content

Each `index.mjs` exports a frozen JS catalog encoding:
- `contract_ref` strings (e.g., `contract.context-compiler.admitted-basis.compile-run-context.v1`)
- Field schemas
- Required-field sets
- Invariants (the primary preservation target for the invariant-sweep packet)

The ref naming format in these files does NOT match the post-reopen
`docs/control-plane/artifact-registry.seed.json` format. These are parallel
pre-reopen contract artifacts that were superseded by the control-plane
registry + spec-digests system.

## Do not import

Nothing in the live Canon or satellite repos imports from this archive. These
files are for design archaeology only. Do not wire them into any build,
tsconfig, package.json, or runtime.

## Reconstruction

Git history before this commit has no trace of these files (they were
uncommitted local workspace artifacts). This commit is the first and only
time they appear in Canon's git history.
