# Lab 06: Evaluation

## Objective

Понять validation loss, perplexity, overfitting и сравнение baseline vs neural model.

## Task

Сравните bigram baseline из `Lab 03` и neural character LM из `Lab 04`. Посчитайте метрики на validation/test split и объясните, где модель переобучается или недообучается.

## Required Artifacts

```text
evaluation.json
comparison_table.md
```

## Checks

Grader будет проверять:

- perplexity is calculated as `exp(loss)`;
- baseline and neural model are compared;
- overfitting is discussed;
- model parameters and training time are reported.

## Submission Notes

Хороший результат здесь - не только lower loss, но и понятное объяснение tradeoffs между baseline и neural model.
