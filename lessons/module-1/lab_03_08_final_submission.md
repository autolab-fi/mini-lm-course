---
index: 9
module: module_1
task: lab_03_08_final_submission
previous: lab_03_07_text_generation
next: lab_04_neural_char_lm
---

# Lab 03.8: Final Bigram Submission

## Objective

Combine all previous steps into one `train_bigram.py` file that the automatic checker can run.

## Task

Create one Python file:

```text
train_bigram.py
```

The checker will run it without arguments:

```bash
python3 train_bigram.py
```

Your program must read the dataset, train the bigram model, evaluate it, generate samples, and save the required artifacts.

## Required Artifacts

Your script must create these files in the current working directory:

```text
bigram_counts.json
metrics.json
samples.json
```

## `bigram_counts.json`

```json
{
  "vocab": ["\n", " ", "a", "b"],
  "char_to_id": {
    "\n": 0,
    " ": 1,
    "a": 2,
    "b": 3
  },
  "counts": [
    [0, 4, 1, 0],
    [2, 0, 9, 1],
    [1, 3, 0, 4],
    [0, 1, 5, 0]
  ]
}
```

## `metrics.json`

```json
{
  "vocab_size": 42,
  "train_chars": 100000,
  "val_chars": 10000,
  "val_loss": 2.95,
  "perplexity": 19.1
}
```

## `samples.json`

```json
{
  "samples": [
    {
      "prompt": "t",
      "generated_text": "the generated text..."
    }
  ]
}
```

You need at least three samples.

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
score >= 70
```

## Rules

- Use only Python standard library modules.
- Do not use `input()`.
- Do not download anything from the internet.
- Do not write files outside the current working directory.
- Your script must finish by itself.

## Conclusion

You have built a complete baseline language model. Later labs will compare this baseline with a neural model.
