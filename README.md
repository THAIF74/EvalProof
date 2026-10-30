# EvalProof

**A lightweight toolkit for auditing AI evaluation metadata and analyzing repeated-run consistency.**

EvalProof explores how AI evaluation results can be made easier to inspect, compare, and reproduce by checking experiment metadata and summarizing variation across repeated trials.

> **Project status:** Early-stage prototype. Metadata auditing and a basic repeated-evaluation runner are implemented. Practical value and differentiation from existing tools remain under investigation.

## The Problem

AI evaluation results can be difficult to compare when task versions, prompt versions, model configurations, runtime environments, and other experiment details are recorded inconsistently.

EvalProof explores two related questions:

- **Evaluation traceability:** Are the essential details of an experiment recorded?
- **Evaluation consistency:** How much do scores vary across repeated runs?

Existing tools already support evaluation tracking and experiment logging. EvalProof's potential differentiation remains unproven and requires further investigation.

## Current Features

### 1. Evaluation Metadata Audit

Checks ten required metadata fields covering experiment identity, task and prompt versions, model, configuration, code version, environment, timestamp, and results.

The audit reports:
- Missing metadata fields
- Metadata completeness percentage
- Limitations identified by the audit

### 2. Repeated Evaluation Runner

Runs an evaluator multiple times and summarizes its scores.

The current implementation reports:
- Individual trial scores
- Mean score
- Minimum and maximum scores
- Score range across trials
- Trial count and known limitations

The current demonstration uses a fixed toy evaluator returning `0.8` for each trial. It validates the workflow, not the performance or consistency of a real AI model.

### 3. Structured Reports

The example workflows generate JSON reports that can be inspected or used as a starting point for further analysis.

## Getting Started

Run these commands from the project root with the project's Python environment activated.

**Run the metadata audit**

```bash
python -m examples.run_audit
```

**Run the repeated evaluation example**

```bash
python -m examples.run_experiment
```

**Run the automated tests**

```bash
python -m unittest discover -s tests -v
```

The current test suite contains 14 tests covering metadata validation and repeated-evaluation behavior.

## Project Structure

```text
EvalProof/
├── src/
│   ├── audit.py
│   └── repeatability.py
├── tests/
│   ├── ...
├── examples/
│   ├── run_audit.py
│   └── run_experiment.py
├── experiments/
│   └── EXPERIMENT_PLAN.md
├── docs/
│   └── EXISTING_TOOLS.md
├── results/
├── README.md
└── progress.md
```

Generated reports are stored in `results/`. The experiment plan and existing-tool research are maintained separately to document the project's methodology and research direction.

## Validation

The current prototype has passed its 14 automated tests.

The metadata-audit example completes successfully and produces a report. The repeated-evaluation example also completes successfully, producing three scores of `0.8`, a mean of `0.8`, and a score range of `0.0`.

These results confirm that the example workflows operate as intended. They do not establish that EvalProof improves reproducibility or offers an advantage over existing tools.

## Limitations

- Metadata completeness does not guarantee reproducibility.
- Field presence does not verify the accuracy of recorded values.
- Required metadata fields represent an initial prototype policy, not an established standard.
- A fixed toy evaluator does not demonstrate real model behavior.
- Score variation alone does not explain why results differ.
- No real AI benchmark results or proven novelty are claimed.
- Practical value and differentiation from existing tools remain to be evaluated.

## Roadmap

1. Refine metadata validation and experiment-record handling.
2. Record additional run information, including configuration and environment details.
3. Test the repeated-run workflow with a meaningful evaluation task.
4. Explore useful comparisons across trials and experiment configurations.
5. Export and inspect structured evaluation results.
6. Compare the workflow with existing evaluation tools and investigate whether a meaningful gap exists.

## Development History

- **Day 1:** Defined the project scope and researched existing tools.
- **Day 2:** Implemented the initial evaluation metadata-audit prototype.
- **Day 3:** Added a basic repeated-evaluation runner and score summaries.

---

EvalProof is an experimental project focused on making evaluation records easier to inspect and repeated-run results easier to analyze. Its usefulness and distinct contribution will be assessed through further implementation and testing.
## Experiment Comparison
EvalProof can compare two experiment records using their mean evaluation scores.
The comparison report includes:
- Baseline and candidate experiment IDs
- Baseline and candidate scores
- Score difference and absolute difference
- Configurable comparison tolerance
- Comparison status and interpretation
The comparison feature validates experiment inputs and identifies score changes beyond a configured tolerance.
Note: A score difference does not establish statistical significance or prove that one model is better.
