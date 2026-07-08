---
index: 5
module: module_1
task: lab_01_06_writing_artifacts
previous: lab_01_05_dataset_statistics
next: lab_01_07_final_dataset_submission
---

# Lab 01.6: Writing Dataset Artifacts

## Objective

Save dataset files and metadata in the format expected by the checker.

## Introduction

The checker reads files created by your program. These files are called artifacts.

For dataset preparation, the artifacts are:

```text
train.txt
val.txt
test.txt
stats.json
dataset_card.md
```

## Theory

### JSON Files

Python dictionaries can be saved as JSON:

```python
Path("stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
```

### Markdown Files

`dataset_card.md` is a short human-readable description of the dataset.

## Python Tools Used

- `json.dumps(data, indent=2)` converts Python data to formatted JSON text. Docs: https://docs.python.org/3/library/json.html#json.dumps
- `Path.write_text(text, encoding="utf-8")` writes text files in UTF-8. Docs: https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text
- A `for` loop repeats work for every item in a list. Docs: https://docs.python.org/3/tutorial/controlflow.html#for-statements

## Assignment

Write all five artifacts and print their filenames.

## Conclusion

You can now produce files that the checker can inspect.
