# Phase 5 full governance, authority, and writeback spec
Version: 1.0
Status: Accepted
Task: P5.1 — Full governance / authority / writeback spec
Artifact ID: reuse.phase5-governance-authority-writeback-spec.v1
Reuse scope: Accepted machine-usable governance pack for policy composition, approval routing, side-effect preview, partial acceptance, rollback/compensation, and scope-aware writeback

## 1. Purpose

This pack turns the accepted invariant governance layer and accepted R7 commissioning boundary into the full operational governance spec.

It exists to:

- define how policy, authority, approval, side-effect preview, and writeback application compose across shared objects,
- make governance machine-usable and reviewable instead of remaining only conceptual,
- lock the operational rules for partial acceptance, compensation, and Task Studio-safe governance continuity.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- policy-bearing object roles and precedence,
- authority admission and scope-widening rules,
- approval routing and decision semantics,
- side-effect preview and run-preflight disclosure rules,
- scope-aware writeback and application behavior,
- partial acceptance and rollback/compensation behavior,
- governance continuity through the R7 -> Task Studio handoff.

### Out of scope

- org-specific people/team routing catalogs,
- domain-specific policy DSLs,
- full verifier-pack or evaluation-rubric depth,
- run-class-specific protocol schemas,
- Task Studio layout or presentation details beyond governance continuity.

## 3. Governance interpretation rules

### 3.1 Invariant-preservation rule

`reuse.phase2-governance-authority-writeback-invariants.v1`, `reuse.phase2-proof-validation-invariants.v1`, and `rel.r7-commissioning-bridge-contract.v1` remain binding.
`GI-01` through `GI-10` plus `PI-08`, `PI-09`, `PI-10`, and `RC-07` remain the minimum contract floor for this deeper pack.
This pack deepens them; it does not revise or bypass them.

### 3.2 Stricter-boundary-wins rule

When two policy-bearing objects differ, the stricter scope, review, or writeback rule wins.
Any loosening requires a new approved governing object before the next consequential run or apply step.

### 3.3 Append-only-governance-history rule

Review, approval, writeback, and compensation history remain append-only and attributable.
Rollback or compensation uses new runs, proposals, reviews, or superseding objects rather than silent undo.

## 4. Policy and authority contract model

### 4.1 Policy-bearing object roles and precedence

| Object | Governance role | Precedence posture | May not do |
| --- | --- | --- | --- |
| Authority Scope | Declares grants, limits, and policy refs for admitted read/write behavior | Highest hard boundary; conflicting rules resolve to the stricter limit | Define objective, acceptance policy, or hidden view-local behavior |
| Contract | Narrows a Commission into executable scope, deliverables, run class, and acceptance policy | Governs serious work ahead of protocol/applet defaults | Widen authority without a new approved scope object |
| Protocol | Packages conservative run, proof, verifier, and writeback defaults | Default only; narrowed by Contract and Authority Scope | Override stricter authority or mix writeback lanes |
| Review | Routes decisioning, required roles, and decision policy for a subject | Governs approval of scope changes or proposals, not execution semantics | Apply durable change or widen authority by itself |
| Applet | Reusable execution envelope with policy bindings and enablement state | May narrow timing or background posture inside approved scope | Grant hidden authority or bypass review/writeback gates |
| Workflow | Composes protocol handoffs and stage rules across reusable execution | May narrow sequence and allowed transitions | Replace Run/Proposal identity or collapse lanes |
| Trigger | Declares schedule/event start conditions | May narrow when work starts | Authorize new scope or writable behavior on its own |

### 4.2 Authority admission and rerun matrix

| Admission path | Minimum refs and gates | New run required? | Notes |
| --- | --- | --- | --- |
| Bounded read-only run inside current wedge | Objective plus frozen admitted basis | Yes | No widened authority is implied |
| Widened read or additional source access | Approved `authority_scope_ref` and, once serious work is in play, `contract_ref` | Yes | No in-place widening of a live run |
| Commissioned consequential run | Accepted Commission, accepted Contract, approved Authority Scope | Yes | Preserves `Commission -> Contract -> Run` chain |
| Artifact-lane proposal generation | Transform-class or protocol default artifact-lane posture plus authority and contract posture above | Yes | Artifact lane is the only default proposal lane |
| Memory/canon/workflow/export proposal generation | Explicit objective, approved authority scope, contract when serious, and reviewable lane policy | Yes | Never a default writeback lane |
| Background writable run | Enabled applet/workflow/trigger plus explicit authority scope and reviewable lane policy | Yes, per execution | Background execution does not widen authority |
| Proposal application | Resolved Review, attributable Approval Decisions, and lane-specific policy satisfied | No new user run; explicit apply job only | Application stays explicit and terminal |
| Compensation or superseding action | New Contract/Authority scope when needed plus new run or new lane-local proposal linked to the prior outcome | Yes or new proposal | Compensation never rewrites prior history |

