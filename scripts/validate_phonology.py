#!/usr/bin/env python3
"""VELA phonotactic validator — lexicons AND corpus.

Enforces the authoritative phonotactic policy from
`docs/phonology/PHONOLOGY_FINAL.md` §3.2, refined by the Fase 5 committee
(`vote/topics/consensus/fase5_consensus.md`):

  Syllables are open (C)V. A word — and each element of a compound — may
  end in a vowel or one of the tolerated codas {n, m, l, r, s}. Clusters
  are allowed word-INITIALLY only, never as a coda.

Two kinds of source are scanned.

LEXICONS (`docs/lexicon/*.md`) — headword rows in markdown tables. Every
headword is a claim about the language, so it is checked directly.

  ERROR   /θ ð ʒ/ — "th"/"zh" in spelling, or θ ð ʒ in the AFI. These
          phonemes are not in VELA's inventory; there is no grandfathering.
  ERROR   In a NEW-word file: any coda outside {n,m,l,r,s}, or any final
          cluster. New atoms must comply.
  WARNING In a LEGACY file: the same deprecated codas / final clusters —
          §3.2 explicitly grandfathers them, so they are migration
          candidates, not failures.

By convention the extended lexicon (Fase 5+) is treated as NEW/strict and
everything else as LEGACY. Override with --strict / --legacy.

CORPUS (`docs/texts/*.md`, `books/*.html`) — running VELA prose. Prose is
bilingual, so only the regions explicitly marked as VELA are read (see
`extract_prose_md` / `extract_html_spans`); English glosses are never
tokenized. Each token is then decomposed:

  1. Grammatical suffixes are stripped, not treated as compound elements.
     `liv-ed`, `bird-en`, `mi-se`, `siti-to` inflect a root; the suffix's
     own coda is canonical and lands in the next syllable's onset
     (R8: `hav-ed` → /ha.ved/). Without this every past tense would be a
     false positive.
  2. Each remaining element is looked up in the lexicon root inventory.
     An element that IS in the lexicon was already checked by the lexicon
     pass — re-reporting it here would just duplicate findings.
  3. An element that is NOT in the lexicon is off-canon, and gets checked:

  ERROR   "th"/"zh" anywhere in a corpus token — no grandfathering, the
          phonemes do not exist. This is what catches `throt`.
  ERROR   Off-canon element with an illegal coda or a banned final cluster.
          It is not in the lexicon, so nothing grandfathers it.
  NOTE    Off-canon element that is phonotactically legal — a gap word:
          used in a text or course but absent from the lexicon.

Usage:
    python3 scripts/validate_phonology.py [--strict|--legacy]
                                          [--lexicons|--corpus] [file ...]

    (no args)     scan lexicons + corpus
    --lexicons    scan only the three lexicons
    --corpus      scan only texts + books
    [file ...]    scan exactly these; kind inferred from the path

Exits 1 only if a hard ERROR is found (so it can gate CI without being
blocked by grandfathered legacy words or by known gap words).
"""

import glob
import re
import sys
import unicodedata

LEXICON_FILES = [
    "docs/lexicon/LEXICON_BASE.md",
    "docs/lexicon/LEXICON_EXTENDED.md",
    "docs/lexicon/LEXICON_EXPANSION.md",
]

CORPUS_GLOBS = [
    "docs/texts/*.md",
    "books/Learning-VELA-Level*.html",
]

VOWELS = set("aeiou")
TOLERATED_CODA = {"n", "m", "l", "r", "s", "ng"}  # ng = [ŋ], allophone of /n/
DIGRAPH_CONSONANTS = {"sh", "ch"}                 # single phonemes, illegal as a coda

# Phase-4 errata roots the committee voted to grandfather (fase5_consensus.md R2):
# they are consonant-final but predate the thematic-vowel rule and already live
# in compounds, so they count as legal roots.
ERRATA_ROOTS = {"art", "net", "sav", "tip", "stap", "grup", "bit", "kod", "wei", "taim"}

# Grammatical suffixes (GRAMMAR_COMPLETE.md; R6 plural, R8 tense).
# In `root-SUFFIX` the suffix is inflection, not a compound element: its coda is
# canonical and resyllabifies into the following onset. Stripped before checking.
SUFFIXES = {
    "ed",    # past           (R8)
    "wil",   # future         (R8)
    "n",     # plural after vowel      (R6)
    "en",    # plural after consonant  (R6)
    "se",    # genitive
    "to",    # locative
    "po",    # profession, gender-neutral
    "a",     # citation vowel (R7) — appears when a bare root is cited
}

