"""Compare the results of two experiment runs."""
import math
from typing import Any
def compare_experiments(
    baseline: dict[str, Any],
    candidate: dict[str, Any],
    tolerance: float = 0.05,
) -> dict[str, Any]:
    """Compare mean scores from two experiment records."""
    if not isinstance(baseline, dict) or not isinstance(candidate, dict):
        raise TypeError("Both experiments must be dictionaries")
    if not isinstance(tolerance, (int, float)) or isinstance(tolerance, bool):
        raise TypeError("tolerance must be a number")
    if not math.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")
    if baseline.get("task_name") != candidate.get("task_name"):
        raise ValueError("Experiments must use the same task")
    for label, experiment in (
        ("baseline", baseline),
        ("candidate", candidate),
    ):
        results = experiment.get("results")
        if not isinstance(results, dict):
            raise TypeError(f"{label} results must be a dictionary")
        score = results.get("mean_score")
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            raise ValueError(f"{label} mean_score must be numeric")
        if not math.isfinite(score):
            raise ValueError(f"{label} mean_score must be finite")
    baseline_score = baseline["results"]["mean_score"]
    candidate_score = candidate["results"]["mean_score"]
    delta = candidate_score - baseline_score
    return {
        "task_name": baseline["task_name"],
        "baseline_experiment_id": baseline.get("experiment_id"),
        "candidate_experiment_id": candidate.get("experiment_id"),
        "baseline_score": baseline_score,
        "candidate_score": candidate_score,
        "score_delta": round(delta, 10),
        "absolute_delta": round(abs(delta), 10),
        "tolerance": tolerance,
        "within_tolerance": abs(delta) <= tolerance,
        "status": (
            "within_tolerance"
            if abs(delta) <= tolerance
            else "changed_beyond_tolerance"
        ),
        "interpretation": (
            "The score difference is within the configured tolerance."
            if abs(delta) <= tolerance
            else "The score difference exceeds the configured tolerance."
        ),
        "limitations": [
            "Score differences do not establish statistical significance.",
            "This comparison does not establish which model is better.",
            "Results depend on the quality of the supplied experiment records.",
        ],
    }

