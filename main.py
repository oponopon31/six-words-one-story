#!/usr/bin/env python3
"""Entry for make.fun competition u-deranalabs-six-words-one-story-f982e410.

Writes one six-word story (1-60 characters) to entry.txt in the output
directory. Pure standard library, deterministic, no network.

Why this text: a grandmother is gone, but her last voicemail is still
there, still saying hello every time it is played. The past ("last")
and the present ("still says") collide in one line: the story is a
whole relationship — a grandchild who keeps listening — told through a
single ordinary object. Nothing is spelled out: who listens, how often,
and what the call was about are all left for the reader to fill in.
The present tense does the work — "still says" keeps her voice in the
room now, not in the past. At 42 characters the line is also compact,
which matters because an exact tie on win rate goes to the smaller text.
"""

import hashlib
import os

TEXT = "Grandma's last voicemail still says hello."

FILENAME = "entry.txt"


def write_and_verify(text: str, out_dir: str) -> tuple[str, str]:
    """Write text to entry.txt in out_dir, then re-read and verify it.

    Returns (path, sha256 hex digest) of the written file.
    """
    data = text.encode("utf-8")
    data.decode("utf-8")  # validate UTF-8 round-trip

    path = os.path.join(out_dir, FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    with open(path, "rb") as f:
        written = f.read()
    digest = hashlib.sha256(data).hexdigest()
    assert written == data, "entry.txt bytes differ from intended text"
    assert hashlib.sha256(written).hexdigest() == digest, "sha256 mismatch"
    return path, digest


def main() -> None:
    text = TEXT
    words = text.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    count = len(text)
    assert 1 <= count <= 60, f"text length {count} out of range 1-60"
    assert text.strip(), "text must not be only whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = "."
    path, digest = write_and_verify(text, out_dir)

    print(f"words: {len(words)}")
    print(f"chars: {count}")
    print(f"sha256: {digest}")
    print(f"wrote: {path}")
    print("verified: entry.txt bytes match the text exactly")


if __name__ == "__main__":
    main()
