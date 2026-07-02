---
index: 6
module: module_1
task: lab_03_05_probabilities
previous: lab_03_04_bigram_counts
next: lab_03_06_validation_loss
---

# Lab 03.5: From Counts to Probabilities

## Objective

Convert raw counts into probabilities for next-character prediction.

## Introduction

Counts tell us how many times something happened. Probabilities tell us how likely it is.

For one current character, the model has one row of counts:

```text
[0, 4, 1, 0]
```

To sample or score the next character, we convert this row into probabilities.

## Theory

### Normalization

Each count is divided by the total row count:

```text
probability = count / row_sum
```

The probabilities in one row should add up to about `1.0`.

### Add-One Smoothing

Some character pairs may never appear in the training text. Without smoothing, their probability would be zero. That would break validation loss because `log(0)` is impossible.

We use add-one smoothing:

```text
probability = (count + 1) / (row_sum + vocab_size)
```

This gives every possible next character a small non-zero probability.

## Assignment

Implement:

```python
row_probabilities(row)
```

Requirements:

1. Use add-one smoothing.
2. Return a list of probabilities.
3. The list length must match the row length.
4. The sum of probabilities should be close to `1.0`.

## Conclusion

The model can now answer: "Given this current character, how likely is each possible next character?"
