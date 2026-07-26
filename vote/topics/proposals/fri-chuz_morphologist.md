# Morphologist Review: fri-chuz

## Verdict
MODIFY

## Confidence
High

---

## Compounding Rules Assessment

### What §15.1 Actually Says

> "Two-root compounds are written **together without space or hyphen**."

The rule is unambiguous. The exception applies to prefix+root compounds (e.g., `self-lov`, `over-hapi`) where `self-` and `over-` are explicitly listed as prefixes in §14.1. For root+root compounds, fusion is mandated.

`fri` is an adjective root ("free"), NOT a prefix. It does not appear in the §14.1 prefix table. `chuz` is a verb root ("to choose"). Therefore `fri-chuz` falls under the **root+root fusion rule**, not the prefix+root hyphen exception.

### Grammar–Lexicon Inconsistency (Systemic)

The grammar rule and actual lexicon practice are in conflict:

| Source | Pattern | Examples |
|--------|---------|---------|
| §15.1 rule text | Root+root = fused | sunlait, hauskel, strongmind, fainal |
| §15.1 examples | Mixed | wotc-man (hyphenated — contradicts rule) |
| LEXICON_BASE.md | Root+root = hyphenated | nau-dei, nof-hu, lern-hous |
| LEXICON_BASE.md | Anomaly: DOT notation | fri.dom (unique — no other dot-compound exists) |
| LEXICON_EXTENDED.md Phase 5 | Universal hyphenation | self-nof, fri-chuz, tru-nes, dep-nof |
| `self-nof` consensus ruling | Prefix+root = hyphen, root+root = fused | Morphologist: "self- is prefix → hyphenated; selfnof would break convention" |

**Finding:** The grammar specification and the baseline lexicon (LEXICON_BASE.md) disagree on compounding orthography. The Phase 5 entries follow the lexicon convention (hyphens everywhere), not the grammar rule (fused for root+root). The `self-nof` committee ruling implicitly affirmed the §15.1 distinction by noting that hyphenation for `self-` is justified *because* it's a prefix, and fusion for non-prefix roots "would break convention."

---

## Orthography Determination

### `fri-chuz` → Should Be `frichuz`

Per §15.1, two root+root compounds are fused:

```
fri (adjective, root) + chuz (verb, root) → frichuz
```

**Typological parallel:** German compounds — *Freiheit* ("freedom"), *Willensfreiheit* ("free will", lit. "will's freedom"). German fuses roots without boundary markers, relying on the learner's knowledge of the root inventory. VELA's small atom set (≤200) makes this feasible: a learner memorizes `fri` and `chuz` as roots, then sees `frichuz` and decomposes it immediately.

**Phonotactic check:** /frai.tʃuz/ — the syllable boundary falls naturally at `/frai.tʃuz/`, matching the morpheme boundary. No ambiguous parsing. No consonant cluster violation. The fusion is phonotactically clean.

### `fri.dom` → Legacy Error, Should Be `fridom`

`fri.dom` is the **only entry in the entire lexicon using DOT notation for a compound.** Dots are used elsewhere in the lexicon only for syllable boundary markers in IPA transcriptions (e.g., `/fri.dom/`). Using `.` as a compound boundary marker has zero precedent in VELA grammar or lexicon.

**Origin hypothesis:** `fri.dom` was likely an early experimental entry that predates the §15 compound rules. The dot may have been intended as a morpheme boundary marker during the exploratory phase, before hyphenation was adopted as the compound convention in LEXICON_BASE.md.

**Correction:** Change to `fridom` (fused, per §15.1) — or `fri-dom` if the committee resolves the systemic hyphenation question in favor of universal hyphenation.

---

## Necessity of Single Compound

### `fri chuz` (two words) vs. `frichuz` (compound)

**Two separate words** (`fri chuz`) would parse as an adjective-noun phrase: "free choice." This denotes a *specific instance* of choosing freely — an event, not a capacity. Example: "Mi meik un fri chuz" = "I make a free choice" (one decision).

**Single compound** (`frichuz`) nominalizes the concept: "free will" as a philosophical capacity. Example: "La frichuz es un filosofik konsept" = "Free will is a philosophical concept."

These are semantically distinct. Two words = concrete event. Compound = abstract capacity. VELA needs the compound for philosophical register, just as English distinguishes "a free choice" (event) from "free will" (capacity), and Spanish distinguishes "una elección libre" from "libre albedrío."

**Conclusion:** A compound is justified and necessary.

---

## Syncretism / Ambiguity Check

### `frichuz` vs. `fridom` (currently `fri.dom`)

| Compound | Composition | Meaning | Semantic Domain |
|----------|-------------|---------|-----------------|
| `fridom` | fri + dom | freedom (state/condition) | Political/social |
| `frichuz` | fri + chuz | free will (capacity/agency) | Philosophical/psychological |

**No syncretism.** These are distinct concepts:
- *Freedom* = absence of constraint, ability to act (external condition)
- *Free will* = capacity to choose independently of determinism (internal agency)

The roots are different (`dom` ≠ `chuz`), the meanings are in different semantic fields, and the formations are phonotactically distinct (`/fri.dom/` vs. `/frai.tʃuz/`). No risk of confusion.

### `frichuz` vs. hypothetical suffix `-wil`

The dossier mentions the alternative `freewil` and flags structural homonymy with suffix `-wil` (future tense). This is a valid concern: `friwil` would parse as `fri + wil` where `wil` could be the future marker. Since `-wil` is a productive verbal suffix (`go-wil` = "will go"), `friwil` would be ambiguous: "will be free" vs. "free will."

