#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "docs/control-plane/artifact-registry.seed.json"
DEFAULT_CHECKLIST_PATH = (
    REPO_ROOT / "docs/control-plane/core/phase-7-architecture-sync-checklist.json"
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run_sync(checklist_path: Path, changed_artifact_refs: list[str]) -> dict:
    checklist = load_json(checklist_path)
    registry = load_json(REGISTRY_PATH)
    registry_by_id = {artifact["artifact_id"]: artifact for artifact in registry["artifacts"]}

    reports = []
    blocked_count = 0
    review_required_count = 0
    highlighted_count = 0

    for group in checklist["check_groups"]:
        required_artifact_reports = []
        missing_basis = False

        for ref in group["required_artifact_refs"]:
            artifact = registry_by_id.get(ref)
            if artifact is None:
                required_artifact_reports.append(
                    {"artifact_ref": ref, "status": "missing"}
                )
                missing_basis = True
                continue

            status = (
                "accepted"
                if artifact["artifact_status"] == "accepted"
                else f"not_{artifact['artifact_status']}"
            )
            required_artifact_reports.append(
                {
                    "artifact_ref": ref,
                    "status": status,
                    "canonical_locator": artifact["canonical_locator"],
                }
            )
            if artifact["artifact_status"] != "accepted":
                missing_basis = True

        highlighted = any(
            ref in changed_artifact_refs for ref in group["required_artifact_refs"]
        )
        if highlighted:
            highlighted_count += 1

        status = "blocked" if missing_basis else "review_required"
        if status == "blocked":
            blocked_count += 1
        else:
            review_required_count += 1

        reports.append(
            {
                "check_group_id": group["check_group_id"],
                "title": group["title"],
                "status": status,
                "highlighted_by_changed_artifacts": highlighted,
                "required_artifact_reports": required_artifact_reports,
                "review_prompts": group["review_prompts"],
                "escalation_on": group["escalation_on"],
            }
        )

    return {
        "architecture_sync_report_meta": {
            "schema_version": "1.0.0",
            "title": "Phase 7 architecture sync report",
            "task_id": "P7.2",
            "generated_on": date.today().isoformat(),
            "checklist_ref": "cp.phase7-architecture-sync-checklist-data.v1",
            "changed_artifact_refs": changed_artifact_refs,
        },
        "check_group_reports": reports,
        "summary": {
            "check_group_count": len(reports),
            "blocked_count": blocked_count,
            "review_required_count": review_required_count,
            "highlighted_group_count": highlighted_count,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--checklist",
        default=str(DEFAULT_CHECKLIST_PATH),
        help="architecture checklist path",
    )
    parser.add_argument(
        "--changed-artifact",
        action="append",
        default=[],
        dest="changed_artifacts",
        help="artifact ref that triggered the sync run",
    )
    parser.add_argument("--write", help="optional output path")
    args = parser.parse_args()

    checklist_path = (
        Path(args.checklist)
        if Path(args.checklist).is_absolute()
        else REPO_ROOT / args.checklist
    )
    results = run_sync(checklist_path, args.changed_artifacts)

    if args.write:
        write_path = (
            Path(args.write)
            if Path(args.write).is_absolute()
            else REPO_ROOT / args.write
        )
        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(results, indent=2))
    return 0 if results["summary"]["blocked_count"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
