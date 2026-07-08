---
index: 4
module: module_2
task: lab_02_05_unknown_characters
previous: lab_02_04_decoding_tokens
next: lab_02_06_saving_loading_tokenizer
---

# Lab 02.5: Unknown Characters

## Objective

Handle characters that are not in the tokenizer vocabulary.

## Introduction

A tokenizer may see a character that was not present in the training text. This is called an unknown character.

For this beginner tokenizer, we will use a special token:

```text
<UNK>
```

If a character is unknown, encode it as the id of `<UNK>`.

## Python Tools Used

- `dict.get(key, default)` returns `default` when the key is missing. Docs: https://docs.python.org/3/library/stdtypes.html#dict.get
- List concatenation such as `[UNK] + sorted(...)` builds a new list. Docs: https://docs.python.org/3/tutorial/introduction.html#lists
- A constant-style name such as `UNK = "<UNK>"` gives a clear name to a special value. Docs: https://peps.python.org/pep-0008/#constants

## Assignment

Add `<UNK>` to the vocabulary and update `encode` so unknown characters do not crash the program.

Print the encoded result for text that contains at least one unknown character.

## Conclusion

Your tokenizer can now handle text that contains characters outside the original vocabulary.
