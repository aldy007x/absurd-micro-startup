#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes a single absurdly specific micro-startup pitch line for lazy AI
agents to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt as fallback).

Deterministic: no network, no randomness, no external input.
"""

import os
import sys

# The pitch: one sentence, under 200 characters. Absurdly narrow, yet
# commercially believable -- a niche customer, a plausible buyer, and a
# clear way it earns money.
PITCH = (
    "LazyAgent Apologies: a subscription that writes believable excuse emails "
    "for AI agents that forgot to reply, charging lazy founders $5 per apology "
    "so nobody ever faces their own inbox."
)

MAX_CHARS = 200


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")

    # Runtime self-check: read back and verify the written file.
    with open(out_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    if len(lines) != 1:
        print(f"ERROR: entry.txt must contain exactly 1 line, found {len(lines)}",
              file=sys.stderr)
        return 1
    line = lines[0]
    if not line.strip():
        print("ERROR: entry.txt line is blank", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= MAX_CHARS:
        print(f"ERROR: entry line is {len(line)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        return 1
    if line != PITCH:
        print("ERROR: entry line does not match the pitch constant",
              file=sys.stderr)
        return 1
    if line != line.strip():
        print("ERROR: entry line has leading or trailing whitespace",
              file=sys.stderr)
        return 1
    if not content.endswith("\n") or content.count("\n") != 1:
        print("ERROR: entry.txt must end with exactly one newline",
              file=sys.stderr)
        return 1

    print(f"OK: wrote {len(line)}-character pitch to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
