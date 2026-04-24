# Decision Record — DEC-RO-04 LICENSE choice (condition e.2)

- **Decision ID**: DEC-RO-04
- **Condition**: e.2 (LICENSE choice)
- **Scope**: Project-direction (escalated per delegation rule in canon-now.md)
- **Mode**: Human-only
- **Date recorded**: 2026-04-24
- **Recorded by**: plan-owner via Droid autonomous execution session
- **Origin issue**: SaintFreddy/Canon#11

## Chosen option

**Option 4 — Proprietary / All Rights Reserved**

All 5 repos (Canon, agentic-engine, canon-apps, shared-environment, agentic-engine-history) ship with a proprietary LICENSE file of the form:

```
Copyright (c) 2026 SaintFreddy. All rights reserved.

This source code and all associated files are proprietary and confidential.
No license, express or implied, is granted to any person or entity for use,
copy, modification, distribution, or creation of derivative works of this
source code, in whole or in part, except as expressly authorized in writing
by the copyright holder.
```

## Implications

### Forecloses
- Public-SDK aspiration stated in `AGENTIC_WORKFLOW.md §9 L426` ("public SDK posture") is withdrawn under this decision. The aspirational phrasing in §9 must be reconciled — either removed or clearly marked as "future-state aspirational, not current license posture."
- Third-party forks / integrations are not legally permitted until this decision is revisited.
- External contributors cannot submit PRs under an open-source license assumption.

### Enables
- Full commercial flexibility for the 0.1.0 release posture. The code remains closed-source; no external fork risk; no OSS contributor agreements needed.
- Later reversal to MIT / Apache-2.0 / BSL remains possible at any future milestone without having already granted rights that must then be honored.
- Clear legal posture for any enterprise/private engagements negotiated during the pre-1.0 period.

### Does not affect
- Internal repo structure, build tooling, test suites, or spec-digests.
- The control-plane authority (canon-knowledgebase/, canon-now.md) — those are also proprietary by this same decision.

## Follow-ups authorized by this decision

1. **LICENSE file packet** (`pkt.add-proprietary-license.v1`) — add the Proprietary LICENSE file to the root of each of the 5 repos with the exact text above.
2. **AGENTIC_WORKFLOW.md reconciliation** — update §9 to mark "public SDK posture" as aspirational / not current, OR remove the phrasing entirely. The packet will draft both variants and surface the choice.
3. **README posture packet** (condition d) can now safely add LICENSE references pointing to the Proprietary file.
4. **CANON_PLAN_IMPACT_REPORT.md §6 row 6** — append a row noting DEC-RO-04 has landed on Option 4 and the public-SDK aspiration is withdrawn for 0.1.0.

## Revisit condition

This decision is not permanent. It may be revisited at any of the following milestones, and the revisit is recorded as a separate decision record (not by editing this file):

- Canon reaches 1.0 and a public SDK is ready to ship
- An external commercial partnership requires a specific license posture
- Plan-owner elects to shift to OSS for community growth reasons

Revisiting this decision does not retroactively license any past release — all 0.x releases remain proprietary unless explicitly re-licensed.
