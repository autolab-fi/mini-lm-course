---
index: 0
module: module_0
task: course_overview
next: lab_01_01_what_is_text_dataset
---

# Mini Language Model Course

## Objective

Understand the full learning path of the course and how the automatic checker will work.

## Course Path

In this course, you will build a small language model step by step:

```text
dataset -> tokenizer -> baseline LM -> neural LM -> evaluation -> generation -> deployment/demo -> feedback
```

Each lab adds one new idea. You will not start with a large machine learning library. First, you will build the basic pieces in plain Python so that the model behavior is visible.

## What You Will Build

1. A prepared text dataset with train, validation, and test splits.
2. A character tokenizer that converts text to token ids and back.
3. A bigram character language model without neural networks.
4. A small neural character language model.
5. A generation script with prompt and temperature controls.
6. An evaluation report comparing the baseline and neural model.
7. A simple inference demo.
8. An edge demo with latency and memory measurements.

## How Checks Work

Most assignments ask you to write Python code in the browser editor. When you click the check button, the platform runs your code automatically.

Your code should create required output files called artifacts. The checker reads those artifacts and returns:

- score;
- passed and failed checks;
- feedback;
- stdout and stderr logs.

For example, `Lab 03` asks your program to create:

```text
bigram_counts.json
metrics.json
samples.json
```

## Current Development Status

The first working worker/grader prototype is implemented for:

```text
Lab 03: Bigram Character Language Model
```

That prototype can run a student submission locally, collect artifacts, grade them, and produce a structured `result.json`.
