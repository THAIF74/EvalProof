# EvalProof progress log

## Day 1 — problem definition and research

- Defined the problem hypothesis and first-version boundaries.
- Documented an initial comparison with LangSmith, MLflow, and Inspect AI.
- Created the experiment plan and project structure.
- Confirmed Python 3.14.8 and the project virtual environment.
- Recorded that novelty and differentiation remain unproven.
- Committed and pushed Day 1 work in separate commits.

## Day 2 — initial metadata-audit prototype

### Implemented
- Added `src/audit.py` with ten required metadata fields.
- Added a completeness percentage and a list of missing fields.
- Added explicit limitations to the generated report.
- Added `examples/run_audit.py`.
- Added eight tests in `tests/test_audit.py`.

### Validation
- All eight metadata-audit tests passed.
- The metadata-audit example had previously run successfully.
- Blank strings and empty collections count as missing.
- Zero and false remain valid present values.

## Day 3 — repeated-evaluation runner

### Implemented
- Added `src/repeatability.py` to run an evaluator multiple times.
- Added mean, minimum, maximum, and score-range summaries.
- Added input validation for trial counts and scores.
- Added six tests in `tests/test_repeatability.py`.
- Added `examples/run_experiment.py` to generate a JSON report.
- Updated the README and experiment plan.

### Validation
- All 14 unit tests passed: eight audit tests and six repeatability tests.
- The repeated-evaluation example ran successfully using `python -m examples.run_experiment`.
- The demo generated `results/repeatability_demo.json`.
- The deterministic demo returned a mean score of 0.8 and a score range of 0.0.
- `git diff --check` passed before the documentation update.

### Remaining work
- Re-run tests and examples after the documentation update.
- Review and commit Day 3 changes.
- Push the commit and verify the working tree.
- Improve run metadata and test a meaningful evaluation task.

## Research caveat

The prototype checks metadata completeness and summarizes repeated scores. It does not establish reproducibility or AI-system reliability. Its originality and practical advantage over existing tools remain unproven.

### Follow-up validation

- Re-ran all 14 tests successfully after the documentation update.
- Confirmed the metadata-audit example generates `results/sample_audit.json`.
- Confirmed the repeated-evaluation example generates `results/repeatability_demo.json`.
- Confirmed `git diff --check` passes and the working tree is clean.
- Installed pytest in the local virtual environment for validation.
