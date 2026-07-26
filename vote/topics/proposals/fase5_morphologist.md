# MORPHOLOGIST Review: Fase 5 Full Lexicon

**Reviewer:** Pi Agent @ pi (morphologist)
**Date:** 2026-05-31
**Scope:** ~246 words, 23 domains — structural/formation analysis only
**Note:** This review is strictly morphological. Lexicographic concerns (atom ceiling, homonymy, loan justification) are in `fase5_lexicographer.md`.

---

## Executive Summary

**Verdict: FLAG — critical plural inconsistency and affix gaps need resolution.**

1. **PLURAL VERDICT**: The committee brief claims grammar says `-s` — this is **FALSE**. GRAMMAR_COMPLETE §4.2 explicitly states: **`-n` after vowels, `-en` after consonants**. The lexicon examples (`selu-en`, `rekord-en`, `lif-tip-en`) correctly use `-en` for consonant-final words. HOWEVER, `selu-en` is wrong — `selu` ends in vowel `/u/`, so it should be **`selu-n`** per the grammar rule. **Recommendation: Keep `-n`/`-en` as grammar states. Fix vowel-final plurals to `-n` only.**

2. **WORST STRUCTURAL OFFENDERS**: `imaj-rekognishon` (native root + 5-syllable un-nativized loan), `servis-mikro` (reversed modifier-head), `pilgrimage` (zero nativization), `kompound` (loan for the concept "compound" in a compound-first language).

3. **TOP 3 FINDINGS**: (1) Affix `-nes` is underused — 6 abstract nouns should use it but don't (`realiti`, `integriti`, `imuniiti`, `korpshon`, `transparens`, `diagnoze-noun`). (2) 5 compounds violate the modifier-head pattern VELA establishes. (3) Hyphenation is consistent but the `-shon` suffix spelling varies: `vershn`, `fikshn`, `korpshon` vs standard `konekshon`, `reakshon`.

---

## PLURAL INCONSISTENCY — DEFINITIVE RESOLUTION

### The Grammar Rule (§4.2)

```
The plural suffix is -n after vowel-final roots, -en after consonant-final roots:
man     → man-en       (consonant-final)
siti    → siti-n       (vowel-final)
famili  → famili-n     (vowel-final)
```

### The Lexicon Examples

| Example | Word | Final sound | Correct plural | Lexicon uses | Verdict |
|---------|------|-------------|----------------|--------------|---------|
| selu-en | selu | /u/ vowel | **selu-n** | selu-en ❌ | WRONG — vowel-final gets `-n` |
| rekord-en | rekord | /d/ consonant | rekord-en | rekord-en ✅ | Correct |
| kord-en | kord | /d/ consonant | kord-en | kord-en ✅ | Correct |
| elemnt-en | elemnt | /t/ consonant | elemnt-en | elemnt-en ✅ | Correct |
| lif-tip-en | lif-tip | /p/ consonant | lif-tip-en | lif-tip-en ✅ | Correct |
| muzik-tool-en | muzik-tool | /l/ consonant | muzik-tool-en ✅ | (not shown) | N/A |

### Verdict

**The `-n`/`-en` system is CORRECT and CONSISTENT with the grammar.** The committee brief's claim that grammar says `-s` is factually wrong. The only error is `selu-en` → should be `selu-n`. All consonant-final `-en` plurals are correct.

**ACTION: Fix `selu-en` → `selu-n`. Audit all other vowel-final words for the same error. No systemic plural rule change needed.**

---

## Compound Length Analysis

### Borderline 3-root compounds (at maximum)

| Compound | Roots | Count | Verdict |
|----------|-------|-------|---------|
| `past-luv-pain` | past + luv + pain | 3 | ✅ At max, but transparent. Nostalgia = "past-love-pain" is elegant. |
| `big-muzik-grup` | big + muzik + grup | 3 | ⚠️ `big` is an adjective, not a root noun. Consider `muzik-grup` + adjective `big`. |
| `far-si-tool` | far + si + tool | 3 | ✅ At max, perfectly transparent. Telescope = "far-see-tool". |
| `muzik-mak-po` | muzik + mak + po | 2 roots + suffix | ✅ `-po` is a suffix, not a root. 2 roots + suffix = acceptable. |
| `film-rul-po` | film + rul + po | 2 roots + suffix | ✅ Same pattern. Acceptable. |
| `vote-po` | vote + po | 1 root + suffix | ✅ Well within limits. |

