"""Demonstrate repeated evaluation with experiment metadata."""

import json
from pathlib import Path

from src.experiment_record import create_experiment_record
from src.repeatability import run_trials


def demo_evaluator() -> float:
    """Return a fixed toy score, not a real AI benchmark result."""
    return 0.8


run_results = run_trials(demo_evaluator, trials=3)

report = create_experiment_record(
    task_name="toy-evaluation",
    task_version="1.0",
    model="deterministic-demo-evaluator",
    prompt_version="not-applicable",
    config={"trials": 3, "score_range": [0.0, 1.0]},
    code_version="local-prototype",
    results=run_results,
)

output_path = Path("results/repeatability_demo.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8",
)

print(json.dumps(report, indent=2))
print(f"\nSaved report to: {output_path}")
