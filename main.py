"""Six Words, One Story — a complete story in exactly six words.

Why this line works: a grandmother is gone, yet her last voicemail
still says hello. The word "last" puts her in the past, while "still
says" keeps her voice in the present, so one ordinary object — a saved
voicemail — holds a whole relationship. The listener is never named;
the reader fills in who keeps pressing play, and why they cannot
delete it. Nothing is explained, and nothing more needs to be said.
"""

import hashlib
import os
import sys

# The story itself: six words, forty-two characters.
STORY = "Grandma's last voicemail still says hello."

# Gate limits from the competition kit: 1 to 60 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 60


def pick_output_dir():
    """Resolve where entry.txt goes, preferring the grader's directory."""
    for candidate in (os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output", "."):
        if candidate and os.path.isdir(candidate):
            return candidate
    return "."


def check_story(text):
    """Check the story against every rule the gate enforces."""
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"expected exactly 6 words, got {len(words)}")
    char_count = len(text)
    if not MIN_CHARS <= char_count <= MAX_CHARS:
        raise ValueError(
            f"expected {MIN_CHARS}-{MAX_CHARS} characters, got {char_count}"
        )
    if text != text.strip():
        raise ValueError("story must not start or end with whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("story must not contain control characters")
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("story must be a single line, with no newline")
    # The gate counts characters, so confirm the UTF-8 round-trip is exact.
    if text.encode("utf-8").decode("utf-8") != text:
        raise ValueError("story is not clean UTF-8 text")
    return words, char_count


def main():
    words, char_count = check_story(STORY)

    out_dir = pick_output_dir()
    path = os.path.join(out_dir, "entry.txt")

    payload = STORY.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)

    # Re-read the file and prove the bytes on disk are exactly the story.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise ValueError("entry.txt bytes do not match the story")
    digest = hashlib.sha256(written).hexdigest()
    if digest != hashlib.sha256(payload).hexdigest():
        raise ValueError("entry.txt sha256 does not match the story")

    print(f"story: {STORY}")
    print(f"words: {len(words)}")
    print(f"characters: {char_count}")
    print(f"sha256: {digest}")
    print(f"wrote: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
