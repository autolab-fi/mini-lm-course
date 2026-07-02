# Lab 08: Raspberry Pi Edge Demo

## Objective

Понять ограничения edge device: CPU, RAM, latency, model size.

## Task

Запустите inference demo на Raspberry Pi или совместимом edge environment и измерьте latency, memory usage и размер модели.

## Required Artifacts

```text
edge_demo.json
```

## `edge_demo.json` Suggested Fields

```json
{
  "device": "Raspberry Pi",
  "model_size_mb": 1.2,
  "latency_ms": 85.0,
  "memory_mb": 120.0,
  "sample_output": "robot moves..."
}
```

## Checks

Grader будет проверять:

- model loads on Raspberry Pi or target edge environment;
- generation works;
- latency and memory usage are reported;
- edge latency is compared with local/server latency.

## Submission Notes

Цель этой лабораторной - увидеть реальные ограничения маленьких устройств и сформулировать, какие изменения помогли бы ускорить inference.
