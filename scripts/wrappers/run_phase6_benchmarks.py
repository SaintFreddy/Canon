#!/usr/bin/env python3

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE_RULES_PATH = REPO_ROOT / "tests/fixtures/fixture-rules.json"
CONTEXT_RULES_PATH = REPO_ROOT / "docs/control-plane/core/agent-packet-context-pack-rules.json"
VALIDATOR_PATH = REPO_ROOT / "scripts/validators/validate_pilot_packets.py"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_validator_module():
    spec = importlib.util.spec_from_file_location("validate_pilot_packets", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load packet validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_benchmarks(matrix_path: Path) -> dict:
    matrix = load_json(matrix_path)
    fixture_rules = load_json(FIXTURE_RULES_PATH)
    context_rules = load_json(CONTEXT_RULES_PATH)
    validator = load_validator_module()

    fixture_bindings = {
        entry["run_class"]: entry["required_fixture_families"]
        for entry in fixture_rules["run_class_bindings"]
    }

    results = []
    pass_count = 0
    fail_count = 0

    for case in matrix["benchmark_cases"]:
        packet_path = REPO_ROOT / case["packet_path"]
        report = validator.validate_packet(packet_path, REPO_ROOT)
        issues = list(report["issues"])

        if report["run_class"] != case["run_class"]:
            issues.append("run class does not match benchmark case")
        if report["selected_budget_band"] != case["selected_budget_band"]:
            issues.append("selected budget band does not match benchmark case")
        if set(report["validation_hook_ids"]) != set(case["expected_validation_hooks"]):
            issues.append("validation hook set does not match benchmark matrix")
        if set(report["whitelist_roots"]) != set(case["expected_root_paths"]):
            issues.append("whitelist roots do not match benchmark matrix")

        expected_fixtures = set(case["expected_fixture_families"])
        actual_fixtures = set(fixture_bindings[case["run_class"]])
        if expected_fixtures != actual_fixtures:
            issues.append("fixture-family binding does not match accepted fixture rules")

        band_limit = context_rules["budget_bands"][case["selected_budget_band"]]["governing_ref_limit"]
        if report["governing_ref_count"] > band_limit:
            issues.append("governing ref count exceeds selected budget band")

        status = "pass" if not issues else "fail"
        if status == "pass":
            pass_count += 1
        else:
            fail_count += 1

        results.append(
            {
                "benchmark_case_id": case["benchmark_case_id"],
                "packet_ref": case["packet_ref"],
                "packet_path": case["packet_path"],
                "run_class": case["run_class"],
                "status": status,
                "benchmark_focus": case["benchmark_focus"],
                "metrics": {
                    "governing_ref_count": report["governing_ref_count"],
                    "governing_ref_limit": band_limit,
                    "whitelist_path_count": len(report["whitelist_paths"]),
                    "whitelist_root_count": len(report["whitelist_roots"]),
                    "validation_hook_count": len(report["validation_hook_ids"]),
                    "expected_fixture_family_count": len(case["expected_fixture_families"]),
                },
                "issues": issues,
            }
        )

    return {
        "benchmark_results_meta": {
            "schema_version": "1.0.0",
            "title": "Phase 6 pilot benchmark results",
            "task_id": "P6.4",
            "generated_on": date.today().isoformat(),
            "benchmark_matrix_ref": "cp.phase6-pilot-benchmark-matrix-data.v1",
            "benchmark_harness_ref": "cp.phase6-factory-benchmark-harness.v1",
            "benchmark_posture": "dry_run_structural"
        },
        "benchmark_results": results,
        "summary": {
            "case_count": len(results),
            "pass_count": pass_count,
            "fail_count": fail_count
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--matrix", required=True, help="benchmark matrix path")
    parser.add_argument("--write", help="results output path")
    args = parser.parse_args()

    matrix_path = REPO_ROOT / args.matrix if not Path(args.matrix).is_absolute() else Path(args.matrix)
    results = run_benchmarks(matrix_path)

    if args.write:
        write_path = REPO_ROOT / args.write if not Path(args.write).is_absolute() else Path(args.write)
        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(results, indent=2))
    return 0 if results["summary"]["fail_count"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
