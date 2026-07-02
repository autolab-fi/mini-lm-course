---
index: 1
module: module_1
task: lab_02_character_tokenizer
previous: lab_01_dataset_preparation
next: lab_03_01_intro_to_character_lm
---

# Lab 02: Character Tokenizer

## Objective

Understand how text becomes a sequence of integer token ids and how those ids can be decoded back to text.

## Introduction

Models work with numbers. A tokenizer converts text into numbers.

In this course, we start with a character tokenizer. Every unique character gets one integer id.

Example:

```text
"a" -> 0
"b" -> 1
" " -> 2
```

## Required API

Implement:

```python
encode(text: str) -> list[int]
decode(tokens: list[int]) -> str
save_tokenizer(path: str) -> None
load_tokenizer(path: str) -> Tokenizer
```

## Required Artifacts

Your program must create:

```text
tokenizer.json
tokenizer_report.json
```

## `tokenizer.json` Suggested Format

```json
{
  "vocab": ["\n", " ", "a", "b"],
  "char_to_id": {
    "\n": 0,
    " ": 1,
    "a": 2,
    "b": 3
  }
}
```

## Checks

The checker will verify that:

- `encode` returns a list of integers;
- `decode(encode(text)) == text` for known text;
- newline, punctuation, and empty string cases work;
- unknown characters are handled or documented;
- `tokenizer.json` is valid JSON.

## Submission Notes

Keep the vocabulary order stable. The next lab will use a similar mapping to build a bigram count matrix.
