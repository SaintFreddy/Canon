#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import shlex
import subprocess
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MATRIX_PATH = (
    REPO_ROOT / "docs/control-plane/core/phase-7-release-gate-recheck-matrix.json"
)
STALE_WRAPPER_PATH = REPO_ROOT / "scripts/wrappers/run_phase7_stale_detection.py"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def excerpt(text: str, limit: int = 8) -> list[str]:
    lines = [line for line in text.strip().splitlines() if line.strip()]
    if len(lines) <= limit:
        return lines
    return lines[-limit:]


def load_stale_wrapper_module():
    spec = importlib.util.spec_from_file_location(
        "run_phase7_stale_detection", STALE_WRAPPER_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load stale detection wrapper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_path(path_value: str, repo_root: Path = REPO_ROOT) -> Path:
    path = Path(path_value)
    return path if path.is_absolute() else repo_root / path


def build_stale_report(
    changed_artifact_refs: list[str], rules_path: Path | None = None
) -> dict:
    module = load_stale_wrapper_module()
    selected_rules_path = (
        rules_path if rules_path is not None else Path(module.DEFAULT_RULES_PATH)
    )
    return module.build_impact_report(
        selected_rules_path,
        changed_artifact_refs,
        apply_registry=False,
        run_regeneration=False,
    )


def selection_inputs_from_stale_report(stale_report: dict) -> tuple[list[str], list[str]]:
    changed_artifact_refs = stale_report["stale_detection_report_meta"][
        "changed_artifact_refs"
    ]
    impacted_artifact_refs = [
        entry["artifact_id"] for entry in stale_report.get("impacted_artifacts", [])
    ]
    combined: list[str] = []
    for ref in [*changed_artifact_refs, *impacted_artifact_refs]:
        if ref not in combined:
            combined.append(ref)
    return combined, impacted_artifact_refs


def select_gate_targets(matrix: dict, stale_report: dict) -> list[dict]:
    selection_inputs, _ = selection_inputs_from_stale_report(stale_report)
    platform_gate_target = next(
        target for target in matrix["gate_targets"] if target["gate_id"] == "platform_gate"
    )

    selected: list[dict] = []
    selected_ids: set[str] = set()
    release_gate_ids: list[str] = []

    for target in sorted(matrix["gate_targets"], key=lambda item: item["release_order"]):
        matched_artifact_refs = [
            ref for ref in selection_inputs if ref in target["trigger_artifact_refs"]
        ]
        if not matched_artifact_refs:
            continue
        selected.append(
            {
                **target,
                "selection_reason": "stale_input_match",
                "matched_artifact_refs": matched_artifact_refs,
                "inherited_from_gate_ids": [],
            }
        )
        selected_ids.add(target["gate_id"])
        if target["release_slug"] is not None:
            release_gate_ids.append(target["gate_id"])

    if release_gate_ids and platform_gate_target["gate_id"] not in selected_ids:
        selected.insert(
            0,
            {
                **platform_gate_target,
                "selection_reason": "inherited_platform_gate",
                "matched_artifact_refs": [],
                "inherited_from_gate_ids": release_gate_ids,
            },
        )

    return sorted(selected, key=lambda item: item["release_order"])


def materialize_command(command: str, changed_artifact_refs: list[str]) -> str:
    if command == "python3 scripts/wrappers/run_phase7_architecture_sync.py":
        if not changed_artifact_refs:
            return command
        parts = [command]
        parts.extend(
            f"--changed-artifact {shlex.quote(ref)}" for ref in changed_artifact_refs
        )
        return " ".join(parts)
    return command


def run_commands(commands: list[str]) -> tuple[list[dict], bool]:
    results: list[dict] = []
    failed = False
    for command in commands:
        completed = subprocess.run(
            shlex.split(command),
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            failed = True
        results.append(
            {
                "command": command,
                "returncode": completed.returncode,
                "stdout_excerpt": excerpt(completed.stdout),
                "stderr_excerpt": excerpt(completed.stderr),
            }
        )
    return results, failed


def build_recheck_report(
    matrix: dict, stale_report: dict, run_recheck_commands: bool = False
) -> dict:
    changed_artifact_refs = stale_report["stale_detection_report_meta"][
        "changed_artifact_refs"
    ]
    _, impacted_artifact_refs = selection_inputs_from_stale_report(stale_report)
    selected_gate_targets = select_gate_targets(matrix, stale_report)

    materialized_commands: list[str] = []
    for target in selected_gate_targets:
        for command in target["recheck_commands"]:
            materialized = materialize_command(command, changed_artifact_refs)
            if materialized not in materialized_commands:
                materialized_commands.append(materialized)

    command_results: list[dict] = []
    recheck_failed = False
    if run_recheck_commands and materialized_commands:
        command_results, recheck_failed = run_commands(materialized_commands)

    if not selected_gate_targets:
        follow_up_state = "not_required"
    elif not run_recheck_commands:
        follow_up_state = "recheck_required"
    elif recheck_failed:
        follow_up_state = "recheck_fail"
    else:
        follow_up_state = "recheck_pass"

    return {
        "release_gate_recheck_report_meta": {
            "schema_version": "1.0.0",
            "title": "Phase 7 release gate recheck report",
            "task_id": "P7.4",
            "generated_on": date.today().isoformat(),
            "matrix_ref": "cp.phase7-release-gate-recheck-matrix-data.v1",
            "stale_input_changed_artifact_refs": changed_artifact_refs,
            "stale_input_impacted_artifact_refs": impacted_artifact_refs,
            "ran_recheck_commands": run_recheck_commands,
        },
        "selected_gate_targets": selected_gate_targets,
        "command_results": command_results,
        "summary": {
            "selected_gate_count": len(selected_gate_targets),
            "release_gate_count": sum(
                1 for target in selected_gate_targets if target["release_slug"] is not None
            ),
            "platform_gate_selected": any(
                target["gate_id"] == "platform_gate" for target in selected_gate_targets
            ),
            "command_count": len(materialized_commands),
            "release_gate_follow_up_state": follow_up_state,
            "recheck_failed": recheck_failed,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--matrix",
        default=str(DEFAULT_MATRIX_PATH),
        help="release gate recheck matrix path",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--stale-report", help="existing stale detection report path")
    group.add_argument(
        "--changed-artifact",
        action="append",
        dest="changed_artifacts",
        help="accepted artifact ref that changed upstream",
    )
    parser.add_argument(
        "--rules",
        help="optional stale regeneration rules path when generating a stale report from changed artifacts",
    )
    parser.add_argument("--run-commands", action="store_true")
    parser.add_argument("--write", help="optional output path")
    args = parser.parse_args()

    matrix_path = resolve_path(args.matrix)
    matrix = load_json(matrix_path)

    if args.stale_report:
        stale_report = load_json(resolve_path(args.stale_report))
    else:
        rules_path = resolve_path(args.rules) if args.rules else None
        stale_report = build_stale_report(args.changed_artifacts, rules_path)

    report = build_recheck_report(
        matrix,
        stale_report,
        run_recheck_commands=args.run_commands,
    )

    if args.write:
        write_path = resolve_path(args.write)
        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report, indent=2))
    return 0 if report["summary"]["release_gate_follow_up_state"] != "recheck_fail" else 1


if __name__ == "__main__":
    sys.exit(main())
