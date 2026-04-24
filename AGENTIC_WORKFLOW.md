# Canon — Agentic Development Workflow

> **Canonical operating manual for any agent session working on Canon.**
> Date authored: 2026-04-18. Solo developer; team-sized meta-tooling budget.
> Domain: TypeScript zero-runtime-dep agentic-engine platform — SDK + 7 layer products + shared environment + apps.
>
> **This document must be read AFTER `CANON_PROJECT_CONTEXT.md`.** Any conflict resolves in favor of that document. Recommendations that violate §7 (do-not-recommend) or §4 (hard constraints) of `CANON_PROJECT_CONTEXT.md` are invalid and must be rejected even if asked for.

---

## 0. How to read this document

You (the assistant receiving this) are being given the *operating manual* for a closed-loop, agentic-led development pipeline tuned for Canon's actual identity:

- **TypeScript pnpm monorepo agentic-engine platform** (`packages/`, `workers/`, `contracts/`, `tests/`, `docs/spec-digests/`)
- **Zero external runtime dependencies, permanently** — root devDeps are exactly `@types/node`, `typescript`, `vitest`; production code only imports `node:*` builtins
- **Canon-native tool protocol** (user-built) supersedes MCP; do not recommend `@modelcontextprotocol/sdk`
- **Multi-tier release**: SDK + seven engine-layer products + shared environment + apps; **apps are the revenue center**
- **Six-week solo timeline** for the full multi-tier scope (as of April 2026)
- **Cloudflare Workers shape** is the deployment surface (V8 isolate, no Node-only runtime APIs except in build/CLI tools)
- **Nineteen typed primitives** per `All Prims.md §5` are load-bearing; every workflow phase must cite specific primitive IDs

The author is a solo developer who has chosen to spend a team-sized budget on **meta-tools that operate ON the project** rather than on runtime libraries shipped IN the project. They have committed to the workflow below; do not recommend "just use Cursor + Claude Code" because that is the single-IDE failure mode this design specifically prevents. Equally, do not recommend any runtime library — the zero-dep property is a permanent design property, not a phase.

When asked to do work, you should:

- Operate as one of the named **stations** in the pipeline (§4).
- Honor the **four-protocol rule** (§2). Do not invent a fifth IPC mechanism.
- Cite the relevant **primitive ID** (5.1–5.19 per `All Prims.md`), `exports.json` surface, or Canon spec digest when justifying a decision.
- Defer correctness verdicts to the **Canon-native verification gates** (contract conformance, replay-compare determinism, spec-drift, vitest, cross-repo contract tests). LLMs draft; the gates decide.
- Never bypass Linear or the Canon-Ref registry. Linear is the single source of truth for work state; Canon-Ref is the single source of truth for accepted-authority pointers.

---

## 1. Mental model in one paragraph

The pipeline is a directed graph from "I had an idea" to "the change is merged, contract-verified, replay-equivalent, and indexed into accepted knowledge." It has **seven stations**: Research → Architecture Decision → Ripple Analysis → Spec Authoring → Bounded-Task Dispatch → Agent Execution → Verification Gates & Knowledge Capture. Each station owns exactly one responsibility, owns exactly one set of meta-tools, and emits exactly one well-typed artifact (often itself a Canon primitive — `ObjectiveSpec`, `EvidenceSet`, `CompiledContextPackage`, `StrategyGraph`, `ProofBundle`, `AcceptedKnowledgeObject`) that the next station consumes. Frontier models (Claude, GPT, Gemini, Grok) are *workers inside stations* invoked by orchestration scripts via vendor SDKs at the dev-tool layer — they are never imported into Canon runtime code. The human's daily job collapses to: judging architectural debates, reviewing the ~5–15 PRs the system surfaces with green gates, and intervening on the small set of issues Linear's "Needs Human" filter shows.

---

## 2. The four protocols (and nothing else)

| Protocol | Used for | Concrete shape |
|---|---|---|
| **Canon-native tool protocol** (user-built) | Agent ↔ tool calls inside Canon runtime | `@canon/engine-tool-gateway` `ToolAdapter` / `ToolRegistry` / `ToolSandbox` over `node:child_process`-based `tool-sandbox` worker. **Do not import `@modelcontextprotocol/sdk` or any MCP binding.** |
| **REST / GraphQL webhooks** | Service ↔ service state transitions for the dev pipeline | Cloudflare Workers (Wrangler-deployed) are the universal glue layer. Inbound webhooks from Linear / Traycer / GitHub fan out to orchestration scripts. |
| **GitHub Actions** | All verification gates and CI-side execution | One workflow file per gate; parallel; blocking via required-status-checks on protected `main`. |
| **Vendor SDKs at the orchestration layer only** | Direct model invocations from `scripts/*.ts` orchestration files (NOT from `packages/` or `workers/` runtime) | TypeScript scripts run via `pnpm tsx` from laptop or a Cloudflare Worker. `@anthropic-ai/sdk`, `xai`, `openai`, `@google/generative-ai` are permitted in `scripts/` and dev-only tooling — never in `packages/*` or `workers/*`. |

If the urge arises to add a Slack bot orchestrator, a Zapier flow, an Electron control panel, or a fifth IPC mechanism — refuse. That is how this stack rots. If the urge arises to import any runtime library into `packages/*` or `workers/*` — refuse harder. The zero-dep property is permanent.

---

## 3. Tool inventory and sole responsibilities

All tools below are **meta-tools, dev-tools, CLIs, or external observer services accessed over HTTP**. None are runtime dependencies of Canon's `packages/*` or `workers/*` code. The runtime stays at zero deps.

