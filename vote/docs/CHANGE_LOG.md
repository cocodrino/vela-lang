# VELA Deliberation Change Log

## 2026-05-13 — System Initialization
- Created 5 specialist agents and 1 orchestrator agent.
- Defined filesystem-based memory architecture.
- Established 6-phase pipeline: Discovery → Discussion Plan → Deliberation → Voting → Consensus → Summary.

---

## 2026-05-13 — Case System Re-evaluation (Completed)
- **Topic**: Re-examination of 2-case system (Genitive -se, Locative -te)
- **Participants**: 4 autonomous agents + 1 manual semanticist voice
  - Phonologist (kimi-k2.6:cloud) — 3 proposals, 2 critical/high
  - Morphologist (deepseek-v4-pro) — 3 proposals, 2 high
  - Lexicographer (glm-5.1:cloud) — 3 proposals, 1 high
  - Aestheticist (kimi-k2.6:cloud) — 3 proposals, 1 critical/2 high
  - Semanticist (qwen2.5-coder) — FAILED ×2; supplemented manually
- **Deliberation mode**: Synthesized consensus from convergent proposals
- **Decisions**: 5 approved changes
  1. Locative -te → -to (vowel differentiation)
  2. Plural+Case order: man-s-se → man-se-s
  3. Eliminate possessive -f forms (unified genitive)
  4. Restrict locative to spatial/temporal (state → bare adjective)
  5. Demonstrative dase → dose (homonymy resolution)
- **Files requiring update**: docs/grammar/03-case-system.md, docs/phonology/PHONOLOGY_FINAL.md, docs/lexicon/LEXICON_BASE.md, README.md


---

## 2026-05-13 — Documentation & Skills Update (System Improvement)
- **Type**: Infrastructure improvement
- **Changes**:
  1. **Graphify integration made mandatory**: All deliberations now require Phase 0 (graphify context extraction)
     - vote/docs/VOTING_PROCESS.md — expanded with Phase 0: Graphify Context Extraction
     - .pi/skills/vela-deliberation/SKILL.md — graphify is now a mandatory step
     - vote/docs/PROCESS.md — every topic must include graphify context
     - vote/templates/graphify_dossier.md — template for extracting graphify insights
  2. **Tool restriction documentation**: Skills updated to explicitly warn about subagent tool restrictions
     - Subagents cannot use Serena tools, native tools, bash, or write
     - Dossier pattern is the only valid approach
  3. **Model change**: Semanticist changed from qwen2.5-coder (failed) to deepseek-v4-pro (tested, reliable)
     - qwen2.5-coder and gpt-5.1 both produce 0 output as subagents
     - deepseek-v4-pro confirmed working with lambda notation output
  4. **Documentation updates**: 
     - docs/grammar/03-case-system.md — applied 5 approved changes from consensus
     - docs/grammar/GRAMMAR_COMPLETE.md — 26 locative references updated (-te → -to)
     - docs/writing/ORTHOGRAPHY.md — 4 locative references updated
     - ROADMAP.md — 5 locative references updated
     - docs/lexicon/LEXICON_BASE.md — possessives unified (mif→mi-se), dase→dose, siti-to
     - README.md — case table updated with -to
  5. **Voting rules documented**: vote/docs/VOTING_PROCESS.md now includes complete voting rules, tie-breaker logic, and special cases

---
---

## 2026-05-13 — Lexicon Quality Audit (Completed)
- **Topic**: VELA Base Lexicon audit — philosophy, pronunciation, compounding
- **Participants**: 5 autonomous agents (all models functional)
  - Phonologist (kimi-k2.6:cloud) — 9 problems, 5 critical
  - Morphologist (deepseek-v4-pro) — 3 problems, 1 critical
  - Lexicographer (glm-5.1:cloud) — 8 problems (5 words + 3 homonymies)
  - Semanticist (deepseek-v4-pro) — 3 problems, 1 critical
  - Aestheticist (kimi-k2.6:cloud) — 3 problems, 1 critical
- **Deliberation mode**: Strong convergence; synthesized directly
- **Decisions**: 15 approved changes
  1. Eliminate adjective suffix -im (unanimous, critical)
  2. envirnmnt → natur
  3. tempratcur → temperaturu
  4. telivizion → far-si
  5. konversashon → kom-tok
  6. bodifikashon → in-bodi
  7. konstitushon → karta
  8. aplikaishon → aplik
  9. stop → topi
  10. draw → rava
  11. build → maki
  12. paint → kolori
  13. fix → repai
  14. Systematic vowel epenthesis for remaining illegal-final words
  15. Homonymy resolution: la(law) → lex; four → kwatro
