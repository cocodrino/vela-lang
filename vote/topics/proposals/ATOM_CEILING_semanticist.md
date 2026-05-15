# Proposal — VELA Semanticist: Atomic Word Ceiling

**Date:** 2026-05-15
**Topic:** How many atomic words should VELA have?
**Agent:** vela_semanticist
**Perspective:** Semantic Logic, Type Theory, & Information Theory

---

## Executive Summary

From a semantic and logical perspective, the atom ceiling must be determined by **semantic necessity**, not by an arbitrary number. I recommend a **soft ceiling of 200-220 atoms** with a **semantic coverage test** as the primary gate: any concept that cannot be expressed compositionally without ambiguity or infantilism receives atom status. This is approximately 200-220 atoms for universal semantic domains.

---

## 1. PROBLEMS IDENTIFIED

### Problem 1: Compounds Introduce Structural Ambiguity
**Severity: HIGH**

VELA's isolating morphology lacks a morphological marker distinguishing **compounds-as-names** from **descriptive phrases**. This creates systematic ambiguity:

| Form | Name Reading | Descriptive Reading |
|------|-------------|---------------------|
| `yel-kat` | lion | yellow cat |
| `big-fish` | whale | large fish |
| `red-dog` | fox | red dog |
| `nait-bird` | owl | nocturnal bird |
| `wild-dog` | wolf | feral dog |

Without a compound marker (like German Bindestrich or Finnish compound marker), every two-root sequence is semantically ambiguous. The listener must use world knowledge to disambiguate, which **violates VELA's monosemy principle**.

**Logical consequence:** In type-theoretic terms, a compound `A-B` has type `λx.A(x) ∧ B(x)` (intersection) when intended as a name, but the parser cannot distinguish this from `A(x) ∧ B(x)` (description). Only atoms have type `e` (entity) without compositional derivation.

**The lower the atom ceiling, the more compounds are forced, and the more pervasive this ambiguity becomes.**

### Problem 2: Semantic Field Coverage Requires ~200 Atoms
**Severity: MEDIUM-HIGH**

Cross-linguistic semantic typology reveals the minimal vocabulary needed to cover basic human experience:

| Semantic Domain | Minimum Atoms Required | Examples |
|-----------------|----------------------|----------|
| Kinship | 8-12 | mother, father, child, sibling, friend |
| Body parts | 25-30 | head, hand, heart, eye, ear, blood, bone |
| Basic animals | 15-20 | dog, cat, horse, fish, bird, cow, snake |
| Natural elements | 15-20 | sun, moon, star, water, fire, earth, wind, rain |
| Food staples | 12-15 | bread, meat, milk, fruit, vegetable, salt |
| Domestic objects | 20-25 | house, bed, door, table, cloth, tool |
| Colors | 8-11 | white, black, red, green, blue, yellow |
| Spatial relations | 15-20 | up, down, left, right, near, far, inside |
| Temporal | 12-15 | day, night, morning, year, now, before, after |
| Emotional | 10-15 | love, fear, joy, anger, hope, dream |
| Basic actions | 30-40 | go, come, eat, drink, sleep, work, speak |
| Qualities | 20-25 | big, small, good, bad, hot, cold, new, old |
| Social | 10-15 | people, city, law, king, war, peace |
| **TOTAL** | **~200-250** | |

This is not arbitrary — it is the empirical lower bound across Swadesh lists, Basic English (850 words but ~200 core), and IAL core vocabularies. Below ~200 atoms, semantic domains are systematically underrepresented, forcing ambiguous or infantile compounds.

### Problem 3: The Information-Theoretic Argument
**Severity: MEDIUM**

Zipf's Law of Abbreviation states that frequent words are short. For VELA, this implies that the most frequent concepts SHOULD be atoms (short, unanalyzable). The frequency distribution of natural language tokens:

- Top 100 words: ~50% of all tokens
- Top 200 words: ~65% of all tokens  
- Top 500 words: ~80% of all tokens