### 4+ root compounds: **NONE FOUND** ✅

No compound exceeds 3 roots. The maximum is respected throughout.

---

## Domain-by-Domain Verdicts

### 1. Software Development (17 words)
**Verdict: APPROVE** — All compounds well-formed; loans are phonotactically valid.

- **TIER A:** kod, bug, loop, kompail, instruk, funkshon, varibl, test-kod, komit, deploy
- **TIER B:**
  - `folt-fix` → well-formed compound. ✅
  - `algoritm` → loan, consonant cluster at end `/ritm/`. Consider `algoritmo` for vowel-final phonotactics.
  - `ran-taim` → compound. `taim` needs errata backfill. ✅ once backfilled.
  - `apdat` → labeled "up + data adapted" but form is `apdat` not `up-dat`. Inconsistent hyphenation — should either be compound `up-dat` or clearly marked as nativized loan.
  - `vershn` → **SPELLING**: Should be `venshon` for consistency with `-shon` pattern (cf. `konekshon`, `reakshon`).
  - `repositori` → 5 syllables. Long but phonotactically valid.
  - `branch` → loan. Phonotactically valid in VELA? `/branch/` has consonant cluster.
- **TIER C:** None structurally.

### 2. Hardware (9 words)
**Verdict: APPROVE** — Excellent compound design.

- **TIER A:** brain-chip, piktur-chip, wok-mem, data-disk, chip, skrin-toch, input, output
- **TIER B:**
  - `port-konekt` → well-formed. `konekt` appears as a new root here — needs backfill or flag as loan.
- **TIER C:** None.

### 3. Internet and Networks (11 words)
**Verdict: FLAG** — Word order issue + spelling inconsistency.

- **TIER A:** lowd-in, lowd-up, klaud-sav, IP-adres, protokol, konekshon, domain, strim
- **TIER B:**
  - `lod-balans` → **SPELLING INCONSISTENCY**: `lowd` (download) vs `lod` (load-balancer). Must standardize to `lowd-balans`.
  - `apli-brij` → well-formed compound. `apli` + `brij` = application-bridge. ✅
- **TIER C:**
  - `servis-mikro` → **REJECT word order**. VELA is modifier-head. Must be `mikro-servis`. Current form reverses the pattern.

### 4. Artificial Intelligence (10 words)
**Verdict: FLAG** — Mixed form issues.

- **TIER A:** masin-lern, brain-net, lern-modl, lern-data, auto-lern, predik, klasifai, predikshon
- **TIER B:**
  - `ai-instruk` → **MIXED FORM**: "AI" is an English acronym, not a VELA morpheme. Should be `masin-instruk` or accept `ai` as a borrowed acronym with explicit justification.
- **TIER C:**
  - `imaj-rekognishon` → **REJECT**: Mixed form — `imaj` (adapted loan root) + `rekognishon` (5-syllable un-nativized English word). Violates compound transparency. Suggest `imaj-nof` (image-know) or `si-nof-tool`.

### 5. Data (9 words)
**Verdict: APPROVE** — Clean domain.

- **TIER A:** data-beis, data-ask, bak-up, kript, rekord, indeks, kash, kolum
- **TIER B:**
  - `sinkr` → consonant cluster `/nkr/` at end. Consider `sinkron` for clarity.
- **TIER C:** None.

### 6. Biology (15 words)
**Verdict: FLAG** — Affix opportunity missed.

- **TIER A:** selu, jen, DNA, lif-kod, lif-tip, eko-sistam, adapt, klon, evolushon, hormon, bakteri, lif-lern
- **TIER B:**
  - `lif-lern` → ✅ Correctly uses `-lern` suffix for "field of study". Good.
  - `fotosintesis` → 5 syllables. Phonotactically valid but very long. No compound alternative is shorter.
  - `protein` → loan, phonotactically valid.
  - `mikrub` → formation is unclear. If `mikro-` + `rub`, then it's a compound but written without hyphen. Should be `mikro-rub` or justified as loan.
