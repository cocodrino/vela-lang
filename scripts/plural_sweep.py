#!/usr/bin/env python3
"""Sweep legacy plural -s in docs/texts and grammar into new plural -n/-en.

Rule: plural is -n after vowel-final stems, -en after consonant-final stems.
We treat hyphenated plural forms: <token>-s, <token>-se-s, <token>-to-s.
Assumes current convention: CASE then PLURAL, so <token>-se-s -> <token>-se-n.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    ROOT / "docs",
    ROOT / "vote",
]

SKIP_DIRS = {
    ".git",
    "graphify-out",
    "node_modules",
    "packages",
}

CASE_PLURAL_REPLACEMENTS = [
    (re.compile(r"-se-s\b"), "-se-n"),
    (re.compile(r"-to-s\b"), "-to-n"),
]

PLURAL_TOKEN_RE = re.compile(r"\b([A-Za-z]+(?:-[A-Za-z]+)*)-s\b")
VOWELS = set("aeiou")


def pluralize(stem: str) -> str:
    last = stem[-1].lower()
    return f"{stem}-n" if last in VOWELS else f"{stem}-en"


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def process_file(path: Path) -> tuple[bool, int]:
    text = path.read_text(encoding="utf-8")
    orig = text

    matches = 0
    for rx, repl in CASE_PLURAL_REPLACEMENTS:
        text, n = rx.subn(repl, text)
        matches += n

    def _sub(m: re.Match) -> str:
        nonlocal matches
        matches += 1
        return pluralize(m.group(1))

    text = PLURAL_TOKEN_RE.sub(_sub, text)

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True, matches
    return False, matches


def main() -> None:
    changed_files = 0
    total_matches = 0

    for base in TARGETS:
        for path in base.rglob("*.md"):
            if should_skip(path):
                continue
            changed, matches = process_file(path)
            if changed:
                changed_files += 1
            total_matches += matches

    print(f"Changed files: {changed_files}")
    print(f"Total plural -s occurrences rewritten: {total_matches}")


if __name__ == "__main__":
    main()
