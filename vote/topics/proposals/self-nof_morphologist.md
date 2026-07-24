# Morphologist Review: self-nof

## Verdict
APPROVE — form `self-nof` (hyphenated) is correct.

## Confidence
High

## Compounding Rules Assessment

### The rule and its systematic exception

GRAMMAR_COMPLETE.md §15.1 states: **"Two-root compounds are written together without space or hyphen."** If applied mechanically, this would yield `selfnof`. However, the same section's examples table reveals a systematic, precedent-backed exception:

| Compound | From | Hyphen? |
|----------|------|---------|
| `sunlait` | sun + lait | No |
| `hauskel` | haus + kel | No |
| `strongmind` | strong + mind | No |
| `fainal` | fain + al | No |
| `self-lov` | self + lov | **Yes** |
| `over-hapi` | over + hapi | **Yes** |

The rule in §14.1 confirms this: `self-`, `over-`, `un-`, `re-`, `under-`, `non-`, `semi-`, `super-`, `inter-` are classified as **productive prefixes**, not free-standing roots. All prefix-root compounds across the grammar use hyphens (`un-gud`, `re-kom`, `pre-lern-hous`, `mis-tok`, `under-dev`, `non-topi`, `auto-matik`, `semi-kol`, `super-nais`, `inter-nais`). No counterexample exists.

**The real rule, reconstructed:** root+root compounds fuse without hyphen; prefix+root compounds use hyphen. This is not a bug — it's a morphological distinction preserving parseability. The hyphen signals that the first element is a bound morpheme with a fixed grammatical function, not a free-standing lexical root.

`self-nof` follows this convention exactly: `self-` is a prefix, `nof` is a root → hyphenated.

## Orthography Determination

Three candidates evaluated:

| Form | Verdict | Reason |
|------|---------|--------|
| `selfnof` | ❌ REJECT | Violates prefix-hyphenation convention. Would be anomalous alongside `self-lov`, `over-hapi` |
| `self-nof` | ✅ APPROVE | Consistent with all existing `self-` compounds and prefix rules |
| `self nof` | ❌ REJECT | Two-root compounds must be joined; space implies two separate words |

### The ORTHOGRAPHY.md labeling issue

ORTHOGRAPHY.md §8.3 states "Los prefijos van **sin guión**" (prefixes go without hyphen) but immediately shows hyphenated examples (`un-gud`, `re-maki`, `self-lov`). This is a documentation bug — the label contradicts the examples. The examples are correct and match GRAMMAR_COMPLETE.md. Recommendation: correct the label in ORTHOGRAPHY.md to "Los prefijos se escriben con guión" or similar. This does not affect the `self-nof` decision.

## Morphological Transparency

**Semantic derivation:** `self` (oneself) + `nof` (to know) → "knowing oneself" → by metonymy = "consciousness."

Cross-linguistic attestation:
- German: *Selbstbewusstsein* = *selbst* (self) + *bewusst* (conscious/aware) + *sein* (being) = self-consciousness — a near-exact parallel. German does not hyphenate, but that's a language-internal orthographic choice; the semantic composition is identical in structure.
- English: *self-awareness* — narrower but semantically adjacent, using the same "self + cognitive state" template.
- Turkish (agglutinative): *bilinç* (consciousness) comes from *bil-* (to know) + *-inç* (abstract noun) — the "knowledge → consciousness" metonymy is independently attested.

**Transparency verdict:** The meaning is adequately derivable. A learner who knows `self` and `nof` will recognize the compound and can infer the extended meaning with minimal context. The metonymic leap from "self-knowledge" to "consciousness" is small — consciousness *is* fundamentally self-knowledge in most philosophical traditions (Descartes' *cogito*, Locke's personal identity, Nagel's "what it is like to be").

**Potential narrowness concern:** `self-nof` could theoretically be read as "self-knowledge" (knowing facts about oneself) rather than "consciousness" (the phenomenal state). However, VELA already has `tru-nes` for abstract truth and `fri-chuz` for free will — the system tolerates a degree of semantic extension. Context disambiguates. In philosophical usage, `self-nof` will reliably map to consciousness. If the narrower sense is needed later, a modifier like `self-nof-deep` or a suffix like `self-nof-skap` can clarify.

## Syncretism / Ambiguity Check

| Existing term | Meaning | Overlap risk |
|---------------|---------|--------------|
| `mind` /maind/ | Mind (seat of thought) | None. `mind` = organ/mechanism; `self-nof` = state/phenomenon |
| `self-lov` | Self-love (emotional) | None. `nof` vs. `lov` are distinct roots with no shared semantic space |
| `nof` alone | To know (general) | None. Bare `nof` never means consciousness |

No syncretism found. The `self-` prefix space is currently sparse (only `self-lov` confirmed), so there is ample room for additional reflexive-prefix compounds without collision.

## Problems Identified

1. **ORTHOGRAPHY.md documentation bug** (minor, non-blocking): §8.3 label "sin guión" contradicts the hyphenated examples shown. This is a documentation inconsistency, not a morphological one. The examples (`self-lov`, `un-gud`, etc.) are the ground truth per GRAMMAR_COMPLETE.md. Recommend fixing the label.

2. **Rule statement vs. examples gap** (minor, non-blocking): GRAMMAR_COMPLETE.md §15.1's blanket "without space or hyphen" statement is misleading because it doesn't mention the prefix exception. The examples implicitly document the exception, but a naïve reader applying the stated rule would produce `selflov`, `overhapi`, `ungud` — all wrong per existing convention. Recommend adding a clarifying sentence: "Prefix-root compounds (self-, over-, un-, etc.) are hyphenated."

## Proposed Alternatives

**No alternative needed.** `self-nof` is the correct form under VELA's established prefix-hyphenation convention. The atomic loan `konshusnes` would violate the 200-atom ceiling without sufficient justification — the compound is transparent, short (2 syllables), and semantically derivable. It should not qualify for atom status under the Quality Gate (fails test 4: "not a transparent compound of existing roots").

If the committee later wants a fully unhyphenated compound, the form would be `selfnof` — but this is **not recommended** as it would break consistency with every existing prefix compound in the grammar.

## Rationale Summary

1. VELA has a de facto rule: **prefix-root compounds are hyphenated**. This is the only consistent reading of the full evidence across §§14.1 and 15.1.
2. `self-nof` obeys this convention identically to `self-lov`, `over-hapi`, `un-gud`, and all other prefix compounds.
3. The semantic derivation is transparent and cross-linguistically attested (cf. German *Selbstbewusstsein*).
4. No syncretism with `mind`, `self-lov`, or bare `nof`.
5. The form is phonotactically clean: /self.nof/ with a clear syllable boundary at /f.n/ — the hyphen orthographically reinforces prosodic structure.
6. **Verdict: APPROVE `self-nof` as written.**
