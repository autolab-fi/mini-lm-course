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


TASKS = {'lab_02_01_why_tokenizers_exist': {'filename': 'main.py',
                                    'command': 'python main.py',
                                    'required_artifacts': [],
                                    'limits': {'timeout_sec': 60,
                                               'memory_mb': 512,
                                               'max_log_mb': 5,
                                               'max_artifact_mb': 20}},
 'lab_02_02_character_vocabulary': {'filename': 'main.py',
                                    'command': 'python main.py',
                                    'required_artifacts': [],
                                    'limits': {'timeout_sec': 60,
                                               'memory_mb': 512,
                                               'max_log_mb': 5,
                                               'max_artifact_mb': 20}},
 'lab_02_03_encoding_text': {'filename': 'main.py',
                             'command': 'python main.py',
                             'required_artifacts': [],
                             'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_02_04_decoding_tokens': {'filename': 'main.py',
                               'command': 'python main.py',
                               'required_artifacts': [],
                               'limits': {'timeout_sec': 60, 'memory_mb': 512, 'max_log_mb': 5, 'max_artifact_mb': 20}},
 'lab_02_05_unknown_characters': {'filename': 'main.py',
                                  'command': 'python main.py',
                                  'required_artifacts': [],
                                  'limits': {'timeout_sec': 60,
                                             'memory_mb': 512,
                                             'max_log_mb': 5,
                                             'max_artifact_mb': 20}},
 'lab_02_06_saving_loading_tokenizer': {'filename': 'main.py',
                                        'command': 'python main.py',
                                        'required_artifacts': ['tokenizer.json'],
                                        'limits': {'timeout_sec': 60,
                                                   'memory_mb': 512,
                                                   'max_log_mb': 5,
                                                   'max_artifact_mb': 20}},
 'lab_02_07_final_tokenizer_submission': {'filename': 'tokenizer.py',
                                          'command': 'python tokenizer.py',
                                          'required_artifacts': ['tokenizer.json', 'tokenizer_report.json'],
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
