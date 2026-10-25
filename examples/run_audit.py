import json
from pathlib import Path

from src.audit import audit_record

record = {
    "experiment_id": "demo-001",
    "task_name": "local-repeatability-demo",
    "task_version": "1.0",
    "model": "deterministic-local-function",
    "prompt_version": "not-applicable-demo-v1",
    "config": {"trials": 3},
    "code_version": "demo-commit",
    "environment": {"python": "record actual version before real use"},
    "timestamp": "2026-10-25T00:00:00Z",
    "results": {"trials": [1, 1, 1]},
}

report = audit_record(record)
output = {
    "record": record,
    "audit": report,
}

destination = Path(__file__).resolve().parents[1] / "results" / "sample_audit.json"
destination.parent.mkdir(exist_ok=True)
destination.write_text(json.dumps(output, indent=2), encoding="utf-8")

print(json.dumps(report, indent=2))
print(f"\nSaved report to: {destination}")
