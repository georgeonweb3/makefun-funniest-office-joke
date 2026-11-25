#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — make.fun entry.

Writes a single original funny line of text to /output/entry.txt:
Karen from Payroll's daily tuna-sandwich ritual since 2019 takes
an unexpected turn when she brings a second sandwich — for the
printer. The printer is the punchline, never the setup: no jam,
no deadline, just an offering.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "Karen from Payroll has eaten the same tuna sandwich at her desk "
    "every day since 2019; yesterday she brought a second one, looked "
    "me dead in the eye, and said, 'for the printer.'"
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 200 characters, not only whitespace — and one line:
    # an embedded newline would split the joke and break the gate.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate wants 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
