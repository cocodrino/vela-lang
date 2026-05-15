# Voting Results — Etymology Policy

**Date:** 2026-05-14
**Question:** What should be the primary etymological source for VELA vocabulary?

## Final Tally

| Specialist | Model | Vote |
|-----------|-------|------|
| Lexicographer | glm-5.1 | **C — Hybrid** |
| Phonologist | kimi-k2.6 | **C — Hybrid** |
| Semanticist | deepseek-v4 | **C — Hybrid** |
| Aestheticist | kimi-k2.6 | **C — Hybrid** |
| Morphologist | deepseek-v4 | **A — English Only** |

**Result: 4-1 in favor of HYBRID (Option C)**

## Arguments for Hybrid (4 votes)

- **Lexicographer:** "Mirrors how natural languages already work—native Anglo-Saxon words for daily life, Latinate words for formal domains. The split is predictably demarcated by semantic domain (concrete/everyday vs. abstract/formal), giving learners a clear heuristic rather than arbitrary memorization."

- **Phonologist:** "Preserves VELA's existing English-root foundation for everyday vocabulary, which maximizes immediate learnability for the largest population of second-language speakers. Latin/Greek roots for scientific and abstract concepts tap into an already globalized stratum of international vocabulary."

- **Semanticist:** "The everyday-concrete vs. scientific-abstract split is not arbitrary—it reflects a well-attested cognitive distinction. Basic-level categories (dog, water, eat) are acquired early, so English roots preserve warmth and recognizability. Abstract concepts are learned later and already draw heavily from Latin/Greek across languages."

- **Aestheticist:** "Concrete vocabulary tends to carry warmth and cultural grounding, while abstract vocabulary gravitates toward systematic, international roots. English roots preserve emotional immediacy and speaker pleasure. Latin/Greek roots create a beautiful, regular 'upper register' that offers international transparency and elegant derivational morphology."

## Dissenting Argument (1 vote)

- **Morphologist:** "English roots for all words is the only option consistent with VELA's core design principles. A single etymological source eliminates the arbitrary tier-boundary problem—where does 'everyday concrete' end and 'science/abstract' begin? That fuzziness introduces a hidden taxonomy learners must memorize, violating both simplicity and logical transparency. Consistency—one source, one rule, no exceptions—is the most beautiful morphological architecture a constructed language can have."

## Decision

The hybrid approach (Option C) is approved by majority vote (4-1). The morphologist's concern about boundary fuzziness is noted and will be addressed by establishing a clear semantic criterion:

**Rule:** If a concept refers to a physical, tangible, directly experienceable entity (animal, body part, tool, food, clothing, natural substance), use English roots. If a concept refers to an abstract, formal, scientific, or institutional entity (justice, economy, system, tradition, culture), use Latin/Greek roots.

Ambiguous cases (e.g., animals) default to English unless the animal name is already international (elephant, giraffe, zebra remain as-is since they're internationally recognizable).

## Applied Examples

| English | Tier | Source | VELA Form |
|---------|------|--------|-----------|
| dog | Everyday | English | dog |
| cat | Everyday | English | kat |
| water | Everyday | English | water |
| justice | Abstract | Latin | justiso |
| culture | Abstract | Latin | kulturo |
| economy | Abstract | Latin/Greek | ekonomi |
| lion | Animal | English | laigon / leono |
| elephant | Animal (international) | Latin | elefanto |
| hospital | Institution | Compound | sik-hous |
| system | Abstract | Latin | sistemo |

## Files Affected
- docs/lexicon/LEXICON_BASE.md — etymology annotations added
- vote/docs/CHANGE_LOG.md — etymology policy entry
