---
index: 2
module: module_1
task: lab_03_01_intro_to_character_lm
previous: lab_02_character_tokenizer
next: lab_03_02_reading_dataset
---

# Lab 03.1: What Is a Character Language Model?

## Objective

Understand the smallest useful language model task: predicting the next character.

## Introduction

A language model learns patterns in text. In this lab series, we will not use neural networks yet. We will build a simple baseline model from counts.

The model will read text one character at a time. For every current character, it will learn which character often comes next.

For example, the word `hello` contains these character pairs:

```text
h -> e
e -> l
l -> l
l -> o
```

A bigram character model uses only one previous character. If the current character is `h`, it asks:

```text
What character usually comes after h?
```

## Theory

### Characters as a Sequence

Python strings are sequences. You can loop over them, slice them, and compare neighboring characters.

```python
text = "hello"
print(text[0])
print(text[1:])
```

### Neighboring Pairs

The expression `zip(text, text[1:])` pairs each character with the next one.

```python
text = "hello"

for current_char, next_char in zip(text, text[1:]):
    print(current_char, "->", next_char)
```

This is the core idea of the whole lab.

## Assignment

Use the starter code to print all neighboring character pairs from a short text.

Requirements:

1. Keep the variable name `text`.
2. Use `zip(text, text[1:])`.
3. Print each pair in the form `current -> next`.
4. Try changing `text` to a different short sentence.

## Conclusion

You have seen the basic training signal for a character language model. The model will learn from many pairs like `current_char -> next_char`.
