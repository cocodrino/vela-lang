# VELA Committee Deliberation — THE 13 UNCOINED CORPUS WORDS

**Date:** 2026-08-09
**Status:** OPEN — pending specialist review
**Proposed by:** Claude (corpus migration team)
**Scope:** 13 English concepts used in `docs/texts/` that have no canonical VELA form
**Blocks:** the last 17 validator errors, including the project's final `th` violation
**Method:** word-by-word verdict (the set is small and each case differs)
**Process:** `vote/docs/PROCESS.md` · voting rules §"Voting Rules"

---

## 1. Why this topic exists

`scripts/validate_phonology.py --corpus` currently reports **FAIL — 17 errors**. Every
one of them traces back to 13 English concepts the corpus needed and the lexicon never
supplied. A script cannot resolve them: choosing a word's shape is a canon decision
(R1–R17), which `PROCESS.md` reserves for the committee.

Reaching **0 errors** requires exactly these 13 decisions. Nothing else is outstanding.

## 2. Phase 0 — graphify context: STALE, DO NOT RELY ON IT

`PROCESS.md` makes reading `graphify-out/GRAPH_REPORT.md` mandatory. That file is dated
**2026-05-14**, before the entire July reform (R7 allomorphy, R8 present=citation, R14
person/pipol, R15 beautification, R17 invariable adjectives). Its community structure
describes a lexicon that no longer exists.

**Recommendation:** run `graphify update .` before treating any graph claim as evidence,
or decide this topic without graph context. The evidence in §4 is drawn directly from the
current lexicons and corpus, not from the graph.

## 3. Constraints every proposal must satisfy

| Rule | Constraint |
|---|---|
| R2 | No illegal final clusters. A root with an illegal coda takes thematic `-a`. |
| R2 | Codas tolerated word-finally: only `{n, m, l, r, s}`. |
| — | `th` (/θ ð/) is not in the inventory. Not negotiable, no grandfathering. |
| R3 | A transparent compound of ≤3 roots beats a loan. Where both work, the compound is preferred and the loan becomes a register synonym. |
| R7 | A root with a hard coda has two forms: citation `root+a` (standalone, dictionary headword) and bare `root-` (inside compounds). |
| R1 | Core stays near ~200 atoms. These 13 are everyday vocabulary, so they count against core — prefer compounds over new atoms. |
| R4 | Tag POETIC / PROSE where the word lands in verse. |

## 4. The evidence, word by word

Each entry gives: where it breaks, the sentence it lives in, what the validator says, and
**what already exists in the lexicon** — checked two ways (headword form and English gloss).

### TIER A — already solved by existing lexicon material (committee: confirm, don't coin)

**1. breath** — `docs/texts/SHORT_STORY_BIRD.md:45`
> `…stand-ed on ston, and breth-ed dipa.`

Validator: *illegal coda `-t` even after resyllabification (from `-th`)* **+ the only
remaining `th` violation in the project.**

**`brita` /ˈbri.ta/ "to breathe" already exists** — `LEXICON_BASE.md`, with a full
paradigm: `brit-a` / `brit-ed` / `brit-wil`. Moreover `LEXICON_EXPANSION.md` records that
a previous committee **already rejected `breta` as a duplicate of `brit`**.

→ Proposed verdict: this is a migration miss, not a coining. `breth-ed` → `brit-ed`.
Kills the last `th` violation with no new word.

**2. life** — `PHRASES_100.md:175`, `POEMS_COLLECTION.md:48`
> `Laif es beautiful.` · `Li tok-a wit moon about fri laif,`

Validator: *deprecated coda `-f`*.

**`lifa` already exists as a bound form** in `LEXICON_EXTENDED.md`: `lifa-koda` (genetic
code), `lifa-tipa` (species), `lifa-lerna` (biology). It has no standalone headword.

→ Proposed verdict: promote `lifa` /ˈli.fa/ to a headword. Corpus `laif` → `lifa`. This
also removes a live inconsistency: the lexicon says `lifa`, the corpus says `laif`.
Note: `lifta` (to lift) exists — check the committee is comfortable with `lifa`/`lifta`.

### TIER B — a transparent compound is available (R3 applies)

**3. breakfast** — `PHRASES_100.md:151`
> `Brekfast es redi.`

Validator: *illegal final cluster `-st`*.

Available parts: **`moring`** (morning, `LEXICON_BASE.md`) + **`fuda`/`fud-`** (food,
`LEXICON_BASE.md`). Precedent for this exact shape: `moring-watre` (dew).

