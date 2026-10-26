# VELA Committee Deliberation — R21: THE PAST SUFFIX `-ed` AND THE VERB "TO BE"

**Date:** 2026-10-26
**Status:** OPEN — pending specialist review
**Proposed by:** Claude, after public feedback on Reddit (r/conlangs)
**Process:** `vote/docs/PROCESS.md` · voting rules §"Voting Rules"

---

## 1. Why this topic exists

A Reddit reviewer found two real inconsistencies in VELA's canon. Both were verified in the repo before opening this round.

1. **`-ed` breaks the coda rule.** `PHONOLOGY_FINAL.md` §3.2 says a word may end only in a vowel or in one of {n, m, l, r, s}. Every past tense ends in `-ed` (`mak-ed`, `hav-ed`), so every past-tense word ends in /d/. The validator never caught it: `scripts/validate_phonology.py` strips `-ed` as a suffix (line ~92) **before** checking the final coda. The rule and the grammar contradict each other, and the tool hid it.
2. **"No irregular verbs" vs. "one irregular verb".** The landing page says both. In the canon:
   - `LEXICON_BASE.md:218` — `bi` "to be": present **`es`**, past `bi-ed`, future `bi-wil`.
   - `LEXICON_BASE.md:219` — `es` "to be (stative)": present `es`, past `es-ed`, future `es-wil` — a fully **regular** verb already.
   - `GRAMMAR_COMPLETE.md` §6.3 (line ~482) calls `bi` "regular", then says its present is `es`, its past `es-ed`, and its future **`wil es`** — a periphrastic future that contradicts the `-wil` suffix everywhere else.
   - `GRAMMAR_COMPLETE.md:1072` (FAQ) says there are no irregular forms at all and lists `bi-a, bi-ed, bi-wil` — pre-R8 forms.
   The reviewer also argued that an auxiliary language does not need even one irregular verb.

## 2. Usage data (corpus `docs/texts/` + the 5 courses, verified 2026-10-26)

| Form | Tokens |
|---|---|
| any `X-ed` (past) | **327** (texts 240, courses 87) — plus ~120 lexicon lines |
| `es` (present "to be") | 227 |
| `es-ed` | 29 |
| `es-wil` | 2 |
| `bi` (free) | 12 (mostly in grammar text) |
| `bi-ed` / `bi-wil` | 2 / 2 |

So in practice the language already uses **`es` / `es-ed` / `es-wil`**; `bi` barely appears.

## 3. Constraints

| Rule | Constraint |
|---|---|
| PHONOLOGY_FINAL §3.2 | Word-final codas only {n, m, l, r, s} (one consonant). |
| R7 | Function words (at, of, and, if, wit, but, self…) are exempt, single form. Suffixes are not function words. |
| R8 / R19 | Present = citation form; past and future attach to the bare root (`mak-ed`, `mak-wil`). |
| Existing suffixes | `-wil` future, `-n`/`-en` plural, `-se` genitive, `-to` locative, `-po` profession. A new suffix must not collide with these or with a pronoun in a way that harms parsing (`de` = they, `di`? check). |
| Principles | Simplicity → Transparency → Beauty → Universality. |

## 4. Questions and options

### Q1 — the past suffix

| | Option | Cost |
|---|---|---|
| **A** | Keep `-ed`; amend §3.2 to say inflectional suffixes may end in /d/ (a documented exception, like R7's function words). | No migration. The coda rule gets a second exception class. |
| **B** | Replace `-ed` with a vowel-final past suffix (e.g. `-eda`, `-edi`, `-de`, `-di`, …). Propose the exact form; check collisions with the suffixes and pronouns above and with headwords. | Mechanical migration of ~450 tokens (scriptable with `scripts/migrate_corpus.py`). Rule stays exceptionless. |
| **C** | Add /d/ to the tolerated word-final codas for every word. | Broad phonology change; loosens a core rule for one suffix. |

### Q2 — "to be"

| | Option | Cost |
|---|---|---|
| **A** | Keep `bi` with irregular present `es`; just fix the docs (`wil es` → `es-wil`/`bi-wil`, FAQ). | One irregular verb remains; landing must say "one irregular verb". |
| **B** | Retire `bi`. `es` becomes the one verb "to be", fully regular: `es` / `es-ed` / `es-wil` (or the Q1 past form). | Zero irregular verbs. ~16 `bi` tokens rewritten; matches what the corpus already does. Check: `es` as citation form is legal (ends in /s/). |
| **C** | Make `bi` regular (present `bi`) and replace the 227 `es`. | Large migration against current usage. |

## 5. Required response format

```
QUESTION: Q1 | Q2
POSITION: A | B | C   (for Q1-B give the exact suffix and its IPA)
WHY: <rule or evidence — cite file and line>
RISK: <collision, migration risk, or "none">
VOTE: approve | approve-with-amendment | reject
```

End with `FINAL VOTE: Q1=<A|B|C> (<suffix if B>), Q2=<A|B|C>`.

## 6. Source files

`docs/phonology/PHONOLOGY_FINAL.md` §3.2 · `vote/topics/consensus/fase5_consensus.md` (R7, R8, R19, R20) · `docs/grammar/GRAMMAR_COMPLETE.md` §6.1–6.3, FAQ · `docs/lexicon/LEXICON_BASE.md:218-219` · `scripts/validate_phonology.py` (SUFFIXES).
