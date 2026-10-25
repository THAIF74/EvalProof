"""Audit evaluation records for required reproducibility metadata."""

from typing import Any

REQUIRED_FIELDS = {
    "experiment_id": "Unique experiment identifier",
    "task_name": "Name of the evaluated task",
    "task_version": "Version of the task or dataset",
    "model": "Model or system evaluated",
    "prompt_version": "Version or identifier of the prompt",
    "config": "Evaluation configuration",
    "code_version": "Code commit or version",
    "environment": "Runtime and dependency information",
    "timestamp": "When the evaluation ran",
    "results": "Evaluation outcome or score",
}


def _is_missing(value: Any) -> bool:
    """Return whether a field lacks a meaningful recorded value."""
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (dict, list, tuple, set)):
        return len(value) == 0
    return False


def audit_record(record: dict[str, Any]) -> dict[str, Any]:
    """Report missing required fields and calculate field completeness.

    The score measures metadata presence only. It does not prove that
    recorded values are accurate or that an experiment can be reproduced.
    """
    if not isinstance(record, dict):
        raise TypeError("record must be a dictionary")

    missing = [
        {"field": field, "description": description}
        for field, description in REQUIRED_FIELDS.items()
        if field not in record or _is_missing(record[field])
    ]

    total = len(REQUIRED_FIELDS)
    present = total - len(missing)

    return {
        "total_required_fields": total,
        "present_fields": present,
        "missing_count": len(missing),
        "completeness_percent": round(present / total * 100, 1),
        "missing_fields": missing,
        "status": "complete" if not missing else "incomplete",
        "limitations": [
            "Completeness does not guarantee reproducibility.",
            "Field presence does not verify that values are correct.",
            "Required fields are an initial prototype policy, not a standard.",
        ],
    }
