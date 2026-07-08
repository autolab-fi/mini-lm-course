---
index: 1
module: module_2
task: lab_02_02_character_vocabulary
previous: lab_02_01_why_tokenizers_exist
next: lab_02_03_encoding_text
---

# Lab 02.2: Character Vocabulary

## Objective

Build a stable character vocabulary from text.

## Introduction

A character tokenizer needs a list of known characters. This list is called the vocabulary.

The order must be stable, because every character receives an id based on its position.

<figure style="background: #ffffff; padding: 16px; border-radius: 6px; border: 1px solid #e5e7eb;">
  <img src="https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/images/commons/ascii-code-chart.svg" alt="ASCII code chart showing characters and numeric codes" style="display: block; width: 100%; height: auto;">
</figure>

*Image source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:ASCII_Code_Chart.svg), Anomie, public domain.*

The chart shows a historical example of the same idea: characters can be represented by numbers. In this lab, you will create a smaller course-specific mapping from the characters in your training text to ids.

## Theory

Use:

```python
vocab = sorted(set(text))
char_to_id = {char: index for index, char in enumerate(vocab)}
id_to_char = {index: char for index, char in enumerate(vocab)}
```

## Python Tools Used

- `set(text)` removes duplicate characters. Docs: https://docs.python.org/3/library/functions.html#set
- `sorted(...)` returns a stable sorted list. Docs: https://docs.python.org/3/library/functions.html#sorted
- `enumerate(vocab)` gives both the index and the character. Docs: https://docs.python.org/3/library/functions.html#enumerate
- A dictionary comprehension creates mappings in one expression. Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Assignment

Implement:

```python
build_vocabulary(text)
```

Print the vocabulary size, vocabulary list, and `char_to_id` dictionary.

## Conclusion

You now have the lookup tables needed for encoding and decoding.
