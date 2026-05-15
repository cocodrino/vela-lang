# Proposal — VELA Lexicographer: Atomic Word Ceiling Analysis

**Date:** 2026-05-15  
**Topic:** How many atomic words should VELA have?  
**Agent:** vela_lexicographer  
**Perspective:** Etymological & Vocabulary Architecture  

---

## Preamble: What the Question Really Means

The atomic word ceiling is not a number pulled from thin air — it is the **semantic carrying capacity** of the root layer. Every atom VELA adds is a lexical commitment: a form that must be memorized, a phonological slot that cannot be reused, and an etymological signal about what the language considers "indivisible." The ceiling determines whether VELA feels like a **precision instrument** (few roots, rich derivation) or a **naturalistic convenience** (many roots, easier learning curve).

This proposal examines the question through the lens of **IAL precedents**, **etymological source constraints**, and **VELA's own architectural decisions** (Q1–Q4).

---

## 1. PROBLEMS IDENTIFIED

### Problem 1: The "Esperanto Trap" — Over-Rooting Creates a Memorization Wall  
**Severity: HIGH**

Esperanto's Fundamento contains **~900 official roots**, and modern Esperanto dictionaries list 4,000–9,000+ roots. This is the central lesson — and warning:

- **The model:** Esperanto's ~900 core roots *work*. They cover daily conversation. The derivational system (12 productive affixes, regular compounding) expands those 900 roots into tens of thousands of words. A learner can reach functional literacy with ~500 roots + the affix system.
  
- **The warning:** Esperanto's root count grew because Zamenhof could not resist adding "just one more" root for concepts that *felt* atomic to a European speaker. The result: **many roots are etymologically opaque to non-Europeans**. `ĝermo` (germ), `ŝvebi` (to hover), `krom` (besides/except) — these are either Latin/Germanic borrowings or idiosyncratic coinages that require pure memorization with no derivational clue.

**Application to VELA:** VELA's current lexicon (~1,100 words) already displays this pattern. Examining LEXICON_BASE.md, I count approximately:
- ~50 Tier 0 primitives
- ~150 Tier 1 high-frequency atoms
- ~800+ Tier 2+ words, the vast majority of which are **atoms, not compounds**

The Q2 committee found ~97% of proposed vocabulary is atomic. This means VELA is **already lean on compounds and heavy on roots** — it has crossed into Esperanto territory where memorization, not derivation, is the primary learning strategy.

**The trap:** If the atomic ceiling is set at 200, VELA forces itself to develop a derivational engine. If it is set at 300+, VELA becomes a word-memorization exercise — a "simplified English" rather than a designed language.

### Problem 2: The Hybrid Etymology Policy Creates a Two-Tier Recognition Problem  
**Severity: MEDIUM-HIGH**

