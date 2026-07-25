#!/usr/bin/env python3
"""One-off lexicon cleanup (idempotent), verified by generate_dictionary.py:

  1. Strip syllable dots from headwords — a dot belongs in the AFI column only
     (`lai.on` -> `laion`; the AFI `/lai.on/` keeps its dots). Also de-dots the
     word inside its own example sentence.
  2. Remove duplicate headword rows (same word listed in more than one section),
     keeping the first occurrence. The genuine homonyms in KEEP_BOTH are left
     untouched for manual resolution.

Run:  python3 scripts/clean_lexicon.py   then regenerate the dictionary.
"""

import re

FILES = ["docs/lexicon/LEXICON_BASE.md", "docs/lexicon/LEXICON_EXTENDED.md"]
KEEP_BOTH = {"dai", "lai"}  # true homonyms — resolved by hand, not deduped
DATA_ROW = re.compile(r"^\|\s*\*\*(?P<word>[^*]+?)\*\*\s*\|")
AFI_COL = 2  # split("|") index of the AFI cell (col 0 is empty, col 1 is the word)


def clean_file(path):
    out, seen = [], set()
    dropped = dedotted = 0
    for line in open(path, encoding="utf-8"):
        m = DATA_ROW.match(line)
        if not m:
            out.append(line)
            continue
        word = m.group("word").strip()
        norm = word.replace(".", "").lower()
        if norm in seen and norm not in KEEP_BOTH:
            dropped += 1
            continue
        seen.add(norm)
        if "." in word:
            cells = line.rstrip("\n").split("|")
            cells = [c if i == AFI_COL else c.replace(".", "") for i, c in enumerate(cells)]
            out.append("|".join(cells) + "\n")
            dedotted += 1
        else:
            out.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    print(f"  {path}: removed {dropped} duplicate(s), de-dotted {dedotted} headword(s)")


if __name__ == "__main__":
    for p in FILES:
        clean_file(p)
