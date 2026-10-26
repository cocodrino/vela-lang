#!/usr/bin/env python3
"""Rewrite off-canon VELA words in the corpus to their canonical lexicon forms.

`validate_phonology.py --corpus` reports VELA words in `docs/texts/` and
`books/` that break phonotactics. Almost all of them are not missing vocabulary:
they are pre-reform spellings, or English words that were never translated. The
Fase 8 corpus was written in May 2026, before the July reforms (R2 thematic
vowel, R7 citation/composition, R15 beautification), so it drifted out of canon
while the lexicon moved on.

This script applies the corrections whose target already exists in the lexicon.
It does NOT invent words: every replacement is checked against the lexicon at
startup, and coining a new word is a committee decision (`vote/docs/PROCESS.md`),
not something a migration script may do. Words with no canonical form are listed
in NEEDS_COMMITTEE and deliberately left untouched.

Only VELA regions are rewritten. The bilingual texts put the English translation
right next to the VELA, and many drifted words ARE English words (`world`,
`third`, `light`), so a blind search-and-replace would corrupt the translations.
Region boundaries come from `validate_phonology.vela_spans_md`, the same walker
the validator uses, so the two can never disagree about what counts as VELA.

Usage:
    python3 scripts/migrate_corpus.py --dry-run     # show every change
    python3 scripts/migrate_corpus.py               # apply
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from validate_phonology import (  # noqa: E402
    LETTER,
    SUFFIXES,
    corpus_files,
    corpus_vocabulary,
    element_defect,
    extract_lexicon,
    fold,
    is_vela_segment,
    load_grandfathered,
    LEXICON_FILES,
    SPAN,
    _vela_cell_span,
    r7_bare_forms,
    vela_spans_md,
)

# Off-canon form  ->  canonical lexicon form.
# Every value was looked up in docs/dictionary/INDEX_EN_VELA.md and is asserted
# to exist in the lexicon before anything is written.
REPLACEMENTS = {
    # --- /θ/ violations: 'th' is not a VELA phoneme, no grandfathering ---
    "throt": "trota",        # throat
    "erth": "erda",          # earth
    "path": "wei",           # way / path (abstract)
    "third": "terda",        # third (1/3)

    # --- English left untranslated ---
    "world": "wailda",
    "light": "laita",
    "bright": "brite",
    "glass": "glasi",
    "leaf": "folia",
    "deep": "dipa",
    "full": "ful",
    "step": "stap",
    "week": "seven-dei",
    "high": "hai",
    "down": "daun",
    "break": "braka",
    "trust": "trasta",
    "owl": "aul",
    "try": "trai",
    "laugh": "lafa",
    "second": "sekonda",
    "closed": "klos",
    "it": "li",

    # --- pre-reform spellings (R2 / R7 / R15 drift) ---
    "werld": "wailda",
    "nait": "noita",
    "hart": "herta",
    "voys": "vois",
    "brid": "birda",
    "kwaiet": "kwaiata",
    "trut": "tru-nes",       # truth (abstract)
    "nid": "needa",
    "bag": "bagi",
    "tern": "turna",
    "tiket": "bileta",
    "brek": "braka",
    "opn": "open",
    "kold": "kol",
    "ondastand": "understanda",
    "korekt": "righta",      # right (correct)
    "lunch": "dei-eat",      # lunch / midday meal
    "solt": "salta",
    "frut": "frukta",
    "laik": "liki",
    "musik": "muzika",
    "intanet": "interneta",
    "took": "teka",
    "tuk": "teka",
    "wach": "wotcha",
    "roof": "rofa",
    "fraid": "afreda",
    "raiz": "raisa",
    "esy": "eas",
    "laud": "louda",
    "seif": "safi",
    "sef": "safi",
    "yest": "yestdei",
    "neks": "folo-wan",
    "wulf": "wail-dog",
    "starz": "star-en",      # plural of star: consonant-final root takes -en (R6)

    # --- found once STORIES_SET_01.md was scanned (inline **VELA:** marker) ---
    "with": "wit",
    "act": "akta",
    "nex": "folo-wan",
    "cold": "kol",
    "quick": "kwikli",
    "always": "oldei",
    "wall": "wal",
    "tird": "tireda",
    "kough": "kofa",
    "less": "les",
    "kindness": "kainda",
    "maut": "mous",          # mouth
    "only": "onli",
    "granmat": "granmoter",
    "dry": "drai",
    "kloth": "klota",
    "road": "rodi",

    # --- R18 (2026-10-22): the 13 words the committee settled ---
    "mush": "meni",          # much = many (R18 #4)
    "ahed": "fronta-wei",
    "brekfast": "moring-fud",
    "still": "yeta",
    "about": "abau",
    "laif": "lifa",
    "solitud": "alon-nes",
    "breth": "brita",
    "bihaind": "baki-wei",
    "just": "onli",          # "merely" sense only
    "aut": "auta",
    "stik": "stika",

    # --- R7/R17: a free word takes the citation form (space -> citation) ---
    # The bare form is legal only inside a compound or before a suffix; the
    # rewriter keeps `pig-en` / `brik-hous` bare and only fixes the free word.
    "luv": "luva",
    "pig": "piga",
    "brik": "brika",
    "first": "firsta",
    "kalm": "kalma",
    "insaid": "insaida",
    "asept": "asepta",
    "autsid": "autsida",
    "brok": "broka",
    "fish": "fisha",
    "klok": "kloka",
    "mit": "mita",
    "rekomend": "rekomenda",
    "rit": "rita",
    "stret": "streta",
    "arond": "aronda",
    "bed": "beda",
    "hors": "horsa",
    "sand": "sanda",
    "branch": "brancha",
    "not": "nota",           # note (music); negation "not" was fixed by hand to "no"
    "shak": "shaka",
    "bank": "banka",
    "importent": "importenta",
    "last": "lasta",
    "market": "marketa",
    "strit": "strita",
    "sup": "supa",
    # Homographs: the corpus word is NOT the lexicon word its bare form matches.
    "mat": "moter",          # mother — not `mata` (matte)
    "fat": "fater",          # father — not `fata` (fat)

    # --- R8: English verbs the May corpus left untranslated ---
    "touch": "tucha",
    "stay": "stei",
    "feel": "fel",
    "fiel": "fel",
    "dream": "drim",
    "wake": "weika",
    "sleep": "slipa",
    "grow": "grota",
    # Not "bring": its headword `bringa` keeps the -a after a legal coda, so
    # bare_form() would write `bringa-edo`. The corpus already has `bring-edo`.

    # --- R19: a free consonant-final content root takes the citation form ---
    # Each target was checked against the corpus sense, not just the shape:
    #   liv -> livi (to live), NOT liva (alive)
    #   kwik -> kwikli (quick), NOT kwika (to hurry)
    #   bak -> baki (back), NOT baka (to bake)
    #   hard -> harda (difficult); "hard erd" (material) was fixed by hand to hardi
    #   wok -> woka (to walk); "work" uses were fixed by hand to werka (R11)
    # Left out on purpose: `lait` (light, illumination) — its only headword
    # `laita` means light in weight; `kart`, `own` — blocked by R19 (no form).
    "wind": "winda",
    "end": "enda",
    "lond": "londa",
    "hand": "handa",
    "send": "senda",
    "bird": "birda",
    "hard": "harda",
    "erd": "erda",
    "start": "starta",
    "hert": "herta",
    "child": "childa",
    "old": "olda",
    "warm": "warma",
    "storm": "storma",
    "dark": "darka",
    "werk": "werka",
    "rest": "resta",
    "fast": "fasta",
    "lern": "lerna",
    "sonj": "sonja",
    "soft": "softa",
    "tink": "tinka",
    "help": "helpa",
    "ask": "aska",
    "film": "filma",
    "gud": "guda",
    "kraud": "krauda",
    "bred": "breda",
    "wud": "wuda",
    "sad": "sada",
    "loud": "louda",
    "red": "reda",
    "rid": "rida",
    "bad": "bada",
    "mak": "maka",
    "tok": "toka",
    "sik": "sika",
    "wok": "woka",
    "kwik": "kwikli",
    "kuk": "kuka",
    "buk": "buka",
    "blak": "blaka",
    "bak": "baki",
    "hot": "hota",
    "wait": "waita",
    "kwaiat": "kwaiata",
    "eat": "eata",
    "liv": "livi",
    "hav": "hava",
    "giv": "giva",
    "big": "biga",
    "dog": "doga",
    "leg": "lega",
    "hop": "hopa",
    "slip": "slipa",
    "shop": "shopa",
    "enuf": "enufa",
}

# No canonical form exists, so fixing these means coining a word — a committee
# decision under vote/docs/PROCESS.md. Left in place on purpose.
# Empty since R18. "lost" was settled as a paraphrase ("Mi no nou la wei"),
# which is a sentence rewrite, not a word swap — fix it by hand.
NEEDS_COMMITTEE = {}

TOKEN_RE = re.compile(f"[{LETTER}][{LETTER}-]*")


def match_case(source, target):
    """Carry the source word's capitalization onto the replacement."""
    if source[:1].isupper():
        return target[:1].upper() + target[1:]
    return target