→ Proposed: `moring-fud` /ˈmo.riŋ.fud/. R3 prefers this over adapting the loan.
⚠️ Separately: the corpus writes `morne` for "morning" everywhere, but the lexicon says
`moring`. That inconsistency is outside this topic but the committee should be aware.

### TIER C — genuine coining required (no existing material)

Verified absent from all three lexicons, by headword and by gloss.

**4. much** — `BENCHMARK.md:143`, `PHRASES_100.md:30`
> `Hau mush?` ("How much?")

Validator: *deprecated coda `-sh`*.

Nearby: **`hou`** = "how much" already exists (`Hou big es la hous?`), and **`meni`** =
many, **`veri`** = very. Options: (a) coin `musha`; (b) reuse `Hou meni?` and let `hou`
carry degree; (c) decide VELA does not split much/many and `meni` covers both.
**Semantic question, not just phonotactic.**

**5. still** (adverb, "todavía") — `POEMS_COLLECTION.md:21`
> `mi still wait-a, and rein sing-a.`

Validator: *illegal final cluster `-ll`*.

⚠️ **Collision:** `stila` /ˈsti.la/ already means **"to steal"**. The obvious thematic-vowel
form is taken. Precedent for this adverb class: `olredi` (already, loan). POETIC context
(R4) — the aestheticist's call matters here.

**6. about** — `POEMS_COLLECTION.md:48`, `SHORT_STORY_BIRD.md:45`
> `Li tok-a wit moon about fri laif,` · `Li tink-ed about wind, about mat-en warm wing…`

Validator: *deprecated coda `-t`*. High frequency: 4 uses in one sentence. Whatever is
chosen will be heard constantly, so cadence matters.

**7. lost** — `PHRASES_100.md:52`
> `Mi es lost.` ("I'm lost.")

Validator: *illegal final cluster `-st`*.

**`luza` /ˈlu.za/ "to lose"** exists (bare `luz-`). But R12 bans the passive, so `Mi es
luz-ed` is not available as a passive. Is "lost" here a state (adjective) or a verb?
The committee must decide the construction, not only the word — e.g. `Mi no nou la wei`
("I don't know the way") avoids the problem entirely.

**8. ahead** — `PHRASES_100.md:68`
> `Go stret ahed.`

Validator: *deprecated coda `-d`*. **`fronta`** (front) exists → a compound is plausible.

**9. behind** — `SHORT_STORY_BIRD.md:65`

Validator: *illegal final cluster `-nd`*. **`baki`** (back) exists → compound plausible.
Symmetry with #8: whatever shape "ahead" takes, "behind" should mirror it.

**10. just** (merely) — `SHORT_STORY_BIRD.md:55`
> `Li just fiel-ed herta ful and open, so li sing-ed.`

Validator: *illegal final cluster `-st`*.

⚠️ Near-collision: **`justis`** (justice) and **`fera`** (fair / just) both exist. The
"merely" sense and the "fair" sense must not converge on one form. "only" has no entry.

**11. out** — `SHORT_STORY_THREE_PIGS.md:32`
> `Wulfi jump-ed aut and ran awe in tu la fores.`

Validator: *deprecated coda `-t`*.

⚠️ **Orthographic inconsistency to settle:** the lexicon has **`autsida`** (outside, /aut.si.da/)
AND **`outputa`** (output, /out.pu.ta/) — `aut-` and `out-` for the same diphthong. The
committee should pick one spelling while it is here.

**12. solitude** — `POEMS_COLLECTION.md:81`
> `bot in solitud mi herta lern-a peis.`

Validator: *deprecated coda `-d`*. "alone" has no entry either, so no compound base
exists yet. POETIC context (R4). Coining "alone" first may be the cleaner path.

**13. stick** (noun) — `CLASSIC_STORY_THREE_PIGS.md:26`
> `Li blow-ed daun la stra hous and la stik hous.`

Validator: *deprecated coda `-k`*. **`wuda`** (wood) exists → compound plausible.
Note it appears in a compound slot (`stik hous`), so R7 needs both forms: citation for
standalone, bare for `…-hous`.

## 5. Summary table

