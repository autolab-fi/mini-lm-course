---
index: 10
module: module_1
task: lab_04_neural_char_lm
previous: lab_03_08_final_submission
next: lab_05_generation_and_sampling
---

# Lab 04: Neural Char LM

## Objective

Understand the training loop, loss, optimizer, validation, and checkpoint saving for a small neural character language model.

## Task

Train a small model with this structure:

```text
character id -> embedding -> GRU/RNN -> linear -> next character logits
```

The model should train on the prepared character dataset and save a checkpoint for later labs.

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
  "num_parameters": 120000,
  "training_time_sec": 35.2
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
