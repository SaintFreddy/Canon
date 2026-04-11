# Control-plane subtree operating contract

This file narrows `/AGENTS.md` for `docs/control-plane/`.
Normative basis: `docs/control-plane/core/repo-agent-operating-contract.md`.

## Subtree role

- This subtree stores planning/spec control-plane artifacts and machine-readable control-plane datasets.
- Repo layout here is a storage convention for control-plane artifacts, not the platform architecture or runtime truth model.

## Working rules

- Use accepted artifacts in this subtree by default; treat drafts, notes, stale or superseded artifacts, and unregistered material as provisional unless the task explicitly targets them.
- Reuse the accepted P0.1 artifact model, dependency edge semantics, validation-hook standards, and stale rules; do not invent task-local metadata models.
- Any new or changed accepted artifact in this subtree must be reflected in `docs/control-plane/artifact-registry.seed.json` and `docs/control-plane/dependency-graph.seed.json`.
- Keep `docs/control-plane/core/master-plan.md` carry-forward entries append-only.
- Update `docs/control-plane/core/master-plan.md` status markers and completion snapshot only after the deliverables exist and the required validations pass.

## Boundaries

- Do not add P0.3-only Factory-specific skills layouts, droid conventions, or headless-run review rules here.
- Do not let repo placement redefine engine/shared-environment/app layer ownership.
