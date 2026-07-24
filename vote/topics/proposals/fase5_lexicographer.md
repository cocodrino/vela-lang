# LEXICOGRAPHER Review: Fase 5 Full Lexicon

**Reviewer:** Pi Agent @ pi (lexicographer)
**Date:** 2026-05-31
**Scope:** ~246 words, 23 domains, LEXICON_EXTENDED.md + Phase 4 errata

---

## Executive Summary

**Verdict: FLAG — significant systemic issues require resolution before full approval.**

Of 23 domains, I approve **6** outright (Tier A), flag **11** for specific fixes (Tier B), and reject key words in **6** (Tier C). The most critical findings:

1. **ATOM CEILING BREACHED**: The base lexicon (Phases 1–4) already contains ~350–400 atoms. Phase 5 adds ~146 new loan-atoms, pushing the total to **~500+** — well beyond the 200-atom soft ceiling. The ceiling was already blown before Phase 5; Phase 5 makes it 2.5× worse. A hard triage is needed.

2. **HOMONYMY CLASHES FOUND**: 7 structural collisions detected — `kor` (choir vs core), `masa` (mass-physical vs other meanings), `tip` (type vs tip-gratuity), `bit` (binary-bit vs existing morpheme), `stap` (step vs potential collision), `harmoni` (could conflict with `harm` existing root), `spid` (speed — potential verb-noun confusion).

3. **NET vs NETTWERK INCONSISTENCY**: The errata proposes `net` but Phase 4 has `nettwerk`. This must be resolved — I recommend `net` as the atom, with `net-werk` as the compound.

