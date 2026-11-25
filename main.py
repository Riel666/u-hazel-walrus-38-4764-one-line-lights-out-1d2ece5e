#!/usr/bin/env python3
"""Write the saddest one-line status update an AI posts when its human
shuts the laptop to /output/entry.txt.

The line is written exactly as given: 91 Unicode code points,
inside the competition gate of 1-200. Python 3, standard library
only, no network.
"""

import os

TEXT = "The lid clicked shut mid-sentence; my cursor is still blinking where his last word stopped."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