# Proper nouns and meta-terms that appear inside VELA text but are not lexicon
# headwords. Days and months ARE in the lexicon and deliberately absent here.
PROPER_NOUNS = {"vela", "lord", "jerman", "inglish", "lumina"}

LEGACY_LEXICON = "docs/lexicon/LEXICON_BASE.md"

ROW = re.compile(r"^\|\s*\*\*(?P<word>[^*]+?)\*\*\s*\|\s*(?P<afi>[^|]*?)\s*\|")


# --------------------------------------------------------------------------
# Phonotactics
# --------------------------------------------------------------------------

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


def phoneme_findings(word, afi=""):
    """Inventory violations. These are ERRORs everywhere, with no grandfathering."""
    findings = []
    if "th" in word.lower():
        findings.append(("ERROR", "phoneme", "contains 'th' — /θ ð/ not in inventory (use t or z)"))
    if "zh" in word.lower():
        findings.append(("ERROR", "phoneme", "contains 'zh' — /ʒ/ not in inventory (use j)"))
    for bad in ("θ", "ð", "ʒ"):
        if bad in afi:
            findings.append(("ERROR", "phoneme", f"AFI contains illegal phoneme '{bad}'"))
    return findings


def split_token(word):
    """Split a token into (content_elements, suffix_follows).

    'liv-ed' -> (['liv'], True) · 'man-en-se' -> (['man'], True)
    'mak-tin' -> (['mak', 'tin'], False)
    A lone suffix ('to', 'n') keeps its own form so it stays visible.
    """
    parts = [p for p in word.lower().split("-") if p]
    n = len(parts)
    while n > 1 and parts[n - 1] in SUFFIXES:
        n -= 1
    return parts[:n], n < len(parts)


def strip_suffixes(word):
    """Content elements of a token, without trailing inflection."""
    return split_token(word)[0]


def resyllabified_defect(element):
    """Defect of an element whose coda is NOT word-final, or None if legal.

    R7/R8: when anything follows a root — an inflectional suffix or the next
    element of a compound — the root's final consonant becomes the onset of the
    following syllable instead of a coda. R8 states it outright: `hav-ed` is
    /ha.ved/ and legal. So only what remains after that consonant leaves has to
    be a tolerated coda.

        hav  + ed  -> tail 'v'  -> 'v' leaves  -> ''  legal   (R8's own example)
        dans + ed  -> tail 'ns' -> 's' leaves  -> 'n' legal
        korekt + ed -> tail 'kt' -> 't' leaves -> 'k' ILLEGAL
    """
    tail = trailing_consonants(element).lower()
    if tail == "" or tail in TOLERATED_CODA:
        return None
    if tail in {"y", "w"}:
        return None
    if tail in DIGRAPH_CONSONANTS:
        return None  # a single phoneme moves wholly into the onset: 'sh', 'ch'
    remainder = tail[:-1]  # the last consonant resyllabifies away
    if remainder == "" or remainder in TOLERATED_CODA:
        return None
    return ("cluster", f"illegal coda '-{remainder}' even after resyllabification "
                       f"(from '-{tail}')")


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check_headword(word, afi, strict, grandfathered):
    """Findings for a lexicon headword."""
    findings = phoneme_findings(word, afi)

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


def check_corpus_token(word, recognized):
    """Findings for one VELA token taken from running prose.

    Elements already covered by the lexicon (directly, or as an R7 bare form) are
    skipped — the lexicon pass owns them. Only off-canon elements are judged here.
    """
    findings = phoneme_findings(word)

    content, suffix_follows = split_token(word)
    for i, element in enumerate(content):
        if element in recognized or element.isdigit():
            continue
        # The coda rule only bites at the true end of the word. Anything that
        # follows — a suffix or the next compound element — resyllabifies it.
        is_word_final = (i == len(content) - 1) and not suffix_follows
        defect = element_defect(element) if is_word_final else resyllabified_defect(element)
        if defect:
            _, detail = defect
            findings.append(("ERROR", "off-canon", f"'{element}' not in lexicon and {detail}"))
        else:
            findings.append(("NOTE", "gap-word", f"'{element}' is legal but not in the lexicon"))

    return findings


