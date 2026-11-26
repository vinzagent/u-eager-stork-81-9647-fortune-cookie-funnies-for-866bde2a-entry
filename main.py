"""Fortune Cookie Funnies for Engineers (u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a).

One original line, written as a single line for the make.fun judge-text
competition "Fortune Cookie Funnies for Engineers": a fortune cookie message for a software engineer.

The gate allows 1-120 characters, so refuse to ship anything longer,
anything blank, or anything that is not exactly one line.
"""

import os

LINE = (
    "Your Friday deploy will succeed. The bug it wakes at 3am has waited for you since 2019. Good luck sleeping tonight."
)

chars = len(LINE)
if chars < 1 or chars > 120:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-120 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
# The grader collects /output as another user, so the file must be
# world-readable: a default mkstemp-style 0600 mode fails "not readable".
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
