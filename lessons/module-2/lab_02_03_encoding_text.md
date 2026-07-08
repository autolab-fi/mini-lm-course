---
index: 2
module: module_2
task: lab_02_03_encoding_text
previous: lab_02_02_character_vocabulary
next: lab_02_04_decoding_tokens
---

# Lab 02.3: Encoding Text

## Objective

Convert text into a list of integer token ids.

## Introduction

Encoding is a lookup operation. For every character in the input text, find its integer id.

Example:

```text
text = "cab"
c -> 2
a -> 0
b -> 1
encoded = [2, 0, 1]
```

## Python Tools Used

- `for char in text` loops through a string one character at a time. Docs: https://docs.python.org/3/tutorial/controlflow.html#for-statements
- A list comprehension creates the encoded token list. Docs: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- `dict[key]` reads a value from a dictionary and raises an error if the key is missing. Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Assignment

Implement:

```python
encode(text, char_to_id)
```

Requirements:

1. Return a list.
2. Every item must be an integer.
3. The encoded list length must match the text length.

## Conclusion

You can now convert known text into model-friendly numbers.
