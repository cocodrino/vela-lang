# Proposal — VELA Semanticist (ollama/deepseek-v4-pro)
## Standby Issues Deliberation — Semantic/Compositional Analysis

---

## ISSUE 1: Atomic Word Threshold (745 atoms, 35 compounds)

### Semantic Assessment: HIGH

**The compositional principle**: "Everything you can deduce, you don't need to memorise." This is not a convenience — it is a semantic design axiom.

In formal terms: a compound `α + β` is semantically compositional iff `⟦α-β⟧ = f(⟦α⟧, ⟦β⟧)` for some transparent compositional function `f` (typically conjunction, modification, or argument saturation).

An opaque atomic word `γ` where no `f` exists over simpler parts requires arbitrary memorization: `⟦γ⟧ = c` (constant), with no derivational path.

**Cognitive semantic argument**: The human lexicon has capacity for ~10,000–50,000 words in native languages. But auxiliary languages target non-native learners who lack the immersive exposure to absorb opacity. For them, every opaque form is a flashcard. Every compound is a puzzle they can solve.

**The ~200 atom proposal** (Semanticist refinement):
Not all atoms are equal. Some encode **primitives** — concepts with no simpler decomposition (pronouns, basic kinship, natural elements, spatial relations, core actions). Others encode **convenience borrowings** — words that COULD be compounds but were borrowed as atoms for brevity (`hospital`, `telefon`).

**Two-tier atomic system**:
- **Tier 0 — Primitives (~80)**: Cannot be decomposed without semantic loss. `wan` (one), `mi` (I), `es` (be), `wata` (water), `faya` (fire), `mama` (mother), `hous` (house), `go` (go), `si` (see).
- **Tier 1 — High-frequency shortcuts (~70)**: Could be compounds but are so frequent that atomicity saves processing time. `kar` (car), `buk` (book), `fo` (food), `moni` (money), `taim` (time), `wok` (work).
- **Everything else**: Compound.

This gives ~150 atoms total. Above this, every additional atom is a semantic debt — an unanalyzed borrowing that future learners must memorize.

**Specific analysis of long atoms**:
- `undrstand` → No simpler decomposition available? Yes: `kom-hendi` (comprehend). Semantic path: `kom` (with) + `hendi` (grasp) = "grasp together" = understand.
- `prezidnt` → `hed-man` (head-man) or `naid-rul-man` (nation-rule-man). Both semantically transparent.
- `sientist` → `nau-man` (know-man) or `siens-man` (science-man). Transparent.
- `vokabulari` → `word-list`. Transparent.
- `aereplan` → `sky-bird`. Metaphorically transparent.
- `buterflai` → `biju-fle` (beauty-fly). Transparent.

**Rating**: HIGH. The current 745-atom lexicon is semantically impoverished — it demands memorization instead of reasoning.

---

## ISSUE 2: PROFIL Homonymy

### Semantic Assessment: CRITICAL

**Formal analysis**:
- `profil₁` (profile): type `e` (entity — a shape/outline/account summary). Predicative use: `La profil es gud.` = "The profile is good."
- `profil₂` (profit): type `e` (entity — monetary gain). Predicative use: `La profil es gud.` = "The profit is good."

Both are count nouns (`un profil`), both take the same determiners, both appear in the same syntactic positions. The sentences are **structurally identical**:
- `La biznes haz gud profil.` → "The business has a good profile." OR "The business has good profit."
- `Mi si la profil.` → "I see the profile." OR "I see the profit."

Context disambiguates in many cases (a person has a profile, a store has profit), but **coreferential ambiguity** is fatal:
- `La profil grow.` → Does a profile grow? (social media). Does profit grow? (finance). Both are equally plausible.

**Homonymy resolution**:
- Keep `profil` = profile (the more visually/conceptually basic meaning — an outline, a side-view).
- Change "profit" to `gain` (monetary gain, increase). `gain` is semantically narrower than `profit` (which includes non-monetary benefit), but in basic vocabulary, narrow precision is preferable to ambiguity.

**Alternative**: `profeto` from Latin *profectus*. Semantically precise but 3 syllables. `gain` is 1 syllable, more basic.

**Rating**: CRITICAL. Perfect homophones with identical syntactic distribution are the most dangerous type of lexical ambiguity.

---

## ISSUE 3: SE Noun vs SE Suffix

### Semantic Assessment: LOW-MEDIUM

**Formal types**:
- `se₁` (sea): type `e` — `⟦se⟧ = λw. sea(w)` (a constant entity in every world)
- `-se₂` (genitive): type `⟨N, N⟩` — `⟦-se⟧ = λPλxλw. P(w)(x) ∧ possessor(w)(x)` (a nominal modifier introducing possession)

