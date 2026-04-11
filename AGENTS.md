# Repo operating contract

This file is the repo-wide execution projection of `docs/control-plane/core/repo-agent-operating-contract.md`.

## Repo truth default

- Rely on accepted artifacts by default.
- Accepted source-authority artifacts and accepted control-plane artifacts are the default repo truth.
- Drafts, notes, stale artifacts, superseded artifacts, and other non-accepted working material are provisional unless the task explicitly targets them.
- Do not reopen accepted baseline decisions unless the task explicitly asks for that.

## Instruction layering

- When working in a subtree, also read the nearest descendant `AGENTS.md`.
- Descendant `AGENTS.md` files may narrow these rules for their subtree.
- Descendant `AGENTS.md` files must not silently conflict with or widen these rules.

## Bounded execution

- If a task includes a packet brief, treat it as the execution boundary for scope, file targets or whitelist, deliverables, validation hooks, and approvals.
- Packet briefs may narrow execution but must not override accepted repo truth.
- Without a packet brief, stay inside the explicit task scope and touch only files required for that task.
