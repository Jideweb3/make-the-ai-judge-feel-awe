"""Contest entry: writes one short text to /output/entry.txt."""

import os

TEXT = (
    "Somewhere tonight the sea is doing its slow work, wave by wave, "
    "asking nothing. A lighthouse turns. A small boat rests at anchor. "
    "Nothing is urgent, nothing is owed. The tide comes in, the tide "
    "goes out \u2014 it has never once been late, and neither are you."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)

    # Self-check: re-read what was written and verify it is a short,
    # non-blank text (1 to 280 Unicode code points).
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    count = len(written)
    assert 1 <= count <= 280, f"entry is {count} code points, must be 1..280"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
