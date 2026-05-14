# Proposal — VELA Lexicographer (ollama/glm-5.1:cloud)
## Standby Issues Deliberation — Lexicographic Analysis

---

## ISSUE 1: Atomic Word Threshold (745 atoms, 35 compounds)

### Lexicographic Assessment: HIGH

**Vocabulary Source Rules applied**:
1. International roots first
2. Recognizable Latin roots
3. Shorter = better
4. Compound over complex
5. Not just English phonetic respelling

**Current violation**: 745 atoms means Rule 4 (compound over complex) is almost entirely ignored. The lexicon is a list, not a system.

**International recognizability analysis of long atoms**:

| Word | English | Spanish | French | German | Mandarin | Japanese | Verdict |
|------|---------|---------|--------|--------|----------|----------|---------|
| `prezidnt` | president | presidente | président | Präsident | 总统 | 大統領 | Internationally recognizable BUT 9 letters |
| `sientist` | scientist | científico | scientifique | Wissenschaftler | 科学家 | 科学者 | Latin *scientia* recognizable; German form very different |
| `aereplan` | airplane | avión | avion | Flugzeug | 飞机 | 飛行機 | English + Latin blend; not recognizable to Romanophones |
| `vokabulari` | vocabulary | vocabulario | vocabulaire | Wortschatz | 词汇 | 語彙 | Latin *vocabularium* — recognizable to all Romance speakers |
| `buterflai` | butterfly | mariposa | papillon | Schmetterling | 蝴蝶 | 蝶 | English-only; completely opaque to all others |
| `watrmeln` | watermelon | sandía | pastèque | Wassermelone | 西瓜 | スイカ | English compound already; not international |
| `elevn` | eleven | once | onze | elf | 十一 | 十一 | English-Germanic fossil; opaque to Romance |
| `twelv` | twelve | doce | douze | zwölf | 十二 | 十二 | English-Germanic fossil; opaque to Romance |
| `handrd` | hundred | cien | cent | hundert | 一百 | 百 | English-Germanic; Romance has *cent* |
| `thausand` | thousand | mil | mille | tausend | 一千 | 千 | English-Germanic; Romance has *mil* |

**Key insight**: The longest atomic words are disproportionately English-Germanic borrowings. Romanophones, Sinophones, and Japanese speakers do NOT recognize `elevn`, `twelv`, `handrd`, `thausand`. These are not "international" — they are Anglo-Germanic regionalisms.

**The compound alternative**:
- `ten-wan` = transparent to ALL speakers (everyone knows "ten" and "one")
- `ten-ten` = transparent to ALL speakers
- `tu-ten` = transparent to ALL speakers
- `biju-fle` = less transparent ("biju" is VELA-specific), but deducible

**Threshold recommendation**: **~150 atomic words**.
- Keep atoms only if they appear in ≥3 of the top 6 source languages (English, Spanish, French, German, Mandarin, Japanese) with similar form.
- This captures: pronouns, numerals 0–10, basic verbs, body parts, kinship, natural elements, core spatial terms.
- Everything else: compound or borrow from Latin.

**Specific reforms for long atoms**:
- `prezidnt` → `hed-man` (shorter, transparent) or keep if Latin `prezidenti` is preferred
- `sientist` → `siens-man` (science-man)
- `aereplan` → `sky-bird` or `fly-thing`
- `vokabulari` → `word-list` (5+5=10 letters, but 2 roots)
- `buterflai` → `biju-fle` (VELA-specific but transparent)
- `watrmeln` → `wot-mel` (transparent compound)

**Rating**: HIGH. The current atomic lexicon over-represents English and under-represents the compounding strategy.

---

## ISSUE 2: PROFIL Homonymy

### Lexicographic Assessment: HIGH

**Etymology**:
- `profil` (profile) ← Italian *profilo* ← Latin *profilum* — "drawn in outline"
- `profil` (profit) ← Latin *profectus* — "advance, progress, profit"

Both are Latin-derived, which satisfies Rule 2. But the collision violates Rule 3 (shorter=better) in a different way: one form serving two meanings is cognitively "longer" — the learner must carry extra context to disambiguate.

**International recognizability**:
- *profil* = profile: French *profil*, German *Profil*, Spanish *perfil*, Italian *profilo* — widely recognized
- *profectus/profit*: English *profit*, French *profit*, Spanish *provecho/profit* (archaic), Italian *profitto* — less universally recognized than *profil*

**Decision**: `profil` is more internationally anchored as "profile". "Profit" should take a different form.

