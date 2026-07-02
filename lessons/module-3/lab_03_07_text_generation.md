---
index: 8
module: module_3
task: lab_03_07_text_generation
previous: lab_03_06_validation_loss
next: lab_03_08_final_submission
---

# Lab 03.7: Generating Text

## Objective

Use the bigram model to generate new text one character at a time.

## Introduction

The model can now predict probabilities. Generation uses those probabilities repeatedly:

```text
start with prompt
choose next character
append it to output
use that character as the new current character
repeat
```

The generated text will not be perfect. A bigram model has very short memory, so it often produces strange words. That is expected.

## Theory

### Weighted Sampling

Python can choose from a list using weights:

```python
random.choices(vocab, weights=probabilities, k=1)[0]
```

Characters with higher probabilities are more likely to be chosen.

### Prompt

The prompt gives the model a starting character or short text. The last character of the prompt becomes the current character.

## Assignment

Implement:

```python
sample_next_char(row, vocab)
generate(prompt, counts, vocab, char_to_id, max_new_chars=100)
```

Requirements:

1. Use `row_probabilities` for sampling weights.
2. Generate one character at a time.
3. Return the full text, including the prompt.
4. Handle unknown prompt characters by choosing a random known character.

## Conclusion

Your baseline model can now generate text. In the final step, you will save the model outputs for the checker.
