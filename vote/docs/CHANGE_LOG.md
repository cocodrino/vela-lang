# VELA Deliberation Change Log

## 2026-07-25 — Phoneme Decision: admit /tʃ/ (ch) and /dʒ/ (j)

Systemic question raised during batch 3. **5-specialist committee voted UNANIMOUS to ADMIT** /tʃ/ and /dʒ/ as consonants #19-20 (inventory 18→20). Rationale: ~74 words already use them (chipa, teach, child, jara, oranja, jen); mapping them out would cause fatal collisions (chip→ship, jen→zen, chin→shin) + a 74-word migration; they are among the world's most common consonants (Universality). Zero word changes — only PHONOLOGY_FINAL.md §1 amended. This unblocks ch/j freely in future vocabulary.


## 2026-07-25 — Expansion Batch 3: Body & Health (+33)

Committee-reviewed (3 specialists), synthesized with verification. Dropped `breta`/`resta`/`healti` (existing `brit`/`rest`/`helti`); `kut-kur→sik-kur` (kut not in base); `chesta→hert-hous`. Kept `blud-lain`/`hert-bit` (verified `lain`/`bit` exist, against stale review claims). Gold-standard series: `big-fingar`=thumb, `fut-fingar`=toe, `blud-lain`=vein, `hot-sik`=fever, `hed-pain`=headache.

**Systemic flag raised (morphologist, twice): /tʃ/ "ch" and /dʒ/ "j" are NOT in the 17-consonant inventory** (PHONOLOGY_FINAL §1). Yet ~19 `ch`-words and many `j`-words exist (jen, imaj, jara, oranja, chip…). Deferred `chin`/`chesta` pending a dedicated committee decision on whether VELA admits /tʃ/,/dʒ/ or maps them (e.g. ch→sh/ts, j→y/zh). **Dictionary 1444 → 1477, 0 duplicates, validator 0 errors.** Progress: **1477 / 3000**.



## 2026-07-25 — Expansion Batch 2: Home & Daily Life (+48)

Same author-generates/committee-reviews pipeline. Improved prompts from batch-1 lessons: told the morphologist to verify every "X exists" claim, told the semanticist to use real/legal roots. All 3 specialists reviewed.

- **Synthesis with verification** — confirmed `wash→wosh`, `kold→kol` (cleaner cold root), and dropped `keki`/`chizi` (existing `keik`/`ces`). Applied `string→stringa`, `metal-string→metal-stringa` (both specialists: /ŋ/ is not in the legal coda set {n,m,l,r,s}). Rejected the phonologist's "ropi is a duplicate" (verified: `ropi` does not exist — kept). Kept clean loans the majority approved over the semanticist's compound suggestions (a candle can stay `kandel`).
- Highlights: transparent compounds `kol-boksi`=fridge, `si-glasi`=mirror, `slip-kover`=blanket, `frute-watre`=juice, `arm-kover`=sleeve.
- Result: 48 words added. **Dictionary 1396 → 1444 entries, 0 duplicates, validator 0 errors.**

Progress: **1444 / 3000**. (Systemic questions flagged for later: is /tʃ/ "ch" in the inventory? `kol`/`kold`, `lon`/`long`, `frukt`/`frute` near-duplicates.)



## 2026-07-25 — Expansion Batch 1: Nature & Environment (+51)

First vocabulary-expansion batch under the "author generates, committee reviews" model. Claude authored ~54 words → validator pre-filter → 3 Pi specialists reviewed (each read the repo first): semanticist (transparency), phonologist+aestheticist (sound/beauty), morphologist+lexicographer (structure/consistency).

