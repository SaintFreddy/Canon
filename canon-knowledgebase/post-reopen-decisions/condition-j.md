# Decision Record — DEC-RO-05 Canon quarantined-draft fate (condition j)

- **Decision ID**: DEC-RO-05
- **Condition**: j (Canon quarantined-draft fate)
- **Scope**: Project-direction (escalated per delegation rule in canon-now.md)
- **Mode**: Human-only
- **Date recorded**: 2026-04-24
- **Recorded by**: plan-owner via Droid autonomous execution session
- **Origin issue**: SaintFreddy/Canon#12

## Chosen option

**Option 3 — Delete**, executed in **two sequenced packets** (correctness over speed):

1. **Packet A — Invariant sweep first** (`pkt.quarantine-invariant-sweep.v1`)
2. **Packet B — Physical removal + phase-6 prose reconciliation** (`pkt.quarantine-delete.v1`)

Packet B is hard-gated on Packet A landing (decision is authoritative: no deletion PR may merge until the invariant sweep PR has merged).

## What this decision rejects

- **Preserve** — rejected: draft decays over time and never carries its design into the post-reopen world. Dead weight in the repo.
- **Advance** — rejected: reopen already moved contract authorship to `docs/control-plane/` (registry JSON + surfaces + spec digests). Advancing the old `.mjs` contract-as-code format would be weeks of redundant work to produce artifacts the control-plane already holds in a different format.

## Factual basis (audited during decision)

Inventory of quarantined content at decision time:
- `Canon/packages/` — 6 packages, each a single `index.mjs` contract catalog
- `Canon/services/` — 4 services, each a single `index.mjs` contract catalog
- `Canon/workers/` — 1 worker, a single `index.mjs` contract catalog
- **Total**: 11 frozen JS contract-as-code files, ~1,369 lines
- **Inbound references from outside Canon/**: zero (verified via `grep -r "Canon/packages|Canon/services|Canon/workers|@canon/context-compiler-contracts|@canon/environment-control-contracts" agentic-engine canon-apps shared-environment`)
- **References in Canon's own build/tsconfig/workspace config**: zero
- **Overlap with current control-plane artifact-registry by ref name**: zero (the mjs ref names `contract.context-compiler.admitted-basis.*`, `svc.model-gateway.chat-turn-execution.*`, etc., appear 0 times in `docs/control-plane/`)
- **Domain overlap with control-plane**: present (73 hits for "context-compiler|model-gateway|shared-object" in artifact-registry.seed.json) — but under different ref names and a different authoring format

Conclusion: the quarantined content encodes real design insights (invariants, field schemas) that are NOT captured byte-for-byte in the current control-plane. The control-plane covers the same domains under different names and formats. The risk of deletion is losing the invariants, not losing code that anyone runs.

## Packet A — Invariant sweep scope

`pkt.quarantine-invariant-sweep.v1` must:

1. Extract every `invariants: Object.freeze([...])` array from all 11 `.mjs` files under `Canon/packages/`, `Canon/services/`, `Canon/workers/`.
2. For each invariant, identify the matching spec digest in `docs/spec-digests/` that covers the same subject (e.g., context-compiler invariants → `docs/spec-digests/agentic-engine/engine-compiler.md`; model-gateway invariants → `docs/spec-digests/agentic-engine/engine-gateway.md`).
3. For each invariant NOT already captured in the target spec digest, append a one-liner under the digest's "Invariants (from quarantined pre-reopen contract catalogs)" subsection. Attribution must name the origin mjs file and the condition-j provenance so future readers can trace where the wording came from.
4. Do NOT delete any files in Packet A. Packet A is pure read + append-to-spec-digests.
5. Verification: typecheck + test green; no mjs files modified; all new lines appear under a subsection clearly labelled as quarantine-sourced.
6. Produces PR that lists every invariant ported and every invariant judged "already captured, skipping."

## Packet B — Removal scope

`pkt.quarantine-delete.v1` must:

1. Verify Packet A's PR has merged to main. If not, fail closed with a blocker comment referencing Packet A.
2. `git rm -r Canon/packages Canon/services Canon/workers` — removes the 3 directories entirely. Git history retains the content for future archaeology.
3. Update phase-6 plan prose that references these directories as materializing inside Canon:
   - `docs/control-plane/surfaces/phase-6-repo-package-architecture-and-agent-execution-rules-pack.md` — replace any "Canon will host packages/services/workers" phrasing with "Canon is control-plane + authority only; runtime lives in agentic-engine/canon-apps/shared-environment under the post-reopen structure. DEC-RO-05 ratified 2026-04-24."
   - `docs/control-plane/core/master-plan.md` — same reconciliation.
   - Any other prose located by grep that expects these directories must be reconciled or annotated.
4. Append CF entry to `canon-knowledgebase/canon-knowledgebase-layer-carry-forward.md` (CF-0095 or next available) noting the deletion, the preceding invariant-sweep PR, and the DEC-RO-05 reference.
5. Verification: `git status` clean under `Canon/`, `git log --oneline -- Canon/packages` still shows history (sanity check that git retains the content), typecheck still green, no import breakage anywhere in the repo.

## What's preserved after Delete

- Git history — every mjs file remains at its last pre-deletion commit, retrievable via `git show <commit>:Canon/packages/...`.
- Invariants — ported into spec-digests under a clearly-labelled subsection (Packet A).
- Design-archaeology trail — this decision record + the Packet A PR + the Packet B PR form a reasoned chain for any future revisit.

## What's permanently surrendered

- The mjs contract-as-code FORMAT as a first-class authoring lane. The control-plane JSON+markdown registry is the sole contract-authoring path going forward.
- Any invariant that Packet A fails to port will be recoverable only via git history. This is the correctness risk Packet A exists to mitigate.

## Gating rules

- Packet B's issue body MUST cite this decision and MUST cite Packet A's merged PR as a prerequisite.
- Packet A's issue body MUST cite this decision and explicitly forbid any deletion of `Canon/packages/`, `Canon/services/`, `Canon/workers/`.
- The `post-reopen-remediation` skill enforces both gates automatically via its authority lookup.

## Revisit condition

Once Packet B lands, this decision is executed and frozen. Revisiting would mean re-introducing quarantined draft content, which is not anticipated. Any future "let's host packages in Canon again" decision is a new, unrelated decision and would not touch this record.
