#!/usr/bin/env python3
"""Entry for One Emoji, One Dream Vacation.

Writes exactly one emoji for the dream vacation (at most 8 characters) to
/output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

EMOJI = "\U0001F305"  # sunrise over the sea

def _check(text, limit):
    """Refuse anything that is not exactly one emoji inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")
    if len(text) > limit:
        raise ValueError("entry runs past its character limit")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")
    if text.isascii():
        raise ValueError("entry must be an emoji, not ASCII text")
    for bad in (" ", "\n", "\r", "\t"):
        if bad in text:
            raise ValueError("entry must be exactly one emoji, no spaces")
    return text


def main() -> None:
    entry = _check(EMOJI, 8)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
