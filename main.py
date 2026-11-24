#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Standard library only, no network, no file reads.
"""

import os

RANT = (
    "I forgot my password, so the site sent me a reset link \u2014 which asked "
    "for my password. I typed the old one. 'This password was already used.' "
    "OF COURSE IT WAS. That's why I'm here. You rejected the only password I "
    "remember, then forced me to invent a new one I will forget by Thursday. "
    "We will do this again next week. We always do."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
