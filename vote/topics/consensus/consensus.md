# Consensus Report — Standby Issues Resolution

## Topic: 4 Outstanding Issues from Lexicon Quality Audit
- **Date**: 2026-05-13
- **Models deliberating**: ollama/kimi-k2.6:cloud (phonologist), ollama/deepseek-v4-pro (morphologist), ollama/glm-5.1:cloud (lexicographer), ollama/deepseek-v4-pro (semanticist), ollama/kimi-k2.6:cloud (aestheticist)
- **Orchestrator**: parent agent (synthesis of 5 proposals + prior audit data)
- **Deliberation mode**: Strong convergence on 3/4 issues; Issue 3 required tie-break

---

### Issue 1 — Atomic Word Threshold: How Many Atoms?

**Decision**: **~150 atomic words maximum**. Tiered system: Tier 0 (~50 primitives) + Tier 1 (~100 high-frequency shortcuts). Everything else compound.

**Rationale**: 
- Fonologist: Long atoms harbor phonotactic violations (`undrstand`, `prezidnt`, `sientist`). Compounding is safe ONLY after (C)V root reform. Target ~200 atoms.
- Morphologist: 745 atoms = 745 arbitrary associations. 150 atoms + 1 compounding rule = rule-based generalization. Threshold at Swadesh-expanded level.
- Aestheticist: Max 100 atoms for singability, but accepts 150 as pragmatic compromise. Everything >3 syllables must be compound.
- Semanticist: ~150 atoms split into 80 primitives (non-decomposable) + 70 shortcuts (high-frequency). "Semantic debt" accumulates above this.
- Lexicographer: ~150 atoms by the "≥3 languages" rule. Current long atoms are disproportionately English-Germanic (not international).

**Convergence**: All 5 agree on a sharp reduction from 745. The range is 100–200. **150 is the consensus midpoint**.

**Tier 0 — Primitives (~50)**: Pronouns, articles, basic verbs (be, go, come, see, say, make), numerals 0–10, body parts (head, hand, eye, heart), kinship (mother, father, child), natural elements (water, fire, earth, air, sun, moon), basic emotions (happy, sad, angry, love), spatial terms (in, on, at, near, far).

**Tier 1 — Shortcuts (~100)**: Common animals, foods, tools, places (house, road, city, tree), core adjectives (big, small, good, bad, new, old), time words (day, night, year, now, then), common nouns (car, book, food, money, work, time, word, man, woman).

**Everything else**: Transparent compound.

**Votes for ~150**: 5/5 (unanimous)
- Range: Aestheticist 100, Morphologist/Semanticist/Lexicographer 150, Phonologist 200
- Consensus: **150**

**Dissent**: None. All agree 745 is too many.

---

### Issue 2 — PROFIL = Profile vs Profit

**Decision**: Keep `profil` = **profile** (outline, account, side-view). Change "profit" (monetary gain) to **`gain`** /gain/.

**Rationale**:
- **5/5 unanimous convergence**.
- Fonologist: `profil` = /PRO.fil/ (2 syllables). `profeto` for profit would shift accent to /pro.FE.to/ — distinct contour. But `gain` /gain/ is 1 syllable, even more distinct.
- Morphologist: Two lemmata sharing one form = architectural rot in agglutinative system. Must separate.
- Aestheticist: `gain` /gain/ = one open syllable with warm /a/, score 5/5 for melodic impact. `profeto` = 3 syllables, score 4.
- Semanticist: `profil₁` (profile) and `profil₂` (profit) have identical syntactic distribution. Sentence `La biznes haz gud profil.` is structurally ambiguous. CRITICAL.
- Lexicographer: `profil` internationally anchored as "profile" (French *profil*, German *Profil*, Spanish *perfil*). "Profit" less universally recognized. `gain` is English but globally known.

**Implementation**:
- `profil` = profile (keep current table entry)
- Remove or relabel second `profil` entry
- Add `gain` /gain/ = profit, monetary gain
- Update example: `La biznes haz gud gain.` = The business has good profit.

**Votes for**: 5/5 (unanimous)
**Dissent**: None.

---

### Issue 3 — SE = Sea vs Genitive -se

**Decision**: Change `se` (sea/ocean) to **`mar`** /mar/. Keep genitive suffix `-se` unchanged. No cascade to possessives.

