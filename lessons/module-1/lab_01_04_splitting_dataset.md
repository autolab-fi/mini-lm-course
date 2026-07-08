---
index: 3
module: module_1
task: lab_01_04_splitting_dataset
previous: lab_01_03_cleaning_text
next: lab_01_05_dataset_statistics
---

# Lab 01.4: Splitting Train, Validation, and Test

## Objective

Split cleaned text into training, validation, and test parts.

## Introduction

We do not evaluate a model on the same text it trained on. That would make the result too optimistic.

We use three splits:

- `train`: text used for learning;
- `val`: text used while developing the model;
- `test`: text kept for the final check.

## Theory

### Simple Character-Based Split

For a small beginner dataset, we can split by character count:

```text
80% train
10% validation
10% test
```

This is simple and good enough for the first lab.

## Python Tools Used

- `int(value)` converts a number to an integer. Docs: https://docs.python.org/3/library/functions.html#int
- `text[:index]`, `text[start:end]`, and `text[index:]` are string slices. Docs: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
- Default function arguments such as `train_ratio=0.8` provide values when the caller does not pass them. Docs: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

## Assignment

Implement:

```python
split_text(text, train_ratio=0.8, val_ratio=0.1)
```

Print the number of characters in every split.

## Conclusion

You now have separate text splits for training and evaluation.
