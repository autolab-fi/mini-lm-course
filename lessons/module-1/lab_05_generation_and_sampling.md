# Lab 05: Generation and Sampling

## Objective

Понять prompt, `max_new_tokens`, temperature и stochastic sampling.

## Task

Реализуйте CLI для генерации текста из checkpoint, полученного в `Lab 04`.

Expected command:

```bash
python generate.py --prompt "the robot" --max-new-tokens 100 --temperature 0.8
```

## Required Artifacts

```text
samples.json
generation_report.md
```

## Checks

Grader будет проверять:

- `generate.py` accepts prompt;
- checkpoint loads without retraining;
- outputs are non-empty;
- latency is reported;
- low and high temperature outputs are compared.

## Submission Notes

В отчете коротко объясните, что меняется при низкой и высокой temperature.
