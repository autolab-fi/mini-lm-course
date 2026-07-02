---
index: 12
module: module_1
task: lab_06_evaluation
previous: lab_05_generation_and_sampling
next: lab_07_deployment_cli_api_demo
---

# Lab 06: Evaluation

## Objective

Understand validation loss, perplexity, overfitting, and comparison between a baseline and a neural model.

## Task

Compare the bigram baseline from `Lab 03` with the neural character LM from `Lab 04`.

Use validation or test text to calculate metrics and explain whether the neural model improves over the baseline.

## Required Artifacts

```text
evaluation.json
comparison_table.md
```

## Checks

The checker will verify that:

- perplexity is calculated as `exp(loss)`;
- baseline and neural model results are compared;
- overfitting is discussed;
- model parameter count and training time are reported.

## Submission Notes

A good result is not only a lower loss. A good result also explains the tradeoffs between the simple baseline and the neural model.
