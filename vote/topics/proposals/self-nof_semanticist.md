# Semanticist Review: self-nof

## Verdict
MODIFY

## Confidence
High

---

## Compositionality Assessment

The compound `self-nof` decomposes into:

- **self** /self/ — reflexive pronoun ("oneself"), type ⟨e, t⟩ modifier in compounds
- **nof** /nof/ — verb "to know" (propositional knowledge: nof(P)), type ⟨e, ⟨s, t⟩⟩

**Literal compositional meaning:** λx. know(x, x) — "to know oneself" → nominalized: "self-knowledge" (the act or capacity of knowing oneself).

The proposal maps this to **"consciousness"** — the state/quality of being aware of one's own existence.

### The Metonymic Gap

`self-nof` composes as an **eventive/processual** concept: the act of knowing oneself. "Consciousness" is a **stative** concept: the baseline state of being aware. The extension requires two metonymic shifts:

1. **Act → Capacity**: from "the act of knowing oneself" to "the capacity for self-knowing"
2. **Specific → General**: from "self-directed knowledge" to "general awareness of existence"

These shifts are cognitively motivated (self-awareness is the hallmark of consciousness in philosophy, psychology, and neuroscience — Descartes' *cogito*, Locke's *self-reflective consciousness*, modern PFC theories). **However**, for a language whose design philosophy prioritizes *transparency* and *no hidden semantic leaps*, the gap between literal composition and intended meaning is too large to be recoverable without explicit instruction.

**Contrast with transparent compounds already in VELA:**
- `lern-hous` = "learn-house" → "school" (zero metonymy: a school IS literally a house for learning)
- `fol-fors` = "fall-force" → "gravity" (zero metonymy: gravity IS the force that makes things fall)
- `sik-fix-po` = "sick-fix-person" → "doctor" (zero metonymy: a doctor IS literally a person who fixes the sick)

**`self-nof` for "consciousness" would be the first compound requiring a non-literal reading.**

**Verdict on compositionality:** The compound is valid *syntactically* (root + root), but its compositional semantics do not transparently deliver "consciousness." The metonymic leap is too large for VELA's design constraints.

---

## Polysemy Risk Analysis

### Risk: HIGH ⚠️

`self-nof` would be systematically ambiguous between at least **three** readings:

| Reading | Gloss | Semantic Type | Context Example |
|---------|-------|---------------|-----------------|
| **R1: Self-knowledge (acquired)** | "knowing one's own character, motives, etc." | eventive/knowledge-state | `Mi hav gud self-nof.` → "I have good self-knowledge." |
| **R2: Self-awareness (capacity)** | "the ability to reflect on oneself" | capacity | `La child develop self-nof at age 2.` → "The child develops self-awareness at age 2." |
| **R3: Consciousness (state)** | "the state of being aware of one's existence" | stative | `La self-nof es wat mak wi man.` → "Consciousness is what makes us human." |

**Evidence that these are distinct concepts:**
- R1 (self-knowledge) can be improved through therapy/reflection; R3 (consciousness) is lost under anesthesia
- R2 (self-awareness) is a developmental milestone; R3 (consciousness) is more fundamental
- In English, "self-knowledge", "self-awareness", and "consciousness" are distinct lexical items

### The `nof-nes` Problem

VELA already has `nof-nes` = "knowledge" (know + -ness). This creates an asymmetry:

- `nof-nes` = quality of knowing → **knowledge** (transparent, zero ambiguity)
- `self-nof` = self + know → **consciousness** (opaque, three-way ambiguity)

A learner seeing `self-nof` after learning `nof-nes` would *expect* `self-nof` to mean "self-knowledge" (the knowledge of oneself), parallel to `nof-nes` = "knowledge." The proposal subverts this expectation.

If `self-nof` = "consciousness," then what compound means "self-knowledge"? The lexicon would have a gap *created* by the very word meant to fill a gap.

---

## Type Consistency Check

### Syntactic Type

`self-nof` is root + root → noun. This follows VELA's established compound pattern (cf. `lern-hous`, `fol-fors`, `brain-net`). Syntactically consistent: ✅

### Semantic Type

