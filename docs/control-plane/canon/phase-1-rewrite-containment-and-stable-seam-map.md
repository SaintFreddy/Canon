# Phase 1 rewrite-containment and stable seam map
Version: 1.0
Status: Accepted
Task: P1.5 — Rewrite-containment / stable seam map
Artifact ID: canon.phase1-rewrite-containment-seams.v1
Canon scope: Accepted high-blast-radius seam map for substrate, release bridges, and app projections

## 1. Purpose

This artifact identifies what must stay stable now, what may change later, and what would be expensive or dangerous to rewrite.

It exists to:

- prevent transcript-first shortcuts from entering high-blast-radius seams,
- identify which semantics must stabilize before deeper implementation work,
- distinguish substrate seams from surface-only seams,
- guide later architecture, repo, and release work away from costly rewrites.

This artifact is accepted for downstream use.

## 2. Scope boundaries

### In scope

- high-blast-radius semantic seams,
- medium-blast-radius integration and packaging seams,
- low-blast-radius view and presentation seams,
- bridge-stage seams at Platform Gate, R4, and R7,
- rewrite-containment rules for later work.

### Out of scope

- detailed code-module boundaries,
- runtime process topology,
- repo/package layout,
- test fixture design,
- specific implementation migrations.

## 3. Seam classes

### 3.1 High-blast-radius seams

These are the seams that must stabilize early because rewriting them later would damage continuity, governance, or ontology integrity.

### 3.2 Medium-blast-radius seams

These seams should stay aligned to the canon, but they can evolve with lower cost if the high-blast-radius seams remain stable.

### 3.3 Low-blast-radius seams

These seams are mostly presentation, projection, or packaging choices.
They may change later without threatening product ontology.

## 4. Stable seam map

| Seam ID | Seam | Owner layer | Must stay stable now | May change later | Rewrite risk if violated |
| --- | --- | --- | --- | --- | --- |
| `SS-01` | Source -> Evidence -> Context lineage | Engine + shared environment projection boundary | Source identity, evidence/context distinction, compiled-context inspectability, provenance continuity | Retrieval ranking heuristics, summarization tactics, packing heuristics | High |
| `SS-02` | Run identity and consequential work model | Shared environment | Run as primary consequential primitive, run linkage to proof/delta/writeback, run replay/branchability | UI presentation of runs, run dashboards, phase visualizations | High |
| `SS-03` | Artifact continuity bridge | Shared environment | Artifact as continuity anchor from R4 onward, artifacts linked back to runs/proof/deltas, proposal-based mutation | Artifact workspace layout, browsing affordances, artifact lens presentation | High |
| `SS-04` | Writeback lane separation | Shared environment | Artifact/memory/canon/workflow/export lanes remain distinct and reviewable | UX wording and grouping of writeback controls | High |
| `SS-05` | Commission -> Contract -> Run chain | Shared environment + Task Studio projection | Serious work resolves through explicit commission/contract/run semantics by R7 and Task Studio | Intake form layout, contract editing affordances, preflight visual arrangement | High |
| `SS-06` | Engine-to-environment projection pairs | Engine + shared environment | Execution Unit/Run, Evidence Set/Evidence Pack, Compiled Context/Context Pack, Accepted Knowledge/Canon Object, Variant/Branch, Persistence Proposal/Writeback Proposal pairings | Naming details inside one surface, inspector grouping, visual labels | High |
| `SS-07` | Branch / replay semantics | Engine + shared environment | Branches fork semantic state, checkpoints, and replay inputs; no transcript-clone substitute | Branch map visuals, compare affordances, replay controls | High |
| `SS-08` | Authority / approval / proof boundary | Shared environment | Authority is separate from strategy, proof separate from persuasive prose, approvals explicit and attributable | Surface wording, inspector layout, queue presentation | High |
| `SS-09` | R7 -> Task Studio handoff | Shared environment + Task Studio projection | Task Studio must be a projection change, not an ontology translation | App-level navigation, shell chrome, onboarding flow | High |
| `SS-10` | Platform Gate prelaunch requirement | Release doctrine / technical baseline bridge | No public launch before substrate proves frozen context, source tracing, run identity, and provenance basis | Internal checklist formatting, test harness arrangement | High |
| `SS-11` | Release-stage continuity model | Shared environment + release topology | Thread-assisted continuity early, branch continuity at R3, artifact-centered continuity at R4, commissioning continuity at R7 | Which surface is primary on a given screen | Medium |
| `SS-12` | Reusable execution packaging | Shared environment | Protocol / Workflow / Applet / Trigger stay composed from run semantics rather than inventing a new execution ontology | Settings layout, packaging metadata arrangement, installer flow | Medium |
| `SS-13` | Prompt asset lineage | Chat-domain + shared artifact lineage | Prompt assets stay governed artifacts with lineage and do not replace reusable execution primitives | Prompt card layout, adaptation UI, card metadata presentation | Medium |
| `SS-14` | Surface grammar reuse | Shared environment projection grammar | Shared grammar primitives remain reusable across apps and releases | Exact per-app composition, styling, rail placement, navigation grouping | Medium |
| `SS-15` | View copy / visual arrangement | App/view layers | None of this is ontology-bearing as long as it does not smuggle truth into the view | Labels, panel ordering, charting, iconography, navigation chrome | Low |

