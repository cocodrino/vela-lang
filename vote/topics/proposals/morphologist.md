# Proposal — VELA Morphologist (ollama/deepseek-v4-pro)
## Standby Issues Deliberation — Morphological Analysis

---

## ISSUE 1: Atomic Word Threshold (745 atoms, 35 compounds)

### Morphological Assessment: HIGH

**The core principle**: "If word order can express it, don't add morphology." The corollary: "If morphology can express it, don't memorize a root."

A lexicon of 745 atomic words is not a designed system — it is an accumulation. The learner must memorize 745 arbitrary sound-meaning mappings. A compound system of ~200 atoms + recursive morphology requires memorizing only ~200 mappings plus the compounding rule.

**Cognitive load comparison**:
- 745 atoms = 745 arbitrary associations (rote memory)
- 200 atoms + compounding = 200 associations + 1 rule (rule-based generalization)

**The compounding prerequisite**: Simple compounding does NOT fix phonotactic violations if the component roots themselves end in illegal consonants. The (C)V reform from the prior consensus must be completed first. Once all roots are (C)V-clean, compounding is safe by construction.

**Threshold recommendation**: **~150 atomic words**.
- Nivel 0 (~50): Pronouns, articles, demonstratives, basic verbs (be, go, come, see, say), numerals 0–10, body parts, kinship terms, natural elements (water, fire, earth, air, sun, moon), basic emotions (happy, sad, angry, love).
- Nivel 1 (~100): Common animals, common foods, common tools, common places (house, road, city, tree), core adjectives (big, small, good, bad, new, old), time words (day, night, year, now, then).
- Everything else: compound.

**Why 150?** It is approximately the Swadesh list expanded (basic vocabulary shared across languages). Below 150, the language loses naturalness — above 300, memorization burden exceeds rule-based efficiency.

**Specific long-atom reforms**:
- `undrstand` → `kom-hendi` (compound from comprehend root, fully (C)V) or `bene-komprendi`
- `prezidnt` → `hed-man` (head-man = leader)
- `sientist` → `nau-man` (know-man) or `siens-man`
- `aereplan` → `sky-bird` or `air-big`
- `vokabulari` → `word-list`
- `buterflai` → `biju-fle` (beauty-fly)
- `watrmeln` → `wot-mel` (water-melon)

**Rating**: HIGH. The current atomic load violates the "deduce, don't memorize" principle. But compounding must follow (C)V root reform, not precede it.

---

## ISSUE 2: PROFIL Homonymy

### Morphological Assessment: HIGH

Two distinct lexemes (`profile` and `profit`) share one surface form. This is a **morphological collision**: one form, two lemmata. In an agglutinative language where morphology is supposed to be one-to-one, this is architectural rot.

**Diagnosis**: The lexicon has accidentally merged two Latin-derived borrowings:
- *profilum* → profile (outline, side-view, account summary)
- *profectus* → profit (advance, gain, benefit)

**Reform options**:
- **A**: Keep `profil` = profile; change "profit" to `gain` / `win` / `profeto`. **Preferred**: `gain` is one syllable, atomically simple, English-derived but internationally transparent.
- **B**: Keep `profil` = profit; change "profile" to `sid-viu` / `fas-piktur`. Less preferred — "profile" is more commonly needed than "profit" in basic vocabulary.
- **C**: Change both. Overkill. One stable form should remain.

**Why not keep both?** Because agglutinative morphology provides no disambiguation mechanism. In Turkish, if two words collide, suffixes (case, possession, plural) might coincidentally help — but here both are bare nouns. `La profil` is ambiguous in every syntactic position.

**Rating**: HIGH. Easy fix, high impact.

---

## ISSUE 3: SE Noun vs SE Suffix

### Morphological Assessment: MEDIUM

