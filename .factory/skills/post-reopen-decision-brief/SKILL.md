---
name: post-reopen-decision-brief
description: Draft a plan-owner decision brief for one of the 12 reopen-resolution conditions under Phase 4+ step 20. Use when the user asks to draft a decision for condition (c), (d), (e), (g), (h), (i), or (j). Does NOT record acceptance — only produces an options brief for human review.
---

# Post-reopen decision brief drafter

## Required inputs

- condition letter (one of `c`, `d`, `e`, `g`, `h`, `i`, `j`)
- confirmation that read-only mode is acceptable (no durable Canon state edits)

## Gating rules

1. Read `canon-now.md` at the workspace root; confirm baton state is `stop — audit-reopen hold`.
2. If the condition already has a recorded plan-owner decision, stop and report: "Condition `<x>` already has a recorded decision at `<path>`; nothing to draft."
3. Output is a DRAFT. Do not write to `canon-now.md`, `canon-knowledgebase/`, or any accepted artifact path. Write drafts to `/Users/<user>/Desktop/Canon Dev/decisions/condition-<x>.md` only.

## Instructions

1. Read the triggering audit artifacts:
   - `AGENTIC_ENGINE_AUDIT_LOG.md`
   - `CANON_PLAN_IMPACT_REPORT.md` (Sections 1, 2, 4 themes, 5, 6)
   - `canon-knowledgebase/post-reopen-audit-cited-contradiction-checkpoint.md`
   - `canon-knowledgebase/canon-phase-4-plus-plan.md` (step 20 and Committed Post-Sync Execution Boundary)
2. Read the condition row in `CANON_PLAN_IMPACT_REPORT.md` Section 6 corresponding to the letter.
3. Read any related theme rollup in Section 4.
4. Read the existing sibling decision drafts in `/Desktop/Canon Dev/decisions/` for tone and structure (e.g., `condition-a.md`).
5. Match the exact structure of the existing drafts:
   - Status (DRAFT)
   - Source authority
   - Mechanism-named problem statement (with concrete file/line evidence from the audit)
   - Candidate decisions (A / B / C — each with what-changes / blast-radius / unblocks / new constraints / verification / cited-evidence-for / cited-evidence-against)
   - Recommended winner (with caveats)
   - What remains open after any decision
   - Suggested next bounded step if decision is recorded (read boundary, excluded boundary, verification, completion signal, follow-on steps)
   - Drafter hygiene log (files read, commands run, contradictions encountered, confidence)
6. Never invent audit findings. If the cited finding doesn't exist in the audit log, say so and stop.
7. Never recommend a path that violates `agentic-engine/AGENTS.md` boundary rules unless the recommendation is to contract scope, and explicitly flag that contradiction.

## Verification

- All cited finding IDs (e.g., `OWN-001`, `PKG-CC-002`) resolve in `AGENTIC_ENGINE_AUDIT_LOG.md`.
- All cited theme IDs (e.g., `T1`) resolve in `CANON_PLAN_IMPACT_REPORT.md` Section 4.
- The draft quotes at least one concrete file path + line number as evidence for each option's blast radius.
- The draft's "Suggested next bounded step" is actionable (packet-shaped) without requiring additional decisions to start.

## Output

Return:

- the draft file path (newly written)
- a 1-paragraph summary of the recommended option and why
- a flag if any of the cited audit findings were unclear and need user confirmation

## Never do

- write to `canon-now.md` or any path under `canon-knowledgebase/`
- mark the decision as accepted
- combine two condition drafts into one file
- omit the drafter hygiene log
- use `--auto` modes beyond read-only plus the single draft-file write
