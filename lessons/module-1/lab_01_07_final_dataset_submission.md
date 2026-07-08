---
index: 6
module: module_1
task: lab_01_07_final_dataset_submission
previous: lab_01_06_writing_artifacts
next: lab_02_character_tokenizer
---

# Lab 01.7: Final Dataset Submission

## Objective

Combine the previous steps into one complete dataset preparation script.

## Task

Create one Python file that:

1. creates or reads raw text;
2. cleans it;
3. splits it into train, validation, and test files;
4. builds dataset statistics;
5. writes the required artifacts.

## Python Tools Used

- `if __name__ == "__main__":` runs `main()` only when the file is executed directly. Docs: https://docs.python.org/3/library/__main__.html
- `json.dumps(..., ensure_ascii=False, indent=2)` writes readable JSON while preserving non-ASCII text. Docs: https://docs.python.org/3/library/json.html#json.dumps
- `Path(...).write_text(...)` creates the required artifact files. Docs: https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text

## Required Artifacts

```text
train.txt
val.txt
test.txt
stats.json
dataset_card.md
```

## `stats.json` Format

```json
{
  "num_chars": 1000,
  "num_lines": 40,
  "vocab_chars": ["\n", " ", "a"]
}
```

## Rules

- Use only Python standard library modules.
- Do not use `input()`.
- Do not download anything from the internet.
- Write artifacts in the current working directory.

## Conclusion

You have prepared the dataset foundation for the tokenizer and language model labs.
