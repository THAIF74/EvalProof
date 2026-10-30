"""Demonstrate comparing two experiment runs."""
import json
from pathlib import Path
from src.comparison import compare_experiments
from src.experiment_record import create_experiment_record
def make_demo_experiment(score):
    return create_experiment_record(
        task_name="toy-evaluation",
        task_version="1.0",
        model="deterministic-demo-evaluator",
        prompt_version="not-applicable",
        config={"trials": 3},
        code_version="local-prototype",
        results={"mean_score": score},
    )
baseline = make_demo_experiment(0.80)
candidate = make_demo_experiment(0.86)
comparison = compare_experiments(
    baseline,
    candidate,
    tolerance=0.05,
)
output_path = Path("results/comparison_demo.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(
    json.dumps(comparison, indent=2),
    encoding="utf-8",
)
print(json.dumps(comparison, indent=2))
print(f"\nSaved comparison to: {output_path}")
