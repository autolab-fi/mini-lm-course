---
index: 4
module: module_1
task: lab_01_05_dataset_statistics
previous: lab_01_04_splitting_dataset
next: lab_01_06_writing_artifacts
---

# Lab 01.5: Dataset Statistics

## Objective

Compute basic statistics for a text dataset.

## Introduction

A dataset should be described. Simple statistics help you understand what the model will see.

For this course, the required statistics are:

```text
num_chars
num_lines
vocab_chars
```

## Theory

### Unique Characters

The character vocabulary is:

```python
sorted(set(text))
```

This includes spaces and newline characters.

## Python Tools Used

- A Python `dict` stores named values such as `{"num_chars": 42}`. Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- `sorted(set(text))` creates a stable list of unique characters. Docs: https://docs.python.org/3/library/functions.html#sorted
- `len(...)` works on strings, lists, and many other containers. Docs: https://docs.python.org/3/library/functions.html#len

## Assignment

Implement:

```python
build_stats(text)
```

Then print the resulting dictionary.

## Conclusion

You can now describe a text dataset in a structured way.
