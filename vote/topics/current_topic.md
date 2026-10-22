# VELA Committee Deliberation — R19: BARE FORMS AS FREE WORDS

**Date:** 2026-10-22
**Status:** OPEN — pending specialist review
**Proposed by:** Claude (corpus migration team)
**Scope:** whether a consonant-final content root may stand alone in a sentence without its citation `-a`
**Blocks:** 308 corpus tokens (59 distinct words), 113 of them in the 5 HTML courses
**Process:** `vote/docs/PROCESS.md` · voting rules §"Voting Rules"

---

## 1. Why this topic exists

The R8 corpus migration (commit `c6d0cfb`) fixed the pre-reform present `X-a` and ~30
unambiguous bare free words. It stopped at 308 tokens because **the canon contradicts
itself** on whether forms like `liv`, `lern`, `old`, `big` may stand alone. A script
cannot pick between two ratified texts; the committee must.

## 2. The contradiction — verified in the files

| Source | What it says |
|---|---|
| **R7** (`fase5_consensus.md` §R7) | Every CONTENT root with a hard final coda (outside {n,m,l,r,s,ng}) has two forms: **citation** `root+a` for standalone use, **bare** only inside compounds. Only FUNCTION words (at, of, and, if, wit, but, self) are grandfathered with a single form. |
| **R8 table** (`fase5_consensus.md` §R8) | Header: "Legal suelta (vocal-final o coda ∈ {n,m,l,r,s,ng})". Rows listed under it: `si`, `go`, `wan`, **`tok`**, **`liv`**, **`lern`**. `tok` ends in /k/ and `liv` in /v/ — both hard codas by R8's own header. `lern` ends in a two-consonant cluster. |
| **GRAMMAR_COMPLETE.md §6.1** | Reconciled later: moves `tok` to the hard-coda row as **`toka`**, but keeps **`lern`** as a legal standalone present. `liv` is not listed. |
| **R2** (`fase5_consensus.md` §R2) | "Banned final clusters": `-tm -mnt -sm -ʃn -bl -ks -st -rd -rs -tr -ns -nt -nd -kl -dl -lt -lf -nr -dr -kt -sk -pt -nkr`. |
| **PHONOLOGY_FINAL.md §4** | "Los clusters (dos o más consonantes seguidas) **solo están permitidos al inicio** de una sílaba." — a general ban, broader than R2's list. |
| **R2 Amendment (2026-07-24)** | Native consonant-final roots (`lern`, `mak`, `sad`, `nof`) stay grandfathered **inside compounds**. Says nothing about standalone use; R7 two days later answered that (citation form). |
| **R17** | Adjectives are invariable, always citation form: `un olda hous`, `un biga famili`, `La famili es biga`. |
| **Lexicon** | Headwords are the citation forms: `lerna`, `toka`, `maka`, `olda`, `biga`, `guda`, `birda`, `childa`… ⚠️ "to live" is **`livi`** (`LEXICON_BASE.md:247`), not `liva` — `liva` is the adjective "alive" (`LEXICON_EXPANSION.md:554`). So under A, `Mi liv` → `Mi livi`. |
| **Validator** (`element_defect`) | Treats any single consonant outside {n,m,l,r,s} as a deprecated coda, and **any** 2+ consonant tail as an illegal cluster — i.e. it follows PHONOLOGY_FINAL §4, not R2's narrower list. |

So the courses (written after the reform) follow the R8 table (`Mi liv…`, `Mi lern…`,
`Mi mak…`), while the lexicon, R7 and R17 say `liva`, `lerna`, `maka`.

## 3. The 308 tokens, by word ending

Format: `word(total: texts t / courses c)`. Texts = `docs/texts/*.md`; courses = `books/Learning-VELA-Level{1..5}.html`.

**Single hard coda** (R7 applies directly — no cluster question):

| Coda | Words |
|---|---|
| `-v` | liv(18: 2t/16c) hav(4: 4t/0c) giv(1: 0t/1c) |
| `-k` | mak(9: 0t/9c) tok(8: 1t/7c) sik(2) wok(2) kwik(2) kuk(2: 0t/2c) buk(1) blak(1) bak(1: 0t/1c) |
| `-d` | gud(10: 8t/2c) kraud(5) bred(5) wud(3) sad(3) loud(2: 1t/1c) red(2) rid(1) bad(1: 0t/1c) |
| `-t` | lait(8: 6t/2c) hot(4) wait(3: 0t/3c) kwaiat(3: 0t/3c) eat(2: 1t/1c) |
| `-g` | big(11: 9t/2c) dog(7) leg(2) |
| `-p` | hop(4: 3t/1c) slip(2: 1t/1c) shop(2: 0t/2c) |

