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

## Assignment

Implement:

```python
split_text(text, train_ratio=0.8, val_ratio=0.1)
```

Print the number of characters in every split.

## Conclusion

You now have separate text splits for training and evaluation.
