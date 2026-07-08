---
index: 7
module: module_3
task: lab_03_06_validation_loss
previous: lab_03_05_probabilities
next: lab_03_07_text_generation
---

# Lab 03.6: Validation Loss and Perplexity

## Objective

Measure how well the bigram model predicts validation text.

## Introduction

Training counts are not enough. We need a number that tells us how good the model is on text it did not train on.

For each validation pair:

```text
current_char -> real_next_char
```

we ask the model:

```text
What probability did you give to the real next character?
```

If the probability is high, the model did well. If the probability is low, the model was surprised.

## Theory

### Negative Log Likelihood

Loss for one prediction:

```text
-log(probability_of_real_next_character)
```

Average validation loss:

```text
average loss over all validation pairs
```

### Perplexity

Perplexity is another way to read the same result:

```text
perplexity = exp(loss)
```

Lower loss and lower perplexity usually mean better predictions.

## Python Tools Used

- `math.log(x)` computes the natural logarithm. Docs: https://docs.python.org/3/library/math.html#math.log
- `math.exp(x)` computes `e ** x`, used for perplexity. Docs: https://docs.python.org/3/library/math.html#math.exp
- `list.append(value)` adds one loss value to a list. Docs: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

## Assignment

Implement:

```python
compute_val_loss(text, counts, char_to_id)
```

Then compute:

```python
perplexity = math.exp(val_loss)
```

Requirements:

1. Use `row_probabilities`.
2. Skip validation pairs that contain unknown characters.
3. Return one average loss number.
4. Print validation loss and perplexity.

## Conclusion

You can now evaluate a language model with a real metric.
