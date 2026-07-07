---
index: 10
module: module_4
task: lab_04_neural_char_lm
previous: lab_03_08_final_submission
next: lab_05_generation_and_sampling
---

# Lab 04: Tiny Neural Char LM

## Objective

Understand the training loop, loss, parameter updates, validation, and checkpoint saving for a small neural character language model.

This first neural lab uses a dependency-free model that can run on CPU inside the current worker:

```text
character id -> embedding -> linear logits -> softmax
```

This is intentionally simpler than an RNN or GRU. A later extension can replace the linear output model with a recurrent layer after the worker image includes the needed ML libraries.

## Module Breakdown

This lab should be taught as a sequence of smaller lessons:

```text
04.1 Why a Neural LM?
04.2 Turning Text Into Training Examples
04.3 Model Configuration and Parameters
04.4 Forward Pass, Softmax, and Loss
04.5 Training Loop
04.6 Validation Loss and Perplexity
04.7 Sampling From the Neural Model
04.8 Final Neural Char LM Submission
```

See `lab_04_lessons_plan.md` for the detailed lesson-by-lesson plan.

## Task

Train a small model with this structure:

```text
character id -> embedding -> linear logits -> softmax probabilities
```

The model should train on the prepared character dataset and save a checkpoint for later generation and evaluation labs.

## Required Artifacts

```text
model.pt
config.yaml
metrics.json
samples.json
loss_curve.png
```

## `metrics.json` Suggested Fields

```json
{
  "train_loss_initial": 4.1,
  "train_loss_final": 2.8,
  "val_loss": 2.95,
  "perplexity": 19.1,
  "num_parameters": 2145,
  "training_time_sec": 5.4
}
```

## Checks

The checker will verify that:

- training starts and completes within the timeout;
- `train_loss_final < train_loss_initial`;
- `val_loss` is finite;
- `model.pt` exists and is not too large;
- generated samples are not empty.

## Submission Notes

Keep the model small. The goal of this lab is to understand the training loop, not to produce perfect text.

Do not use PyTorch, TensorFlow, or external downloads in the current version of this lab. Use the Python standard library so the checker can run the submission in the existing worker environment.
