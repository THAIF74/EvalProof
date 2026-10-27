# EvalProof

**Status:** Day 3 — metadata auditing and a basic repeated-evaluation runner implemented.

EvalProof explores whether a lightweight workflow can make AI evaluation records easier to inspect, compare, and reproduce.

## Problem hypothesis

Evaluation results can be difficult to compare when task versions, configuration, runtime details, and other experiment metadata are recorded inconsistently.

Existing tools already support evaluation tracking and experiment logging. EvalProof's potential differentiation remains unproven.

## Current prototype

### 1. Metadata audit
`src/audit.py` checks ten required metadata fields and reports missing fields, a completeness percentage, and limitations.

### 2. Repeated-evaluation runner
`src/repeatability.py` runs an evaluator multiple times and summarizes:
- Individual trial scores
- Mean score
- Minimum and maximum scores
- Score range

The current demo uses a fixed score of 0.8 across three trials. It validates the runner's basic workflow, not the reliability of a real AI model.

## Run the examples

Metadata audit:

`python -m examples.run_audit`

Repeated-evaluation demo:

`python -m examples.run_experiment`

The repeated-evaluation report is written to `results/repeatability_demo.json`.

## Run the tests

`python -m unittest discover -s tests -v`

The suite covers metadata validation and repeated-run score summaries, including invalid trial counts and invalid scores.

## Limitations

- Metadata completeness does not guarantee reproducibility.
- Field presence does not verify value accuracy.
- Required metadata fields are an initial prototype policy, not an established standard.
- The demo evaluator is deterministic and does not call a real AI model.
- The runner does not control evaluator randomness or the execution environment.
- A score range of zero in this demo does not establish AI reliability.
- Novelty and practical value compared with existing tools remain unproven.

## Project structure

- `src/audit.py` — metadata audit logic.
- `src/repeatability.py` — repeated-run score summaries.
- `tests/` — automated tests.
- `examples/run_audit.py` — metadata audit example.
- `examples/run_experiment.py` — repeated-evaluation demo.
- `experiments/EXPERIMENT_PLAN.md` — experiment plan and open questions.
- `docs/EXISTING_TOOLS.md` — initial existing-tool comparison.
- `results/` — generated reports.
- `progress.md` — day-by-day progress.

## Roadmap

1. Improve experiment records with useful run metadata.
2. Record elapsed time and execution details.
3. Decide how failed trials should be represented.
4. Test with a meaningful evaluation task.
5. Compare the workflow with existing tools and assess whether a genuine gap exists.
