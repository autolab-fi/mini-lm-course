# Lab 02: Character Tokenizer

## Objective

Понять, как текст превращается в последовательность token ids и обратно.

## Task

Реализуйте символьный tokenizer. Он должен строить vocabulary по training text, кодировать строки в integer token ids и восстанавливать исходный текст через decode.

## Required API

```python
encode(text: str) -> list[int]
decode(tokens: list[int]) -> str
save_tokenizer(path: str) -> None
load_tokenizer(path: str) -> Tokenizer
```

## Required Artifacts

```text
tokenizer.json
tokenizer_report.json
```

## `tokenizer.json` Suggested Format

```json
{
  "vocab": ["\n", " ", "a", "b"],
  "char_to_id": {
    "\n": 0,
    " ": 1,
    "a": 2,
    "b": 3
  }
}
```

## Checks

Grader будет проверять:

- `encode` returns a list of integers;
- `decode(encode(text)) == text` for known text;
- newline, punctuation and empty string work;
- unknown characters are handled or documented;
- `tokenizer.json` is valid JSON.

## Submission Notes

Следующая лабораторная будет использовать идею next-character prediction, поэтому убедитесь, что порядок символов в vocabulary стабилен и сохраняется в `tokenizer.json`.
