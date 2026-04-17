# Phase 4 R6 Governed Agent / Applet Chat contract pack
Version: 1.0
Status: Accepted
Task: P4.8 — R6 Governed Agent / Applet Chat contract pack
Artifact ID: rel.r6-governed-agent-applet-chat-contract.v1
Release ID: r6-governed-agent-applet-chat-contract
Release scope: Accepted R6 contract pack covering Protocol/Applet/Workflow/Trigger surfaces, bounded background runs, queue/inbox governance, tool-execution hardening, inherited package floors, exit criteria, and explicit non-goals

This artifact is accepted for downstream use.

## 0. Convergence status (Phase 4+ update)

This contract pack was accepted as P4.8 under the accepted Phase 4 milestone
architecture plan (`rel.chat-native-milestone-architecture-plan.v1`) and the
accepted release-to-SDK maturity matrix
(`rel.chat-native-maturity-matrix.v1`).

As of Phase 4+ convergence:

- P4.7 remains the accepted upstream contract for governed prompt assets,
  adaptation lineage, and reusable execution inputs that R6 inherits rather
  than replaces.
- P4.9 (R7 Commissioning Bridge) is accepted as the direct downstream
  realization of the R6 handoff described in Section 5.
- Accepted Phase 5 governance and reusable-execution composition packs deepen
  the R6 governed reusable-execution substrate without reopening its
  no-hidden-autonomy or no-second-ontology refusal boundaries.
- Later accepted commissioning and Task Studio handoff surfaces inherit the R6
  locks on explicit policy, queue/inbox lineage, typed tool execution, and
  bounded background-run governance rather than softening them into agent
  theater.

This pack remains the accepted R6 contract authority. Sections below are kept
verbatim as the accepted human-owned contract record; convergence context is
noted here rather than rewritten into body sections.

## 1. Purpose

This pack turns the accepted milestone architecture story into the concrete contract for R6 Governed Agent / Applet Chat.

It exists to:

- define how governed reusable execution becomes real through Protocol, Applet, Workflow, and Trigger objects rather than agent theater,
- make bounded background runs, queue/inbox governance, and tool-execution hardening explicit after the accepted R5 prompt-asset boundary,
- lock the package-maturity floor, exit criteria, and anti-drift constraints for the R6 boundary.

## 2. Scope boundaries

### In scope

- the R6 user-facing product promise,
- the R6 reusable-execution continuity center and shared primitives,
- the R6 projection-only additions for agent profiles, starter context packs, memory policies, contradiction guards, and chatlet projections,
- the R6 package-maturity floor inherited from `rel.chat-native-maturity-matrix.v1`,
- the R6 exit criteria and explicit non-goals.

### Out of scope

- explicit Commission/Contract preflight as the primary interaction loop,
- Task Studio handoff completion,
- treating prompt assets or prompt cards as reusable execution ontology,
- hidden autonomy widening through applet settings, triggers, or background execution,
- second-stack orchestration drift or applet-private runtime semantics.

## 3. Inherited stage rules

### 3.1 R5 prompt-asset boundary remains binding

R6 inherits the accepted Platform Gate baseline plus the accepted R1-R5 release contracts.
Protocols, workflows, triggers, and applets may consume prompt assets, but they may not replace the accepted R5 lineage, staleness, and model-profile boundary with chat-local execution lore.

### 3.2 Reusable execution stays composed from run semantics

Protocols, workflows, triggers, and applets package accepted run semantics rather than creating a second execution ontology.
Background work therefore emits the same Run, Proof Bundle, State Delta, and Writeback Proposal objects as interactive work.

### 3.3 Authority, policy, and tooling remain explicit

Applet settings, workflows, triggers, memory policies, contradiction guards, and tool execution may constrain or route work, but they may not hide policy in prompt text or surface arrangement, widen authority silently, or bypass typed gateway contracts.

## 4. R6 contract

### 4.1 Stage summary

| Dimension | Contract |
| --- | --- |
| User-facing promise | Governed reusable execution becomes real as Protocol/Applet/Workflow/Trigger surfaces with bounded background runs, queue/inbox governance, and tool-execution hardening without replacing shared primitives or collapsing into agent theater |
| Continuity center | Reusable execution continuity through Protocol/Applet/Workflow objects |
| Shared primitives foregrounded | Protocol, Context Recipe, Strategy Preset, Verifier Pack, Workflow, Trigger, Applet, Run, Proof Bundle, State Delta, Writeback Proposal, Assignment |
| Projection-only additions | Agent Profile, Starter Context Pack, Memory Policy, Contradiction Guard, Chatlet Projection |
| Protected seams and scenarios | `SS-08`, `SS-12`, `GS-10`, `GS-11`, `EC-05`, plus Platform Gate tests `PG-06` and `PG-07` as inherited blockers |
| Handoff obligation | R6 -> R7 preserves protocol/applet context, governance state, run lineage, and approval/queue state while escalating serious work into explicit Commission and Contract objects |

