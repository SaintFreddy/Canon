#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "docs/control-plane/artifact-registry.seed.json"
GRAPH_PATH = REPO_ROOT / "docs/control-plane/dependency-graph.seed.json"
DEFAULT_RULES_PATH = (
    REPO_ROOT / "docs/control-plane/core/phase-7-stale-regeneration-rules.json"
)

ACTION_PRIORITY = {
    "ignore": 0,
    "manual_review": 1,
    "revalidate": 2,
    "mark_stale": 3,
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def excerpt(text: str, limit: int = 8) -> list[str]:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if len(lines) <= limit:
        return lines
    return lines[-limit:]


def resolve_commands(
    artifact_id: str,
    artifact_type_id: str,
    override_map: dict[str, dict],
    type_rule_map: dict[str, dict],
) -> tuple[list[str], str]:
    if artifact_id in override_map:
        return override_map[artifact_id]["regeneration_commands"], "artifact_override"
    if artifact_type_id in type_rule_map:
        return type_rule_map[artifact_type_id]["regeneration_commands"], "artifact_type_rule"
    return [], "none"


def build_impact_report(
    rules_path: Path,
    changed_artifact_refs: list[str],
    apply_registry: bool = False,
    run_regeneration: bool = False,
) -> dict:
    rules = load_json(rules_path)
    registry = load_json(REGISTRY_PATH)
    graph = load_json(GRAPH_PATH)

    registry_by_id = {artifact["artifact_id"]: artifact for artifact in registry["artifacts"]}
    graph_nodes_by_id = {node["artifact_id"]: node for node in graph["nodes"]}
    override_map = {
        entry["artifact_ref"]: entry for entry in rules["artifact_overrides"]
    }
    type_rule_map = {
        entry["artifact_type_id"]: entry for entry in rules["artifact_type_rules"]
    }
    action_by_mode = {
        entry["propagation_mode"]: entry["action"]
        for entry in rules["propagation_action_map"]
    }

    missing_changed = [ref for ref in changed_artifact_refs if ref not in registry_by_id]
    if missing_changed:
        raise ValueError(f"unknown changed artifact refs: {missing_changed}")

    reverse_edges: dict[str, list[dict]] = {}
    for edge in graph["edges"]:
        reverse_edges.setdefault(edge["to_artifact_id"], []).append(edge)

    impacted: dict[str, dict] = {}
    queue = list(changed_artifact_refs)
    visited = set(changed_artifact_refs)

    while queue:
        upstream_id = queue.pop(0)
        for edge in reverse_edges.get(upstream_id, []):
            downstream_id = edge["from_artifact_id"]
            if downstream_id in changed_artifact_refs:
                continue

            action = action_by_mode.get(edge["propagation_mode"], "ignore")
            if action == "ignore":
                continue

            artifact = registry_by_id[downstream_id]
            commands, rule_source = resolve_commands(
                downstream_id,
                artifact["artifact_type_id"],
                override_map,
                type_rule_map,
            )

            record = impacted.setdefault(
                downstream_id,
                {
                    "artifact_id": downstream_id,
                    "artifact_type_id": artifact["artifact_type_id"],
                    "current_status": artifact["artifact_status"],
                    "recommended_action": action,
                    "triggering_artifact_refs": [],
                    "triggering_edge_ids": [],
                    "propagation_modes": [],
                    "regeneration_commands": [],
                    "rule_sources": [],
                },
            )

            if ACTION_PRIORITY[action] > ACTION_PRIORITY[record["recommended_action"]]:
                record["recommended_action"] = action

            if upstream_id not in record["triggering_artifact_refs"]:
                record["triggering_artifact_refs"].append(upstream_id)
            if edge["edge_id"] not in record["triggering_edge_ids"]:
                record["triggering_edge_ids"].append(edge["edge_id"])
            if edge["propagation_mode"] not in record["propagation_modes"]:
                record["propagation_modes"].append(edge["propagation_mode"])
            for command in commands:
                if command not in record["regeneration_commands"]:
                    record["regeneration_commands"].append(command)
            if rule_source not in record["rule_sources"]:
                record["rule_sources"].append(rule_source)

            if downstream_id not in visited:
                visited.add(downstream_id)
                queue.append(downstream_id)

    stale_marker_updates: list[str] = []
    if apply_registry:
        for artifact_id, record in impacted.items():
            if record["recommended_action"] != "mark_stale":
                continue
            registry_artifact = registry_by_id[artifact_id]
            graph_node = graph_nodes_by_id[artifact_id]
            if registry_artifact["artifact_status"] == "accepted":
                registry_artifact["artifact_status"] = "stale"
                graph_node["artifact_status"] = "stale"
                stale_marker_updates.append(artifact_id)

        if stale_marker_updates:
            REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
            GRAPH_PATH.write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")

    regeneration_results = []
    regeneration_failed = False
    if run_regeneration:
        seen_commands: list[str] = []
        for record in impacted.values():
            for command in record["regeneration_commands"]:
                if command not in seen_commands:
                    seen_commands.append(command)

        for command in seen_commands:
            completed = subprocess.run(
                shlex.split(command),
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            if completed.returncode != 0:
                regeneration_failed = True
            regeneration_results.append(
                {
                    "command": command,
                    "returncode": completed.returncode,
                    "stdout_excerpt": excerpt(completed.stdout),
                    "stderr_excerpt": excerpt(completed.stderr),
                }
            )

    impacted_reports = sorted(impacted.values(), key=lambda item: item["artifact_id"])

    return {
        "stale_detection_report_meta": {
            "schema_version": "1.0.0",
            "title": "Phase 7 stale detection report",
            "task_id": "P7.3",
            "generated_on": date.today().isoformat(),
            "rules_ref": "cp.phase7-stale-regeneration-rules-data.v1",
            "changed_artifact_refs": changed_artifact_refs,
            "applied_registry_updates": apply_registry,
            "ran_regeneration": run_regeneration,
        },
        "impacted_artifacts": impacted_reports,
        "stale_marker_updates": stale_marker_updates,
        "regeneration_results": regeneration_results,
        "summary": {
            "impacted_artifact_count": len(impacted_reports),
            "mark_stale_count": sum(
                1
                for item in impacted_reports
                if item["recommended_action"] == "mark_stale"
            ),
            "manual_review_count": sum(
                1
                for item in impacted_reports
                if item["recommended_action"] == "manual_review"
            ),
            "revalidate_count": sum(
                1
                for item in impacted_reports
                if item["recommended_action"] == "revalidate"
            ),
            "regeneration_failed": regeneration_failed,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rules",
        default=str(DEFAULT_RULES_PATH),
        help="stale regeneration rules path",
    )
    parser.add_argument(
        "--changed-artifact",
        action="append",
        required=True,
        dest="changed_artifacts",
        help="accepted artifact ref that changed upstream",
    )
    parser.add_argument("--apply-registry", action="store_true")
    parser.add_argument("--run-regeneration", action="store_true")
    parser.add_argument("--write", help="optional output path")
    args = parser.parse_args()

    rules_path = (
        Path(args.rules)
        if Path(args.rules).is_absolute()
        else REPO_ROOT / args.rules
    )

    results = build_impact_report(
        rules_path,
        args.changed_artifacts,
        apply_registry=args.apply_registry,
        run_regeneration=args.run_regeneration,
    )

    if args.write:
        write_path = (
            Path(args.write)
            if Path(args.write).is_absolute()
            else REPO_ROOT / args.write
        )
        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(results, indent=2))
    return 0 if not results["summary"]["regeneration_failed"] else 1


if __name__ == "__main__":
    sys.exit(main())
