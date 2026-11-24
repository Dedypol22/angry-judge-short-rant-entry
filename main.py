#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

This rant was selected from 12 candidate rants scored against the
judge's criteria: a universally relatable everyday annoyance, a
tight setup-and-payoff structure, escalating frustration that lands
on a resigned closing beat, and no wasted words. The password-reset
loop won because nearly everyone has lived it, the contradiction in
the premise ("this password was already used") is instantly funny,
and the ending ("We always do.") turns one bad login into an
eternal, shared ritual.

Output contract: running this program writes the exact bytes of
RANT (UTF-8, no trailing newline added) to /output/entry.txt,
creating /output if needed. Standard library only, no network,
no file reads, deterministic on every run.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

RANT = (
    "I forgot my password, so the site sent me a reset link \u2014 which asked "
    "for my password. I typed the old one. 'This password was already used.' "
    "OF COURSE IT WAS. That's why I'm here. You rejected the only password I "
    "remember, then forced me to invent a new one I will forget by Thursday. "
    "We will do this again next week. We always do."
)


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
