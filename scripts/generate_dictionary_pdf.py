#!/usr/bin/env python3
"""Render a compact, printable VELA dictionary PDF from the generated tables.

Reads the two canonical, already-generated files:

  docs/dictionary/DICTIONARY.md      VELA -> English (7-col table)
  docs/dictionary/INDEX_EN_VELA.md   English -> VELA (3-col table)

and emits a print-optimised, two-column Typst document plus its PDF:

  books/VELA-Dictionary.typ
  books/VELA-Dictionary.pdf

The 7-column reference tables are unreadable on paper, so each row is
collapsed into a real dictionary entry line. This does NOT touch the
lexicon or invent anything — regenerate the lexicons, rerun
generate_dictionary.py, then rerun this.

Usage:  python3 scripts/generate_dictionary_pdf.py
Requires: typst on PATH.
"""

import subprocess
import sys

DICT = "docs/dictionary/DICTIONARY.md"
INDEX = "docs/dictionary/INDEX_EN_VELA.md"
OUT_TYP = "books/VELA-Dictionary.typ"
OUT_PDF = "books/VELA-Dictionary.pdf"


def rows(path):
    """Yield lists of stripped cells for real table rows (skip headers/separators)."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not cells or not cells[0]:
                continue
            joined = "".join(cells)
            if set(joined) <= set("-: "):        # separator row
                continue
            if cells[0] in ("VELA", "English"):   # header row
                continue
            yield cells


def ts(s):
    r"""Escape a Python string for a Typst double-quoted string literal."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def group_by_letter(items, key):
    """Return ordered [(letter, [items])] grouped by uppercased first letter of key."""
    groups = {}
    for it in items:
        k = key(it)
        letter = k[0].upper() if k and k[0].isalpha() else "#"
        groups.setdefault(letter, []).append(it)
    return sorted(groups.items(), key=lambda kv: (kv[0] == "#", kv[0]))


def parse_dict():
    """VELA -> (vela, ipa, cat, definition)."""
    out = []
    for c in rows(DICT):
        vela = c[0]
        ipa = c[1] if len(c) > 1 else ""
        cat = c[2] if len(c) > 2 else ""
        definition = c[3] if len(c) > 3 else ""
        if not vela or not definition:
            continue
        out.append((vela, ipa, cat, definition))
    out.sort(key=lambda e: e[0].lower())
    return out


def parse_index():
    """English -> (english, vela, ipa)."""
    out = []
    for c in rows(INDEX):
        eng = c[0]
        vela = c[1] if len(c) > 1 else ""
        ipa = c[2] if len(c) > 2 else ""
        if not eng or not vela:
            continue
        out.append((eng, vela, ipa))
    out.sort(key=lambda e: e[0].lower())
    return out


PREAMBLE = r'''#set document(title: "VELA Dictionary", author: "VELA Language Project")
#set page(paper: "a4", margin: (x: 1.5cm, top: 1.8cm, bottom: 1.6cm),
  numbering: "1", number-align: center)
#set text(size: 9.5pt, hyphenate: false)
#set par(justify: false, leading: 0.42em, spacing: 0.5em)

#let brand = rgb("#0f6e7e")
#let sun = rgb("#b3760f")
#let muted = rgb("#5b7683")

// one dictionary entry: bold headword, small IPA, gloss
#let e(head, ipa, gloss) = block(breakable: false, spacing: 0.5em)[
  #text(weight: "bold", fill: brand)[#head]#if ipa != "" [ #text(size: 8pt, fill: muted, font: "DejaVu Sans Mono")[#ipa]] #h(0.15em) #gloss
]

#let letter(l) = block(above: 0.9em, below: 0.55em, breakable: false)[
  #text(size: 14pt, weight: 800, fill: sun)[#l]
  #v(-0.35em)
  #line(length: 100%, stroke: 0.6pt + sun)
]

// ---- title page ----
#align(center + horizon)[
  #text(size: 46pt, weight: 800, fill: brand)[VELA]
  #v(0.1em)
  #text(size: 20pt, weight: 600)[Dictionary]
  #v(0.4em)
  #text(size: 12pt, fill: muted)[The universal conlang based on English]
  #v(2em)
  #text(size: 11pt)[VELA #sym.arrow English  ·  English #sym.arrow VELA]
  #v(0.3em)
  #text(size: 10pt, fill: muted)[__ENTRYCOUNT__ entries · Level: reference]
]
#pagebreak()
'''


def section(title, subtitle, groups, render_entry):
    parts = [f'#text(size: 22pt, weight: 800, fill: brand)[{title}]\n',
             f'#v(0.1em)\n#text(size: 10pt, fill: muted)[{subtitle}]\n#v(0.7em)\n',
             "#columns(2, gutter: 1.1em)[\n"]
    for letter_, items in groups:
        parts.append(f'#letter("{ts(letter_)}")\n')
        for it in items:
            parts.append(render_entry(it))
    parts.append("]\n")
    return "".join(parts)


def main():
    dict_entries = parse_dict()
    index_entries = parse_index()

    def d_entry(e):
        vela, ipa, cat, definition = e
        base = f'#e("{ts(vela)}", "{ts(ipa)}", [{ts(definition)}'
        if cat:
            base += f' #text(fill: muted, size: 8pt, style: "italic")[{ts(cat)}]'
        base += "])\n"
        return base

    def i_entry(e):
        eng, vela, ipa = e
        val = f'#sym.arrow.r #text(weight: "bold", fill: brand)[{ts(vela)}]'
        if ipa:
            val += f' #text(size: 8pt, fill: muted, font: "DejaVu Sans Mono")[{ts(ipa)}]'
        return f'#e("{ts(eng)}", "", [{val}])\n'

    body = PREAMBLE.replace("__ENTRYCOUNT__", f"{len(dict_entries):,}")
    body += section("VELA → English",
                    "Headword, pronunciation, meaning.",
                    group_by_letter(dict_entries, key=lambda e: e[0]),
                    d_entry)
    body += "\n#pagebreak()\n"
    body += section("English → VELA",
                    "Look up an English word, find its VELA form.",
                    group_by_letter(index_entries, key=lambda e: e[0]),
                    i_entry)

    with open(OUT_TYP, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"wrote {OUT_TYP}  ({len(dict_entries)} + {len(index_entries)} entries)")

    try:
        subprocess.run(["typst", "compile", OUT_TYP, OUT_PDF], check=True)
    except FileNotFoundError:
        print("typst not found on PATH — .typ written, compile it manually.", file=sys.stderr)
        return 1
    print(f"wrote {OUT_PDF}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
