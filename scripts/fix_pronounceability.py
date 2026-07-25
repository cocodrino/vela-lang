#!/usr/bin/env python3
"""Restore the dropped vowel in words whose spelling is unpronounceable.

VELA is write-as-you-speak, but ~49 legacy words dropped the English schwa
entirely, leaving an obstruent+sonorant cluster with no vowel (`rivr`, `botl`,
`opn`, `gvrnmnt`). That both breaks (C)V and makes the word unreadable. Here we
put the pure vowel back (`rivr` -> `river`), matching the English source.

Applies a whole-word replacement across the lexicons and the corpus (headword,
AFI, and every example use), then you regenerate the dictionary and validate.
"""

import glob
import re

MAP = {
    "advrtais": "advertais", "appl": "apel", "batn": "baton", "bikl": "baikel",
    "botl": "botel", "brotr": "broter", "butr": "buter", "citizn": "sitizen",
    "dificlti": "difikulti", "diskovr": "diskover", "doktr": "dokter", "fatr": "fater",
    "fly": "flai", "gardn": "garden", "granfatr": "granfater", "granmotr": "granmoter",
    "gvrnmnt": "goverment", "hotl": "hotel", "igl": "igel", "imposibl": "imposibel",
    "kompiutr": "kompiuter", "kuzn": "kuzen", "kwikly": "kwikli", "letr": "leter",
    "livr": "liver", "medikl": "medikal", "miscl": "muskul", "mitn": "miten",
    "motr": "moter", "neibr": "neiber", "nevr": "never", "nombr": "nomber",
    "ofn": "ofen", "opn": "open", "oprtuniti": "oportuniti", "pasengr": "pasenjer",
    "posibl": "posibel", "postr": "poster", "ppl": "pipel", "purpl": "purpel",
    "remembr": "remember", "rivr": "river", "sevn": "seven", "sugr": "sugar",
    "tartl": "tartel", "undrstand": "understand", "unkl": "unkel", "vinegr": "vinegar",
    "watrmeln": "watre-melon",
    "Septembr": "September", "Octobr": "Oktober", "Novembr": "November",
    "Decembr": "Desember", "Satrdei": "Saterdei",
}

FILES = (["docs/lexicon/LEXICON_BASE.md", "docs/lexicon/LEXICON_EXTENDED.md",
          "docs/lexicon/LEXICON_EXPANSION.md", "vote/topics/proposals/exp_nature.md"]
         + glob.glob("docs/texts/*.md"))

# longest keys first so e.g. `granfatr` is handled before `fatr`
PATTERN = re.compile(r"\b(" + "|".join(sorted(MAP, key=len, reverse=True)) + r")\b")


def main():
    total = 0
    for path in FILES:
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        new, n = PATTERN.subn(lambda m: MAP[m.group(1)], text)
        if n:
            open(path, "w", encoding="utf-8").write(new)
            total += n
            print(f"  {path}: {n} replacement(s)")
    print(f"Done — {total} replacement(s) across {len(FILES)} file(s).")


if __name__ == "__main__":
    main()
