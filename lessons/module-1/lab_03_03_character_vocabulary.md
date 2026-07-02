---
index: 4
module: module_1
task: lab_03_03_character_vocabulary
previous: lab_03_02_reading_dataset
next: lab_03_04_bigram_counts
---

# Lab 03.3: Building a Character Vocabulary

## Objective

Build a list of unique characters and assign an integer id to each character.

## Introduction

A count matrix cannot use characters directly as row and column numbers. We need integer ids.

Example:

```text
"\n" -> 0
" "  -> 1
"a"  -> 2
"b"  -> 3
```

This mapping is called a vocabulary.

## Theory

### Unique Characters

`set(text)` gives the unique characters in a string. `sorted(...)` gives them a stable order.

```python
vocab = sorted(set(text))
```

### Character to Id

A dictionary lets us find the id for a character quickly:

```python
char_to_id = {"a": 0, "b": 1}
print(char_to_id["a"])
```

### Why Stable Order Matters

The checker will compare `vocab`, `char_to_id`, and `counts`. If the order changes randomly, your output becomes harder to understand. Sorting the vocabulary keeps it stable.

## Assignment

Implement `build_vocab(text)`.

Requirements:

1. Return `vocab` as a non-empty list of strings.
2. Return `char_to_id` as a dictionary.
3. Ids must start at `0`.
4. Ids must be contiguous: `0, 1, 2, ...`.

## Conclusion

You now have the index system that the count matrix will use.