### 4.3 Scope-widening and amendment rules

1. Any widened read or writable behavior requires a new or amended Authority Scope and then a new run.
2. Any material Contract amendment creates a new `contract_id` linked through `amends_contract_ref` before downstream execution.
3. Preflight must show requested scope, granted scope, denied capabilities, and any conditions or expiry relevant to execution.
4. No prompt, retry, replay, enable toggle, or approval action may smuggle wider scope without the new governing object chain above.

## 5. Approval routing and decision model

### 5.1 Approval-routing matrix

| Governance event | Review subject | Minimum routing basis | Allowed outcomes | Required continuation |
| --- | --- | --- | --- | --- |
| Scope widening before consequential rerun | Authority/Contract change set | Requested vs granted scope, risk basis, reason for widening, expiry/condition refs | `approved`, `approved_with_conditions`, `rejected`, `deferred` | Approval creates the new governing objects, then a new run may start |
| Artifact-lane proposal application | Artifact-lane `Writeback Proposal` | `operation_set`, target objects, proof basis, lane policy | `approved`, `approved_with_conditions`, `rejected`, `deferred` | Conditions or partial approval must leave residual operations explicit |
| Memory-lane proposal application | Memory-lane `Writeback Proposal` | Activation/deactivation basis, target memory refs, proof basis | `approved`, `approved_with_conditions`, `rejected`, `deferred` | Residual or conditioned memory work becomes explicit follow-up proposal state |
| Canon promotion | Canon candidate plus supporting proposal/proof basis | `acceptance_basis_refs`, acceptance policy, proof basis, reviewer set | `approved`, `approved_with_conditions`, `rejected`, `deferred` | Canon remains unaccepted until the explicit review chain resolves |
| Workflow/export-lane application | Lane-local `Writeback Proposal` | Target refs, side-effect preview if external, lane policy, proof basis | `approved`, `approved_with_conditions`, `rejected`, `deferred` | Apply or remediation path stays explicit and attributable |
| Writable background enablement | Applet/workflow/trigger policy binding | Protocol defaults, authority scope, reviewable lane policy, side-effect posture | `approved`, `rejected`, `deferred` | Approval enables background work; later runs remain individually governed |
| Compensation or superseding action | Compensating proposal or amended contract | Prior outcome refs, remediation basis, scope delta, proof basis | `approved`, `approved_with_conditions`, `rejected`, `deferred` | Approval creates explicit superseding work; no silent undo |

### 5.2 Decision-outcome semantics

| Outcome | Meaning | Effect on review/proposal state | What must stay explicit |
| --- | --- | --- | --- |
| `approved` | Decision policy is satisfied for the submitted scope or proposal | Review may resolve; proposal may move to `approved`/`applied` when gates are satisfied | Exact decision scope, decider identity, and approval basis |
| `approved_with_conditions` | Approval exists but only for an explicitly conditioned subset or path | Review stays open or proposal enters `partially_approved` until conditions are satisfied | Conditions, residual operations, and any required follow-up run/proposal |
| `rejected` | Submitted scope or proposal is refused | Review or proposal path becomes terminal for that subject | Rejection rationale and unaffected remaining work |
| `deferred` | Work is blocked pending more information or authority | Review remains open with blocking items; no apply or rerun proceeds | Missing inputs, blocking items, and re-entry conditions |

### 5.3 Delegation and escalation rules

1. Delegation records delegator, delegate, decision scope, and expiry; it does not create hidden authority.
2. Escalation may add required roles or stricter decision policy, but it does not erase earlier attributable decisions.
3. Delegated or escalated routes may narrow or clarify the approval path; they may not widen scope without the explicit authority/contract amendments from Section 4.

## 6. Side-effect preview and preflight model

### 6.1 Side-effect class contract

