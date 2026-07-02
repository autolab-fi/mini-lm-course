---
index: 3
module: module_3
task: lab_03_02_reading_dataset
previous: lab_03_01_intro_to_character_lm
next: lab_03_03_character_vocabulary
---

# Lab 03.2: Reading the Dataset

## Objective

Read the training and validation text files that the checker provides.

## Introduction

The model needs text data. During automatic checking, the dataset is available in a read-only directory:

```text
/datasets/toy_chars_100kb/
```

For local development, the worker may provide a different dataset root through an environment variable:

```text
DATASETS_DIR
```

The starter code supports both cases.

## Theory

### Paths with `pathlib`

Python's `Path` object helps you build file paths without manually writing slashes.

```python
from pathlib import Path

folder = Path("/datasets") / "toy_chars_100kb"
train_path = folder / "train.txt"
```

### Reading UTF-8 Text

Always read course text files with UTF-8 encoding:

```python
text = train_path.read_text(encoding="utf-8")
```

### Train and Validation Splits

We use:

- `train.txt` to count patterns;
- `val.txt` to measure how well the model predicts unseen text.

## Assignment

Read `train.txt` and `val.txt`, then print:

1. number of characters in training text;
2. number of characters in validation text;
3. first 200 characters of training text.

## Conclusion

You can now load the text that the bigram model will learn from.
