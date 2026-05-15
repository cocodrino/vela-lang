# VELA Text Benchmark — Foundational Translation

**Date:** 2026-05-14
**Status:** Phase 8 — Textos y Muestras
**Purpose:** Validate ~1100-word lexicon and grammar in real sentences. Expose gaps.

---

## 1. Primary Benchmark Text

### Source (English)
> "Go forth in peace to love and serve the Lord."

### VELA Translation
> **"Go forti in pasi tu luv and servi la Lord."**

Or in standard VELA orthography with pitch accent marking:
> **Go fórti in pasi tu luv and servi la Lòrd.**

---

## 2. Gap Analysis — Words Discovered Missing

| English | VELA | Status | Etymology Decision | Rationale |
|---------|------|--------|-------------------|-----------|
| forth | **forti** | NEW | English "forth" + vowel | Directional adverb. Pattern: ap, daun, forti |
| peace | **pasi** | NEW | Latin *pax* | Abstract concept → Latin per Q4 hybrid policy. Replaces rejected `pis` |
| serve | **servi** | NEW | Latin *servire* | Abstract/institutional verb → Latin per Q4 |
| Lord | **Lord** | NEW | Proper noun | Name of deity → capitalized per orthography rule |

**Total new words required for benchmark:** 4

---

## 3. Grammatical Decisions Forced by This Text

### 3.1 Imperative Mood
**Decision:** Imperative = bare verb root (no suffix).
- "Go" = **Go** (not "Go-a" or "Go-ed")
- This follows natural imperative patterns (English "Go!", Spanish "¡Ve!")
- Confirmation: VELA core verbs already use bare root for commands: "Kom!" "Si!"

### 3.2 Directional Adverbs
**Decision:** Directional adverbs are atomic words, NOT compounds.
- `ap` = up, `daun` = down, `lefa` = left, `raia` = right
- `forti` = forth/forward (new)
- Rationale: These are fundamental spatial primitives. The user rejected descriptive compounds (yel-kat = lion). Directionals are similarly primitive.

### 3.3 Abstract Preposition "in"
**Decision:** `in` = locative preposition for abstract states.
- "in peace" = **in pasi**
- Alternative considered: `pasi-to` (locative suffix). Rejected: abstract states use bare adjective (already decided in earlier phase).
- Confirmed: `in` + abstract noun = abstract location.

### 3.4 Infinitive Marker
**Decision:** `tu` = infinitive marker ("to" in English).
- "to love" = **tu luv**
- "to serve" = **tu servi**
- This is distinct from preposition `tu` (direction: "go tu hous"). Context disambiguates.
- Rationale: VELA avoids polysemy where possible, but `tu` as infinitive marker is globally recognizable (English "to", Romance infinitives).

### 3.5 Proper Nouns — Capitalization
**Decision:** Proper nouns = first letter UPPERCASE.
- "the Lord" = **la Lord**
- Confirmed by orthography rule: "Mayúsculas — solo oración + nombres propios"
- Religious titles as proper names: Lord, God (if added later), Buddha, Allah.

### 3.6 Serial Verbs / Infinitive Chains
**Decision:** Multiple infinitives joined by `and`.
- "to love and serve" = **tu luv and servi**
- The infinitive marker `tu` scopes over both verbs (distributed).
- Alternative: "tu luv and tu servi" — rejected as redundant. Natural languages distribute: "I want to eat and drink" = one "to".

---

## 4. Phonotactic Validation

| Word | Syllables | (C)V Check | Status |
|------|-----------|------------|--------|
| Go | /go/ | (C)V | ✅ |
| forti | /for.ti/ | (C)V.(C)V | ✅ |
| in | /in/ | (C)V | ✅ |
| pasi | /pa.si/ | (C)V.(C)V | ✅ |
| tu | /tu/ | (C)V | ✅ |
| luv | /luv/ | (C)V | ✅ |
| and | /and/ → /a.nu/? | (C)V(C) — WAIT | ⚠️ FLAG |
| servi | /ser.vi/ | (C)V.(C)V | ✅ |
| la | /la/ | V | ✅ |
| Lord | /lord/ → /lor.du/? | (C)V(C) — FLAG | ⚠️ FLAG |

**Flags:**
- `and` = /and/ — ends in /d/. Under strict (C)V, should be /a.nu/ or /a.na/?
  - But `and` is an existing core word, grandfathered.
  - **Note for future:** If reforming existing words, `and` → `anu` or `a`?
- `Lord` = /lord/ — ends in /d/. Proper noun should follow phonotactics too.
  - **Decision:** `Lord` → **Lordu** or **Lor**? 
  - Since it's a proper name (external to VELA phonotactics), we can keep close to source form. But for consistency: **Lordi** or **Loru**?
  - Recommendation: **Loru** — matches pattern of vowel-final for new words.

**Revised translation:**
> **"Go forti in pasi tu luv and servi la Loru."**

---

## 5. Alternative Translation — Simpler Register

If the liturgical tone is too elevated, a simpler secular version:

**"Go forward in calmness to help and work for people."**
> **"Go forti in kalm tu help and wok for de."**

New gaps: `kalm` (calmness), `for` (for/benefactive preposition)
- `kalm` = English "calm" + vowel? /kal.mi/? Actually `kalm` ends in /m/ which IS a sonorant — permitted!
- Wait: /m/ is sonorant, so `kalm` = /kalm/ = (C)V(C) where C = sonorant. Is this allowed?
- Per strict (C)V: only /n,m,l,r/ word-finally. So `kalm` IS valid!
- `for` = existing preposition. /for/ — ends in /r/, sonorant. Valid.

