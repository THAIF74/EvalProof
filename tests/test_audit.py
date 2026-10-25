import unittest

from src.audit import REQUIRED_FIELDS, audit_record


def valid_record():
    """Return a sample record with every required field populated."""
    return {
        "experiment_id": "demo-001",
        "task_name": "repeatability-test",
        "task_version": "1.0",
        "model": "local-demo",
        "prompt_version": "prompt-v1",
        "config": {"trials": 3},
        "code_version": "abc123",
        "environment": {"python": "3.x"},
        "timestamp": "2026-10-26T00:00:00Z",
        "results": {"score": 0},
    }


class AuditRecordTests(unittest.TestCase):
    def test_empty_record_reports_all_fields_missing(self):
        report = audit_record({})
        self.assertEqual(report["missing_count"], len(REQUIRED_FIELDS))
        self.assertEqual(report["completeness_percent"], 0.0)
        self.assertEqual(report["status"], "incomplete")

    def test_complete_record_has_no_missing_fields(self):
        report = audit_record(valid_record())
        self.assertEqual(report["missing_count"], 0)
        self.assertEqual(report["completeness_percent"], 100.0)
        self.assertEqual(report["status"], "complete")

    def test_missing_field_is_named(self):
        record = valid_record()
        del record["code_version"]
        report = audit_record(record)
        missing_names = [item["field"] for item in report["missing_fields"]]
        self.assertIn("code_version", missing_names)
        self.assertEqual(report["missing_count"], 1)

    def test_empty_string_counts_as_missing(self):
        record = valid_record()
        record["model"] = ""
        self.assertEqual(audit_record(record)["missing_count"], 1)

    def test_whitespace_only_string_counts_as_missing(self):
        record = valid_record()
        record["model"] = "   "
        self.assertEqual(audit_record(record)["missing_count"], 1)

    def test_empty_list_counts_as_missing(self):
        record = valid_record()
        record["results"] = []
        self.assertEqual(audit_record(record)["missing_count"], 1)

    def test_zero_and_false_are_valid_present_values(self):
        record = valid_record()
        record["results"] = {"score": 0, "passed": False}
        self.assertEqual(audit_record(record)["missing_count"], 0)

    def test_non_dictionary_raises_type_error(self):
        with self.assertRaises(TypeError):
            audit_record("not a record")


if __name__ == "__main__":
    unittest.main()