**Disambiguation mechanism**:
- `se₁` appears as a **head noun**: `la se`, `in la se`, `La se es kold.` It is saturated by the article or preposition.
- `-se₂` appears as a **modifier** attached to a noun/pronoun: `mi-se buk`, `la buk-se kava`. It is a clitic, not a free word.

**Syntactic environments**:
- After article (`la se`) = sea
- After pronoun (`mi-se`) = genitive
- After noun (`buk-se`) = genitive

These environments are disjoint. A genitive suffix never follows an article; a noun "sea" never follows a pronoun directly.

**The only edge case**: `se-se` (sea-GEN). Phonologically `/se.se/`, syntactically `[[se]-se]`. Could this be parsed as `[se [se]]` = "the sea's sea"? In theory, yes, but semantically vacuous. No learner would produce this.

**Semanticist verdict**: The collision is **formal but not functional**. The types and syntactic distributions are disjoint. However, for maximal monosemy (one form = one meaning), changing "sea" to `mar` or `oce` is a zero-cost improvement.

**Rating**: LOW-MEDIUM. Syntactic containment is robust. Change is cosmetic, not urgent.

---

## ISSUE 4: Numbers 0–1000

### Semantic Assessment: HIGH

**The semantic structure of numerals**:
Numerals denote **cardinal quantities** — functions from sets to truth values: `⟦ten⟧ = λX. |X| = 10`. The semantic composition of complex numerals is arithmetic: `⟦ten-wan⟧ = λX. |X| = 10 + 1 = 11`.

**Current system semantic defects**:
1. `elevn` — opaque. No semantic relationship to `ten` + `wan` is recoverable from the surface form. The learner must memorize: "elevn means 11" as an arbitrary fact.
2. `twelv` — same opacity. "twelv means 12" — arbitrary.
3. `twenti` — marginally related to `tu` (two), but the relationship is not transparent. English "twenty" ← Old English *twentig* (two-ty), but the compound fossilized.
4. `handrd` — completely opaque. No relationship to `ten` is visible.

**Semantic transparency**: A numeral system is transparent iff the semantic value of each compound is predictable from its parts.
- `ten-wan` = 10 + 1 → transparent ✓
- `tu-ten` = 2 × 10 → transparent ✓
- `ten-ten` = 10 × 10 → transparent ✓
- `elevn` = 11 → opaque ✗
- `handrd` = 100 → opaque ✗

**Cross-linguistic semantic evidence**:
- Chinese: 十一 = 10+1, 二十 = 2×10, 一百 = 1×100. Fully transparent.
- Japanese: 十一 = 10+1, 二十 = 2×10. Fully transparent (except 100 = hyaku, 1000 = sen — atomic exceptions).
- English: eleven, twelve, twenty, thirty... mostly opaque. English learners memorize these as arbitrary forms.

**VELA should follow the Chinese/Japanese model**, not the English/German model.

**Zero exception**: `zero` is semantically the null cardinal. It is not 0×10 or any compound. Keeping it atomic is semantically justified — it is the additive identity, not a quantity.

**Recommended system**:

| # | Form | Semantic Composition |
|---|------|---------------------|
| 0 | `zero` | atomic (null element) |
| 1–10 | `wan...ten` | atomic (primitives) |
| 11–19 | `ten-wan...ten-nain` | 10 + n |
| 20–90 | `tu-ten...nain-ten` | n × 10 |
| 21–99 | `tu-ten-wan...nain-ten-nain` | (n×10) + m |
| 100 | `ten-ten` | 10 × 10 |
| 101–999 | `ten-ten-wan...` | recursive |
| 1000 | `ten-ten-ten` | 10 × 10 × 10 |

**Rating**: HIGH. Numbers are a closed semantic field where transparency has maximum payoff — every learner uses them daily.

---

## Summary Table

| Issue | Semantic Risk | Recommended Reform |
|-------|--------------|--------------------|
| 1 — Atomic threshold | HIGH | ~150 atoms (primitives + high-frequency shortcuts); compound everything else |
| 2 — PROFIL | CRITICAL | Keep `profil` = profile; "profit" → `gain` |
| 3 — SE collision | LOW-MEDIUM | Leave as-is (types are disjoint), OR change sea → `mar` for purity |
| 4 — Numbers | HIGH | Full decimal compounding; `elevn`→`ten-wan`, `handrd`→`ten-ten` |

**Meta-priority**: Issue 2 (profil) > Issue 4 (numbers) > Issue 1 (atoms) > Issue 3 (se).

---
*Semanticist — Standby Issues Deliberation*
*Focus: formal semantics, compositionality, type theory, functional load, lexical ambiguity*