- **TIER C:** None.

### 7. Chemistry (10 words)
**Verdict: FLAG** — `-lern` suffix should apply here too.

- **TIER A:** atom, molkul, reakshon, asid, alkalin, kim-bond, period-tebl, laboratori
- **TIER B:**
  - `elemnt` → **PHONOTACTICS**: consonant cluster `/lmnt/`. Should be `element` or `elemnto`.
  - `kompound` → **AFFIX MISUSE**: This concept SHOULD be expressible via VELA's own morphology (`join-part`, `tuor-mor`). Using a loan for "compound" in a compound-first language is structurally ironic.
- **TIER C:**
  - Chemistry SHOULD have a `-lern` form (`kim-lern` = chemistry-as-study) but doesn't. Missing affix opportunity.

### 8. Physics (14 words)
**Verdict: FLAG** — Affix gaps and phonotactic issues.

- **TIER A:** fol-fors, partikl, wav, magnet, elektrik, elektron, termal, vibr
- **TIER B:**
  - `fors` → standalone atom AND used in `fol-fors`. The `-fors` suffix is established. `fors` as generic "force" + `fol-fors` as "gravity" is consistent. ✅
  - `enrji` → loan, phonotactically valid.
  - `kwantm` → **PHONOTACTICS**: consonant cluster `/ntm/`. Should be `kwantom`.
  - `masa` → phonotactically valid, but **homonymy concern** (per lexicographer review).
  - `momentm` → **PHONOTACTICS**: `/ntm/` cluster. Should be `momentom`.
  - `spid` → loan, valid.
- **TIER C:** None structurally, but physics SHOULD have `fors-lern` (force-study = physics). Missing `-lern` form.

### 9. Astronomy (13 words)
**Verdict: APPROVE** — Clean.

- **TIER A:** univers, planite, galaksi, orbita, komet, asteroid, blak-hol, far-si-tool, star-grup, son-sistam, astronaut, rokete, supernova
- **TIER B:** None structurally.
- **TIER C:** None.

### 10. Medicine Extended (12 words)
**Verdict: FLAG** — Missing `-nes` opportunities.

- **TIER A:** simtom, infekshon, anti-bodik, kron-sik, mental-healt, terapia, doz, diagnoze
- **TIER B:**
  - `imuniiti` → **AFFIX GAP**: Should this be `sik-fens-nes` (sick-defense-ness)? The `-nes` suffix could create a VELA-native form. Offer both: `imuniiti` (loan, medical register) + `sik-fens-nes` (native, everyday).
  - `tretmnt` → **PHONOTACTICS**: `/tmnt/` cluster. Should be `tretmant`.
  - `anestezi` → loan, valid.
  - `sikoloji` → **AFFIX GAP**: Should use `-lern` pattern: `maind-lern` (mind-study) or `sik-lern` (sick-study). Offer both.
- **TIER C:** None structurally.

### 11. Music (16 words)
**Verdict: FLAG** — `kor` homonymy; `big-muzik-grup` structure.

- **TIER A:** melodi, ritm, konser, harmoni, gitar, piano, drum, viulin, tempa, kord, muzik-tool, muzik-bit, nota-muzik
- **TIER B:**
  - `kor` → **HOMONYMY**: Per lexicographer review, `kor` = "choir" could collide with "core/heart." Morphologically fine but semantically risky. Suggest `sing-grup`.
  - `muzik-mak-po` → 2 roots + `-po` suffix. ✅ Within limits. Well-formed.
- **TIER C:**
  - `big-muzik-grup` → **STRUCTURAL ISSUE**: Embeds adjective `big` inside compound. VELA compounds should use noun roots only. "Big orchestra" should be `muzik-grup` + adjective `big`, not `big-muzik-grup` as a single lexical item. **Reject as compound; keep as adjective+noun phrase.**

### 12. Visual Arts (10 words)
**Verdict: APPROVE** — Clean, all loans + one compound.

- **TIER A:** skulptur, fotografi, art-hous, ekshibishon, kanvas, portret, mural, kolaj, dizain, stail
- **TIER B:** None structurally.
- **TIER C:** None.
### 13. Literature (13 words)
**Verdict: FLAG** — Spelling inconsistency with `-shon` pattern.