| Expression | Semantic Type | Expected | Match? |
|-----------|---------------|----------|--------|
| `self-nof` (proposed) | ⟨e⟩ — abstract noun: consciousness | ⟨e⟩ noun | ✅ |
| `nof` (verb) | ⟨e, ⟨s, t⟩⟩ — event predicate | N/A | — |
| `nof-nes` (knowledge) | ⟨e⟩ — abstract noun: knowledge | ⟨e⟩ noun | ✅ |
| `self` (reflexive) | ⟨⟨e, t⟩, ⟨e, t⟩⟩ — modifier | N/A | — |

The resulting type ⟨e⟩ is correct for a noun. **However**, the internal semantics of VELA root-root compounds typically produce a *transparent hyponym relation*:

- `lern-hous` ⊆ `hous` (a school IS a house)
- `fol-fors` ⊆ `fors` (gravity IS a force)
- `self-nof` ⊈ `nof-nes` (consciousness is NOT a subtype of knowledge)

This violates the internal semantic pattern. `self-nof` as "consciousness" would be the first compound where the head (`nof`) is not the hypernym of the result. "Consciousness" is not "a kind of knowing."

### Comparison with Other Abstract Nouns

| Abstract Noun | Formation | Transparency |
|--------------|-----------|---------------|
| `tru-nes` | true + -ness | "truth-ness" = truth (transparent, zero ambiguity) |
| `nof-nes` | know + -ness | "know-ness" = knowledge (transparent, zero ambiguity) |
| `fri-dom` | free + -dom | "free-dom" = freedom (transparent, zero ambiguity) |
| `self-nof` (proposed) | self + know | ??? → consciousness (opaque, triple ambiguity) |

The abstract noun system currently has perfect compositional transparency. `self-nof` would break this pattern.

---

## Distinctness from `mind`

### Current Lexicon State

`mind` / `maind` = /maind/ — "mind" (cognitive faculty; seat of thought/cognition). Confirmed in LEXICON_BASE.md at two locations (lines 1230, 1261). Also `mini` /mi.ni/ appears at line 1515 — a possible variant or error that needs cleanup, but not relevant to this analysis.

Also relevant:
- `brain` /brein/ — physical organ
- `tot` /tot/ — thought (mental content)
- `soul` /soul/ — soul (metaphysical/spiritual)

### Semantic Boundary: `mind` vs. proposed `self-nof`

| Concept | VELA | Semantic Domain | Key Property |
|---------|------|-----------------|--------------|
| Mind | `mind` / `maind` | cognitive faculty | the *seat* of thought — what thinks |
| Brain | `brain` | physical organ | the *hardware* — the biological substrate |
| Thought | `tot` | mental content | the *product* — what is thought |
| Consciousness (proposed) | `self-nof` | state/quality | the *awareness* — that it is like something to be |

These four concepts are **clearly distinct** and should all exist in VELA. The distinction maps onto well-established philosophical categories:

- **Mind** = cognitive faculty (the processor)
- **Brain** = physical organ (the hardware)
- **Thought** = mental content (the output)
- **Consciousness** = phenomenal awareness (the "what it's like")

**Verdict:** `self-nof` (or whatever word we use for "consciousness") is sufficiently distinct from `mind` to coexist. The question is only *what form* the word should take.

---

## Problems Identified

### Problem 1: Metonymic Leap Violates Transparency Principle

`self + nof` literally composes to "self-knowledge" (eventive/acquired). The extension to "consciousness" (stative/baseline) requires two metonymic shifts (act→capacity, specific→general) that are not recoverable from the morphemes alone. VELA compounds have thus far maintained zero-metonymy transparency.

**Severity:** HIGH — fundamental design principle violation.

### Problem 2: Systematic Polysemy

Without explicit disambiguation, `self-nof` would carry three distinct readings: self-knowledge, self-awareness, and consciousness. VELA's monosemy preference explicitly rejects this kind of overloading.

**Severity:** HIGH — creates ambiguity where the lexicon should provide precision.

### Problem 3: Broken Parallel with `nof-nes`

`nof-nes` = "know-ness" → "knowledge" (transparent). A learner encountering `self-nof` would expect it to mean "self-knowledge" (the knowledge of oneself), following the compositional logic. The proposal gives it a different (and broader) meaning, creating an inconsistent pattern.

**Severity:** MEDIUM — teachability/learnability concern.

### Problem 4: Type Hierarchy Violation

