from __future__ import annotations

from pathlib import Path
import ast
import json
import math
import re
from typing import Any


DEFAULT_LIMITS = {
    "timeout_sec": 60,
    "memory_mb": 512,
    "max_log_mb": 5,
    "max_artifact_mb": 20,
}


TASKS = {'lab_03_01_intro_to_character_lm': {'filename': 'main.py',
                                     'command': 'python main.py',
                                     'required_artifacts': [],
                                     'limits': {'timeout_sec': 60,
                                                'memory_mb': 512,
                                                'max_log_mb': 5,
                                                'max_artifact_mb': 20}},
 'lab_03_02_reading_dataset': {'filename': 'main.py',
                               'command': 'python main.py',
                               'required_artifacts': [],
                               'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_03_03_character_vocabulary': {'filename': 'main.py',
                                    'command': 'python main.py',
                                    'required_artifacts': [],
                                    'limits': {'timeout_sec': 60,
                                               'memory_mb': 512,
                                               'max_log_mb': 5,
                                               'max_artifact_mb': 20}},
 'lab_03_04_bigram_counts': {'filename': 'main.py',
                             'command': 'python main.py',
                             'required_artifacts': [],
                             'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_03_05_probabilities': {'filename': 'main.py',
                             'command': 'python main.py',
                             'required_artifacts': [],
                             'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_03_06_validation_loss': {'filename': 'main.py',
                               'command': 'python main.py',
                               'required_artifacts': [],
                               'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_03_07_text_generation': {'filename': 'main.py',
                               'command': 'python main.py',
                               'required_artifacts': [],
                               'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_03_08_final_submission': {'filename': 'train_bigram.py',
                                'command': 'python train_bigram.py',
                                'required_artifacts': ['bigram_counts.json', 'metrics.json', 'samples.json'],
                                'limits': {'timeout_sec': 60,
                                           'memory_mb': 512,
                                           'max_log_mb': 5,
                                           'max_artifact_mb': 20}}}


def get_task_config(task_id: str) -> dict[str, Any]:
    if task_id not in TASKS:
        raise ValueError(f"Unknown task_id: {task_id}")
    return dict(TASKS[task_id])

def grade(task_id: str, context: dict[str, Any]) -> dict[str, Any]:
    if task_id not in TASKS:
        return _result([_failed("task_id", 0, f"Unknown task_id: {task_id}")])
    checker = globals().get(task_id)
    if checker is None:
        return _result([_failed("checker", 0, f"No checker function for {task_id}")])
    return checker(context)

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
    status = "passed" if score >= pass_score and not failed else "failed"
    return {
        "status": status,
        "score": score,
        "max_score": max_score,
        "checks": checks,
        "feedback": _feedback(failed),
    }

def _feedback(failed: list[dict[str, Any]]) -> dict[str, Any]:
    if not failed:
        return {
            "summary": "The submission passed the lesson checks.",
            "suggestions": [],
        }
    return {
        "summary": "The submission ran, but one or more lesson checks failed.",
        "suggestions": [check["message"] for check in failed[:3]],
    }

def _runtime_check(context: dict[str, Any], max_points: int = 20) -> dict[str, Any]:
    if context.get("timed_out"):
        return _failed("runtime", max_points, "The program timed out.")
    if context.get("return_code") != 0:
        stderr = str(context.get("stderr", "")).strip()
        detail = stderr.splitlines()[-1] if stderr else "The program exited with an error."
        return _failed("runtime", max_points, detail)
    return _passed("runtime", max_points, "The program completed successfully.")

def _stdout(context: dict[str, Any]) -> str:
    return str(context.get("stdout", ""))

def _numbers_after_labels(stdout: str, labels: list[str]) -> list[int]:
    numbers: list[int] = []
    for label in labels:
        match = re.search(re.escape(label) + r"\s*(\d+)", stdout)
        if match:
            numbers.append(int(match.group(1)))
    return numbers

def _extract_list_after_label(stdout: str, label: str) -> list[Any] | None:
    for line in stdout.splitlines():
        if line.startswith(label):
            _, value = line.split(":", 1)
            try:
                parsed = ast.literal_eval(value.strip())
            except Exception:
                return None
            return parsed if isinstance(parsed, list) else None
    return None

def _extract_dict_after_label(stdout: str, label: str) -> dict[str, Any] | None:
    for line in stdout.splitlines():
        if line.startswith(label):
            _, value = line.split(":", 1)
            try:
                parsed = ast.literal_eval(value.strip())
            except Exception:
                return None
            return parsed if isinstance(parsed, dict) else None
    return None

def _extract_float_after_label(stdout: str, label: str) -> float | None:
    match = re.search(re.escape(label) + r"\s*([-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)", stdout)
    if not match:
        return None
    try:
        value = float(match.group(1))
    except ValueError:
        return None
    return value if math.isfinite(value) else None

def _load_json(path: Path) -> tuple[Any | None, str | None]:
    if not path.is_file():
        return None, "file not found"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as exc:
        return None, str(exc)

def _artifact_path(context: dict[str, Any], name: str) -> Path:
    return Path(str(context["artifacts_dir"])) / name

def lab_03_01_intro_to_character_lm(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    pair_lines = [line for line in stdout.splitlines() if "->" in line]
    checks = [
        _runtime_check(context),
        _passed("character_pairs", 80, "Printed neighboring character pairs.")
        if len(pair_lines) >= 1
        else _failed("character_pairs", 80, "Print at least one neighboring pair such as h -> e."),
    ]
    return _result(checks)

def lab_03_02_reading_dataset(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    counts = _numbers_after_labels(stdout, ["Train characters:", "Validation characters:"])
    checks = [
        _runtime_check(context),
        _passed("dataset_counts", 60, "Printed positive train and validation character counts.")
        if len(counts) == 2 and all(value > 0 for value in counts)
        else _failed("dataset_counts", 60, "Print positive Train characters and Validation characters counts."),
        _passed("dataset_preview", 20, "Printed a training text preview.")
        if "First 200 training characters:" in stdout and len(stdout.strip().splitlines()) >= 4
        else _failed("dataset_preview", 20, "Print the first 200 training characters."),
    ]
    return _result(checks)

def lab_03_03_character_vocabulary(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    vocab_size = _extract_float_after_label(stdout, "Vocabulary size:")
    first_chars = _extract_list_after_label(stdout, "First 10 characters")
    checks = [
        _runtime_check(context),
        _passed("vocab_size", 40, "Vocabulary size is positive.")
        if vocab_size is not None and vocab_size > 0
        else _failed("vocab_size", 40, "Print a positive Vocabulary size."),
        _passed("vocab_preview", 40, "Printed a vocabulary preview list.")
        if first_chars is not None and len(first_chars) > 0 and all(isinstance(item, str) for item in first_chars)
        else _failed("vocab_preview", 40, "Print First 10 characters as a non-empty Python list of strings."),
    ]
    return _result(checks)

def lab_03_04_bigram_counts(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    vocab_size = _extract_float_after_label(stdout, "Vocabulary size:")
    matrix_rows = _extract_float_after_label(stdout, "Matrix rows:")
    first_row = _extract_list_after_label(stdout, "First row")
    checks = [
        _runtime_check(context),
        _passed("matrix_shape", 40, "Counts matrix row count matches vocabulary size.")
        if vocab_size is not None and matrix_rows is not None and int(vocab_size) == int(matrix_rows) and matrix_rows > 0
        else _failed("matrix_shape", 40, "Print Matrix rows equal to Vocabulary size."),
        _passed("counts_row", 40, "First row contains non-negative integer counts.")
        if first_row is not None and len(first_row) > 0 and all(isinstance(value, int) and value >= 0 for value in first_row)
        else _failed("counts_row", 40, "Print First row as a non-empty list of non-negative integers."),
    ]
    return _result(checks)

def lab_03_05_probabilities(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    probabilities = _extract_list_after_label(stdout, "Probabilities")
    probability_sum = _extract_float_after_label(stdout, "Sum:")
    checks = [
        _runtime_check(context),
        _passed("probabilities", 40, "Returned non-zero probabilities.")
        if probabilities is not None and len(probabilities) > 0 and all(isinstance(value, float) and value > 0 for value in probabilities)
        else _failed("probabilities", 40, "Print Probabilities as a non-empty list of positive floats."),
        _passed("probability_sum", 40, "Probabilities sum to 1.")
        if probability_sum is not None and abs(probability_sum - 1.0) < 1e-6
        else _failed("probability_sum", 40, "The probability sum should be very close to 1.0."),
    ]
    return _result(checks)

def lab_03_06_validation_loss(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    val_loss = _extract_float_after_label(stdout, "Validation loss:")
    perplexity = _extract_float_after_label(stdout, "Perplexity:")
    checks = [
        _runtime_check(context),
        _passed("val_loss", 40, "Validation loss is finite and positive.")
        if val_loss is not None and val_loss > 0
        else _failed("val_loss", 40, "Print a finite positive Validation loss."),
        _passed("perplexity", 40, "Perplexity is finite and positive.")
        if perplexity is not None and perplexity > 0
        else _failed("perplexity", 40, "Print a finite positive Perplexity."),
    ]
    return _result(checks)

def lab_03_07_text_generation(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context).strip()
    generated_lines = [line for line in stdout.splitlines() if line.strip()]
    generated_text = generated_lines[-1] if generated_lines else ""
    checks = [
        _runtime_check(context),
        _passed("generated_text", 80, "Generated non-empty text longer than the prompt.")
        if len(generated_text) > 1
        else _failed("generated_text", 80, "Print generated text longer than the prompt."),
    ]
    return _result(checks)

def lab_03_08_final_submission(context: dict[str, Any]) -> dict[str, Any]:
    missing = context.get("missing_artifacts", [])
    oversized = context.get("oversized_artifacts", [])
    checks = [
        _runtime_check(context, max_points=10),
        _required_artifacts_check(missing, oversized),
        _bigram_counts_check(context),
        _metrics_check(context),
        _samples_check(context),
        _artifact_size_check(oversized),
    ]
    return _result(checks)

def _required_artifacts_check(missing: list[str], oversized: list[str]) -> dict[str, Any]:
    if missing:
        return _failed("required_files", 20, f"Missing required artifact(s): {', '.join(missing)}")
    if oversized:
        return _failed("required_files", 20, f"Oversized artifact(s): {', '.join(oversized)}")
    return _passed("required_files", 20, "All required artifacts were found.")

def _bigram_counts_check(context: dict[str, Any]) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "bigram_counts.json"))
    if error:
        return _failed("bigram_counts", 20, f"bigram_counts.json is not valid JSON: {error}")
    if not isinstance(data, dict):
        return _failed("bigram_counts", 20, "bigram_counts.json must contain a JSON object.")
    vocab = data.get("vocab")
    char_to_id = data.get("char_to_id")
    counts = data.get("counts")
    if not isinstance(vocab, list) or not vocab or not all(isinstance(item, str) for item in vocab):
        return _failed("bigram_counts", 20, "vocab must be a non-empty list of strings.")
    if not isinstance(char_to_id, dict) or set(char_to_id.keys()) != set(vocab):
        return _failed("bigram_counts", 20, "char_to_id must contain exactly the characters from vocab.")
    if set(char_to_id.values()) != set(range(len(vocab))):
        return _failed("bigram_counts", 20, "char_to_id values must be contiguous ids starting at 0.")
    if not isinstance(counts, list) or len(counts) != len(vocab):
        return _failed("bigram_counts", 20, "counts must be a square matrix matching vocab size.")
    for row in counts:
        if not isinstance(row, list) or len(row) != len(vocab):
            return _failed("bigram_counts", 20, "counts must be a square matrix matching vocab size.")
        if not all(isinstance(value, int) and value >= 0 for value in row):
            return _failed("bigram_counts", 20, "counts values must be non-negative integers.")
    return _passed("bigram_counts", 20, "Bigram vocabulary and counts matrix are valid.")

def _metrics_check(context: dict[str, Any]) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "metrics.json"))
    if error:
        return _failed("metrics", 20, f"metrics.json is not valid JSON: {error}")
    if not isinstance(data, dict):
        return _failed("metrics", 20, "metrics.json must contain a JSON object.")
    for key in ("dataset_id", "vocab_size", "train_chars", "val_chars", "val_loss", "perplexity"):
        if key not in data:
            return _failed("metrics", 20, f"metrics.json is missing {key}.")
    expected_dataset_id = str(context.get("dataset_id", "tiny_shakespeare_chars"))
    if data["dataset_id"] != expected_dataset_id:
        return _failed("metrics", 20, f"dataset_id must be {expected_dataset_id}.")
    if not isinstance(data["vocab_size"], int) or data["vocab_size"] <= 0:
        return _failed("metrics", 20, "vocab_size must be a positive integer.")
    if not isinstance(data["train_chars"], int) or data["train_chars"] <= 0:
        return _failed("metrics", 20, "train_chars must be a positive integer.")
    if not isinstance(data["val_chars"], int) or data["val_chars"] <= 0:
        return _failed("metrics", 20, "val_chars must be a positive integer.")
    dataset_dir = Path(str(context.get("datasets_dir", "/datasets"))) / expected_dataset_id
    try:
        train_text = (dataset_dir / "train.txt").read_text(encoding="utf-8")
        val_text = (dataset_dir / "val.txt").read_text(encoding="utf-8")
    except Exception as exc:
        return _failed("metrics", 20, f"Could not read checker dataset files: {exc}")
    expected_vocab_size = len(set(train_text))
    if data["train_chars"] != len(train_text) or data["val_chars"] != len(val_text):
        return _failed("metrics", 20, "train_chars and val_chars must match the selected dataset.")
    if data["vocab_size"] != expected_vocab_size:
        return _failed("metrics", 20, "vocab_size must match the selected training text.")
    if not _finite_number(data["val_loss"]) or not _finite_number(data["perplexity"]):
        return _failed("metrics", 20, "val_loss and perplexity must be finite numbers.")
    return _passed("metrics", 20, "metrics.json matches the selected dataset and contains finite validation metrics.")

def _samples_check(context: dict[str, Any]) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "samples.json"))
    if error:
        return _failed("samples", 20, f"samples.json is not valid JSON: {error}")
    if not isinstance(data, dict):
        return _failed("samples", 20, "samples.json must contain a JSON object.")
    samples = data.get("samples")
    if not isinstance(samples, list) or len(samples) < 3:
        return _failed("samples", 20, "samples must contain at least 3 generated samples.")
    for sample in samples:
        if not isinstance(sample, dict):
            return _failed("samples", 20, "each sample must be an object.")
        generated_text = sample.get("generated_text")
        if not isinstance(generated_text, str) or not generated_text:
            return _failed("samples", 20, "each generated_text must be a non-empty string.")
    return _passed("samples", 20, "samples.json contains non-empty generated samples.")

def _artifact_size_check(oversized: list[str]) -> dict[str, Any]:
    if oversized:
        return _failed("artifact_sizes", 10, f"Oversized artifact(s): {', '.join(oversized)}")
    return _passed("artifact_sizes", 10, "Artifact sizes are within limits.")

def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value)
