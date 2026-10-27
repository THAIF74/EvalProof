"""Demonstrate repeated evaluation with a deterministic toy evaluator."""

import json
from pathlib import Path

from src.repeatability import run_trials


def demo_evaluator() -> float:
    """Return a fixed demo score; this is not an AI model evaluation."""
    return 0.8


report = run_trials(demo_evaluator, trials=3)

output_path = Path("results/repeatability_demo.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8",
)

print(json.dumps(report, indent=2))
print(f"\nSaved report to: {output_path}")
