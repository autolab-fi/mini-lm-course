---
index: 14
module: module_4
task: lab_08_raspberry_pi_edge_demo
previous: lab_07_deployment_cli_api_demo
---

# Lab 08: Raspberry Pi Edge Demo

## Objective

Understand edge-device limits: CPU, RAM, latency, and model size.

## Task

Run the inference demo on a Raspberry Pi or compatible edge environment. Measure latency, memory usage, and model size.

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
  "sample_output": "summer rain..."
}
```

## Checks

The checker will verify that:

- the model loads on Raspberry Pi or the target edge environment;
- generation works;
- latency and memory usage are reported;
- edge latency is compared with local or server latency.

## Submission Notes

The goal is to see real limitations of small devices and explain which changes could make inference faster.