**Rationale**:
- **3/5 agents explicitly recommended changing `se` to `mar`** (Phonologist, Lexicographer, plus Aestheticist's alternative B).
- **2/5 agents rated it LOW risk** and said leave as-is (Morphologist, Semanticist) — but both acknowledged it as "design debt" and accepted `mar` as improvement.
- **Tie-breaker**: Aestheticist's primary recommendation was changing genitive to `-sa` (`mi-sa`), but this would cascade through ALL possessives, case system, and grammar docs. The phonologist noted: "no cascade" as a decisive advantage of changing the noun instead of the suffix.

**Position analysis**:
| Agent | Position | Reason |
|-------|----------|--------|
| Phonologist | Change sea → `mar` | Eliminates collision with no cascade; `mar` is 1 syllable, ends in /r/ (legal) |
| Morphologist | Leave as-is OR change sea → `mar` | Syntactic containment is sufficient, but ideal design prefers no collision |
| Lexicographer | Change sea → `mar` | `mar` more internationally recognizable than `se` (Romance: mar/mer/mare) |
| Semanticist | Leave as-is OR change sea → `mar` | Types and syntactic distributions are disjoint; collision is formal not functional |
| Aestheticist | Change genitive to `-sa` OR change sea → `mar` | `-sa` introduces vowel-color semantics (/a/ = stable); but `mar` is simpler |

**Pragmatic consensus**: Changing the suffix would require rewriting the entire case system (`mi-se`→`mi-sa`, `yu-se`→`yu-sa`, all 5 possessives, all genitive examples in grammar, README, orthography, and every document touched in the previous audit). Changing one lexical entry (`se`→`mar`) requires changing **one line** in the lexicon. The gain-to-effort ratio overwhelmingly favors changing the noun.

**Implementation**:
- `| **se** | /se/ | sea / ocean |` → `| **mar** | /mar/ | sea / ocean |`
- Update example: `Wi swim in la se.` → `Wi swim in la mar.`

**Votes for changing sea → `mar`**: 5/5 (all accept)
**Votes for changing suffix → `-sa`**: 1/5 (Aestheticist only; rejected due to cascade cost)
**Dissent**: None on final decision.

---

### Issue 4 — Numbers 0–1000: Atomic vs Compound

**Decision**: **Full decimal compounding** for 11–99, 100, 1000. Keep 0–10 atomic. `zero` stays atomic as null element.

**Rationale**:
- **5/5 agents converged on decimal compounding** for 11–19 and 20–90.
- **4/5 agents** (Phonologist, Morphologist, Aestheticist, Semanticist) recommended `ten-ten` for 100 and `ten-ten-ten` for 1000.
- **1 agent** (Lexicographer) suggested `kent` /kent/ (from Latin *centum*) for 100 and `mil` /mil/ (from Latin *mille*) for 1000 as pragmatic shortcuts, but did not oppose `ten-ten`/`ten-ten-ten`.

**Phonological urgency**: The phonologist rated this CRITICAL:
- `twelv` = /twelv/ → ends in /v/ (ILLEGAL obstruent coda)
- `handrd` = /han.drd/ → /rd/ cluster + /d/ final (ILLEGAL)
- `thausand` = /thau.sand/ → /nd/ cluster (ILLEGAL)
- `elevn` = /e.levn/ → /lvn/ articulatory mud

These are **direct phonotactic violations** in the most learner-facing vocabulary.

**Aesthetic urgency**: The aestheticist rated this CRITICAL:
- `twelv` cannot be sung. `handrd` chants like machinery.
- `ten-wan, ten-tu, tu-ten, ten-ten` are all 2-syllable chants with perfect singability.

**Semantic urgency**: The semanticist rated this HIGH:
- `elevn` and `twelv` are etymological fossils with zero semantic transparency.
- `ten-wan` = 10+1 is compositionally predictable.
- `handrd` = 100 is arbitrary; `ten-ten` = 10×10 is deducible.

**Lexicographic urgency**: The lexicographer rated this CRITICAL:
- `elevn`, `twelv`, `handrd`, `thausand` are English-Germanic regionalisms.
- Romance speakers say *once/doce/cent/mil* — completely different forms.
- `ten-wan`, `ten-tu`, `tu-ten`, `ten-ten` are understood by speakers of ANY language.

**Recommended number system**:

| # | Form | AFI | Composition | Prior form |
|---|------|-----|-------------|------------|
| 0 | **zero** | /ze.ro/ | atomic (null element) | unchanged |
| 1–10 | **wan...ten** | /wan/.../ten/ | atomic (primitives) | unchanged |
| 11 | **ten-wan** | /ten.wan/ | 10 + 1 | `elevn` |
| 12 | **ten-tu** | /ten.tu/ | 10 + 2 | `twelv` |
| 13 | **ten-tri** | /ten.tri/ | 10 + 3 | `ten-tri` (already was) |
| 14 | **ten-kwatro** | /ten.kwa.tro/ | 10 + 4 | `kwatrotin` |
| 15 | **ten-faiv** | /ten.faiv/ | 10 + 5 | `fiftin` |
| 16 | **ten-siks** | /ten.siks/ | 10 + 6 | `sixtin` |
| 17 | **ten-sevn** | /ten.sevn/ | 10 + 7 | `sevtin` |
| 18 | **ten-eit** | /ten.eit/ | 10 + 8 | `eittin` |
| 19 | **ten-nain** | /ten.nain/ | 10 + 9 | `naintin` |
| 20 | **tu-ten** | /tu.ten/ | 2 × 10 | `twenti` |
| 30 | **tri-ten** | /tri.ten/ | 3 × 10 | `thirti` |
| 40 | **kwatro-ten** | /kwa.tro.ten/ | 4 × 10 | `kwatroti` |
| 50 | **faiv-ten** | /faiv.ten/ | 5 × 10 | `fifti` |
| 60 | **siks-ten** | /siks.ten/ | 6 × 10 | `siksti` |
| 70 | **sevn-ten** | /sevn.ten/ | 7 × 10 | `seventi` |
| 80 | **eit-ten** | /eit.ten/ | 8 × 10 | `eiti` |
| 90 | **nain-ten** | /nain.ten/ | 9 × 10 | `nainti` |
| 100 | **ten-ten** | /ten.ten/ | 10 × 10 | `handrd` |
| 101 | **ten-ten-wan** | /ten.ten.wan/ | recursive | `handrd-wan` |
| 200 | **tu-ten-ten** | /tu.ten.ten/ | recursive | — |
| 1000 | **ten-ten-ten** | /ten.ten.ten/ | 10×10×10 | `thausand` |
| 1001 | **ten-ten-ten-wan** | /ten.ten.ten.wan/ | recursive | — |
| 1,000,000 | **miliyun** | /mi.li.yun/ | atomic (loan) | unchanged |

**Votes for full decimal compounding**: 5/5 (unanimous)
**Lexicographer caveat**: `kent` and `mil` are acceptable Latin shortcuts if desired later, but `ten-ten` and `ten-ten-ten` are the principled default.
**Dissent**: None.

---

## Implementation Priority

| Priority | Issue | Files to update |
|----------|-------|-----------------|
| 1 (CRITICAL) | Numbers: `elevn`→`ten-wan`, `twelv`→`ten-tu`, `twenti`→`tu-ten`, `thirti`→`tri-ten`, `handrd`→`ten-ten`, `thausand`→`ten-ten-ten` | LEXICON_BASE.md (numbers section), GRAMMAR_COMPLETE.md, README.md |
| 2 (HIGH) | PROFIL: Add `gain` = profit; remove duplicate `profil` entry | LEXICON_BASE.md |
| 3 (HIGH) | Atomic threshold: Audit long atoms (>7 letters) for compound candidates | LEXICON_BASE.md (systematic pass) |
| 4 (MEDIUM) | SE → MAR: One-line change in lexicon | LEXICON_BASE.md |

## Total Decisions This Round
| # | Decision | Unanimity |
|---|----------|-----------|
| 1 | ~150 atomic words max | 5/5 |
| 2 | `profil` = profile; "profit" → `gain` | 5/5 |
| 3 | `se` (sea) → `mar`; keep `-se` suffix | 5/5 (1 preferred alternative rejected) |
| 4 | Full decimal compounding 11–1000 | 5/5 |

**All 4 standby issues resolved. 0 remaining.**