## 5. Bridge seams that must not be broken

### 5.1 Platform Gate seam

Before R1, the substrate must already support:

- frozen context snapshots,
- source-region traceability,
- run identity independent of provider transcript state,
- provenance capture.

Breaking this seam creates the transcript-first rewrite trap.

### 5.2 Artifact Workspace seam

R4 must shift visible continuity from transcript gravity to artifact-centered work **without** demoting runs as the primary consequential unit.

Breaking this seam creates silent mutation risk and continuity drift.

### 5.3 Commissioning Bridge seam

R7 must expose explicit commissioning semantics before Task Studio becomes primary.

Breaking this seam would force Task Studio to invent a new ontology instead of inheriting one.

## 6. What may safely change later

The following areas are allowed to evolve with comparatively low risk if the stable seams above are preserved:

- surface naming and arrangement,
- mode presentation,
- shell chrome,
- artifact browsing layout,
- queue/inbox presentation,
- prompt-card visuals,
- applet configuration UI,
- onboarding flows,
- release-by-release polish and emphasis.

## 7. What must not be rewritten casually

The following would be catastrophic or near-catastrophic to rewrite after public hardening begins:

1. run identity and run-to-proof/delta/writeback linkage,
2. evidence/context separation,
3. artifact lineage and proposal/writeback separation,
4. branch/replay semantics,
5. commission/contract/authority/proof semantics,
6. R7 -> Task Studio object continuity,
7. engine-to-environment projection pair boundaries,
8. the fixed release order around Platform Gate, R4, and R7.

## 8. Rewrite-containment rules for later work

1. Put ontology-bearing semantics below view-specific UI logic.
2. Treat transcript-only state as disposable projection state, not as substrate truth.
3. Keep repo/package structure downstream of accepted semantic ownership, never upstream of it.
4. If a proposed change touches a high-blast-radius seam, treat it as canon/architecture work, not routine implementation.
5. Prefer changes to low-blast-radius seams when experimenting with UX.

## 9. Downstream implications

### 9.1 For P1.6 — Golden scenario corpus

- scenarios should explicitly exercise the high-blast-radius seams and bridge seams.

### 9.2 For Phase 3 architecture work

- architecture should stabilize around `SS-01` through `SS-10` before optimizing view-specific concerns.

### 9.3 For Phase 6 repo/package work

- package boundaries should follow these seam classes rather than treating current file placement as architecture proof.

## 10. Review notes

Human review should confirm that this seam map:

- clearly distinguishes high, medium, and low blast radius,
- places high-blast-radius semantics below view-specific logic,
- preserves Platform Gate, R4, and R7 as key bridge seams,
- does not confuse repo shape with architecture ownership.
