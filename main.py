"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
``entry.txt`` inside the directory named by MAKEFUN_OUTPUT_DIR
(falling back to the current directory when unset).
"""

import os

# One line, 103 characters: the paradox is the setup, the refund policy
# is the joke, and the sting lands on the last two words.
ENTRY = (
    "WARNING: Passengers who prevent their own birth forfeit their refund. "
    "No exceptions for the never-born."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
