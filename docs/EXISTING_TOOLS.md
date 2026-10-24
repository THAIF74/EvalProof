# Existing-tool comparison — Day 1

## LangSmith
Official documentation:
https://docs.langchain.com/langsmith/evaluation

Relevant existing capabilities:
- Dataset-based evaluations
- Repeated evaluations and experiment comparisons
- Recording evaluator feedback and run metadata

Implication:
Basic evaluation tracking and comparison are not unique to EvalProof.

## MLflow
Official documentation:
https://mlflow.org/docs/latest/tracking/

Relevant existing capabilities:
- Experiment and run tracking
- Parameters, metrics, timestamps, and artifacts
- Dataset and code-related tracking features

Implication:
Basic experiment metadata and metric logging are not unique.

## Inspect AI
Official documentation:
https://inspect.aisi.org.uk/eval-logs.html

Relevant existing capabilities:
- Structured evaluation logs
- Results, samples, model configuration, usage statistics, and errors
- Tools for inspecting and retrying evaluations

Implication:
Evaluation logging and error recording are not unique.

## Current conclusion
EvalProof is not yet proven novel. A possible direction to investigate is a small, framework-independent reproducibility audit that checks whether an evaluation contains sufficient information to repeat it, identifies missing metadata, and compares repeated-run variation.

This direction is only a hypothesis. We still need a feature-by-feature comparison and a working prototype before claiming a meaningful gap.

## Sources checked
- LangSmith official documentation
- MLflow official documentation
- Inspect AI official documentation

## Research update — 25 October 2026

Official documentation checked:
- LangSmith supports repeated evaluation runs.
- MLflow tracks run parameters, metrics, metadata, and artifacts.
- Inspect AI records structured evaluation logs, results, and errors.

Conclusion:
Basic evaluation logging, experiment tracking, and repeated runs already exist. EvalProof must not claim these features as novel.

Next hypothesis to investigate:
A framework-independent audit that checks whether an evaluation records enough information to reproduce it, flags missing fields, and reports repeat-run variation. This is not yet proven to be a unique or valuable gap.