| # | Concept | Breaks | Existing material | Path |
|---|---|---|---|---|
| 1 | breath | `th` + coda `-t` | **`brita`/`brit-`** | confirm, no coining |
| 2 | life | coda `-f` | **`lifa-`** (bound) | promote to headword |
| 3 | breakfast | cluster `-st` | `moring` + `fud-` | compound (R3) |
| 4 | much | coda `-sh` | `hou`, `meni`, `veri` | semantic decision |
| 5 | still | cluster `-ll` | ⚠️ `stila` = steal | coin, avoid collision |
| 6 | about | coda `-t` | — | coin (high frequency) |
| 7 | lost | cluster `-st` | `luza`, but R12 no passive | construction decision |
| 8 | ahead | coda `-d` | `fronta` | compound or coin |
| 9 | behind | cluster `-nd` | `baki` | mirror #8 |
| 10 | just (merely) | cluster `-st` | ⚠️ `justis`, `fera` | coin, avoid collision |
| 11 | out | coda `-t` | ⚠️ `autsida` vs `outputa` | coin + settle spelling |
| 12 | solitude | coda `-d` | — | coin "alone" first? |
| 13 | stick | coda `-k` | `wuda` | compound or coin |

## 6. Focus questions for the specialists

1. **Tier A (breath, life):** do you confirm these need no new coining, only that the
   corpus be corrected to `brit-` and `lifa`? If you dissent, say why the existing entry
   is unsuitable.
2. **`still`:** `stila` is taken by "to steal". Propose a form that does not collide, and
   say whether VELA needs a distinct "still/yet" at all or can paraphrase.
3. **`much`:** does VELA distinguish much from many? `meni` and `hou` already exist. One
   word or two?
4. **`lost`:** is this an adjective or a verb phrase? R12 forbids the passive — give the
   construction, not only the word.
5. **`ahead` / `behind`:** must they be symmetric? Compound from `fronta`/`baki`, or two
   new atoms?
6. **`out`:** settle `aut-` vs `out-` orthography, since the lexicon currently has both.
7. **`about`, `solitude`, `just`, `stick`, `breakfast`:** propose a form with IPA, an
   etymology note, and one example sentence, respecting R2/R3/R7.
8. **R1 budget:** how many of these 13 should become new core atoms versus compounds?

## 7. Required response format

For each word you rule on:

```
WORD: <english>
FORM: <vela> /IPA/            (citation form; give the bare form too if it has a hard coda)
TYPE: atom | compound | existing-entry | paraphrase
WHY:  <one or two sentences — the canon rule that drives it>
EXAMPLE: <one VELA sentence> → <english>
RISK: <collision or objection you can foresee, or "none">
VOTE: approve | approve-with-amendment | reject
```

If you have no competence on a word, write `ABSTAIN` — `PROCESS.md` records abstentions
without counting them.

## 8. Voting rules in force (`PROCESS.md`)

- One vote per specialist per discussion point.
- Majority wins. **Tie → the aestheticist breaks it** (beauty principle prevails).
- Abstentions recorded, not counted.
- Minimum 3 voices for a valid round.

⚠️ **Quorum warning for this round:** `PROCESS.md` specifies a 5-specialist committee
(phonologist, morphologist, lexicographer, semanticist, aestheticist). If this round runs
with fewer voices, the tiebreak rule has no aestheticist to invoke and the 3-voice minimum
may not be met. Record the actual roster in the consensus file.

## 9. Source files

| File | Why |
|---|---|
| `docs/grammar/GRAMMAR_COMPLETE.md` | current grammar canon |
| `vote/topics/consensus/fase5_consensus.md` | R1–R17, single source of canon |
| `docs/lexicon/LEXICON_BASE.md` | `brita`, `lifa`-compounds, `moring`, `fuda`, `luza`, `baki`, `autsida`, `meni`, `veri`, `hou`, `wuda` |
| `docs/lexicon/LEXICON_EXTENDED.md` | `lifa-koda`, `lifa-tipa`, `lifa-lerna` |
| `docs/lexicon/LEXICON_EXPANSION.md` | `stila`, `fronta`, `olredi`, `fera`, `lifta`, the `breta`→`brit` rejection |
| `docs/texts/*.md` | the 16 occurrences quoted in §4 |
| `scripts/validate_phonology.py` | run `--corpus` to reproduce the 17 errors |

## 10. Deliverables after the round

Per `PROCESS.md` Phase 3, the orchestrator (not the specialists) writes:

- `vote/topics/proposals/*.md` — one archival copy per specialist
- `vote/topics/discussion_plan.md` — synthesized conflicts
- `vote/topics/consensus/consensus.md` — final decisions, as **R18**
- `vote/docs/CHANGE_LOG.md` — appended entry
- then: lexicon entries, corpus migration, re-run the validator, target **0 errors**
