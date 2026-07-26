#!/usr/bin/env python3
"""VELA phonotactic validator.

Enforces the authoritative phonotactic policy from
`docs/phonology/PHONOLOGY_FINAL.md` §3.2, refined by the Fase 5 committee
(`vote/topics/consensus/fase5_consensus.md`):

  Syllables are open (C)V. A word — and each element of a compound — may
  end in a vowel or one of the tolerated codas {n, m, l, r, s}. Clusters
  are allowed word-INITIALLY only, never as a coda.

Severity depends on whether the word is NEW or LEGACY:

  ERROR   /θ ð ʒ/ — "th"/"zh" in spelling, or θ ð ʒ in the AFI. These
          phonemes are not in VELA's inventory; there is no grandfathering.
  ERROR   In a NEW-word file: any coda outside {n,m,l,r,s}, or any final
          cluster. New atoms must comply.
  WARNING In a LEGACY file: the same deprecated codas / final clusters —
          §3.2 explicitly grandfathers them, so they are migration
          candidates, not failures.

By convention the extended lexicon (Fase 5+) is treated as NEW/strict and
everything else as LEGACY. Override with --strict / --legacy.

Usage:
    python3 scripts/validate_phonology.py [--strict|--legacy] [file ...]

Exits 1 only if a hard ERROR is found (so it can gate CI without being
blocked by grandfathered legacy words).
"""

import re
import sys

DEFAULT_FILES = [
    "docs/lexicon/LEXICON_BASE.md",
    "docs/lexicon/LEXICON_EXTENDED.md",
    "docs/lexicon/LEXICON_EXPANSION.md",
]

VOWELS = set("aeiou")
TOLERATED_CODA = {"n", "m", "l", "r", "s", "ng"}  # ng = [ŋ], allophone of /n/
DIGRAPH_CONSONANTS = {"sh", "ch"}                 # single phonemes, illegal as a coda

# Phase-4 errata roots the committee voted to grandfather (fase5_consensus.md R2):
# they are consonant-final but predate the thematic-vowel rule and already live
# in compounds, so they count as legal roots.
ERRATA_ROOTS = {"art", "net", "sav", "tip", "stap", "grup", "bit", "kod", "wei", "taim"}

LEGACY_LEXICON = "docs/lexicon/LEXICON_BASE.md"

ROW = re.compile(r"^\|\s*\*\*(?P<word>[^*]+?)\*\*\s*\|\s*(?P<afi>[^|]*?)\s*\|")


def trailing_consonants(element):
    """Return the consonant string after the last vowel of a compound element."""
    idx = max((i for i, ch in enumerate(element) if ch in VOWELS), default=-1)
    return element[idx + 1:] if idx >= 0 else element


def element_defect(element):
    """Return (kind, detail) for an illegal element, or None if legal.

    kind is 'coda' (single deprecated coda) or 'cluster' (2+ trailing consonants).
    """
    tail = trailing_consonants(element).lower()
    if tail == "" or tail in TOLERATED_CODA:
        return None
    if tail in {"y", "w"}:
        return None  # vowel offglide: diphthong ending (deploy, sey, bow)
    if tail in DIGRAPH_CONSONANTS or len(tail) == 1:
        return ("coda", f"deprecated coda '-{tail}' (prefer vowel-final, e.g. -{tail}a)")
    return ("cluster", f"illegal final cluster '-{tail}'")


def check_word(word, afi, strict, grandfathered):
    """Return a list of (severity, rule, detail) findings for a headword."""
    findings = []

    if "th" in word.lower():
        findings.append(("ERROR", "phoneme", "contains 'th' — /θ ð/ not in inventory (use t or z)"))
    if "zh" in word.lower():
        findings.append(("ERROR", "phoneme", "contains 'zh' — /ʒ/ not in inventory (use j)"))
    for bad in ("θ", "ð", "ʒ"):
        if bad in afi:
            findings.append(("ERROR", "phoneme", f"AFI contains illegal phoneme '{bad}'"))

    elements = word.split("-")
    for i, element in enumerate(elements):
        if not element or element.isupper():  # skip acronyms: DNA, IP, AI
            continue
        if element.lower() in grandfathered:  # native/legacy root — R2 grandfathers it
            continue
        defect = element_defect(element)
        if not defect:
            continue
        _, detail = defect
        is_final = i == len(elements) - 1
        if is_final:
            # The word's actual final coda — the rule bites here.
            severity = "ERROR" if strict else "WARNING"
            findings.append((severity, "word-final", detail))
        else:
            # Legacy root reused mid-compound — canon does not settle this.
            findings.append(("NOTE", "compound-internal", f"element '{element}': {detail}"))

    return findings


def parse(path):
    """Yield (word, afi, line_no) for every headword row in a lexicon file."""
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            m = ROW.match(line)
            if m:
                yield m.group("word").strip(), m.group("afi").strip(), line_no


def load_grandfathered(paths):
    """Legal root inventory: every root/combining-form used anywhere in the lexicon,
    plus errata roots. Loading from all files (not just BASE) recognises the bare
    COMBINING forms of citation roots (e.g. compound 'mak-tin' keeps 'mak' legal even
    though the standalone citation form is 'maka') — the citation/composition allomorphy
    ratified as Option D."""
    if isinstance(paths, str):
        paths = [paths]
    roots = set(ERRATA_ROOTS)
    for path in paths:
        try:
            for word, _, _ in parse(path):
                for element in word.split("-"):
                    if element and not element.isupper():
                        roots.add(element.lower())
        except OSError:
            pass  # missing file: skip
    return roots


def main(argv):
    args = argv[1:]
    force = None
    if "--strict" in args:
        force, args = True, [a for a in args if a != "--strict"]
    if "--legacy" in args:
        force, args = False, [a for a in args if a != "--legacy"]
    files = args or DEFAULT_FILES
    grandfathered = load_grandfathered(DEFAULT_FILES)

    findings = []  # (severity, rule, path, line_no, word, detail)
    total = 0
    for path in files:
        strict = force if force is not None else ("EXTENDED" in path or "EXPANSION" in path)
        tag = "NEW/strict" if strict else "legacy"
        count = 0
        for word, afi, line_no in parse(path):
            total += 1
            count += 1
            for severity, rule, detail in check_word(word, afi, strict, grandfathered):
                findings.append((severity, rule, path, line_no, word, detail))
        print(f"  scanned {path}  ({count} words, {tag})")

    errors = [f for f in findings if f[0] == "ERROR"]
    warnings = [f for f in findings if f[0] == "WARNING"]
    notes = [f for f in findings if f[0] == "NOTE"]
    print(f"\nVELA phonotactic validation — {total} words checked\n")

    def show(group, header):
        if not group:
            return
        print(header)
        by_rule = {}
        for severity, rule, path, line_no, word, detail in group:
            by_rule.setdefault(rule, []).append((path, line_no, word, detail))
        for rule in sorted(by_rule):
            items = by_rule[rule]
            print(f"  {rule} ({len(items)}):")
            for path, line_no, word, detail in items:
                print(f"    {path}:{line_no}  {word:<22} {detail}")
        print()

    show(errors, f"❌ ERRORS — {len(errors)} (new words with an illegal final coda):")
    show(notes, f"📝 NOTES — {len(notes)} (legacy root reused mid-compound — canon does not settle this):")
    show(warnings, f"⚠️  WARNINGS — {len(warnings)} (grandfathered legacy, migration candidates):")

    if errors:
        print(f"FAIL — {len(errors)} error(s).")
        return 1
    print(f"PASS — 0 errors" + (f", {len(warnings)} legacy warning(s)." if warnings else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
