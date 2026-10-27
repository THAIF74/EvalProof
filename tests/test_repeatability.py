import unittest

from src.repeatability import run_trials


class RepeatabilityTests(unittest.TestCase):
    def test_identical_scores_have_zero_range(self):
        result = run_trials(lambda: 0.8, trials=3)
        self.assertEqual(result["trial_count"], 3)
        self.assertEqual(result["mean_score"], 0.8)
        self.assertEqual(result["score_range"], 0.0)

    def test_variable_scores_are_summarized(self):
        values = iter([0.5, 0.7, 0.9])
        result = run_trials(lambda: next(values), trials=3)
        self.assertEqual(result["mean_score"], 0.7)
        self.assertEqual(result["min_score"], 0.5)
        self.assertEqual(result["max_score"], 0.9)
        self.assertEqual(result["score_range"], 0.4)

    def test_one_trial_is_supported(self):
        result = run_trials(lambda: 1.0, trials=1)
        self.assertEqual(result["trial_count"], 1)
        self.assertEqual(result["score_range"], 0.0)

    def test_zero_trials_are_rejected(self):
        with self.assertRaises(ValueError):
            run_trials(lambda: 0.5, trials=0)

    def test_scores_outside_range_are_rejected(self):
        with self.assertRaises(ValueError):
            run_trials(lambda: 1.2)

    def test_non_numeric_score_is_rejected(self):
        with self.assertRaises(TypeError):
            run_trials(lambda: "0.8")


if __name__ == "__main__":
    unittest.main()
