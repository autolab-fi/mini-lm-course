---
index: 11
module: module_4
task: lab_05_generation_and_sampling
previous: lab_04_neural_char_lm
next: lab_06_evaluation
---

# Lab 05: Generation and Sampling

## Objective

Understand prompt, `max_new_tokens`, temperature, and stochastic sampling.

## Task

Implement a command-line generation script that loads the checkpoint from `Lab 04`.

Expected command:

```bash
python3 generate.py --prompt "the robot" --max-new-tokens 100 --temperature 0.8
```

## Required Artifacts

```text
samples.json
generation_report.md
```

## Checks

The checker will verify that:

- `generate.py` accepts a prompt;
- the checkpoint loads without retraining;
- outputs are not empty;
- latency is reported;
- low and high temperature outputs are compared.

## Submission Notes

In the report, briefly explain how generated text changes when temperature is low or high.
