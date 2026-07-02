# Lab 01: Dataset Preparation

## Objective

Понять, что language model обучается на корпусе текста, и подготовить train/validation/test split.

## Task

Подготовьте текстовый dataset для следующих лабораторных. Вам нужно прочитать raw text, нормализовать encoding и переносы строк, разделить данные на train/validation/test и сохранить краткое описание датасета.

## What to Implement

Создайте скрипт или notebook, который:

1. Читает исходный текстовый файл.
2. Нормализует текст в UTF-8.
3. Делит текст на `train.txt`, `val.txt`, `test.txt`.
4. Считает базовую статистику.
5. Сохраняет `dataset_card.md`.

## Required Artifacts

```text
train.txt
val.txt
test.txt
stats.json
dataset_card.md
```

## `stats.json` Minimum Format

```json
{
  "num_chars": 100000,
  "num_lines": 1200,
  "vocab_chars": ["\n", " ", "a"]
}
```

## Checks

Grader будет проверять:

- required files exist;
- files are valid UTF-8;
- split files are non-empty;
- train split is larger than validation and test splits;
- `stats.json` contains `num_chars`, `num_lines`, `vocab_chars`;
- split files do not fully overlap.

## Submission Notes

Сохраняйте output files в текущую рабочую директорию submission. Не скачивайте внешние данные во время проверки.