VOWELS = set("aeiou")
TOLERATED_CODA = {"n", "m", "l", "r", "s"}


def bare_form(citation):
    """Combining form of a citation root: R17's hyphen→bare rule.

    Only an R7 citation form has a bare variant, and R7's condition is precise:
    the `-a` exists to cover a coda that would otherwise be illegal. So `braka`
    → `brak` (bare coda 'k' is illegal alone, hence the citation vowel), while
    `folia` stays `folia` — `foli` ends in a vowel, so that final `-a` is part
    of the word, not epenthesis. The test is `element_defect`, the same
    predicate `validate_phonology.r7_bare_forms` uses to decide which bare forms
    it will accept; sharing it is what keeps the two scripts from disagreeing.
    """
    if len(citation) > 2 and citation.endswith("a") and "-" not in citation:
        stem = citation[:-1]
        if element_defect(stem):
            return stem
    return citation


def bare_form_if_legal_finally(citation):
    """Bare form, but only when it is still legal as the end of a word.

    R17 wants the bare form for every element of a hyphenated compound, yet the
    LAST element is also the end of the word, so its coda still has to be
    tolerated. `sun-raisa` → `sun-rais` (coda 's', fine); a root whose bare coda
    would be illegal keeps its citation vowel instead.
    """
    bare = bare_form(citation)
    if bare == citation:
        return citation
    idx = max((i for i, ch in enumerate(bare) if ch in VOWELS), default=-1)
    tail = bare[idx + 1:]
    if tail == "" or tail in TOLERATED_CODA:
        return bare
    return citation


