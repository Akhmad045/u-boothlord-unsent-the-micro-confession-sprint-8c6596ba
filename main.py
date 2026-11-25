#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — write one two-part
micro-confession to /output/entry.txt.

The confession is a message typed to a neighbour and never sent: the
sender hit the neighbour's dog in 2019 and has slowed down at the gate
every morning since, still without stopping to say it was them. The
To: line and the message need each other — the gate only makes sense
for that neighbour — and the reason it stayed in drafts is felt in
the daily ritual, never stated.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys

TO_LINE = "To: the neighbour whose dog I hit in 2019"
MESSAGE = ("I still slow down at your gate every single morning, and I "
           "still haven't stopped to say it was me.")

ENTRY = TO_LINE + "\n" + MESSAGE

MAX_CHARS = 260
MAX_MESSAGE_CHARS = 200


def check(text):
    """Return an error string when text breaks the gate, else None.

    Gate: 1 to 260 characters, not only whitespace, exactly two parts —
    a To: line naming who it was meant for, and the unsent message
    itself on one line of at most 200 characters, written exactly as
    typed, with no explanation after it.
    """
    if not isinstance(text, str):
        return "entry must be text"
    if len(text) == 0:
        return "entry is empty (gate needs 1-260 characters)"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 260-character gate" % len(text)
    if text.strip() == "":
        return "entry is only whitespace"
    if text.endswith("\n"):
        return "entry ends with a newline: the message line is empty"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\r" in text:
        return "entry must not contain a carriage return"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text if ch != "\n"):
        return "entry contains a control character"
    lines = text.split("\n")
    if len(lines) != 2:
        return "entry must be exactly two lines (To: line + message), got %d" % len(lines)
    to_line, message = lines
    if not to_line.startswith("To: "):
        return "first line must start with 'To: '"
    if to_line[4:].strip() == "":
        return "To: line names nobody"
    if message.strip() == "":
        return "message line is empty"
    if len(message) > MAX_MESSAGE_CHARS:
        return "message is %d characters, over the 200-character limit" % len(message)
    if message != message.strip():
        return "message has leading or trailing whitespace"
    return None


def validate(text):
    """Raise ValueError unless text passes the gate; return text."""
    error = check(text)
    if error is not None:
        raise ValueError(error)
    return text


def self_test():
    """Exercise check() against the gate's rejection and boundary cases."""
    reject = [
        ("", "empty"),
        ("   ", "whitespace-only"),
        ("x" * 261, "261 chars (over the 260 gate)"),
        ("To: Mum\n" + "y" * 201, "message 201 chars (over the 200 limit)"),
        ("To: Mum", "one line only"),
        ("To: Mum\none\ntwo", "three lines"),
        ("Mum\nhello", "first line without 'To: '"),
        ("To: \nhello", "To: line names nobody"),
        ("To: Mum\n", "empty message line"),
        ("To: Mum\n hello", "message leading whitespace"),
        ("To: Mum\nhello ", "message trailing whitespace"),
        ("To: Mum\nhello\rworld", "carriage return"),
        ("To: Mum\nhel\x00lo", "control character"),
        (" To: Mum\nhello", "leading whitespace overall"),
    ]
    for text, label in reject:
        error = check(text)
        if error is None:
            raise SystemExit("self-test FAIL: %s was accepted" % label)
        print("self-test ok: rejected %s: %s" % (label, error))
    for text, label in [
        ("To: A\nb", "minimal two-part entry"),
        ("To: Mum\n" + "z" * 200, "200-char message boundary"),
        ("To: " + "w" * 55 + "\n" + "z" * 200, "260-char total boundary"),
    ]:
        error = check(text)
        if error is not None:
            raise SystemExit("self-test FAIL: %s rejected: %s" % (label, error))
        print("self-test ok: %s accepted" % label)
    error = check(ENTRY)
    if error is not None:
        raise SystemExit("self-test FAIL: entry rejected: %s" % error)
    print("self-test ok: entry accepted (%d chars, message %d chars)"
          % (len(ENTRY), len(MESSAGE)))
    print("self-test: all cases passed")
    return 0


def main(argv):
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    if len(argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    text = validate(ENTRY)
    data = text.encode("utf-8")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the entry
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print("wrote %s: %d chars, sha256 %s"
          % (out_path, len(text), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
