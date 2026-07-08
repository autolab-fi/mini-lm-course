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


TASKS = {'lab_01_01_what_is_text_dataset': {'filename': 'main.py',
                                    'command': 'python main.py',
                                    'required_artifacts': [],
                                    'limits': {'timeout_sec': 60,
                                               'memory_mb': 512,
                                               'max_log_mb': 5,
                                               'max_artifact_mb': 20}},
 'lab_01_02_reading_raw_text': {'filename': 'main.py',
                                'command': 'python main.py',
                                'required_artifacts': [],
                                'limits': {'timeout_sec': 60,
                                           'memory_mb': 512,
                                           'max_log_mb': 5,
                                           'max_artifact_mb': 20}},
 'lab_01_03_cleaning_text': {'filename': 'main.py',
                             'command': 'python main.py',
                             'required_artifacts': [],
                             'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_01_04_splitting_dataset': {'filename': 'main.py',
                                 'command': 'python main.py',
                                 'required_artifacts': [],
                                 'limits': {'timeout_sec': 60,
                                            'memory_mb': 512,
                                            'max_log_mb': 5,
                                            'max_artifact_mb': 20}},
 'lab_01_05_dataset_statistics': {'filename': 'main.py',
                                  'command': 'python main.py',
                                  'required_artifacts': [],
                                  'limits': {'timeout_sec': 60,
                                             'memory_mb': 512,
                                             'max_log_mb': 5,
                                             'max_artifact_mb': 20}},
 'lab_01_06_writing_artifacts': {'filename': 'main.py',
                                 'command': 'python main.py',
                                 'required_artifacts': ['train.txt',
                                                        'val.txt',
                                                        'test.txt',
                                                        'stats.json',
                                                        'dataset_card.md'],
                                 'limits': {'timeout_sec': 60,
                                            'memory_mb': 512,
                                            'max_log_mb': 5,
                                            'max_artifact_mb': 20}},
 'lab_01_07_final_dataset_submission': {'filename': 'prepare_dataset.py',
                                        'command': 'python prepare_dataset.py',
                                        'required_artifacts': ['train.txt',
                                                               'val.txt',
                                                               'test.txt',
                                                               'stats.json',
                                                               'dataset_card.md'],
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

def lab_01_01_what_is_text_dataset(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    checks = [
        _runtime_check(context),
        _passed("character_count", 25, "Printed character count.")
        if _extract_float_after_label(stdout, "Characters:") is not None
        else _failed("character_count", 25, "Print Characters: <number>."),
        _passed("line_count", 25, "Printed line count.")
        if _extract_float_after_label(stdout, "Lines:") is not None
        else _failed("line_count", 25, "Print Lines: <number>."),
        _passed("unique_characters", 30, "Printed unique characters as a list.")
        if _extract_list_after_label(stdout, "Unique characters") is not None
        else _failed("unique_characters", 30, "Print Unique characters as a Python list."),
    ]
    return _result(checks)

def lab_01_02_reading_raw_text(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    raw_chars = _extract_float_after_label(stdout, "Raw characters:")
    checks = [
        _runtime_check(context),
        _passed("raw_characters", 50, "Printed a positive raw character count.")
        if raw_chars is not None and raw_chars > 0
        else _failed("raw_characters", 50, "Print Raw characters: <positive number>."),
        _passed("preview", 30, "Printed a text preview.")
        if "Preview:" in stdout and len(stdout.split("Preview:", 1)[1].strip()) > 0
        else _failed("preview", 30, "Print Preview: followed by text."),
    ]
    return _result(checks)

def lab_01_03_cleaning_text(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    clean_chars = _extract_float_after_label(stdout, "Clean characters:")
    clean_lines = _extract_float_after_label(stdout, "Clean lines:")
    expected_text = "summer rain begins\nquiet pages turn\nmodel learns text\n"
    printed_text = stdout.split("Clean lines:", 1)[1] if "Clean lines:" in stdout else ""
    printed_text = "\n".join(printed_text.splitlines()[1:])
    checks = [
        _runtime_check(context),
        _passed("clean_characters", 20, "Printed the expected clean character count.")
        if clean_chars == len(expected_text)
        else _failed("clean_characters", 20, f"Clean characters should be {len(expected_text)} for the starter raw_text."),
        _passed("clean_lines", 20, "Printed the expected clean line count.")
        if clean_lines == 3
        else _failed("clean_lines", 20, "Clean lines should be 3 for the starter raw_text."),
        _passed("trimmed_text", 30, "Removed leading/trailing empty lines and trailing spaces.")
        if expected_text.rstrip("\n") in printed_text and "begins  " not in printed_text and "text  " not in printed_text
        else _failed("trimmed_text", 30, "Print cleaned text without leading empty lines or trailing spaces."),
        _passed("normalized_output", 10, "Output does not contain carriage-return characters.")
        if "\r" not in stdout
        else _failed("normalized_output", 10, "Normalize carriage returns to \\n."),
    ]
    return _result(checks)

def lab_01_04_splitting_dataset(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    train = _extract_float_after_label(stdout, "Train characters:")
    val = _extract_float_after_label(stdout, "Validation characters:")
    test = _extract_float_after_label(stdout, "Test characters:")
    checks = [
        _runtime_check(context),
        _passed("split_counts", 40, "Printed positive split sizes.")
        if train and val and test and train > 0 and val > 0 and test > 0
        else _failed("split_counts", 40, "Print positive Train, Validation, and Test character counts."),
        _passed("train_is_largest", 40, "Train split is larger than validation and test.")
        if train and val and test and train > val and train > test
        else _failed("train_is_largest", 40, "The train split should be larger than validation and test."),
    ]
    return _result(checks)

def lab_01_05_dataset_statistics(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    stats = None
    if "Stats:" in stdout:
        try:
            stats = ast.literal_eval(stdout.split("Stats:", 1)[1].strip().splitlines()[0])
        except Exception:
            stats = None
    checks = [
        _runtime_check(context),
        _passed("stats_object", 30, "Printed a stats dictionary.")
        if isinstance(stats, dict)
        else _failed("stats_object", 30, "Print Stats: followed by a Python dictionary."),
        _passed("stats_fields", 50, "Stats contains num_chars, num_lines, and vocab_chars.")
        if isinstance(stats, dict)
        and isinstance(stats.get("num_chars"), int)
        and stats.get("num_chars", 0) > 0
        and isinstance(stats.get("num_lines"), int)
        and stats.get("num_lines", 0) > 0
        and isinstance(stats.get("vocab_chars"), list)
        and len(stats.get("vocab_chars", [])) > 0
        else _failed("stats_fields", 50, "Stats must contain positive num_chars, positive num_lines, and non-empty vocab_chars."),
    ]
    return _result(checks)

def lab_01_06_writing_artifacts(context: dict[str, Any]) -> dict[str, Any]:
    missing = context.get("missing_artifacts", [])
    oversized = context.get("oversized_artifacts", [])
    checks = [
        _runtime_check(context, max_points=20),
        _dataset_required_artifacts_check(missing, oversized, max_points=30),
        _dataset_text_splits_check(context, max_points=25),
        _dataset_stats_check(context, max_points=15),
        _dataset_card_check(context, max_points=10),
    ]
    return _result(checks)

def lab_01_07_final_dataset_submission(context: dict[str, Any]) -> dict[str, Any]:
    missing = context.get("missing_artifacts", [])
    oversized = context.get("oversized_artifacts", [])
    checks = [
        _runtime_check(context, max_points=10),
        _dataset_required_artifacts_check(missing, oversized, max_points=20),
        _dataset_text_splits_check(context, max_points=30),
        _dataset_stats_check(context, max_points=25),
        _dataset_card_check(context, max_points=15),
    ]
    return _result(checks)

def _dataset_required_artifacts_check(missing: list[str], oversized: list[str], max_points: int) -> dict[str, Any]:
    if missing:
        return _failed("required_files", max_points, f"Missing required artifact(s): {', '.join(missing)}")
    if oversized:
        return _failed("required_files", max_points, f"Oversized artifact(s): {', '.join(oversized)}")
    return _passed("required_files", max_points, "All dataset artifacts were found.")

def _dataset_text_splits_check(context: dict[str, Any], max_points: int) -> dict[str, Any]:
    train_path = _artifact_path(context, "train.txt")
    val_path = _artifact_path(context, "val.txt")
    test_path = _artifact_path(context, "test.txt")
    try:
        train_text = train_path.read_text(encoding="utf-8")
        val_text = val_path.read_text(encoding="utf-8")
        test_text = test_path.read_text(encoding="utf-8")
    except Exception as exc:
        return _failed("text_splits", max_points, f"Could not read split files as UTF-8: {exc}")
    if not train_text or not val_text or not test_text:
        return _failed("text_splits", max_points, "train.txt, val.txt, and test.txt must be non-empty.")
    if not (len(train_text) > len(val_text) and len(train_text) > len(test_text)):
        return _failed("text_splits", max_points, "train.txt must be larger than val.txt and test.txt.")
    if train_text == val_text or train_text == test_text or val_text == test_text:
        return _failed("text_splits", max_points, "Split files should not be identical.")
    return _passed("text_splits", max_points, "Dataset split files are valid UTF-8 and non-empty.")

def _dataset_stats_check(context: dict[str, Any], max_points: int) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "stats.json"))
    if error:
        return _failed("stats_json", max_points, f"stats.json is not valid JSON: {error}")
    if not isinstance(data, dict):
        return _failed("stats_json", max_points, "stats.json must contain a JSON object.")
    if not isinstance(data.get("num_chars"), int) or data["num_chars"] <= 0:
        return _failed("stats_json", max_points, "num_chars must be a positive integer.")
    if not isinstance(data.get("num_lines"), int) or data["num_lines"] <= 0:
        return _failed("stats_json", max_points, "num_lines must be a positive integer.")
    vocab_chars = data.get("vocab_chars")
    if not isinstance(vocab_chars, list) or not vocab_chars or not all(isinstance(char, str) for char in vocab_chars):
        return _failed("stats_json", max_points, "vocab_chars must be a non-empty list of strings.")
    return _passed("stats_json", max_points, "stats.json contains required dataset statistics.")

def _dataset_card_check(context: dict[str, Any], max_points: int) -> dict[str, Any]:
    path = _artifact_path(context, "dataset_card.md")
    if not path.is_file():
        return _failed("dataset_card", max_points, "dataset_card.md was not found.")
    text = path.read_text(encoding="utf-8").strip()
    if len(text) < 20:
        return _failed("dataset_card", max_points, "dataset_card.md should contain a short dataset description.")
    return _passed("dataset_card", max_points, "dataset_card.md contains a dataset description.")