| Side-effect class | Minimum preview content | Governance posture | Compensation posture |
| --- | --- | --- | --- |
| `none` | Declared no external side effects beyond bounded computation | Normal run admission plus any writeback review rules still apply | No external compensation path needed |
| `read_only_external` | External systems touched, credential binding, data categories accessed, expected read scope | Must remain inside approved authority scope; no writeback implied | Audit only; no fake writeback or undo semantics |
| `reversible_external_write` | Target system/object, side-effect preview or dry-run basis, expected mutation class, retryability, reversal path | Explicit authority plus review when consequential; preview required when supported | Compensation path must be declared before execution |
| `irreversible_external_write` | Blast radius, irreversible warning, operator-visible approval basis, remediation posture if available | Highest explicit review and authority posture; no silent auto-apply or hidden retry | Remediation only; irreversibility must remain visible in proof and ledger |

### 6.2 Run Preflight disclosure matrix

| Preflight element | Derived from | Must answer |
| --- | --- | --- |
| Objective and contract fit | Commission, Contract, Run Class | What is being done, under which contract, and with which run-class intent |
| Authority scope | Authority Scope, Contract | Which reads/writes are allowed, denied, narrowed, or conditioned |
| Frozen admitted basis | Input snapshot, Evidence/Context refs, Context compiler basis | What exact basis will be used and what is excluded |
| Proof and verifier plan | Protocol, proof policy, verifier slots/pack refs | How the result will be evaluated and what counts as failure |
| Side-effect preview | Tool side-effect class, preview refs, dry-run result or lack thereof | What external effects may occur and how reversible they are |
| Writeback preview | State Delta, Writeback Proposal, target-object refs | Which lanes and operations may change if approved |
| Review path | Review policy, required roles, decision policy | Who must decide and what remains pending |
| Failure or compensation posture | Failure classes, compensation model, prior outcome refs when relevant | What happens if execution fails, conditions are unmet, or reversal is requested |

### 6.3 Preview integrity rules

1. Preview results are derived views linked back to authoritative Run, Tool, State Delta, or Writeback Proposal refs.
2. If dry-run or preview is unavailable, preflight must say so explicitly and surface the elevated risk/approval posture.
3. No tool execution may start before its declared side-effect class and authority basis are bound to the admitted run.

## 7. Scope-aware writeback and application model

### 7.1 Lane contract matrix

| Lane | Default eligibility | Required scope and contract posture | Review/apply posture | Compensation posture |
| --- | --- | --- | --- | --- |
| `artifact` | Only default proposal lane for `transform`/protocol defaults | Artifact-target read plus proposal authority; contract required once serious work is in play | Explicit Review and Approval before `applied` | Superseding artifact revision/proposal; no history erase |
| `memory` | Never default | Explicit objective, authority scope, and contract when serious | Lane-local review and approval before activation/deactivation | Deactivation or superseding memory proposal |
| `canon` | Never default | Explicit authority, acceptance basis, and review chain | Review plus attributable Approval Decisions before candidate becomes `accepted` | Superseding/demotion path stays explicit; accepted history is never erased |
| `workflow` | Never default | Explicit objective, authority scope, and reviewable policy | Lane-local review before workflow/trigger state changes apply | Disable, retire, or supersede through a new explicit proposal |
| `export` | Never default | Explicit objective, authority scope, side-effect preview, and review | Lane-local review plus external side-effect posture before apply | Compensating export/remediation record or explicit irreversibility note |

### 7.2 Application phase contract

| Phase | Required inputs | Output | Rule |
| --- | --- | --- | --- |
| Proposal drafting | `State Delta`, lane target, authority scope, operation set | `Writeback Proposal` in `drafted` state | One proposal per lane; no mixed-lane object |
| Submission | Draft proposal plus linked `Review` container | Proposal in `submitted`; review active | Submission never implies approval |
| Partial approval handling | Decision records plus explicit accepted/residual operation mapping | Proposal in `partially_approved` or successor proposal/residual op set | No operation may disappear silently |
| Final approval | Resolved Review plus attributable Approval Decisions | Proposal in `approved` | Approved scope cannot exceed the submitted operation set |
| Apply | Approved proposal plus lane policy and apply job inputs | Proposal in `applied` plus apply result refs/events | Application is explicit and terminal |
| Post-apply audit | Apply results, review history, compensation posture | Append-only audit trail and any follow-up compensation work | Audit never rewrites the applied record |

### 7.3 Scope-aware application rules

1. Apply workers enforce tenant, scope, and target-object filters at apply time, not only at run time.
2. Approval cannot expand `target_object_refs` or `operation_set`; any expansion requires a new proposal.
3. Export or other external side effects must carry preview basis and remediation posture into the post-apply audit trail.