- **Synthesis with verification** — several morphologist fixes were stale/wrong and rejected after checking the actual lexicon (claimed `river`→`rivr` but we'd just fixed that; claimed `ais`/`daun` missing but they exist). Phonologist's `-lond → -londa` fixes were rejected as contradicting the ratified Option A (native roots grandfathered in compounds).
- **Applied consensus** — `watre-lond → mar-lond` (island, not "wetland"); `morn → moring`; `jema → biju-ston` (transparent); dropped season compounds (samr/winter/spring/fol already exist) and `sanda`/`beri` (duplicates); backfilled gap roots `tre, lo, lain, rais`.
- Result: `docs/lexicon/LEXICON_EXPANSION.md` (51 words), added to the validator + dictionary pipeline. **Dictionary 1345 → 1396 entries, 0 duplicates, validator 0 errors.**

Progress: **1396 / 3000**.



## 2026-07-25 — Lexicon Cleanup (pre-expansion)

Surfaced by `generate_dictionary.py`, applied via `scripts/clean_lexicon.py` (idempotent) + manual fixes. Verified: dictionary regenerated with **0 duplicate headwords**, phonotactic validator still **0 errors**.

- **De-dotted 29 headwords** — the syllable dot belongs in the AFI only: `lai.on → laion`, `dol.fin → dolfin`, `e.le.fant → elefant`, etc. (AFI keeps its dots).
- **Removed ~99 duplicate rows** — same headword listed in multiple thematic sections (all intra-file; kept the first occurrence).
- **Resolved homonyms:** `dai` (die/duck) → duck is now `duk`; `lai` (lie/luck) → luck is now `luki`. The basic verbs keep the short form.
- **Merged spelling variant:** removed `mind` (pronounced /maind/ — violated write-as-you-speak); `maind` is canonical.
- **Flagged, not changed:** `mini` /mi.ni/ glossed "mind" looks like a mis-gloss (should likely be "mini/small") — needs review.
- **Pronounceability pass (`scripts/fix_pronounceability.py`)** — 54 words dropped the English schwa entirely, leaving an unreadable obstruent+sonorant cluster (`rivr`, `botl`, `opn`, `sevn`, `ppl`, `gvrnmnt`, months `Septembr`…). Restored the pure vowel so they read as they sound: `rivr→river`, `nevr→never`, `opn→open`, `sevn→seven`, `ppl→pipel`, `letr→leter`, `Septembr→September`, `watrmeln→watre-melon`, etc. (177 replacements across lexicons + corpus). This fixes a triple violation: write-as-you-speak, the schwa→pure-vowel rule, and (C)V.

Lexicon now: **1345 unique entries**, clean and pronounceable — base for vocabulary expansion.



## 2026-07-24 — Fase 7: Diccionario

**Deliverable:** `docs/dictionary/DICTIONARY.md` (1446 entries) + `docs/dictionary/INDEX_EN_VELA.md` (English→VELA reverse index), generated by `scripts/generate_dictionary.py`.

- Built entirely from existing lexicons (LEXICON_BASE + LEXICON_EXTENDED) — **no new vocabulary**. Reformats, merges, sorts, and auto-derives etymology (`god-hous` → "god + house") and the compounds-per-root list (`hous` → sik-hous, god-hous, lern-hous...).
- Parser is **header-aware** — the lexicons use ~13 different table column layouts; it maps columns by header name, persists headers across mid-table prose/blank lines, splits the "two-entries-per-row" layout, and falls back to a positional default. Skips non-entry rows (design-note tables) via a bold-headword guard.
- **Audit findings** (surfaced by generation, for a future lexicon cleanup): 85 duplicate headwords (e.g. far-si, fon, foto, dep); several entries carry a syllable dot in the headword (`lai.on`, `fri.dom`, `dol.fin`) which belongs in the AFI only.

### Open (lexicon cleanup candidates)
- 85 duplicate headwords + dotted headwords → normalize in a lexicon pass. Also the earlier `maind`/`mind` duplicate.

---

## 2026-07-24 — Fase 6: Gramática de Referencia

**Deliverable:** `docs/grammar/GRAMMAR_COMPLETE.md` polished to an 18-section reference manual.

- Added §17 **FAQ** (10 common questions) and §18 **Exceptions & Closed Classes** (closed-class function words, suppletive comparisons, atomic exceptions) — TOC updated.
- **Compound orthography decision (committee):** the owner proposed dropping the hyphen for elegance; both specialists voted **KEEP THE HYPHEN** unanimously. Aestheticist: "the hyphen IS the elegance" for short-root VELA (`sik-hous` = haiku, `sikhous` = barcode). Morphologist: without it, `liv-ed`/`li-ved`, `man-se`/`ma-nse` are ambiguous; transparency ranks above beauty in VELA's principles. §15.1 fixed to match `ORTHOGRAPHY.md` §6.3 (hyphen between all morphemes).
- Updated §15.0 atomic ceiling to the two-tier model (Fase 5 R1).
- Canon reconciliation carried from the Fase 5 work: plural `-n/-en`, morpheme order root-number-case, locative `-to`, comparative `mor/mos + base`.

### Open (lexicon, not grammar)
- Duplicate `maind`/`mind` (both = mind) — dedup candidate, like the `mont`/`munts` merge.

---

## 2026-07-24 — Fase 5: Full Lexicon Review (23 domains, ~246 words)

**Committee:** 5 specialist roles across 3 Pi agents (distinct models) over the NATS bridge, 2 rounds.
**Method:** Domain-level review → consensus ballot (APPROVE/AMEND/REJECT per resolution).
**Result:** ✅ RATIFIED — see `vote/topics/consensus/fase5_consensus.md`.

### Resolutions adopted
| # | Decision | Vote |
|---|----------|------|
| R1 | **Two-tier atom ceiling** — soft ~200 core target + open domain registers; every loan carries a ≤3-root compound alternative | APPROVE ×2, AMEND ×1 |
| R2 | **Thematic vowel /a/** for illegal single codas (~115 words) + **banned final clusters** (~32 words restructured); grandfathered roots `fors/art/self/god → forsa/arta/sela/goda` (2-release window) | unanimous |
| R3 | **Loan reduction** in Ethics/Politics/Arts — `moral→rait-rong-sistam`, `etik→rait-rong-lern`, `harm→bada-mak`, `responsibil→du-nob`, `parlamnt→rul-mak-hous`; loans kept as domain-register synonyms | APPROVE ×2, AMEND ×1 |
| R4 | **Emotion clusters kept** (gold standard); POETIC/PROSE tag adopted; clinical forms get poetic synonyms, not replacement | unanimous |
| R5 | `pilgrimage→pilgrimej`; `-shon` standardized; beauty swaps `tretmnt→kura`, `govrnr→rul-po`, `varibl→chanj-tip`, `vershn→edi-shon`, `ekshibishon→shou-hous` | unanimous |
| R6 | **Plural canon fixed** — `-n`/`-en` is the single rule (all `-s` deleted); morpheme order **root→number→case** (`man-en-se`); `man-se-n` removed | unanimous |

### Follow-up review (same day)
- **Homonymies — resolved, no action.** `fors→forsa`, `spid→spida`, `bit`→`muzika-bita` already eliminated the real clashes; `masa`≠`mas` (not homonyms); `stap`≠`stop` (`topi`); `tip` = benign polysemy. Only `kor` (choir) is a **reserved form** — latent risk if `core` is added later.
- **Locative `-te`/`-to` — FIXED.** Finished applying the prior consensus (`-to`) across GRAMMAR_COMPLETE.md (rules, AFI, paradigm, summary). Also fixed a stale `mor/mos + im` comparison line (`-im` was already eliminated).

- **Phonotactic validator built** — `scripts/validate_phonology.py` (from PHONOLOGY_FINAL.md §3.2). It exposed that R2's thematic vowel clashed with compounding from consonant-final native roots. **Both specialists voted Option A:** thematic vowel for loans/new roots only; native roots grandfathered in compounds (legal inventory = BASE headwords + errata roots); diphthong `-y/-w` endings are vowel-final. Fixed 6 new coinages (`chanja-tip`, `du-noba`, `kolaja`, `pilgrimeja`, `paraiza`; `deploy` kept). LEXICON_EXTENDED.md now validates 0 errors.

- **`th` = /θ ð/ nativization DONE** — 9 legacy words fixed with `/θ/→/t/`, `/ð/→/d/` (the convention already in their own AFI): `think→tink, thick→tik, thin→tin, smooth→smud, helthi→helti, month→mont, lethr→leder, theory→teori, throu→trou`. `trou` keeps `/ou/` to avoid clashing with `tru` (true); `zh` rejected (spells /ʒ/, also not in inventory). Corpus swept. Validator: 0 errors / 1439 words.

- **Duplicate `month` merged** — removed `munts` (worse phonotactically, ends in /nts/ cluster); `mont` is canonical. Plural is `mont-en` (fixed `yeer` example: "ten-tu mont-en" = twelve months).

### Carried forward
- Poet-vocabulary gap (sensory/atmosphere atoms) → Fase 6.

### Files changed
- `docs/lexicon/LEXICON_EXTENDED.md` — word forms, AFI, examples, plurals
- `docs/grammar/GRAMMAR_COMPLETE.md` — §4.9 morpheme order + plural summary
- `ROADMAP.md` — Fase 5 status + plural note
- `vote/topics/consensus/fase5_consensus.md` — new

---

## 2026-05-31 — Phase 5: Single Word Review (self-nof = consciousness)

**Committee:** 5 specialists (Phonologist, Morphologist, Lexicographer, Semanticist, Aestheticist)
**Word reviewed:** `self-nof` (self + nof) = consciousness / consciencia
**Domain:** Philosophy / Core Concepts

### Deliberation Summary
| Specialist | Verdict | Confidence |
|------------|---------|------------|
| Phonologist | ✅ APPROVE | High |
| Morphologist | ✅ APPROVE | High |
| Lexicographer | ✅ APPROVE | Med-High |
| Semanticist | ⚠️ MODIFY | High |
| Aestheticist | ✅ APPROVE | Med-High |

**Result:** APPROVED (4/5, 1 modify with alternative proposal)

### Decision
- **Approved:** `self-nof` = consciousness / consciencia
- **AFI:** /self.nof/
- **Formation:** prefix compound (`self-` + `nof`)
- **Orthography:** hyphenated (`self-nof`) — `self-` is prefix, not root
- **Register:** philosophical consciousness (self-awareness of existence)

### Semanticist Dissent (archived)
- Proposed: `self-nof` = "self-knowledge" (literal), `mind-wek` = "consciousness"
- Preserved for future review if polysemy issues arise in usage

### Files Updated
- `vote/topics/consensus/self-nof_consensus.md` — full rationale and dissent
- `vote/topics/proposals/self-nof_*.md` — per-specialist reviews (5 files)

---

| 2026-05-31 | `fri-chuz` = free will | APPROVED (4/5, 1 modify) | Compound of existing roots; phonotactically clean; semantically one of strongest in Phase 5; hyphenated form chosen for consistency with entire existing lexicon; morphologist orthography dissent noted for systemic follow-up |

---

## 2026-05-14 — Phase 4: Lexicon Expansion (Committee Review)

**Committee:** 5 specialists (Phonologist, Morphologist, Lexicographer, Semanticist, Aestheticist)
**Words reviewed:** 186 new proposals
**Applied to LEXICON_BASE.md:** 161 words

### Decisions Applied
- **Q1:** Strict (C)V phonotactics — 97 words amended (final obstruents → vowels, /ou/ → /au/)
- **Q2:** Tiered atom system (~50/~150/~500+) — 161 atoms, 0 descriptive compounds
- **Q3:** New words vowel-final — all 161 end in vowel or sonorant
- **Q4:** Hybrid etymology (English + Latin) — applied per semantic domain

### Rejected (10 words)
- auk, hai.po, shart, but, pis, fri.dom, los, our, so, to
- Reasons: vulgar collisions, dot notation, Spanish article collision, English function-word collision

### Structural Fixes
- tartl → tatu, batn → batu, ovn → ovu, ovr → ovar, lethr → lera, masl → masil, niaz → niasi
- skwiral → skwirali (onset reduced)
- erkweik → ert-kweik (compound reform)

### Polysemy Flags (11 words)
- ber, sil, tai, kap, ring, wotch, bank, bil, nail, fan, left
- Resolution: primary meaning kept; secondary meanings to be added as separate atoms

### Files Updated
- docs/lexicon/LEXICON_BASE.md — 161 new words in 6 subsections
- vote/topics/consensus/DECISIONS_MASTER.md — all Q1-Q4 decisions documented
- vote/topics/consensus/FINAL_WORD_REVIEW.md — per-word verdicts



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
  2. Plural system: -s → -n/-en; Case+Plural: man-se + PL → man-se-n (order: CASE → PL)
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

---

## 2026-05-14 — ROADMAP.md Updated
- **Action**: Complete rewrite of ROADMAP.md to reflect actual project state
- **Changes**:
  - Fase 1-3 marked as COMPLETE with links to deliverables
  - Fase 4: ~780/1000 words documented (~78%)
  - Fase 8 marked as NEXT PRIORITY (text benchmark)
  - Added detailed pending checklists for each incomplete phase
  - Added "Sistema de Deliberación — Estado Actual" section
  - Added "Decisiones Pendientes de Deliberación Futura" table
  - Documented all consensus-driven changes (locative, adjectives, professions, numbers)
- **Status**: COMPLETE

---

## 2026-05-14 — Fase 4: Léxico Base Expanded (732 → 1004 words)
- **Action**: Added 6 blocks of ~50 words each (300 new words) organized by semantic category
- **Blocks created in word_review/**:
  - Block 1: Verbos Esenciales Extendidos (39 verbs)
  - Block 2: Animales (47 animals)
  - Block 3: Clothing, Materials and Textures (50 words)
  - Block 4: Technology, Tools and Modern Household (50 words)
  - Block 5: Shapes, Directions, Space and Measures (50 words)
  - Block 6: Abstract Concepts, Society, Economy and System (50 words)
- **New sections in LEXICON_BASE.md**:
  - Clothing, Materials and Textures
  - Shapes, Directions, Space and Measures
- **Existing sections expanded**:
  - Nature and Environment (animals)
  - Technology and Tools (modern tech)
  - Abstract and Emotional Concepts (society/economy)
  - Verbs — Extended Set (essential verbs)
- **Status**: 1004 total words / 934 unique — Fase 4 COMPLETE

---

## 2026-05-15 — Atomic Word Ceiling Deliberation (Committee Consensus)

**Committee:** 5 specialists (Phonologist, Morphologist, Lexicographer, Semanticist, Aestheticist)
**Topic:** How many atomic words should VELA have?
**Status:** ✅ CONSENSUS REACHED

### Decision: Soft Ceiling at 200 Atoms

- **Tier 0:** 50 primitives (pronouns, numbers 0-10, core verbs) — CLOSED class
- **Tier 1:** 150 high-frequency atoms (body parts, nature, animals, tools, food, emotions) — OPEN within ceiling
- **Tier 2+:** Compounds only, subject to Quality Gate (SHORT, MEANINGFUL, SOUNDS GOOD, NOT INFANTILE)

### Rationale (4/5 convergence)
- **Lexicographer:** 200 hard ceiling — prevents Esperanto trap (~900 roots = memorization wall)
- **Morphologist:** ~200 soft ceiling — compound engine breaks below this (60-70% of needed compounds fail Quality Gate)
- **Semanticist:** 200-220 by semantic necessity — Swadesh + basic domains empirically require ~200 atoms
- **Phonologist:** ~220 soft ceiling — prosodic demotion in 3+ syllable compounds degrades melodic profile
- **Aestheticist:** 250 soft ceiling — cradle test fails for emotional vocabulary at 200 (dissent recorded)

### Policy Decisions
1. **No retroactive elimination** — existing ~600-700 unique atoms are grandfathered
2. **Quality Gate remains active filter** — new atoms only if ALL 4 tests fail as compound
3. **Semantic Necessity Test** for new atoms: uniqueness + frequency + non-decomposability + cultural centrality

### Dissent
- **Aestheticist:** Advocated 250 atoms for poetic register. Deferred to 200 with exception path via Semantic Test.

### Files Created
- vote/topics/current_topic.md
- vote/topics/proposals/ATOM_CEILING_{lexicographer,phonologist,morphologist,semanticist,aestheticist}.md
- vote/topics/consensus/ATOM_CEILING_consensus.md
- vote/SUMMARY.md

### Files to Update (pending)
- docs/grammar/GRAMMAR_COMPLETE.md — add ceiling to Section 15
- vote/topics/consensus/ATOMS_VS_COMPOUNDS_Q2.md — append ceiling decision
- README.md — note lexicon ceiling in vocabulary section

---

## 2026-05-15 — Fase 8: Textos y Muestras — Creative Writing (pi-teams)

**Method:** pi-teams (teammates in tmux panes)
**Agents:** vela_poet (kimi-k2.6), vela_narrator (deepseek-v4-pro)
**Status:** ✅ COMPLETE

### Deliverables

1. **100 Daily Phrases** — docs/texts/PHRASES_100.md
   - 10 categories × 10 phrases each
   - ~55 new vocabulary gaps identified

2. **4 Original Poems** — docs/texts/POEMS_COLLECTION.md
   - "La Rein and La Longin" (rain/longing)
   - "La Child and La Dream" (child/dream)
   - "La Mar and La Solitud" (sea/solitude)
   - "Tu Luv" (love)

3. **1 Short Story** — docs/texts/SHORT_STORY_BIRD.md
   - "Wan Smol Bird" (bird learns to sing)
   - ~650 words, 7 paragraphs, bilingual

### pi-teams Success Notes
- Agents spawned successfully in tmux panes (%11, %12)
- Communication via mailbox worked
- Prompts included full vocabulary dossiers (no file reads needed)
- Both agents completed within ~90 seconds

### New Words for Committee Review
| Word | English | Source |
|------|---------|--------|
| longin | longing | English |
| solitud | solitude | Latin |
| kwaiet | quietly | English |
| krei | cry | English |
| throt | throat | English |
| biliv | believe | English |
| proud | proud | English |
| teer | tear (eye) | English |
| raiz | rise | English |

