# 🗺️ VELA Development Roadmap

> Roadmap for building VELA from concept to a complete, speakable language.  
> Based on `INITIAL_RESEARCH.md` — the foundational design document — and deep research.

---

## VELA's Fixed Design Decisions

These decisions are **already made** and do not change:

```
PHONOLOGY:
  ✅ 5 vowels: a, e, i, o, u (no schwa, no reduced vowels)
  ✅ 17 consonants: p, t, k, b, d, g, m, n, f, v, s, z, sh, h, l, r, w, y
  ❌ NO: th, schwa, zh, difficult clusters (str-, spr-, thr-)
  ✅ Syllable structure: (C)V — every syllable ends in a vowel
  ✅ Pitch accent (penultimate) — NOT stress — like Japanese/Spanish
  ✅ Clusters allowed at onset only: st-, sp-, tr-, pr-, bl-, cl-, gr-, fl- etc.

GRAMMAR:
  ✅ SVO word order
  ✅ Zero irregular verbs
  ✅ Present: root + -a | Past: root + -ed | Future: root + -wil
  ✅ No grammatical gender — "li" = he/she/it
  ✅ One article: la (the), un (a/an)
  ✅ Agglutinative morphology

WORD BUILDING:
  ✅ Roots + affixes = compound words
  ✅ Every morpheme has one transparent meaning
  ✅ Categories by ending: -a (verb), -i (noun), -im (adj), -um (adv)

VOCABULARY SOURCE:
  ✅ Based on English words, phonetically regularised
  ✅ ~1000 core words as foundation
  ✅ Fully transparent compounding
```

---

## Development Stages

```
Stage 0  → Research & Foundation   ← DONE (INITIAL_RESEARCH.md)
Stage 1  → Phonology Finalisation    (2-3 weeks)
Stage 2  → Writing System           (2-4 weeks)
Stage 3  → Grammar Deepening         (4-6 weeks)
Stage 4  → Core Lexicon (1000 words) (4-8 weeks)
Stage 5  → Extended Lexicon         (ongoing)
Stage 6  → Texts & Documentation   (ongoing)
Stage 7  → Community & Evolution     (future)
```

---

## Stage 0 — Research & Foundation ✅ DONE

**Status:** Complete. `INITIAL_RESEARCH.md` is the source of truth.

**Deliverables:**
- [x] `INITIAL_RESEARCH.md` — bilingual (ES/EN) foundational design document
- [x] `docs/research/01-phonology.md` — deep research: sound systems
- [x] `docs/research/02-writing-systems.md` — script design principles
- [x] `docs/research/03-semantic-typology.md` — typological foundations

---

## Stage 1 — Phonology Finalisation

**Goal:** Finalise every sound, rule, and pattern of VELA's phonology.

### 1.1 Finalise Consonant Inventory
- [ ] Confirm 17 consonants are correct and sufficient
- [ ] Define allophonic rules (how sounds vary in context)
- [ ] Document each sound with IPA symbol + VELA letter + example words

### 1.2 Finalise Vowel Inventory
- [ ] Confirm 5 vowels are correct
- [ ] Define if vowel length exists (long/short distinction)
- [ ] Define nasalised vowels (ã, ẽ etc.) — YES or NO
- [ ] Define diphthongs (which, how many)

### 1.3 Phonotactics — The (C)V Rule
- [ ] Confirm: every syllable ends in a vowel
- [ ] Document all permitted onset clusters (st-, sp-, tr- etc.)
- [ ] Document prohibited combinations
- [ ] Define stress/pitch accent rules precisely:
  - Penultimate if vowel-final
  - Ultimate if consonant-final
  - Exceptions (if any)

### 1.4 Pitch Accent System (VELA's Key Innovation)
- [ ] Document the pitch contour: penultimate syllable goes HIGH
- [ ] Define how pitch interacts with phrase-level intonation
- [ ] Create audio examples of pitch accent vs. stress
- [ ] Test with speakers of different native languages

