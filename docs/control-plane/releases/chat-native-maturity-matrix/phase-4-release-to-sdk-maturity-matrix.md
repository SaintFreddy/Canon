# Phase 4 release-to-SDK maturity matrix
Version: 1.0
Status: Accepted
Task: P4.1 — Release-to-SDK maturity matrix
Artifact ID: rel.chat-native-maturity-matrix.v1
Release ID: chat-native-maturity-matrix
Release scope: Accepted cross-stage matrix mapping Platform Gate and R1-R7 to required SDK/package maturity floors for the chat-native path

## 0. Convergence status (Phase 4+ update)

This matrix was accepted as P4.1, establishing the first cross-stage
package-maturity baseline for the chat-native path.

As of Phase 4+ convergence:
- P4.2 (milestone architecture plan) and P4.3-P4.9 (R1-R7 contract packs)
  have each cited this matrix as their package-maturity authority.
- Phase 5 semantics packs (P5.1-P5.7) inherited the M4 floors established
  here for `pkg.shared-object-api`, `pkg.review-writeback`, `pkg.replay-compare`,
  `pkg.model-gateway`, `pkg.environment-control`, and `pkg.monitor-inspect`.
- Phase 6 implementation packets (P6.2-P6.6) mapped the nine package areas in
  §5 to concrete execution packets without collapsing their ownership boundaries.

This matrix remains the package-maturity authority. §9 downstream implications
are kept verbatim as the original intent record; convergence outcomes are
noted here.

> **Platform Gate reopen notice (2026-04-23).** This artifact transitively depends on `arch.phase3-platform-gate-spec.v1`. On 2026-04-23 the plan-owner (SaintFreddy) recorded a formal reopen of the Platform Gate P3.6 acceptance marker against the 2026-04-18 agentic-engine audit-cited contradiction event per `canon-knowledgebase/post-reopen-decisions/condition-f.md` (Option A). Platform Gate's next status is `pending PG-01.1 + PG-07.1 + PG-10.1`. This artifact itself remains `accepted` for downstream use — the release doctrine and package-maturity guidance below are unchanged and are not reopened. Consumers reading this artifact should, however, be aware that PG-01.1 (Clock + stableStringify + localeCompare + frozenAt), PG-07.1 (credentialScope enforcement), and PG-10.1 (spawnToolSandboxWorker + IPC export) are remediation sub-gates still closing. Engine sub-gate remediation landed on `SaintFreddy/agentic-engine` main on 2026-04-24 via 8 autonomous PRs (see `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` CF-0089..CF-0096); downstream blueprint propagation landed via Canon PR #35 (PG-R2, see CF-0098). The sub-gates formally close after the small sub-gate-closure packet flips PG-01.1 / PG-07.1 / PG-10.1 from pending to closed in the Platform Gate spec §0.1.1, which is hard-gated on this packet (PG-R3) landing. See `docs/control-plane/architecture/phase-3-platform-gate-spec-and-exit-audit.md` §0.1 for the full gate reopen markup and successor-checkpoint reference.

## 1. Purpose

This pack turns the accepted Platform Gate package areas into one explicit release-maturity matrix.

It exists to:

- show which package areas each release forces to become more real,
- prevent release names from hand-waving missing substrate maturity,
- give Phase 4 and Phase 6 one shared baseline for what must harden when.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- Platform Gate through R7 package-maturity floors,
- maturity-level definitions,
- stage-by-stage floor raises,
- anti-handwave rules for later release packs.

### Out of scope

- the human-only milestone architecture plan in P4.2,
- per-release product-promise detail beyond maturity forcing,
- exact repo/package layout,
- implementation blueprints or packetization,
- Task Studio post-R7 surface details.

## 3. Matrix interpretation rules

### 3.1 Inherited-floor rule

Later stages inherit all maturity floors already forced by earlier stages.
No later release pack may silently downgrade an earlier floor.

### 3.2 Promise-to-package rule

If a release promise centers a capability, the supporting package areas must be at least `M3` for that stage.
If the capability must carry continuity or governance into later stages, the package areas must reach `M4`.

### 3.3 Bridge-stage rule

Platform Gate, R4, and R7 are bridge stages.
When a package area becomes part of one of those bridge seams, the matrix raises it to a carry-forward floor rather than a stage-local one.

### 3.4 No-handwave rule

A later release pack may not claim a capability while pointing to a package area that is below the floor required here.
Inherited substrate maturity must be cited explicitly rather than assumed as magic.

### 3.5 Logical-package rule

The package areas below are logical seams, not repo-shape mandates.
Phase 6 may map them into concrete packages or services, but it may not collapse their ownership boundaries.

## 4. Maturity scale

| Level | Meaning |
| --- | --- |
| `M1` | Substrate-real: the seam exists on the shared substrate and passes Platform Gate on real execution paths |
| `M2` | Stage-usable: the stage can expose the seam in a bounded, user-visible or operator-visible flow |
| `M3` | Stage-critical: the release promise breaks if this seam is weak or fake |
| `M4` | Carry-forward: later stages must inherit this seam as a hardened substrate assumption rather than reopen it |

## 5. Package-area baseline

| Package area | Baseline responsibility in this matrix |
| --- | --- |
| `pkg.shared-object-api` | Shared object refs, queries, and continuity-bearing contracts |
| `pkg.environment-control` | Admission, replay, branch, review, preflight, and monitor entrypoints |
| `pkg.context-compiler` | Evidence/context freeze, injection, replay basis, and compilation diagnostics |
| `pkg.event-provenance-spine` | Append-only events, lineage, replayable cursors, and audit reconstruction |
| `pkg.review-writeback` | Lane-local proposal, review, approval, and apply behavior |
| `pkg.replay-compare` | Checkpoints, branch/replay execution, basis diffs, and compare handling |
| `pkg.model-gateway` | Provider abstraction, model-profile behavior, usage accounting, and typed failures |
| `pkg.tool-gateway-sandbox` | Typed tool execution, side-effect classification, scoped credentials, and logs |
| `pkg.monitor-inspect` | Live monitor, inspectors, ledgers, and projection-grade inspection surfaces |

