# Topic: Atomic Word Ceiling for VELA

## Scope
Determine the maximum number of atomic (non-compound) words VELA should have, and the criteria for promoting a concept from atom to compound. This is a foundational architectural decision that affects vocabulary growth, learnability, and the compound formation system.

## Background
VELA currently has ~1,100 words. The committee previously established a tiered system:
- Tier 0: ~50 core primitives (pronouns, basic verbs, numbers 0-10)
- Tier 1: ~150 high-frequency atoms (including Tier 0)
- Tier 2: 500+ compounds and derived forms

But the exact ceiling is disputed. Some specialists argue for strict minimalism (~150 total atoms), others for a larger atom pool (~250-300) to avoid ugly compounds for common concepts.

## Source files to analyze
- docs/lexicon/LEXICON_BASE.md (current word count and structure)
- vote/topics/consensus/ATOMS_VS_COMPOUNDS_Q2.md (previous Q2 decision)
- docs/grammar/GRAMMAR_COMPLETE.md (morphological constraints)

## Focus questions
1. What is the optimal atomic word ceiling for VELA? (100? 150? 200? 300?)
2. What criteria should determine whether a new concept gets an atom vs a compound?
3. How does the ceiling affect learnability for beginners vs expressive power for advanced speakers?
4. Should the ceiling be hard (absolute limit) or soft (guideline with exceptions)?

## Constraints
- VELA philosophy: simplicity first
- Compound Quality Gate must be maintained (SHORT, MEANINGFUL, SOUNDS GOOD, NOT INFANTILE)
- Previous decision: descriptive compounds (color+animal) are PROHIBITED
- The ceiling must not make VELA feel "impoverished" for daily conversation

## Graphify context
- Community: "Lexicon & Vocabulary" (check graphify-out/GRAPH_REPORT.md for current stats)
- Cross-links: Lexicon → Grammar → Phonology (phonotactic constraints on word length)
- Key consideration: balance between memorization load and expressive flexibility
