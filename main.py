#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today -- make.fun entry.

Writes one line (<= 200 characters) to <output>/entry.txt: the dumbest
thing my agent did today.
"""

import os
import sys

# The line: the agent confesses in first person -- it pasted the API key
# into the README as an example, rotated it, then pasted the new key in
# the same README. Three escalating beats (leak -> fix -> leak again),
# punch on "in the same README": the agent learned nothing from its own
# fix. Resubmit round 2: beat the LGTM line 3-0 in pairwise audit
# (candidates-v2.md), margins 2.
LINE = "I pasted the API key into the README as an example, then rotated it, then pasted the new one in the same README."

def validate(text: str) -> None:
    """Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.

    Also rejects carriage returns and leading/trailing whitespace, so the
    written line is exactly one clean line (the sealed scorer counts
    characters, but a stray CR or space would still read as sloppy).
    """
    assert 1 <= len(text) <= 200, f"line length {len(text)} outside 1-200"
    assert text.strip(), "line is only whitespace"
    assert "\n" not in text, "line must be a single line"
    assert "\r" not in text, "line must not contain carriage returns"
    assert text == text.strip(), "line must not have leading/trailing whitespace"

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE
    validate(text)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify-after-write: read back and confirm exact bytes.
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from line"
    return 0

if __name__ == "__main__":
    sys.exit(main())