So simpler version requires only 1 new word: `forti`.

---

## 6. Frases Cotidianas — 20 High-Frequency Samples

### Saludos y Cortesía

| # | English | VELA | Notes |
|---|---------|------|-------|
| 1 | Hello! | **Helo!** | New word needed? Or use `gud dei`? |
| 2 | Good morning. | **Gud morne.** | `morne` = morning. New. |
| 3 | How are you? | **Yu es gud?** | Or: `Hau yu?` — `hau` = how. New. |
| 4 | Thank you. | **Tanke yu.** | `tanke` = thanks. New. |
| 5 | You're welcome. | **Yu welkom.** | `welkom` = welcome. New. |
| 6 | Goodbye. | **Gudbai.** | `gudbai` = goodbye. New. |
| 7 | Please. | **Plise.** | `plise` = please. New. |
| 8 | Excuse me. | **Ekskus mi.** | `ekskus` = excuse. New. |
| 9 | I'm sorry. | **Mi es sori.** | `sori` = sorry. New. |
| 10 | Yes / No | **Ok / No** | ✅ Already in lexicon |

### Compras y Restaurante

| # | English | VELA | Notes |
|---|---------|------|-------|
| 11 | How much? | **Hau mush?** | `mush` = much. New. |
| 12 | I want this. | **Mi wan la dis.** | `dis` = this. New. |
| 13 | The bill, please. | **La bil, plise.** | `bil` ✅ exists |
| 14 | Water, please. | **Water, plise.** | `water` ✅ |
| 15 | Where is the bathroom? | **Wer es la batrum?** | `wer` = where, `batrum` = bathroom. Both new. |

### Emergencias

| # | English | VELA | Notes |
|---|---------|------|-------|
| 16 | Help! | **Help!** | ✅ Already in lexicon |
| 17 | Call a doctor! | **Kol a doktr!** | `kol` = call. New. `doktr` = doctor. New? Wait, `doktr` — ends in /r/. Sonorant. Valid. But is it in lexicon? Check... |
| 18 | I'm sick. | **Mi es sik.** | `sik` = sick. New. |
| 19 | Where is the hospital? | **Wer es la sik-hous?** | `sik-hous` = compound (house for sick). Valid per Quality Gate! |
| 20 | Police! | **Polis!** | `polis` = police. New. Ends in /s/ → needs amendment: `polisi`. |

---

## 7. Gap Summary — All New Words Needed for Functional VELA

### From Benchmark (4 words)
| Word | English | Source | AFI |
|------|---------|--------|-----|
| forti | forth, forward | English | /for.ti/ |
| pasi | peace | Latin *pax* | /pa.si/ |
| servi | serve | Latin *servire* | /ser.vi/ |
| Loru | Lord (proper noun) | Source name | /lo.ru/ |

### From Daily Phrases (13+ words)
| Word | English | Source | AFI | Priority |
|------|---------|--------|-----|----------|
| helo | hello | English | /he.lo/ | HIGH |
| morne | morning | English | /mor.ne/ | HIGH |
| hau | how | English | /hau/ | HIGH |
| tanke | thanks | English | /tan.ke/ | HIGH |
| welkom | welcome | English | /wel.kom/ → /wel.ko.mu/? | HIGH |
| gudbai | goodbye | English | /gud.bai/ → /gu.bai/? | HIGH |
| plise | please | English | /pli.se/ | HIGH |
| ekskus | excuse | English | /ek.sku.si/? | MEDIUM |
| sori | sorry | English | /so.ri/ | HIGH |
| mush | much | English | /mu.shi/? | MEDIUM |
| dis | this | English | /dis/ → /di.si/? | HIGH |
| wer | where | English | /wer/ → /we.ru/? | HIGH |
| batrum | bathroom | English compound | /ba.trum/ → /ba.tru.mu/? | MEDIUM |
| kol | call | English | /kol/ → /ko.lu/? | HIGH |
| sik | sick | English | /sik/ → /si.ki/? | HIGH |
| polisi | police | English | /po.li.si/ | MEDIUM |

**Total new gaps discovered:** ~17 words for basic functional fluency.

---

## 8. Decisions Logged

| Decision | Context | Status |
|----------|---------|--------|
| Imperative = bare root | "Go!" | ✅ Confirmed |
| Directional adverbs = atoms | ap, daun, forti | ✅ New pattern |
| Infinitive marker `tu` | "to love" | ✅ Confirmed |
| `tu` distributes over chains | "to love and serve" | ✅ New rule |
| Proper nouns = UPPERCASE | "Lord" | ✅ Confirmed |
| Abstract state = `in` + noun | "in peace" | ✅ Confirmed |
| Existing core words grandfathered | `and`, `lord` | ⚠️ Phonotactic exception noted |

---

## 9. Next Steps

1. **Add 4 benchmark words** to LEXICON_BASE.md (forti, pasi, servi, Loru)
2. **Add 17 daily phrase words** to LEXICON_BASE.md
3. **Write 5 poems** in VELA (exercise creative use of ~1100 words)
4. **Write 1 short story** (500-1000 words) in VELA
5. **Document all grammatical decisions** in GRAMMAR_COMPLETE.md

---

*Generated by VELA Committee — Fase 8: Textos y Muestras*
