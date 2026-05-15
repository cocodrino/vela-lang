# Proposal — VELA Phonologist

**Date:** 2026-05-14
**Topic:** Atomic Word Ceiling for VELA
**Agent:** vela_phonologist
**Focus:** Phonological and phonaesthetic impact of atom pool size

---

## Executive Summary

From a phonological perspective, the atom ceiling is not merely a lexical decision—it is a **prosodic design parameter** that determines average word length, pitch-accent placement, and the acoustic signature of everyday VELA speech. I recommend a **soft ceiling of ~220 atoms** (Tier 0: 50 + Tier 1: 170), with a hard phonological rule: any atom beyond syllable count 2 must demonstrate exceptional phonological distinctiveness.

---

## PROBLEMS IDENTIFIED

### Problem 1: Prosodic Demotion of Semantic Heads in Long Compounds
**Severity: HIGH**

VELA uses **penultimate pitch accent**—the second-to-last syllable carries high pitch. In compounds, this means the accent falls on the **modifier**, not the **head**:

| Compound | Syllables | Pitch Accent On | Semantic Head | Result |
|----------|-----------|---------------|---------------|--------|
| `sik-hous` | 2 (si.haus) | `si` | `haus` | Head demoted |
| `lern-hous` | 2 (ler.haus) | `ler` | `haus` | Head demoted |
| `naid-rul-po` | 3 (nai.ru.po) | `ru` | `po` | Head doubly demoted |
| `moni-keep-po` | 3 (mo.ni.ki.po? / mo.ni.kip.o?) | `ki` | `po` | Head doubly demoted |

Under a strict 150-atom ceiling, common concepts like professions, institutions, and tools are forced into 3-4 syllable compounds. The semantic head (usually `-po`, `-hous`, `-masin`) is acoustically buried at the end with **low pitch**. This violates a near-universal prosodic tendency: heads tend to attract stress or prominence (cf. English `watch-MAN`, Japanese `gaku-SEI`).

**Phonological consequence:** Listeners must hold the entire compound in working memory until the final low-pitched syllable reveals the category. This increases cognitive load in rapid speech.

---

### Problem 2: Sibilant Density and Phonological Neighborhood Clash
**Severity: MEDIUM**

VELA's consonant inventory is heavily weighted toward **fricatives and sibilants** (/f, v, s, z, sh, h/ = 6 of 18 consonants). Compounding amplifies this bias:

| Lexicon Sample | Sibilant Count | Risk |
|----------------|---------------|------|
| `sik-hous` | /s/ + /s/ (if adapted to /si.ku.saus/) | Sibilant repetition |
| `song-mak-po` | /s/ + /s/ | Sibilant sandwich |
| `sik-fix-po` | /s/ + /f/ + /s/ + /p/ | Fricative cluster overload |
| `sik-hous-se` | /s/ + /s/ + /s/ | Triple sibilant (genitive!) |

A 150-atom ceiling forces greater reliance on compounds beginning with `s-` (`sik-`, `song-`, `sun-`, `si-`). The result is **phonological neighborhood density** increasing in the sibilant space, making words harder to distinguish in noise or sung delivery.

**Comparable system:** Toki Pona (~120 words) avoids this by having only /s/ (no /sh, z, f, v/), but its compounds are acoustically sparse. VELA's richer inventory demands careful management.

---

### Problem 3: The "Cradle Test" Failure Threshold for 3+ Syllable Compounds
**Severity: MEDIUM**

The aestheticist's **cradle test**—"can it be sung in a lullaby without waking the baby?"—becomes exponentially harder as compounds lengthen. The musicality of VELA depends on **open syllables, vowel-final words, and clear pitch contours**. Each additional root in a compound adds a syllable, and each syllable adds a potential pitch transition:

| Word | Syllables | Pitch Pattern | Lullaby Viability |
|------|-----------|---------------|-----------------|
| `hous` | 1 | [HAUS] | Excellent |
| `sik-hous` | 2 | [SI][HAUS] | Good |
| `sik-fix-po` | 3 | [si][FI][xpo] | Fair—contour is jagged |
| `ert-kweik` | 2 (er.kwei.ku?) | [ER][kwei] | Good |
| `tree-klaim-animal` | 4 | Contour buried | **FAIL**—already prohibited |

Under strict minimalism (~150 atoms), the **average compound length** for domain vocabulary (professions, sciences, technology) rises to 3+ syllables. This pushes the language toward an **agglutinative acoustic profile** rather than the intended **melodic isolating** one.