### 4.2 Shared-object contract

| Object family | R6 contract |
| --- | --- |
| Protocol | Packages accepted run semantics through explicit run class, authority default, verifier slots, and writeback default instead of inventing a second execution ontology |
| Context Recipe | Keeps reusable context assembly explicit, frozen, and inspectable for protocol or applet launches rather than ambient chat memory |
| Strategy Preset | Reuses bounded strategy settings over accepted run semantics without carrying hidden authority or truth state |
| Verifier Pack | Makes verifier slots, evaluation policy, and failure basis explicit so applets and background runs cannot skip reviewable proof |
| Workflow | Composes protocol handoffs and stage rules over existing objects without replacing Run, Applet, Review, or Approval identities |
| Trigger | Starts scheduled or evented execution through explicit policy-bearing objects; enabling a trigger never widens authority or bypasses review |
| Applet | Installs governed reusable execution pinned to protocol version, policy bindings, and optional trigger/context/strategy refs while background execution still emits Run, Proof Bundle, State Delta, and Writeback Proposal objects |
| Run | Interactive and background launches share the same typed lifecycle, proof, delta, and gateway/tool event basis |
| Proof Bundle | Queue / Inbox, approval, and failure handling must surface verifier results, uncertainty, contradiction items, and policy violations rather than prose-only agent narration |
| State Delta | Every governed run produces explicit delta state, even when empty, instead of hiding consequences in chatlet settings or notifications |
| Writeback Proposal | Durable effects remain lane-separated, attributable, and review-gated even when proposed by background reusable execution |
| Assignment | Queue / Inbox routes pending governed work, approvals, failures, and escalations through attributable assignments with concrete next actions |

### 4.3 Projection-only additions

| R6 addition | Contract |
| --- | --- |
| Agent Profile | Projects a governed applet or agent stance, defaults, and boundaries over underlying Protocol, Applet, and Policy objects rather than becoming a new autonomous root |
| Starter Context Pack | Projects reusable starting context refs for governed runs while preserving explicit context-pack or recipe lineage |
| Memory Policy | Projects allowed memory read/write behavior as explicit policy that can constrain reuse without creating new truth objects or hidden authority |
| Contradiction Guard | Projects reusable contradiction-checking control so material conflicts stay explicit and attributable rather than being smoothed away by agent narration |
| Chatlet Projection | Presents a chat-facing applet or agent experience while preserving underlying Applet, Run, Proof Bundle, Queue / Inbox, and Writeback identities |

### 4.4 Package-maturity floor

| Package area | Required floor in R6 | Why R6 depends on it |
| --- | --- | --- |
| `pkg.tool-gateway-sandbox` | `M4` | R6 makes typed tool execution, side-effect classification, scoped credentials, and inspectable failures first-class and unavoidable |
| `pkg.shared-object-api` | `M4` | Protocols, workflows, triggers, applets, runs, and queue items must remain stable shared objects with explicit refs, versions, and policy bindings |
| `pkg.context-compiler` | `M4` | Starter context packs and context recipes must keep reusable execution grounded in explicit frozen inputs rather than ambient state |
| `pkg.event-provenance-spine` | `M4` | Background and interactive run lineage, queue transitions, gateway events, and approval history must remain append-only and reconstructable |
| `pkg.review-writeback` | `M4` | Queue / Inbox review, approval gates, and lane-separated writeback proposals remain binding even for governed background execution |
| `pkg.replay-compare` | `M4` | Protocol/app version comparisons, replay inspection, and governance review over reusable execution must operate on explicit refs rather than chat-local summaries |
| `pkg.model-gateway` | `M4` | Prompt-backed reusable execution still depends on typed provider abstraction rather than applet-local model lore |
| `pkg.environment-control` | `M3` | Workspace, app, authority, and enable/disable boundaries remain explicit for installed reusable execution |
| `pkg.monitor-inspect` | `M3` | Queue / Inbox, browser, board, live-monitor, and console surfaces must project authoritative reusable-execution state |

