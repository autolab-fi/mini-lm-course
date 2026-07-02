---
index: 13
module: module_4
task: lab_07_deployment_cli_api_demo
previous: lab_06_evaluation
next: lab_08_raspberry_pi_edge_demo
---

# Lab 07: Deployment CLI/API Demo

## Objective

Turn a trained model into a simple inference tool.

## Task

Prepare a minimal demo interface that generates text from a saved checkpoint.

Required CLI:

```bash
python3 generate.py --prompt "summer rain" --max-new-tokens 100
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

The checker will verify that:

- the model loads from a checkpoint;
- generation completes within the timeout;
- latency is reported;
- output is valid UTF-8.

## Submission Notes

Do not train the model inside the demo. The inference tool should only load a checkpoint and generate text.