- **TIER A:** long-stor, buk-part, poem-lain, metafor, jenr, plot, karektr, narator, simbolism, poem, poetri
- **TIER B:**
  - `fikshn` → **SPELLING**: Should be `fikshon` for consistency with `-shon` suffix pattern.
  - `non-fikshn` → Same issue. Should be `non-fikshon`.
- **TIER C:** None structurally.

### 14. Film and Theater (8 words)
**Verdict: APPROVE** — Clean.

- **TIER A:** film-rit, sini, editar, teattr, skrining, produkshon, vizal-efekt, film-rul-po
- **TIER B:** None structurally. `film-rul-po` = 2 roots + suffix. ✅
- **TIER C:** None.

### 15. Philosophy (12 words)
**Verdict: APPROVE** — Gold standard for VELA morphology.

- **TIER A:** self-nof, fri-chuz, tru-nes, nof-nes, dep-nof, eksistens, logik, paradoks, abstrak, konkret, perspektiv, realiti
- **TIER B:**
  - `tru-nes` and `nof-nes` → **Correctly use `-nes` suffix.** Model for other domains.
  - `dep-nof` → 2-root compound, transparent. ✅
- **TIER C:** None.

### 16. Ethics and Morality (10 words)
**Verdict: FLAG** — Zero compounds, zero affix use. Worst morphology.

- **TIER A:** harm, etik, duti, konsent, empatia
- **TIER B:**
  - `moral` → loan, valid.
  - `virtu` → loan, valid.
  - `justifai` → loan verb, valid.
- **TIER C:**
  - `responsibil` → **AFFIX GAP**: 5 syllables. Needs compound: `duti-nes` or `rai-duti`.
  - `integriti` → **REDUNDANT**: `tru-nes` already means "truth-ness" = integrity. Loan is unnecessary.
  - `transparens` → **AFFIX GAP**: Could be `klar-nes` (clear-ness).
  - **ENTIRE DOMAIN**: Missing `-nes`, `-po`, `-hous` alternatives. Should have `rai-rong` (right-wrong = ethics), `duti-po` (duty-person).

### 17. Politics and Society (11 words)
**Verdict: FLAG** — Missing affix forms and phonotactic issues.

- **TIER A:** diplomat, aktivist, refom, refyuji, vote-po
- **TIER B:**
  - `parlamnt` → **PHONOTACTICS**: `/lamnt/` cluster. Should be `parlament`. Also needs `-hous` form: `lex-hous`.
  - `konstitushon` → 5 syllables. Consider `rai-lex`.
  - `govrnr` → **PHONOTACTICS**: `/vrnr/` cluster. Consider `land-rul-po`.
  - `korpshon` → **SPELLING**: Must be `korupshon`.
  - `transparens` → Needs `-nes` alternative: `klar-nes`.
  - `negosiat` → 4 syllables. Consider `tok-mid`.
- **TIER C:**
  - `korpshon` → **REJECT spelling**: Must be `korupshon`.

### 18. Religion and Spirituality (10 words)
**Verdict: FLAG** — Zero nativization on `pilgrimage`; isolated `-u` suffix.

- **TIER A:** god-ador, holi, ritual, mirakl, profet, meditashon, paraiz, blesing
- **TIER B:**
  - `spiritu` → Uses `-u` adjectival suffix. Only instance in entire lexicon. Must document `-u` as productive or treat as plain loan.
  - `blesing` → English `-ing` gerund suffix is not VELA morpheme. Should be `bles-ing` compound or nativized differently.
- **TIER C:**
  - `pilgrimage` → **REJECT**: Zero nativization. Must become `pilgrimej` or `god-trip`.

### 19. Sadness Cluster (5 words)
**Verdict: APPROVE** — Exemplary VELA morphology.

- **TIER A:** dep-sad, los-pain, blok-angri, past-luv-pain
- **TIER B:**
  - `loili-sad` → `loili` is not an existing VELA root. Base lexicon has `lonli`. Must be **`lonli-sad`**.
- **TIER C:** None structurally.

### 20. Joy Cluster (4 words) — APPROVE
### 21. Fear Cluster (4 words) — APPROVE
### 22. Love Cluster (5 words)
**Verdict: FLAG** — `kea` is morphologically opaque.

