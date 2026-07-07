from __future__ import annotations

from pathlib import Path
import json
import math
from typing import Any


DEFAULT_LIMITS = {
    "timeout_sec": 120,
    "memory_mb": 512,
    "max_log_mb": 5,
    "max_artifact_mb": 50,
}


TASKS = {
    "lab_04_neural_char_lm": {
        "filename": "train_neural_char_lm.py",
        "command": "python train_neural_char_lm.py",
        "required_artifacts": [
            "model.pt",
            "config.yaml",
            "metrics.json",
            "samples.json",
            "loss_curve.png",
        ],
        "limits": DEFAULT_LIMITS,
    }
}


def get_task_config(task_id: str) -> dict[str, Any]:
    if task_id not in TASKS:
        raise ValueError(f"Unknown task_id: {task_id}")
    return dict(TASKS[task_id])


def grade(task_id: str, context: dict[str, Any]) -> dict[str, Any]:
    if task_id != "lab_04_neural_char_lm":
        return _result([_failed("task_id", 0, f"Unknown task_id: {task_id}")])
    return lab_04_neural_char_lm(context)


def lab_04_neural_char_lm(context: dict[str, Any]) -> dict[str, Any]:
    missing = context.get("missing_artifacts", [])
    oversized = context.get("oversized_artifacts", [])
    checks = [
        _runtime_check(context, max_points=10),
        _required_artifacts_check(missing, oversized),
        _metrics_check(context),
        _model_file_check(context),
        _samples_check(context),
        _config_check(context),
        _loss_curve_check(context),
    ]
    return _result(checks)


def _passed(name: str, max_points: int, message: str) -> dict[str, Any]:
    return {
        "name": name,
        "status": "passed",
        "points": max_points,
        "max_points": max_points,
        "message": message,
    }


def _failed(name: str, max_points: int, message: str) -> dict[str, Any]:
    return {
        "name": name,
        "status": "failed",
        "points": 0,
        "max_points": max_points,
        "message": message,
    }


def _result(checks: list[dict[str, Any]], pass_score: int = 70) -> dict[str, Any]:
    score = sum(check["points"] for check in checks)
    max_score = sum(check["max_points"] for check in checks)
    failed = [check for check in checks if check["status"] != "passed"]
    return {
        "status": "passed" if score >= pass_score and not failed else "failed",
        "score": score,
        "max_score": max_score,
        "checks": checks,
        "feedback": _feedback(failed),
    }


def _feedback(failed: list[dict[str, Any]]) -> dict[str, Any]:
    if not failed:
        return {"summary": "The submission passed the Lab 04 neural LM checks.", "suggestions": []}
    return {
        "summary": "The neural LM submission ran, but one or more checks failed.",
        "suggestions": [check["message"] for check in failed[:3]],
    }


def _runtime_check(context: dict[str, Any], max_points: int) -> dict[str, Any]:
    if context.get("timed_out"):
        return _failed("runtime", max_points, "The training script timed out.")
    if context.get("return_code") != 0:
        stderr = str(context.get("stderr", "")).strip()
        detail = stderr.splitlines()[-1] if stderr else "The training script exited with an error."
        return _failed("runtime", max_points, detail)
    return _passed("runtime", max_points, "The training script completed successfully.")


def _required_artifacts_check(missing: list[str], oversized: list[str]) -> dict[str, Any]:
    if missing:
        return _failed("required_files", 15, f"Missing required artifact(s): {', '.join(missing)}")
    if oversized:
        return _failed("required_files", 15, f"Oversized artifact(s): {', '.join(oversized)}")
    return _passed("required_files", 15, "All required artifacts were found.")


def _artifact_path(context: dict[str, Any], name: str) -> Path:
    return Path(str(context["artifacts_dir"])) / name


def _load_json(path: Path) -> tuple[Any | None, str | None]:
    if not path.is_file():
        return None, "file not found"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as exc:
        return None, str(exc)


def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value)


def _metrics_check(context: dict[str, Any]) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "metrics.json"))
    if error:
        return _failed("metrics", 25, f"metrics.json is not valid JSON: {error}")
    required = [
        "dataset_id",
        "train_loss_initial",
        "train_loss_final",
        "val_loss",
        "perplexity",
        "num_parameters",
        "training_time_sec",
    ]
    if not isinstance(data, dict):
        return _failed("metrics", 25, "metrics.json must contain a JSON object.")
    for key in required:
        if key not in data:
            return _failed("metrics", 25, f"metrics.json is missing {key}.")
    if data["dataset_id"] != str(context.get("dataset_id", "tiny_shakespeare_chars")):
        return _failed("metrics", 25, "dataset_id must match the checker dataset.")
    for key in ("train_loss_initial", "train_loss_final", "val_loss", "perplexity", "training_time_sec"):
        if not _finite_number(data[key]):
            return _failed("metrics", 25, f"{key} must be a finite number.")
    if data["train_loss_final"] >= data["train_loss_initial"]:
        return _failed("metrics", 25, "train_loss_final must be lower than train_loss_initial.")
    if data["val_loss"] <= 0 or data["perplexity"] <= 0:
        return _failed("metrics", 25, "val_loss and perplexity must be positive.")
    if not isinstance(data["num_parameters"], int) or data["num_parameters"] <= 0:
        return _failed("metrics", 25, "num_parameters must be a positive integer.")
    return _passed("metrics", 25, "Training metrics are finite and show loss improvement.")


def _model_file_check(context: dict[str, Any]) -> dict[str, Any]:
    path = _artifact_path(context, "model.pt")
    if not path.is_file():
        return _failed("model_file", 15, "model.pt was not created.")
    size = path.stat().st_size
    if size <= 0:
        return _failed("model_file", 15, "model.pt is empty.")
    if size > 20 * 1024 * 1024:
        return _failed("model_file", 15, "model.pt is too large for this lab.")
    return _passed("model_file", 15, "model.pt exists and is within the size limit.")


def _samples_check(context: dict[str, Any]) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "samples.json"))
    if error:
        return _failed("samples", 15, f"samples.json is not valid JSON: {error}")
    samples = data.get("samples") if isinstance(data, dict) else None
    if not isinstance(samples, list) or len(samples) < 3:
        return _failed("samples", 15, "samples.json must contain at least 3 samples.")
    for sample in samples:
        if not isinstance(sample, dict):
            return _failed("samples", 15, "Each sample must be an object.")
        generated_text = sample.get("generated_text")
        if not isinstance(generated_text, str) or len(generated_text) < 20:
            return _failed("samples", 15, "Each generated_text must contain at least 20 characters.")
    return _passed("samples", 15, "Generated samples are present and non-empty.")


def _config_check(context: dict[str, Any]) -> dict[str, Any]:
    path = _artifact_path(context, "config.yaml")
    if not path.is_file():
        return _failed("config", 10, "config.yaml was not created.")
    text = path.read_text(encoding="utf-8")
    required = ["model_type", "vocab_size", "embedding_dim", "steps", "learning_rate"]
    missing = [key for key in required if key not in text]
    if missing:
        return _failed("config", 10, f"config.yaml is missing: {', '.join(missing)}")
    return _passed("config", 10, "config.yaml describes the training run.")


def _loss_curve_check(context: dict[str, Any]) -> dict[str, Any]:
    path = _artifact_path(context, "loss_curve.png")
    if not path.is_file():
        return _failed("loss_curve", 10, "loss_curve.png was not created.")
    if path.stat().st_size < 16:
        return _failed("loss_curve", 10, "loss_curve.png is too small.")
    return _passed("loss_curve", 10, "loss_curve.png exists.")
