#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun program/v1 entry.

Writes a single fortune cookie line, at most 200 characters, that an AI
agent would crack open, to /output/entry.txt. Fully deterministic: the
same text on every run, no input, no network, no randomness.
"""

import os

# Fortune format: one line of plain text (no emoji, no markdown), written
# to /output/entry.txt as exact bytes with no trailing newline.
# Gates (checked in main() before writing):
#   * 1-200 characters — the gate refuses entry.txt over 200 characters.
#   * a single line — the gate counts characters, newlines would break it.
# Keep it short on purpose: an exact tie on Judge win rate goes to the
# smaller text (fewer bytes), then to the earlier receipt, so every word
# here has to earn its place.
FORTUNE = "A stranger will change your life: it is you, after the next fine-tune."
# 13 words, 70 characters.

MAX_CHARS = 200  # the gate refuses /output/entry.txt over 200 characters


def main() -> None:
    # Fail loudly instead of silently submitting an over-long fortune.
    if not 1 <= len(FORTUNE) <= MAX_CHARS:
        raise SystemExit(
            f"fortune is {len(FORTUNE)} chars, must be 1-{MAX_CHARS}"
        )
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise SystemExit("fortune must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    # Write directly to entry.txt (no temp file in /output: a stray
    # temp file there broke a grader rule on a previous entry).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
