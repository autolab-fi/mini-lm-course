---
index: 2
module: module_1
task: lab_01_03_cleaning_text
previous: lab_01_02_reading_raw_text
next: lab_01_04_splitting_dataset
---

# Lab 01.3: Cleaning Text

## Objective

Normalize simple text formatting before creating dataset splits.

## Introduction

Raw text often contains inconsistent newlines and extra spaces. We do not need complex cleaning in this course, but we do want predictable text.

For this lab, cleaning means:

1. normalize Windows newlines `\r\n` to `\n`;
2. remove trailing spaces on each line;
3. remove empty lines at the beginning or end;
4. keep one final newline.

## Theory

### Newlines

Different systems may write line breaks differently:

```text
\n    Unix/Linux/macOS
\r\n  Windows
```

We normalize both to `\n`.

## Python Tools Used

- `text.replace(old, new)` replaces one substring with another. Docs: https://docs.python.org/3/library/stdtypes.html#str.replace
- `line.rstrip()` removes whitespace from the right side of a line. Docs: https://docs.python.org/3/library/stdtypes.html#str.rstrip
- `text.strip()` removes whitespace from both ends of a string. Docs: https://docs.python.org/3/library/stdtypes.html#str.strip
- `"\\n".join(lines)` joins strings with newline separators. Docs: https://docs.python.org/3/library/stdtypes.html#str.join

## Assignment

Implement:

```python
clean_text(text)
```

Then print:

```text
Clean characters: <number>
Clean lines: <number>
```

## Conclusion

You now have predictable text that is easier to split and check.
