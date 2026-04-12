#!/usr/bin/env python3
from __future__ import annotations

import json
import shlex
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
ARCHITECTURE_CHECKLIST_PATH = (
    REPO_ROOT / "docs/control-plane/core/phase-7-architecture-sync-checklist.json"
)
STALE_RULES_PATH = (
    REPO_ROOT / "docs/control-plane/core/phase-7-stale-regeneration-rules.json"
)
RELEASE_GATE_MATRIX_PATH = (
    REPO_ROOT / "docs/control-plane/core/phase-7-release-gate-recheck-matrix.json"
)

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

ARCHITECTURE_REQUIRED_STATUSES = {
    "aligned",
    "review_required",
    "stale_candidate",
    "blocked",
}

EXPECTED_PROPAGATION_ACTIONS = {
    "auto": "mark_stale",
    "manual": "manual_review",
    "revalidate": "revalidate",
    "none": "ignore",
}

EXPECTED_RELEASE_GATE_FOLLOW_UP_STATES = {
    "not_required",
    "recheck_required",
    "recheck_pass",
    "recheck_fail",
}

EXPECTED_RELEASE_GATE_TEST_IDS = {
    "platform_gate": [
        "PG-01",
        "PG-02",
        "PG-03",
        "PG-04",
        "PG-05",
        "PG-06",
        "PG-07",
        "PG-08",
        "PG-09",
        "PG-10",
    ],
    "r1-conversation": ["PG-01", "PG-02", "PG-03"],
    "r2-context-control": ["PG-01", "PG-02"],
    "r3-branch-replay": ["PG-01", "PG-04"],
    "r4-artifact-workspace": ["PG-05", "PG-06"],
    "r5-prompt-assets": ["PG-06", "PG-07"],
    "r6-governed-reusable-execution": ["PG-06", "PG-07"],
    "r7-commissioning-bridge": ["PG-05", "PG-06", "PG-08", "PG-09"],
}

PLATFORM_GATE_TRIGGER_REFS = [
    "arch.phase3-platform-gate-spec.v1",
    "rel.chat-native-maturity-matrix.v1",
    "rel.chat-native-milestone-architecture-plan.v1",
    "sync.phase7-recurring-architecture-sync.v1",
    "cp.phase7-architecture-sync-checklist-data.v1",
    "sync.phase7-stale-regeneration-loop.v1",
    "cp.phase7-stale-regeneration-rules-data.v1",
]

PLATFORM_GATE_COMMANDS = [
    "python3 scripts/validators/validate_control_plane_integrity.py",
    "python3 scripts/validators/validate_phase7_sync_artifacts.py",
    "python3 scripts/wrappers/run_phase7_architecture_sync.py",
]