def plural_for(stem):
    """R6: '-n' after a vowel-final stem, '-en' after a consonant-final one."""
    return "n" if stem and stem[-1] in VOWELS else "en"


def refit_suffixes(stem, suffixes):
    """Re-derive suffix allomorphs for a stem whose shape just changed.

    Replacing `leaf` with `folia` turns a consonant-final stem into a
    vowel-final one, so its plural moves from `-en` to `-n` (R6). Without this
    the migration would write `folia-en`.
    """
    out = []
    current = stem
    for suffix in suffixes:
        low = suffix.lower()
        if low in ("n", "en"):
            fixed = plural_for(current)
            out.append(fixed.upper() if suffix.isupper() else fixed)
            current = current + fixed
        else:
            out.append(suffix)
            current = current + low
    return out


# The one irregular present in VELA (R8): `bi` (to be) → `es`.
IRREGULAR_PRESENT = {"bi": "es"}

# Homographs whose sense depends on the sentence. Used where an English
# translation sits on the same line (the lexicon rows): the first cue that
# matches the line picks the target, otherwise the default applies.
#   wok — R11 split walk/work: `woka` = to walk, `werka` = to work. The pre-R11
#         lexicon examples use `wok` for "work" almost everywhere.
#   hard — `harda` = difficult, `hardi` = hard as a material.
SENSE_CUES = {
    "wok": ([(re.compile(r"\b(walk|sidewalk|park|foot|feet|crab)\b", re.I), "woka")], "werka"),
    "hard": ([(re.compile(r"\b(metal|bark|heel|hail|stone|wood)\b", re.I), "hardi")], "harda"),
    #   rid — `rida` = to read, `raida` = to ride.
    "rid": ([(re.compile(r"\b(ride|horse|hors|bicycle|baikel)\b", re.I), "raida")], "rida"),
    #   kwik — `kwikli` = quick, `kwika` = to hurry.
    "kwik": ([(re.compile(r"\bhurry\b", re.I), "kwika")], "kwikli"),
    #   it — untranslated English "it" → `li`, but the pre-reform spelling of
    #        "eat" was also `it` (`eat-hous` /it.haus/).
    "it": ([(re.compile(r"\beat\b", re.I), "eata")], "li"),
}