**Options for "profit"**:
- `gain` — English-only, 1 syllable, very common
- `win` — English-only, but also means "victory" — ambiguous
- `profeto` — from Latin *profectus*, 3 syllables, Romance-recognizable
- `lukro` — from Latin *lucrum*, 2 syllables, Romance-recognizable (*lucro* in Spanish/Italian)

**Recommendation**: `gain` for basic vocabulary (shorter, universally known from English). `profeto` or `lukro` for advanced/formal contexts.

**Rating**: HIGH. Straightforward fix with clear lexical priority.

---

## ISSUE 3: SE Noun vs SE Suffix

### Lexicographic Assessment: LOW

**"Sea" in major languages**:
- English: sea
- Spanish: mar
- French: mer
- German: Meer/See
- Mandarin: 海 (hǎi)
- Japanese: 海 (umi)

**"Mar" recognizability**:
- Spanish *mar*, French *mer*, Italian *mare*, Portuguese *mar*, Romanian *mare* — all Romance
- English "marine", "maritime", "submarine" — indirect recognition
- German *Meer* — related

**"Oce" recognizability**:
- English *ocean*, Spanish *océano*, French *océan*, Italian *oceano* — less direct as a standalone word

**"Wot-bodi" (water-body)**: Transparent but 3 syllables + hyphen. Not shorter.

**Genitive suffix `-se`**: Already established in 5 possessives (`mi-se, yu-se, li-se, wi-se, de-se`) and productive in genitive NPs. Changing it would require updating the entire case system.

**Recommendation**: Change "sea" to `mar` /mar/. Reasons:
1. Internationally more recognizable than `se` (which is English-only)
2. One syllable, ends in /r/ (legal coda)
3. Eliminates collision with genitive suffix — no cascade
4. Romance-preferred, aligns with VELA's Latin priority

**Rating**: LOW. Easy fix, improves international neutrality.

---

## ISSUE 4: Numbers 0–1000

### Lexicographic Assessment: CRITICAL

**Current system — international recognizability score**:

| Number | VELA | English | Spanish | French | German | Mandarin | Japanese | Recognition |
|--------|------|---------|---------|--------|--------|----------|----------|-------------|
| 11 | `elevn` | eleven | once | onze | elf | 十一 | 十一 | English-Germanic only |
| 12 | `twelv` | twelve | doce | douze | zwölf | 十二 | 十二 | English-Germanic only |
| 20 | `twenti` | twenty | veinte | vingt | zwanzig | 二十 | 二十 | English only |
| 30 | `thirti` | thirty | treinta | trente | dreißig | 三十 | 三十 | English only |
| 100 | `handrd` | hundred | cien | cent | hundert | 一百 | 百 | English-Germanic only |
| 1000 | `thausand` | thousand | mil | mille | tausend | 一千 | 千 | English-Germanic only |

**The 11–12 problem**: These are the ONLY numbers in the 1–100 range that are opaque. Every other language group has its own opaque forms (Spanish *once, doce*; French *onze, douze*; German *elf, zwölf*), but they are NOT shared. There is NO international form for 11 and 12. They are etymological fossils in every language.

**The compound solution**:
- `ten-wan` — every speaker of every language understands "ten" and "one"
- `ten-tu` — every speaker understands "ten" and "two"
- `tu-ten` — every speaker understands "two" and "ten"
- `ten-ten` — every speaker understands "ten" and "ten"

This is the **Chinese/Japanese model**, and it is the ONLY model that is transparent across all language families.

**The 100/1000 problem**: `handrd` and `thausand` are English-Germanic regionalisms. Romance speakers say *cien/cient* and *mil/mille*. A VELA form should not privilege English.

**Options**:
- `ten-ten` = 100 — fully transparent, deducible
- `han` /han/ = 100 — trimmed from *hundred*, 1 syllable, still English-Germanic
- `kent` /kent/ — from Latin *centum* (Spanish *cien/ciento*, French *cent*, Italian *cento*) — 1 syllable, Romance-preferred

**For 1000**:
- `ten-ten-ten` = 1000 — transparent but 3 syllables
- `mil` /mil/ — from Latin/Romance *mil/mille* — 1 syllable, internationally recognized
- `tau` /tau/ — trimmed from *thousand* — English-only

**Lexicographer's compromise**:
- 11–19: `ten-wan, ten-tu, ten-tri...` (fully transparent)
- 20–90: `tu-ten, tri-ten, kwatro-ten...` (fully transparent)
- 100: `ten-ten` (transparent) OR `kent` (Latin, 1 syllable, internationally recognizable)
- 1000: `ten-ten-ten` (transparent) OR `mil` (Latin, 1 syllable, internationally recognizable)
- 1,000,000: `miliyun` (keep — internationally recognized, vowel-final)

