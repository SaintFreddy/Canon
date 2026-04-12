#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "docs/control-plane/artifact-registry.seed.json"
GRAPH_PATH = REPO_ROOT / "docs/control-plane/dependency-graph.seed.json"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    registry = load_json(REGISTRY_PATH)
    graph = load_json(GRAPH_PATH)

    issues: list[str] = []

    artifact_status_values = set(registry["artifact_status_values"])
    validation_hook_ids = {
        hook["hook_id"] for hook in registry["validation_hook_standards"]
    }
    stale_rule_ids = {
        rule["stale_rule_id"] for rule in registry["stale_rule_catalog"]
    }
    edge_type_values = {entry["edge_type"] for entry in graph["edge_type_catalog"]}
    propagation_mode_values = {"auto", "manual", "revalidate", "none"}
    dependency_ref_required_fields = set(
        registry["shape_catalog"]["dependency_ref.v1"]["required_fields"]
    )

    registry_by_id: dict[str, dict] = {}
    canonical_locators: dict[str, str] = {}
    for artifact in registry["artifacts"]:
        artifact_id = artifact["artifact_id"]
        if artifact_id in registry_by_id:
            issues.append(f"duplicate registry artifact id: {artifact_id}")
            continue
        registry_by_id[artifact_id] = artifact

        canonical_locator = artifact["canonical_locator"]
        if canonical_locator in canonical_locators:
            issues.append(
                "duplicate canonical locator: "
                f"{canonical_locator} ({artifact_id}, {canonical_locators[canonical_locator]})"
            )
        else:
            canonical_locators[canonical_locator] = artifact_id

        if artifact["artifact_status"] not in artifact_status_values:
            issues.append(
                f"invalid artifact status for {artifact_id}: {artifact['artifact_status']}"
            )
        if artifact["stale_rule_id"] not in stale_rule_ids:
            issues.append(f"unknown stale rule for {artifact_id}: {artifact['stale_rule_id']}")

        for hook in artifact.get("validation_hooks", []):
            hook_id = hook.get("hook_id")
            if hook_id not in validation_hook_ids:
                issues.append(f"unknown validation hook for {artifact_id}: {hook_id}")

    graph_nodes_by_id: dict[str, dict] = {}
    for node in graph["nodes"]:
        artifact_id = node["artifact_id"]
        if artifact_id in graph_nodes_by_id:
            issues.append(f"duplicate graph node artifact id: {artifact_id}")
            continue
        graph_nodes_by_id[artifact_id] = node
        registry_artifact = registry_by_id.get(artifact_id)
        if registry_artifact is None:
            issues.append(f"graph node missing registry artifact: {artifact_id}")
            continue
        for field in ("artifact_type_id", "artifact_status", "canonical_locator"):
            if node[field] != registry_artifact[field]:
                issues.append(
                    f"graph node {artifact_id} field mismatch for {field}: "
                    f"{node[field]!r} != {registry_artifact[field]!r}"
                )

    missing_graph_nodes = sorted(set(registry_by_id) - set(graph_nodes_by_id))
    if missing_graph_nodes:
        issues.append(f"registry artifacts missing graph nodes: {missing_graph_nodes}")

    graph_edge_index: set[tuple[str, str, str, str]] = set()
    seen_edge_ids: set[str] = set()
    for edge in graph["edges"]:
        edge_id = edge["edge_id"]
        if edge_id in seen_edge_ids:
            issues.append(f"duplicate edge id: {edge_id}")
        seen_edge_ids.add(edge_id)

        if edge["from_artifact_id"] not in registry_by_id:
            issues.append(
                f"graph edge {edge_id} references unknown from_artifact_id: "
                f"{edge['from_artifact_id']}"
            )
        if edge["to_artifact_id"] not in registry_by_id:
            issues.append(
                f"graph edge {edge_id} references unknown to_artifact_id: "
                f"{edge['to_artifact_id']}"
            )
        if edge["edge_type"] not in edge_type_values:
            issues.append(f"graph edge {edge_id} has unknown edge_type: {edge['edge_type']}")
        if edge["propagation_mode"] not in propagation_mode_values:
            issues.append(
                f"graph edge {edge_id} has unknown propagation_mode: "
                f"{edge['propagation_mode']}"
            )

        graph_edge_index.add(
            (
                edge["from_artifact_id"],
                edge["to_artifact_id"],
                edge["edge_type"],
                edge["propagation_mode"],
            )
        )

    for artifact in registry["artifacts"]:
        artifact_id = artifact["artifact_id"]

        for ref in artifact.get("source_authority_refs", []):
            if ref not in registry_by_id:
                issues.append(
                    f"unknown source_authority_ref on {artifact_id}: {ref}"
                )

        for dependency_ref in artifact.get("dependency_refs", []):
            missing_fields = dependency_ref_required_fields - set(dependency_ref)
            if missing_fields:
                issues.append(
                    f"dependency ref on {artifact_id} missing fields: "
                    f"{sorted(missing_fields)}"
                )

            upstream_id = dependency_ref.get("artifact_id")
            edge_type = dependency_ref.get("edge_type")
            propagation_mode = dependency_ref.get("propagation_mode")

            if upstream_id not in registry_by_id:
                issues.append(
                    f"dependency ref on {artifact_id} points to unknown artifact: "
                    f"{upstream_id}"
                )
                continue
            if edge_type not in edge_type_values:
                issues.append(
                    f"dependency ref on {artifact_id} has unknown edge_type: {edge_type}"
                )
            if propagation_mode not in propagation_mode_values:
                issues.append(
                    "dependency ref on "
                    f"{artifact_id} has unknown propagation_mode: {propagation_mode}"
                )

            graph_key = (artifact_id, upstream_id, edge_type, propagation_mode)
            if graph_key not in graph_edge_index:
                issues.append(
                    "dependency ref missing graph edge: "
                    f"{artifact_id} -> {upstream_id} ({edge_type}, {propagation_mode})"
                )

    result = {
        "registry_artifact_count": len(registry["artifacts"]),
        "graph_node_count": len(graph["nodes"]),
        "graph_edge_count": len(graph["edges"]),
        "status": "pass" if not issues else "fail",
        "issues": issues,
    }
    print(json.dumps(result, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    sys.exit(main())
