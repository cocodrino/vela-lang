#!/usr/bin/env python3
"""Generate the official VELA dictionary from the existing lexicons.

This does NOT invent vocabulary. It parses `LEXICON_BASE.md` and
`LEXICON_EXTENDED.md`, merges and sorts every entry, derives the etymology
and the list of compounds that use each root, and renders:

  docs/dictionary/DICTIONARY.md      VELA -> IPA -> gloss (grouped by letter)
  docs/dictionary/INDEX_EN_VELA.md   reverse index: English -> VELA

The lexicon tables use ~13 different column layouts, so parsing is
header-aware: each table's header row maps column position to a field name.
Only Word (col 1) and AFI (col 2) are guaranteed; everything else is optional.

Usage:  python3 scripts/generate_dictionary.py
Prints a generation report (counts, duplicates, entries missing AFI/gloss).
"""

import re
import sys

SOURCES = ["docs/lexicon/LEXICON_BASE.md", "docs/lexicon/LEXICON_EXTENDED.md"]
OUT_DIR = "docs/dictionary"

FORMATION_KEYS = ("formation", "compound", "compound notes", "structure")
EXAMPLE_KEYS = ("vela example", "example")
SEP_RE = re.compile(r"^[\s:|-]+$")
BAD_WORD_RE = re.compile(r'[*"]')  # markdown/quote artifacts — a note row, not a real headword


def split_row(line):
    """Split a markdown table row into stripped cells."""
    return [c.strip() for c in line.strip().strip("|").split("|")]


def field(header, cells, *names):
    """Return the first cell whose column header matches one of names."""
    for name in names:
        if name in header:
            i = header.index(name)
            if i < len(cells):
                return cells[i]
    return ""


DEFAULT_HEADERS = {
    4: ["word", "afi", "english", "example"],
    5: ["word", "afi", "english", "formation", "example"],
    6: ["word", "afi", "type", "english", "vela example", "english"],
    7: ["word", "afi", "english", "present", "past", "future", "example"],
}


def entry_from(header, cells):
    """Build a normalized entry dict from one data row, or None if unusable."""
    word = field(header, cells, "word").strip("*").strip()
    if not word or word.lower() == "word" or BAD_WORD_RE.search(word):
        return None
    category = field(header, cells, "type")
    if not category and "present" in header:
        category = "verb"
    example = field(header, cells, *EXAMPLE_KEYS)
    if not example and len(cells) >= 4:  # header-less table: last cell is the example
        example = cells[-1]
    formation = field(header, cells, *FORMATION_KEYS)
    if formation == example:  # mismatched inherited header mapped the example as formation
        formation = ""
    return {
        "word": word,
        "afi": field(header, cells, "afi"),
        "gloss": field(header, cells, "english"),
        "formation": formation,
        "example": example,
        "category": category,
    }


def parse_lexicon(path):
    """Yield normalized entries from one lexicon file (header-aware).

    A header persists until the next section heading (#) or the next `| Word |`
    row — NOT until the next blank line, since header-less continuation tables
    and mid-table prose are common. Rows under no header fall back to a
    positional default keyed on column count.
    """
    header = None
    entries = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("#"):        # section boundary — scope the header
                header = None
                continue
            if not s.startswith("|"):    # prose/blank — keep the current header
                continue
            cells = split_row(s)
            if all(SEP_RE.match(c) for c in cells):  # |---|---| separator
                continue
            if cells and cells[0].lower() == "word":  # a header row always wins
                header = [c.lower() for c in cells]
                continue
            if not cells or not cells[0].startswith("**"):  # only bold headwords are entries
                continue
            active = header or DEFAULT_HEADERS.get(len(cells), ["word", "afi", "english"])
            halves = [(active, cells)]
            if active.count("word") == 2:  # rare "two entries per row" layout
                mid = active.index("word", 1)
                halves = [(active[:mid], cells[:mid]), (active[mid:], cells[mid:])]
            for h, c in halves:
                e = entry_from(h, c)
                if e:
                    e["source"] = path
                    entries.append(e)
    return entries


def build_compound_index(entries):
    """Map each root -> sorted list of compound words that contain it."""
    index = {}
    for e in entries:
        parts = e["word"].split("-")
        if len(parts) < 2:
            continue
        for part in parts:
            key = part.lower()
            index.setdefault(key, set()).add(e["word"])
    return {k: sorted(v) for k, v in index.items()}


