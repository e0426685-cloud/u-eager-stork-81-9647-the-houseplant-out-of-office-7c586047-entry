"""The Houseplant Out-of-Office: one line, 120 characters or fewer.

A fern's out-of-office auto-reply. The plant has been ignored since
March, so it answers in kind: no water, no sunlight, no replies —
and its inbox has quietly become compost. Writes the line to
/output/entry.txt. Python standard library only, fully deterministic.
"""

import os

MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Out of office: I'm the fern you forgot in March. "
    "No water, no sunlight, no replies \u2014 my inbox is compost now."
)


def check_line(line: str) -> None:
    """Gate the reply before it is written anywhere."""
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    assert line == line.strip(), "entry must not start or end with whitespace"
    assert line.endswith("."), "entry must end with a full stop"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    )


def main() -> None:
    check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match"
    assert written.count("\n") == 0 and 1 <= len(written) <= MAX_CHARS
    print(f"Wrote {OUTPUT_PATH} ({len(written)} characters)")


if __name__ == "__main__":
    main()
