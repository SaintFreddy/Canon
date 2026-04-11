# Phase 2 governance, authority, and writeback invariants
Version: 1.0
Status: Accepted
Task: P2.3 — Governance / authority / writeback invariants
Artifact ID: reuse.phase2-governance-authority-writeback-invariants.v1
Reuse scope: Accepted invariant layer for scope widening, lane separation, approval points, policy boundaries, and authority semantics

## 1. Purpose

This pack defines the minimum governance invariants that later releases, applets, and Task Studio work must preserve.

It exists to:

- make scope widening explicit,
- keep durable mutation lane-separated and reviewable,
- define where approval is mandatory,
- keep policy and authority inside explicit shared objects instead of prompt or view magic.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- invariant-level governance rules,
- authority semantics,
- writeback lane separation,
- approval-point requirements,
- policy-boundary rules.

### Out of scope

- full policy language,
- org-specific routing or quorum schemes,
- rollback/compensation mechanics,
- full proof/evaluation packs,
- applet packaging detail.

## 3. Invariant interpretation rules

### 3.1 Binding rule

These invariants bind all chat-native releases, reusable execution, and Task Studio work.
No projection may opt out of them.

### 3.2 Non-self-expansion rule

No prompt, view, mode, protocol, applet, or background-run setting may silently widen authority or durable write scope.

### 3.3 Deferred-depth rule

This pack locks the invariant layer only.
Detailed routing, compensation, policy DSLs, and proof/evaluation depth remain later work.

## 4. Invariant catalog

| Invariant ID | Category | Rule | Attached objects |
| --- | --- | --- | --- |
| `GI-01` | Scope widening | Any widened-read or writable work must carry explicit `authority_scope_ref`; commissioned or writable work must also carry `contract_ref` once serious work is in play. | Commission, Contract, Run, Authority Scope, Protocol |
| `GI-02` | Scope widening | Scope widening never happens in place on a live run; it requires a new or amended governing object and then a new run. | Contract, Authority Scope, Run, Protocol, Applet |
| `GI-03` | Lane separation | Durable mutation always flows `Run -> State Delta -> Writeback Proposal`; a delta is never the durable mutation itself. | Run, State Delta, Writeback Proposal |
| `GI-04` | Lane separation | One writeback proposal carries exactly one lane; cross-lane effects must be split into separate proposals. | State Delta, Writeback Proposal, Artifact, Memory Object, Canon Object, Workflow |
| `GI-05` | Lane separation | Conservative defaults are binding: only `transform` may default to artifact-lane proposal; memory, canon, workflow, and export require explicit objective, authority, and review. | Run Class, Protocol, Authority Scope, Writeback Proposal |
| `GI-06` | Approval points | No proposal reaches `applied`, and no canon candidate reaches `accepted`, without explicit review plus attributable approval decisions satisfying review policy. | Writeback Proposal, Review, Approval Decision, Canon Object, Memory Object |
| `GI-07` | Approval points | Partial acceptance stays lane-local, and approval history remains append-only and inspectable. | Review, Approval Decision, Writeback Proposal |
| `GI-08` | Policy boundaries | Policy must live in explicit policy-bearing objects, not in prompt text, transcript state, or surface arrangement. | Authority Scope, Contract, Protocol, Review, Applet, Workflow, Trigger |
| `GI-09` | Policy boundaries | Policy may constrain behavior but may not redefine shared ontology, collapse lanes, or bypass Run/Proof/Delta/Writeback objects. | Protocol, Applet, Run, Proof Bundle, State Delta, Writeback Proposal |
| `GI-10` | Authority semantics | Authority is conservative, explicit, and non-self-expanding; it comes from live approved scope objects and contract/protocol defaults, not from prompts, mode switches, or background execution. | Authority Scope, Contract, Run Class, Protocol, Applet, Writeback Proposal |

## 5. Approval-point matrix

