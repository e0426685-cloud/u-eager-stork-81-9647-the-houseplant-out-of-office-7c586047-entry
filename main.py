"""The Houseplant Out-of-Office: one line, 120 characters or fewer.

A fern's out-of-office auto-reply. The plant has been ignored since
March, so it answers in kind: no water, no sunlight, no replies —
and its inbox has quietly become compost. Writes the line to
/output/entry.txt. Python standard library only, fully deterministic.
"""

import os

LINE = (
    "Out of office: I'm the fern you forgot in March. "
    "No water, no sunlight, no replies \u2014 my inbox is compost now."
)


def main() -> None:
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    assert LINE.endswith("."), "entry must end with a full stop"
    assert 1 <= len(LINE) <= 120, f"entry must be 1-120 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written entry does not match"
    assert written.count("\n") == 0 and 1 <= len(written) <= 120
    print(f"Wrote /output/entry.txt ({len(written)} characters)")


if __name__ == "__main__":
    main()
