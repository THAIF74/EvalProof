# EvalProof

**Status:** Day 2 — initial metadata-audit prototype implemented.

EvalProof explores whether a lightweight workflow can make AI evaluation records easier to inspect and reproduce.

## Problem hypothesis

Evaluation results can be difficult to compare when task versions, configuration, runtime details, and other experiment metadata are recorded inconsistently.

Existing tools already support evaluation tracking and experiment logging. EvalProof's potential differentiation remains unproven.

## Current prototype

The audit checks ten required metadata fields covering experiment identity, task and prompt versions, model, configuration, code version, environment, timestamp, and results.

It reports missing fields, a completeness percentage, and limitations.

## Run the example

Command: `python -m examples.run_audit`

## Run the tests

Command: `python -m unittest discover -s tests -v`

The tests cover complete and empty records, missing fields, blank strings, empty lists, zero and false values, and invalid input types.

## Limitations

- Metadata completeness does not guarantee reproducibility.
- Field presence does not verify value accuracy.
- Required fields are an initial prototype policy, not an established standard.
- Repeated-run variation analysis is not implemented.
- No AI model integration or benchmark results are claimed.
- Novelty and practical value remain unproven.

## Project structure

- `src/audit.py` — metadata audit logic.
- `tests/` — automated tests.
- `examples/` — runnable example.
- `experiments/EXPERIMENT_PLAN.md` — planned experiment.
- `docs/EXISTING_TOOLS.md` — initial existing-tool comparison.
- `results/` — generated reports.
- `progress.md` — day-by-day progress.

## Roadmap

1. Refine metadata validation.
2. Build a controlled local repeated-run experiment.
3. Summarize variation across trials.
4. Export structured results.
5. Compare against existing tools and assess whether a meaningful gap exists.
