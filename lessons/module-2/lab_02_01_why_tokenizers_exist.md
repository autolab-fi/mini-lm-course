---
index: 0
module: module_2
task: lab_02_01_why_tokenizers_exist
previous: lab_01_07_final_dataset_submission
next: lab_02_02_character_vocabulary
---

# Lab 02.1: Why Tokenizers Exist

## Objective

Understand why language models need tokenizers.

## Introduction

Models work with numbers. Text is made of characters. A tokenizer is the bridge between them.

In this course, we start with a character tokenizer:

```text
"a" -> 0
"b" -> 1
" " -> 2
```

The tokenizer must also be able to turn token ids back into text.

## Theory

### Encoding and Decoding

Encoding converts text to integers:

```text
"ab" -> [0, 1]
```

Decoding converts integers back to text:

```text
[0, 1] -> "ab"
```

## Python Tools Used

- A dictionary maps keys to values, for example `{"a": 0}`. Docs: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- A list comprehension such as `[char_to_id[char] for char in text]` builds a list from a loop. Docs: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- `"".join(parts)` joins decoded characters back into one string. Docs: https://docs.python.org/3/library/stdtypes.html#str.join

## Assignment

Use a small hand-written mapping and print:

1. the original text;
2. the encoded token ids;
3. the decoded text.

## Conclusion

You have seen the basic purpose of a tokenizer: text in, numbers out, and text back again.
