import unittest

from src.experiment_record import create_experiment_record


class ExperimentRecordTests(unittest.TestCase):
    def make_record(self, **overrides):
        data = {
            "task_name": "toy-classification",
            "task_version": "1.0",
            "model": "demo-evaluator",
            "prompt_version": "prompt-v1",
            "config": {"trials": 3, "seed": 42},
            "code_version": "prototype",
            "results": {"mean_score": 0.8, "score_range": 0.0},
        }
        data.update(overrides)
        return create_experiment_record(**data)

    def test_record_contains_required_metadata(self):
        record = self.make_record()
        required_fields = (
            "experiment_id", "task_name", "task_version", "model",
            "prompt_version", "config", "code_version", "timestamp",
            "environment", "results",
        )
        for field in required_fields:
            self.assertIn(field, record)

    def test_experiment_ids_are_unique(self):
        self.assertNotEqual(
            self.make_record()["experiment_id"],
            self.make_record()["experiment_id"],
        )

    def test_environment_contains_python_and_os(self):
        environment = self.make_record()["environment"]
        self.assertTrue(environment["python_version"])
        self.assertTrue(environment["operating_system"])

    def test_blank_task_name_is_rejected(self):
        with self.assertRaises(ValueError):
            self.make_record(task_name=" ")

    def test_config_must_be_a_dictionary(self):
        with self.assertRaises(TypeError):
            self.make_record(config="trials=3")

    def test_empty_results_are_rejected(self):
        with self.assertRaises(ValueError):
            self.make_record(results={})

    def test_results_must_be_a_dictionary(self):
        with self.assertRaises(TypeError):
            self.make_record(results=[0.8])


if __name__ == "__main__":
    unittest.main()
