# pkt.quarantine-invariant-sweep.v1

- **Packet ID**: `pkt.quarantine-invariant-sweep.v1`
- **Authority**: DEC-RO-05 recorded at `canon-knowledgebase/post-reopen-decisions/condition-j.md`
- **Carry-forward**: CF-0096
- **Scope**: `SaintFreddy/Canon` control-plane only
- **Ordering**: PREREQUISITE for `pkt.quarantine-delete.v1`. The delete packet is hard-gated on this packet's PR landing on main.
- **Execution mode**: Autonomous via `droid-issue-exec.yml`

## Goal

Before any physical removal of the quarantined draft directories (`Canon/packages/`, `Canon/services/`, `Canon/workers/`), extract every design invariant encoded in their `.mjs` contract-as-code files, identify which invariants are already captured in the post-reopen spec-digests, and port any uncaptured invariants as one-liners into the correct spec-digest file. This preserves design knowledge that git history alone doesn't make discoverable.

## Factual basis (pre-audited during decision)

- **Files in scope**: 11 `.mjs` files totaling 1,369 LOC across 3 directories:
  - `Canon/packages/context-compiler-contracts/admitted-basis/index.mjs`
  - `Canon/packages/environment-control-contracts/run-launch/index.mjs`
  - `Canon/packages/event-provenance-contracts/run-lineage/index.mjs`
  - `Canon/packages/model-gateway-contracts/chat-turn/index.mjs`
  - `Canon/packages/shared-object-api/run-continuity/index.mjs`
  - `Canon/packages/shared-object-schemas/run-and-source/index.mjs`
  - `Canon/services/environment-shell-api/conversation-entry/index.mjs`
  - `Canon/services/event-provenance/run-trace/index.mjs`
  - `Canon/services/execution-control/run-dispatch/index.mjs`
  - `Canon/services/model-gateway/chat-turn-execution/index.mjs`
  - `Canon/workers/context-compiler/compile-run-context/index.mjs`
- **Inbound imports**: zero from outside `Canon/` (audited).
- **Ref-name overlap with control-plane**: zero (audited).
- **Domain overlap with spec-digests**: present but under different naming.

## Execution steps

1. **Extract**: For each of the 11 `.mjs` files, parse out every `invariants: Object.freeze([...])` array. Record each invariant as: `{file, contract_catalog_id, invariant_text}`.

2. **Map to spec digest**: For each extracted invariant, identify the target spec digest under `docs/spec-digests/` by subject:
   - `context-compiler-*` → `docs/spec-digests/agentic-engine/engine-compiler.md`
   - `model-gateway-*` → `docs/spec-digests/agentic-engine/engine-gateway.md`
   - `event-provenance-*` → `docs/spec-digests/agentic-engine/engine-core.md` (or create a new provenance-specific digest if one does not exist; prefer adding to engine-core to avoid scope growth).
   - `environment-control-*` / `environment-shell-api` → `docs/spec-digests/shared-environment/env-control.md`
   - `shared-object-api` / `shared-object-schemas` → `docs/spec-digests/shared-environment/env-shared-objects.md`
   - `execution-control` → `docs/spec-digests/shared-environment/env-governance.md`
   - `context-compiler` worker → `docs/spec-digests/agentic-engine/engine-compiler.md`

3. **De-duplicate against existing digest content**: For each invariant, grep the target digest for the key concept (e.g., "Explicit admitted inputs take precedence"). If the concept is already present, mark as "already-captured, skipping." Use semantic match; exact string match is not required. When unsure, port it.

4. **Append under clearly-labelled subsection**: In each target spec digest, create (or append to) a subsection with this exact heading and body:

   ```
   ## Invariants (ported from quarantined pre-reopen contract catalogs, DEC-RO-05)

   The following invariants were extracted from `Canon/{packages|services|workers}/<path>/index.mjs`
   during the quarantine invariant-sweep packet (`pkt.quarantine-invariant-sweep.v1`,
   authorized by DEC-RO-05 / CF-0096). The source files were subsequently removed by
   `pkt.quarantine-delete.v1`; git history retains them for archaeology.

   - *[invariant text]* — sourced from `Canon/<path>/index.mjs` contract `<contract_id>`.
   - ...
   ```

5. **Do NOT delete the .mjs files**. This packet is read-and-append only.

## Forbidden

- Do NOT delete, rename, or modify any file under `Canon/packages/`, `Canon/services/`, `Canon/workers/`. That is Packet B's job.
- Do NOT touch `canon-now.md`, `canon-knowledgebase/`, `AGENTIC_ENGINE_AUDIT_LOG.md`, `CANON_PLAN_IMPACT_REPORT.md` (authority records).
- Do NOT invent invariants. Only port invariants that exist verbatim in the `.mjs` source.
- Do NOT merge invariants from different source files into one bullet. One invariant = one bullet, with origin attribution.

## Verification

- `git diff --stat` shows changes ONLY in `docs/spec-digests/*.md` files.
- `git diff -- Canon/packages Canon/services Canon/workers` is empty.
- PR body lists every invariant found (categorized as "ported" vs "already-captured, skipped") with file attribution.
- A final checklist confirms all 11 source files were scanned.
- `pnpm typecheck` (if applicable in Canon) + Canon's spec-digest validation remain green.

## PR body template

The PR must include:
- Summary of invariants found per source file
- For each invariant: "ported to `X.md`" or "already-captured in `Y.md` section Z, skipped"
- A statement confirming Packet B (`pkt.quarantine-delete.v1`) is now authorized to execute

## Audit trail

After this packet's PR merges:
- Append CF-0097 to `canon-knowledgebase-layer-carry-forward.md` listing the invariants ported (can be appended separately by plan-owner or by a follow-up packet — not required inside this packet's PR).
- `pkt.quarantine-delete.v1` becomes unblocked. Plan-owner may then re-comment `@droid run` on that packet's issue, or the workflow auto-advances if the issue body cites this PR's merge.
