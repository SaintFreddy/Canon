# Post-reopen remediation packet queue

Version: 1.0
Status: Scaffolds only — not authorized for execution without recorded plan-owner decisions.

This directory holds seven remediation packet scaffolds for the Phase 4+ step 20 audit-cited-contradiction reopen hold. Each packet depends on one or more recorded plan-owner decisions in `canon-knowledgebase/post-reopen-decisions/`.

## Dependency order

```
condition (a) decision  ─┬─> pkt.remediate-clock-timeprovider.v1       (wave A.1)
                         ├─> pkt.remediate-thaw-timestamp-authority.v1 (wave A.2, after A.1)
                         ├─> pkt.remediate-localecompare-sort-paths.v1 (wave A.3, can parallel A.2)
                         └─> pkt.remediate-frozenat-in-hashed-doc.v1   (wave A.4, after A.1 + frozenAt decision)

condition (d) decision  ──> pkt.remediate-stablestringify-unification.v1 (wave A.5, parallel A.1-A.4)

condition (b) decision  ─┬─> pkt.remediate-credentialscope-enforcement.v1 (wave B.1)
                         └─> pkt.remediate-toolsandboxworker-fork.v1      (wave B.2, parallel B.1)

condition (f) decision  ──> pkt.remediate-platform-gate-truth-status.v1   (wave C, control-plane only)
                                                                           (ordering depends on the decision:
                                                                            formal reopen = first,
                                                                            retain-with-footnotes = last)
```

## Execution gating

Each packet's `Prerequisite condition` field names the recorded decision(s) that must exist under `canon-knowledgebase/post-reopen-decisions/` before execution is authorized. If the prerequisite is missing, the `post-reopen-remediation` skill will refuse to start.

## Not in this queue

The following reopen conditions do not have remediation packets in this initial queue:
- (c) policy-matcher pattern vs strict-equals
- (e) LICENSE + engine version discipline
- (g) intra-workspace peerDependency carve-out
- (h) replay-compare diff-semantics
- (i) successor checkpoint acknowledgement (already handled in `canon-now.md`)
- (j) Canon/packages,services,workers quarantine status

Those either resolve by authoritative statement without code changes, or belong to later waves. Add new packet scaffolds here as those decisions come due.

## Model and runtime posture

All remediation packets pin:
- `model: claude-opus-4-7`
- `reasoning_effort: high`

Runtime can be either GitHub Actions (via `@droid` issue tag) or a local CLI session. The CLI session is preferred when the packet touches more than ~20 files or needs live interaction for edge cases.

## How to kick off a remediation packet

Once the prerequisite decision is recorded:

1. Open a new issue on `SaintFreddy/agentic-engine` titled `[remediation] <packet-id>`.
2. Body: `@droid` tag plus a one-paragraph description referencing the packet file path and the recorded decision file path.
3. The Opus 4.7 droid workflow picks it up. The `post-reopen-remediation` skill enforces scope and validators.
4. PR opens; `droid-review.yml` (Opus 4.7) auto-reviews.
5. If green and decisions match, auto-merge fires (assuming branch protection requires `droid-review` + CI).
6. The Monday weekly audit reports on every merged remediation PR.