### 1.5 Phonological Word List
- [ ] Generate 500 test words following all rules
- [ ] Read aloud — does it sound musical and flowing?
- [ ] Adjust rules if any sound awkward or unnatural

**Deliverable:** `docs/phonology/PHONOLOGY_FINAL.md`

---

## Stage 2 — Writing System

**Goal:** Create a VELA script that is beautiful, original, and functional.

### 2.1 Script Design
- [ ] Choose script type:
  - **Option A:** Adapted Latin alphabet (A-Z + accented variants) — easiest to read
  - **Option B:** Original syllabic script (Hangul-inspired blocks) — most distinctive
  - **Option C:** Original alphabetic script (Tengwar-inspired) — elegant, distinctive
- [ ] Research: Cherokee (invented 1820s), Hangul (1446), Zhuyin (1900s)
- [ ] Design every character (15-50 strokes each, no more)
- [ ] Ensure each character is visually distinct
- [ ] Create handwritten/cursive variant

### 2.2 Punctuation and Conventions
- [ ] Direction: LTR confirmed
- [ ] Define punctuation marks (invented or adapted?)
- [ ] Capitalisation rules
- [ ] Number format
- [ ] Word spacing (confirmed: spaces between words)

### 2.3 Font Development
- [ ] Create digital font for the chosen script
- [ ] Define bold, italic variants
- [ ] Test at different sizes and contexts

### 2.4 Script Decision Algorithm
```
IF script = Latin adaptation:
  → Every VELA letter = one Latin letter
  → Special letters: sh (ʃ), ng (ŋ) etc.
ELIF script = original:
  → Each consonant gets a unique glyph
  → Each vowel gets a unique glyph or diacritic
  → Layout: linear, block, or syllabic?
```

**Deliverable:** `docs/writing/SCRIPT_DESIGN.md` + font files

---

## Stage 3 — Grammar Deepening

**Goal:** Expand the grammatical system from the initial research into full detail.

### 3.1 Confirm Core Grammar
Based on `INITIAL_RESEARCH.md`:

```
SVO word order — CONFIRMED
Articles: la (the), un (a/an) — CONFIRMED
Pronouns: mi, yu, li, wi, de — CONFIRMED
Verbs: root-a (present), root-ed (past), root-wil (future) — CONFIRMED
No gender — CONFIRMED
```

### 3.2 Case System — 4 CASES (CONFIRMED)

Based on deep research: VELA adopts a 4-case system for precision without complexity.

| Case | Suffix | Function | Example |
|------|-------|---------|---------|
| **Nominative** | (none) | Subject of sentence | *Mi si la film.* — I see the film |
| **Accusative** | -**a** | Direct object | *Yu si la man-a.* — You see the man |
| **Genitive** | -**de** | Possession | *la man-de hous* — the man's house |
| **Locative** | -**en** | Location, time | *la siti-en* — in the city, *la dei-en* — on that day |

**Key insight from research:** All four cases follow the agglutinative principle — transparent suffixes that never fuse. No fusional mess like Spanish ("el→del"). Every suffix is separable and learnable.

- [ ] Confirm case endings: -a (acc), -de (gen), -en (loc)
- [ ] Test: do all noun forms work with the (C)V syllable rule?
- [ ] Document: case + plural interaction (e.g. plural accusative)
- [ ] Prepositions override case: "la man EN la siti" = the man (LOC) in the city
- [ ] Test 100 sentences with cases — does it feel natural or forced?

**See:** `docs/grammar/03-case-system.md` for full implementation

### 3.2 Expand TAM (Tense-Aspect-Modality)
- [ ] **Aspect:** Perfective (-ed), Progressive (-ing / -an?)
- [ ] **Modality:** Ability (kan), Necessity (mas), Desire (wan)
- [ ] **Conditional:** if + clause + wud + result
- [ ] **Subjunctive:** Confirm if needed or if -ed covers it