`frichuz` avoids this entirely by using the verb root `chuz` instead of the tense suffix `-wil`. Clean disambiguation.

---

## Problems Identified

### P1: Systemic Grammar–Lexicon Inconsistency (CRITICAL)

§15.1 says "no hyphen" for root+root compounds, but LEXICON_BASE.md, LEXICON_EXTENDED.md Phase 5, and even §15.1's own example table (`wotc-man`) use hyphens for root+root compounds. This is not just about `fri-chuz` — it affects the entire compounding system.

**Scope:** At minimum, the following entries need audit:
- LEXICON_BASE.md: `nau-dei`, `nof-hu`, `lern-hous` (and others)
- LEXICON_EXTENDED.md: `tru-nes`, `nof-nes`, `dep-nof`, `fri-chuz`
- GRAMMAR_COMPLETE.md §15.1: `wotc-man` (example contradicts the rule it illustrates)

**Resolution options:**

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A: Enforce §15.1 | Fuse all root+root compounds, hyphen only for prefix+root | Aligns with rule text; less visual clutter for common compounds | Requires mass lexicon edit; reduces explicit morpheme boundary visibility |
| B: Revise §15.1 | Hyphenate ALL compounds (root+root AND prefix+root) | Maximizes morphological transparency; aligns with existing lexicon practice; one consistent rule, no exceptions | Adds one character per compound boundary; visual density for frequent compounds |
| C: Hybrid | Hyphenate only when fusion creates phonotactic ambiguity or consonant cluster, fuse otherwise | German-like pragmatism | Introduces phonologically conditioned allomorphy (violates principle #2); subjective judgment calls |

**Recommendation:** Option B (universal hyphenation). Justification:
1. **One-to-one mapping:** Hyphens make every morpheme boundary explicit, which is the core principle of agglutinative transparency.
2. **No allomorphy:** A single, invariant rule. No exceptions for phonotactic edge cases.
3. **Cognitive load:** The cost is one ASCII character per boundary. The benefit is zero parsing ambiguity. Net positive for a learned language where roots are memorized as a set.
4. **Existing practice:** LEXICON_BASE.md already uses hyphens universally. Revising the grammar rule is cheaper than rewriting the entire lexicon.
5. **Typological precedent:** Esperanto uses hyphens optionally for clarity in compounds (though it also fuses). Hungarian, a highly agglutinative language, uses neither hyphens nor spaces — but Hungarian has vowel harmony as a boundary signal. VELA has no harmonic cues, so explicit boundaries add value.

### P2: `fri.dom` DOT Notation (MODERATE)

`fri.dom` is a unique anomaly. The dot is not used for any other compound in the lexicon. It most likely predates the compound orthography rules and should be corrected to `fridom` (or `fri-dom`, per Option B above).

### P3: `wotc-man` Inconsistency in §15.1 Example Table (MINOR)

The example `wotc-man` (watchman) in §15.1 is hyphenated despite both `wotc` and `man` being roots. This makes the example table contradict the rule text it illustrates. Either the rule or the example needs correction.

---

## Proposed Alternatives

### If MODIFY (current verdict): `fri-chuz` → `frichuz`

Apply §15.1 strictly. Fuse all root+root compounds. Reserve hyphens for prefix+root only.

| Current | Corrected | Reason |
|---------|-----------|--------|
| `fri-chuz` | `frichuz` | Root+root → fused per §15.1 |
| `fri.dom` | `fridom` | Dot notation has no precedent; root+root → fused |
| `nau-dei` | `naudei` | Same rule |
| `dep-nof` | `depnof` | Same rule |
| `tru-nes` | `trunes` | Root+suffix; `-nes` is suffix → may keep hyphen (suffix boundary convention) or fuse |

**Risk:** Massive lexicon churn. Every hyphenated root+root compound in LEXICON_BASE.md and LEXICON_EXTENDED.md must be edited. This is costly but establishes a clean, consistent system.

### If Option B (universal hyphenation) is adopted:

- Keep `fri-chuz` as-is (APPROVE)
- Merge `fri.dom` → `fri-dom`
- Merge all root+root compounds to hyphenated form
- Revise §15.1 text to: "Two-root compounds are written with a hyphen between roots."
- This is the **least disruptive** option — lexicon matches grammar with minimal edits.

---

## Rationale Summary

1. **`fri` is not a prefix.** It's an adjective root. The `self-nof` precedent (prefix+root = hyphen) does NOT apply here. Per §15.1, root+root compounds are fused → `frichuz`.

2. **`fri.dom` uses dot notation**, which has zero precedent in VELA grammar or lexicon. It's a legacy error and should be corrected to `fridom` (or `fri-dom` under Option B).

3. **A single compound is justified.** `fri chuz` (two words) = "free choice" (event). `frichuz` (compound) = "free will" (capacity). Different semantics, different forms.

4. **No syncretism with `fri.dom`.** "Freedom" (state) ≠ "free will" (capacity). Distinct roots, distinct meanings, distinct pronunciations.

5. **Systemic inconsistency detected.** The grammar mandates fusion but the lexicon uses hyphens. This conflict predates `fri-chuz` and affects the entire compounding system. The committee should resolve this at the system level before processing individual Phase 5 compounds. My recommendation: adopt universal hyphenation (Option B) for maximum morphological transparency, then process all compounds uniformly.
