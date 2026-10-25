# VELA Committee Deliberation — R20: THREE MISSING WORDS + LEGACY HARD-CODA HEADWORDS

**Date:** 2026-10-22
**Status:** OPEN — pending specialist review
**Proposed by:** Claude (corpus migration team)
**Process:** `vote/docs/PROCESS.md` · voting rules §"Voting Rules"
**Prior rounds:** R18 (13 corpus words), R19 (free consonant-final roots take the citation form, 5-0)

---

## 1. Why this topic exists

Applying R19 left three things a migration script cannot decide:

- **Part A** — three concepts the corpus uses with **no usable VELA form**: "light" (illumination), "cards", "own" (adjective).
- **Part B** — **legacy headwords** that end in a hard coda (`nof`, `art`, `grup`…). R19 says a free consonant-final content root takes the citation form, so these headwords look like errata — but renaming a headword is a canon decision, and several renames collide with existing words.
- **Part C** — two lines of grammar text that contradict R19 (modal rows).

## 2. Constraints

| Rule | Constraint |
|---|---|
| R2 / PHONOLOGY_FINAL §3.2 | Word-final codas only {n,m,l,r,s}, one consonant. Diphthong endings count as vowel-final. |
| R3 | A transparent compound of ≤3 roots beats a loan. |
| R7 / R19 | Content roots: citation form (`root+a`) free, bare form in compounds/before suffixes. Function words (at, of, and, if, wit, but, self…) keep one form. |
| R1 | Core stays near ~200 atoms; prefer compounds. |
| Semantics | No new homonym: a coined form must not equal an existing headword. |

---

## PART A — three missing words

### A1. "light" (illumination)

**The problem.** `lait` is used everywhere as "light" (illumination), but **only as a bound root** — the one free headword is **`laita` = light in WEIGHT** (`LEXICON_BASE.md:406`, example "la laimt box | the light box").

- Bound `lait` in lexicon compounds: `lo-lait` (`LEXICON_EXPANSION.md:637`), `soft-lait` (`:652`), `warm-lait` (`:658`), `kol-lait` (`:659`), `lait-red` "pink" (`:451`), `lait-spida` (`LEXICON_EXTENDED.md:178`).
- Free `lait` in the corpus (8 uses): `POEM_01_SUN_AND_MOON.md:17,27,57,67` ("Yu es mi lait"), `SHORT_STORY_BIRD.md:45,55`, `STORIES_SET_01.md:20` ("windo lait"), `PHRASES_100.md:104`.
- **Two wrong migrations already in the corpus:** an August mapping `light → laita` turned illumination into weight: `STORIES_SET_01.md:20` ("Yu hous laita save-ed wi herta") and `POEMS_COLLECTION.md:42` ("at morne laita").
- Nearby existing words: `brite` (bright), `lampi` (lamp), `shain`/`shin` (shine), `fai-flasha` (lightning).

**Options to weigh:** (a) `laita` becomes "light (illumination)" — the far more frequent sense — and "light (weight)" gets a new form or a compound (e.g. `no-hevi`); (b) keep `laita` = weight and coin a separate free form for illumination (e.g. a pan-Romance `luma`/`lumi`), leaving the `lait-` compounds as they are or migrating them; (c) another proposal.

### A2. "cards" (payment / playing cards)

**Corpus:** `PHRASES_100.md:38` — `Yu asepta kart?` ("Do you accept cards?").
**Problem:** `kart` + `-a` = `karta`, which already means **"constitution"** (`LEXICON_BASE.md:1101`). No "card" headword exists. Related: `pei-tek-po` (cashier, `LEXICON_EXPANSION.md:1380`).
Note: R19's semanticist proposed `plei-karta`, which still reuses `karta` (constitution) as its head.

### A3. "own" (adjective — "their own houses")

**Corpus:** `CLASSIC_STORY_THREE_PIGS.md:19` — `Tri smol piga-en go-ed from hom tu maki de-se own hous-en.`
**Problem:** `own` + `-a` = `owna`, which already means **"to own"** (verb, `LEXICON_EXPANSION.md:251`). The function word `self` exists (R7 single-form list), and so does the possessive `-se` (`de-se` = their).
**Options:** paraphrase (`de-se hous-en`, the possessive already says it), `self`-based (`de-self hous-en`?), or coin.

---

## PART B — legacy headwords ending in a hard coda