### 3.3 Pronoun System Deep Dive
- [ ] Pronouns: mi, yu, li, wi, de — confirm all forms
- [ ] Possessive: mif, yuf, liz, wef, def — confirm
- [ ] Reflexive: self + pronoun — as in research?
- [ ] Demonstratives: dis, dat, dese, dase
- [ ] Indefinites: som, eni, no, evri
- [ ] Relatives: who → hu, what → wat, when → wen

### 3.4 Question System
- [ ] Yes/No questions: verb-first + q particle? (Si-a yu la film?)
- [ ] Wh-questions: hu, wat, wen, wer, hai, wai, hou
- [ ] Confirm: all wh-words = English base + phonetic regularisation

### 3.5 Prepositions and Conjunctions
- [ ] Core prepositions: a (at/to), in, on, from, for, wit (with), from
- [ ] Conjunctions: and, bot (but), or, so, bikos (because)

### 3.6 Negation
Based on the research:
- [ ] no + verb = normal negation: Mi no si la film.
- [ ] nevr + verb = absolute negation: Li nevr tok.
- [ ] un- + adjective = antonym prefix: gud → un-gud

### 3.7 Number System
From the research:
```
wan, tu, tri, for, faiv, siks, sevn, eit, nain, ten
ten-wan = 11 ... ten-nain = 19
twenti = 20, tu-ten = 20, for-ten-tri = 43
handrd = 100, zausand = 1000
```

### 3.8 Time and Calendar
- [ ] Days of week (already designed in research)
- [ ] Months (need names)
- [ ] Time expressions: now, den (then), bifor (before), aft (after)

### 3.9 Passive Voice
- [ ] Is passive needed? How is it formed?
  - Option: woz + verb → La buuk woz rit-ed bai mi. (The book was written by me.)
- [ ] Confirm or decide against

**Deliverable:** `docs/grammar/GRAMMAR_FULL.md`

---

## Stage 4 — Core Lexicon (1000 Words)

**Goal:** Build the foundation vocabulary. Based on `INITIAL_RESEARCH.md`.

### 4.1 The 5 Word Categories (from Research)
```
Category     | Suffix  | Example
Verb (present) | -a   | tok-a
Verb (past)     | -ed  | liv-ed
Verb (future)   | -wil | si-wil
Noun           | -i    | famili
Adjective      | -im   | belim
Adverb         | -um   | quick-um
```

### 4.2 Core Vocabulary Sourcing
- [ ] Top 1000 English words → VELA phonetic regularisation
- [ ] Source: already documented in `INITIAL_RESEARCH.md`
- [ ] Formalise into `lexicon/vela_1000_words.json`

### 4.3 Productive Affix System
```
PREFIXES:
  un-  = negation       → un-gud (bad)
  re-  = repetition     → re-go (return)
  pre- = before         → pre-skol (preschool)
  mis- = error          → mis-tok (misspeak)
  self-= reflexive      → self-lov (self-love)
  non- = absence        → non-stop
  over-= excess         → over-hapi (too happy)
  under-= deficiency    → under-dev (underdeveloped)

SUFFIXES:
  -er  = agent          → wotc-er (watcher)
  -ing = action         → wotc-ing (watching)
  -li  = adverb         → quick-li (quickly)
  -nes = abstract noun  → happi-nes (happiness)
  -ful = full of        → hope-ful
  -les = without        → hope-les (hopeless)
  -bl  = capable        → understand-bl (understandable)
  -ish = resembling     → child-ish
  -skap= condition     → happi-skap (happiness/condition)
```

### 4.4 Sound Symbolism System
Based on research into phonosemantics:
- [ ] Build systematic sound-meaning associations
- [ ] Front vowels (i, e) → small, sharp, light
- [ ] Back vowels (o, u) → large, round, heavy
- [ ] Nasals (m, n) → continuous, soft
- [ ] Plosives (p, t, k) → abrupt, sudden
- [ ] Apply consistently to new word creation

### 4.5 Word List Validation
- [ ] All 1000 words follow (C)V syllable structure
- [ ] No forbidden sounds or clusters
- [ ] All words are pronouncable by speakers of Spanish, English, Mandarin, Arabic
- [ ] All words pass the "root test" (can be understood from components)