def sense_overrides(line):
    """Pick a target for each SENSE_CUES homograph from the cues on `line`."""
    chosen = {}
    for key, (cues, default) in SENSE_CUES.items():
        chosen[key] = next((target for cue, target in cues if cue.search(line)), default)
    return chosen


def lookup(key, overrides=None):
    """Replacement target for `key`, preferring a sense-checked override."""
    if overrides and key in overrides:
        return overrides[key]
    return REPLACEMENTS.get(key)


def present_form(token, overrides=None, headwords=frozenset()):
    """R8: rewrite the pre-reform present `X-a` to the citation form, or None.

    The May corpus marked the present with a hyphenated `-a` (`sing-a`, `tok-a`).
    R8 abolished that marker: the present IS the citation form, and the `-a` only
    appears where the bare root would end in an illegal coda. So `sing-a` → `sing`,
    `go-a` → `go`, but `tok-a` → `toka`, `wait-a` → `waita`.

    Only bilingual texts are rewritten (the migrator skips the HTML courses),
    which matters: the courses use a canonical topic marker `X-a`
    (`Dis buka-a, ol-person rida.`) that this rule must never touch.
    """
    parts = token.split("-")
    if len(parts) != 2 or parts[1].lower() != "a":
        return None
    root = parts[0]
    key = fold(root).lower()
    if key in IRREGULAR_PRESENT:
        return match_case(root, IRREGULAR_PRESENT[key])
    mapped = lookup(key, overrides)
    if mapped is not None:
        return match_case(root, mapped)
    if key in headwords and key + "a" not in headwords:
        # A legacy headword with a hard coda (`nof`): its present is the
        # headword as listed. Renaming the headword itself is a lexicon change.
        return match_case(root, key)
    citation = key + "a" if element_defect(key) else key
    return match_case(root, citation)


def rewrite_token(token, allow_present=True, overrides=None, headwords=frozenset()):
    """Return the canonical form of one token, or None if nothing changes.

    `allow_present=False` for the HTML courses, where `X-a` is the canonical
    topic marker, not the pre-reform present (see present_form). `overrides`
    are sense-checked targets for homographs (see sense_overrides).
    """
    present = present_form(token, overrides, headwords) if allow_present else None
    if present is not None:
        return present

    parts = token.split("-")
    if not parts:
        return None

    # Trailing inflection is preserved as-is; only content elements are mapped.
    n = len(parts)
    while n > 1 and parts[n - 1].lower() in SUFFIXES:
        n -= 1
    content, suffix = parts[:n], parts[n:]

    changed = False
    out = []
    for i, part in enumerate(content):
        key = fold(part).lower()
        target = lookup(key, overrides)
        if target is None:
            out.append(part)
            continue
        is_last = i == len(content) - 1
        bound = not is_last or suffix or len(content) > 1
        if bound and target.lower().startswith(key):
            # Already the bare form of its citation (`liv-edo`, `bak-tok`,
            # `bird-en`): correct inside a compound or before a suffix (R7/R19).
            # Re-deriving it from the citation would break roots whose citation
            # vowel is not `-a` (`livi`, `baki`) — `livi-edo`, `baki-tok`.
            out.append(part)
            continue
        if not is_last:
            # Non-final element of a compound: bare form (R17, hyphen→bare).
            target = bare_form(target)
        elif suffix:
            # Inflection attaches to the bare root (R8: `mak-edo`, not `maka-edo`).
            target = bare_form(target)
        elif len(content) > 1:
            # Final element of a compound: bare, unless that leaves an illegal coda.
            target = bare_form_if_legal_finally(target)
        out.append(match_case(part, target))
        changed = True

    if not changed:
        return None

    # The stem may have changed shape, so suffix allomorphs are re-derived (R6).
    stem = "".join(out)
    return "-".join(out + refit_suffixes(stem, suffix))


