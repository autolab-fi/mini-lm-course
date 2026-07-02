---
index: 1
module: module_1
task: lab_01_02_reading_raw_text
previous: lab_01_01_what_is_text_dataset
next: lab_01_03_cleaning_text
---

# Lab 01.2: Reading Raw Text

## Objective

Read raw text from a file using Python.

## Introduction

Most datasets start as files. Python can read text files with `Path.read_text()`.

Always use UTF-8 encoding in this course:

```python
text = path.read_text(encoding="utf-8")
```

## Theory

### Why Encoding Matters

Encoding is the rule used to store characters as bytes. UTF-8 supports English text, punctuation, newlines, and many other characters.

If you do not specify encoding, your program may work on one computer and fail on another.

## Assignment

Create a small `raw_text.txt` file from Python, read it back, and print:

1. `Raw characters: <number>`;
2. the first 80 characters.

## Conclusion

You can now read text data from a file.
