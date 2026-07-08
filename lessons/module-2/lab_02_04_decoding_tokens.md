---
index: 3
module: module_2
task: lab_02_04_decoding_tokens
previous: lab_02_03_encoding_text
next: lab_02_05_unknown_characters
---

# Lab 02.4: Decoding Tokens

## Objective

Convert integer token ids back into text.

## Introduction

Decoding is the reverse of encoding. For every token id, find the matching character and join the characters together.

## Theory

Python can join a list of characters:

```python
text = "".join(["r", "o", "b", "o", "t"])
```

## Python Tools Used

- A generator expression like `id_to_char[token] for token in tokens` produces values one at a time. Docs: https://docs.python.org/3/tutorial/classes.html#generator-expressions
- `"".join(...)` combines decoded characters into a string. Docs: https://docs.python.org/3/library/stdtypes.html#str.join
- `decoded == text` checks whether the round trip recovered the original string. Docs: https://docs.python.org/3/library/stdtypes.html#comparisons

## Assignment

Implement:

```python
decode(tokens, id_to_char)
```

Then test:

```python
decode(encode(text, char_to_id), id_to_char) == text
```

## Conclusion

You can now round-trip text through token ids and back.
