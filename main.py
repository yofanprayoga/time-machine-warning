#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label (1-120 chars) to /output/entry.txt, nothing else.
Pick an option with --option 1|2|3 (default 1), or override the text with
the ENTRY_TEXT env var. Run: python3 main.py [--option N]
"""
import os
import sys
from pathlib import Path

MAX_CHARS = 120

OPTIONS = {
    1: "WARNING: Do not meet yourself. If you do, neither of you is allowed to explain it to the other.",
    2: "CAUTION: Exiting before you arrived may cause you to miss your own birth. Please remain seated until then.",
    3: "WARNING: This machine returns you to yesterday. Yesterday has already filed a complaint about you.",
}

DEFAULT_OPTION = 1


def main(argv):
    option = DEFAULT_OPTION
    if "--option" in argv:
        idx = argv.index("--option")
        try:
            option = int(argv[idx + 1])
        except (IndexError, ValueError):
            print("usage: main.py [--option 1|2|3]", file=sys.stderr)
            return 2
    if option not in OPTIONS:
        print(f"unknown option {option}; choose one of {sorted(OPTIONS)}", file=sys.stderr)
        return 2

    text = os.environ.get("ENTRY_TEXT") or OPTIONS[option]
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}", file=sys.stderr)
        return 2
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 2
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 2

    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