- **Files requiring update**: docs/lexicon/LEXICON_BASE.md, docs/grammar/GRAMMAR_COMPLETE.md, docs/phonology/PHONOLOGY_FINAL.md, README.md

## New entries append below (orchestrator will add them automatically)


---

## 2026-05-13 — Standby Issues Resolution (Completed)
- **Topic**: 4 deferred issues from Lexicon Quality Audit
- **Participants**: 5 specialists (all models functional)
  - Phonologist (kimi-k2.6:cloud) — 200-line phonotactic analysis
  - Morphologist (deepseek-v4-pro) — 150-atoms threshold
  - Lexicographer (glm-5.1:cloud) — international neutrality focus
  - Semanticist (deepseek-v4-pro) — formal type analysis
  - Aestheticist (kimi-k2.6:cloud) — 192 lines, melodic scoring
- **Deliberation mode**: Strong convergence on 3/4; Issue 3 (SE) required pragmatic tie-break
- **Decisions**: 6 approved changes
  1. Limit atomic words to ~150 (5/5 unanimous)
  2. PROFIL = profile only; profit → gain (5/5 unanimous)
  3. se (sea) → mar; keep -se suffix (5/5 accepted after tie-break)
  4. Full decimal compounding 11–1000 (5/5 unanimous)
  5. All "-teen" → ten-N (consistency)
  6. All "-ty" → N-ten (consistency)
- **Files requiring update**: docs/lexicon/LEXICON_BASE.md, docs/grammar/GRAMMAR_COMPLETE.md, docs/phonology/PHONOLOGY_FINAL.md, README.md

---

## 2026-05-13 — Number System Override + Profession Gender Neutrality (In Progress)
- **Topic**: User-requested corrections to standby consensus
- **Changes applied**:
  1. Numbers 100→kent (Latin centum), 1000→mil (Latin mille) — both atomic
  2. Full decimal compounding 11–99 applied to LEXICON_BASE.md
  3. Removed ten-ten/ten-ten-ten from approved standard
- **User priority**: Gender-inclusivity in professions (rejected -man suffix)
- **Queued**: Profession suffix deliberation (neutral form needed)

---

## 2026-05-13 — Gender Neutral Profession Suffix: -po (User Decision)
- **Topic**: Replace -man with gender-neutral suffix
- **Initial user preference**: -er
- **After deliberation**: User switched to -po (morphological + aesthetic arguments)
- **User override on -ist**: Explicitly rejected. Single suffix only.
- **Decision**: -po as UNIVERSAL profession suffix. No exceptions.
- **Pattern**: [action]-po = profession. Updated in propose.md
  - lern-po, sik-fix-po, food-mak-po, masin-fix-po, law-keep-po, war-fajt-po, sik-help-po, law-speak-po, news-tak-po, rol-play-po, song-mak-po
- **Status**: COMPLETE

---

## 2026-05-14 — Professions Applied to LEXICON_BASE.md (Completed)
- **Action**: Replaced ALL atomic profession entries with compound + -po forms
- **Removed**: tice, student, droctor, lavyr, injinir, artis, muzishn, ritr, bos, workr, biznisman, famer, fisher, kuk (as noun), driver, pilat, sailr, prezidnt, soldier (polis-man also removed)
- **Kept**: doktr (atomic, Latin universal), king, kwain, citizn (titles/status, not professions)
- **Added 23 compound professions**:
  lern-po, stodi-po, sik-fix-po, food-mak-po, plant-grow-po, word-mak-po, biju-mak-po, masin-fix-po, law-keep-po, war-fajt-po, sik-help-po, law-speak-po, news-tak-po, rol-play-po, song-mak-po, muzik-po, kar-po, hed-po, wok-po, fis-kat-po, naid-rul-po, moni-keep-po, fly-po, mar-po
- **Status**: COMPLETE — LEXICON_BASE.md updated

---

## 2026-05-14 — README Updated with Consensus Engine Documentation
- **Action**: Added "The Consensus Engine — How Design Decisions Are Made" section to README.md
- **Content**: 
  - Specialist panel with 5 roles and models
  - 5-phase process (Graphify → Prompt → Deliberation → Consensus → Apply)
  - Voting rules (unanimous fast-track, 4/5, 3/5 tie-breaker)
  - User override policy
  - Complete file structure in vote/ directory
- **Status**: COMPLETE