**Noun `se`** (sea) = free morpheme, type `N`, can take case suffixes: `se-to` (at sea), `se-se` (sea's — potentially confusing but syntactically marked).
**Suffix `-se`** (genitive) = bound morpheme, type `N→N` (nominal modifier), attaches to pronouns or nouns: `mi-se`, `yu-se`, `buk-se`.

**Syntactic disambiguation**:
- `se` as noun: appears as head of NP, after article (`la se`), after preposition (`in la se`), as subject (`La se es big.`).
- `-se` as suffix: appears immediately after a noun/pronoun, modifying the following head noun (`mi-se buk`).

These positions are **non-overlapping**. A genitive suffix never appears where a noun can appear, and vice versa. Therefore the collision is **syntactically contained**.

**However**: Morphological systems aspire to zero ambiguity, not merely manageable ambiguity. The existence of a perfect homophone between a productive suffix and a content word is a **design debt**.

**Reform options**:
- **A**: Leave as-is. Syntactic containment is sufficient. **Default position** — no cascade.
- **B**: Change "sea" to `mar` / `oce` / `wot-bodi`. **Preferred if we fix it**. `mar` is one syllable, ends in /r/ (legal), cross-linguistically transparent.
- **C**: Change genitive suffix to `-sa` / `-si`. **Not recommended**. This would cascade to all 5 possessives plus every genitive in the lexicon — a massive morphological earthquake for a contained problem.

**Rating**: MEDIUM. Syntactic containment handles it, but ideal design would eliminate the collision.

---

## ISSUE 4: Numbers 0–1000

### Morphological Assessment: CRITICAL

**The principle**: Numbers are a closed subsystem. Closed subsystems should be maximally regular because they are high-frequency and early-acquired.

**Current system irregularities**:
1. `elevn` (11) — opaque etymology (*ainlif*), /lvn/ cluster
2. `twelv` (12) — /v/ final = phonotactic violation
3. `twenti` (20), `thirti` (30)... — semi-opaque; /nt/ cluster in some
4. `handrd` (100) — /rd/ cluster + /d/ final = violation
5. `thausand` (1000) — /nd/ cluster = violation

**The compounding logic**:
- 11 = 10 + 1 → `ten-wan`
- 12 = 10 + 2 → `ten-tu`
- 20 = 2 × 10 → `tu-ten`
- 100 = 10 × 10 → `ten-ten`
- 1000 = 10 × 10 × 10 → `ten-ten-ten`

This is fully regular, fully deducible, and eliminates all phonotactic violations.

**Morphological precedent**: Chinese (十一 = ten-one), Japanese (十一 = juu-ichi), Finnish (yksitoista = one-of-second-ten), and Hungarian all use this pattern. Even English retains traces: "twenty-one" = twenty + one.

**Why not keep `elevn` and `twelv`?** Because they are etymological fossils, not designed forms. "Eleven" comes from Old English *endleofan* (one-left-after-ten) — a compound that fossilized into opacity 1000 years ago. "Twelve" from *twalif* (two-left). These forms survived in Germanic by inertia, not by design. VELA has no inertia — it is being built now.

**Recommended system**:

| # | Form | Composition |
|---|------|-------------|
| 0–10 | `zero, wan, tu, tri, kwatro, faiv, siks, sevn, eit, nain, ten` | atomic (stable) |
| 11–19 | `ten-wan, ten-tu, ten-tri, ten-kwatro, ten-faiv...` | 10 + N |
| 20–90 | `tu-ten, tri-ten, kwatro-ten, faiv-ten...` | N × 10 |
| 21–99 | `tu-ten-wan, tu-ten-tu... tri-ten-wan...` | recursive |
| 100 | `ten-ten` | 10 × 10 |
| 101–999 | `ten-ten-wan... ten-ten-ten-wan` | recursive |
| 1000 | `ten-ten-ten` | 10 × 10 × 10 |
| 1001+ | `ten-ten-ten-wan...` | recursive |

**Zero**: Keep `zero` — it is internationally recognizable, vowel-final, and its irregularity (not following the decimal pattern) is acceptable because it is the null element.

**Alternative for 100/1000**: Keep `handrd` → `han` /han/ (trimmed, legal, recognizable) and `thausand` → `tau` /tau/ if we want dedicated short roots. But `ten-ten` and `ten-ten-ten` are more principled.

**Rating**: CRITICAL. The number system is the face of the language to every learner. If the first twelve numbers contain violations and irregularities, the learner loses trust in the system.

---

## Summary Table

| Issue | Morphological Risk | Recommended Reform |
|-------|--------------------|--------------------|
| 1 — Atomic threshold | HIGH | ~150 atoms max; compound rest after (C)V reform |
| 2 — PROFIL | HIGH | Keep `profil` = profile; "profit" → `gain` |
| 3 — SE collision | MEDIUM | Leave as-is (syntactic containment), OR change sea → `mar` |
| 4 — Numbers | CRITICAL | Full decimal compounding: `ten-wan, ten-tu, tu-ten, ten-ten` |

**Meta-priority**: Issue 4 (numbers) > Issue 2 (profil) > Issue 1 (atoms) > Issue 3 (se).

---
*Morphologist — Standby Issues Deliberation*
*Focus: morphological economy, regularity, learnability, rule consistency, zero allomorphy*

---

## ISSUE 5: Profession Suffix (CURRENT TOPIC)

### Morphological Assessment: DECISIONAL

**The morphological question**: Is a profession suffix derivational morphology (adding a rule) or compounding (using existing rules)?

VELA's axiom: *"If word order can express it, don't add morphology."* The corollary: when we DO need a morpheme, prefer compounding (two free roots) over derivation (bound affix + rule). Every new derivational rule is a permanent tax on the learner.

---

### Candidate-by-candidate morphological analysis

#### `-er` (user preference)

**Morphological type**: AMBIVALENT — can be analyzed either way.

- **Derivational reading**: `-er` is a bound suffix that nominalizes action compounds. Rule: `[action] + -er → [agent N]`. This adds 1 morphological rule to the grammar. English `teach-er`, `sing-er`, `drive-er` follow this pattern. The suffix cannot stand alone — you don't say *"the er."*

- **Compounding reading**: If VELA defines `er` as a **root morpheme** meaning "agent/doer" in the lexicon, then `lern-er` = `lern` (learn) + `er` (doer) is a compound. Zero new rules — only 1 new root. The question is whether `er` has viable free-standing meaning. Can `La er es gud.` mean "The agent is good"? Possibly, but `er` as "agent" is abstract — not a natural primitive like `po` = "person."

**Morphological cost**: 1 new root (`er` = agent), OR 1 new derivational rule (if analyzed as suffix).

**Phonotactics**: Ends in /r/ (legal coda). One syllable. Clean.

**Systematicity**: Creates a universal pattern: `[any action compound] + -er = person who does that action`. This is productive and predictable. The learner learns `-er` once and can derive every profession.

**Morphological precedent**: English `-er`, Latin `-or/-tor`, French `-eur`, Spanish `-ero/-dor`, German `-er`. Cross-linguistically, this is the most common agentive suffix in Indo-European. However, it IS a suffix — it carries the derivational morphology legacy of IE languages.

---

#### `-po` (from "person")

**Morphological type**: PURE COMPOUND.

- `po` = free root meaning "person." `lern-po` = learn + person = "learning person" = teacher. The compounding rule already exists: `[root] + [root] → [compound N]`.

**Morphological cost**: 1 new root (`po` = person). Zero new rules. The learner already knows compounding from `wot-mel`, `sky-bird`, etc.

**Free-standing viability**: `po` works naturally as an independent word. `La po es gud.` = "The person is good." `Un po veni.` = "A person comes." This is more natural than `er` as a free word.

**Phonotactics**: One syllable, vowel-final /po/ — fully (C)V compliant. The cleanest option phonotactically.

**International recognizability weakness**: `po` as abbreviation of "person" is not self-evident. English "person" begins with /pɜ/, Spanish "persona" with /pe/, French "personne" with /pɛ/. The /o/ vowel doesn't clearly point to "person" — it must be learned as an arbitrary root. But this is true of ALL VELA roots — `wot` for water, `mel` for melon. Arbitrariness is normal for roots.

**Semantic precision**: "Person" is broader than "professional." `lern-po` could mean "person who learns" (student), not just "person who teaches." This is a semantic narrowing problem, not a morphological one.

---

#### No suffix (context-only)

**Morphological type**: ZERO-DERIVATION (invisible conversion).

- This is the morphologically minimal option: 0 new morphemes, 0 new rules. The word `lern` means both "to learn" (verb) and "teacher" (noun), disambiguated by syntactic position and context.

**Morphological cost**: Zero on the surface. But conversion/zero-derivation IS a morphological operation — an invisible one.

**The ambiguity cost**:
- `La lern es gud.` = "The teacher is good" OR "The learning is good" OR "Learning is good."
- `Mi lern.` = "I learn" (verb, mi = subject pronoun) OR "My teacher" (if mi = possessive pronoun) — ambiguous parse.

VELA does not have a dedicated syntactic slot that distinguishes professions from actions. In Japanese, `sensei` (teacher) is unambiguous because it's ONLY a noun — it doesn't double as a verb. In VELA, `lern` is fundamentally a verb root. Repurposing it as a profession noun without marking is **conversion**, which is itself a morphological operation — just an invisible one.

**Morphological verdict**: Zero-derivation is still derivation. The learner must memorize that `lern` can be both V and N, and infer which reading applies from context. This is cognitively equivalent to learning a rule — just unmarked. Worse, it's a **lexically specific rule**: which words can double as professions? All actions? Only some? `-er` or `-po`, by contrast, is a **fully general rule**.

---

#### `-ist` / `-or` / `-isti`

**Morphological type**: DERIVATIONAL (bound suffixes).

- `-ist`: 1 syllable, ends in /t/ (ILLEGAL — obstruent coda). Must become `-isti` (2 syllables) for phonotactic compliance.
- `-or`: 1 syllable, ends in /r/ (legal). But carries Romance masculine connotation (`actor`, `doctor`, `professor`). Gender baggage.
- `-isti`: 2 syllables, vowel-final, phonotactically clean. But 2 syllables doubles the suffix length vs `-er` or `-po`.

**Morphological cost**: 1 new derivational rule each. `-isti` adds syllable weight to every profession.

**Verdict**: Inferior to `-er` or `-po` on all dimensions — longer, phonotactically problematic, gender-loaded, or heavier.

---

### Rule Count Analysis

| Candidate | New Roots | New Rules | Total | Syllable Weight |
|-----------|-----------|-----------|-------|-----------------|
| `-er` (as compound) | 1 (`er`="agent") | 0 | 1 | +1 |
| `-er` (as derivation) | 0 | 1 (V→N) | 1 | +1 |
| `-po` | 1 (`po`="person") | 0 | 1 | +1 |
| No suffix | 0 | 0 (+ conversion) | 0 (+ hidden) | +0 |
| `-isti` | 0 | 1 (V→N) | 1 | +2 |
| `-ist` | 0 | 1 | 1 | +1 (illegal coda) |
| `-or` | 0 | 1 | 1 | +1 |

---

### The Compounding-vs-Derivation Distinction (Critical Insight)

If VELA defines ANY of these as a **root** in the lexicon, it becomes compounding. If it defines them as a **suffix** (bound, cannot stand alone), it becomes derivation.

The morphological architecture is determined by the **lexical entry**, not by the surface form:

- If `er` = root `er | N | agent, doer` → `lern-er` is a compound (like `wot-mel`).
- If `po` = root `po | N | person, human` → `lern-po` is a compound.
- If `-er` = bound suffix `-er | N→N | agentive nominalizer` → derivation.

**Surface form alone does not determine morphological type.** Both `-er` and `-po` can be compounding — the difference is semantic transparency of the root:
- `po` = "person" — concrete, natural free-standing meaning.
- `er` = "agent/doer" — abstract, less natural as a free word.

---

### Learnability

**`-er`**: High for English speakers (native intuition). Medium for Romance speakers (recognizable from `-eur/-ero/-or`). Low for Sinophones/Japanophones — Chinese uses person-compounds: 老师 (old-master), not learn-er. `-er` is a piece of Indo-European morphological heritage. NOT universal.

**`-po`**: Neutral for everyone. No speaker group has native intuition for `po` = person. But the pattern (action + person) is cognitively transparent to ALL: Chinese 工人 = work-person. The concept is universal.

**No suffix**: Hardest. Every profession is a lexical exception to the verb-only reading. Which action words can mean professions? The learner memorizes a list.

---

### The Decisive Morphological Argument: Occam's Razor

In VELA, `po` would ALREADY need to exist as the word for "person" — it is a Tier 0 primitive (basic human terms cannot be compounded from simpler parts). So `-po` **adds zero new roots** — it REUSES an existing one in a compound slot.

`-er`, by contrast, introduces a brand-new root `er` = "agent" that serves no other purpose. It is a net addition to the lexicon.

**Net morphological cost**:
- `-po`: **0 new anything.** Reuses existing root `po` = person. Zero new rules.
- `-er`: **+1 new root** (`er` = agent) used ONLY in profession compounds. Zero new rules if analyzed as compounding; +1 rule if derivational.

This is the morphological version of Occam's razor: *do not multiply roots beyond necessity.*

---

### Morphologist's Formal Vote

**1st choice: `-po`** — Morphologically pure. Zero new roots, zero new rules, pure compounding, fully (C)V, one syllable, universally learnable.

**2nd choice: `-er`** — User preference, internationally recognizable in IE languages, one syllable, legal coda. Can be analyzed as compounding if `er` is defined as root "agent." Acceptable but introduces a new root.

**Rejected**: No suffix (hidden derivation cost, ambiguity), `-ist/-or/-isti` (phonotactics, gender baggage, syllable weight).

---

### Summary Table (All Issues)

| Issue | Morphological Risk | Recommended Reform |
|-------|--------------------|--------------------|
| 1 — Atomic threshold | HIGH | ~150 atoms max; compound rest after (C)V reform |
| 2 — PROFIL | HIGH | Keep `profil` = profile; "profit" → `gain` |
| 3 — SE collision | MEDIUM | Leave as-is (syntactic containment), OR change sea → `mar` |
| 4 — Numbers | CRITICAL | Already resolved: `kent` (100), `mil` (1000), rest decimal compounds |
| 5 — Profession suffix | DECISIONAL | **VOTE: `-po`** (1st), `-er` (2nd) |

**Meta-priority (all issues)**: Issue 4 (numbers) — RESOLVED > Issue 2 (profil) > Issue 1 (atoms) > Issue 5 (profession suffix — CURRENT) > Issue 3 (se).

---
*Morphologist — Standby Issues + Profession Suffix Deliberation*
*Focus: morphological economy, regularity, learnability, rule consistency, zero allomorphy*