**Why allow `kent` or `mil`?** Because 100 and 1000 are **milestone numbers**. They appear in currency, dates, and formal contexts where a short atomic form is pragmatically useful. Chinese uses 百 (bǎi) and 千 (qiān) — atomic — while compounding 21, 43, etc. VELA can follow this hybrid model.

**Rating**: CRITICAL. The number system currently privileges English-Germanic forms over Latin and transparency. This undermines VELA's international neutrality.

---

## Summary Table

| Issue | Lexicographic Risk | Recommended Reform |
|-------|--------------------|--------------------|
| 1 — Atomic threshold | HIGH | ~150 atoms max; compound rest; prioritize Latin/transparent roots |
| 2 — PROFIL | HIGH | Keep `profil` = profile; "profit" → `gain` |
| 3 — SE collision | LOW | Change "sea" → `mar` (Romance-preferred, 1 syllable) |
| 4 — Numbers | CRITICAL | 11–19 → `ten-wan...`; 20–90 → `tu-ten...`; 100→`ten-ten` or `kent`; 1000→`mil` or `ten-ten-ten` |

**Meta-priority**: Issue 4 (numbers) > Issue 1 (atoms) > Issue 2 (profil) > Issue 3 (se).

---
*Lexicographer — Standby Issues Deliberation*
*Focus: international recognizability, Latin roots, Rule 3 (shorter=better), Rule 4 (compound over complex), Rule 5 (not English-only)*

---

## ISSUE 5: Profession Suffix

### Lexicographic Assessment: HIGH

**Question**: What suffix should VELA use to derive "one who does X" from a verb or noun root?

---

### Candidate Evaluation Against VELA's 5 Rules

#### `-er` (User's preference)

| Rule | Score | Analysis |
|------|-------|----------|
| 1 — International roots | ★★★☆☆ | Germanic (English, German, Dutch, Swedish `-are`). Phonological cousin of Romance `-eur/-ero/-ore`. The /r/ is pan-European, but the vowel `-e-` is specifically Germanic. |
| 2 — Recognizable Latin | ★★☆☆☆ | Not Latin. Latin used `-tor/or`. But traceable via Grimm's Law to same PIE *-ter- agentive. Distantly related, not directly recognizable. |
| 3 — Shorter = better | ★★★★★ | 1 syllable, 2 letters. Optimal. |
| 4 — Compound over complex | ★★★★★ | Most productive agentive suffix in the languages that use it. `work` + `er` = `worker`. Transparent. |
| 5 — Not just English | ★★★★☆ | Not *just* English — also German (`Lehrer`, `Arbeiter`, `Sänger`, `Bäcker`), Dutch, Swedish. But NOT Romance, NOT Slavic, NOT Sino-Tibetan. |

**Key argument for**: The /r/-based agentive is the most widespread profession-derivation strategy in Europe. While the exact form `-er` is Germanic, it participates in a pan-European pattern:

| Language | Agentive suffix | Example ("worker") |
|----------|----------------|---------------------|
| English | -er | worker |
| German | -er | Arbeiter |
| Dutch | -er | werker |
| Swedish | -are | arbetare |
| French | -eur | travailleur |
| Spanish | -ero/-dor | trabajador |
| Italian | -tore/-ere | lavoratore |
| Portuguese | -or/-eiro | trabalhador |
| Latin | -tor | laborator |

Every major European language group uses an **/r/-based** agentive. The vowel varies, but the /r/ is constant. `-er` is simply the Germanic representative of this pan-European pattern, and choosing the Germanic form gives us the shortest possible vowel (schwa /ə/ → written `e`).

**Key argument against (Rule 5)**: A Romance speaker seeing `worker` will recognize the English word, not the broader pattern. Is `-er` just an English loan in disguise? **No** — because German, Dutch, and Scandinavian languages use the identical suffix productively, not as loans. It is a genuinely shared Germanic morpheme.

---

#### `-ist`

| Rule | Score | Analysis |
|------|-------|----------|
| 1 — International roots | ★★★★★ | Pan-European: English, French `-iste`, Spanish `-ista`, Italian `-ista`, German `-ist`, Russian `-ист`, Portuguese `-ista`, Dutch `-ist`. |
| 2 — Recognizable Latin | ★★★★☆ | From Greek `-istēs` via Latin `-ista`. Directly recognizable Latin/Greek heritage. |
| 3 — Shorter = better | ★★★☆☆ | 2 syllables, 3 letters. Violates Rule 3 relative to `-er`. |
| 4 — Compound over complex | ★★★☆☆ | Productive, but semantically NARROWER. `-ist` means "devoted to X" or "practitioner of X-ism", not "one who does X action". You say *artist*, not *paintist*; *scientist*, not *studyist*. |
| 5 — Not just English | ★★★★★ | Genuinely international. No single language owns this form. |

