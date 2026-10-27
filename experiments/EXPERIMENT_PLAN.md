# First experiment plan

## Purpose

Test whether a local workflow can record repeated outcomes and summarize score variation consistently. This initial plumbing test does not establish AI-agent reliability or prove project novelty.

## Current implementation

`src/repeatability.py` provides `run_trials(evaluator, trials=3)`. It runs a callable repeatedly, validates that each score is numeric and between 0 and 1, and returns the individual scores, mean, minimum, maximum, and score range.

`examples/run_experiment.py` demonstrates the workflow using a fixed score of 0.8. Its report is saved to `results/repeatability_demo.json`.

## Current validation

- The repeated-run example completed successfully.
- All 14 unit tests passed: 8 metadata-audit tests and 6 repeatability tests.
- The fixed-score example produced a mean of 0.8 and a score range of 0.0.

These results verify basic program behavior only. They are not benchmark results from a real AI model.

## Proposed next experiment

Use a meaningful local evaluation task and record enough information to understand each run.

Potential fields:
- Experiment ID
- Task ID and task-set version
- Trial number
- Configuration
- Python version and platform
- Timestamp and elapsed time
- Outcome or score
- Error details, if any

## Research questions

1. Which fields are essential for reproducibility?
2. Should output use JSON or JSONL?
3. How should failed trials be represented?
4. Which existing tools already capture these fields?
5. What specific gap, if any, could EvalProof address?

## Limitations

The current runner does not control evaluator randomness or the environment. Repeated scores alone do not prove reproducibility. The fixed demo evaluator is not an AI model benchmark, and project novelty remains unverified.