**Final cluster** (R2 bans some explicitly; PHONOLOGY_FINAL §4 bans all):

| Cluster | In R2's banned list? | Words |
|---|---|---|
| `-nd` | yes | wind(16: 12t/4c) end(10: 1t/9c) lond(7: 3t/4c) hand(7) send(1) |
| `-rd` | yes | bird(22: 19t/3c) hard(5: 1t/4c) erd(1) |
| `-st` | yes | rest(2: 0t/2c) fast(1) |
| `-sk` | yes | ask(1) |
| `-ld` | no | child(17: 12t/5c) old(17: 16t/1c) |
| `-rn` | no | **lern(15: 1t/14c)** |
| `-rm` | no | warm(7) storm(5) |
| `-rk` | no | dark(5) werk(3: 0t/3c) |
| `-rt` | no | start(2: 1t/1c) kart(1) hert(1: 0t/1c) |
| `-nj` | no | sonj(11) |
| `-ft` | no | soft(7) |
| `-nk` | no | tink(6: 0t/6c) |
| `-lp` | no | help(5: 4t/1c) |
| `-lm` | no | film(1) |
| `-wn` | no (diphthong + n?) | own(1) |

**Total: 308 tokens, 59 distinct words, 113 in the courses.** The biggest course items:
`liv` 16, `lern` 14, `mak` 9, `end` 9, `tok` 7, `tink` 6.

**No lexicon form at all** (separate question): `enuf` (enough), `kart` (cards — `karta` means "constitution"), `own` (adjective — `owna` is the verb "to own").

## 4. Options

| | Rule | Effect |
|---|---|---|
| **A** | **Literal R7.** Every consonant-final content root takes `-a` when free (`Mi livi`, `Mi lerna`, `un olda hous`). The R8 table rows `tok`/`liv`/`lern` and GRAMMAR's `lern` are errata. | Migrate all 308 tokens, including 113 in the courses. One rule, no exceptions. |
| **B** | **R2's list is exhaustive.** Single hard codas take `-a` (A), but clusters NOT on R2's list are legal standalone (`lern`, `old`, `child`, `warm`, `dark`…). | Migrates the single-coda words + R2-listed clusters; keeps `lern`, `old`, `warm`. Validator and PHONOLOGY_FINAL §4 must be amended. |
| **C** | **Grandfather a closed list of high-frequency native roots** with a single form, like the function words (`liv`, `lern`, `mak`, `tok`, `gud`, `big`, `old`…). | Fewer changes to the courses, but a new exception class next to R7, and the lexicon headwords for those roots must change. |

## 5. Focus questions

1. **Errata or rule?** Are the R8 table's `tok`/`liv`/`lern` rows an error (its own header defines "legal" as one soft coda), or did R8 intend to grandfather them?
2. **Clusters:** is R2's banned-cluster list exhaustive (B) or illustrative of PHONOLOGY_FINAL §4's general ban (A)?
3. **Grandfathering:** should any high-frequency content roots join the function-word exception (C)? If yes, name the closed list and the test for entering it.
4. **Courses:** the 5 courses teach `Mi liv`, `Mi lern`, `Mi mak` from Level 1. Is the pedagogical cost of changing them acceptable, and does your option need them changed?
5. **Gaps:** `enuf`, `kart` (cards), `own` (adjective) — coin, compound or paraphrase?

## 6. Required response format

```
QUESTION: <1-5>
POSITION: <A | B | C | specific answer>
WHY: <the canon rule that drives it — cite file and section>
CONSEQUENCE: <what changes in lexicon, grammar, courses, validator>
RISK: <what could go wrong, or "none">
VOTE: approve | approve-with-amendment | reject   (on your chosen option)
```

Close with one line: **FINAL VOTE: A | B | C** (or a named variant).

## 7. Voting rules in force (`PROCESS.md`)

One vote per specialist; majority wins; tie → aestheticist; abstentions recorded, not counted; minimum 3 voices.

## 8. Source files

| File | Why |
|---|---|
| `vote/topics/consensus/fase5_consensus.md` | R2, R2 Amendment, R7, R8, R17 |
| `docs/grammar/GRAMMAR_COMPLETE.md` §6.1 | present-tense table |
| `docs/phonology/PHONOLOGY_FINAL.md` §4 | general cluster ban |
| `docs/lexicon/LEXICON_BASE.md` | citation headwords (`livi`, `lerna`, `toka`, `maka`…) |
| `books/Learning-VELA-Level1.html` … `Level5.html` | the 113 course tokens (`<span class="vela">`) |
| `scripts/validate_phonology.py` | `element_defect` — how legality is computed today |
