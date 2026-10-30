import unittest
from src.comparison import compare_experiments
class ComparisonTests(unittest.TestCase):
    def make_experiment(self, score, task="toy-classification"):
        return {
            "experiment_id": f"experiment-{score}",
            "task_name": task,
            "results": {"mean_score": score},
        }
    def test_equal_scores_are_within_tolerance(self):
        result = compare_experiments(
            self.make_experiment(0.8),
            self.make_experiment(0.8),
        )
        self.assertTrue(result["within_tolerance"])
    def test_small_difference_is_within_tolerance(self):
        result = compare_experiments(
            self.make_experiment(0.80),
            self.make_experiment(0.82),
        )
        self.assertTrue(result["within_tolerance"])
    def test_large_difference_exceeds_tolerance(self):
        result = compare_experiments(
            self.make_experiment(0.70),
            self.make_experiment(0.90),
        )
        self.assertFalse(result["within_tolerance"])
    def test_score_delta_is_calculated(self):
        result = compare_experiments(
            self.make_experiment(0.70),
            self.make_experiment(0.85),
        )
        self.assertAlmostEqual(result["score_delta"], 0.15)
    def test_negative_delta_is_supported(self):
        result = compare_experiments(
            self.make_experiment(0.90),
            self.make_experiment(0.70),
        )
        self.assertAlmostEqual(result["score_delta"], -0.20)
    def test_different_tasks_are_rejected(self):
        with self.assertRaises(ValueError):
            compare_experiments(
                self.make_experiment(0.8),
                self.make_experiment(0.9, task="other-task"),
            )
    def test_invalid_score_is_rejected(self):
        with self.assertRaises(ValueError):
            compare_experiments(
                self.make_experiment(0.8),
                self.make_experiment("invalid"),
            )
    def test_negative_tolerance_is_rejected(self):
        with self.assertRaises(ValueError):
            compare_experiments(
                self.make_experiment(0.8),
                self.make_experiment(0.9),
                tolerance=-0.1,
            )
if __name__ == "__main__":
    unittest.main()