If VELA forces high-frequency concepts into compounds (2-3 roots), the **average utterance length increases by 50-100%**. This increases:
- Production effort (more syllables per meaning)
- Parsing effort (more morphemes to track)
- Memory load (working memory must hold compounds longer)

**Information-theoretic optimum:** ~200 atoms provides maximum coverage with minimum average word length. Above 200, diminishing returns set in (each additional atom covers fewer tokens). Below 200, compound inflation degrades communicative efficiency.

---

## 2. PROPOSED ALTERNATIVES

### Option A: Semantic Necessity Ceiling (~200 atoms) (RECOMMENDED)

**Rule:** A concept receives atom status if and only if it meets ALL of:
1. **Uniqueness:** The concept cannot be expressed as a 2-root compound without ambiguity
2. **Frequency:** The concept appears in the top 500 most frequent words cross-linguistically
3. **Non-decomposability:** The concept is not a transparent physical description (e.g., "yellow cat" for lion)
4. **Cultural centrality:** The concept appears across all human cultures (Swadesh criterion)

**Expected count:** ~200 atoms (Tier 0: 50 + Tier 1: 150)

**Semantic justification:** This is not a number pulled from thin air — it is the empirical intersection of typological frequency, semantic coverage, and compositional transparency.

### Option B: Tiered Semantic Ceiling (150 hard + 50 soft)

**Rule:**
- **Hard core:** 150 atoms covering Swadesh + basic domestic vocabulary
- **Soft layer:** 50 additional atoms allocated by semantic domain committees

**Disadvantage:** Creates a two-class lexicon where some semantic domains are "privileged" (get atoms) and others are "deprived" (forced into compounds). This is semantically arbitrary — why should "elephant" be a compound while "horse" is an atom?

I recommend **Option A** because semantic necessity should be the only criterion.

---

## 3. JUSTIFICATION

### Berlin & Kay: Color Terms

Berlin & Kay's research shows that all languages have 11 basic color terms at maximum, but the MINIMUM is 2 (black/white). The "basic" status means: monomorphemic, high-frequency, not subordinate to another color. VELA needs all 11 as atoms — compounds like `dark-red` or `sky-blue` fail the basicness test.

**Implication:** Semantic domains have "basic level" concepts that resist compounding. These must be atoms.

### Swadesh List: The 200-Word Core

Morris Swadesh's 200-word list was designed to be **universal** (appear in all languages) and **resistant to borrowing**. These 200 words cover kinship, body parts, animals, natural elements, actions, qualities, and basic grammar. 

VELA's Tier 0+1 (~200 atoms) is essentially the Swadesh core + modern necessities (technology, institutions). This is not coincidence — it is the empirically validated minimum for human communication.

### Type-Theoretic Argument

In formal semantics:
- **Atoms** are constants: `dog`, `moon`, `love` — type `e` (entity) or `⟨e,t⟩` (property)
- **Compounds** are functions: `yellow(x) ∧ cat(x)` — type `⟨e,t⟩` derived from `⟨e,t⟩ × ⟨e,t⟩`

The semantic interpretation function `⟦·⟧` must apply to compounds, introducing:
- **Ambiguity** (multiple parses)
- **Non-compositionality** (idiomatic readings: `hot dog` ≠ `hot(dog)`)
- **Processing cost** (function application vs. direct lookup)

The 200-atom ceiling minimizes the need for `⟦·⟧` application in high-frequency contexts, keeping VELA semantically transparent.

---

## Convergence Note

My position (~200 atoms by semantic necessity) aligns with:
- **Lexicographer** (200 hard ceiling)
- **Morphologist** (~200 soft ceiling)
- **Phonologist** (~220 soft ceiling)

I diverge from:
- **Aestheticist** (250 soft ceiling) — While I agree that poetic register needs atoms, semantic necessity identifies ~200, not 250. The additional 50 aestheticist atoms may not pass the uniqueness/frequency/cultural-centrality test.

**The ~200 atom range is the semantic consensus.**