R6 must not overclaim commissioning-preflight or Task Studio handoff depth that belongs to R7 and later work.

### 4.5 Exit criteria

R6 is contract-complete only when all of the following are true:

1. A successful governed flow can be saved as a versioned Protocol and installed as an Applet without inventing a second execution ontology.
2. Protocols, Context Recipes, Strategy Presets, Verifier Packs, Workflows, Triggers, and Applets resolve to explicit shared objects with inspectable refs, versions, lifecycle state, and policy state rather than chat-local configuration blobs.
3. Prompt assets remain R5 lineage-bearing inputs to reusable execution and never replace Protocol/Applet identity or run-class ownership.
4. Background runs emit the same Run, Proof Bundle, State Delta, and Writeback Proposal objects as interactive work, and Queue / Inbox items resolve to concrete shared objects, urgency, and next actions.
5. Queue / Inbox, approval gates, and failure handling surface proof, delta, verifier outcomes, authority limits, and lane-separated writeback state rather than notification-only UI or agent narration.
6. Applet, Workflow, Trigger, Strategy Preset, and Memory Policy settings may narrow behavior but may not silently widen authority, bypass verifier slots, or mix writeback lanes.
7. Tool execution is typed, side-effect-classified, scoped by authority and credential bindings, and inspectable; background execution cannot hide tool results or failures behind chat phrasing.
8. Contradiction controls keep material conflicts explicit and attributable rather than smoothing them away inside reusable execution flows.
9. Serious work still hands off into explicit Commission/Contract semantics for R7 rather than being absorbed by R6 chat UX.

### 4.6 Explicit non-goals and refusals

R6 deliberately refuses to overbuild any of the following:

- agent theater or chat-private persona semantics as substitutes for Protocol, Workflow, Trigger, or Applet objects,
- hidden autonomy widening from prompts, applet settings, triggers, memory policy, or background runs,
- second-stack orchestration drift or applet-private execution ontology,
- prompt cards or prompt assets as substitutes for Protocol, Workflow, Trigger, or Applet semantics,
- applets or protocols bypassing verifier slots, queue/review/approval gates, or lane-separated writeback,
- policy, memory, or contradiction handling hidden in prompt text, transcript state, or surface arrangement,
- tool execution without typed side-effect classification, scoped credentials, and inspectable failures,
- treating R6 as the commissioning bridge or Task Studio handoff completion.

## 5. Downstream handoff to R7

R7 may escalate serious work into explicit Commission/Contract preflight, but it must inherit the R6 governed reusable-execution substrate rather than wrap it in chat-private commissioning semantics.

> P4.9 is now accepted as the direct downstream realization of this handoff.
> The locks below remain the R6 -> R7 inheritance record.

The R6 contract therefore carries forward these locks:

- protocol, workflow, trigger, and applet identities and versions remain explicit shared objects through the handoff,
- queue/inbox, background-run, and approval state preserve Run, Proof Bundle, State Delta, and Writeback Proposal lineage instead of collapsing into agent status prose,
- authority and policy remain explicit and non-self-expanding; serious widening still requires later Commission/Contract semantics,
- prompt assets remain reusable inputs to governed execution and commissioning rather than replacement execution ontology,
- typed model and tool gateway traces plus failures remain inspectable across live-monitor and preflight surfaces.

## 6. Downstream implications

- P4.9 should narrow into Commission, Contract, Authority Scope, preflight,
  live-monitor, proof-ledger, delta-inspection, and handoff semantics rather
  than rediscovering whether Protocol/Applet packaging and governed background
  execution are already real. *(Resolved - P4.9 accepted as the direct
  commissioning and handoff realization of this R6 boundary.)*
- Later releases must treat R6 as the proof that bounded autonomy is governed
  substrate rather than agent theater or second-stack orchestration.
  *(Resolved - inherited by accepted R7 and later Task Studio-safe follow-on
  surfaces.)*
- Phase 5 object and invariant packs should deepen Workflow, Trigger, Applet,
  proof, and governance semantics on top of this boundary rather than
  reopening it. *(Resolved - accepted Phase 5 governance and reusable-
  execution composition packs deepen this boundary without reopening it.)*

## 7. Acceptance notes

- This accepted artifact defines the R6 boundary, not the whole release doctrine.
- This accepted artifact keeps R6 intentionally focused on governed reusable execution and bounded background work so R7 can inherit one explicit governance story without ontology drift.