PLATFORM_GATE_GOVERNING_REFS = [
    "arch.phase3-platform-gate-spec.v1",
    "rel.chat-native-maturity-matrix.v1",
    "rel.chat-native-milestone-architecture-plan.v1",
    "sync.phase7-recurring-architecture-sync.v1",
    "cp.phase7-architecture-sync-checklist-data.v1",
    "sync.phase7-stale-regeneration-loop.v1",
    "cp.phase7-stale-regeneration-rules-data.v1",
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


def validate_command_refs(command: str) -> list[str]:
    issues: list[str] = []
    tokens = shlex.split(command)
    if not tokens:
        return ["empty regeneration command"]

    for token in tokens[1:]:
        if token.startswith(("scripts/", "docs/", "tests/", ".factory/")):
            if not (REPO_ROOT / token).exists():
                issues.append(f"command references missing path: {token}")

    return issues


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


def validate_architecture_checklist(registry_ids: set[str]) -> dict | None:
    if not ARCHITECTURE_CHECKLIST_PATH.exists():
        return None

    issues: list[str] = []
    checklist = load_json(ARCHITECTURE_CHECKLIST_PATH)
    meta = checklist["architecture_sync_checklist_meta"]
    groups = checklist["check_groups"]
    status_catalog = checklist["result_status_catalog"]

    for ref_key in ("sync_pack_ref", "delta_pack_ref", "baseline_sync_pass_ref"):
        if meta[ref_key] not in registry_ids:
            issues.append(f"metadata ref is not registered: {meta[ref_key]}")

    status_values = {entry["status"] for entry in status_catalog}
    if status_values != ARCHITECTURE_REQUIRED_STATUSES:
        issues.append("architecture status catalog does not match accepted baseline")

    for group in groups:
        if not group["review_prompts"]:
            issues.append(f"check group missing review prompts: {group['check_group_id']}")
        if not group["escalation_on"]:
            issues.append(f"check group missing escalation list: {group['check_group_id']}")
        for ref in group["required_artifact_refs"]:
            if ref not in registry_ids:
                issues.append(
                    f"check group references unregistered artifact: {group['check_group_id']} -> {ref}"
                )

    if checklist["summary"]["check_group_count"] != len(groups):
        issues.append("architecture checklist summary count mismatch")

    wrapper_path = REPO_ROOT / "scripts/wrappers/run_phase7_architecture_sync.py"
    if not wrapper_path.exists():
        issues.append("architecture sync wrapper is missing")

    return {
        "artifact_id": "cp.phase7-architecture-sync-checklist-data.v1",
        "canonical_locator": "docs/control-plane/core/phase-7-architecture-sync-checklist.json",
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "check_group_count": len(groups),
    }


def validate_stale_regeneration_rules(
    registry_ids: set[str], artifact_type_ids: set[str]
) -> dict | None:
    if not STALE_RULES_PATH.exists():
        return None

    issues: list[str] = []
    rules = load_json(STALE_RULES_PATH)
    meta = rules["stale_regeneration_rules_meta"]
    propagation_action_map = rules["propagation_action_map"]
    type_rules = rules["artifact_type_rules"]
    overrides = rules["artifact_overrides"]

    for ref_key in (
        "sync_pack_ref",
        "delta_pack_ref",
        "architecture_checklist_ref",
        "registry_ref",
        "dependency_graph_ref",
    ):
        if meta[ref_key] not in registry_ids:
            issues.append(f"metadata ref is not registered: {meta[ref_key]}")

    actual_action_map = {
        entry["propagation_mode"]: entry["action"] for entry in propagation_action_map
    }
    if actual_action_map != EXPECTED_PROPAGATION_ACTIONS:
        issues.append("propagation_action_map does not match accepted action baseline")

    for rule in type_rules:
        if rule["artifact_type_id"] not in artifact_type_ids:
            issues.append(
                f"artifact_type_rule references unknown artifact type: {rule['artifact_type_id']}"
            )
        if not rule["regeneration_commands"]:
            issues.append(
                f"artifact_type_rule missing regeneration commands: {rule['artifact_type_id']}"
            )
        for command in rule["regeneration_commands"]:
            issues.extend(validate_command_refs(command))

    for override in overrides:
        if override["artifact_ref"] not in registry_ids:
            issues.append(
                f"artifact_override references unregistered artifact: {override['artifact_ref']}"
            )
        if not override["regeneration_commands"]:
            issues.append(
                f"artifact_override missing regeneration commands: {override['artifact_ref']}"
            )
        for command in override["regeneration_commands"]:
            issues.extend(validate_command_refs(command))

    if rules["summary"]["artifact_type_rule_count"] != len(type_rules):
        issues.append("artifact_type_rule_count summary mismatch")
    if rules["summary"]["artifact_override_count"] != len(overrides):
        issues.append("artifact_override_count summary mismatch")

    wrapper_path = REPO_ROOT / "scripts/wrappers/run_phase7_stale_detection.py"
    if not wrapper_path.exists():
        issues.append("stale detection wrapper is missing")

    return {
        "artifact_id": "cp.phase7-stale-regeneration-rules-data.v1",
        "canonical_locator": "docs/control-plane/core/phase-7-stale-regeneration-rules.json",
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "artifact_type_rule_count": len(type_rules),
        "artifact_override_count": len(overrides),
    }


def validate_release_gate_recheck_matrix(
    registry_ids: set[str], validation_hook_ids: set[str]
) -> dict | None:
    if not RELEASE_GATE_MATRIX_PATH.exists():
        return None

    issues: list[str] = []
    matrix = load_json(RELEASE_GATE_MATRIX_PATH)
    delta_index = load_json(DELTA_INDEX_PATH)
    blueprint_index = load_json(BLUEPRINT_INDEX_PATH)
    packet_index = load_json(PACKET_INDEX_PATH)

    meta = matrix["release_gate_recheck_matrix_meta"]
    state_catalog = matrix["release_gate_follow_up_state_catalog"]
    gate_targets = matrix["gate_targets"]

    for ref_key in (
        "delta_pack_index_ref",
        "architecture_sync_ref",
        "architecture_checklist_ref",
        "stale_sync_pack_ref",
        "stale_rules_ref",
        "platform_gate_ref",
        "maturity_matrix_ref",
        "milestone_plan_ref",
        "release_blueprint_index_ref",
        "execution_packet_index_ref",
    ):
        if meta[ref_key] not in registry_ids:
            issues.append(f"metadata ref is not registered: {meta[ref_key]}")

    actual_states = {entry["state"] for entry in state_catalog}
    if actual_states != EXPECTED_RELEASE_GATE_FOLLOW_UP_STATES:
        issues.append("release gate follow-up states do not match accepted baseline")

    release_by_slug = {
        entry["release_slug"]: entry for entry in delta_index["tracked_releases"]
    }
    blueprint_by_slug = {
        entry["release_slug"]: entry for entry in blueprint_index["release_blueprints"]
    }
    packets_by_slug: dict[str, list[dict]] = {}
    for entry in packet_index["execution_packets"]:
        packets_by_slug.setdefault(entry["release_slug"], []).append(entry)
    for entries in packets_by_slug.values():
        entries.sort(key=lambda item: item["packet_order"])

    seen_gate_ids: set[str] = set()
    platform_gate_count = 0
    for target in gate_targets:
        if target["gate_id"] in seen_gate_ids:
            issues.append(f"duplicate gate target id: {target['gate_id']}")
            continue
        seen_gate_ids.add(target["gate_id"])

        expected_test_ids = EXPECTED_RELEASE_GATE_TEST_IDS.get(target["gate_id"])
        if expected_test_ids is None:
            issues.append(f"unexpected gate target id: {target['gate_id']}")
            continue

        if target["gate_ref"] not in registry_ids:
            issues.append(f"gate_ref is not registered: {target['gate_id']}")
        if target["blueprint_ref"] is not None and target["blueprint_ref"] not in registry_ids:
            issues.append(f"blueprint_ref is not registered: {target['gate_id']}")

        for ref in (
            target["trigger_artifact_refs"]
            + target["packet_refs"]
            + target["governing_artifact_refs"]
        ):
            if ref not in registry_ids:
                issues.append(
                    f"gate target references unregistered artifact: {target['gate_id']} -> {ref}"
                )

        for hook_id in target["validation_hook_ids"]:
            if hook_id not in validation_hook_ids:
                issues.append(
                    f"gate target references unknown validation hook: {target['gate_id']} -> {hook_id}"
                )

        for command in target["recheck_commands"]:
            issues.extend(validate_command_refs(command))

        if target["platform_gate_test_ids"] != expected_test_ids:
            issues.append(
                f"platform_gate_test_ids do not match accepted baseline for {target['gate_id']}"
            )

        if target["gate_id"] == "platform_gate":
            platform_gate_count += 1
            if target["release_slug"] is not None:
                issues.append("platform_gate release_slug must be null")
            if target["release_order"] != 0:
                issues.append("platform_gate release_order must be 0")
            if target["inherits_platform_gate"]:
                issues.append("platform_gate may not inherit itself")
            if target["blueprint_ref"] is not None:
                issues.append("platform_gate blueprint_ref must be null")
            if target["packet_refs"]:
                issues.append("platform_gate packet_refs must be empty")
            if target["trigger_artifact_refs"] != PLATFORM_GATE_TRIGGER_REFS:
                issues.append("platform_gate trigger_artifact_refs are out of sync")
            if target["recheck_commands"] != PLATFORM_GATE_COMMANDS:
                issues.append("platform_gate recheck_commands are out of sync")
            if target["governing_artifact_refs"] != PLATFORM_GATE_GOVERNING_REFS:
                issues.append("platform_gate governing_artifact_refs are out of sync")
            continue

        release_slug = target["release_slug"]
        if release_slug not in release_by_slug:
            issues.append(f"release gate has unknown release_slug: {target['gate_id']}")
            continue

        release = release_by_slug[release_slug]
        blueprint = blueprint_by_slug[release_slug]
        packets = packets_by_slug[release_slug]
        expected_packet_refs = [entry["packet_artifact_id"] for entry in packets]
        expected_trigger_refs = [
            release["release_ref"],
            blueprint["blueprint_artifact_id"],
            *expected_packet_refs,
        ]
        expected_packet_command = (
            "python3 scripts/validators/validate_pilot_packets.py "
            + " ".join(entry["packet_path"] for entry in packets)
        )
        expected_governing_refs = [
            release["release_ref"],
            "arch.phase3-platform-gate-spec.v1",
            "rel.chat-native-maturity-matrix.v1",
            "rel.chat-native-milestone-architecture-plan.v1",
            blueprint["blueprint_artifact_id"],
        ]

        if target["gate_ref"] != release["release_ref"]:
            issues.append(f"gate_ref mismatch for {target['gate_id']}")
        if target["release_order"] != blueprint["release_order"]:
            issues.append(f"release_order mismatch for {target['gate_id']}")
        if not target["inherits_platform_gate"]:
            issues.append(f"release gate must inherit Platform Gate: {target['gate_id']}")
        if target["blueprint_ref"] != blueprint["blueprint_artifact_id"]:
            issues.append(f"blueprint_ref mismatch for {target['gate_id']}")
        if target["packet_refs"] != expected_packet_refs:
            issues.append(f"packet_refs mismatch for {target['gate_id']}")
        if target["trigger_artifact_refs"] != expected_trigger_refs:
            issues.append(f"trigger_artifact_refs mismatch for {target['gate_id']}")
        if target["required_fixture_families"] != blueprint["required_fixture_families"]:
            issues.append(f"required_fixture_families mismatch for {target['gate_id']}")
        if target["validation_hook_ids"] != blueprint["validation_hooks"]:
            issues.append(f"validation_hook_ids mismatch for {target['gate_id']}")
        if target["recheck_commands"] != [
            "python3 scripts/validators/validate_release_blueprints.py",
            expected_packet_command,
        ]:
            issues.append(f"recheck_commands mismatch for {target['gate_id']}")
        if target["governing_artifact_refs"] != expected_governing_refs:
            issues.append(f"governing_artifact_refs mismatch for {target['gate_id']}")

    if platform_gate_count != 1:
        issues.append("release gate matrix must contain exactly one platform_gate target")

    shared_commands: list[str] = []
    for target in gate_targets:
        for command in target["recheck_commands"]:
            if command not in shared_commands:
                shared_commands.append(command)

    if matrix["summary"]["gate_target_count"] != len(gate_targets):
        issues.append("gate_target_count summary mismatch")
    if matrix["summary"]["release_gate_count"] != len(gate_targets) - 1:
        issues.append("release_gate_count summary mismatch")
    if matrix["summary"]["shared_command_count"] != len(shared_commands):
        issues.append("shared_command_count summary mismatch")

    wrapper_path = REPO_ROOT / "scripts/wrappers/run_phase7_release_gate_rechecks.py"
    if not wrapper_path.exists():
        issues.append("release gate recheck wrapper is missing")

    return {
        "artifact_id": "cp.phase7-release-gate-recheck-matrix-data.v1",
        "canonical_locator": "docs/control-plane/core/phase-7-release-gate-recheck-matrix.json",
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "gate_target_count": len(gate_targets),
        "release_gate_count": len(gate_targets) - 1,
    }


def main() -> int:
    registry = load_json(REGISTRY_PATH)
    manifest_index = load_json(MANIFEST_PATH)
    current_state = load_json(CURRENT_STATE_PATH)

    registry_ids = {artifact["artifact_id"] for artifact in registry["artifacts"]}
    validation_hook_ids = {
        hook["hook_id"] for hook in registry["validation_hook_standards"]
    }
    artifact_type_ids = {
        artifact_type["artifact_type_id"] for artifact_type in registry["artifact_types"]
    }
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
    architecture_report = validate_architecture_checklist(registry_ids)
    if architecture_report is not None:
        reports.append(architecture_report)
    stale_rules_report = validate_stale_regeneration_rules(
        registry_ids, artifact_type_ids
    )
    if stale_rules_report is not None:
        reports.append(stale_rules_report)
    release_gate_report = validate_release_gate_recheck_matrix(
        registry_ids, validation_hook_ids
    )
    if release_gate_report is not None:
        reports.append(release_gate_report)

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
