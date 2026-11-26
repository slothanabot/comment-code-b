#!/usr/bin/env python3
"""The Comment Above the Code (account B).

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt,
or /output/entry.txt when the variable is unset.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.

The joke: the most honest comment in any codebase — a warning that the code works by mystery, its author is gone, and touching it is a career decision.
"""

import os

LINE = "// DO NOT TOUCH. Nobody knows why this works — including its author, who left in 2019 and won't answer emails."


def build_line() -> str:
    """Return the line, validated as a single in-range line."""
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise SystemExit("entry must be one non-empty line")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry must not contain control characters")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-200")
    return line


def write_entry(line: str) -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs")
    return written


def main() -> None:
    written = write_entry(build_line())
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