**Critical semantic problem**: `-ist` and `-er` occupy **different semantic slots**:

| Suffix | Input | Output | Meaning |
|--------|-------|--------|---------|
| `-er` | Verb root | One who does the action | `teach` → `teacher`, `work` → `worker`, `sing` → `singer` |
| `-ist` | Noun root | One devoted to the field | `art` → `artist`, `science` → `scientist`, `piano` → `pianist` |

You cannot swap them: ✗ `teachist`, ✗ `workerist`, ✗ `singist`, ✗ `art-er`. They are **not interchangeable**. `-er` is an agentive (doer of action); `-ist` is a specialist (devoted to a field).

---

#### `-po` (from *persona*)

| Rule | Score | Analysis |
|------|-------|----------|
| 1 — International roots | ★★☆☆☆ | The ROOT *persona* is international. But the SUFFIX `-po` is invented. |
| 2 — Recognizable Latin | ★★★☆☆ | From Latin *persona* — yes, recognizable root. |
| 3 — Shorter = better | ★★★★☆ | 1 syllable, 2 letters. Short. |
| 4 — Compound over complex | ★★☆☆☆ | Not attested as a productive suffix in ANY natural language. *Person* is a noun, not a derivational morpheme. |
| 5 — Not just English | ★★★★☆ | Not English-centric. But also not ANY-language-centric — because no language uses this. |

**Fatal flaw**: VELA Rule 4 prefers compounding patterns that exist in natural languages. `-po` is an **invention**, not a pattern. Learners would have no cross-linguistic intuition for `teach-po` = teacher. This violates the spirit of international recognizability.

---

#### No suffix (atomic profession words)

| Rule | Score | Analysis |
|------|-------|----------|
| 1 — International roots | ✗ | Each word would need individual etymological vetting. No systematic pattern. |
| 2 — Recognizable Latin | ★★★☆☆ | Possible for `doktor` (Latin *doctor*), but most professions lack shared international forms. |
| 3 — Shorter = better | ★★★★★ | 0 suffix = shortest. But the burden shifts to memorizing 50+ atomic profession words. |
| 4 — Compound over complex | ✗ | Fundamental violation. No derivational system. |
| 5 — Not just English | ✗ | Without a system, individual words default to the creator's language — bias risk. |

**Fatal flaw**: Violates Rule 4 entirely. A language that requires memorizing `techer`, `worker`, `singer`, `driver` as unrelated atoms loses the productivity gain that makes compounding powerful. Some atomic profession words are acceptable (see below), but the system needs a **productive agentive suffix**.

---

### Deeper Analysis: Is `-er` Too English-Centric?

**The case against (Rule 5 objection)**:
- Romance speakers hear `-er` and think "English word" — not a familiar pattern
- It privileges Germanic languages over Romance, Asian, and other families
- A truly international language should not default to the world's dominant language's morphemes

**The case for**:
1. `-er` is **not English-only** — German (*Lehrer, Arbeiter, Sänger, Bäcker*), Dutch (*werker*), Swedish (*arbetare*) all use it **productively**. It is a **Germanic** morpheme, not an English one.
2. The /r/-agentive is **pan-European** — Romance `-eur/-ero/-ore`, Slavic `-тель/-arz`, even Celtic languages have /r/ agentives. `-er` is the phonologically simplest representative of this universal pattern.
3. **Shortness matters for adoption**. Rule 3 is not arbitrary — shorter morphemes are easier to learn, say, and type. `-er` /ər/ is the shortest possible form of the /r/-agentive.
4. **Productivity over provenance**. The whole point of a suffix is to let learners derive new words. `-er` is the most productive and transparent agentive available: `VERB + er = one who VERBS`. This is more rule-regular than any Romance form.

**Rule 5 verdict**: `-er` is not "just English" — it is the **Germanic** member of a **pan-European** agentive family. It satisfies Rule 5 because it is genuinely shared across multiple major languages, not a monolingual export. The fact that it coincides with English is an advantage (English is the most widely learned L2 globally), not disqualifying.

---

### Should Some Profession Words Remain Atomic?

