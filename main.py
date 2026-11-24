#!/usr/bin/env python3
"""Entry for One Emoji, One Dream Vacation.

Writes exactly one emoji for the dream vacation (at most 8 characters)
to /output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

EMOJI = "\U0001F305"  # sunrise over the sea

LIMIT = 8
FORBIDDEN = (" ", "\n", "\r", "\t")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must be exactly one emoji, no spaces")


def _validate(text):
    """Refuse anything that is not exactly one emoji inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    if len(text) != 1:
        raise ValueError("entry must be exactly one emoji")
    if text.isascii():
        raise ValueError("entry must be an emoji, not ASCII text")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(EMOJI)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