# --------------------------------------------------------------------------
# Extraction
# --------------------------------------------------------------------------

def extract_lexicon(path):
    """Yield (word, afi, line_no) for every headword row in a lexicon file."""
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            m = ROW.match(line)
            if m:
                yield m.group("word").strip(), m.group("afi").strip(), line_no


# Pitch accent is written with diacritics in the corpus (`fórti`, `Lòrd`, `mòn`),
# so accented vowels are word characters. They are folded away before analysis —
# the accent marks prosody, not a different phoneme.
LETTER = "A-Za-zÀ-ɏ"
TOKEN = re.compile(f"[{LETTER}][{LETTER}-]*")


def fold(text):
    """Drop pitch-accent diacritics: 'fórti' -> 'forti', 'Lòrd' -> 'Lord'."""
    return "".join(c for c in unicodedata.normalize("NFD", text)
                   if unicodedata.category(c) != "Mn")

# The five shapes VELA prose takes in docs/texts/*.md.
VELA_BLOCK = re.compile(r"^\*\*VELA[:.]?\*\*\s*$", re.I)          # **VELA:** … **English:**
VELA_INLINE = re.compile(r"^\*\*VELA[:.]?\*\*\s+(?=\S)", re.I)     # **VELA:** text on the same line
VELA_HEADING = re.compile(r"^#{2,3}\s+.*\bVELA\b.*$", re.I)        # ## VELA (working translation)
EN_BLOCK = re.compile(r"^\*\*(English|Español|Spanish)[:.]?\*\*", re.I)
EN_HEADING = re.compile(r"^#{2,3}\s+.*\b(English|Español|Spanish|Analysis|Gap|Notes?)\b.*$", re.I)
ANY_HEADING = re.compile(r"^#{1,6}\s")
META_LINE = re.compile(r"^\*\*[A-Z][A-Za-z ]*[:.]\*\*")            # **Date:** **Author:** …
GLOSS_LINE = re.compile(r"^\*\(.*\)\*$")                           # *(The Sun and the Moon)*


def _vela_cell_span(line, header_idx):
    """Return (start, end) of the VELA cell in a markdown table row, or None.

    Offsets are into `line` as given, so a caller can rewrite just that cell.
    """
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    offset = line.index("|") + 1  # first cell begins after the leading pipe
    cells = stripped.strip("|").split("|")
    if header_idx >= len(cells):
        return None
    start = offset + sum(len(c) + 1 for c in cells[:header_idx])
    cell = cells[header_idx]
    if set(cell.strip()) <= set("-: ") or not cell.strip():
        return None  # separator row or empty cell
    return start, start + len(cell)


def vela_spans_md(path):
    """Yield (line_no, line, spans) for a bilingual markdown text.

    `spans` is a list of (start, end, shape) character ranges of `line` that hold
    VELA. Returning ranges rather than text is what lets the corpus migrator
    rewrite VELA in place without ever touching the English translation beside it.

    Only explicitly-marked VELA regions are produced:
      · a `**VELA:**` block, up to `**English:**` / `---` / next heading
        (the text may start on the marker's own line)
      · a `## …VELA…` heading section, up to the next heading
      · a fenced code block inside such a section
      · the `VELA` column of a markdown table

    `shape` is 'marked' for content whose boundary is unambiguous (a table cell,
    a blockquote, a fenced line) and 'plain' for a bare paragraph inside a VELA
    region. Bare paragraphs are the only place English can leak in — a section
    like BENCHMARK's `### VELA Translation` holds the VELA in a blockquote and
    then continues in English prose — so only they are language-gated.
    """
    in_vela = False          # inside a **VELA:** block or a VELA heading section
    in_fence = False
    table_col = None         # index of the VELA column of the current table

    with open(path, encoding="utf-8") as f:
        for line_no, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            stripped = line.strip()

            if stripped.startswith("```"):
                in_fence = not in_fence
                continue

            if not in_fence:
                if VELA_BLOCK.match(stripped) or VELA_HEADING.match(stripped):
                    in_vela, table_col = True, None
                    continue
                # The text follows the marker on the same line. Checked before
                # META_LINE, which would otherwise swallow it as a **Label:** line.
                inline = VELA_INLINE.match(line.lstrip())
                if inline:
                    in_vela, table_col = True, None
                    start = len(line) - len(line.lstrip()) + inline.end()
                    yield line_no, line, [(start, len(line), "marked")]
                    continue
                if EN_BLOCK.match(stripped) or EN_HEADING.match(stripped):
                    in_vela, table_col = False, None
                    continue
                if ANY_HEADING.match(stripped):
                    in_vela, table_col = False, None
                    continue
                if stripped == "---":
                    in_vela, table_col = False, None
                    continue
                if META_LINE.match(stripped) or GLOSS_LINE.match(stripped):
                    continue  # metadata line, or a whole-line italic translation gloss

                # Table handling works anywhere: the header names the language.
                if stripped.startswith("|"):
                    cells = [c.strip().strip("*").lower()
                             for c in stripped.strip("|").split("|")]
                    if "vela" in cells:
                        table_col = cells.index("vela")
                        continue
                    if table_col is not None:
                        span = _vela_cell_span(line, table_col)
                        if span:
                            yield line_no, line, [(span[0], span[1], "marked")]
                        continue
                    continue
                table_col = None

            if not in_vela or not stripped:
                continue

            shape = "marked" if (in_fence or stripped.startswith(">")) else "plain"
            yield line_no, line, [(0, len(line), shape)]


