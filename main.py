#!/usr/bin/env python3
"""The 3 AM Excuse.

Writes one line to /output/entry.txt: the excuse a hardware wallet gives
for refusing to sign a transaction at 3 AM, in the wallet's own voice.

The line is a fixed, hand-written string. The program makes no network
calls, reads no input files and takes no arguments: it validates the
competition gate itself (1 to 200 characters, UTF-8 text, not only
whitespace) and then writes the line exactly as written, with no
trailing newline.
"""

ENTRY = "You only wake me at 3 AM to sign things you'll regret by breakfast. I've read your history. I refuse."

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the entry line, checked against the competition gate."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    return line


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to path and return it."""
    line = build_entry()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return line


if __name__ == "__main__":
    written = write_entry()
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
