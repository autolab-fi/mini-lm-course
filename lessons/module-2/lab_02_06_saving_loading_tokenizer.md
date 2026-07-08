---
index: 5
module: module_2
task: lab_02_06_saving_loading_tokenizer
previous: lab_02_05_unknown_characters
next: lab_02_07_final_tokenizer_submission
---

# Lab 02.6: Saving and Loading a Tokenizer

## Objective

Save tokenizer data to JSON and load it back.

## Introduction

Later scripts need to reuse the same tokenizer. That means we must save the vocabulary and mappings.

The checker expects a JSON file:

```text
tokenizer.json
```

## Theory

JSON object keys are strings. When saving `id_to_char`, integer keys may become strings. A simple format is:

```json
{
  "vocab": ["<UNK>", "a", "b"],
  "char_to_id": {
    "<UNK>": 0,
    "a": 1,
    "b": 2
  }
}
```

`id_to_char` can be rebuilt from `vocab`.

## Python Tools Used

- `json.dumps(...)` converts Python dictionaries and lists to JSON text. Docs: https://docs.python.org/3/library/json.html#json.dumps
- `json.loads(...)` parses JSON text back into Python data. Docs: https://docs.python.org/3/library/json.html#json.loads
- `Path.read_text()` and `Path.write_text()` read and write files. Docs: https://docs.python.org/3/library/pathlib.html

## Assignment

Implement:

```python
save_tokenizer(path, vocab, char_to_id)
load_tokenizer(path)
```

Then save and load `tokenizer.json`.

## Conclusion

You can now persist a tokenizer for later labs.
