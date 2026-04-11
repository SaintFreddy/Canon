---
name: review-guidelines
description: Canon repo review rules for automated review and approval-prep runs. Use when reviewing diffs, validating accepted control-plane changes, or preparing human acceptance.
user-invocable: false
---

# Canon review guidelines

When reviewing changes in this repo, prioritize the following checks.

## 1. Baseline preservation

- Do not reopen accepted three-layer, chat-projection, release-order, or human-owned-truth decisions unless the task explicitly asks for that.
- P0.3 artifacts must extend accepted P0.2 behavior rather than rewrite it.

## 2. Control-plane integrity

- Every new accepted artifact must be registered in `docs/control-plane/artifact-registry.seed.json`.
- Every new dependency-graph node or edge must resolve to registered artifact IDs.
- Edge types, validation hooks, and stale rules must come from the accepted P0.1 catalogs.

## 3. Scope discipline

- Flag any P0.5-only packet-budget, context-budget, local-doc-first, or subagent exploration behavior that leaks into P0.3.
- Flag any attempt to introduce a second orchestration stack or to treat repo layout as platform architecture.

## 4. Review and approval discipline

- Automated runs may prepare patches and validation evidence, but human acceptance remains authoritative.
- Status markers and carry-forward entries may change only after deliverables exist and validators pass.
- Flag any change that silently presents unaccepted material as accepted repo truth.

## Review output

Return:

- summary
- findings
- required before acceptance
- explicit note when the diff is structurally clean but still needs human acceptance
