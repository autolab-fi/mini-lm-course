---
index: 3
module: module_3
task: lab_03_02_reading_dataset
previous: lab_03_01_intro_to_character_lm
next: lab_03_03_character_vocabulary
---

# Lab 03.2: Reading the Dataset

## Objective

Read the training and validation text files that the checker provides.

## Introduction

The model needs text data. During automatic checking, the selected dataset is available in a read-only directory:

```text
/datasets/<dataset_id>/
```

You do not edit these files in the browser editor. Your code only reads them.

The default dataset is `tiny_shakespeare_chars`. The platform may also let you choose another dataset theme before running the same code.

You can preview the available datasets in the open course repository:

| Dataset ID | Theme | Preview |
| --- | --- | --- |
| `tiny_shakespeare_chars` | English drama dialogue | [card](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/tiny_shakespeare_chars/dataset_card.md), [train](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/tiny_shakespeare_chars/train.txt), [val](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/tiny_shakespeare_chars/val.txt), [test](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/tiny_shakespeare_chars/test.txt) |
| `kalevala_finnish_chars` | Finnish epic poetry | [card](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/kalevala_finnish_chars/dataset_card.md), [train](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/kalevala_finnish_chars/train.txt), [val](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/kalevala_finnish_chars/val.txt), [test](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/kalevala_finnish_chars/test.txt) |
| `suomalainen_lukemisto_chars` | Finnish prose and poetry anthology | [card](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/suomalainen_lukemisto_chars/dataset_card.md), [train](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/suomalainen_lukemisto_chars/train.txt), [val](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/suomalainen_lukemisto_chars/val.txt), [test](https://raw.githubusercontent.com/autolab-fi/mini-lm-course/main/datasets/suomalainen_lukemisto_chars/test.txt) |

These links are for preview. In your Python code, always read the local checker files through `DATASETS_DIR`.

The checker provides two environment variables:

```text
DATASETS_DIR
DATASET_ID
```

The starter code supports both cases.

## Theory

### Paths with `pathlib`

Python's `Path` object helps you build file paths without manually writing slashes.

```python
from pathlib import Path
import os

datasets_dir = Path(os.environ.get("DATASETS_DIR", "/datasets"))
dataset_id = os.environ.get("DATASET_ID", "tiny_shakespeare_chars")
folder = datasets_dir / dataset_id
train_path = folder / "train.txt"
```

### Reading UTF-8 Text

Always read course text files with UTF-8 encoding:

```python
text = train_path.read_text(encoding="utf-8")
```

### Train and Validation Splits

We use:

- `train.txt` to count patterns;
- `val.txt` to measure how well the model predicts unseen text.

## Python Tools Used

- `os.environ.get("NAME", default)` reads an environment variable or returns a default. Docs: https://docs.python.org/3/library/os.html#os.environ
- The `/` operator on `Path` joins path parts, for example `datasets_dir / dataset_id`. Docs: https://docs.python.org/3/library/pathlib.html#operators
- `Path.read_text(encoding="utf-8")` reads the dataset file. Docs: https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text

## Assignment

Read `train.txt` and `val.txt`, then print:

1. number of characters in training text;
2. number of characters in validation text;
3. first 200 characters of training text.

## Conclusion

You can now load the text that the bigram model will learn from.
