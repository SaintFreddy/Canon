#!/usr/bin/env python3
"""
Canon Spec Digest Generator

Reads Canon source-authority and control-plane artifacts and generates
compact, task-scoped spec digest markdown files for each implementation repo.

These digests are Tier 2 context: loaded per-task by implementation agents
to avoid loading the full Canon control plane into every session.

Usage:
    python3 scripts/generate-spec-digests.py

Output:
    docs/spec-digests/{repo-name}/{digest-name}.md

The generator uses explicit source-section mappings rather than
arbitrary semantic extraction. Each digest definition specifies
exactly which source sections to extract and how to assemble them.
"""

import json
import os
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_DIGESTS_DIR = REPO_ROOT / "docs" / "spec-digests"

# ---------------------------------------------------------------------------
# Source file paths
# ---------------------------------------------------------------------------

ALL_PRIMS = REPO_ROOT.parent / "All-Prims-3.md"
CHAT_PLAN = REPO_ROOT.parent / "Chat-Native-Release-Plan-4.md"
TASK_STUDIO = REPO_ROOT.parent / "Task-Studio-North-Star-commissioned-work-app-5.md"
MASTER_PLAN = REPO_ROOT / "docs" / "control-plane" / "core" / "master-plan.md"
LAYER_PACK = REPO_ROOT / "docs" / "control-plane" / "canon" / "phase-1-layer-and-primitive-separation-pack.md"
FORBIDDEN = REPO_ROOT / "docs" / "control-plane" / "core" / "forbidden-shortcuts-register.md"
REPO_CONTRACT = REPO_ROOT / "docs" / "control-plane" / "core" / "repo-agent-operating-contract.md"

# ---------------------------------------------------------------------------
# Extraction helpers
# ---------------------------------------------------------------------------