## 8. Partial acceptance and rollback/compensation model

### 8.1 Partial-acceptance granularity

| Granularity | Allowed? | Requirements | Resulting records |
| --- | --- | --- | --- |
| Lane-level across separate proposals | Yes | Separate lane proposals stay independent | Some proposals may apply while others remain rejected/deferred |
| Operation-level within one lane | Yes | Accepted and residual operations must be explicit and attributable | Original proposal enters `partially_approved` and residual work stays in explicit successor state |
| Condition-based approval | Yes | Conditions remain explicit; no silent proposal edits | Open items or successor proposal before final apply |
| Cross-lane partial acceptance inside one proposal | No | Work must first be split into separate lane proposals | No mixed-lane object is ever approved/applied |

### 8.2 Rollback and compensation matrix

| Lane | After-apply posture | Allowed compensation pattern | What must never happen |
| --- | --- | --- | --- |
| `artifact` | Applied artifact revision becomes historical fact | New run/proposal creates superseding revision or corrective artifact | Deleting or mutating the applied history in place |
| `memory` | Activation/deactivation remains historical fact | New proposal supersedes or deactivates the memory object | Erasing prior activation history |
| `canon` | Acceptance remains attributable historical fact | New review/proposal may supersede or retire current canon status explicitly | Rewriting accepted canon history in place |
| `workflow` | Enabled/disabled/retired workflow state remains historical fact | New proposal disables, retires, or supersedes the workflow/trigger | Silent background disablement without explicit governance |
| `export` | External effect or publication remains historical fact | Compensating export, recall, or remediation record when supported; otherwise explicit irreversibility note | Pretending an irreversible external effect was undone |

### 8.3 Compensation rules

1. Compensation never rewrites proof, review, approval, or event history.
2. If compensation requires more authority than the original act, a new Authority Scope and Contract path is required before execution.
3. Irreversible external effects remain explicit in proof, ledger, and audit state even when remediation is attempted.

## 9. Scenario and shortcut grounding

| Governance area | Strongest scenarios / edge cases | Shortcut protection |
| --- | --- | --- |
| Scope widening and commissioning preflight | `GS-12`, `GS-13`, `EC-06` | `fs.no-master-chat-truth`, `fs.no-transcript-first-rewrite-trap`, `fs.no-agent-builder-first` |
| Lane-separated writeback and partial acceptance | `GS-07`, `GS-13`, `EC-03` | `fs.no-silent-proposal-application` |
| Background writable behavior and side-effect preview | `GS-11`, `EC-05` | `fs.no-agent-builder-first`, `fs.no-silent-proposal-application` |
| Memory/canon/workflow/export boundaries | `GS-07`, `GS-15`, `EC-03` | `fs.no-hidden-memory-sludge`, `fs.no-silent-proposal-application` |
| Task Studio-safe governance continuity | `GS-14`, `EC-07` | `fs.no-master-chat-truth`, `fs.no-separate-backend-per-view` |

## 10. Boundary locks for downstream work

1. `P5.2` may deepen proof and evaluation, but it may not let proof replace authority, review, or writeback objects.
2. `P5.3` protocol packs must encode authority defaults, preview classes, review hooks, and writeback posture using this governance model.
3. `P5.4` workflow, trigger, applet, pack, and integration specs must reuse the routing, enablement, side-effect, and compensation rules here.
4. `P5.5` and `P5.7` must project these governance objects and append-only histories into Task Studio without object translation.
5. Repo/package or infrastructure choices may not collapse authoritative lanes or append-only governance history into generic backend state.

## 11. Downstream implications

### 11.1 For P5.2 and P5.3

- proof packs should attach verifier/evaluator detail to this routing, approval, and compensation model rather than redefining it,
- protocol packs should map run-class defaults, proof hooks, and failure classes onto this accepted governance substrate.

### 11.2 For P5.4 through P5.7 and Task Studio

- reusable-execution composition packs and Task Studio packs should use this spec as the operational governance baseline for enablement, review, compensation, and handoff continuity.

## 12. Review notes

Human review should confirm that this pack:

- makes policy composition and authority precedence explicit,
- turns review and writeback routing into machine-usable rules,
- keeps side-effect preview, partial acceptance, and compensation explicit and append-only,
- preserves R7 -> Task Studio governance continuity without inventing new ontology.

