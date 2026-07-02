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

## Assignment

Implement:

```python
build_stats(text)
```

Then print the resulting dictionary.

## Conclusion

You can now describe a text dataset in a structured way.
