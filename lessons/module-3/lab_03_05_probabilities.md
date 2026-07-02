---
index: 6
module: module_3
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

![A small directed probability graph](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/images/commons/markov-chain-weather-graph.png)

*Image source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Markov_Chain_weather_model_matrix_as_a_graph.png), Pmdusso, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).*

Each outgoing arrow from a state has a probability. For a character language model, one row of the probability matrix contains all outgoing probabilities for one current character.

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
