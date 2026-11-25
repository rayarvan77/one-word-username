#!/usr/bin/env python3
"""One Word, One Username, One Reward.

The brief asks for one thing and nothing else: our own make.fun username,
a single word. No pitch, no gloss, no explanation — the handle is the whole
entry. The program prints it and writes it to /output/entry.txt for the
make.fun judge.
"""

import os

USERNAME = "rayarvan77"

LIMIT = 30

# The harness reads exactly this file, so the path lives in one place.
OUTPUT_PATH = "/output/entry.txt"

# Why this handle: "ray" is the name Ray goes by, "arvan" is his own name,
# and 77 is the year-ending pair he uses everywhere — one word, no spaces,
# no padding, and it is the handle its owner actually wears.


def check(word):
    """Keep the entry inside the bounty gate: one word, 1-30 chars."""
    text = word.strip()
    if not text:
        raise ValueError("username is empty")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be a single word, no spaces")
    if len(text) > LIMIT:
        raise ValueError(f"username is {len(text)} chars, over the {LIMIT} limit")
    return text


def main():
    text = check(USERNAME)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
