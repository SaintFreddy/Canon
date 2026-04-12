#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PACKET_SCHEMA_PATH = REPO_ROOT / "docs/control-plane/core/packet-brief.schema.json"
REGISTRY_PATH = REPO_ROOT / "docs/control-plane/artifact-registry.seed.json"
MANIFEST_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/workspace-manifest-index.json"

RUN_CLASSES = {
    "compare",
    "synthesize",
    "extract",
    "transform",
    "audit",
    "plan",
    "triage",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_header(text: str) -> dict[str, str]:
    header = {}
    for line in text.splitlines():
        if line.startswith("## "):
            break
        if ": " in line:
            key, value = line.split(": ", 1)
            header[key.strip()] = value.strip()
    return header


def extract_packet_brief(text: str) -> dict:
    match = re.search(r"## Packet brief\s+```json\n(.*?)\n```", text, flags=re.DOTALL)
    if not match:
        raise ValueError("missing packet brief JSON block")
    return json.loads(match.group(1))


def extract_section(text: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\n(.*?)(?:\n## |\Z)"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"missing section: {heading}")
    return match.group(1).strip()


def extract_whitelist_paths(text: str) -> list[str]:
    match = re.search(r"## File whitelist[^\n]*\n(.*?)(?:\n## |\Z)", text, flags=re.DOTALL)
    if not match:
        raise ValueError("missing section: File whitelist")
    section = match.group(1).strip()
    paths = []
    for line in section.splitlines():
        line = line.strip()
        match = re.match(r"- `([^`]+)`", line)
        if match:
            paths.append(match.group(1))
    if not paths:
        raise ValueError("missing whitelist paths")
    return paths


def extract_run_class(text: str) -> str:
    match = re.search(r"- Run class: `([^`]+)`", text)
    if not match:
        raise ValueError("missing run class line")
    return match.group(1)


def extract_budget_band(text: str) -> str:
    match = re.search(r"- Selected budget band: `([^`]+)`", text)
    if not match:
        raise ValueError("missing selected budget band line")
    return match.group(1)


def validate_packet(packet_path: Path, repo_root: Path = REPO_ROOT) -> dict:
    schema = load_json(PACKET_SCHEMA_PATH)
    registry = load_json(REGISTRY_PATH)
    manifest_index = load_json(MANIFEST_INDEX_PATH)

    validation_hook_ids = {
        item["hook_id"] for item in registry["validation_hook_standards"]
    }
    registry_ids = {artifact["artifact_id"] for artifact in registry["artifacts"]}

    text = packet_path.read_text(encoding="utf-8")
    header = extract_header(text)
    brief = extract_packet_brief(text)
    whitelist_paths = extract_whitelist_paths(text)
    run_class = extract_run_class(text)
    budget_band = extract_budget_band(text)

    issues: list[str] = []

    required = set(schema["required"])
    allowed = set(schema["properties"])
    missing = sorted(required - set(brief))
    extra = sorted(set(brief) - allowed)
    if missing:
        issues.append(f"missing packet-brief fields: {missing}")
    if extra:
        issues.append(f"unexpected packet-brief fields: {extra}")

    if header.get("Artifact ID") != brief.get("packet_id"):
        issues.append("header artifact id does not match packet_id")
    if header.get("File whitelist ref") != brief.get("file_whitelist_ref"):
        issues.append("header file whitelist ref does not match packet brief")

    packet_id_pattern = re.compile(schema["properties"]["packet_id"]["pattern"])
    task_id_pattern = re.compile(schema["properties"]["task_id"]["pattern"])
    artifact_id_pattern = re.compile(schema["$defs"]["artifactId"]["pattern"])
    hook_id_pattern = re.compile(schema["$defs"]["validationHookRef"]["properties"]["hook_id"]["pattern"])

    if not packet_id_pattern.fullmatch(brief.get("packet_id", "")):
        issues.append("packet_id does not match accepted pattern")
    if not task_id_pattern.fullmatch(brief.get("task_id", "")):
        issues.append("task_id does not match accepted pattern")

    for field in ("source_authority_refs", "accepted_artifact_refs"):
        for ref in brief.get(field, []):
            if not artifact_id_pattern.fullmatch(ref):
                issues.append(f"{field} contains invalid artifact id: {ref}")
            elif ref not in registry_ids:
                issues.append(f"{field} contains unregistered artifact id: {ref}")

    hook_ids = []
    for hook in brief.get("validation_hooks", []):
        hook_id = hook.get("hook_id", "")
        hook_ids.append(hook_id)
        if not hook_id_pattern.fullmatch(hook_id):
            issues.append(f"invalid validation hook id: {hook_id}")
        elif hook_id not in validation_hook_ids:
            issues.append(f"unknown validation hook id: {hook_id}")

    if brief.get("execution_mode") != "factory_first":
        issues.append("execution_mode must be factory_first for pilot execution packets")

    if run_class not in RUN_CLASSES:
        issues.append(f"unknown run class: {run_class}")
    if budget_band not in {"narrow", "standard", "extended"}:
        issues.append(f"unknown budget band: {budget_band}")

    manifest_entries = manifest_index["workspace_manifests"]
    whitelist_roots: list[str] = []
    for whitelist_path in whitelist_paths:
        matched_root = None
        matched_entry = None
        for entry in manifest_entries:
            root_path = entry["root_path"]
            if whitelist_path.startswith(root_path):
                if matched_root is None or len(root_path) > len(matched_root):
                    matched_root = root_path
                    matched_entry = entry
        if matched_root is None or matched_entry is None:
            issues.append(f"whitelist path does not map to accepted root: {whitelist_path}")
            continue
        if matched_root not in whitelist_roots:
            whitelist_roots.append(matched_root)

        if matched_root == "docs/control-plane/":
            relative = whitelist_path[len(matched_root):]
            if "/" in relative:
                child = relative.split("/", 1)[0] + "/"
            else:
                child = relative
            if child not in matched_entry["allowed_children"]:
                issues.append(
                    f"docs/control-plane child is not allowed by manifest index: {whitelist_path}"
                )

    return {
        "packet_path": str(packet_path.relative_to(repo_root)),
        "packet_id": brief.get("packet_id"),
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "validation_hook_ids": hook_ids,
        "whitelist_paths": whitelist_paths,
        "whitelist_roots": whitelist_roots,
        "run_class": run_class,
        "selected_budget_band": budget_band,
        "governing_ref_count": len(brief.get("source_authority_refs", []))
        + len(brief.get("accepted_artifact_refs", [])),
    }


def default_packet_paths() -> list[Path]:
    packet_dir = REPO_ROOT / "docs/control-plane/implementation/packets"
    return sorted(packet_dir.glob("phase-6-pilot-*.md"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("packet_paths", nargs="*", help="packet markdown paths")
    args = parser.parse_args()

    packet_paths = [REPO_ROOT / path for path in args.packet_paths] if args.packet_paths else default_packet_paths()
    reports = [validate_packet(path) for path in packet_paths]
    print(json.dumps({"reports": reports}, indent=2))
    return 0 if all(report["status"] == "pass" for report in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