R19's rule, applied to the headwords themselves. Found by scanning every single-word headword whose ending `element_defect` flags (28 hits), then removing false positives (words ending in vowel-`y` such as `baby`, `navy`, `army`, `sallery`, `amnbasy`, `shy`) and R7's function words (`aft`, `and`, `at`, `bot`, `but`, `dat`, `if`, `of`, `self`, `wat`, `wit`).

| Headword | Meaning | Where | `+a` form | Collision? |
|---|---|---|---|---|
| `nof` | to know | `LEXICON_BASE.md:220` | `nofa` | none found |
| `let` | late | `LEXICON_BASE.md:171` | `leta` | none found |
| `ap` | up | `LEXICON_BASE.md:1444` (tagged "noun") | `apa` | none found — **or is `ap` a function word?** |
| `wot` | which | `LEXICON_BASE.md:147` | — | question word: function class? |
| `art` | art | `LEXICON_EXTENDED.md:491` (errata root, R2 Amendment) | `arta` | none; `arta-hous` already in use |
| `grup` | group | `LEXICON_EXTENDED.md:496` (errata root) | `grupa` | none; `star-grupa`, `muzika-grupa` in use |
| `tip` | type | `LEXICON_EXTENDED.md:494` (errata root) | `tipa` | none; `lifa-tipa` in use |
| `stap` | step | `LEXICON_EXTENDED.md:495` (errata root) | `stapa` | none found |
| `sav` | save | `LEXICON_EXTENDED.md:493` (errata root) | `sava` | **`sava` = to save already exists** (`LEXICON_EXPANSION.md:203`) — a duplicate, merge |
| `net` | network | `LEXICON_EXTENDED.md:492` (errata root) | `neta` | **`neta` = net (fishing)** (`LEXICON_EXPANSION.md:709`) — same concept or homonym? |
| `bit` | bit (computing) | `LEXICON_EXTENDED.md:497` (errata root) | `bita` | **`bita` = bitter** (`LEXICON_EXPANSION.md:625`) — real homonym |

Note: the R2 Amendment (`fase5_consensus.md` §Amendment 2026-07-24) listed `art, net, sav, tip, stap, grup, bit, kod, wei, taim` as legal **roots** so compounds could use them — written two days **before** R7 introduced citation forms. `kod`, `wei`, `taim` are not in this table: `kod` already has `koda`; `wei` and `taim` end in a diphthong or `-m` and are legal.

---

## PART C — grammar text that contradicts R19

`LEXICON_BASE.md:376-380` (modal rows):
- `kan` — "kan + bare root" · `mas` — "mas + bare root" · `shoda` — "shod + bare root", example `Yu shod kom.`

After a modal the verb stands free (space), so under R19 it takes the citation form — the courses already write `Mi no kan draiva`. And `shod` in `Yu shod kom` is the bare form of the headword `shoda`, used free. Confirm: the wording becomes "+ citation form", the example `Yu shoda kom`.

---

## 3. Focus questions

1. **A1:** which sense does `laita` keep? Give the free form for the other sense, and say what happens to the bound `lait-` compounds.
2. **A2:** form for "card(s)", collision-free.
3. **A3:** paraphrase or coinage for "own" (adjective)?
4. **B:** for each headword in the table — rename to `+a`, merge with an existing entry, or classify as a function word (exempt)? Resolve `bit`/`bita` and `net`/`neta`.
5. **C:** confirm the modal-row correction.

## 4. Required response format

```
ITEM: <A1 | A2 | A3 | B:<headword> | C>
FORM: <vela> /IPA/  (or "rename", "merge with X", "function word", "paraphrase: …")
WHY: <the rule — cite file and section>
RISK: <collision or objection, or "none">
VOTE: approve | approve-with-amendment | reject
```

## 5. Voting rules (`PROCESS.md`)

One vote per specialist per item; majority wins; tie → aestheticist; abstentions recorded, not counted; minimum 3 voices.

## 6. Source files

| File | Why |
|---|---|
| `vote/topics/consensus/fase5_consensus.md` | R2 + Amendment, R3, R7, R19 |
| `docs/phonology/PHONOLOGY_FINAL.md` §3.2, §4 | legal codas |
| `docs/lexicon/LEXICON_BASE.md`, `LEXICON_EXTENDED.md`, `LEXICON_EXPANSION.md` | headwords and collisions cited above |
| `docs/texts/*.md` | the corpus lines cited above |
