---
index: 6
module: module_2
task: lab_02_07_final_tokenizer_submission
previous: lab_02_06_saving_loading_tokenizer
next: lab_03_01_intro_to_character_lm
---

# Lab 02.7: Final Tokenizer Submission

## Objective

Build a complete character tokenizer submission.

## Task

Create a Python script that:

1. builds a character vocabulary;
2. adds `<UNK>`;
3. implements encode and decode;
4. saves `tokenizer.json`;
5. saves `tokenizer_report.json`.

## Python Tools Used

- `Path("tokenizer.json").write_text(...)` writes the tokenizer artifact. Docs: https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text
- `json.dumps(..., ensure_ascii=False, indent=2)` creates readable JSON output. Docs: https://docs.python.org/3/library/json.html#json.dumps
- Function composition such as `decode(encode(text, char_to_id), id_to_char)` tests that two functions work together. Docs: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

## Required Artifacts

```text
tokenizer.json
tokenizer_report.json
```

## `tokenizer.json` Format

```json
{
  "vocab": ["<UNK>", "\n", " ", "a"],
  "char_to_id": {
    "<UNK>": 0,
    "\n": 1,
    " ": 2,
    "a": 3
  }
}
```

## `tokenizer_report.json` Suggested Format

```json
{
  "vocab_size": 42,
  "roundtrip_ok": true,
  "unknown_token": "<UNK>",
  "example_text": "poem",
  "example_tokens": [10, 4, 3, 4, 12],
  "decoded_text": "poem"
}
```

## Rules

- Use only Python standard library modules.
- Do not use `input()`.
- Write artifacts in the current working directory.

## Conclusion

You now have a tokenizer that future language model labs can reuse.