def etymology(e, gloss_of):
    """Use the formation note if present; else derive from compound parts."""
    if e["formation"]:
        return e["formation"]
    parts = e["word"].split("-")
    if len(parts) < 2:
        return ""
    return " + ".join(f"{p} ({gloss_of[p.lower()]})" if p.lower() in gloss_of else p
                      for p in parts)


def md_escape(text):
    return text.replace("|", "\\|")


def render_dictionary(entries, compounds, gloss_of):
    lines = [
        "# VELA Dictionary — Official",
        "",
        "> Generated from `LEXICON_BASE.md` + `LEXICON_EXTENDED.md` by "
        "`scripts/generate_dictionary.py`. Do not edit by hand — edit the lexicons and regenerate.",
        f"> Entries: {len(entries)}. Format: VELA | IPA | Category | Definition | Etymology | Compounds | Example.",
        "",
    ]
    letter = None
    seen = set()  # collapse fully-identical duplicate rows (distinct glosses stay visible)
    for e in sorted(entries, key=lambda x: x["word"].lower()):
        key = (e["word"].lower(), e["afi"], e["gloss"], e["example"])
        if key in seen:
            continue
        seen.add(key)
        first = e["word"][0].upper()
        if first != letter:
            letter = first
            lines += ["", f"## {letter}", "",
                      "| VELA | IPA | Cat. | Definition | Etymology | Compounds | Example |",
                      "|------|-----|------|-----------|-----------|-----------|---------|"]
        comps = ", ".join(compounds.get(e["word"].lower(), []))
        row = [e["word"], e["afi"], e["category"], e["gloss"],
               etymology(e, gloss_of), comps, e["example"]]
        lines.append("| " + " | ".join(md_escape(c) for c in row) + " |")
    return "\n".join(lines) + "\n"


def render_reverse(entries):
    lines = ["# VELA Dictionary — English → VELA Index", "",
             "> Reverse lookup, generated. Edit the lexicons and regenerate.", "",
             "| English | VELA | IPA |", "|---------|------|-----|"]
    seen = set()
    for e in sorted(entries, key=lambda x: (x["gloss"].lower(), x["word"].lower())):
        if not e["gloss"]:
            continue
        key = (e["gloss"].lower(), e["word"].lower())
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"| {md_escape(e['gloss'])} | {e['word']} | {md_escape(e['afi'])} |")
    return "\n".join(lines) + "\n"


def main():
    all_entries = []
    for path in SOURCES:
        found = parse_lexicon(path)
        all_entries += found
        print(f"  parsed {path}: {len(found)} entries")

    gloss_of = {e["word"].lower(): e["gloss"] for e in all_entries if e["gloss"]}
    compounds = build_compound_index(all_entries)

    import os
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(f"{OUT_DIR}/DICTIONARY.md", "w", encoding="utf-8") as f:
        f.write(render_dictionary(all_entries, compounds, gloss_of))
    with open(f"{OUT_DIR}/INDEX_EN_VELA.md", "w", encoding="utf-8") as f:
        f.write(render_reverse(all_entries))

    # Quality report
    seen, dups = {}, []
    for e in all_entries:
        w = e["word"].lower()
        if w in seen:
            dups.append(e["word"])
        seen[w] = e
    no_afi = [e["word"] for e in all_entries if not e["afi"]]
    no_gloss = [e["word"] for e in all_entries if not e["gloss"]]

    print(f"\nDictionary written to {OUT_DIR}/ — {len(all_entries)} entries "
          f"({len(seen)} unique headwords).")
    if dups:
        print(f"⚠️  {len(dups)} duplicate headword(s): {', '.join(sorted(set(dups))[:20])}"
              + (" ..." if len(set(dups)) > 20 else ""))
    if no_afi:
        print(f"⚠️  {len(no_afi)} entr(y/ies) missing AFI: {', '.join(no_afi[:20])}"
              + (" ..." if len(no_afi) > 20 else ""))
    if no_gloss:
        print(f"⚠️  {len(no_gloss)} entr(y/ies) missing gloss: {', '.join(no_gloss[:20])}"
              + (" ..." if len(no_gloss) > 20 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
