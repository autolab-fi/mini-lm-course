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

## Assignment

Write all five artifacts and print their filenames.

## Conclusion

You can now produce files that the checker can inspect.
