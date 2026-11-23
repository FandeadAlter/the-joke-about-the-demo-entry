"""Write a one-line joke about working beside AI coding agents.

The joke is written byte-exact to /output/entry.txt (UTF-8, no trailing
newline): 100 Unicode code points, 102 UTF-8 bytes.

Run: python3 main.py
"""

import os

JOKE = "I told my agent 'just make it work for the demo' \u2014 it hardcoded my slides, my applause, and the Q&A."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Self-check: the file must hold exactly the joke, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == JOKE, "entry.txt does not match the joke exactly"
    assert len(written) == 100, "joke must be 100 characters"
    assert len(written.encode("utf-8")) == 102, "joke must be 102 UTF-8 bytes"


if __name__ == "__main__":
    main()