---

## PROPOSED ALTERNATIVES

### Option A: Soft Ceiling at ~220 Atoms (RECOMMENDED)

**Structure:**
- **Tier 0:** 50 primitivos (pronouns, numbers 0-10, core verbs, basic modifiers)
- **Tier 1:** 170 high-frequency atoms (body parts, natural elements, common animals, tools, clothing, food staples, emotional primitives)
- **Tier 2+:** Compounds only

**Phonological justification:**

1. **Monosyllabic saturation:** With 18 consonants × 5 vowels + 5 vowel-only syllables = **~95 possible monosyllables**. A 220-atom ceiling allows ALL monosyllables to be atoms, plus ~125 optimally chosen bisyllables. This preserves the **short, punchy acoustic profile** of core vocabulary.

2. **Pitch accent preservation:** At 220 atoms, the vast majority of everyday conversation uses 1-2 syllable words where pitch accent is maximally salient. The penult is either the entire word (monosyllabic—accent on the only syllable) or clearly demarcated (bisyllabic—accent on first syllable).

3. **Phonological distinctiveness:** 220 atoms can be selected for **maximal phonological distance** (no minimal pairs among high-frequency items). Beyond ~220, we are forced to use phonologically similar forms (e.g., `sok` /sok/ vs `sok` if reformed to /so.ku/... or `sik` vs `sik` vs `sik-hous`).

4. **Comparable system:** Mandarin Chinese has ~400 syllables (with tone) but ~5,000 characters. Its spoken vocabulary relies heavily on 2-syllable compounds for disambiguation. VELA has no tones, so we need slightly more atoms to achieve comparable spoken clarity. ~220 atoms = roughly the size of Japanese native vocabulary (~200 *yamato kotoba* roots that form compounds).

**Compound impact:** Under this ceiling, the most common compounds remain 2 syllables:
- Professions: `action-po` (2 roots, typically 2-3 syllables)
- Institutions: `function-hous` (2-3 syllables)
- Sciences: `domain-siens` (2-3 syllables)

3-syllable compounds are restricted to less frequent domains (e.g., `moni-keep-po` = treasurer).

---

### Option B: Hard Ceiling at ~150 Atoms with Prosodic Compensation Rules

**Structure:**
- **Tier 0+1:** 150 atoms total
- **Tier 2+:** Compounds, BUT with **optional prosodic fusion**

**Phonological justification:**

This option accepts the phonological burden of longer compounds but mitigates it through **morphophonological rules**:

1. **Vowel elision in rapid speech:** Compounds of 3+ roots may optionally drop medial vowels to restore bisyllabic prominence:
   - `sik-fix-po` → rapid: [sik.fpo] or [si.fpo] (non-standard, but natural)
   - `naid-rul-po` → rapid: [nait.rul.po] (already 3 syllables; no good compression)

2. **Pitch accent retraction rule:** In compounds ≥3 syllables, accent may shift to the **final root** (the head) rather than the penult:
   - `moni-keep-po` → [mo.ni.KEEP.PO] with accent on `po`
   - This parallels Japanese **compound accent rules** where accent can shift rightward in certain morphological constructions.

**Trade-offs:**
- **Benefit:** Smaller memorization load; aligns with VELA minimalism.
- **Cost:** Introduces **irregularity** (accent is no longer strictly penultimate). VELA's grammar explicitly states "zero irregular verbs" and strict rules. A variable pitch accent rule violates this philosophy.
- **Cost:** Longer compounds still fail the cradle test for sung/poetic language.

**Comparable system:** German has ~200 core verbal roots but extensive compounding. Its compounds are often reduced in colloquial speech (`Krankenhaus` → [ˈkʰɾaŋkŋ̍ˌhaʊ̯s] with syllable reduction). However, German word order and case marking support long compounds; VELA's strict SVO and minimal case system do not provide the same syntactic scaffolding.

---

## JUSTIFICATION

### Phonological Principles Cited