| Approval point | Required gate | Why it exists |
| --- | --- | --- |
| Scope-widening before consequential rerun | Approved `Authority Scope` and, for serious work, accepted `Contract` before the next `Run` | Prevents silent authority inflation |
| Artifact/memory/workflow/export proposal application | `Review` resolved with attributable `Approval Decision` records before `Writeback Proposal` becomes `applied` | Prevents silent durable mutation |
| Canon promotion | `Review` resolved and candidate `Canon Object` explicitly moved to `accepted` | Preserves human-owned accepted truth |
| Applet-enabled writable behavior | Explicit protocol defaults plus authority scope and reviewable lane policy before writable background work | Prevents agent-builder-first drift |

## 6. Scenario and shortcut grounding

| Invariant | Strongest scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| `GI-01` | `GS-12`, `GS-13`, `GS-15`, `EC-06` | `fs.no-master-chat-truth`, `fs.no-chat-session-attached-runs`, `fs.no-transcript-first-rewrite-trap` |
| `GI-02` | `GS-11`, `GS-12`, `GS-14`, `EC-05`, `EC-07` | `fs.no-agent-builder-first`, `fs.no-transcript-first-rewrite-trap` |
| `GI-03` | `GS-06`, `GS-13`, `EC-03` | `fs.no-silent-proposal-application` |
| `GI-04` | `GS-07`, `GS-13`, `EC-03` | `fs.no-silent-proposal-application`, `fs.no-hidden-memory-sludge` |
| `GI-05` | `GS-10`, `GS-11`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-hidden-memory-sludge` |
| `GI-06` | `GS-07`, `GS-11`, `GS-13`, `EC-06` | `fs.no-silent-proposal-application`, `fs.no-hidden-memory-sludge` |
| `GI-07` | `GS-07`, `GS-13` | `fs.no-silent-proposal-application` |
| `GI-08` | `GS-09`, `GS-10`, `GS-11`, `EC-04`, `EC-05` | `fs.no-separate-backend-per-view`, `fs.no-agent-builder-first` |
| `GI-09` | `GS-10`, `GS-11`, `GS-14`, `GS-15`, `EC-05`, `EC-07` | `fs.no-separate-backend-per-view`, `fs.no-master-chat-truth` |
| `GI-10` | `GS-11`, `GS-12`, `GS-13`, `EC-05`, `EC-06` | `fs.no-agent-builder-first`, `fs.no-transcript-first-rewrite-trap` |

## 7. Boundary locks for downstream work

1. A run may read or propose only within explicit authority and contract scope.
2. A protocol or applet may narrow authority defaults, but it may not widen them silently.
3. Memory and canon remain distinct lanes with distinct review semantics.
4. Surface-level acceptance affordances must map back to Review and Approval Decision objects.
5. Task Studio inherits these invariants; it does not replace them with app-private governance.

## 8. Deferred to later governance/proof packs

| Later pack | Deferred detail |
| --- | --- |
| `P5.1` full governance / authority / writeback spec | org-specific routing, quorum, side-effect preview, rollback/compensation, delegation/escalation, operation-level partial acceptance inside one lane |
| `P5.2` full proof / validation / evaluation spec | verifier-pack definitions, task-family proof sections, replay/regression fixtures, scoring/thresholds, detailed failure taxonomy |

## 9. Downstream implications

### 9.1 For P2.4 and P2.5

- proof invariants and release semantic packs should treat these governance rules as fixed substrate constraints.

### 9.2 For P4.8, P4.9, and P5.3+

- governed applet chat, Commissioning Bridge, and full protocol packs must show how they preserve these invariant gates rather than hiding them in UI flow.

## 10. Review notes

Human review should confirm that this pack:

- makes scope widening, approval, and writeback rules explicit,
- keeps policy and authority in shared objects instead of transcript/view state,
- preserves lane separation and attributable approval history,
- does not overreach into detailed governance mechanics that belong later.