## 6. Release-to-SDK maturity matrix

| Package area | Platform Gate | R1 | R2 | R3 | R4 | R5 | R6 | R7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `pkg.shared-object-api` | `M1` | `M2` | `M3` | `M3` | `M4` | `M4` | `M4` | `M4` |
| `pkg.environment-control` | `M1` | `M3` | `M3` | `M3` | `M3` | `M3` | `M3` | `M4` |
| `pkg.context-compiler` | `M1` | `M3` | `M4` | `M4` | `M4` | `M4` | `M4` | `M4` |
| `pkg.event-provenance-spine` | `M1` | `M2` | `M3` | `M4` | `M4` | `M4` | `M4` | `M4` |
| `pkg.review-writeback` | `M1` | `M1` | `M1` | `M2` | `M4` | `M4` | `M4` | `M4` |
| `pkg.replay-compare` | `M1` | `M1` | `M2` | `M4` | `M4` | `M4` | `M4` | `M4` |
| `pkg.model-gateway` | `M1` | `M2` | `M2` | `M2` | `M2` | `M4` | `M4` | `M4` |
| `pkg.tool-gateway-sandbox` | `M1` | `M1` | `M1` | `M1` | `M1` | `M1` | `M4` | `M4` |
| `pkg.monitor-inspect` | `M1` | `M2` | `M3` | `M3` | `M3` | `M3` | `M3` | `M4` |

## 7. Stage forcing summary

| Stage | New floor raises forced here | Why this stage forces them |
| --- | --- | --- |
| Platform Gate | All listed package areas -> `M1` | The substrate must already be real before any public release contract is credible |
| R1 Transcript Chat | `pkg.environment-control` -> `M3`; `pkg.context-compiler` -> `M3`; `pkg.shared-object-api`, `pkg.model-gateway`, `pkg.event-provenance-spine`, `pkg.monitor-inspect` -> `M2` | Familiar chat UX still has to run on bounded runs, frozen context, source grounding, and compact inspection rather than transcript truth |
| R2 Context Chat | `pkg.context-compiler` -> `M4`; `pkg.shared-object-api` -> `M3`; `pkg.replay-compare` -> `M2`; `pkg.event-provenance-spine` and `pkg.monitor-inspect` -> `M3` | Explicit pack control, freeze, diff, and replay move context assembly out of backstage status and make it a permanent substrate commitment |
| R3 Branch / Visual Thinker | `pkg.event-provenance-spine` -> `M4`; `pkg.replay-compare` -> `M4`; `pkg.review-writeback` -> `M2` | Semantic branching, replay, compare, and merge proposals require explicit lineage and proposal-bearing state rather than transcript forks |
| R4 Artifact Workspace | `pkg.shared-object-api` -> `M4`; `pkg.review-writeback` -> `M4` | Artifact-centered continuity and proposal inbox flows become a bridge seam that later stages must inherit unchanged |
| R5 Prompt Studio | `pkg.model-gateway` -> `M4` | Prompt assets, model profiles, and adaptations force provider abstraction to become governed substrate rather than hidden lore |
| R6 Governed Agent / Applet Chat | `pkg.tool-gateway-sandbox` -> `M4` | Bounded reusable execution and background work make typed tool execution, side-effect classification, and scoped credentials first-class and unavoidable |
| R7 Commissioning Bridge | `pkg.environment-control` -> `M4`; `pkg.monitor-inspect` -> `M4` | Commission/Contract preflight, live monitoring, proof ledger, delta inspection, and chat-to-run handoff require commissioning-grade control and inspection seams |

## 8. Anti-drift locks for later release packs

1. Later release packs must reference this matrix when naming the package areas they force to mature.
2. A stage may build on inherited `M4` floors, but it may not re-describe them as optional or view-local.
3. No release pack may claim a new continuity center while lowering the run-native, provenance-bearing, or lane-separated substrate floors already forced here.
4. Phase 6 repo/package work must preserve these logical seams even if the concrete module map differs.

## 9. Downstream implications

### 9.1 For P4.2 and later Phase 4 contract packs

*(Resolved - P4.2-P4.9 accepted, all citing this matrix.)*

- the human-only milestone architecture plan and the later R1-R7 packs should use this matrix as the package-maturity baseline instead of rediscovering it stage by stage.

### 9.2 For Phase 5 reusable semantics

*(Resolved - P5.1-P5.7 accepted on inherited M4 floors.)*

- protocol, workflow, applet, proof, governance, and handoff packs should assume the relevant `M4` floors already exist and focus on semantic deepening rather than substrate reinvention.

### 9.3 For Phase 6 repo/package planning

*(Resolved - P6.2 repo/package execution baseline and P6.3-P6.6 packets
accepted against these areas.)*

- concrete package and service plans should map directly onto these forced areas and their stage floors.

## 10. Review notes

> Review completed at acceptance (P4.1). The criteria below are kept as the
> original audit record; they are met by the accepted downstream packs.

Human review should confirm that this matrix:

- makes every release force explicit substrate maturity,
- keeps Platform Gate and the bridge releases from being hand-waved,
- gives Phase 4 and Phase 6 one shared package-maturity story,
- does not smuggle repo-shape or view-local shortcuts back into the release doctrine.
