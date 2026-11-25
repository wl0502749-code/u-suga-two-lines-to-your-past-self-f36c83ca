#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes the entry to /output/entry.txt: line one warns the past self about
one specific moment; line two says why that moment mattered.
"""

import os

ENTRY = (
    "When Dad says 'stay for dinner' on your last night home "
    "before the night bus, stay.\n"
    "He never asked again, and every missed call since "
    "has been you trying to finish that meal.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    print(f"wrote /output/entry.txt ({len(text)} chars)")
    print(text)


if __name__ == "__main__":
    main()