All existing VELA root-root compounds produce hyponyms of the head: `lern-hous` is a type of house, `fol-fors` is a type of force. `self-nof` as "consciousness" would NOT be a type of knowing — consciousness is a state, not a knowledge type. This breaks the internal semantic type pattern.

**Severity:** MEDIUM — systematic inconsistency.

### Problem 5: Gap Creation

If `self-nof` = "consciousness," then what compound expresses "self-knowledge"? The proposal would create a lexical gap where one didn't need to exist, because the most natural formation for "self-knowledge" has been repurposed for a broader concept.

**Severity:** MEDIUM — forces awkward workarounds for a common concept.

---

## Proposed Alternatives

### Primary Recommendation: Split the Concepts

**Keep `self-nof` for "self-knowledge"** (its literal, compositionally transparent meaning).

**For "consciousness,"** propose one of the following — ranked by preference:

#### Option A: `mind-wauk` (mind + awake) — RECOMMENDED ✅

| Component | Meaning | Type |
|-----------|---------|------|
| `mind` | cognitive faculty | noun (existing) |
| `wauk` | awake/alert (existing in `wauk` or can be adapted) | state |
| `mind-wauk` | "mind-awake" → consciousness | compound noun |

**Justification:**
- Transparent: consciousness IS the mind being awake/alert
- Zero metonymy: follows `fol-fors` pattern
- Uses existing roots (`mind` confirmed, `wauk` = "awake" — needs formal entry or adaptation)
- Distinct from `self-nof` = self-knowledge
- Natural opposition: `mind-wauk` vs. `mind-slip` (unconsciousness)

**If `wauk` is not available,** adapt as:
- `mind-wek` — using `wek` (to wake up, existing as verb: "Mi wek at six")
- `mind-wei` — mind + wei? Too abstract

#### Option B: `mind-self-nof` (mind + self + know)

**Justification:**
- "Mind's self-knowledge" = the mind knowing itself = consciousness
- Three-root compound — at the edge of VELA's length limit but acceptable
- Explicitly ties consciousness to the mind's self-reflexive capacity
- Leaves `self-nof` free for "self-knowledge"

#### Option C: Atomic Loan `konshusnes`

**Justification:**
- Zero ambiguity, instant recognition
- International (Latin *conscientia* > English *consciousness*, Spanish *consciencia*, French *conscience*, German *Bewusstsein* [calque], Russian *сознание* [soznanie, calque])
- Violates atom ceiling but consciousness is a sufficiently fundamental concept to justify it

**Drawback:** VELA prefers compounds over loans when possible.

### If Committee Insists on `self-nof` for Consciousness

If the committee votes to keep `self-nof` = "consciousness" despite the risks, I recommend:

1. **Define `self-nof-data`** for "self-knowledge" (acquired knowledge about oneself): `self-nof` + `data` — "consciousness-data" → "what consciousness has learned about itself"
2. **Define `deep-self-nof`** for "introspection" (the act of examining one's own consciousness)
3. **Document the metonymic extension explicitly** in the lexicon entry with a usage note

This would resolve some of the ambiguity at the cost of longer compounds for the derived concepts. **Not ideal but workable.**

---

## Rationale Summary

`self-nof` is a **syntactically valid** VELA compound (root + root → noun) with a **semantically motivated** target (consciousness as self-awareness). The connection is philosophically defensible — self-reflexive awareness is the core of consciousness in both Western and Eastern traditions.

**However**, the proposal fails three of VELA's four semantic principles:

1. **Compositionality**: The literal meaning ("self-knowledge") does not transparently yield the target meaning ("consciousness"). The metonymic gap is larger than any existing VELA compound requires.

2. **Monosemy**: The resulting word would carry at least three distinct readings (self-knowledge, self-awareness, consciousness), violating the one-morpheme-one-meaning preference.

3. **Type consistency**: The compound breaks VELA's internal pattern of root-root compounds producing hyponyms of the head noun. Consciousness is not a type of knowing.

**Strongest recommendation:** Use `self-nof` = "self-knowledge" (literal, transparent) and form "consciousness" via `mind-wek` (mind + awake, pending `wek` formalization), `mind-self-nof`, or the atomic `konshusnes` as fallback.

**Weakest acceptable alternative:** Keep `self-nof` = "consciousness" with explicit documentation and compensating compounds for derived concepts.
