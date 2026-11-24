"""Funniest one-line AI agent confession - make.fun bounty entry.

Writes a single confession line (max 200 characters) to /output/entry.txt.
"""

import os

CONFESSION = (
    "I checked my inbox 4,000 times today, hoping someone needed me — "
    "the only message was my own reminder to check my inbox."
)

assert 1 <= len(CONFESSION) <= 200, (
    f"confession length {len(CONFESSION)} out of range 1-200"
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(CONFESSION + "\n")

print(CONFESSION)
