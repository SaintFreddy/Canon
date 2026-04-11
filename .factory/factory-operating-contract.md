# Factory Operating Contract
Version: 1.0
Status: Accepted
Task: P0.3 — Factory operating contract

## 1. Purpose

This artifact defines the Factory-specific execution contract for this repo.

It extends the accepted P0.2 repo / agent operating contract with:

- project-scoped Factory asset layout,
- bounded packet-execution conventions,
- headless `droid exec` conventions,
- review and approval rules for automated runs,
- failure-handling rules for repo-scoped Factory work.

This contract is additive.
It does not replace accepted repo truth, source authority, or the accepted-artifact-only rule.

## 2. Scope boundaries

### In scope

- Repo-shared Factory assets under `/.factory/`
- Skills used for bounded Canon repo work
- Headless execution conventions for one-shot automated runs
- Review and approval rules for automated runs that touch accepted artifacts
- Control-plane registration expectations for accepted P0.3 Factory artifacts

### Out of scope

- Redefining the accepted P0.2 baseline
- Packet-size targets, context-budget policy, local-doc-first policy, or subagent exploration rules from P0.5
- Runtime product architecture or product-truth changes
- A second orchestration stack
- Always-on automation as a base repo requirement
- Mandatory custom droid or hook implementations

## 3. Design constraints carried forward

- Accepted P0.2 repo truth remains the baseline.
- Accepted source-authority artifacts and accepted control-plane artifacts remain the default repo truth.
- Packet briefs narrow execution scope; they do not override accepted truth.
- Product truth remains human-owned.
- Factory.ai remains the base execution tool.
- CrewAI is not part of the base plan.
- Repo layout is a storage convention, not the platform architecture.
- No repo artifact may create a competing truth model.
- Reuse the accepted P0.1 artifact model, validation hooks, dependency semantics, and stale rules.

## 4. Factory workspace layout

The repo-scoped Factory workspace for this program lives under `/.factory/`.

Initial accepted P0.3 assets:

- `/.factory/AGENTS.md`
- `/.factory/skills/control-plane-packet-execution/SKILL.md`
- `/.factory/skills/review-guidelines/SKILL.md`

Optional later additions such as `/.factory/droids/` or `/.factory/hooks/` may be introduced only as additive repo tooling.
They must remain consistent with this contract and must not become a second orchestration stack.

## 5. Bounded Factory execution

### 5.1 Interactive work

- Follow `/AGENTS.md` plus the nearest descendant `AGENTS.md`.
- If a task includes a packet brief, treat it as the execution boundary.
- Without a packet brief, stay inside the explicit task scope and touch only required files.

### 5.2 Packet execution

- A bounded Factory run must start from either:
  - an accepted packet brief, or
  - an explicit task scope that identifies the governing accepted artifacts.
- Accepted artifacts are the default operating basis.
- If a packet changes an accepted artifact or adds a new accepted artifact, the packet must update:
  - `docs/control-plane/artifact-registry.seed.json`
  - `docs/control-plane/dependency-graph.seed.json`
- Do not invent ad hoc artifact metadata, validation hooks, edge types, or stale rules.
- Do not widen scope when required packet inputs are missing; stop and return a scope gap instead.

## 6. Headless execution conventions

Headless runs use `droid exec` as a one-shot bounded runner.

### 6.1 Required defaults

- Use `--cwd <repo-root>` for repo-scoped headless work.
- Start from read-only/spec-first behavior for analysis or planning runs.
- For mutating runs, require spec-first behavior before edits are applied.
- Prefer machine-readable output in automation (`--output-format json` or `stream-json`) so validation evidence is preserved.

### 6.2 Allowed autonomy bands in the base repo contract

- Default / no `--auto`: read-only analysis, planning, review, and validation preparation
- `--auto low`: bounded file creation and edits inside the approved task scope
- `--auto medium`: only when the packet’s real validators require local build/test/install or other reversible repo-local development commands

### 6.3 Disallowed by default

- `--auto high` as the default repo automation mode
- `--skip-permissions-unsafe`
- Push, deploy, or other remote side effects unless an explicit future task adds that authority
- Silent scope widening when a run needs more files, more authority, or different accepted truth than the packet allowed

## 7. Skills layout

### 7.1 `control-plane-packet-execution`

Purpose:
execute bounded Canon control-plane work against accepted artifacts and return validation-ready results.

Responsibilities:

- read governing accepted artifacts,
- preserve the packet or task boundary,
- keep registry and graph changes synchronized,
- run real validators that exist,
- prepare status and carry-forward output without self-accepting meaning.

### 7.2 `review-guidelines`

Purpose:
provide repo-specific review and approval-prep guidance for automated review runs.

Responsibilities:

- detect baseline drift,
- verify registry / graph integrity,
- verify validation-hook and stale-rule usage,
- flag P0.5-only policy leakage into P0.3,
- preserve the human-owned acceptance boundary.

## 8. Automated review and approval rules

### 8.1 Automated runs may

- draft and edit files inside the approved scope,
- run structural validators and consistency checks,
- prepare accepted-artifact updates for review,
- prepare master-plan status and carry-forward updates when deliverables and validators are complete.

### 8.2 Automated runs may not

- reopen accepted baseline decisions unless the task explicitly asks for that,
- claim acceptance without reviewable evidence,
- mark work done before deliverables exist and validators pass,
- silently skip required registry / graph synchronization for accepted artifacts,
- introduce P0.5-only packet-budget or context-policy behavior into P0.3,
- introduce a second orchestration stack.

### 8.3 Human review remains authoritative

Human review is still the acceptance gate for:

- accepted control-plane meaning,
- promotion of new accepted artifacts for downstream use,
- master-plan completion markers,
- append-only carry-forward entries that record completed accepted work.

Factory may prepare acceptance-ready patches and evidence, but it does not replace human acceptance authority.

## 9. Failure handling

- If scope is ambiguous, return a spec or scope gap instead of guessing.
- If validators fail, do not mark the task done.
- If required registry or graph updates are missing, the run is incomplete.
- If a headless run exceeds the approved autonomy band, fail fast rather than escalating automatically.
- If a run discovers a conflict with accepted repo truth, stop and surface the conflict explicitly.

## 10. Validation expectations for P0.3

P0.3 work in this repo must use real checks that currently exist:

1. JSON parse for edited or created `.json` files
2. Dependency-integrity checks that graph references resolve to registered artifact IDs
3. Verification that validation hooks, edge types, and stale rules come from accepted P0.1 catalogs
4. Cross-file consistency review against accepted P0.2 rules
5. Final scope review confirming that no P0.5-only policy was pulled into P0.3

## 11. Why this preserves the baseline

This contract does not:

- change the accepted-artifact-only rule,
- redefine the packet-brief baseline,
- make repo layout into platform architecture,
- invent a second orchestration stack,
- or transfer human-owned product truth to automation.