- **TIER A:** warm-fel, strong-luv, dep-luv
- **TIER B:** `luv` → Must be formally backfilled as atom.
- **TIER C:** `kea` → **REJECT**: No morphology, no etymology. Suggest `soft-fel`.

### 23. Wonder and Curiosity (4 words)
**Verdict: FLAG** — `kurius` should have compound alternative.

- **TIER A:** wait-hapi, inspir, wundr
- **TIER C:** `kurius` → **WEAK REJECT**: Offer `wan-nof` (want-know) as primary VELA form.

---

## Systemic Morphological Issues

### 1. `-shon` SUFFIX SPELLING INCONSISTENCY

| Standard | Inconsistent | Fix |
|----------|-------------|-----|
| `konekshon` | `vershn` | → `venshon` |
| `reakshon` | `fikshn` | → `fikshon` |
| `infekshon` | `korpshon` | → `korupshon` |

**RULE: Always spell as `-shon`. Never truncate to `-shn` or `-ps`.**

### 2. `-nes` AFFIX UNDERUSE

| Current loan | Should also have `-nes` form |
|-------------|-------------------------------|
| `realiti` | `rai-nes` (real-ness) |
| `integriti` | `tru-nes` (already exists!) |
| `transparens` | `klar-nes` (clear-ness) |
| `imuniiti` | `sik-fens-nes` (sick-defense-ness) |
| `responsibil` | `duti-nes` (duty-ness) |

### 3. MISSING `-lern` FORMS

| Domain | Current | Should have |
|--------|---------|-------------|
| Physics | (scattered loans) | `fors-lern` (force-study) |
| Chemistry | (scattered loans) | `kim-lern` (chemistry-study) |
| Psychology | `sikoloji` | `maind-lern` or `sik-lern` |

### 4. MISSING `-po` AND `-hous` FORMS

Professions and places that are loans should also have VELA-native alternatives:
- `diplomat` → `tok-mid-po` (talk-middle-person)
- `govrnr` → `land-rul-po` (land-rule-person)
- `parlamnt` → `lex-hous` (law-house)
- `laboratori` → `test-hous` (test-house)

### 5. PHONOTACTIC CLUSTERS TO FIX

| Word | Problem | Fix |
|------|---------|-----|
| `kwantm` | `/ntm/` cluster | → `kwantom` |
| `momentm` | `/ntm/` cluster | → `momentom` |
| `elemnt` | `/lmnt/` cluster | → `element` |
| `tretmnt` | `/tmnt/` cluster | → `tretmant` |
| `parlamnt` | `/lamnt/` cluster | → `parlament` |
| `govrnr` | `/vrnr/` cluster | → compound `land-rul-po` |
| `vershn` | truncated suffix | → `venshon` |
| `fikshn` | truncated suffix | → `fikshon` |

---

## Top 5 Morphological Recommendations

1. **FIX PLURAL**: Keep `-n`/`-en` per grammar §4.2. Fix `selu-en` → `selu-n`. Committee brief's `-s` claim is factually wrong.

2. **STANDARDIZE `-shon`**: Always `-shon`, never `-shn` or `-ps`. Fix `vershn`, `fikshn`, `korpshon`.

3. **FIX PHONOTACTIC CLUSTERS**: Add vowels to `kwantm` → `kwantom`, `momentm` → `momentom`, `elemnt` → `element`, `tretmnt` → `tretmant`, `parlamnt` → `parlament`.

4. **ADD DUAL-FORM STRATEGY**: Every abstract noun loan gets a VELA-native `-nes` alternative: `realiti` + `rai-nes`, `integriti` + `tru-nes`, `transparens` + `klar-nes`.

5. **FIX 5 STRUCTURAL OFFENDERS**:
   - `servis-mikro` → `mikro-servis` (word order)
   - `big-muzik-grup` → `muzik-grup` + adjective (no adj in compounds)
   - `imaj-rekognishon` → `imaj-nof` (mixed form)
   - `pilgrimage` → `pilgrimej` (zero nativization)
   - `loili-sad` → `lonli-sad` (non-existent root)

---

*Morphologist review complete. Submitted for committee deliberation.*