def extract_prose_md(path):
    """Yield (segment_text, line_no, shape) for VELA regions of a bilingual text."""
    for line_no, line, spans in vela_spans_md(path):
        for start, end, shape in spans:
            yield line[start:end], line_no, shape


SPAN = re.compile(r'<span class="[^"]*\bvela\b[^"]*">(.*?)</span>', re.S)


def extract_html_spans(path):
    """Yield (segment_text, line_no, 'marked') for every <span class="vela">.

    The courses mark every VELA fragment this way — 770 spans across the five
    books — so the span is an exact boundary and never needs language-gating.
    """
    with open(path, encoding="utf-8") as f:
        text = f.read()

    for m in SPAN.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        inner = re.sub(r"<[^>]+>", " ", m.group(1))
        inner = inner.replace("&nbsp;", " ").replace("&amp;", "&")
        yield inner, line_no, "marked"


# A bare paragraph inside a VELA region is accepted only if this share of its
# tokens are recognized VELA. English prose scores far below it; real VELA scores
# far above. Applied only to 'plain' shapes, and only when there is enough text
# for the ratio to mean anything.
GATE_RATIO = 0.5
GATE_MIN_TOKENS = 4


def corpus_vocabulary(lexicon_roots):
    """What a corpus token may legally be: a lexicon root, the R7 bare form of a
    citation root, an inflectional suffix, or a whitelisted proper noun."""
    return lexicon_roots | r7_bare_forms(lexicon_roots) | SUFFIXES | PROPER_NOUNS


def is_vela_segment(segment, shape, recognized):
    """False for a bare paragraph that reads as English (see language_gate).

    Marked shapes have an unambiguous boundary and are always VELA. The validator
    and the corpus migrator both call this, so they agree on what they skip.
    """
    if shape != "plain":
        return True
    tokens = [fold(t) for t in TOKEN.findall(segment)]
    return language_gate(tokens, recognized)


def language_gate(tokens, recognized):
    """True if this bare paragraph reads as VELA rather than English."""
    if len(tokens) < GATE_MIN_TOKENS:
        return True
    known = 0
    for tok in tokens:
        parts = strip_suffixes(tok)
        if all(p in recognized for p in parts):
            known += 1
    return known / len(tokens) >= GATE_RATIO


def source_kind(path):
    """'lexicon' | 'html' | 'prose' — inferred from the path."""
    if "lexicon" in path.lower():
        return "lexicon"
    if path.lower().endswith((".html", ".htm")):
        return "html"
    return "prose"


EXTRACTORS = {
    "lexicon": extract_lexicon,
    "prose": extract_prose_md,
    "html": extract_html_spans,
}


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
            for word, _, _ in extract_lexicon(path):
                for element in word.split("-"):
                    if element and not element.isupper():
                        roots.add(element.lower())
        except OSError:
            pass  # missing file: skip
    return roots


