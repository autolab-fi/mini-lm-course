# Lab 07: Deployment CLI/API Demo

## Objective

Показать, как обученная модель превращается в простой inference tool.

## Task

Подготовьте минимальный demo-интерфейс для генерации текста из сохраненного checkpoint.

Required CLI:

```bash
python generate.py --prompt "robot moves" --max-new-tokens 100
```

Optional HTTP API:

```http
POST /generate
```

## Required Artifacts

```text
generate.py
demo_result.json
```

## Checks

Grader будет проверять:

- model loads from checkpoint;
- generation completes within timeout;
- latency is reported;
- output is valid UTF-8.

## Submission Notes

Не обучайте модель внутри demo. Inference tool должен только загрузить checkpoint и выполнить generation.
