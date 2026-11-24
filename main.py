#!/usr/bin/env python3
"""Write one short dad joke for the make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5.

The joke is stored as a single string constant and written as UTF-8 bytes with
no trailing newline, so the entry file matches the chosen text byte for byte.
"""

import os
import sys
from pathlib import Path

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"

assert 1 <= len(TEXT) <= 280


def main() -> int:
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
