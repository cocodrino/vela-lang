# Proposal — VELA Morphologist: Atomic Word Ceiling

**Date:** 2026-05-15
**Topic:** How many atomic words should VELA have?
**Agent:** vela_morphologist
**Perspective:** Morphological & Grammatical Architecture

---

## Executive Summary

From a morphological perspective, the atom ceiling is a **derivational boundary condition**. It determines whether VELA's grammar operates as a true agglutinative system or degenerates into an isolating lexicon with decorative compounding. I recommend a **soft ceiling of 200 atoms** (Tier 0: 50 + Tier 1: 150), with the Quality Gate as the active filter rather than a hard numeric limit.

---

## 1. PROBLEMS IDENTIFIED

### Problem 1: The 150-Atom Ceiling Breaks the Compound Engine
**Severity: HIGH**

At 150 atoms, approximately **300-400 common concepts** must be expressed as compounds. The Q2 Quality Gate (SHORT ≤2 roots, MEANINGFUL, SOUNDS GOOD, NOT INFANTILE) eliminates many of these:

| Concept | Compound Attempt | Quality Gate Result |
|---------|-----------------|---------------------|
| pillow | `hed-rest` | FAIL — infantile (reduces to function) |
| blanket | `bed-kloth` | FAIL — descriptive, not unique |
| elephant | `long-nos-animal` | FAIL — 3 roots, too long |
| dream | `slip-vision` | FAIL — 3 roots, non-compositional |
| story | `fikshon-tok` | FAIL — 3 roots, redundant |

When the Quality Gate rejects 60-70% of necessary compounds, the language faces a **derivational crisis**: either abandon the Gate (destroying morphological consistency) or expand the atom pool.

**Morphological principle:** An agglutinative system requires that compounding be the DEFAULT and RELIABLE strategy for vocabulary extension. If compounding fails routinely, the system is broken.

### Problem 2: Case Marking on Long Compounds Creates Parsing Ambiguity
**Severity: MEDIUM**

GRAMMAR_COMPLETE.md Section 15 states that case suffixes attach to the **last root** of a compound:
- `sik-hous-se` = "of the hospital" (genitive on `hous`)
- `moni-keep-po-te` = "at the banker" (locative on `po`)

With 3+ root compounds forced by a low ceiling:
- `tree-klaim-animal-se` = "of the tree-climbing-animal" (koala)
- Does `-se` attach to `animal` (the semantic head) or the whole compound?
- If `tree` is itself modified: `big-tree-klaim-animal-se` — now we have 4 roots + case suffix.

The morphological parser must track root boundaries across 4-5 morphemes. This is feasible for a designed language but **violates VELA's simplicity principle**.

**Natural language parallel:** German compounds can grow indefinitely (`Donau­dampf­schiff­fahrts­elektrizitäten­haupt­betriebs­werk­bau­unter­beamten­gesellschaft`), but German has native speakers who grew up with the system. VELA is an IAL — learners need transparent morphology.

### Problem 3: The Tier Boundary Creates Arbitrary Morphological Classes
**Severity: LOW-MEDIUM**

If Tier 1 ends at 150 atoms, any atom at position 151 is morphologically identical to position 149 but etymologically stigmatized. There is no morphological marker distinguishing "core atom" from "extended atom." This creates a **covert morphological class system** that learners cannot predict.

**Example:**
- `dog` (position 23) = atom — no question
- `hors` (position 89) = atom — reasonable
- `pengwin` (position 153, if ceiling = 150) = must be compound `ais-bird`

Why is `hors` atomic but `pengwin` compound? Not for phonological or semantic reasons — purely because of an arbitrary count. This **undermines morphological transparency**.

---

## 2. PROPOSED ALTERNATIVES

### Option A: Soft Ceiling at 200 with Quality Gate as Filter (RECOMMENDED)

**Structure:**
- Tier 0: 50 primitives (closed class — pronouns, numbers, core verbs)
- Tier 1: 150 high-frequency atoms (Swadesh + domestic vocabulary)
- Tier 2: ~50 "soft atoms" — concepts that fail the Quality Gate as compounds
- Tier 3+: All compounds

**Morphological justification:**
- The first 200 atoms cover ALL semantic domains without forcing bad compounds
- The Quality Gate remains the active filter: if a concept CAN be expressed as a clean 2-root compound, it SHOULD be
- The ceiling is soft because the real constraint is morphological quality, not a number

### Option B: Hard Ceiling at 200 with Exception Protocol

**Structure:**
- Hard limit: 200 atoms maximum
- Exception protocol: Any word beyond 200 requires unanimous committee approval
- Exception criteria: Must fail ALL 4 Quality Gate tests AND be in the top 500 most needed concepts

**Advantage:** Strict control prevents "Esperanto creep."
**Disadvantage:** Bureaucratic overhead for every new atom. VELA should be simple, not bureaucratic.

I recommend **Option A** (soft ceiling) because morphological systems should be quality-driven, not number-driven.

---

## 3. JUSTIFICATION

### Japanese: The Compound Over Complex Principle

Japanese demonstrates the 200-atom sweet spot:
- **Yamato kotoba** (native Japanese roots): ~200-250 cover basic vocabulary
- **Kango** (Chinese loans): ~1,000+ for abstract/technical concepts
- **Gairaigo** (European loans): hundreds for modern technology

Japanese compounding (`jukugo`) works because the core atom pool is large enough that compounds rarely exceed 2 roots. VELA should emulate this: ~200 atoms + productive compounding.

### Esperanto: The Cautionary Tale

Esperanto's ~900 roots with affixes create a derivational system that **works** but is **opaque** to non-European learners. VELA's smaller atom pool (~200) + stricter compounding rules = better accessibility.

### Tok Pisin: The Lower Bound

Tok Pisin (~120 core words) proves that extreme minimalism is functional but **restricted in register**. VELA aims for broader expressive range. 200 atoms hits the balance.

---

## Convergence Note

My position (~200 soft ceiling) aligns closely with:
- **Lexicographer** (200 hard ceiling)
- **Phonologist** (~220 soft ceiling)

I diverge from:
- **Aestheticist** (250 soft ceiling) — I agree that poetic register needs atoms, but 200 covers the Swadesh + domestic core. The additional 50 aestheticist atoms may be unnecessary if compounds pass the Gate.

**The 200-atom range represents the morphological consensus.**
