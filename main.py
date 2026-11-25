#!/usr/bin/env python3
"""The 3AM Fridge Text - a make.fun entry.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
the text message a smart fridge sends its owner at 3am.
Stdlib only.
"""
import os

LINE = (
    "3:00 AM report: Sunday's leftovers have formed a government. "
    "They voted 6 to 1. You no longer control the top shelf."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
