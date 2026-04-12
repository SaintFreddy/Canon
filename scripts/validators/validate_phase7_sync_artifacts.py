#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SYNC_DIR = REPO_ROOT / "docs/control-plane/sync"
REGISTRY_PATH = REPO_ROOT / "docs/control-plane/artifact-registry.seed.json"
MANIFEST_PATH = REPO_ROOT / "docs/control-plane/core/workspace-manifest-index.json"
CURRENT_STATE_PATH = REPO_ROOT / "docs/control-plane/core/codebase-current-state.json"
BLUEPRINT_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/phase-6-release-blueprint-index.json"
PACKET_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/phase-6-execution-packet-index.json"
DELTA_INDEX_PATH = REPO_ROOT / "docs/control-plane/core/phase-7-delta-pack-index.json"

SYNC_REQUIRED_HEADINGS = [
    "## 1. Purpose",
    "## 2. Scope boundaries",
    "## 3. Governing baseline",
    "## 4. Operating loop",
    "## 5. Validation and review",
    "## 6. Acceptance notes",
]

DELTA_REQUIRED_FIELDS = [
    "trigger artifact ref or accepted task ID",
    "accepted change summary",
    "touched accepted artifact refs",
    "affected downstream artifact refs",
    "required stale-review or revalidation actions",
    "regeneration commands or explicit `None`",
    "release-gate follow-up state",
    "master-plan carry-forward entry ref",
]