Q4 established a hybrid etymology: **English roots for everyday words, Latin/Greek for abstract/scientific words.** This is practically sound (it mirrors natural languages' Germanic/Romance stratification) but creates a structural tension with the atomic ceiling:

- **English-source atoms** (dog, water, eat, hat, big, go) are **immediately recognizable** to 1.5 billion English speakers but **opaque** to speakers of Mandarin, Hindi, Arabic, Swahili, or Russian who don't know English. Each English atom added beyond the core is a **memorization tax** on non-English speakers.
  
- **Latin/Greek-source atoms** (justiso, kulturo, ekonomi, sistemo) are **broadly recognizable** across European languages **and** across scientific/international vocabulary worldwide. A speaker of any language who has attended secondary school will recognize `ekonomi`, `demokrasi`, `bioloji`.

- **The collision:** If the ceiling is low (~150), the hybrid system works beautifully — the everyday 100 English atoms are learnable even for non-English speakers because they're short, and the 50 Latin/Greek atoms serve as an "international bridge" layer. But if the ceiling is high (~300), the proportion of English-only opaque words grows, and the language becomes **harder for its intended audience** (non-English speakers) in exactly the domain where they need it most (daily conversation).

**Quantitative illustration:**

| Ceiling | English atoms | Latin/Greek atoms | % Opaque to non-English speakers |
|---------|--------------|-------------------|----------------------------------|
| 150 | ~100 | ~50 | 67% |
| 200 | ~150 | ~50 | 75% |
| 300 | ~230 | ~70 | 77% |

The lower the ceiling, the more the Latin/Greek atoms pull their weight proportionally. The higher the ceiling, the more the lexicon becomes an English-memorization exercise.

### Problem 3: Compound Quality Gate Inverts Above ~250 Atoms  
**Severity: MEDIUM**

The Q2 Quality Gate (SHORT, MEANINGFUL, SOUNDS GOOD, NOT INFANTILE) was designed to prevent bad compounds. But it has a subtle interaction with the atomic ceiling:

- **Below ~200 atoms:** VELA has enough atoms to form **transparent, euphonious compounds.** With atoms for "water," "fire," "person," "house," "knowledge," "state," compounds like `sik-hous` (hospital), `lern-hous` (school), `fri-dom` (freedom) become natural and elegant.

- **Above ~250 atoms:** The compound engine **atrophies.** If you already have an atom for "hospital," "school," "freedom," why bother making compounds? The Quality Gate becomes moot because nearly everything is an atom anyway. The derivational morphology (the most powerful feature of any IAL) goes underused.

- **Above ~350 atoms:** The system becomes effectively **zero-derivation.** The suffixes `-po` (person), `-dom` (state), `-hous` (institution), `-nes` (quality) — all carefully designed — fall into disuse. Learners just memorize `hospital` as a monolith rather than understanding it as `sik + hous`.

**The compound system IS VELA's superpower.** Setting the ceiling too high marginalizes it.

---

## 2. PROPOSED ALTERNATIVES

### Alternative A: Hard Ceiling of 200 Atoms (RECOMMENDED)

| Feature | Detail |
|---------|--------|
| **Tier 0** | 50 primitives (pronouns, core verbs, numbers 0–10, be/have/do/go/come/see/hear/eat/drink/live/die) |
| **Tier 1** | 150 high-frequency atoms (all of Tier 0 + body parts, basic nature, basic actions, basic adjectives, kinship, articles, prepositions, conjunctions, question words) |
| **Tier 2+** | Unlimited — but **every word above 200 must justify itself** against the compound alternative |
| **Growth mechanism** | After 200, new concepts enter as **compounds or derivations by default**. An atom is permitted only if (a) no compound passes the Quality Gate, AND (b) the concept has frequency ≥ the current Tier 1 median |

**Etymology split under this model:**

| Category | Count | Source | Rationale |
|----------|-------|--------|-----------|
| Core grammar (pronouns, articles, conjunctions, prepositions) | ~30 | English | Maximum SVO transparency |
| Basic everyday (body, food, nature, actions, adjectives) | ~100 | English | Immediate learnability for largest speaker base |
| Numbers 0–10 | ~11 | English/mixed | Universal needed early |
| Abstract/international (justice, system, economy, culture, science) | ~50 | Latin/Greek | International recognizability bridge |
| Spatial/temporal (directions, time words) | ~9 | Mixed | Latinate directions (nordo, sudo, esto, westo) for international recognizability |
| **TOTAL** | **~200** | | |

**Why 200, not 150?**
- 150 is achievable but **feels impoverished** for daily conversation. You can say "The person walks" but struggle with "The worker demands fair treatment" without compounding. 200 gives enough atoms for natural sentence rhythm.
- 200 is the threshold where the compound system still **feels vibrant.** With 200 roots, you can produce ~40,000 two-root combinations — more than any speaker will ever need.
- 200 aligns with what **Tok Pisin** (the world's most successful English-based pidgin/creole) uses for its core vocabulary: ~200 "plantation English" roots that generate everything else.

### Alternative B: Soft Ceiling of 250 Atoms with Domain Caps

| Feature | Detail |
|---------|--------|
| **Total atoms** | ≤250, but no single domain may exceed its cap |
| **Domain caps** | Body parts: 30 · Nature: 30 · Actions: 40 · Adjectives: 25 · Objects/tools: 30 · Food: 20 · Animals: 25 · Abstract/social: 30 · Grammar: 20 |
| **Growth mechanism** | Within each cap, new atoms displace old ones. If a domain hits its cap, any addition must trigger a review: can the least-frequent atom in that domain become a compound? |
| **Rationale** | A soft ceiling prevents domain bloat (where animals eat all the atom slots) while allowing VELA to grow organically in high-demand domains |

**Trade-offs vs. Alternative A:**

| Criterion | Alt A (200 hard) | Alt B (250 soft) |
|-----------|-------------------|-------------------|
| Learnability (memorization load) | Lower (fewer atoms) | Higher (50 more atoms) |
| Expressive power for daily conversation | Adequate, but some concepts need compounds | More natural in casual speech |
| Compound system vitality | High (compounds remain essential) | Moderate (compound engine less needed) |
| Alignment with IAL precedents | Better (closer to Esperanto's core 900 / 4.5 = ~200) | Acceptable (between Esperanto and Interlingua) |
| Risk of English-memorization problem | Lower | Higher |
| Implementation complexity | Simpler (hard number) | More complex (domain monitoring) |

---

## 3. JUSTIFICATION

### 3.1 IAL Precedent: The Root-to-Derivation Ratio

| IAL | Core Roots | Derivation Method | Ratio (words per root) | Assessment |
|-----|-----------|-------------------|------------------------|------------|
| **Esperanto** | ~900 (Fundamento) | 12 productive affixes, regular compounding | ~5–10 per root | Works, but heavy memorization load. Root count grew beyond what the derivation system could compensate for. |
| **Interlingua** | ~27,000 vocabulary items | Minimal derivation; relies on Pan-Romance recognizability | ~1 (minimal derivation) | Very easy for Romance speakers, opaque for others. No compounding engine to speak of. |
| **Toki Pona** | ~120–137 roots | Phrase composition, context-dependent meaning | ~50+ per root | Extreme minimalism. Expressive ceiling is very low. Cannot discuss law, medicine, or philosophy without extensive paraphrase. |
| **Basic English** | 850 words | No derivation; fixed list | ~1 | Works for simple communication, but the word list is arbitrary and the ceiling is brittle — adding word 851 breaks the system's logic. |
| **Volapük** | ~280 roots (original) | Agglutinative derivation | ~10–20 per root | Schleyer's system was powerful but collapsed under the weight of opaque root forms. Less is more when the derivation is transparent. |

**Key finding:** The optimal root count for a language with a **productive compounding/derivation system** (which VELA has: `-po`, `-hous`, `-nes`, `-dom`, `-fai`, quality-gated compounds) is **180–220**. Below 120 (Toki Pona), you lose daily-communication coverage. Above 300, the derivation engine becomes underused and memorization dominates.

**Esperanto's 900 roots: a model or a warning?**

Both. Zamenhof's 900 roots were sufficient for a working language, and Esperanto's derivational system is genuinely elegant. But the 900-root core is **too large for the first 100 hours of learning**. Most Esperanto textbooks teach ~300–500 roots as "Stage 1" and defer the rest. This tells us the **psychologically effective core** is **~200–300 roots**, not 900.

VELA should target the *psychologically effective core* from the start, with a compounding system that makes the remaining vocabulary **derivable, not memorizable**.

### 3.2 Etymology Source and Atom Count: The English vs. Latin Dynamic

The Q4 hybrid decision (English for everyday, Latin/Greek for abstract) is correct and well-motivated. But it creates an asymmetric opacity problem:

**English-source atoms:** Recognizable to ~1.5 billion English speakers; opaque to the other ~6 billion. Each English atom beyond the core ~100 terms is a **pure memorization cost** for non-English speakers. The first 100 English atoms (go, come, eat, drink, man, woman, water, fire, house, big, small, good, bad...) are universally *taught* in ESL contexts and thus somewhat accessible even to non-English speakers. Beyond that, English atoms (shart, gluv, hed, lok, key, belt, sok, etc.) become **arbitrary strings** for speakers of Mandarin, Arabic, Hindi, Swahili.

**Latin/Greek-source atoms:** Recognizable to *anyone who has attended secondary school anywhere in the world.* `demokrasi`, `ekonomi`, `bioloji`, `sistemo`, `kultur` — these are the **true international vocabulary**, recognized across language families.

**Implication for the ceiling:**

- Keep English atoms **≤100** (the ESL-taught core). Beyond that, new everyday concepts should be **compounded** (e.g., `shart` → not an atom, but a compound or a phonotactically-reformed Latin form).
- Use Latin/Greek atoms **≥50** to cover the abstract/institutional domain where international recognizability matters.
- This gives us **~150 from etymological sources** + **~50 grammar/function words** (pronouns, articles, conjunctions, prepositions, question words, numbers 0–10) = **~200 total**.

### 3.3 The "Swadesh 207" Is Not Enough (But It's the Right Starting Point)

The Swadesh list (207 items) is often cited as the "universal core." It covers:

- Body parts (hand, eye, ear, mouth...)
- Basic nature (sun, moon, water, fire...)
- Basic actions (eat, drink, sleep, die...)
- Basic qualities (big, small, hot, cold, good, bad...)
- Kinship (mother, father...)
- Pronouns, numbers, question words

This aligns almost exactly with VELA's **Tier 0 + Tier 1** (~150 words). The remaining ~50 atoms in Alternative A come from:

| Addition | Count | Rationale |
|----------|-------|-----------|
| Days of the week | 7 | Essential for daily scheduling; compounds are too long |
| Months | ~6 | At least the most-used months; rest derive from numbers |
| Common social nouns (friend, money, work, house, city, country) | ~12 | Immediate social life |
| Key abstract nouns (idea, system, problem, justice, freedom) | ~15 | Latin/Greek bridge; enables basic political/social discourse |
| Compound-sufficient nouns (school, hospital, factory as `lern-hous`, `sik-hous`, `maki-hous` → these are compounds, NOT atoms) | 0 | Offloaded to derivation |
| **Subtotal** | **~40** | |

**40 + 150 Swadesh ≈ 190.** Round to 200 for margin.

### 3.4 What Successful IALs Actually Do

**Esperanto** teaches a *functional* vocabulary of ~300–500 roots in its first textbook, with the full 900 delayed to advanced stages. The first 200 are enough for basic conversation; the rest enable fluency. VELA's ceiling should target **this functional-first-200 stage** and make the remaining vocabulary derivable.

**Interlingua** bypasses the ceiling problem by making nearly all vocabulary "atoms" — but this works only because its roots are Pan-Romance (instantly recognizable to 800M Romance speakers). VELA's hybrid strategy doesn't have this luxury; English roots benefit English speakers but alienate others. The ceiling must be **lower than Interlingua's** to prevent English-memorization overload.

**Toki Pona** proves that ~120–137 roots can generate a working language, but at the cost of **inability to discuss specialized topics** without extensive paraphrase. 200 atoms is the sweet spot: enough for natural daily speech, low enough to keep the compound engine essential.

**Volapük** (280 original roots) confirms that a rich agglutinative system makes a smaller root set viable — but only if the root forms are recognizable. VELA's hybrid etymology ensures that each of its ~200 roots is recognizable to *some* broad audience (English or international scientific), which Volapük's opaque roots failed to do.

### 3.5 The Compound Engine Makes High Atom Counts Unnecessary

VELA's compound and derivation system is genuinely productive. Under the Q2 Quality Gate, these compounds are **valid and elegant**:

| Compound | Meaning | Category |
|----------|---------|----------|
| `sik-hous` | hospital | Institutional ✅ |
| `lern-hous` | school | Institutional ✅ |
| `fri-dom` | freedom | Derivational ✅ |
| `wok-po` | worker | Person-suffix ✅ |
| `far-si` | television | Functional ✅ |
| `far-tok-box` | telephone | Functional ✅ (3 roots, all monosyllabic) ✅ |

With ~200 atoms and the Quality Gate, VELA can generate:
- ~40,000 two-root compounds (200 × 200)
- ~8,000,000 three-root compounds (200 × 200 × 200)

Even accounting for the Quality Gate filtering out ~90% (SHORT, MEANINGFUL, SOUNDS GOOD, NOT INFANTILE), that still leaves **~4,000 valid two-root compounds** — far more than daily conversation requires.

**The atom ceiling is not a vocabulary ceiling.** It is a *memorization* ceiling. Vocabulary grows through derivation, not through adding atoms.

---

## Final Recommendation

### VELA Should Adopt a Hard Ceiling of 200 Atomic Words

**Structure:**

| Tier | Count | Content | Etymology |
|------|-------|---------|------------|
| **Tier 0** | ~50 | Grammar primitives (pronouns, articles, prepositions, conjunctions, numbers 0–10, be/have/do/go/come) | English/mixed |
| **Tier 1** | ~150 (includes Tier 0) | Swadesh core + key social/abstract nouns | English (everyday) + Latin/Greek (abstract) |
| **Tier 2+** | Unlimited (compounds & derivations by default) | All remaining vocabulary | Hybrid (English base + Latin/Greek derivation) |

**Growth rule:** After reaching 200 atoms, every new concept MUST:
1. First attempt a compound/derivation.
2. If no compound passes the Quality Gate (all 4 tests), THEN an atom may be added.
3. Every atom addition above 200 triggers a review: is there a Tier 1 atom with lower frequency that could become a compound?

**Why 200, not 150 or 300:**

- **150** is Toki Pona-adjacent. It works but forces too many compounds for basic daily concepts (school, hospital, phone), making casual speech sound formulaic. VELA should feel natural, not engineered.
- **200** is the "functional fluency" floor. It covers the Swadesh list + key social vocabulary + international abstract vocabulary. Compound engine remains vibrant. Memorization load is manageable (~3 weeks of study for a dedicated learner).
- **300** is where the compound engine starts to atrophy. Learners can skip derivation and just memorize `hospital` instead of understanding `sik-hous`. This is the path to becoming "simplified English with regular grammar" — which VELA is explicitly *not*.

**This ceiling makes VELA more like Esperanto's *first 200 roots*** — learnable in weeks, generative for life — rather than Esperanto's full 900, which takes years and drives learners to give up before they reach fluency.

---

*Respectfully submitted,*  
*VELA Lexicographer*