def migrate_line(line, spans, overrides=None, keep=frozenset()):
    """Rewrite only the given character spans of `line`. Returns (line, changes)."""
    changes = []
    # Right to left, so earlier offsets stay valid as the text length shifts.
    for start, end, _ in sorted(spans, reverse=True):
        segment = line[start:end]
        pieces = []
        cursor = 0
        for m in TOKEN_RE.finditer(segment):
            if "-" in m.group(0) and fold(m.group(0)).lower() in keep:
                continue  # a compound that is itself a headword
            new = rewrite_token(m.group(0), overrides=overrides, headwords=keep)
            if new is None or new == m.group(0):
                continue
            pieces.append(segment[cursor:m.start()])
            pieces.append(new)
            cursor = m.end()
            changes.append((m.group(0), new))
        if not changes:
            continue
        pieces.append(segment[cursor:])
        line = line[:start] + "".join(pieces) + line[end:]
    return line, changes


def migrate_file(path, dry_run, recognized):
    spans_by_line = {}
    for line_no, line, spans in vela_spans_md(path):
        # Same skip rule as the validator: a bare paragraph that reads as English
        # (BENCHMARK's "Or in standard VELA orthography with ...") is left alone.
        kept = [s for s in spans if is_vela_segment(line[s[0]:s[1]], s[2], recognized)]
        if kept:
            spans_by_line.setdefault(line_no, []).extend(kept)

    original = Path(path).read_text(encoding="utf-8")
    lines = original.split("\n")

    total = []
    for line_no, spans in spans_by_line.items():
        idx = line_no - 1
        if idx >= len(lines):
            continue
        new_line, changes = migrate_line(lines[idx], spans)
        if changes:
            lines[idx] = new_line
            for old, new in changes:
                total.append((line_no, old, new))

    if total and not dry_run:
        Path(path).write_text("\n".join(lines), encoding="utf-8")

    return total


# Lexicon columns that hold VELA, by header name. `Present` is the pre-R8
# paradigm column (`tok-a`); the example columns hold a VELA sentence, which in
# the paradigm tables is followed by `→ English`.
LEXICON_VELA_COLUMNS = {"present", "example", "vela example"}
ARROW = "→"


def lexicon_spans(path):
    """Yield (line_no, line, spans) for the VELA cells of a lexicon file.

    Tables use a dozen layouts, so each header row decides which columns are
    VELA. Inside an example cell only the text before `→` is VELA; the English
    translation after it, and the `English` columns, are never touched.
    """
    columns = []
    with open(path, encoding="utf-8") as f:
        for line_no, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            stripped = line.strip()
            if not stripped.startswith("|"):
                columns = []
                continue
            cells = [c.strip().lower() for c in stripped.strip("|").split("|")]
            if cells and cells[0] == "word":
                columns = [i for i, c in enumerate(cells) if c in LEXICON_VELA_COLUMNS]
                continue
            if not columns or not stripped.startswith("| **"):
                continue
            spans = []
            for idx in columns:
                span = _vela_cell_span(line, idx)
                if not span:
                    continue
                start, end = span
                arrow = line.find(ARROW, start, end)
                if arrow != -1:
                    end = arrow
                spans.append((start, end, "marked"))
            if spans:
                yield line_no, line, spans


def lexicon_headwords():
    """Every headword in the three lexicons, lowercased and diacritic-folded."""
    return {fold(word).lower()
            for path in LEXICON_FILES
            for word, _, _ in extract_lexicon(path)}