**Deliverable:** `lexicon/vela_1000_words.json`

---

## Stage 5 — Extended Lexicon

**Goal:** Expand vocabulary to cover all topics naturally.

### 5.1 Semantic Fields to Expand
- [ ] Technology & computing: software, hardware, internet, AI...
- [ ] Science: biology, chemistry, physics, medicine...
- [ ] Arts: music, painting, literature, cinema...
- [ ] Abstract concepts: philosophy, ethics, politics, law...
- [ ] Emotions (fine distinctions): melancholy, serenity, restlessness...
- [ ] Religion/spirituality (for VELA's user community)
- [ ] Food, cooking, clothing, customs
- [ ] Trades, professions, tools

### 5.2 Loanword Policy
- [ ] When VELA takes a word from English (or other languages):
  - Phonetically regularise it: computer → kompiutr
  - Morphologically adapt it: verb + -a ending
- [ ] Create native VELA compound for common concepts

### 5.3 Idiom Development
- [ ] Develop VELA-specific idioms that don't translate from English
- [ ] These give VELA cultural character:
  - *"La ston no kan swim"* — literal: the stone cannot swim
  - Meaning: you can't change your nature

**Deliverable:** `lexicon/vela_extended_words.json`

---

## Stage 6 — Texts & Documentation

**Goal:** VELA exists in the world through real texts.

### 6.1 The Benchmark Text
The standard test for any conlang — translate:

```
"Go forth in peace to love and serve the Lord."
```

In VELA: *「Go-ed fors in pis a lov and serv la Lord.」*

This becomes VELA's signature sentence.

### 6.2 Sample Texts
- [ ] Write 5 poems in VELA
- [ ] Write a short story (500-1000 words)
- [ ] Translate a children's story
- [ ] Write a short philosophical text
- [ ] Document each translation decision

### 6.3 The Reference Grammar
- [ ] Consolidate all grammar decisions into one document
- [ ] Format: reference manual (not tutorial)
- [ ] Include paradigms for every word class
- [ ] Include examples for every rule

### 6.4 The VELA Dictionary
- [ ] Format: VELA word → IPA pronunciation → category → definition → compound examples
- [ ] Minimum: 1000 entries
- [ ] Target: 3000+ entries

**Deliverables:** `texts/`, `docs/vela_reference_grammar.md`, `lexicon/vela_dictionary.md`

---

## Stage 7 — Community & Evolution (Future)

- [ ] Online community of speakers
- [ ] VELA Wikipedia (one language describing itself)
- [ ] Literature and music in VELA
- [ ] Translation challenges
- [ ] Decide: will VELA evolve with a "Proto-VELA" history?

---

## Priority Task Order

```
IMMEDIATE NEXT STEPS (this week):
1. Stage 1.1 → Confirm all 17 consonants + 5 vowels
2. Stage 1.4 → Document pitch accent rules with audio examples
3. Stage 2   → Decide script type (Latin or original?)
4. Stage 3   → Expand the grammar from research into full document
5. Stage 4   → Formalise the 1000-word list into JSON

NEXT MONTH:
6. Stage 1   → Phonology complete
7. Stage 2   → Script design decided + draft characters
8. Stage 4   → Core lexicon finalised
```

---

## Open Design Questions (to resolve)

```
✅ SCRIPT: Latin adaptation CONFIRMED
□ VOWEL LENGTH: Does VELA have long/short vowel distinction?
□ NASAL VOWELS: Does VELA have ã, ẽ etc.?
□ CASE SYSTEM: ✅ Nominative + Accusative + Genitive + Locative CONFIRMED (4 cases)
□ DIALECTS: Will VELA have official variants?
□ PRONUNCIATION AUDIO: Who records the first audio samples?
□ COMMUNITY: Where does the community gather?
```

---

*Roadmap based on `INITIAL_RESEARCH.md` and deep research.*
*VELA — for when the world needs to talk.*
