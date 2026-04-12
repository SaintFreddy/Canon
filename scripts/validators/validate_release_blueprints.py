#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BLUEPRINT_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/phase-6-release-blueprint-index.json"
REGISTRY_PATH = REPO_ROOT / "docs/control-plane/artifact-registry.seed.json"
MANIFEST_PATH = REPO_ROOT / "docs/control-plane/core/workspace-manifest-index.json"
CURRENT_STATE_PATH = REPO_ROOT / "docs/control-plane/core/codebase-current-state.json"
FIXTURE_RULES_PATH = REPO_ROOT / "tests/fixtures/fixture-rules.json"

REQUIRED_HEADINGS = [
    "## 1. Purpose",
    "## 2. Scope boundaries",
    "## 3. Governing baseline",
    "## 4. Implementation blueprint",
    "### 4.1 Workspace roots and module clusters",
    "### 4.2 Shared schemas, contracts, and object seams",
    "### 4.3 APIs, events, and execution seams",
    "### 4.4 Storage, provenance, and migration posture",
    "### 4.5 UI states and surface projections",
    "### 4.6 Tests, fixtures, and validators",
    "### 4.7 Explicit exclusions and deferred work",
    "## 5. Acceptance notes",
]

ALLOWED_CLUSTER_PREFIXES = [
    "apps/chat-native/",
    "apps/task-studio/",
    "packages/projection-grammar/",
    "packages/shared-object-schemas/",
    "packages/shared-object-api/",
    "packages/environment-control-contracts/",
    "packages/context-compiler-contracts/",
    "packages/event-provenance-contracts/",
    "packages/review-writeback-contracts/",
    "packages/replay-compare-contracts/",
    "packages/model-gateway-contracts/",
    "packages/tool-gateway-contracts/",
    "packages/monitor-inspect/",
    "services/environment-shell-api/",
    "services/execution-control/",
    "services/review-writeback/",
    "services/event-provenance/",
    "services/model-gateway/",
    "services/tool-gateway/",
    "workers/context-compiler/",
    "workers/replay-compare/",
    "workers/apply-writeback/",
    "workers/tool-sandbox/",
    "tests/contracts/",
    "tests/fixtures/",
]


def load_json(path: Path):
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


def infer_root(path: str, manifest_entries: list[dict]) -> str | None:
    match = None
    for entry in manifest_entries:
        root = entry["root_path"]
        if path.startswith(root):
            if match is None or len(root) > len(match):
                match = root
    return match


def validate_blueprint(entry: dict, registry_ids: set[str], validation_hook_ids: set[str], manifest_entries: list[dict], current_state_roots: set[str], known_fixture_families: set[str]) -> dict:
    issues: list[str] = []
    path = REPO_ROOT / entry["blueprint_path"]
    if not path.exists():
        issues.append("blueprint file missing")
        return {
            "blueprint_path": entry["blueprint_path"],
            "blueprint_artifact_id": entry["blueprint_artifact_id"],
            "status": "fail",
            "issues": issues,
        }

    text = path.read_text(encoding="utf-8")
    header = extract_header(text)
    if header.get("Artifact ID") != entry["blueprint_artifact_id"]:
        issues.append("header artifact id does not match index entry")
    if header.get("Release ref") != entry["release_ref"]:
        issues.append("header release ref does not match index entry")
    if header.get("Implementation scope") != entry["implementation_scope"]:
        issues.append("header implementation scope does not match index entry")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            issues.append(f"missing heading: {heading}")

    if entry["release_ref"] not in registry_ids:
        issues.append("release ref not registered")

    for ref in entry["governing_artifact_refs"]:
        if ref not in registry_ids:
            issues.append(f"governing artifact ref not registered: {ref}")
        if ref not in text:
            issues.append(f"governing artifact ref not cited in blueprint text: {ref}")

    derived_roots: set[str] = set()
    for cluster in entry["module_clusters"]:
        if not any(cluster.startswith(prefix) for prefix in ALLOWED_CLUSTER_PREFIXES):
            issues.append(f"module cluster outside accepted prefixes: {cluster}")
        root = infer_root(cluster, manifest_entries)
        if root is None:
            issues.append(f"module cluster does not map to accepted workspace root: {cluster}")
        else:
            derived_roots.add(root)
            if root not in current_state_roots:
                issues.append(f"mapped root missing from current-state dataset: {root}")
        if cluster not in text:
            issues.append(f"module cluster not cited in blueprint text: {cluster}")

    if derived_roots != set(entry["touched_workspace_roots"]):
        issues.append("touched workspace roots do not match module-cluster-derived roots")

    for fixture_family in entry["required_fixture_families"]:
        if fixture_family not in known_fixture_families:
            issues.append(f"unknown fixture family: {fixture_family}")
        if fixture_family not in text:
            issues.append(f"fixture family not cited in blueprint text: {fixture_family}")

    for hook_id in entry["validation_hooks"]:
        if hook_id not in validation_hook_ids:
            issues.append(f"unknown validation hook id: {hook_id}")
        if hook_id not in text:
            issues.append(f"validation hook not cited in blueprint text: {hook_id}")

    return {
        "blueprint_path": entry["blueprint_path"],
        "blueprint_artifact_id": entry["blueprint_artifact_id"],
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "touched_workspace_roots": entry["touched_workspace_roots"],
        "module_cluster_count": len(entry["module_clusters"]),
        "fixture_families": entry["required_fixture_families"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    del args

    index = load_json(BLUEPRINT_INDEX_PATH)
    registry = load_json(REGISTRY_PATH)
    manifest_index = load_json(MANIFEST_PATH)
    current_state = load_json(CURRENT_STATE_PATH)
    fixture_rules = load_json(FIXTURE_RULES_PATH)

    registry_ids = {artifact["artifact_id"] for artifact in registry["artifacts"]}
    validation_hook_ids = {hook["hook_id"] for hook in registry["validation_hook_standards"]}
    manifest_entries = manifest_index["workspace_manifests"]
    current_state_roots = {entry["root_path"] for entry in current_state["workspace_states"]}
    known_fixture_families = {entry["fixture_family"] for entry in fixture_rules["fixture_families"]}

    seen_ids = set()
    seen_paths = set()
    reports = []
    for entry in index["release_blueprints"]:
        if entry["blueprint_artifact_id"] in seen_ids:
            raise SystemExit(f"duplicate blueprint artifact id: {entry['blueprint_artifact_id']}")
        if entry["blueprint_path"] in seen_paths:
            raise SystemExit(f"duplicate blueprint path: {entry['blueprint_path']}")
        seen_ids.add(entry["blueprint_artifact_id"])
        seen_paths.add(entry["blueprint_path"])
        reports.append(validate_blueprint(entry, registry_ids, validation_hook_ids, manifest_entries, current_state_roots, known_fixture_families))

    print(json.dumps({"reports": reports}, indent=2))
    return 0 if all(report["status"] == "pass" for report in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
