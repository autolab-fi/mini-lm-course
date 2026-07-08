---
index: 5
module: module_3
task: lab_03_04_bigram_counts
previous: lab_03_03_character_vocabulary
next: lab_03_05_probabilities
---

# Lab 03.4: Counting Bigrams

## Objective

Count how often each character follows each other character.

## Introduction

The bigram model stores counts in a square matrix:

```text
counts[current_char_id][next_char_id]
```

Rows represent the current character. Columns represent the next character.

If `counts[3][7] == 12`, that means:

```text
character with id 7 appeared after character with id 3 twelve times
```

![A Markov chain transition matrix shown as connected states](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/images/commons/markov-chain-matrix.svg)

*Image source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Markov_chain_SVG.svg), IkamusumeFan, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0).*

The diagram connects two equivalent views: a table of transition values and arrows between states. Your `counts` matrix is the table form. Later, probabilities turn those counts into transition weights.

## Theory

### Empty Matrix

For a vocabulary of size `vocab_size`, the matrix must have:

```text
vocab_size rows
vocab_size columns in every row
```

### Updating Counts

For every neighboring pair, convert both characters to ids and update the matrix:

```python
current_id = char_to_id[current_char]
next_id = char_to_id[next_char]
counts[current_id][next_id] += 1
```

## Python Tools Used

- A nested list such as `[[0 for _ in range(vocab_size)] for _ in range(vocab_size)]` creates a matrix. Docs: https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
- `range(vocab_size)` creates a sequence of indexes. Docs: https://docs.python.org/3/library/stdtypes.html#range
- `counts[current_id][next_id] += 1` updates one cell in a list-of-lists matrix. Docs: https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements

## Assignment

Implement:

```python
create_empty_counts(vocab_size)
count_bigrams(text, char_to_id, vocab_size)
```

Requirements:

1. `counts` must be a square list of lists.
2. Every value must be a non-negative integer.
3. Use `zip(text, text[1:])` to read neighboring pairs.
4. Print a few counts to inspect the result.

## Conclusion

You have trained the first version of the model. It does not know probabilities yet, but it has learned frequency patterns from text.
