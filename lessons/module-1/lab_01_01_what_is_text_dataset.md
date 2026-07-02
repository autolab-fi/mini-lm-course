---
index: 0
module: module_1
task: lab_01_01_what_is_text_dataset
previous: course_overview
next: lab_01_02_reading_raw_text
---

# Lab 01.1: What Is a Text Dataset?

## Objective

Understand what a text dataset is and why a language model needs one.

## Introduction

A language model learns from examples of text. Before we build a tokenizer or a model, we need a clean text corpus.

In this course, a dataset is just text split into files:

```text
train.txt
val.txt
test.txt
```

The model learns from `train.txt`. We use `val.txt` and `test.txt` to check how well the model works on text it did not train on.

## Theory

### Characters, Lines, and Vocabulary

Even a simple text file has useful information:

- number of characters;
- number of lines;
- unique characters used in the text.

The unique characters are important because later we will build a character tokenizer and a character language model.

## Assignment

Use the starter text and print:

1. the text itself;
2. the number of characters;
3. the number of lines;
4. the sorted list of unique characters.

## Conclusion

You have inspected the basic pieces of a text dataset.