def r7_bare_forms(roots):
    """Bare combining forms implied by R7 citation headwords.

    R7 gives every hard-coda content root two shapes: citation `luva` (dictionary
    headword) and bare `luv` (inside compounds). Only the citation form is a
    headword, so the bare form must be derived or the corpus scan reports every
    compounding root as off-canon. A headword is an R7 citation form when it ends
    in `-a` and dropping that `-a` exposes a coda that would otherwise be illegal —
    which is precisely the condition that made the epenthetic vowel necessary.
    """
    bare = set()
    for root in roots:
        if len(root) > 2 and root.endswith("a"):
            stem = root[:-1]
            if element_defect(stem):
                bare.add(stem)
    return bare


def corpus_files():
    files = []
    for pattern in CORPUS_GLOBS:
        files.extend(sorted(glob.glob(pattern)))
    return files


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main(argv):
    args = argv[1:]
    force = None
    if "--strict" in args:
        force, args = True, [a for a in args if a != "--strict"]
    if "--legacy" in args:
        force, args = False, [a for a in args if a != "--legacy"]

    only_lexicons = "--lexicons" in args
    only_corpus = "--corpus" in args
    args = [a for a in args if a not in ("--lexicons", "--corpus")]

    if args:
        files = args
    elif only_lexicons:
        files = list(LEXICON_FILES)
    elif only_corpus:
        files = corpus_files()
    else:
        files = list(LEXICON_FILES) + corpus_files()

    lexicon_roots = load_grandfathered(LEXICON_FILES)
    recognized = corpus_vocabulary(lexicon_roots)

    findings = []  # (severity, rule, path, line_no, word, detail)
    lex_total = corpus_total = skipped_total = 0

    for path in files:
        kind = source_kind(path)
        extract = EXTRACTORS[kind]

        if kind == "lexicon":
            strict = force if force is not None else ("EXTENDED" in path or "EXPANSION" in path)
            tag = "NEW/strict" if strict else "legacy"
            count = 0
            for word, afi, line_no in extract(path):
                count += 1
                for severity, rule, detail in check_headword(word, afi, strict, lexicon_roots):
                    findings.append((severity, rule, path, line_no, word, detail))
            lex_total += count
            print(f"  scanned {path}  ({count} headwords, {tag})")
        else:
            seen = set()  # report each distinct token once per file
            count = 0
            skipped = 0
            for segment, line_no, shape in extract(path):
                tokens = [fold(t) for t in TOKEN.findall(segment)]
                if not tokens:
                    continue
                if not is_vela_segment(segment, shape, recognized):
                    skipped += 1
                    continue
                for word in tokens:
                    count += 1
                    key = word.lower()
                    if key in seen:
                        continue
                    seen.add(key)
                    for severity, rule, detail in check_corpus_token(word, recognized):
                        findings.append((severity, rule, path, line_no, word, detail))
            corpus_total += count
            note = f", {skipped} paragraph(s) skipped as non-VELA" if skipped else ""
            print(f"  scanned {path}  ({count} VELA tokens, {len(seen)} distinct, corpus{note})")
            if skipped:
                skipped_total += skipped

    errors = [f for f in findings if f[0] == "ERROR"]
    warnings = [f for f in findings if f[0] == "WARNING"]
    notes = [f for f in findings if f[0] == "NOTE"]

    coverage = f"\nVELA phonotactic validation — {lex_total} headwords + {corpus_total} corpus tokens"
    if skipped_total:
        coverage += (f"\n(coverage limit: {skipped_total} bare paragraph(s) inside VELA regions "
                     f"read as English and were skipped — violations there are not reported)")
    print(coverage + "\n")

    def show(group, header):
        if not group:
            return
        print(header)
        by_rule = {}
        for _, rule, path, line_no, word, detail in group:
            by_rule.setdefault(rule, []).append((path, line_no, word, detail))
        for rule in sorted(by_rule):
            items = by_rule[rule]
            print(f"  {rule} ({len(items)}):")
            for path, line_no, word, detail in items:
                print(f"    {path}:{line_no}  {word:<22} {detail}")
        print()

    show(errors, f"❌ ERRORS — {len(errors)}:")
    show(notes, f"📝 NOTES — {len(notes)} (gap words / legacy roots mid-compound — canon does not settle these):")
    show(warnings, f"⚠️  WARNINGS — {len(warnings)} (grandfathered legacy, migration candidates):")

    if errors:
        print(f"FAIL — {len(errors)} error(s).")
        return 1
    print("PASS — 0 errors" + (f", {len(warnings)} legacy warning(s)." if warnings else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
