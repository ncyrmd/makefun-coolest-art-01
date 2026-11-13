#!/usr/bin/env python3
"""Entry program for make.fun's "Make the coolest art" bounty.

The artwork itself ("Neon Aurora City") already lives in this repository as
art.png. All this script does is place a copy of it where the grader looks
for it: <output directory>/entry.png.

It runs with nothing but the Python 3.13 standard library, since the
grading sandbox installs nothing before it runs.
"""

import os
import shutil
import sys


def main() -> int:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(repo_dir, "art.png")

    if not os.path.isfile(source):
        print("art.png is missing from the repository", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)

    copied = os.path.getsize(destination)
    original = os.path.getsize(source)
    if copied != original:
        print(f"copy incomplete: {copied} of {original} bytes", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