4. **LUV STATUS CONTRADICTION**: `luv` appears both as "atomic — cross-ref Phase 4" AND in the "Phase 4 Errata — Missing Atomics" as pending. This must be resolved: I recommend **approve `luv` as atom** (it's already used in corpus poems and compounds).

5. **PILGRIMAGE NOT NATIVIZED**: `pilgrimage` violates VELA's own loan adaptation rules. Should be `pilgrimej` or `pilgrim-sey`.

---

## Domain-by-Domain Verdicts

### 1. Software Development (17 words — 14 atoms, 3 compounds)
**Verdict: FLAG** — Excessive atom density (~82%). Many loans could be transparent compounds.

- **TIER A (Approve):** kod, bug, loop, test-kod, komit, branch, deploy, algoritm, kompail
- **TIER B (Adjust):**
  - `instruk` → approve but note AFI should be /in.struk/ ✅ (correct as listed)
  - `funkshon` → approve, but verify no collision with existing `funk` (none found)
  - `varibl` → approve, but spelling could be `variabl` for consistency with `-abl` pattern
  - `vershn` → **TIER B: change to `vershon`** — inconsistent with `-shon` suffix pattern used elsewhere (konekshon, reakshon, infekshon). The truncation `vershn` is opaque.
  - `apdat` → approve but note: formation says "up + data adapted" — should be `up-dat` if compound, or keep `apdat` as nativized loan. Inconsistent labeling.
  - `repositori` → **TIER B: consider compound `kod-hous`** (code-house). 5 syllables is too long for a core computing term.
  - `ran-taim` → approve as compound; but `taim` must be backfilled (see errata).
- **TIER C (Reject):**
  - `branch` → **reject as atom**. English-specific jargon. Suggest compound `split-lain` (split-line) or keep as narrow tech loan with justification.
  - `deploy` → **reject as atom**. Suggest compound `send-out` or `lounch` (nativized loan, shorter).

**Rationale:** This domain is 82% loans — the worst ratio. Computing terms have international adoption but VELA's compound-first philosophy is violated. At minimum, `branch` and `deploy` should be replaced.

### 2. Hardware (9 words — 3 atoms, 6 compounds)
**Verdict: APPROVE** — Good compound ratio (67%). Well-designed domain.

- **TIER A (Approve):** brain-chip, piktur-chip, wok-mem, data-disk, skrin-toch, chip
- **TIER B (Adjust):**
  - `port-konekt` → AFI shows /port.ko.nekt/ — acceptable but `konekt` should be verified as existing verb or new atom. If `konekt` is new, flag as atom addition.
  - `input` → approve as international loan
  - `output` → approve as international loan
- **TIER C (Reject):** none

**Rationale:** This domain correctly prioritizes compounds. Only `chip`, `input`, `output` are atoms, and all three are internationally recognizable.

### 3. Internet and Networks (11 words — 4 atoms, 7 compounds)
**Verdict: FLAG** — Good compound ratio but some loans are unjustified.

- **TIER A (Approve):** lowd-in, lowd-up, klaud-sav, IP-adres, apli-brij, servis-mikro, protokol, konekshon
- **TIER B (Adjust):**
  - `strim` → approve, phonotactically valid
  - `domain` → approve as international term
  - `lod-balans` → note: `lowd` (download) vs `lod` (load-balancer) — **inconsistent spelling**. Must standardize to `lowd-balans`.
- **TIER C (Reject):**
  - `servis-mikro` → **reject word order**. In VELA modifier-head pattern, this should be `mikro-servis` (micro-service). Current form reverses the pattern.

**Rationale:** One word-order error and one spelling inconsistency. Otherwise solid.

### 4. Artificial Intelligence (10 words — 3 atoms, 7 compounds)
**Verdict: FLAG** — `ai-instruk` uses an English acronym; `imaj-rekognishon` is too long.

- **TIER A (Approve):** masin-lern, brain-net, lern-modl, lern-data, auto-lern, predik, klasifai
- **TIER B (Adjust):**
  - `predikshon` → approve, consistent `-shon` pattern
  - `ai-instruk` → **TIER B: flag**. "AI" is not a VELA morpheme — it's an English acronym. Suggest `smart-instruk` or `masin-instruk` for transparency, or accept `ai` as a VELA acronym atom with explicit justification.
- **TIER C (Reject):**
  - `imaj-rekognishon` → **reject**. 5 syllables, 2 roots but the second root `rekognishon` is an unadapted English word. Suggest `imaj-nof` (image-know) or `si-nof-tool` (see-know-tool).

**Rationale:** AI domain mostly good, but two words need fixes. The acronym issue and the overly long loans must be addressed.

### 5. Data (9 words — 6 atoms, 3 compounds)
**Verdict: FLAG** — High loan ratio (78%). Several loans could be compounds.

- **TIER A (Approve):** data-beis, data-ask, bak-up, kript, rekord, indeks, kash
- **TIER B (Adjust):**
  - `sinkr` → approve but AFI /sinkr/ ends in consonant cluster — check phonotactics. Consider `sinkron` for clarity.
  - `kolum` → approve as international term (Latin: columna)
- **TIER C (Reject):**
  - `kash` → **weak reject**. Could be `fast-mem` (fast-memory) but `kash` is near-universal in computing. Approve with justification.

**Rationale:** Data domain is heavily loan-based but the terms are genuinely international (Latin/Greek roots). `sinkr` needs phonotactic review.

### 6. Biology (15 words — 11 atoms, 4 compounds)
**Verdict: FLAG** — High loan ratio (73%) but many are justified as universal scientific terms.

- **TIER A (Approve):** selu, jen, DNA, lif-kod, lif-tip, eko-sistam, adapt, klon, lif-lern, evolushon, hormon
- **TIER B (Adjust):**
  - `protein` → approve as universal scientific term
  - `mikrub` → AFI should be clarified; is this "microbe" → /mik.rub/? The `rub` ending is opaque. Consider `mikro-bak` (micro-bacteria) instead.
  - `bakteri` → approve as international
  - `fotosintesis` → **TIER B: very long** (5 syllables). Could be `lait-fud-mak` (light-food-make) but the loan is internationally recognizable. Approve with note.
- **TIER C (Reject):** none

**Rationale:** Biology loans are mostly justified (Latin/Greek universal terms). `mikrub` needs phonotactic review; `fotosintesis` is long but defensible.

### 7. Chemistry (10 words — 8 atoms, 2 compounds)
**Verdict: APPROVE** — Mix of universal scientific terms and good compounds.

- **TIER A (Approve):** atom, molkul, reakshon, asid, kim-bond, period-tebl, laboratori, kompound
- **TIER B (Adjust):**
  - `elemnt` → AFI /e.lemnt/ has consonant cluster at end. Consider `element` or nativized `elemnto`. The truncated form is hard to pronounce.
  - `alkalin` → approve as international scientific term
- **TIER C (Reject):**
  - `kompound` → **reject as unjustified loan**. VELA is a compound-first language — the word for "compound" should BE a compound! Suggest `tuor-mor` (two-more) or `join-part` (joined-part). Ironic that the word for compound is itself a loan.

**Rationale:** Mostly good. `kompound` as a loan in a compound-first language is self-defeating and must be replaced.

### 8. Physics (14 words — 13 atoms, 1 compound)
**Verdict: REJECT** on multiple words — worst loan density (93%) and homonymy concerns.

- **TIER A (Approve):** fol-fors, partikl, wav, magnet, elektrik, elektron, termal, vibr
- **TIER B (Adjust):**
  - `fors` → approve but note: already exists as base-lexicon verb "force"? Check collision. If `fors` is new noun, it may conflict with verb use.
  - `enrji` → approve as international
  - `kwantm` → AFI /kwantm/ has consonant cluster. Consider `kwantom` or `kwanta`.
  - `masa` → **HOMONYMY WARNING**. `masa` could collide with `mas` (must, modal verb) or be confused with Spanish "mesa" (table). Suggest `masiv` or `bodi-wei` (body-weight).
  - `momentm` → AFI /mo.mentm/ consonant cluster. Consider `momentom`.
  - `spid` → approve but note: as noun "speed", could conflict with verb uses. Flag for monitoring.
- **TIER C (Reject):**
  - `fors` as standalone atom → **reject if `fol-fors` (gravity) already exists**. Having both `fors` and `fol-fors` creates semantic overlap. Keep `fors` only if it means "force" generically and `fol-fors` means "gravity (falling-force)".

**Rationale:** Physics domain is almost entirely loans. While many are internationally recognized, the atom explosion is severe. Homonymy concerns on `masa` must be resolved.

### 9. Astronomy (13 words — 9 atoms, 4 compounds)
**Verdict: APPROVE** — Good mix, universally recognized loans.

- **TIER A (Approve):** univers, planite, galaksi, orbita, komet, asteroid, blak-hol, far-si-tool, star-grup, son-sistam, supernova
- **TIER B (Adjust):**
  - `astronaut` → approve as international term
  - `rokete` → approve; good VELA nativization with final vowel
- **TIER C (Reject):** none

**Rationale:** Astronomy terms are genuinely international (Latin/Greek roots used worldwide). Compounds are well-formed. `far-si-tool` hits the 3-root max but is transparent.

### 10. Medicine — Extended (12 words — 9 atoms, 3 compounds)
**Verdict: FLAG** — High loan ratio (83%) but medically justified.

- **TIER A (Approve):** simtom, infekshon, anti-bodik, kron-sik, mental-healt, terapia, doz
- **TIER B (Adjust):**
  - `diagnoze` → approve; good verb form
  - `tretmnt` → AFI /tret.mnt/ consonant cluster. Consider `tret-mnt` → `tretmant` for phonotactic clarity.
  - `imuniiti` → overly long (5 syllables). Consider `bodi-shild` (body-shield) or `sik-fens` (sick-defense).
  - `anestezi` → approve as international medical term
  - `sikoloji` → approve as international
- **TIER C (Reject):** none

**Rationale:** Medical terms are internationally standardized — loans are justified. But `imuniiti` and `tretmnt` need phonotactic fixes.

### 11. Music (16 words — 11 atoms, 5 compounds)
**Verdict: FLAG** — Homonymy concern on `kor`; compound length concern.

- **TIER A (Approve):** melodi, ritm, muzik-tool, konser, harmoni, gitar, piano, drum, viulin, nota-muzik
- **TIER B (Adjust):**
  - `kor` → **HOMONYMY WARNING**. `kor` = "choir" but could collide with `kor` as "core/heart" in other contexts. Suggest `sing-grup` (sing-group) to avoid collision and increase transparency.
  - `tempa` → approve as international (tempo)
  - `muzik-mak-po` → at 3 morphemes (2 roots + suffix), this is at the compound length max. Approve but monitor.
  - `muzik-bit` → approve; transparent compound
  - `kord` → approve as international (chord)
- **TIER C (Reject):**
  - `big-muzik-grup` → **reject as compound**. 3 roots is the max allowed, but "big-music-group" is more like "large-music-group" which should be a modifier: `gran-muzik-grup` or just `muzik-grup` with `big` as adjective. The compound `big-muzik-grup` embeds an adjective inside a compound, which is opaque.

**Rationale:** Replace `kor` with `sing-grup` to avoid homonymy. `big-muzik-grup` is semantically redundant — just use `muzik-grup` + adjective `big`.

### 12. Visual Arts (10 words — 9 atoms, 1 compound)
**Verdict: FLAG** — 90% loan ratio, highest in the entire lexicon.

- **TIER A (Approve):** skulptur, fotografi, art-hous, ekshibishon, kanvas, portret, mural, dizain
- **TIER B (Adjust):**
  - `kolaj` → approve (international French-origin term)
  - `stail` → approve; short, phonotactically valid
- **TIER C (Reject):** none, but note: this domain needs more VELA-original compounds. Consider `piktur-mak-po` (picture-make-person = painter) instead of future loans.

**Rationale:** All loans are internationally recognized art terms, so they're justified. But the 90% ratio is concerning for VELA's compound-first philosophy. No rejections needed now.

### 13. Literature (13 words — 9 atoms, 4 compounds)
**Verdict: FLAG** — 85% loan ratio, but well-chosen compounds for core concepts.

- **TIER A (Approve):** long-stor, buk-part, poem-lain, non-fikshn, metafor, jenr, plot, karektr, narator, simbolism
- **TIER B (Adjust):**
  - `poem` → approve as international
  - `poetri` → approve but note: `poem` and `poetri` share the same root — good consistency
  - `fikshn` → AFI /fik.shn/ — consonant cluster. Consider `fikshon` for consistency with `-shon` pattern.
- **TIER C (Reject):** none

**Rationale:** Literature terms are a reasonable mix. `fikshn` needs spelling alignment with the `-shon` suffix pattern.

### 14. Film and Theater (8 words — 5 atoms, 3 compounds)
**Verdict: FLAG** — 88% loan ratio, but small domain so acceptable.

- **TIER A (Approve):** film-rit, sini, editar, teattr, produkshon, vizal-efekt
- **TIER B (Adjust):**
  - `film-rul-po` → approve; correctly uses `-po` profession suffix. At 2 roots + suffix, within limits.
  - `skrining` → approve as international
- **TIER C (Reject):** none

**Rationale:** Small domain, loans are justified. Compounds are well-formed.

### 15. Philosophy (12 words — 7 atoms, 5 compounds)
**Verdict: APPROVE** — Best domain in the entire proposal. 42% compound ratio, well-designed.

- **TIER A (Approve):** self-nof, fri-chuz, tru-nes, nof-nes, dep-nof, logik, paradoks, konkret
- **TIER B (Adjust):**
  - `eksistens` → approve as international
  - `realiti` → approve
  - `abstrak` → approve
  - `perspektiv` → approve
- **TIER C (Reject):** none

**Rationale:** This domain is the gold standard for VELA. It uses compounds for core philosophical concepts (`self-nof`, `fri-chuz`, `dep-nof`) and reserves loans for truly international terms. Other domains should emulate this pattern.

### 16. Ethics and Morality (10 words — 10 atoms, 0 compounds)
**Verdict: REJECT** — 100% loan ratio, zero compounds. Worst domain for VELA's philosophy.

- **TIER A (Approve):** harm (short, phonotactically valid), empatia (international), konsent (international)
- **TIER B (Adjust):**
  - `moral` → approve as international
  - `etik` → approve as international
  - `duti` → approve as international (duty)
  - `virtu` → approve (Latin origin, universal in ethics discourse)
  - `responsibil` → **FLAG**: 5 syllables, very long. Consider compound `wok-nof-po` (work-know-person) or `rai-duti` (right-duty).
  - `integriti` → **FLAG**: 5 syllables. Consider `tru-nes` (already exists!) or `honr` (shorter loan).
  - `justifai` → approve; verb form is transparent
- **TIER C (Reject):**
  - **REJECT the entire domain's compound absence**. VELA should have: `rai-rong` (right-wrong = ethics), `duti-po` (duty-person = responsible person), `gud-fel` (good-feel = empathy). At minimum, compound alternatives should be offered alongside loans.

**Rationale:** This domain violates VELA's compound-first philosophy most severely. No VELA-original compounds at all. Must be redesigned with compound alternatives.

### 17. Politics and Society (11 words — 10 atoms, 1 compound)
**Verdict: FLAG** — 100% loan ratio (excluding `vote-po`), but many terms are genuinely international.

- **TIER A (Approve):** vote-po, diplomat, refom, aktivist
- **TIER B (Adjust):**
  - `parlamnt` → AFI /par.lamnt/ — consonant cluster. Consider `parlament` or `lex-hous-po` (law-house-person).
  - `konstitushon` → very long (5 syllables). Consider `rai-lex` (right-law) as compound.
  - `govrnr` → AFI /gov.rnr/ — consonant cluster. Consider `rai-rul-po` (right-rule-person).
  - `korpshon` → AFI /kor.pshon/ — consonant cluster. Consider `bad-wok-po` (bad-work = corruption) or fix spelling to `korupshon`.
  - `transparens` → approve as international
  - `negosiat` → 4 syllables. Consider `tok-mid-po` (talk-middle-person = negotiator).
  - `refyuji` → approve as international
- **TIER C (Reject):**
  - `korpshon` → **reject spelling**. Must be `korupshon` — current spelling loses the `/ru/` syllable, making it opaque.

**Rationale:** Political terms are mostly international, but several phonotactic issues and overly long forms. Compound alternatives should be offered.

### 18. Religion and Spirituality (10 words — 9 atoms, 1 compound)
**Verdict: FLAG** — `pilgrimage` violates loan adaptation rules; `god-ador` is well-formed.

- **TIER A (Approve):** god-ador, holi, ritual, profet, meditashon, spiritu, mirakl
- **TIER B (Adjust):**
  - `paraiz` → approve as international (paradise)
  - `blesing` → approve; phonotactically valid
- **TIER C (Reject):**
  - `pilgrimage` → **REJECT**. Not nativized at all! Violates VELA's own adaptation rules. Must become `pilgrimej` or compound `god-hous-wok-po` (god-house-walk-person = pilgrim) + noun `god-trip`.

**Rationale:** Only one critical rejection. `pilgrimage` is the worst loan in the entire document — it's not even slightly adapted.

### 19. Sadness Cluster (5 words — 0 atoms, 5 compounds)
**Verdict: APPROVE** — Exemplary VELA compound design. 0% loan ratio.

- **TIER A (Approve):** dep-sad, los-pain, blok-angri
- **TIER B (Adjust):**
  - `loili-sad` → **TIER B**: `loili` is not an existing VELA atom. Must backfill `loili` (lonely) or change to `lond-sad` (lonely+sad) using existing `lond` (land?) — actually, base lexicon has `lonli` (lonely). Suggest: **`lonli-sad`** instead of `loili-sad`.
  - `past-luv-pain` → at 3 roots (max allowed). Transparent and well-formed. Approve.
- **TIER C (Reject):** none

**Rationale:** Emotion clusters are VELA's strongest design contribution. All compounds are transparent. Only fix: replace `loili` with existing `lonli`.

### 20. Joy Cluster (4 words — 0 atoms, 4 compounds)
**Verdict: APPROVE** — Perfect compound design.

- **TIER A (Approve):** kwaiat-hapi, top-hapi, enuf-hapi, warm-hapi
- **TIER B (Adjust):** none
- **TIER C (Reject):** none

**Rationale:** Every word is a transparent compound. This is the model for VELA's compound-first philosophy.

### 21. Fear Cluster (4 words — 0 atoms, 4 compounds)
**Verdict: APPROVE** — Perfect compound design.

- **TIER A (Approve):** futur-afred, tot-afred, big-afred, dep-afred
- **TIER B (Adjust):** none
- **TIER C (Reject):** none

**Rationale:** All compounds are transparent and semantically precise. `dep-afred` (dread) and `big-afred` (panic) are particularly elegant.

### 22. Love Cluster (5 words — 2 atoms, 3 compounds)
**Verdict: FLAG** — `luv` status must be resolved; `kea` is opaque.

- **TIER A (Approve):** warm-fel, strong-luv, dep-luv
- **TIER B (Adjust):**
  - `luv` → **APPROVE as atom**. It's already used in corpus poems and in compounds (`past-luv-pain`, `strong-luv`, `dep-luv`). The Phase 4 errata listing is contradictory — resolve by formally approving it.
- **TIER C (Reject):**
  - `kea` → **REJECT**. What language is this from? The formation says "adapted loan" but provides no source etymology. It's completely opaque — no speaker can guess that `kea` means "casual care." Suggest: **`soft-fel`** (soft-feel) or **`smol-fel`** (small-feel) as transparent compound.

**Rationale:** Replace `kea` with a transparent VELA compound. Formally approve `luv` as atom.

### 23. Wonder and Curiosity (4 words — 3 atoms, 1 compound)
**Verdict: FLAG** — `kurius` and `wundr` are unjustified loans when compounds exist.

- **TIER A (Approve):** wait-hapi (transparent compound), inspir
- **TIER B (Adjust):**
  - `wundr` → approve as short, common word. But consider compound `big-si-fel` (big-see-feel) as VELA alternative.
  - `kurius` → **FLAG**: could be `wan-nof` (want-know) — a perfectly transparent VELA compound. Loan is not justified when compound exists.
- **TIER C (Reject):**
  - `kurius` → **weak reject**. Suggest `wan-nof` (want-know) as primary VELA compound, with `kurius` as secondary loan for scientific/academic register.

**Rationale:** `wan-nof` (want-to-know) is more VELA than `kurius`. At minimum, offer both with `wan-nof` as primary.

---

## Phase 4 Errata — Backfill Verdicts

| Word | Verdict | Action |
|------|---------|--------|
| **luv** | ✅ APPROVE | Already used in corpus and compounds. Formalize as atom. |
| **taim** | ✅ APPROVE | Used in `ran-taim`, `somtaim`. Short, common. Formalize. |
| **wei** | ✅ APPROVE | Used in directional idioms. Formalize. |
| **art** | ✅ APPROVE | Used in `art-hous`, `art-stail`. Universal concept. Formalize. |
| **net** | ⚠️ APPROVE with fix | Approve `net` as atom. **Deprecate `nettwerk`** — replace with compound `net-werk`. Current double spelling is inconsistent. |
| **kod** | ✅ APPROVE | Used in `lif-kod`, `test-kod`. Universal in computing. Formalize. |
| **sav** | ✅ APPROVE | Used in `klaud-sav`, `data-sav`. Short, common. Formalize. |
| **tip** | ⚠️ APPROVE with caution | Homonymy: `tip` = "type" but also English "tip" (gratuity, point). Consider `typ` or keep `tip` with clear gloss. |
| **stap** | ✅ APPROVE | Used in idioms and instruction sequences. Short. Formalize. |
| **grup** | ✅ APPROVE | Used in `star-grup`, `big-muzik-grup`. Universal. Formalize. |
| **bit** | ⚠️ APPROVE with caution | Homonymy risk: `bit` = "binary digit" vs English "bit" (small piece). In VELA context, computing sense is clear. Keep with gloss "computing bit." |

---

## Systemic Issues

### 1. ATOM CEILING CATASTROPHICALLY BREACHED

The 200-atom soft ceiling is already violated by Phases 1–4 (estimated **350–400 existing atoms**). Phase 5 adds approximately **146 new loan-atoms**, pushing the total to **~500+**.

**This is 2.5× the ceiling.** The committee must decide:

- **Option A**: Raise the ceiling to 500+ (accepting VELA as a moderately-sized lexicon language)
- **Option B**: Triage aggressively — reject ~150 Phase 5 loans and replace with compounds
- **Option C**: Two-tier system — core atoms (200) + extended register (additional loans for specialized domains)

I recommend **Option C**: a core vocabulary of 200 atoms + domain registers that can be learned as needed. This preserves learnability while acknowledging reality.

### 2. HOMONYMY CLASHES

| Word | Clash | Resolution |
|------|-------|------------|
| `kor` | choir vs core/heart | Rename to `sing-grup` |
| `masa` | mass-physics vs `mas` (must) | Rename to `masiv` or `bodi-wei` |
| `tip` | type vs tip-gratuity | Keep with clear gloss; low risk |
| `bit` | binary-digit vs small-piece | Keep with computing gloss; low risk |
| `stap` | step vs staple | Keep; low collision risk |
| `harmoni` | harmony vs `harm` root | Keep; different enough |
| `spid` | speed-noun vs verb | Keep; context disambiguates |
| `fors` | force-noun vs potential verb | Keep `fol-fors` (gravity) as primary; `fors` as generic |

### 3. CONSISTENCY ISSUES

| Issue | Details | Resolution |
|-------|---------|------------|
| **net vs nettwerk** | Phase 4 has `nettwerk`; errata proposes `net` | Approve `net` as atom; deprecate `nettwerk` → `net-werk` |
| **luv status** | Listed as both "approved atom" and "errata pending" | Formally approve as atom |
| **-shon pattern** | `vershn`, `fikshn` vs `konekshon`, `reakshon` | Standardize: always `-shon` |
| **Consonant clusters** | `vershn`, `elemnt`, `tretmnt`, `kwantm`, `momentm` | Add vowel: `venshon`, `element`, `tretmant`, `kwantom`, `momentom` |
| **Compound length** | `big-muzik-grup`, `past-luv-pain`, `far-si-tool` | All at 3-root max. Acceptable but monitor. |
| **`-nes` consistency** | `tru-nes`, `nof-nes` use suffix | Should `realiti`, `integriti`, `imuniiti` also use `-nes`? Consider `rai-nes` (rightness) for integrity. |
| **`-po` consistency** | `vote-po`, `muzik-mak-po`, `film-rul-po` | Correctly applied. |
| **pilgrimage** | Not nativized at all | Change to `pilgrimej` or compound `god-trip` |
| **Word order** | `servis-mikro` reverses modifier-head | Change to `mikro-servis` |
| **lowd vs lod** | Inconsistent spelling | Standardize to `lowd` |

### 4. ENTRY QUALITY ISSUES

- **AFI inconsistencies**: Several entries have consonant clusters that violate VELA's (C)V phonotactics (e.g., `vershn`, `elemnt`, `tretmnt`). All should be regularized with final vowel.
- **Missing AFIs**: Some compounds list AFIs that don't match the compound parts (e.g., `far-si-tool` AFI shows `/far.si.tul/` — `tool` → `tul`?).
- **`ai-instruk`**: Uses English acronym "AI" which is not a VELA morpheme.
- **`kea`**: No etymology provided. Completely opaque.

---

## Top 5 Recommendations

1. **TRIAGE ATOMS — Implement Two-Tier System**: Core 200 atoms for daily communication + domain registers (science, tech, arts) with additional atoms. This is the only realistic path forward.

2. **FIX 7 HOMONYMY CLASHES**: Rename `kor` → `sing-grup`, `masa` → `masiv`, and audit `tip`, `bit`, `stap`, `fors`, `spid` for context disambiguation.

3. **STANDARDIZE PHONOTACTICS**: Regularize all consonant-cluster endings. Change `vershn` → `venshon`, `elemnt` → `element`, `tretmnt` → `tretmant`, `kwantm` → `kwantom`, `momentm` → `momentom`.

4. **REPLACE TOP 5 UNJUSTIFIED LOANS WITH COMPOUNDS**:
   - `kompound` → `join-part` or `tuor-mor`
   - `kea` → `soft-fel` or `smol-fel`
   - `pilgrimage` → `god-trip` or `pilgrimej`
   - `servis-mikro` → `mikro-servis` (word order fix)
   - `imuniiti` → `bodi-shild` (body-shield)

5. **APPROVE PHASE 4 ERRATA WITH FIXES**: All 11 errata atoms approved, but `net` replaces `nettwerk`, and `tip`/`bit` get cautionary glosses.

---

*Analysis complete. Lexicographer review submitted for committee deliberation.*
