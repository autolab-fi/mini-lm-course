# Lab 04: Neural Char LM

## Objective

Понять training loop, loss, optimizer, validation и checkpoint.

## Task

Обучите маленькую neural character language model:

```text
character id -> embedding -> GRU/RNN -> linear -> next character logits
```

Модель должна обучаться на prepared character dataset и сохранять checkpoint для следующих лабораторных.

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

Grader будет проверять:

- training starts and completes within timeout;
- `train_loss_final < train_loss_initial`;
- `val_loss` is finite;
- `model.pt` exists and is not too large;
- generated samples are non-empty.

## Submission Notes

Держите модель маленькой. Цель этой лабораторной - понять training loop, а не добиться высокого качества текста.
