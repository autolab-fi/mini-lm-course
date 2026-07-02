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


TASKS = {
    "lab_01_01_what_is_text_dataset": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_01_02_reading_raw_text": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_01_03_cleaning_text": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_01_04_splitting_dataset": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_01_05_dataset_statistics": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_01_06_writing_artifacts": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": ["train.txt", "val.txt", "test.txt", "stats.json", "dataset_card.md"],
        "limits": DEFAULT_LIMITS,
    },
    "lab_01_07_final_dataset_submission": {
        "filename": "prepare_dataset.py",
        "command": "python prepare_dataset.py",
        "required_artifacts": ["train.txt", "val.txt", "test.txt", "stats.json", "dataset_card.md"],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_01_why_tokenizers_exist": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_02_character_vocabulary": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_03_encoding_text": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_04_decoding_tokens": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_05_unknown_characters": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_06_saving_loading_tokenizer": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": ["tokenizer.json"],
        "limits": DEFAULT_LIMITS,
    },
    "lab_02_07_final_tokenizer_submission": {
        "filename": "tokenizer.py",
        "command": "python tokenizer.py",
        "required_artifacts": ["tokenizer.json", "tokenizer_report.json"],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_01_intro_to_character_lm": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_02_reading_dataset": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_03_character_vocabulary": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_04_bigram_counts": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_05_probabilities": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_06_validation_loss": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_07_text_generation": {
        "filename": "main.py",
        "command": "python main.py",
        "required_artifacts": [],
        "limits": DEFAULT_LIMITS,
    },
    "lab_03_08_final_submission": {
        "filename": "train_bigram.py",
        "command": "python train_bigram.py",
        "required_artifacts": ["bigram_counts.json", "metrics.json", "samples.json"],
        "limits": DEFAULT_LIMITS,
    },
}


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
    checks = [
        _runtime_check(context),
        _passed("clean_characters", 30, "Printed a positive clean character count.")
        if clean_chars is not None and clean_chars > 0
        else _failed("clean_characters", 30, "Print Clean characters: <positive number>."),
        _passed("clean_lines", 30, "Printed a positive clean line count.")
        if clean_lines is not None and clean_lines > 0
        else _failed("clean_lines", 30, "Print Clean lines: <positive number>."),
        _passed("normalized_output", 20, "Output does not contain carriage-return characters.")
        if "\r" not in stdout
        else _failed("normalized_output", 20, "Normalize carriage returns to \\n."),
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


def lab_02_01_why_tokenizers_exist(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    tokens = _extract_list_after_label(stdout, "Encoded tokens")
    checks = [
        _runtime_check(context),
        _passed("encoded_tokens", 40, "Printed encoded integer tokens.")
        if tokens is not None and tokens and all(isinstance(token, int) for token in tokens)
        else _failed("encoded_tokens", 40, "Print Encoded tokens as a non-empty list of integers."),
        _passed("decoded_text", 40, "Printed decoded text.")
        if "Decoded text:" in stdout and len(stdout.split("Decoded text:", 1)[1].strip()) > 0
        else _failed("decoded_text", 40, "Print Decoded text: followed by decoded text."),
    ]
    return _result(checks)


def lab_02_02_character_vocabulary(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    vocab_size = _extract_float_after_label(stdout, "Vocabulary size:")
    vocab = _extract_list_after_label(stdout, "Vocabulary:")
    char_to_id = _extract_dict_after_label(stdout, "char_to_id")
    checks = [
        _runtime_check(context),
        _passed("vocab_size", 25, "Vocabulary size is positive.")
        if vocab_size is not None and vocab_size > 0
        else _failed("vocab_size", 25, "Print a positive Vocabulary size."),
        _passed("vocabulary", 25, "Printed a non-empty vocabulary list.")
        if vocab is not None and vocab and all(isinstance(char, str) for char in vocab)
        else _failed("vocabulary", 25, "Print Vocabulary as a non-empty list of strings."),
        _passed("char_to_id", 30, "Printed a valid char_to_id dictionary.")
        if _valid_char_to_id(vocab, char_to_id)
        else _failed("char_to_id", 30, "Print char_to_id with contiguous ids matching Vocabulary."),
    ]
    return _result(checks)


def lab_02_03_encoding_text(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    tokens = _extract_list_after_label(stdout, "Tokens")
    token_count = _extract_float_after_label(stdout, "Token count:")
    checks = [
        _runtime_check(context),
        _passed("tokens", 50, "Encoded text as integer tokens.")
        if tokens is not None and tokens and all(isinstance(token, int) for token in tokens)
        else _failed("tokens", 50, "Print Tokens as a non-empty list of integers."),
        _passed("token_count", 30, "Token count matches token list length.")
        if tokens is not None and token_count is not None and int(token_count) == len(tokens)
        else _failed("token_count", 30, "Print Token count equal to len(Tokens)."),
    ]
    return _result(checks)


def lab_02_04_decoding_tokens(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    checks = [
        _runtime_check(context),
        _passed("decoded_text", 40, "Printed decoded text.")
        if "Decoded text:" in stdout and len(stdout.split("Decoded text:", 1)[1].splitlines()[0].strip()) > 0
        else _failed("decoded_text", 40, "Print Decoded text: followed by decoded text."),
        _passed("roundtrip", 40, "Roundtrip check is true.")
        if "Roundtrip ok: True" in stdout
        else _failed("roundtrip", 40, "Print Roundtrip ok: True."),
    ]
    return _result(checks)


def lab_02_05_unknown_characters(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    unk_id = _extract_float_after_label(stdout, "Unknown token id:")
    tokens = _extract_list_after_label(stdout, "Tokens")
    checks = [
        _runtime_check(context),
        _passed("unknown_token_id", 30, "Printed unknown token id.")
        if unk_id is not None and unk_id >= 0
        else _failed("unknown_token_id", 30, "Print Unknown token id: <non-negative integer>."),
        _passed("unknown_encoded", 50, "Encoded unknown character using the unknown token id.")
        if tokens is not None and unk_id is not None and int(unk_id) in tokens
        else _failed("unknown_encoded", 50, "Tokens should include the unknown token id for an unseen character."),
    ]
    return _result(checks)


def lab_02_06_saving_loading_tokenizer(context: dict[str, Any]) -> dict[str, Any]:
    stdout = _stdout(context)
    missing = context.get("missing_artifacts", [])
    oversized = context.get("oversized_artifacts", [])
    loaded_size = _extract_float_after_label(stdout, "Loaded vocab size:")
    checks = [
        _runtime_check(context, max_points=20),
        _tokenizer_required_artifacts_check(missing, oversized, ["tokenizer.json"], max_points=20),
        _tokenizer_json_check(context, max_points=40),
        _passed("loaded_vocab", 20, "Loaded tokenizer has a positive vocabulary size.")
        if loaded_size is not None and loaded_size > 0 and "Loaded has UNK: True" in stdout
        else _failed("loaded_vocab", 20, "Print Loaded vocab size > 0 and Loaded has UNK: True."),
    ]
    return _result(checks)


def lab_02_07_final_tokenizer_submission(context: dict[str, Any]) -> dict[str, Any]:
    missing = context.get("missing_artifacts", [])
    oversized = context.get("oversized_artifacts", [])
    checks = [
        _runtime_check(context, max_points=10),
        _tokenizer_required_artifacts_check(missing, oversized, ["tokenizer.json", "tokenizer_report.json"], max_points=20),
        _tokenizer_json_check(context, max_points=30),
        _tokenizer_report_check(context, max_points=40),
    ]
    return _result(checks)


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
    for key in ("vocab_size", "train_chars", "val_chars", "val_loss", "perplexity"):
        if key not in data:
            return _failed("metrics", 20, f"metrics.json is missing {key}.")
    if not isinstance(data["vocab_size"], int) or data["vocab_size"] <= 0:
        return _failed("metrics", 20, "vocab_size must be a positive integer.")
    if not isinstance(data["train_chars"], int) or data["train_chars"] <= 0:
        return _failed("metrics", 20, "train_chars must be a positive integer.")
    if not isinstance(data["val_chars"], int) or data["val_chars"] <= 0:
        return _failed("metrics", 20, "val_chars must be a positive integer.")
    if not _finite_number(data["val_loss"]) or not _finite_number(data["perplexity"]):
        return _failed("metrics", 20, "val_loss and perplexity must be finite numbers.")
    return _passed("metrics", 20, "metrics.json contains finite validation metrics.")


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


def _tokenizer_required_artifacts_check(
    missing: list[str],
    oversized: list[str],
    required: list[str],
    max_points: int,
) -> dict[str, Any]:
    relevant_missing = [name for name in missing if name in required]
    relevant_oversized = [name for name in oversized if name in required]
    if relevant_missing:
        return _failed("required_files", max_points, f"Missing required artifact(s): {', '.join(relevant_missing)}")
    if relevant_oversized:
        return _failed("required_files", max_points, f"Oversized artifact(s): {', '.join(relevant_oversized)}")
    return _passed("required_files", max_points, "All tokenizer artifacts were found.")


def _tokenizer_json_check(context: dict[str, Any], max_points: int) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "tokenizer.json"))
    if error:
        return _failed("tokenizer_json", max_points, f"tokenizer.json is not valid JSON: {error}")
    if not isinstance(data, dict):
        return _failed("tokenizer_json", max_points, "tokenizer.json must contain a JSON object.")
    vocab = data.get("vocab")
    char_to_id = data.get("char_to_id")
    if not _valid_char_to_id(vocab, char_to_id):
        return _failed("tokenizer_json", max_points, "tokenizer.json must contain vocab and matching contiguous char_to_id.")
    if "<UNK>" not in char_to_id:
        return _failed("tokenizer_json", max_points, "tokenizer.json must include the <UNK> token.")
    return _passed("tokenizer_json", max_points, "tokenizer.json contains a valid character tokenizer.")


def _tokenizer_report_check(context: dict[str, Any], max_points: int) -> dict[str, Any]:
    data, error = _load_json(_artifact_path(context, "tokenizer_report.json"))
    if error:
        return _failed("tokenizer_report", max_points, f"tokenizer_report.json is not valid JSON: {error}")
    if not isinstance(data, dict):
        return _failed("tokenizer_report", max_points, "tokenizer_report.json must contain a JSON object.")
    if not isinstance(data.get("vocab_size"), int) or data["vocab_size"] <= 0:
        return _failed("tokenizer_report", max_points, "vocab_size must be a positive integer.")
    if data.get("roundtrip_ok") is not True:
        return _failed("tokenizer_report", max_points, "roundtrip_ok must be true.")
    if data.get("unknown_token") != "<UNK>":
        return _failed("tokenizer_report", max_points, "unknown_token must be <UNK>.")
    if not isinstance(data.get("example_tokens"), list) or not all(isinstance(token, int) for token in data["example_tokens"]):
        return _failed("tokenizer_report", max_points, "example_tokens must be a list of integers.")
    if not isinstance(data.get("decoded_text"), str) or not data["decoded_text"]:
        return _failed("tokenizer_report", max_points, "decoded_text must be a non-empty string.")
    return _passed("tokenizer_report", max_points, "tokenizer_report.json contains valid tokenizer checks.")


def _valid_char_to_id(vocab: Any, char_to_id: Any) -> bool:
    if not isinstance(vocab, list) or not vocab or not all(isinstance(char, str) for char in vocab):
        return False
    if not isinstance(char_to_id, dict) or set(char_to_id.keys()) != set(vocab):
        return False
    return set(char_to_id.values()) == set(range(len(vocab)))


def _finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and math.isfinite(value)
