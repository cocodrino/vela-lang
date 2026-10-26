# R21 — Morphologist ruling
**Date:** 2026-10-26 · Claude subagent, read-only · **FINAL VOTE: Q1=B (-eda), Q2=B**

**Dossier corrections (verified):** the validator strips `-ed` by design (`validate_phonology.py:33-37`: "the suffix's own coda is canonical"), not by accident. §3.2 calls other codas "deprecated / SHOULD avoid" rather than forbidding them outright; the hard contradiction is with R19 (free words take the citation form), since `mak-ed` is a free word ending in /d/. R8 (`fase5_consensus.md:160`) ratified `es` as the "única excepción", so Q2-B must explicitly supersede it. `GRAMMAR_COMPLETE.md:498` marks `Mi es-wil hapi` as ❌; `wil es` appears 8 times; history row :1169 is stale. Side finding: `nof` row still in `LEXICON_BASE.md:220` although R20 renamed it.

**Q1 = B, `-eda` /e.da/.** R19 applied to the suffix: free word ending in a hard coda takes `-a`. Vowel-initial, so R8 resyllabification is unchanged: `mak-eda` /ma.ke.da/, `hav-eda`, `si-eda`, `es-eda`. Migration is one regex. Rejects `-de` (= pronoun `de` "they") and `-di` (near `de`/`dis`, internal clusters). Risks: root+eda resembling `-eda` headwords (`deda`, `neda`…; none reproduced); validator must list `eda` before `a`; `liv-ed-an` needs handling.

**Q2 = B.** `es` is already regular (`LEXICON_BASE.md:219`); retire `bi`. Paradigm `es / es-eda / es-wil`. `bi` has no compounds. Q2-B guarantees zero irregular verbs, not zero exceptions overall (modals, suppletive phrases at GRAMMAR:1099 unchecked).
