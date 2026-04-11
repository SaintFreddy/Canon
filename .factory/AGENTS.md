# Factory workspace operating contract

This file narrows `/AGENTS.md` for `/.factory/`.
Normative basis: `/.factory/factory-operating-contract.md`.

## Subtree role

- This subtree stores repo-shared Factory execution assets for this project.
- Assets here may include skills and, if later accepted, droids or hooks.
- These assets encode how repo work should be executed; they do not redefine repo truth.

## Working rules

- Keep all Factory assets additive to accepted P0.2 repo truth.
- Prefer small, single-purpose skills tied to explicit repo tasks.
- Point skills back to accepted artifacts when those artifacts govern execution.
- Keep automated execution bounded to explicit task scope or packet scope.
- Keep headless and review rules consistent with `/.factory/factory-operating-contract.md`.

## Boundaries

- Do not encode P0.5-only packet-budget, context-budget, local-doc-first, or subagent exploration policy here.
- Do not treat this subtree as a second orchestration layer.
- Do not let repo placement imply platform architecture ownership.
- Do not add assets that silently widen authority beyond the accepted repo contract.
