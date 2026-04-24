# Canon Tasks

This is the no-noise tracker for long-running Canon work across threads.
Open this first when more than one Canon task is live.

## Update Rules

- Track the task, not the chat thread.
- Add a row when work will span more than one thread, commit, or session.
- Update a row only when durable state changes: opened, status moved, branch changed, commit made, push landed, blocker changed, or next checkpoint changed.
- Keep `Latest durable state` to one blunt sentence.
- When a task is done, move it to `Recently Closed` with the last commit and last push recorded.
- For workspace-doc tasks that are not inside a git repo, use `n/a` for `Last commit` and `Last push`.

## Status

`active`, `handoff`, `blocked`, `parked`, `done`

## Active Tasks

| Task ID | Status | Surface | Latest durable state | Thread / ref | Last commit | Last push | Next checkpoint |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agentic-system-phase-4-release` | `handoff` | `canon-ref:dev/kb` + `github.com/SaintFreddy/{Canon,agentic-engine,canon-apps,shared-environment,agentic-engine-history}` | Phase-4+ reopen closure plus Platform Gate follow-up/sub-gate closure are complete, the baton is ready, and the next bounded step is intentionally unassigned pending plan-owner selection. | `canon-ref:dev/canon-now` + `CF-0097..CF-0100` | `n/a (multi-repo wave; see CF-0097..CF-0100)` | `Canon/main@2026-04-24; agentic-engine/main@2026-04-24; canon-apps/main@2026-04-24; shared-environment/main@2026-04-24; agentic-engine-history/main@2026-04-24` | Choose one bounded next track: Phase 6 materialization pilot, second-model review pass, or another explicit plan-owner task. |

## Parked Or Blocked

| Task ID | Status | Surface | Latest durable state | Thread / ref | Last commit | Last push | Resume trigger |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `wiki-rigor-phase-3` | `parked` | `wiki-play/wiki-system/` + `wiki-play/phase-3-wiki/` | Wiki remains preserved as the dropped first-attempt planning record; it is not the active architecture path for the knowledgebase rollout. | `T-019d9042-79b2-7161-9101-55eb977ffe0a` | `n/a` | `n/a` | Resume only if you need historical comparison, contradiction review, or recovery of lessons from the dropped Wiki path. |
| `canon-wiki-startup` | `parked` | `wiki-play/canon-wiki/` | Canon Wiki startup surfaces are preserved as historical handoff material from the dropped Wiki attempt, not as active rollout authority for the knowledgebase plan. | `T-019d903d-3f3b-7548-8e38-2357608a15dd`; oldest seeded thread `T-019d81a4-6bb1-718c-8b4c-38e6fefbcbe0` | `n/a` | `n/a` | Resume only if later historical review needs the preserved startup seed or handoff notes. |
| `shared-environment-starter` | `parked` | `shared-environment/` + `shared-environment-starter-packet.md` | A real local `shared-environment` checkout now exists, so the old missing-checkout blocker is gone; the starter packet is parked until the shared-environment track is explicitly selected. | `shared-environment-starter-packet.md` | `n/a` | `n/a` | Choose the shared-environment track as the next bounded step, then recover from `shared-environment-starter-packet.md` against the real checkout. |

## Recently Closed

| Task ID | Closed state | Surface | Final durable result | Last commit | Last push |
| --- | --- | --- | --- | --- | --- |
| `post-reopen-remediation-wave-a` | `done` | `canon-knowledgebase/post-reopen-decisions/` + `github.com/SaintFreddy/{Canon,agentic-engine,canon-apps,shared-environment,agentic-engine-history}` | All reopen decisions are recorded, the full remediation + Platform Gate follow-up wave is closed, the baton is `ready`, and the next bounded step is intentionally unassigned pending plan-owner selection. | `n/a (multi-repo wave; see CF-0089..CF-0100)` | `Canon/main@2026-04-24; agentic-engine/main@2026-04-24; canon-apps/main@2026-04-24; shared-environment/main@2026-04-24; agentic-engine-history/main@2026-04-24` |
| `agentic-engine-finish-and-handoff` | `done` | `canon-ref:engine` + `agentic-engine-finish-session-plan.md` + `shared-environment-starter-packet.md` | Session 6 is complete: the engine finish track produced a durable next-repo handoff packet, identified `shared-environment` as the next layer above `canon-ref:engine`, and stopped honestly at the then-missing-checkout boundary. | `agentic-engine:06bc935` | `agentic-engine/main@2026-04-17` |
| `canon-ref-v1` | `done` | `canon-ref:dev/scripts/canon-ref.py` + `canon-ref:dev/kb/identity/canon-ref-registry.json` + active authority markdown | Canon-Ref v1 scaffold is landed locally, the active live-doc scope is migrated to Canon-Ref tokens, and `python3 scripts/canon-ref.py validate --registry canon-knowledgebase/identity/canon-ref-registry.json` passes. | `n/a` | `n/a` |
| `model-ref-v1` | `done` | `canon-ref:dev/kb/identity/model-ref-registry` + `canon-ref:dev/scripts/model-ref.py` + `canon-ref:dev/scripts/migrate-amp-coupling.py` + active authority markdown | Model-Ref v1 is landed locally, the live baton and router surfaces are runner-neutral, and the deterministic runner-coupling inventory tool is available for report/apply reruns. | `n/a` | `n/a` |
| `baton-flow-contract-v1` | `done` | `canon-ref:dev/baton/baton-protocol` + `canon-ref:dev/baton/baton-automation-plan` + `canon-ref:dev/scripts/canon-baton-next.sh` + active authority markdown | Baton flow is now explicitly defined as session-owned successor creation with one exact baton packet that should be injected directly into one fresh same-runner successor when the host exposes that path, otherwise written verbatim into durable files. | `n/a` | `n/a` |
| `baton-safety-hardening-v1` | `done` | `canon-ref:dev/baton/baton-protocol` + `canon-ref:dev/baton/baton-automation-plan` + `canon-ref:dev/scripts/canon-baton-next.sh` + `canon-ref:dev/kb/identity/model-ref-registry` + active authority markdown | Baton safety hardening is now landed locally: `canon-ref:dev/canon-now` carries an explicit stop-state gate, the baton helper emits no successor packet while that state is `stop`, Model-Ref validation enforces the typed runner-adapter contract, and the runner-coupling migration checker distinguishes stale path drift from intentional runner-adapter references. | `n/a` | `n/a` |
| `runner-adapter-cli-capability-audit-v1` | `done` | `canon-ref:dev/kb/identity/model-ref-registry` + `canon-ref:dev/scripts/model-ref.py` + `canon-ref:dev/baton/baton-protocol` + `canon-ref:dev/baton/baton-automation-plan` + active authority markdown | Codex and Claude Code baton adapters are now tied to verified local CLI startup, resume, and fork surfaces with prompt injection, and the native baton label is reserved only for runners with a verified in-session handoff tool. | `n/a` | `n/a` |

## Row Template

```md
| `task-id` | `active` | `path/or/surface` | One blunt sentence about current durable truth. | `T-...` or other durable ref | `abc1234` or `n/a` | `branch@YYYY-MM-DD` or `n/a` | Next concrete checkpoint. |
```