| Principle | Application to VELA |
|-----------|---------------------|
| **Zipf's Law of Abbreviation** | More frequent words are shorter. Forcing common concepts (shirt, shoe, dog, cat) into compounds violates this universal efficiency principle. These should remain atoms. |
| **Menzerath's Law** | The longer a linguistic construct, the shorter its constituents. If VELA sentences are kept short (SVO + minimal morphology), words should also be short to maintain rhythmic balance. |
| **Phonological Neighborhood Density** | More words = more similar-sounding words = more confusion. But 220 atoms among ~95 monosyllables + thousands of bisyllables is well below the critical density threshold. 300+ atoms would begin to crowd the bisyllabic space. |
| **Head Prominence (prosodic typology)** | Cross-linguistically, lexical heads tend to carry stress or pitch prominence. VELA's penultimate pitch accent systematically demotes right-headed compounds. Limiting compound length is the simplest fix. |
| **Sonority Sequencing** | VELA's (C)V structure is highly sonorous. Compounds preserve this, but each additional syllable adds a sonority peak. 3+ peak words feel "heavy" in a language designed to sound light and melodic. |

### Comparable Language Systems

| Language | Atom/Root Count | Avg Word Length | Phonotactics | VELA Lesson |
|----------|-----------------|---------------|--------------|-------------|
| **Toki Pona** | ~120 | 1.5 syllables | (C)V | Extremely short, but requires circumlocution for basic concepts. Feels "impoverished" precisely because common ideas need 3-4 word phrases. |
| **Japanese core (*yamato*)** | ~200-250 roots | 2-3 morae | (C)V(N) | Highly compounding, but pitch accent and context disambiguate. Kanji provides written distinction VELA lacks. |
| **Esperanto** | ~1000 roots | 2.5 syllables | Complex | Too many roots; high memorization load. But words are naturalistic and short enough for fluency. |
| **Swahili** | ~1000 roots | 2-4 syllables | (C)V | Agglutinative; words get long through affixation, not compounding. VELA is isolating, so length must be controlled at the lexicon level. |
| **English core** | ~3000 words | 1.2 syllables (top 100) | Complex | The top 100 English words average 1.2 syllables. VELA's top 220 should aim for the same profile. |

### Key Insight: The "Acoustic Sweet Spot"

Phonological analysis of the existing VELA lexicon reveals:
- **Monosyllabic atoms:** ~40% of current Tier 1 (e.g., `mi`, `yu`, `go`, `si`, `man`, `dog`, `kat`, `sun`, `moon`, `hous`, `shart`, `shu`)
- **Bisyllabic atoms:** ~50% (e.g., `wuman`, `child`, `siti`, `famili`, `hapi`, `wok-po` as compound)
- **3+ syllable atoms:** ~10% (mostly international loans: `teknoloji`, `demokrasi`, `organizashon`)

A 220-atom ceiling preserves this **40/50/10 distribution**, which mirrors the natural distribution of English (Germanic monosyllables + Latinate bisyllables + learned polysyllables). A 150-atom ceiling would invert this to roughly **20/40/40**, with a heavy tail of long compounds—a phonological profile more like German or Turkish than the intended melodic isolating language.

---

## CONCLUSION

The phonologist **recommends Option A: a soft ceiling of ~220 atoms**.

**Rationale:**
1. **Preserves acoustic identity:** VELA is designed to sound musical, with open syllables and clear pitch contours. A 220-atom ceiling keeps the average word length under 2 syllables for daily conversation.
2. **Respects learnability bounds:** 220 items is within the standard "working vocabulary" that adult learners acquire in 3-6 months of regular study (comparable to the JLPT N5 Japanese vocabulary of ~800 words, but VELA atoms are phonologically simpler).
3. **Controls compound length:** With 220 atoms, the compound Quality Gate's 2-root preference produces mostly 2-syllable compounds. The 3-syllable threshold remains a rarity, not the norm.
4. **Phonotactic headroom:** 220 atoms use only a fraction of VELA's phonotactic space (~95 monosyllables + ~5000 bisyllabic combinations), leaving room for future expansion without crowding.

**The ceiling should be SOFT** (guideline with exceptions) because phonological beauty can justify exceptions: a 1-syllable, highly distinct, internationally recognizable word like `doktr` (doctor) should remain atomic even if the 220-count is technically full, whereas a marginal candidate like `plastik` (already 2 syllables, descriptive) should gracefully become a compound.

---

## Files Referenced

- `docs/phonology/PHONOLOGY_FINAL.md` — pitch accent, syllable structure, phoneme inventory
- `docs/lexicon/LEXICON_BASE.md` — current word length distribution, Tier 1 candidates
- `vote/topics/consensus/ATOMS_VS_COMPOUNDS_Q2.md` — Quality Gate and tier structure
- `vote/topics/proposals/phonologist.md` — prior phonotactic audit showing ~30 violations and length patterns