### 3.1 Meta-agent IDEs and orchestrators (already in the owner's stack)

| Tool | Sole responsibility | Triggered by |
|---|---|---|
| **AMP (Sourcegraph)** | Primary agentic IDE for human exploratory work and cross-repo queries | Human, interactively (already the owner's daily driver) |
| **Factory.AI droids** | Long-horizon (L-tier) autonomous execution against bounded tasks | Linear router → `.factory/` skills already in the repo |
| **Claude Code + Claude Agent SDK** | Standing-orders container; reusable agent recipes; baton protocol participant | `.mcp.json` (dev-tooling MCP only — see §2 caveat) and `claude-skills/` loaded per session |
| **Conductor** | Parallel M-tier Claude Code sessions with human as observer dashboard | Linear router |
| **Augment Code** | Deep semantic symbol graph over the monorepo as a meta-tool (NOT imported); used for ripple analysis | Every agent session on startup; ripple analyzer |
| **Traycer.ai** | Spec authoring + spec-drift verifier against Canon control-plane | Human authors; CI runs drift on every PR |

### 3.2 Frontier models (invoked from orchestration scripts only — never from runtime)

| Model | Sole responsibility | Triggered by |
|---|---|---|
| **Claude Opus 4.7 (extended thinking)** | Debate judge; ripple-effect analysis; multi-reviewer personas; complex spec-drift adjudication | `scripts/*.ts` orchestration files |
| **Claude Sonnet 4.6** | Bulk agent work inside Claude Code / Factory droids; first-pass triage of test failures | Inside Claude Code, Factory droids, CI workflows |
| **Claude Haiku 4.5** | Cheap batch classification (label suggestion, flake detection, log clustering) | CI hooks |
| **Grok 4 Heavy** | Multi-persona architectural debate (proponent / skeptic / historian / downstream-consumer / security) | `scripts/adr-debate.ts` |
| **GPT-5 / Codex Cloud** | Parallel async PR generation when Factory.AI is saturated | Linear router fallback |
| **Gemini 3 Pro (2M context)** | Whole-monorepo dump analysis when Augment + AMP can't fit it | `scripts/ripple-analyzer.ts` >1M-token fallback |

### 3.3 Research and human-in-loop

| Tool | Sole responsibility | Triggered by |
|---|---|---|
| **Perplexity Computer** | External research orchestration (competitive landscape, standards, framework releases) | Human ad-hoc; cron for moving targets (TC39, Cloudflare Workers updates, agentic-framework npm releases) |
| **Linear + Linear Agents + Linear MCP (dev-tooling MCP only)** | Single source of truth for "what work exists, what state it's in" | Traycer webhook in; router Worker out |

### 3.4 CI / dev / verification (compatible with §8 of `CANON_PROJECT_CONTEXT.md`)

| Tool | Sole responsibility | Triggered by |
|---|---|---|
| **vitest** (already a devDep) | Unit + integration + cross-repo contract tests | `pnpm test` locally; `01-vitest.yml` in CI |
| **tsc** (`tsc --noEmit`) | Type checking — the lint surface (no ESLint, no Biome, no Prettier per §2 of context) | `pnpm typecheck`; `02-typecheck.yml` |
| **Custom `scripts/build-package.mjs`** (already in the repo) | Per-workspace build | `pnpm build`; packaging tests verify the output |
| **`packages/*` and `workers/*` contract verification** | `contracts/exports.json` matches actual exported surface | `tests/cross-repo-contracts.test.ts` (already implemented); `03-contract-conformance.yml` |
| **Replay-compare worker** (`workers/replay-compare/`, already implemented) | Deterministic replay across provenance / model / context / strategy boundaries | `04-replay-determinism.yml`; runs before any PR touching `provenance/`, `model-gateway/`, `context-compiler/`, or `policy/` merges |
| **Traycer drift API** | Spec drift between PR diff and accepted Canon control-plane specs | `05-spec-drift.yml`; blocks if `drift_severity != "none"` |
| **ast-grep** (CLI) | Structural lint for control-plane validators (e.g., catch any `import` from a non-`node:` module appearing in `packages/*` or `workers/*`) | `06-zero-dep-guard.yml` |
| **gitleaks** (CLI) | Secret scanning on every commit attempt | Skill on commit; `07-gitleaks.yml` |
| **Cloudflare Wrangler** (CLI) | Workers deployment | `pnpm wrangler deploy` per worker |
| **GitHub Actions** | Orchestration of all gates above | Every PR |
| **Codspeed** | Continuous performance regression gate (free for open source; HTTP-uploaded result) | GitHub App, every PR |

### 3.5 External observer services (HTTP/JSON only — no client SDK imported)

| Service | Sole responsibility | How it's wired (zero-dep-compliant) |
|---|---|---|
| **Langfuse self-hosted** | Trace forensics for orchestration scripts; opened only when bisecting a Braintrust regression | `fetch()` to Langfuse OTLP/HTTP JSON ingest endpoint from `scripts/*.ts` (orchestration only). **Do not import `langfuse` client SDK.** |
| **Braintrust** | Agent-quality KPI tracking over time (per-agent `merge_no_revert`, `all_gates_first_try`) | `fetch()` to Braintrust HTTP ingestion endpoint from `12-knowledge-capture.yml`. **Do not import `braintrust` client SDK.** |

If observability ever becomes required *inside* runtime code (`packages/*` or `workers/*`), emit the **OpenTelemetry wire format** (OTLP/HTTP with JSON payloads) directly via `fetch`. This keeps the zero-dep property while staying standards-compliant. **Do not import `@opentelemetry/api` or any `@opentelemetry/*` package.**

### 3.6 Canon-internal control-plane infrastructure (already in place)

| Component | Sole responsibility |
|---|---|
| **Canon-Ref registry** (`canon-ref:*` tokens, `scripts/canon-ref.py`) | Single source of truth for accepted-authority pointers across repos |
| **Packet protocol** (P00–P13 and beyond) | Bounded knowledge-package handoffs between sessions |
| **Baton protocol** (`amp-baton/amp-deep-baton.md`) | Cross-session context handoff between AMP sessions |
| **Factory skills** (`.factory/skills/`) | Reusable Factory droid recipes |
| **Control-plane validators** (`scripts/validators/validate_control_plane_integrity.py` in Canon control-plane repo) | Mechanical guard against architecture drift |
| **Artifact registry** (`docs/control-plane/artifact-registry.seed.json`) + dependency-graph seeds | Cross-repo coordination of release artifacts and tier dependencies |
| **Spec digests** (`agentic-engine/docs/spec-digests/`) | Task-scoped extracts from Canon control-plane; agents read these before reaching for upstream Canon documents |

---

## 4. Repository layout (canonical for `agentic-engine`)

This is the **engine repo** layout. The shared-environment, control-plane, and apps repos follow the same `contracts/` + `docs/spec-digests/` + `tests/cross-repo-contracts.test.ts` pattern. **Do not invent a different layout per repo.**

```
agentic-engine/
├── .github/
│   └── workflows/
│       ├── 01-vitest.yml
│       ├── 02-typecheck.yml
│       ├── 03-contract-conformance.yml      # exports.json ⇄ actual exports
│       ├── 04-replay-determinism.yml        # workers/replay-compare on PR
│       ├── 05-spec-drift.yml                # Traycer drift API
│       ├── 06-zero-dep-guard.yml            # ast-grep: no non-node imports in packages|workers
│       ├── 07-gitleaks.yml
│       ├── 08-codspeed.yml                  # perf regression
│       ├── 09-multi-reviewer.yml            # 5-persona Opus 4.7 reviewer
│       ├── 10-knowledge-capture.yml         # on-merge → Braintrust + AcceptedKnowledgeObject seed + Linear close
│       └── 11-packaging.yml                 # tarball + external-consumer packaging tests (already exist in tests/)
├── AGENTS.md                                # Repo-local execution projection (already exists)
├── CONTEXT.md                               # Repo purpose + boundary rules (already exists)
├── package.json                             # Root devDeps: @types/node, typescript, vitest — nothing else
├── pnpm-workspace.yaml
├── pnpm-lock.yaml                           # ~1.1k lines — minimal transitive graph
├── tsconfig.base.json                       # strict, ESM, .js import extensions
├── contracts/
│   ├── exports.json                         # canon.dev/schemas/repo-exports.v1.json
│   └── imports.json                         # depends only on Canon specs
├── docs/
│   └── spec-digests/                        # Task-scoped Canon extracts
│       ├── phase-1-engine-sdk.md
│       ├── phase-2-context-chat-engine.md
│       └── phase-3-branch-replay.md
├── packages/
│   ├── core/                                # 19 primitives (5.1–5.19) + typed errors
│   ├── context-compiler/                    # IngestionHandler, ContextCompilerPipeline, SnapshotFreezer
│   ├── model-gateway/                       # ModelAdapter, ProviderRegistry, CapabilityNegotiator
│   ├── tool-gateway/                        # ToolAdapter, ToolRegistry, ToolSandbox  ← Canon-native protocol lives here
│   ├── policy/                              # PolicyEvaluator, AuthorityScope, PolicyObject
│   ├── provenance/                          # ProvenanceGraph, EventStream, ReplayCursor, DiffEngine
│   └── validation/                          # ValidationPipeline, ProofAssembler, VerificationHook
├── workers/
│   ├── run-executor/                        # Bounded run execution (CF-Workers shape)
│   ├── context-compiler/                    # Standalone CompiledContextPackage assembly
│   ├── replay-compare/                      # Deterministic replay across primitive boundaries
│   └── tool-sandbox/                        # node:child_process tool execution (NOT container isolation)
├── tests/
│   ├── build-package-cleanliness.test.ts
│   ├── cross-repo-contracts.test.ts         # Already implemented — keystone gate
│   ├── external-consumer-packaging.test.ts
│   ├── packed-tarball-contents.test.ts
│   ├── packaging-test-utils.ts
│   └── phase-3-suite-lock.test.ts
├── scripts/
│   ├── build-package.mjs                    # Already exists
│   ├── adr-debate.ts                        # Grok 4 Heavy multi-persona orchestrator (vendor SDK OK in scripts/)
│   ├── ripple-analyzer.ts                   # Augment + Opus 4.7 extended thinking
│   ├── traycer-to-linear.ts                 # CF Worker (deployed via Wrangler)
│   ├── linear-router.ts                     # CF Worker: Linear → Factory / Conductor / Claude Code Action
│   ├── perplexity-to-knowledge.ts           # Research → AcceptedKnowledgeObject seed
│   └── post-verdict.ts                      # CI verdict poster
└── claude-skills/
    ├── verify-contracts/SKILL.md            # Validate exports.json matches actual surface
    ├── add-primitive/SKILL.md               # Add a 5.x primitive end-to-end (file + export + test + contract update)
    ├── port-spec-digest/SKILL.md            # Bring a fresh Canon spec extract into docs/spec-digests/
    └── triage-test-failure/SKILL.md         # Classify a vitest failure (real bug | flake | spec drift)
```

---

## 5. The Canon-native tool protocol substrate (`@canon/engine-tool-gateway`)

The Canon-native tool protocol is **not MCP**. It supersedes MCP for tool interop inside the Canon universe. It lives in `packages/tool-gateway/` and exposes:

- `ToolAdapter` — typed contract a tool implementation must satisfy
- `ToolRegistry` — registry of `RegisteredTool` entries with `ToolDefinition`, `CredentialScope`, `ToolCategory`
- `ToolSandbox` — execution surface backed by the `tool-sandbox` worker (`node:child_process`-based, NOT container isolation; documented as such)
- `ToolExecutionResult`, `ToolExecutionError`, `MockToolAdapter`, `MockToolAdapterOptions` — the test surface

A **`ToolInvocationRecord`** (primitive 5.12) is emitted for every action taken through a tool. The protocol is what makes `ToolInvocationRecord` typed end-to-end.

**Where MCP fits — and where it does NOT:**

- **Dev-tooling MCP servers (`.mcp.json`)** are permitted because they are not Canon runtime code. Augment, Linear, GitHub, Composio, Traycer dev MCP servers may be configured in the developer's `.mcp.json` for use by Claude Code / AMP / Factory droids during the dev pipeline. **They are CLIs spawned by the agent IDE, not imports.**
- **Canon runtime `packages/*` and `workers/*`** must NOT import `@modelcontextprotocol/sdk` or any MCP client/server library. Tool interop inside Canon flows through the Canon-native `ToolGateway`.

If a future requirement asks Canon to interoperate with an external MCP-only tool, the bridge is implemented as a `ToolAdapter` in user code that speaks MCP wire-format via `fetch` / `node:child_process` — never as a runtime dependency import.

---

## 6. Secrets layer

- All API keys in **1Password**, three vaults: `canon-prod`, `canon-ci`, `canon-personal`.
- Local invocation: `op run --env-file=.env.tpl -- <command>`.
- GitHub Actions: keys mirrored as **org-level secrets**: `ANTHROPIC_API_KEY`, `XAI_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `AUGMENT_API_KEY`, `AMP_TOKEN`, `TRAYCER_API_KEY`, `LINEAR_API_KEY`, `FACTORY_API_KEY`, `BRAINTRUST_API_KEY`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `CODSPEED_TOKEN`, `PERPLEXITY_API_KEY`, `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`.
- No keys in repo `.env`. `gitleaks` runs as a Skill on every commit attempt and as gate `07`.

---

## 7. Pipeline detail (every edge specified, every primitive cited)

The seven stations map onto Canon's primitives. **Every artifact emitted by a station should either be a Canon primitive instance or an explicit input to one.**

### Phase A — Research → AcceptedKnowledgeObject seed

1. Fire Perplexity Computer:
   ```
   POST https://api.perplexity.ai/computer/sessions
   { "objective": "<question>", "depth": "deep", "max_steps": 40, "output_format": "markdown_with_citations" }
   ```
2. Webhook → `scripts/perplexity-to-knowledge.ts` (Cloudflare Worker; uses `fetch` only, no client SDK).
3. The Worker emits a **draft `AcceptedKnowledgeObject`** (primitive 5.8) seed: structured candidate that the human promotes to `AcceptedKnowledgeObject` status via a Linear "promote knowledge" action. Until promoted, it lives as a `MemoryObject` (5.7) tagged `{class: "research", status: "candidate"}`.
4. The Worker creates an Augment annotation (`POST /v1/workspaces/<ws>/annotations`) tying the research to the relevant symbol IDs in `packages/*` so future agent sessions retrieve it as inherent context.

The trichotomy matters: research enters as `MemoryObject`, gets promoted to `AcceptedKnowledgeObject` only after human review. This is the engine's load-bearing distinction (§5.1 of `CANON_PROJECT_CONTEXT.md`); the workflow respects it from the inbox onward.

### Phase B — Architecture Decision (Grok 4 Heavy debate, Opus judge) → DecisionEvent

1. Human runs `pnpm tsx scripts/adr-debate.ts --title "<decision>"`.
2. Script issues 5 parallel `xAI` calls with persona system prompts: proponent / skeptic / historian / downstream-consumer / security. Each uses `model: "grok-4-heavy"`, `reasoning.effort: "high"`, `parallel_agents: 4`. **Vendor SDK calls live in `scripts/` only — never in `packages/*` or `workers/*`.**
3. `contextBundle` is built from Augment symbol-graph queries + a search across past `AcceptedKnowledgeObject` entries for prior decisions on this topic.
4. All five outputs concatenated → Claude Opus 4.7 judge call with `thinking.budget_tokens: 60000`.
5. Output written to `agentic-engine/docs/adr/NNNN-<slug>.md`, committed by the script.
6. A **`DecisionEvent`** (primitive 5.17) is materialized: `{decision_type, outcome, alternatives_considered, owner_invariants, accepted_authority_refs}`.
7. Augment annotation on every symbol the ADR touches.
8. If the decision creates or modifies a constraint, a **`PolicyObject`** (5.18) seed is also emitted into `packages/policy/` for review — machine-enforceable form first, prose second.

### Phase C — Ripple-Effect Deep-Dive (the unique seat for Opus 4.7 + Augment) → StrategyGraph

1. Human runs `pnpm tsx scripts/ripple-analyzer.ts --change "<one-liner>"`.
2. Augment graph expansion: `POST /v1/workspaces/<ws>/graph/expand` with `depth: 2, include_callers: true, include_callees: true, include_subtypes: true`. Cross-repo: query the Canon-Ref registry to fan out into `shared-environment` and `canon-apps` consumer surfaces.
3. AMP queries for downstream callers across the multi-tier surface (SDK + 7 layer products + environment + apps). Recall: every layer is a separable product, so a ripple in `packages/core/` may cascade into seven distinct release surfaces.
4. Bundle (typically 200–500K tokens; >1M falls back to Gemini 3 Pro) → Opus 4.7 with `thinking.budget_tokens: 100000`.
5. Output: cascading-implication tree → a **draft `StrategyGraph`** (primitive 5.10) JSON committed as `agentic-engine/docs/specs/ripple-<slug>.json`. Nodes = consumer surfaces affected; edges = the propagation order; phases = which release tier ships in which window. A Linear issue is opened with label `ripple-analysis-pending-review`.
6. Human reads, approves, modifies, or rejects. **~20 minutes; the most important judgment of the week** because each ripple potentially perturbs ten release surfaces.

### Phase D — Spec Authoring (Traycer) → ObjectiveSpec set

1. Human opens Traycer with the ADR (`DecisionEvent`), ripple JSON (`StrategyGraph`), Augment workspace, and Canon control-plane spec digests already linked.
2. Traycer outputs `agentic-engine/docs/specs/spec.md`, `plan.md`, and `tasks.json`. Every task entry is shaped to materialize as an **`ObjectiveSpec`** (primitive 5.2) when picked up:
   ```json
   {
     "tasks": [{
       "id": "T-001",
       "title": "...",
       "spec_fragment": "...",
       "raw_instruction": "...",                       // → ObjectiveSpec.raw_instruction
       "interpreted_objective": "...",                 // → ObjectiveSpec.interpreted_objective
       "execution_class": "implementation|test|doc",   // → ObjectiveSpec.execution_class
       "acceptance_criteria": ["..."],                 // → ObjectiveSpec.acceptance_criteria
       "primitive_refs": ["5.6", "5.10"],              // Which All-Prims §5.x entries the task touches
       "exports_json_surface": ["@canon/engine-core: CompiledContextPackage"],
       "verification_gates": ["contract-conformance", "replay-determinism", "vitest"],
       "complexity_tier": "S|M|L",
       "blocked_by": [],
       "estimated_loc": 250,
       "release_tier": "engine-core|context-compiler|model-gateway|tool-gateway|policy|provenance|validation|environment|apps"
     }]
   }
   ```
3. Webhook → `scripts/traycer-to-linear.ts` (CF Worker).

### Phase E — Bounded-Task Dispatch (Linear → Factory / Conductor / Claude Code Action) → ExecutionUnit per task

1. `scripts/traycer-to-linear.ts` ingests `tasks.json` and creates one Linear issue per task via GraphQL `issueCreate`. Custom fields: `traycer_task_id`, `complexity_tier`, `verification_gates`, `release_tier`, `primitive_refs`. Labels: `agent-ready` and `area:*`.
2. Linear webhook on `Issue.updated where state == "Ready"` fires `scripts/linear-router.ts` (CF Worker).
3. Router by `complexity_tier`:
   - **L** → `POST https://api.factory.ai/v1/droids/spawn` with `{droid_type: "code", repo, task_brief, dev_mcp_servers, skills, verification_gates, callback_url}`.
   - **M** → `POST https://conductor.canon.dev/sessions` with `{task_id, branch, model: "claude-opus-4-7", skills, issue_url}`.
   - **S** → `gh workflow run claude-code-task.yml -F issue_id=<id>`.
4. When the agent begins work, it materializes the task as an **`ExecutionUnit`** (primitive 5.1) — `ObjectiveSpec` snapshot + `CompiledContextPackage` snapshot (assembled from Phase A's promoted `AcceptedKnowledgeObject` set + relevant `MemoryObject` entries + active `PolicyObject` entries) + `StrategyGraph` snapshot from Phase C + `AuthorityConstraintSnapshot` + `PolicyConstraintSnapshot`. The `ExecutionUnit` is the unit of consequential work; everything else is a snapshot inside it.
5. All three paths converge: agent opens PR, links to Linear issue (`attachmentLinkURL`), updates issue to `In Review`. PR body includes `Closes <linear-issue>`, `ADR: docs/adr/...`, `Primitives touched: 5.x...`, `Exports.json surface: ...`, `Release tier: ...`, `Verification gates required: ...`.

### Phase F — Agent Execution Inner Loop

Every agent, regardless of execution path, runs the same five startup steps:

1. Search the **`AcceptedKnowledgeObject` + `MemoryObject` corpus** for the task title + cited primitives via the Augment-indexed seed (orchestration-side; runtime-side this would be `EvidenceSet` assembly, but here we're at the dev-tool layer).
2. `augment.semantic_search({query: spec_fragment, scope: "callers"})` and `augment.callers_of(seed_symbols)` across the relevant `packages/*` and the cross-repo surface enumerated by Canon-Ref.
3. `traycer.get_invariants({task_id})` to retrieve any relevant `PolicyObject` constraints.
4. Read `agentic-engine/CONTEXT.md`, the relevant `agentic-engine/docs/spec-digests/*` extract, `agentic-engine/AGENTS.md`, and any nearest descendant `AGENTS.md` in the touched subtree.
5. Post **plan summary** (4–6 bullets, including which `exports.json` surface entries will move) to the Linear issue. Wait 5 minutes for human veto. No veto → proceed.

Then: edit, run local checks (`pnpm typecheck && pnpm test && pnpm --filter @canon/engine-* build` + the relevant cross-repo contract test), commit in small chunks, open PR with the structured body specified in Phase E.

### Phase G — Verification Gates (parallel CI, all blocking)

All gates share one shape (example for contract conformance):

```yaml
name: contract-conformance
on:
  pull_request:
    paths:
      - 'packages/**'
      - 'workers/**'
      - 'contracts/**'
      - 'tests/cross-repo-contracts.test.ts'
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22' }
      - run: pnpm install --frozen-lockfile
      - run: pnpm --filter '@canon/*' build
      - run: pnpm vitest run tests/cross-repo-contracts.test.ts
      - run: pnpm tsx scripts/post-verdict.ts contract-conformance
```

Gates (each one workflow file in `.github/workflows/`):

- **01 vitest** — full unit + integration suite (`pnpm test`).
- **02 typecheck** — `pnpm typecheck` (the lint surface; no ESLint/Biome/Prettier).
- **03 contract-conformance** — `tests/cross-repo-contracts.test.ts` already enforces that every name in `contracts/exports.json` is actually exported by the corresponding `packages/*`. Blocks if surface drifts. **Keystone gate.**
- **04 replay-determinism** — runs `workers/replay-compare/` against a curated `ReplayCursor` set (`ReplayDimension`: provenance, model, context, strategy). Output is `DiffResult`-empty on every dimension or the gate fails. Triggers on PRs touching `packages/provenance/`, `packages/model-gateway/`, `packages/context-compiler/`, `packages/policy/`, `packages/core/` (any primitive shape change), or `workers/run-executor/`.
- **05 spec-drift** — Traycer drift API; blocks if `drift_severity != "none"`. Catches the case where the implementation observable surface no longer matches the accepted Canon control-plane spec.
- **06 zero-dep-guard** — `ast-grep` rule scanning every `packages/*/src/**/*.ts` and `workers/*/src/**/*.ts` for any `import` whose specifier is not `node:*` or a `@canon/*` workspace sibling. Blocks the PR if any new external runtime dep is introduced. **This gate is what makes the zero-dep property mechanically enforced rather than merely documented.**
- **07 gitleaks** — secret scanning.
- **08 codspeed** — perf regression on the curated benchmark set; opens a PR comment if the regression exceeds 5%.
- **09 multi-reviewer** — five Opus 4.7 personas (correctness against `All Prims.md` / perf / security / API stability against `exports.json` / maintainability); Sonnet 4.6 dedupes and ranks. Output is a single PR review.
- **11 packaging** — `tests/build-package-cleanliness.test.ts`, `tests/external-consumer-packaging.test.ts`, `tests/packed-tarball-contents.test.ts` already verify the published tarball shape. Blocks if anything ships that shouldn't or if a `workspace:*` reference leaks into a published manifest.

Required-status-checks on protected `main` make 01–07 and 11 blocking. 08 and 09 are advisory (block only on red, not yellow).

### Phase H — Knowledge Capture on Merge → AcceptedKnowledgeObject + EventObject

`10-knowledge-capture.yml` triggers on `pull_request.closed && merged`:

1. Emit an **`EventObject`** (primitive 5.19) with `engine_event_type: "merge"`, full provenance index (PR URL, commit, primitives touched, exports.json delta, release tier).
2. If the PR closes a Phase B `DecisionEvent` ("did this implementation realize what the ADR proposed?"), emit a corresponding `ValidationRecord` (5.13) closing the loop.
3. Emit a draft **`AcceptedKnowledgeObject`** (5.8) summarizing what was learned — only promoted to accepted status after the next weekly review (do not auto-promote; accepted knowledge is human-owned per `CANON_PROJECT_CONTEXT.md` §5).
4. Augment reindex: `POST /v1/workspaces/<ws>/reindex` with changed paths.
5. Braintrust eval row (`fetch` to ingestion endpoint — no SDK): `agent-quality` dataset entry with `{task_id, agent, gates_passed, revisions, scores: {merge_no_revert, all_gates_first_try}}`.
6. Linear close with retrospective summary.
7. If the PR shifts the public `exports.json` surface of any released layer-product, the artifact registry (`docs/control-plane/artifact-registry.seed.json`) is updated and a draft release note is filed for that tier.

### Phase I — Observability

Every model call in `scripts/*.ts` is wrapped via direct `fetch` to Langfuse OTLP/HTTP JSON ingest:

```ts
// scripts/lib/observe.ts — orchestration-only, NOT runtime
async function observe<T>(name: string, metadata: Record<string, unknown>, fn: () => Promise<T>): Promise<T> {
  const traceId = crypto.randomUUID();
  const start = Date.now();
  try {
    const result = await fn();
    await fetch(`${process.env.LANGFUSE_HOST}/api/public/ingestion`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Basic ${Buffer.from(`${process.env.LANGFUSE_PUBLIC_KEY}:${process.env.LANGFUSE_SECRET_KEY}`).toString("base64")}` },
      body: JSON.stringify({ batch: [{ id: traceId, type: "trace-create", body: { id: traceId, name, metadata, startTime: new Date(start).toISOString(), endTime: new Date().toISOString() } }] }),
    });
    return result;
  } catch (err) {
    // emit error trace via fetch then rethrow
    throw err;
  }
}
```

You only open Langfuse when Braintrust shows a regression. Then bisect: which prompt change, which model version, which orchestration-script change caused the drop in `merge_no_revert`.

If Canon runtime ever needs internal observability, the same pattern applies inside `packages/*` / `workers/*` — direct `fetch` to OTLP/HTTP JSON. **No `@opentelemetry/*` import, ever.**

---

## 8. Daily and weekly cadence

**Daily (≤2 hours human time — the six-week timeline depends on this):**

- **09:00** — Conductor dashboard. Eyeball 5–10 in-flight M-tier sessions; intervene only on red.
- **09:30** — Linear "Needs Human" filter (~3 issues). Approve a plan, resolve a blocker, or punt with a comment.
- **11:00** — Multi-reviewer queue. Read 5–15 PRs with all gates green; act as final-review tiebreaker.
- **14:00** — If an architectural fork is in flight, run `scripts/adr-debate.ts` and read Opus's judgment.
- **16:00** — Promote the day's draft `AcceptedKnowledgeObject` candidates into accepted status (or reject). This is the human-owned step the engine cannot automate.
- **EOD** — Braintrust dashboard. Five seconds: green → close laptop. Yellow → 10-minute Langfuse bisect.

**Weekly:**

- **Monday** — `traycer.list_drift_history --since 7d`. Drift means the spec is wrong (amend the Canon control-plane spec) or agents are systematically misreading something (fix the relevant `claude-skills/*/SKILL.md`, repo `AGENTS.md`, or spec digest — not per-PR).
- **Wednesday** — Review the multi-tier release artifact registry. For each of the seven layer-products + SDK + environment + apps tier: are versions, contract surfaces, and dependency seeds in sync? Any tier whose `exports.json` shifted needs a draft release note.
- **Friday** — Run the `consolidate-memory` skill against the `MemoryObject` / `AcceptedKnowledgeObject` corpus. Consolidate duplicates, prune stale candidates, update the index.

**Monthly:**

- Re-run Phase B debates against the top 3 architectural decisions, conditioned on the past month's data. If any prior judgment no longer dominates, open an RFC.
- Audit the zero-dep guard's exclusion list (should be empty). Audit `pnpm-lock.yaml` line count (should stay near 1.1k absent a major Node typing bump).
- Audit the `exports.json` surface of every layer-product against the published tarball — packaging gate catches drift on PR, but a monthly read sanity-checks decay.

---

## 9. Honest critique that survives all reframes

These concerns remain valid regardless of zero-dep, multi-tier release, the Canon-native tool protocol, or the six-week timeline. **Do not soften them; the owner asked for calibrated observation and committed to the bet anyway. Calibration is its own respect.**

1. **Solo velocity vs funded teams.** Mastra has two founders + YC + DevRel. Vercel AI SDK has Vercel. Anthropic has Anthropic. Microsoft Agent Framework 1.0 (April 2026) has Microsoft. Canon has one person. The gap is 10–50× in nominal throughput. Only differentiation on a sharp axis closes it, not feature-for-feature parity. This workflow is engineered to convert tool-spend into throughput, but it does not abolish the gap.
2. **Ten product surfaces (SDK + 7 engine layers + environment + apps) is coordination-heavy.** Each surface needs docs, versioning, examples, release notes, semver discipline. A breaking change in `@canon/engine-core` ripples through `context-compiler`, `model-gateway`, `tool-gateway`, `policy`, `provenance`, `validation`, every worker, the shared environment, and every app. The replay-determinism gate and contract-conformance gate catch the *mechanical* breakage; humans still own the *semantic* coordination.
3. **Launch surfaces required before SDK public release:** a docs site, a Discord or equivalent, at least one runnable demo (the deterministic-replay-across-primitives demo is the strongest pitch), a 1.0 API surface (not 0.0.0). These are not optional if the SDK is going to be taken seriously by anyone who isn't already watching Canon. The six-week timeline must absorb building these, not assume they're free. *[Aspirational only; not current license posture. DEC-RO-04 (2026-04-24) set current LICENSE to Proprietary / All Rights Reserved; see `canon-knowledgebase/post-reopen-decisions/condition-e-license.md` for revisit conditions.]*
4. **Zero-dep + Canon-native-tool-protocol cost.** SDK adoption will be reduced by the deliberate incompatibility with the existing MCP tool ecosystem. Every integrator faces a choice: import a Canon `ToolAdapter` shim or stay in the MCP ecosystem. This cost is accepted for product-integrity reasons, but it is real and should not be hand-waved as "ours is just better."
5. **Apps are where revenue lives.** Engine and layer polishing past MVP is moat investment, not revenue. Discipline on "engine enough for now → apps next" is the business-critical decision. The temptation to keep polishing primitives because they are pleasing to polish is the single largest schedule risk on the six-week clock.
6. **Calendar-time of market validation is not compressible.** Enterprise procurement cycles, security review for governance-positioning customers, and ecosystem adoption all run on bureaucracy calendar, not developer calendar. Six weeks of build does not equal six weeks of validation; validation starts when the build ends.
7. **Six-week commitment is 2–3 standard deviations above the historical base rate** for solo vertical AI platform builds spanning SDK + 7 layer-products + environment + apps. The owner has accepted this; the workflow is designed to give it the best shot via aggressive parallelism through Factory droids + Conductor + dispatched Sonnet sessions; calibrated observation has to note the base rate anyway.
8. **Positioning remains under-sharpened.** "Governance-first agent engine" reads as enterprise compliance to the developer audience. The sharp pitch should be one of: (a) "the engine for regulated-industry agents" (enterprise buyer) or (b) "the engine with deterministic replay across every primitive" (engineering-rigor audience). Pick one. Microsoft Agent Governance Toolkit (April 2026) just started competing on (a) — that may push the choice toward (b).
9. **Multi-tier release coordination is itself a product surface.** The artifact registry, dependency-graph seeds, Canon-Ref registry, packet protocol, baton protocol, and spec-digest discipline are not optional infrastructure — they are the only thing keeping ten release surfaces from drifting independently. If any of those degrade (stale seeds, packet protocol used inconsistently, spec digests not refreshed), the whole multi-tier story degrades with them.

---

## 10. The keystone: `contracts/exports.json` + `All Prims.md §5`

This pair is the keystone. It is the machine-readable definition of every exported name, mapped to a primitive in `All Prims.md §5`.

- **`contracts/exports.json`** lists every name the repo publishes per `surface` (core, context-compiler, model-gateway, tool-gateway, validation, provenance, policy, plus the four worker surfaces).
- **`All Prims.md §5`** defines the 19 primitives (5.1 ExecutionUnit through 5.19 EventObject) plus the typed error surface (`EngineError`, `CapabilityError`, `InvalidTransitionError`).
- **`tests/cross-repo-contracts.test.ts`** mechanically verifies that every name in `exports.json` is actually exported.
- **Traycer's `tasks.json`** references `primitive_refs` and `exports_json_surface` per task.
- **The multi-reviewer correctness persona** is prompted with the relevant subset of primitives and the relevant slice of `exports.json` per PR.
- **Replay-compare** verifies determinism across primitive boundaries (provenance, model, context, strategy).

If you under-invest here, the rest of the pipeline degrades gracefully but loses its sharp edge. If you maintain it ruthlessly — every primitive a typed export, every typed export contract-tested, every contract-test mechanically gated — every other tool in this document gets ~3× more leverage.

**Build (and maintain) this pair first. Then everything else around it.**

---

## 11. Quick-reference glossary for incoming agents

- **Primitive (5.1–5.19)** — One of the 19 first-class typed objects defined in `All Prims.md §5`. Examples: `ExecutionUnit` (5.1), `CompiledContextPackage` (5.6), `AcceptedKnowledgeObject` (5.8), `StrategyGraph` (5.10), `ToolInvocationRecord` (5.12), `ProofBundle` (5.14), `PolicyObject` (5.18), `EventObject` (5.19).
- **`exports.json` surface** — The bidirectional cross-repo contract surface for a layer-product. Schema: `canon.dev/schemas/repo-exports.v1.json`. Mechanically verified by `tests/cross-repo-contracts.test.ts`.
- **Canon-native tool protocol** — The user-built protocol implemented in `@canon/engine-tool-gateway` that supersedes MCP for tool interop inside Canon runtime. Dev-tooling MCP servers in `.mcp.json` are unrelated and permitted.
- **Zero-dep guard (gate 06)** — `ast-grep` rule that mechanically enforces zero external runtime deps in `packages/*` and `workers/*`. The mechanical complement to the design property.
- **Replay-determinism gate (gate 04)** — `workers/replay-compare/` run across `ReplayDimension`-typed boundaries. Empty `DiffResult` on every dimension or the gate fails.
- **Release tier** — One of: `engine-core`, `context-compiler`, `model-gateway`, `tool-gateway`, `policy`, `provenance`, `validation`, `environment`, `apps`. Each has its own version cadence and `exports.json` surface.
- **Bounded task** — A Linear issue created from a Traycer `tasks.json` entry; materializes as an `ExecutionUnit` (5.1) when picked up. The atomic unit of work an agent can execute end-to-end.
- **Complexity tier** — `S` (single-file, ≤100 LOC, Claude Code Action), `M` (multi-file, ≤500 LOC, Conductor + Opus 4.7), `L` (subsystem, ≥500 LOC, Factory.AI droid).
- **Drift** — When an agent-implemented PR's observable surface differs from the Canon control-plane spec or `exports.json`. Detected by gate 03 (contract) or gate 05 (spec).
- **Gate** — A blocking GitHub Actions workflow whose verdict is required for merge.
- **Plan veto** — The 5-minute human-veto window after an agent posts its plan summary on a Linear issue.
- **Ripple analysis** — Phase C output. A draft `StrategyGraph` (5.10) showing direct, second-order, and third-order effects of a proposed change across all ten release surfaces.
- **Skill** — A reusable agent recipe stored in `claude-skills/<name>/SKILL.md`, loaded by Claude Code on demand. Distinct from a Factory skill in `.factory/skills/`.
- **Spec digest** — A task-scoped extract of a Canon control-plane document, kept in `agentic-engine/docs/spec-digests/`. Agents read these before reaching for upstream Canon artifacts.
- **Canon-Ref registry** — `canon-ref:*` token registry maintained by `scripts/canon-ref.py`. Cross-repo accepted-authority pointer system.

---

## 12. What to do if you (incoming assistant) are asked to deviate

If the user asks you to do something this document or `CANON_PROJECT_CONTEXT.md` forbids — bypass Linear, skip a gate, hand-roll a fifth IPC mechanism, **import any external runtime dependency into `packages/*` or `workers/*`**, **import `@modelcontextprotocol/sdk` anywhere in runtime**, **import any `@opentelemetry/*` package**, **bring back any of the LLVM/formal-methods tools listed in `CANON_PROJECT_CONTEXT.md` §7** — push back once with a one-sentence reference to the relevant section. If they confirm, proceed and emit a draft `EventObject` (5.19) tagged `{engine_event_type: "deviation", reason}` so the deviation is auditable.

If the user asks you to extend this workflow (new meta-tool, new gate, new station), require all four answers before proceeding:

1. Which existing tool is being replaced or which capability gap is being filled?
2. Which of the four protocols (§2) does the new tool speak?
3. Which station owns it?
4. **Is the new tool a runtime dep, an external HTTP service, a CLI, or a meta-tool that operates ON the project?** If it is a runtime dep, the answer is no — full stop. Re-read `CANON_PROJECT_CONTEXT.md` §4 hard constraint #1.

No tool enters the stack without all four answers. The zero-dep property is permanent, and ten release surfaces is already coordination-heavy without unjustified additions.
