---
index: 10
module: module_4
task: lab_04_lessons_plan
previous: lab_03_08_final_submission
next: lab_04_01_neural_lm_overview
---

# Lab 04 Lesson Plan: Neural Character Language Model

## Goal

Turn `Lab 04` into a sequence of small lessons that gradually moves from the `Lab 03` bigram baseline to a trainable neural character model.

The final student submission should create:

```text
model.pt
config.yaml
metrics.json
samples.json
loss_curve.png
```

The module should stay small enough to run on CPU in the browser-worker flow. The goal is to teach the training loop, not to chase model quality.

## Lab 04.1: Why a Neural LM?

Objective:

```text
Understand what the bigram baseline cannot remember and why a trainable model can improve it.
```

Student work:

- load the same dataset used in `Lab 03`;
- print a few character windows such as `context -> next_char`;
- compare one-character context with a longer context.

Starter task:

```python
text = "summer rain"
context_size = 4

for index in range(context_size, len(text)):
    context = text[index - context_size:index]
    target = text[index]
    print(context, "->", target)
```

Checks:

- program runs;
- prints at least one `context -> target` pair;
- explains that a neural model can use learned parameters instead of raw counts.

## Lab 04.2: Turning Text Into Training Examples

Objective:

```text
Create integer training pairs or short context windows from text.
```

Student work:

- build `vocab`, `char_to_id`, `id_to_char`;
- encode text into ids;
- create `(input_ids, target_id)` examples.

Expected output:

```text
Vocabulary size: 65
Example input ids: [...]
Example target id: ...
```

Checks:

- vocab is non-empty;
- encoded ids are integers;
- training examples are non-empty;
- target id is inside vocabulary range.

## Lab 04.3: Model Configuration and Parameters

Objective:

```text
Define a small model shape and count its parameters.
```

Student work:

- choose `embedding_dim`;
- initialize small parameter matrices;
- write `config.yaml`;
- calculate `num_parameters`.

Suggested CPU-safe model for the first implementation:

```text
character id -> embedding vector -> linear logits -> softmax
```

Later versions may replace the linear layer with `RNN/GRU`, but the first checker can accept a tiny embedding-softmax model to avoid heavy dependencies.

Checks:

- `config.yaml` exists;
- contains `model_type`, `vocab_size`, `embedding_dim`, `steps`, `learning_rate`;
- `num_parameters` is positive.

## Lab 04.4: Forward Pass, Softmax, and Loss

Objective:

```text
Compute next-character probabilities and negative log likelihood.
```

Student work:

- implement `softmax(logits)`;
- run a forward pass for one input character;
- compute loss for the correct next character.

Checks:

- probabilities are positive;
- probabilities sum to approximately `1.0`;
- loss is finite and positive.

## Lab 04.5: Training Loop

Objective:

```text
Update model parameters and show that training loss can go down.
```

Student work:

- sample training pairs;
- run a fixed number of update steps;
- print progress every N steps;
- track initial and final training loss.

Recommended first target:

```text
1000-5000 update steps on CPU
```

Checks:

- training script finishes within timeout;
- progress is printed;
- `train_loss_final < train_loss_initial`;
- no internet access or external downloads are needed.

## Lab 04.6: Validation Loss and Perplexity

Objective:

```text
Evaluate the trained model on validation text.
```

Student work:

- compute `val_loss`;
- compute `perplexity = exp(val_loss)`;
- compare train and validation loss.

Checks:

- `val_loss` is finite and positive;
- `perplexity` is finite and positive;
- validation is not computed on the exact same slice as training.

## Lab 04.7: Sampling From the Neural Model

Objective:

```text
Generate text from learned probabilities.
```

Student work:

- implement `sample_next_char`;
- generate at least three samples from different prompts;
- write `samples.json`.

Checks:

- `samples.json` is valid JSON;
- contains at least three samples;
- every `generated_text` is non-empty and longer than the prompt.

## Lab 04.8: Final Neural Char LM Submission

Objective:

```text
Assemble the complete training script and save all required artifacts.
```

Required script:

```text
train_neural_char_lm.py
```

Required artifacts:

```text
model.pt
config.yaml
metrics.json
samples.json
loss_curve.png
```

`metrics.json` fields:

```json
{
  "dataset_id": "tiny_shakespeare_chars",
  "train_loss_initial": 4.1,
  "train_loss_final": 2.8,
  "val_loss": 2.95,
  "perplexity": 19.1,
  "num_parameters": 2145,
  "training_time_sec": 5.4
}
```

Checks:

- code runs within timeout;
- all required artifacts exist;
- `train_loss_final < train_loss_initial`;
- validation metrics are finite;
- `model.pt` is non-empty and under the size limit;
- generated samples are present;
- config describes the model and training run.

## Activation Notes

Do not enable this module in `lessons-list.json` until each planned lesson has a matching verifier.

The current prototype verifier supports only the final task:

```text
lab_04_neural_char_lm
```

The current prototype sample is intentionally dependency-free and CPU-safe. A later PyTorch-based version can be added when the worker image includes `torch`.
