# Lab 03: Bigram Character Language Model

## Objective

Реализовать простую символьную language model, которая предсказывает следующий символ по текущему символу.

В этой лабораторной вы строите baseline без neural networks:

```text
P(next_char | current_char)
```

Такой baseline нужен, чтобы позже сравнить его с neural character LM.

## What You Should Understand

К концу lab вы должны понимать:

- language model предсказывает следующий token или character;
- bigram model смотрит только на один предыдущий символ;
- counts можно превратить в probabilities;
- validation loss показывает, насколько модель "удивляется" validation text;
- perplexity = `exp(loss)`;
- generation работает через repeated sampling next character;
- baseline нужен для сравнения с neural model.

## Task

Напишите файл:

```text
train_bigram.py
```

Скрипт должен запускаться без аргументов:

```bash
python train_bigram.py
```

В worker/grader окружении dataset доступен по read-only path:

```text
/datasets/toy_chars_100kb/train.txt
/datasets/toy_chars_100kb/val.txt
/datasets/toy_chars_100kb/test.txt
```

Локальный прототип также передает путь через environment variable:

```text
DATASETS_DIR=<repo>/datasets
```

## What to Implement

`train_bigram.py` должен:

1. Прочитать `train.txt` и `val.txt`.
2. Построить vocabulary символов.
3. Создать mapping `char_to_id`.
4. Посчитать bigram counts:

```text
counts[current_char_id][next_char_id] += 1
```

5. Использовать smoothing для validation loss, чтобы не получать zero probability.
6. Посчитать validation negative log likelihood.
7. Посчитать perplexity.
8. Сгенерировать минимум 3 text samples.
9. Сохранить required artifacts.

## Required Artifacts

```text
bigram_counts.json
metrics.json
samples.json
```

## `bigram_counts.json` Format

```json
{
  "vocab": ["\n", " ", "a", "b", "c"],
  "char_to_id": {
    "\n": 0,
    " ": 1,
    "a": 2,
    "b": 3,
    "c": 4
  },
  "counts": [
    [0, 4, 1, 0, 0],
    [2, 0, 9, 1, 1],
    [1, 3, 0, 4, 2],
    [0, 1, 5, 0, 3],
    [2, 1, 0, 2, 0]
  ]
}
```

Requirements:

- `vocab` is a non-empty list of strings;
- `char_to_id` contains exactly the characters from `vocab`;
- ids are contiguous and start at `0`;
- `counts` is a square matrix `vocab_size x vocab_size`;
- all count values are non-negative integers.

## `metrics.json` Format

```json
{
  "vocab_size": 42,
  "train_chars": 100000,
  "val_chars": 10000,
  "val_loss": 2.95,
  "perplexity": 19.1
}
```

Requirements:

- `vocab_size > 0`;
- `train_chars > 0`;
- `val_chars > 0`;
- `val_loss` is finite;
- `perplexity` is finite.

## `samples.json` Format

```json
{
  "samples": [
    {
      "prompt": "a",
      "generated_text": "and then the robot..."
    },
    {
      "prompt": "t",
      "generated_text": "the model..."
    },
    {
      "prompt": "\n",
      "generated_text": "\nonce..."
    }
  ]
}
```

Requirements:

- `samples` is a list;
- at least 3 samples are present;
- every `generated_text` is a non-empty UTF-8 string.

## Scoring

Total: 100 points.

```text
20 points: required files exist
20 points: bigram vocabulary/counts structure is valid
20 points: metrics.json is valid and finite
20 points: samples.json contains non-empty generated samples
10 points: code runs within timeout
10 points: artifact sizes are within limits
```

Passing threshold:

```text
score >= 70 and no critical runtime error
```

## Implementation Hint

Use add-one smoothing:

```python
probability = (count + 1) / (row_sum + vocab_size)
```

Validation loss:

```python
loss = average(-log P(next_char | current_char))
perplexity = exp(loss)
```

Generation can repeatedly sample the next character from the probability distribution for the current character.
