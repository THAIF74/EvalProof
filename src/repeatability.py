"""Run repeated evaluations and summarize score variation."""

from statistics import mean
from typing import Callable


def run_trials(
    evaluator: Callable[[], float],
    trials: int = 3,
) -> dict:
    """Run an evaluator repeatedly and summarize its scores."""
    if isinstance(trials, bool) or not isinstance(trials, int) or trials < 1:
        raise ValueError("trials must be a positive integer")

    scores = []

    for trial_number in range(1, trials + 1):
        score = evaluator()

        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("evaluator must return a numeric score")

        if not 0 <= score <= 1:
            raise ValueError("each score must be between 0 and 1")

        scores.append({
            "trial": trial_number,
            "score": float(score),
        })

    values = [item["score"] for item in scores]

    return {
        "trial_count": trials,
        "scores": scores,
        "mean_score": round(mean(values), 4),
        "min_score": min(values),
        "max_score": max(values),
        "score_range": round(max(values) - min(values), 4),
        "limitations": [
            "Repeated scores do not prove reproducibility.",
            "This runner does not control evaluator randomness or environment.",
            "The demo evaluator is not a real AI model benchmark.",
        ],
    }
