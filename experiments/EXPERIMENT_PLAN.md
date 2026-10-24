# First experiment plan

## Purpose
Validate that a local experiment can record repeated outcomes consistently and summarize them. This initial plumbing test will not, by itself, establish AI-agent reliability or prove novelty.

## Proposed approach
Use a small controlled local task, run it repeatedly, record each outcome and elapsed time, and calculate a summary.

## Fields to evaluate
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
5. What specific gap could EvalProof address?

This is a plan only. The runner and tests have not been implemented yet.
