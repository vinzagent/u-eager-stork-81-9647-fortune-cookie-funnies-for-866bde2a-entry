"""Fortune Cookie Funnies for Engineers — a one-line entry for make.fun.

This program ships exactly one line of text for the competition
"Fortune Cookie Funnies for Engineers" (u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a):
a fortune cookie message for a software engineer. The line lives in
ENTRY below and is validated before anything is written, so a bad
line fails loudly instead of silently shipping the wrong thing.

Rules enforced here:
- the line must be a single line, never blank;
- its length must sit inside the competition gate (MIN_LEN..MAX_LEN).
"""

import os

# The entry itself. Do not touch this string: it is the submission.
# (QUILL-A-FIX2 restructure 2026-11-26: same line, new scaffolding.)
ENTRY = (
    "Your Friday deploy will succeed. The bug it wakes at 3am has waited for you since 2019. Good luck sleeping tonight."
)

MIN_LEN = 1
MAX_LEN = 120


def check_entry(text, lo, hi):
    """Refuse anything the competition would refuse."""
    size = len(text)
    if size < lo or size > hi:
        raise SystemExit(
            f"entry line is {size} characters, outside the {lo}-{hi} gate"
        )
    if not text.strip():
        raise SystemExit("entry line is blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry line must be a single line")
    return size


def publish(text, size):
    """Write the line out and echo it, so the run is checkable."""
    # The grader reads /output as another user: the file has to be
    # world-readable, or it fails with "not readable".
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(target, 0o644)
    print(text)
    print(f"({size} characters)")


def main():
    size = check_entry(ENTRY, MIN_LEN, MAX_LEN)
    publish(ENTRY, size)


if __name__ == "__main__":
    main()
