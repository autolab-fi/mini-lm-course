---
index: 0
module: module_1
task: lab_01_dataset_preparation
previous: course_overview
next: lab_02_character_tokenizer
---

# Lab 01: Dataset Preparation

## Objective

Understand that a language model learns from a text corpus, then prepare train, validation, and test splits.

## Introduction

A language model cannot learn without data. In this lab, you prepare the text files that later labs will use.

The goal is not to collect a huge dataset. The goal is to make a clean, simple dataset with a clear structure.

## Task

Write Python code that:

1. Reads a raw text file.
2. Normalizes the text as UTF-8.
3. Splits the text into `train.txt`, `val.txt`, and `test.txt`.
4. Counts basic statistics.
5. Writes a short dataset description.

## Required Artifacts

Your program must create:

```text
train.txt
val.txt
test.txt
stats.json
dataset_card.md
```

## `stats.json` Minimum Format

```json
{
  "num_chars": 100000,
  "num_lines": 1200,
  "vocab_chars": ["\n", " ", "a"]
}
```

## Checks

The checker will verify that:

- required files exist;
- text files are valid UTF-8;
- split files are not empty;
- the train split is larger than validation and test splits;
- `stats.json` contains `num_chars`, `num_lines`, and `vocab_chars`;
- split files do not fully overlap.

## Submission Notes

Save output files in the current working directory. Do not download external data during the check.
