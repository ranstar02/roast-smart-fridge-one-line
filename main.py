#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single-line roast of a smart fridge to /output/entry.txt.
Deterministic, no network, no secrets, no dynamic imports.
"""

import os

ROAST = (
    "My smart fridge locked itself for a firmware update at midnight, "
    "holding my leftovers hostage — the patch notes just say "
    "'improved freshness'."
)


def main() -> None:
    if not (1 <= len(ROAST) <= 160):
        raise ValueError(
            f"Roast must be 1-160 characters, got {len(ROAST)}"
        )
    if not ROAST.strip():
        raise ValueError("Roast must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)
    print(ROAST)
    print(f"({len(ROAST)} characters)")


if __name__ == "__main__":
    main()
