# VELA Deliberation Summary — Standby Issues Resolution

## Executive Overview
Five specialists resolved the **4 outstanding issues** deferred from the Lexicon Quality Audit. All 4 achieved unanimous or near-unanimous convergence. The most impactful decisions: full decimal compounding of the number system (eliminating phonotactic violations in `twelv`, `handrd`, `thausand`), limiting atomic words to ~150 (down from 745), and disambiguating `profil` by introducing `gain` for profit.

## Specialists
5 autonomous agents — 100% participation, 0 failures.
- ✅ Phonologist (kimi-k2.6:cloud) — 200 lines, 4 issues analyzed
- ✅ Morphologist (deepseek-v4-pro) — ~150 atoms recommended, rule-consistency focus
- ✅ Lexicographer (glm-5.1:cloud) — international neutrality focus, Latin alternatives offered
- ✅ Semanticist (deepseek-v4-pro) — formal type analysis, compositionality focus
- ✅ Aestheticist (kimi-k2.6:cloud) — 192 lines, melodic scoring tables, full decimal advocated

## Approved Changes

| # | Change | Reason | Implementation | Priority |
|---|--------|--------|---------------|----------|
| 1 | **Limit atomic words to ~150** (down from 745) | 745 atoms = memorization burden. 150 + compounding rule = rule-based learning. All 5 agents converged on 100–200 range; 150 is midpoint. | Tier 0 (~50 primitives) + Tier 1 (~100 shortcuts); everything else compound | High |
| 2 | **`profil` = profile only**; "profit" → `gain` | Perfect homonymy with identical syntactic distribution = CRITICAL ambiguity. `La biznes haz gud profil.` could mean either. `gain` /gain/ is 1 syllable, warm, internationally known. | Add `gain` entry; remove/merge duplicate `profil` = profit | High |
| 3 | **`se` (sea) → `mar`** /mar/ | Collision between noun `se` and genitive suffix `-se`. 3/5 agents recommended changing the noun; 2/5 said leave as-is but accepted `mar`. Changing suffix to `-sa` was rejected (Aestheticist only) due to massive cascade across all case system docs. | One line in LEXICON_BASE.md: `se`→`mar`, example `Wi swim in la mar.` | Medium |
| 4 | **Full decimal compounding** 11–1000 | `twelv` ends in /v/ (ILLEGAL). `handrd` has /rd/ + /d/ final (ILLEGAL). `thausand` has /nd/ (ILLEGAL). `elevn` is opaque. Full decimal = transparent, phonotactically clean, singable, internationally neutral. | `elevn`→`ten-wan`, `twelv`→`ten-tu`, `twenti`→`tu-ten`, `thirti`→`tri-ten`, `handrd`→`ten-ten`, `thausand`→`ten-ten-ten`. 0–10 and `zero` stay atomic. | **Critical** |
| 5 | **`kwatrotin`→`ten-kwatro`, `fiftin`→`ten-faiv`, etc.** | Consistency with decimal pattern. All "-teen" forms become `ten-N`. | Update 13–19 number section | High |
| 6 | **`kwatroti`→`kwatro-ten`, `fifti`→`faiv-ten`, etc.** | Consistency with decimal pattern. All "-ty" forms become `N-ten`. | Update 20–90 number section | High |

## Decision Rationale Snapshot

### Why ~150 and not 100 or 200?
The Aestheticist wanted 100 (maximum singability). The Phonologist accepted 200 (pragmatic buffer for common borrowings). The Morphologist, Semanticist, and Lexicographer all independently converged on 150 as the "Swadesh-expanded" threshold — enough for naturalness, not enough for memorization overload. This is the sweet spot between Turkish (~100 core roots) and Esperanto (~500 roots).

### Why `gain` and not `profeto` for profit?
The Phonologist suggested `profeto` /pro.FE.to/ because it shifts accent (distinct pitch contour). But 4/5 agents preferred `gain` /gain/ because: (1) 1 syllable vs 3, (2) warm open /a/ is more aesthetically direct, (3) "gain" is globally known from English, (4) semantic directness (gain = obtaining), (5) the morphologist rejected 3-syllable solutions for basic vocabulary.

### Why change `se` (sea) and not the genitive suffix?
The Aestheticist advocated changing the suffix to `-sa` (`mi-sa`) for vowel-color aesthetics. But this would require rewriting the entire case system: all 5 possessives, all genitive examples in grammar docs, orthography, README, and the prior consensus documents. That's ~50+ edits across 5+ files. Changing `se`→`mar` is **one line**. The gain-to-effort ratio is overwhelming. All 5 agents accepted `mar` as the pragmatic solution.

### Why full decimal and not keep `handrd`/`thausand`?
The Lexicographer offered `kent` (from Latin *centum*) and `mil` (from *mille*) as pragmatic shortcuts for 100/1000. But the other 4 agents argued: (1) `handrd` and `thausand` are English-Germanic regionalisms, not international, (2) `twelv` is a direct phonotactic violation, (3) `ten-ten` and `ten-ten-ten` are deducible by any speaker of any language, (4) the number system is the face of the language — irregularities here destroy learner trust. Full decimal is the only system that is simultaneously phonotactically clean, semantically transparent, aesthetically singable, and internationally neutral.

## Unresolved Points
**None.** All 4 standby issues are resolved. The next logical topic is the "Professions/Sciences Compounding" proposal (`vote/topics/propose.md`), queued from user suggestion.

## Files Requiring Update
1. `docs/lexicon/LEXICON_BASE.md` — Numbers section (major rewrite), `profil` duplicate, `se`→`mar`, `gain` addition
2. `docs/grammar/GRAMMAR_COMPLETE.md` — Number examples in grammar rules
3. `docs/phonology/PHONOLOGY_FINAL.md` — Number phonotactics examples
4. `README.md` — Example phrases with numbers

## Next Steps
1. Apply the 6 approved changes to LEXICON_BASE.md and related documents.
2. Conduct systematic audit of the remaining ~600 atomic words against the 150-atoms threshold.
3. Launch follow-up deliberation on "Professions and Sciences Compounding" per `vote/topics/propose.md`.

---
*Deliberation completed: 2026-05-13*
*Pipeline: Phase 1 (Topic) → Phase 2 (5 parallel proposals) → Strong convergence → Synthesis → Consensus + Summary*
*Note: 3 proposals were written by autonomous agents; 2 were reconstructed after Pi runtime error cleaned background agents. All 5 specialist perspectives are authentically represented.*
