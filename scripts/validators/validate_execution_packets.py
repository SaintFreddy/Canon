#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PACKET_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/phase-6-execution-packet-index.json"
BLUEPRINT_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/phase-6-release-blueprint-index.json"
CONTEXT_RULES_PATH = REPO_ROOT / "docs/control-plane/core/agent-packet-context-pack-rules.json"
VALIDATOR_PATH = REPO_ROOT / "scripts/validators/validate_pilot_packets.py"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_packet_validator():
    spec = importlib.util.spec_from_file_location("validate_pilot_packets", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load packet validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_packet_entry(entry: dict, family_catalog: dict, blueprint_map: dict, budget_bands: dict, packet_map: dict, validator_module) -> dict:
    issues: list[str] = []
    path = REPO_ROOT / entry["packet_path"]
    if not path.exists():
        issues.append("packet file missing")
        return {"packet_artifact_id": entry["packet_artifact_id"], "packet_path": entry["packet_path"], "status": "fail", "issues": issues}

    report = validator_module.validate_packet(path, REPO_ROOT)
    issues.extend(report["issues"])

    if report["packet_id"] != entry["packet_artifact_id"]:
        issues.append("packet id does not match packet index entry")
    if report["run_class"] != entry["run_class"]:
        issues.append("run class does not match packet index entry")
    if report["selected_budget_band"] != entry["selected_budget_band"]:
        issues.append("selected budget band does not match packet index entry")
    if set(report["validation_hook_ids"]) != set(entry["validation_hooks"]):
        issues.append("validation hook set does not match packet index entry")
    if report["whitelist_paths"] != entry["file_whitelist_paths"]:
        issues.append("whitelist paths do not match packet index entry")
    if set(report["whitelist_roots"]) != set(entry["touched_workspace_roots"]):
        issues.append("touched roots do not match packet index entry")

    blueprint = blueprint_map[entry["blueprint_ref"]]
    if not set(entry["file_whitelist_paths"]).issubset(set(blueprint["module_clusters"])):
        issues.append("packet whitelist is not a subset of the governing blueprint module clusters")
    if entry["required_fixture_families"] != blueprint["required_fixture_families"]:
        issues.append("packet fixture families do not match governing blueprint fixture families")

    family = family_catalog[entry["packet_family"]]
    for whitelist_path in entry["file_whitelist_paths"]:
        if not any(whitelist_path.startswith(prefix) for prefix in family["allowed_prefixes"]):
            issues.append(f"whitelist path violates packet-family allowed prefixes: {whitelist_path}")

    band_limit = budget_bands[entry["selected_budget_band"]]["governing_ref_limit"]
    if report["governing_ref_count"] > band_limit:
        issues.append("governing ref count exceeds selected budget band")

    for prerequisite in entry["prerequisite_packet_refs"]:
        if prerequisite not in packet_map:
            issues.append(f"missing prerequisite packet ref: {prerequisite}")
            continue
        prereq_entry = packet_map[prerequisite]
        if prereq_entry["release_slug"] != entry["release_slug"]:
            issues.append("prerequisite packet crosses release boundary")
        if prereq_entry["packet_order"] >= entry["packet_order"]:
            issues.append("prerequisite packet order is not earlier than the dependent packet")

    if entry["packet_family"] == "task_studio_handoff":
        for whitelist_path in entry["file_whitelist_paths"]:
            if not whitelist_path.startswith("apps/task-studio/"):
                issues.append("task_studio_handoff packet may only target apps/task-studio/ paths")

    return {
        "packet_artifact_id": entry["packet_artifact_id"],
        "packet_path": entry["packet_path"],
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "packet_family": entry["packet_family"],
        "whitelist_path_count": len(entry["file_whitelist_paths"]),
        "fixture_families": entry["required_fixture_families"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    del args

    packet_index = load_json(PACKET_INDEX_PATH)
    blueprint_index = load_json(BLUEPRINT_INDEX_PATH)
    context_rules = load_json(CONTEXT_RULES_PATH)
    validator_module = load_packet_validator()

    family_catalog = {entry["packet_family"]: entry for entry in packet_index["packet_family_catalog"]}
    blueprint_map = {entry["blueprint_artifact_id"]: entry for entry in blueprint_index["release_blueprints"]}
    packet_map = {entry["packet_artifact_id"]: entry for entry in packet_index["execution_packets"]}

    reports = []
    for entry in packet_index["execution_packets"]:
        reports.append(validate_packet_entry(entry, family_catalog, blueprint_map, context_rules["budget_bands"], packet_map, validator_module))

    expected_defaults = packet_index["release_packet_defaults"]
    release_groups = {}
    for entry in packet_index["execution_packets"]:
        release_groups.setdefault(entry["release_slug"], []).append(entry)
    for release_slug, entries in release_groups.items():
        ordered = [entry["packet_family"] for entry in sorted(entries, key=lambda item: item["packet_order"])]
        expected = expected_defaults.get(release_slug, expected_defaults["default"])
        if ordered != expected:
            raise SystemExit(f"packet family coverage mismatch for {release_slug}: {ordered} != {expected}")

    print(json.dumps({"reports": reports}, indent=2))
    return 0 if all(report["status"] == "pass" for report in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
