#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — v2 entry.

Winner: "My Smoke Detector Detects Sleep" (272 chars). Chosen from 7
candidates because its mechanism is the most different from the crowded
board (no password/auth, typo, self-checkout or traffic angles): a safety
device that only chirps at 3 a.m., whose beep migrates between detectors,
capped by the reframe "It doesn't detect smoke. It detects sleep."

Output contract: writes exactly RANT (UTF-8, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it to stdout.
"""

import os
from pathlib import Path

# Resubmit v2 (25 Nov 2026): new rant, counts from round 2; Force_Last replaces v1.
RANT = "My smoke detector only beeps at 3 a.m. One chirp. Then silence. I stand on a chair, ear to the ceiling, waiting for the next one — which comes 47 minutes later, from a DIFFERENT detector. By morning, all four are silent and smug. It doesn't detect smoke. It detects sleep."

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / OUTPUT_FILENAME
    path.write_text(RANT, encoding="utf-8")
    print(RANT)


if __name__ == "__main__":
    main()
