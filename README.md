# EvalProof

**Status:** Day 1 — problem definition and setup  
**Working concept:** Reproducibility and transparency for AI-agent evaluations.

## Problem hypothesis

AI-agent evaluation results can be difficult to compare when settings, task versions, repeated-trial results, runtime, and execution details are recorded inconsistently.

EvalProof will investigate whether a lightweight workflow can make those details easier to capture and compare. This is a hypothesis, not a claim that existing tools cannot already do it.

## Initial goals

1. Record experiment configuration and software/runtime metadata.
2. Store trial outcomes and elapsed time consistently.
3. Repeat experiments and summarize variation.
4. Export machine-readable results.
5. Test the calculations automatically.

## First-version boundaries

- Start with a controlled local experiment; no paid model API required.
- Do not claim universal reproducibility.
- Do not claim uniqueness until existing tools have been compared.
- Do not claim working features before they are implemented and tested.

## Day 1 checklist

- [x] Project folder and virtual environment exist.
- [x] Initial directory structure exists.
- [ ] Problem hypothesis and scope documented.
- [ ] Existing-tool comparison researched.
- [ ] Git repository initialized and Day 1 commit created.

## Project structure

- `experiments/` — experiment plan and runner.
- `results/` — generated output.
- `tests/` — automated tests.
- `docs/` — research notes.
- `progress.md` — day-by-day progress.

## Current status

The project is at the problem-definition stage. No working runner, benchmark results, or proven novelty is claimed yet.
