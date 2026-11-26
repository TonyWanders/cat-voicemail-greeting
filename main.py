#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting - make.fun entry.

Writes the one-line voicemail greeting a cat would record to
/output/entry.txt (or the path given as the first argument, or $OUTPUT_PATH).
Deterministic: the same line on every run.
"""

import os
import sys

ENTRY = "Hi, you've reached Mittens. I'm busy knocking things off tables. Leave a message, and I'll ignore it from a sunbeam."

DEFAULT_OUTPUT = "/output/entry.txt"


def write_entry(path, text):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)
    write_entry(path, ENTRY)


if __name__ == "__main__":
    main()