def read_file(path: Path) -> str:
    """Read a file, returning empty string if it doesn't exist."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def extract_section(content: str, heading_pattern: str, level: int = 2) -> str:
    """
    Extract a markdown section by heading pattern (regex-capable).
    Returns the heading and all content until the next heading of same or higher level.
    """
    prefix = "#" * level
    lines = content.split("\n")
    start = None
    end = None

    for i, line in enumerate(lines):
        if start is None:
            if re.match(rf"^{prefix}\s+{heading_pattern}", line, re.IGNORECASE):
                start = i
        elif re.match(rf"^#{{{1},{level}}}\s", line):
            end = i
            break

    if start is None:
        return ""
    return "\n".join(lines[start:end]).strip()


def extract_range(content: str, start_pattern: str, end_pattern: str, level: int = 3) -> str:
    """
    Extract a range of sections from start_pattern to end_pattern (inclusive).
    """
    prefix = "#" * level
    lines = content.split("\n")
    start = None
    end = None
    past_end_heading = False

    for i, line in enumerate(lines):
        if start is None:
            if re.match(rf"^{prefix}\s+{start_pattern}", line, re.IGNORECASE):
                start = i
        elif not past_end_heading:
            if re.match(rf"^{prefix}\s+{end_pattern}", line, re.IGNORECASE):
                past_end_heading = True
        elif past_end_heading:
            # Stop at next same-level or higher heading
            if re.match(rf"^#{{{1},{level}}}\s", line):
                end = i
                break

    if start is None:
        return ""
    return "\n".join(lines[start:end]).strip()


# ---------------------------------------------------------------------------
# Digest definitions
# ---------------------------------------------------------------------------

@dataclass
class SourceExtract:
    """A single source extraction directive."""
    file: Path
    label: str
    mode: str  # "section", "range", "summary", "lines"
    # For section mode:
    heading: str = ""
    level: int = 2
    # For range mode:
    start_heading: str = ""
    end_heading: str = ""
    # For summary mode:
    summary: str = ""
    # For lines mode:
    start_line: int = 0
    end_line: int = 0


@dataclass
class DigestDef:
    """Definition of a spec digest to generate."""
    repo: str
    name: str
    title: str
    description: str
    sources: list[SourceExtract] = field(default_factory=list)


# All-Prims uses ### for numbered layers.
# Engine layers are 5-34 under "### AGENTIC INFRASTRUCTURE ENGINE — SDK FEATURE SET"
# Shared env sections start at "### SHARED ENVIRONMENT — PRIMITIVE SET"

DIGESTS: list[DigestDef] = [
    # --- agentic-engine digests ---
    DigestDef(
        repo="agentic-engine",
        name="engine-core",
        title="Engine Core Primitives Digest",
        description="Governing spec sections for the engine core: execution units, objects, context system, orchestration, validation, proof, policy, persistence, replay, and provenance.",
        sources=[
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Engine Document Purpose and Architectural Stance",
                mode="range",
                start_heading=r"0\.\s*DOCUMENT PURPOSE",
                end_heading=r"2\.\s*LAYER BOUNDARY",
                level=2,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Engine Core First-Class Objects (Layer 0)",
                mode="section",
                heading=r"5\.\s*CORE FIRST-CLASS OBJECTS",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Engine Orchestration Runtime (Layer 9)",
                mode="section",
                heading=r"14\.\s*LAYER 9",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Engine Validation and Proof (Layers 11-12)",
                mode="range",
                start_heading=r"16\.\s*LAYER 11",
                end_heading=r"17\.\s*LAYER 12",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Engine Policy and Authority (Layer 13)",
                mode="section",
                heading=r"18\.\s*LAYER 13",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — What Does Not Belong in the Engine",
                mode="section",
                heading=r"31\.\s*WHAT DOES NOT BELONG",
                level=3,
            ),
        ],
    ),
    DigestDef(
        repo="agentic-engine",
        name="engine-compiler",
        title="Engine Context Compiler Digest",
        description="Governing spec sections for context compilation: source ingestion, compiled context system, memory, and accepted knowledge.",
        sources=[
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Source Ingestion and Retrieval (Layer 4)",
                mode="section",
                heading=r"9\.\s*LAYER 4",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Compiled Context System (Layer 5)",
                mode="section",
                heading=r"10\.\s*LAYER 5",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Memory System (Layer 6)",
                mode="section",
                heading=r"11\.\s*LAYER 6",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Accepted Knowledge (Layer 7)",
                mode="section",
                heading=r"12\.\s*LAYER 7",
                level=3,
            ),
        ],
    ),
    DigestDef(
        repo="agentic-engine",
        name="engine-gateway",
        title="Engine Model and Tool Gateway Digest",
        description="Governing spec sections for model and tool gateways: model abstraction, tool framework, provider adapters.",
        sources=[
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Model and Inference Abstraction (Layer 2)",
                mode="section",
                heading=r"7\.\s*LAYER 2",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Tool and Adapter Framework (Layer 3)",
                mode="section",
                heading=r"8\.\s*LAYER 3",
                level=3,
            ),
        ],
    ),

    # --- shared-environment digests ---
    DigestDef(
        repo="shared-environment",
        name="env-shared-objects",
        title="Shared Object Schemas Digest",
        description="Governing spec sections for shared environment objects: topology, identity, delegation, grounding, reuse, collaboration, and projection grammar.",
        sources=[
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Shared Environment Purpose and Design Requirements",
                mode="range",
                start_heading=r"SHARED ENVIRONMENT",
                end_heading=r"5\.\s*PRIMITIVE FAMILIES",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Topology and Scope Primitives",
                mode="section",
                heading=r"6\.\s*A\.\s*TOPOLOGY",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Identity and Participation Primitives",
                mode="section",
                heading=r"7\.\s*B\.\s*IDENTITY",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Delegation and Execution Primitives",
                mode="section",
                heading=r"8\.\s*C\.\s*DELEGATION",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Grounding and Durable Knowledge Primitives",
                mode="section",
                heading=r"9\.\s*D\.\s*GROUNDING",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Canonical Environment Primitive Set",
                mode="section",
                heading=r"13\.\s*THE CANONICAL",
                level=3,
            ),
        ],
    ),
    DigestDef(
        repo="shared-environment",
        name="env-control",
        title="Environment Control Digest",
        description="Governing spec sections for environment control, reuse/composition, collaboration/governance, and projection grammar.",
        sources=[
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Reuse and Composition Primitives",
                mode="section",
                heading=r"10\.\s*E\.\s*REUSE",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Collaboration and Governance Primitives",
                mode="section",
                heading=r"11\.\s*F\.\s*COLLABORATION",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Projection Grammar Primitives",
                mode="section",
                heading=r"12\.\s*G\.\s*PROJECTION",
                level=3,
            ),
        ],
    ),
    DigestDef(
        repo="shared-environment",
        name="env-governance",
        title="Environment Governance and Review Digest",
        description="Governing spec sections for what belongs/doesn't belong in the environment, plus the forbidden shortcuts register.",
        sources=[
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — What Does Not Belong in the Environment",
                mode="section",
                heading=r"15\.\s*WHAT DOES NOT BELONG",
                level=3,
            ),
            SourceExtract(
                file=ALL_PRIMS,
                label="All-Prims — Relationship to the Engine",
                mode="section",
                heading=r"14\.\s*RELATIONSHIP TO THE ENGINE",
                level=3,
            ),
            SourceExtract(
                file=FORBIDDEN,
                label="Forbidden Shortcuts Register — Full Shortcut List",
                mode="section",
                heading=r"7\.\s*Shortcut register",
                level=2,
            ),
        ],
    ),

    # --- canon-apps digests ---
    DigestDef(
        repo="canon-apps",
        name="app-r1-conversation",
        title="R1 Transcript Chat Digest",
        description="Governing spec sections for R1 Transcript Chat: platform gate, product promise, required primitives, exit criteria.",
        sources=[
            SourceExtract(
                file=CHAT_PLAN,
                label="Chat-Native Release Plan — Shared Across All Releases",
                mode="section",
                heading=r"2\.\s*What is shared",
                level=2,
            ),
            SourceExtract(
                file=CHAT_PLAN,
                label="Chat-Native Release Plan — Platform Gate",
                mode="section",
                heading=r"4\.\s*Mandatory internal platform gate",
                level=2,
            ),
            SourceExtract(
                file=CHAT_PLAN,
                label="Chat-Native Release Plan — R1 Transcript Chat",
                mode="section",
                heading=r"5\.\s*Release 1",
                level=2,
            ),
            SourceExtract(
                file=CHAT_PLAN,
                label="Chat-Native Release Plan — View-Specific Primitives",
                mode="section",
                heading=r"3\.\s*What is unique",
                level=2,
            ),
        ],
    ),
]


# ---------------------------------------------------------------------------
# Generator
# ---------------------------------------------------------------------------

def apply_extract(src: SourceExtract) -> str:
    """Apply an extraction directive and return the result."""
    if src.mode == "summary":
        return src.summary

    content = read_file(src.file)
    if not content:
        return f"*Source file not found: {src.file}*"

    if src.mode == "section":
        result = extract_section(content, src.heading, src.level)
        return result if result else f"*Section matching '{src.heading}' not found.*"

    if src.mode == "range":
        result = extract_range(content, src.start_heading, src.end_heading, src.level)
        return result if result else f"*Range '{src.start_heading}' to '{src.end_heading}' not found.*"

    return "*Unknown extraction mode.*"


def generate_digest(d: DigestDef) -> str:
    """Generate a spec digest markdown document from a digest definition."""
    lines = [
        f"# {d.title}",
        "",
        f"> Auto-generated by `scripts/generate-spec-digests.py`",
        f"> Target repo: `{d.repo}`",
        "",
        f"## Purpose",
        "",
        d.description,
        "",
    ]

    for src in d.sources:
        lines.append("---")
        lines.append("")
        lines.append(f"## Source: {src.label}")
        lines.append("")
        lines.append(apply_extract(src))
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"*End of digest for `{d.repo}/{d.name}`*")
    return "\n".join(lines)


def main():
    """Generate all defined spec digests."""
    print("Canon Spec Digest Generator")
    print(f"Output directory: {SPEC_DIGESTS_DIR}")
    print(f"Generating {len(DIGESTS)} digests...")
    print()

    generated = []

    for d in DIGESTS:
        out_dir = SPEC_DIGESTS_DIR / d.repo
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{d.name}.md"

        content = generate_digest(d)
        out_path.write_text(content, encoding="utf-8")

        size_kb = len(content.encode("utf-8")) / 1024
        print(f"  [{d.repo}] {d.name}.md — {size_kb:.1f} KB")
        generated.append(str(out_path.relative_to(REPO_ROOT)))

    print()
    print(f"Generated {len(generated)} digest files:")
    for g in generated:
        print(f"  {g}")


if __name__ == "__main__":
    main()