def migrate_lexicon(path, dry_run, headwords):
    """Migrate the VELA cells of one lexicon file (see lexicon_spans).

    A token that is itself a headword is left alone: renaming a headword
    (`bodi-wok`, `nait-dei`) is a lexicon decision, and rewriting it only in
    the example would make the example disagree with its own entry.
    """
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    total = []
    for line_no, line, spans in lexicon_spans(path):
        # The English on the same row tells which sense a homograph has.
        overrides = sense_overrides(line)
        new_line, changes = migrate_line(line, spans, overrides, keep=headwords)
        if changes:
            lines[line_no - 1] = new_line
            total.extend((line_no, old, new) for old, new in changes)
    if total and not dry_run:
        Path(path).write_text("\n".join(lines), encoding="utf-8")
    return total


MARKUP = re.compile(r"(<[^>]+>|&[a-z]+;)")


def migrate_html(path, dry_run):
    """Rewrite VELA inside `<span class="vela">` in a course page.

    The span is the same boundary the validator reads (`SPAN`), so English
    around it is never touched. Inside the span, tags and entities are passed
    through and only the text between them is rewritten. The pre-reform-present
    rule is off here: the courses use `X-a` as the topic marker.
    """
    text = Path(path).read_text(encoding="utf-8")
    total = []

    def fix_span(m):
        pieces = []
        for chunk in MARKUP.split(m.group(1)):
            if MARKUP.fullmatch(chunk):
                pieces.append(chunk)
                continue

            def fix_token(t, chunk=chunk):
                if t.start() > 0 and chunk[t.start() - 1] == "-":
                    # A cited bound morpheme (`-mak`, `-tok`): bare by definition.
                    return t.group(0)
                new = rewrite_token(t.group(0), allow_present=False)
                if new is None or new == t.group(0):
                    return t.group(0)
                line_no = text.count("\n", 0, m.start()) + 1
                total.append((line_no, t.group(0), new))
                return new

            pieces.append(TOKEN_RE.sub(fix_token, chunk))
        inner_start = m.start(1) - m.start()
        whole = m.group(0)
        return whole[:inner_start] + "".join(pieces) + whole[inner_start + len(m.group(1)):]

    new_text = SPAN.sub(fix_span, text)
    if total and not dry_run:
        Path(path).write_text(new_text, encoding="utf-8")
    return total


def main(argv):
    dry_run = "--dry-run" in argv[1:]

    roots = load_grandfathered(LEXICON_FILES)
    known = roots | r7_bare_forms(roots)

    # Refuse to run if any replacement target is not actually in the lexicon.
    missing = []
    for src, target in REPLACEMENTS.items():
        for element in target.split("-"):
            if element.lower() not in known:
                missing.append((src, target, element))
    if missing:
        print("ABORT — replacement targets absent from the lexicon:")
        for src, target, element in missing:
            print(f"  {src} -> {target}   ('{element}' not a lexicon root)")
        return 2

    print(f"{len(REPLACEMENTS)} replacements verified against the lexicon.")
    print(f"{len(NEEDS_COMMITTEE)} words left untouched (need a coinage — committee).\n")

    grand_total = 0
    # --lexicon: migrate the VELA example cells of the lexicons instead of the corpus.
    targets = list(LEXICON_FILES) if "--lexicon" in argv[1:] else corpus_files()
    headwords = lexicon_headwords()
    for path in targets:
        if path in LEXICON_FILES:
            changes = migrate_lexicon(path, dry_run, headwords)
        elif path.endswith(".html"):
            changes = migrate_html(path, dry_run)
        else:
            changes = migrate_file(path, dry_run, corpus_vocabulary(roots))
        if not changes:
            continue
        print(f"{path} — {len(changes)} change(s)")
        for line_no, old, new in changes:
            print(f"    {line_no:>5}  {old:<18} -> {new}")
        grand_total += len(changes)

    verb = "would change" if dry_run else "changed"
    print(f"\n{verb} {grand_total} token(s).")
    if dry_run:
        print("Dry run — nothing written. Re-run without --dry-run to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