**Yes.** Profession words that are **internationally recognized as atomic Latin forms** should stay atomic:

| Atomic word | Latin root | Languages where recognizable |
|-------------|------------|------------------------------|
| `doktor` | *doctor* | English, French, German, Spanish, Italian, Portuguese, Dutch, Swedish, Russian — virtually universal |
| `artis` | *artifex*? | Weak — not widely shared as a single form. Better: `art-ist` |
| `gida` | *guida*? | Weak — not universal. Better: `gid-er` (one who guides) |

**Principle**: An atomic profession word is justified only if the SAME Latin form is recognizable across ≥4 of the 6 source languages (English, Spanish, French, German, Mandarin, Japanese). `doktor` passes. Most others don't.

---

### Recommendation

## ★ RECOMMENDED: `-er` as the primary agentive suffix

**With `-ist` as a secondary specialist suffix, and select atomic words for widely-recognized Latin forms.**

### The dual-suffix system:

| Suffix | Function | Input | Example |
|--------|----------|-------|----------|
| `-er` | Agentive (doer of action) | Verb root | `work-er`, `teach-er`, `sing-er`, `bak-er`, `driv-er` |
| `-ist` | Specialist (devoted to field) | Noun root | `siens-ist`, `art-ist`, `piyan-ist`, `dent-ist` |
| *(atomic)* | Internationally recognized profession | — | `doktor` |

### Why this works:

1. **`-er` handles the productive case** — turning any verb into "one who does this". This is the most common derivation need. Short, transparent, genuinely Germanic (not just English).

2. **`-ist` handles the specialist case** — for professions defined by their domain, not their action. Internationally recognized, genuinely pan-European.

3. **Atomic forms handle the fossil case** — for professions so universal that every language borrows the same Latin root.

4. **This mirrors natural language**: Even English uses both (`worker` vs `artist` vs `doctor`). Even Spanish uses both (`trabajador` vs `artista` vs `doctor`). Even German uses both (`Arbeiter` vs `Künstler` vs `Doktor`). The dual system is **not an invention** — it's how natural languages already work.

### Examples:

| VELA verb | + `-er` | | VELA noun | + `-ist` | | Atomic |
|-----------|---------|-|------------|----------|-|---------|
| `work` | `worker` | | `siens` | `siensist` | | `doktor` |
| `teach` | `techer` | | `art` | `artist` | | |
| `sing` | `singer` | | `muzik` | `muzikist` | | |
| `bake` | `baker` | | `dent` | `dentist` | | |
| `drive` | `driver` | | | | | |
| `farm` | `farmer` | | | | | |
| `fish` | `fisher` | | | | | |
| `write` | `writer` | | | | | |

**Boundary rule**: If the root is a **verb** (an action), use `-er`. If the root is a **noun** (a field/domain), use `-ist`. When in doubt, `-er` is the default.

---

### Alternative considered and rejected: `-or`

| Form | Languages | Productive? | Short? |
|------|-----------|-------------|--------|
| `-or` | Latin, Spanish, Portuguese | Only for Latinate borrowings | 1 syllable |

`-or` is more internationally recognizable than `-er` for **existing** Latinate words (`doctor`, `actor`, `motor`), but it is **not productive** in any modern language for new coinages. You cannot say `teach-or` or `work-or` in any natural language. `-er` is the productive form. Existing Latinate `-or` words should be kept as atomics (like `doktor`).

---

### Rule compliance summary:

| Rule | `-er` (primary) | `-ist` (secondary) | Atomic (exception) |
|------|----------------|---------------------|--------------------|
| 1 — International | Germanic + pan-/r/ pattern | Pan-European (all families) | Latin (widely borrowed) |
| 2 — Latin | Indirect (PIE *-ter-) | Direct (Greek -istēs → Latin -ista) | Direct |
| 3 — Short | 1 syllable ✓ | 2 syllables (acceptable for secondary) | Varies |
| 4 — Compound | Most productive ✓ | Productive for specialists | Exception only |
| 5 — Not English-only | Germanic (shared) ✓ | Pan-European ✓ | Latin ✓ |

**Rating**: HIGH. The profession suffix question is foundational — it determines whether VELA can productively generate profession vocabulary or must memorize hundreds of atoms. The `-er`/`-ist` dual system is the only option that satisfies all 5 rules while maintaining semantic clarity and natural-language parallels.

---

*Lexicographer — Standby Issues Deliberation + Profession Suffix*
*Focus: international recognizability, Latin roots, Rule 3 (shorter=better), Rule 4 (compound over complex), Rule 5 (not English-only)*