DELTA_REQUIRED_COMMANDS = [
    "python3 scripts/validators/validate_control_plane_integrity.py",
    "python3 scripts/validators/validate_phase7_sync_artifacts.py",
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_header(text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in text.splitlines():
        if line.startswith("## "):
            break
        if ": " in line:
            key, value = line.split(": ", 1)
            header[key.strip()] = value.strip()
    return header


def validate_sync_pack(entry: dict, registry_ids: set[str]) -> dict:
    issues: list[str] = []
    path = REPO_ROOT / entry["canonical_locator"]
    if not path.exists():
        issues.append("sync pack file missing")
        return {
            "artifact_id": entry["artifact_id"],
            "canonical_locator": entry["canonical_locator"],
            "status": "fail",
            "issues": issues,
        }

    text = path.read_text(encoding="utf-8")
    header = extract_header(text)

    if header.get("Artifact ID") != entry["artifact_id"]:
        issues.append("header artifact id does not match registry entry")
    if header.get("Sync scope") != entry["sync_scope"]:
        issues.append("header sync scope does not match registry entry")
    if header.get("Status") != "Accepted":
        issues.append("sync pack status must be Accepted")

    for heading in SYNC_REQUIRED_HEADINGS:
        if heading not in text:
            issues.append(f"missing heading: {heading}")

    governing_refs = list(entry.get("source_authority_refs", []))
    governing_refs.extend(
        ref["artifact_id"]
        for ref in entry.get("dependency_refs", [])
        if ref.get("required_for_acceptance")
    )
    for ref in governing_refs:
        if ref not in registry_ids:
            issues.append(f"unknown governing ref in registry entry: {ref}")
        elif ref not in text:
            issues.append(f"governing ref not cited in sync pack text: {ref}")

    return {
        "artifact_id": entry["artifact_id"],
        "canonical_locator": entry["canonical_locator"],
        "status": "pass" if not issues else "fail",
        "issues": issues,
    }


def validate_delta_index(registry_ids: set[str]) -> dict:
    issues: list[str] = []

    if not DELTA_INDEX_PATH.exists():
        return {
            "artifact_id": "cp.phase7-delta-pack-index-data.v1",
            "status": "fail",
            "issues": ["delta index file missing"],
        }

    delta_index = load_json(DELTA_INDEX_PATH)
    blueprint_index = load_json(BLUEPRINT_INDEX_PATH)
    packet_index = load_json(PACKET_INDEX_PATH)

    meta = delta_index["delta_pack_index_meta"]
    requirements = delta_index["delta_template_requirements"]
    tracked_releases = delta_index["tracked_releases"]
    tracked_packets = delta_index["tracked_packets"]

    for ref_key in (
        "release_blueprint_index_ref",
        "execution_packet_index_ref",
        "delta_sync_pack_ref",
    ):
        if meta[ref_key] not in registry_ids:
            issues.append(f"metadata ref is not registered: {meta[ref_key]}")

    if requirements["required_section_headings"] != SYNC_REQUIRED_HEADINGS:
        issues.append("required section headings do not match sync validator baseline")
    if requirements["required_capture_fields"] != DELTA_REQUIRED_FIELDS:
        issues.append("required capture fields do not match delta baseline")
    if requirements["required_validator_commands"] != DELTA_REQUIRED_COMMANDS:
        issues.append("required validator commands do not match delta baseline")
    if requirements["carry_forward_log_ref"] != "cp.master-plan.v1":
        issues.append("carry_forward_log_ref must be cp.master-plan.v1")

    blueprint_entries = blueprint_index["release_blueprints"]
    packet_entries = packet_index["execution_packets"]

    expected_release_refs = {entry["release_ref"] for entry in blueprint_entries}
    expected_blueprint_refs = {
        entry["blueprint_artifact_id"] for entry in blueprint_entries
    }
    expected_packet_refs = {
        entry["packet_artifact_id"] for entry in packet_entries
    }

    actual_release_refs = {entry["release_ref"] for entry in tracked_releases}
    actual_blueprint_refs = {entry["blueprint_ref"] for entry in tracked_releases}
    actual_packet_refs = {entry["packet_ref"] for entry in tracked_packets}

    if actual_release_refs != expected_release_refs:
        issues.append("tracked release refs do not match blueprint index release refs")
    if actual_blueprint_refs != expected_blueprint_refs:
        issues.append("tracked blueprint refs do not match blueprint index artifact ids")
    if actual_packet_refs != expected_packet_refs:
        issues.append("tracked packet refs do not match execution packet index artifact ids")

    packet_refs_by_release: dict[str, list[str]] = {}
    for packet in packet_entries:
        packet_refs_by_release.setdefault(packet["release_slug"], []).append(
            packet["packet_artifact_id"]
        )

    for release in tracked_releases:
        if release["release_ref"] not in registry_ids:
            issues.append(f"tracked release ref is not registered: {release['release_ref']}")
        if release["blueprint_ref"] not in registry_ids:
            issues.append(
                f"tracked blueprint ref is not registered: {release['blueprint_ref']}"
            )
        expected_release_packets = packet_refs_by_release[release["release_slug"]]
        if release["packet_refs"] != expected_release_packets:
            issues.append(
                f"packet refs out of sync for release {release['release_slug']}"
            )

    packet_map = {entry["packet_artifact_id"]: entry for entry in packet_entries}
    for packet in tracked_packets:
        entry = packet_map.get(packet["packet_ref"])
        if entry is None:
            issues.append(f"tracked packet ref missing from packet index: {packet['packet_ref']}")
            continue
        if packet["release_slug"] != entry["release_slug"]:
            issues.append(f"tracked packet release mismatch for {packet['packet_ref']}")
        if packet["packet_family"] != entry["packet_family"]:
            issues.append(f"tracked packet family mismatch for {packet['packet_ref']}")
        if packet["packet_order"] != entry["packet_order"]:
            issues.append(f"tracked packet order mismatch for {packet['packet_ref']}")
        if packet["prerequisite_packet_refs"] != entry["prerequisite_packet_refs"]:
            issues.append(
                f"tracked packet prerequisite mismatch for {packet['packet_ref']}"
            )

    summary = delta_index["summary"]
    if summary["tracked_release_count"] != len(tracked_releases):
        issues.append("tracked_release_count summary mismatch")
    if summary["tracked_packet_count"] != len(tracked_packets):
        issues.append("tracked_packet_count summary mismatch")

    return {
        "artifact_id": "cp.phase7-delta-pack-index-data.v1",
        "canonical_locator": "docs/control-plane/core/phase-7-delta-pack-index.json",
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "tracked_release_count": len(tracked_releases),
        "tracked_packet_count": len(tracked_packets),
    }


def main() -> int:
    registry = load_json(REGISTRY_PATH)
    manifest_index = load_json(MANIFEST_PATH)
    current_state = load_json(CURRENT_STATE_PATH)

    registry_ids = {artifact["artifact_id"] for artifact in registry["artifacts"]}
    sync_entries = [
        artifact
        for artifact in registry["artifacts"]
        if artifact["artifact_type_id"] == "sync.delta_sync_pack"
    ]

    issues: list[str] = []
    if not SYNC_DIR.exists():
        issues.append("docs/control-plane/sync directory is missing")

    docs_entry = next(
        (
            entry
            for entry in manifest_index["workspace_manifests"]
            if entry["root_path"] == "docs/control-plane/"
        ),
        None,
    )
    if docs_entry is None:
        issues.append("docs/control-plane workspace manifest missing")
    else:
        if "sync/" not in docs_entry["allowed_children"]:
            issues.append("workspace manifest is missing sync/ allowed child")

    docs_state = next(
        (
            entry
            for entry in current_state["workspace_states"]
            if entry["root_path"] == "docs/control-plane/"
        ),
        None,
    )
    if docs_state is None:
        issues.append("docs/control-plane current-state entry missing")
    else:
        if "sync/" not in docs_state["notable_entries"]:
            issues.append("current-state notable entries are missing sync/")

    reports = [validate_sync_pack(entry, registry_ids) for entry in sync_entries]
    reports.append(validate_delta_index(registry_ids))

    result = {
        "status": "pass"
        if not issues and all(report["status"] == "pass" for report in reports)
        else "fail",
        "issues": issues,
        "reports": reports,
    }
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
