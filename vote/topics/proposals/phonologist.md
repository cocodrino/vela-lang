# Proposal — VELA Phonologist (ollama/kimi-k2.6:cloud)
## Standby Issues Deliberation — Phonotactic Analysis

---

## ISSUE 1: Atomic Word Threshold (745 atoms, only 35 compounds)

### Phonological Assessment: HIGH RISK

The (C)V template is violated not at the margins but *inside* long atomic words. The problem is cumulative: every additional syllable is an additional opportunity for an illegal cluster or coda to emerge, and long opaque borrowings harbor them in spades.

#### Violation Inventory

| Word | Surface | Syllabification | Violation | Severity |
|------|---------|-----------------|-----------|----------|
| `undrstand` | /undrstand/ | [un.drs.tand] or [undr.stand] | CCC onset + CC coda + /d/ final | CRITICAL |
| `prezidnt` | /prezidnt/ | [pre.zid.nt] | /nt/ coda | CRITICAL |
| `sientist` | /sientist/ | [sie.nist] or [si.en.tist] | /nt/ coda | CRITICAL |
| `handrd` | /handrd/ | [han.drd] | /rd/ cluster + /d/ final | CRITICAL |
| `twelv` | /twelv/ | [twelv] | /v/ final (obstruent) | CRITICAL |
| `dangerus` | /dangerus/ | [dan.ge.rus] | /nd/ onset if reanalyzed; /ng/ not phonemic | HIGH |
| `smaurtfon` | /smaurtfon/ | [smau.r.tfon] or [smaur.tfon] | /rt/ cluster; /tf/ cluster | HIGH |
| `aereplan` | /aereplan/ | [ae.re.plan] | /pl/ onset cluster (legal but dense) | LOW |
| `temperaturu` | /tem.pe.ra.tu.ru/ | [tem.pe.ra.tu.ru] | None — fully (C)V | LEGAL |

**Key insight**: `temperaturu` is 5 syllables and perfectly legal. Length alone is NOT a phonotactic violation. But length *correlates* with violation because long words in VELA are overwhelmingly English/Latin borrowings that retain their original cluster structure under a thin orthographic veneer.

#### Compound vs Atomic from a Phonotactic POV

Compounds decompose violations across morpheme boundaries:
- `mid-naight` → /mid.nait/ → /d/ + /n/ resyllabifies as coda + onset, but VELA forbids coda /d/. Better: `mid-nait` still broken.
- `sik-hous` → /sik.haus/ → /k/ becomes coda. Still illegal.

Wait — simple compounding does NOT automatically fix phonotactics if the component roots themselves end in illegal consonants. The morphologist's reform of roots to (C)V is a *prerequisite* for clean compounding.

**Analogy**: Finnish compounding is phonotactically safe because every root ends in a vowel or /n/. Finnish `rakennus` (building) + `tarkastus` (inspection) = `rakennustarkastus` seamlessly. Turkish `ev` + `kapı` = `evkapı` — hiatus, but legal. Japanese `gakkou` + `seikatsu` = `gakkouseikatsu` — every syllable open.

**Recommendation**: Compounding is phonotactically advantageous ONLY if the atomic roots are first brought into (C)V compliance. The priority order is:
1. Fix all atomic roots to (C)V (add final vowels where needed)
2. THEN encourage compounding, which will be safe by construction

**Specific reforms for Issue 1**:
- `undrstand` → `unda-stani` (4 open syllables) or compound `bene-komprendi` (understand)
- `prezidnt` → `prezidenti` (pre.zi.den.ti) or `hed-man` (head-man = president)
- `sientist` → `sientisti` or compound `nau-man` (know-man = scientist)
- `dangerus` → `dangeru` (4 syllables, all open) or `riski-fai` (risk-full = dangerous)

**Rating**: HIGH. The sheer number of violations in long atoms creates a two-tier lexicon where "short words are legal, long words are suspect." This erodes the learner's confidence in the template.

---

## ISSUE 2: PROFIL Homonymy

### Phonological Assessment: MEDIUM-HIGH RISK

**Form**: Both entries = /pro.fil/ — two syllables, penultimate pitch accent on /pro/, final /l/ (legal coda consonant).

**Pitch-accent disambiguation**: VELA pitch accent is *fixed* (penultimate = HIGH). There is NO tonal distinction possible between "profile" PROFIL and "profit" PROFIL. In a true pitch-accent language like Japanese, homophones are disambiguated by pitch *shape*:
- *hashi* (bridge) = HLL
- *hashi* (chopsticks) = LHL
- *hashi* (edge) = LHH

VELA's rigid penultimate rule eliminates this possibility. Two words with identical syllable count and identical segmental content are *indistinguishable in the phonological signal*.

**Functional load**: Both "profile" and "profit" are concrete nouns likely to appear in business/technical contexts. "The company profit" vs "the company profile" — identical prosody, identical segments.

**Analogy**: Mandarin Chinese has massive homophony (shi = 10+ characters) but survives through tone + compounding + context. VELA has no tone, no compounding in these words, and relies on context alone. Finnish has minimal homophony due to agglutination; Turkish similarly resolves through suffixation.

**Phonological reform options**:
- **A**: Lengthen one form — `profila` (profile) vs `profil` (profit). VELA has no phonemic vowel length, so this would be orthographic only, not phonological.
- **B**: Change one word's syllable count to shift accent — `profitu` /pro.fi.tu/ places accent on /fi/, audibly distinct from /PRO.fil/. This is the most phonologically elegant solution.
- **C**: Replace entirely — `profeto` /pro.fe.to/ (profit, from Latin *profectus*) vs `profil` (profile). Both legal, distinct accent locus, international recognizability preserved.

**Rating**: MEDIUM-HIGH. Not a phonotactic violation, but a phonological *systemic* risk. Pitch-accent languages require either flexible accent placement (Japanese) or rich morphology (Finnish) to survive homophony. VELA has neither.

**Recommendation**: Option C. `profeto` for "profit" (from Latin/Romance roots, ends in vowel, accent on /fe/ = /pro.FE.to/) keeps the lexicon open-syllable and introduces accentual contrast.

---

## ISSUE 3: SE Noun vs SE Suffix

### Phonological Assessment: MEDIUM RISK

**Forms**:
- Lexical `se` (sea) = /se/ — free morpheme, could receive independent pitch accent if disyllabic; as monosyllable, accent is neutral
- Suffix `-se` (genitive) = /se/ — clitic, forms a phonological word with its host

**Sandhi behavior**: In continuous speech, clitics typically resyllabify with their hosts:
- `la mi-se buk` = /la.mi.se.buk/ → phonological word is [la] [mi.se.buk] or [la.mi] [se.buk] depending on parsing.
- `in la se` = /in.la.se/ → [in] [la] [se].

The genitive `-se` is a post-clitic; the noun `se` is a free word. In isolation they are identical. In connected speech, the genitive will always be the *second element* of a phonological word, while the noun `se` will be an independent prosodic word.

**Prosodic disambiguation test**:
- `mi-se` (my) = /mi.se/ — genitive clitic attaches to pronoun. Two syllables, accent on penultimate /mi/ = MI-se.
- `la se` (the sea) = /la.se/ — article + noun. Two syllables, accent on penultimate /la/ = LA-se.

Both are [X-se] with penultimate accent. The accent falls on the same relative syllable. **There is NO prosodic distinction.**

However, syntax fully disambiguates:
- Genitive `se` never appears without a host (pronoun or noun).
- Lexical `se` never appears directly after a noun without an article or preposition.

The only dangerous case: could a noun end in /s/ and take genitive `-se`, creating `X-s-se`? VELA allows /s/ final? No — /s/ is not in the permitted final set {n, m, l, r}. So no noun ends in /s/. The worst case is `se-se` (sea-GEN) = /se.se/, which is merely repetitive, not ambiguous with `se` as a free noun.

**Analogy**: Turkish genitive `-in` /-ɯn/-/in/ is not homophonous with a major noun. But Turkish has vowel harmony which changes the suffix: `ev-in` (house-GEN) vs `okul-un` (school-GEN). VELA has no vowel harmony to provide allomorphic variation.

**Finnish analogy**: Finnish `-n` is genitive singular. It happens to be identical to the nominative singular of some nouns, but case endings are unambiguous by position.

**Phonological reform options**:
- **A**: Leave as-is. Syntax disambiguates; collision is theoretical, not practical.
- **B**: Change genitive suffix to `si` /si/ or `sa` /sa/. Creates distance from `se` /se/. But cascades to all 5 existing possessives (`mi-se`, `yu-se`, etc.). Low phonological cost, high morphological cost.
- **C**: Change "sea" to `mar` /mar/ (one syllable, /r/ final, legal). `mar` is internationally recognizable (Latin *mare*, Spanish *mar*, French *mer*).

**Rating**: MEDIUM. Not a phonotactic violation. The collision is syntactically contained. However, in a language aspiring to zero ambiguity, perfect homophony between a high-frequency content word and a productive grammatical suffix is a long-term liability.

**Recommendation**: Option C. Replace "sea" with `mar` /mar/ (or `oce` /o.se/ if Romance transparency is preferred). `mar` is one syllable, ends in /r/ (legal), is cross-linguistically transparent, and eliminates the collision entirely. The possessives (`mi-se`, `yu-se`) remain untouched — no cascade.

---

## ISSUE 4: Numbers

### Phonological Assessment: CRITICAL

This is the clearest and most urgent violation in the standby set. Multiple number words breach the (C)V template at the most basic level of the lexicon.

#### Violation Inventory

| Number | Current | Phonotactic Analysis | Violation | Fix |
|--------|---------|---------------------|-----------|-----|
| 11 | `elevn` | /e.levn/ or /e.le.vn/ | /lvn/ cluster; /v/ + /n/ is articulatorily awkward | `ten-wan` /ten.wan/ |
| 12 | `twelv` | /twelv/ | /v/ final — ILLEGAL obstruent coda | `ten-tu` /ten.tu/ |
| 100 | `handrd` | /han.drd/ | /rd/ cluster; /d/ final — ILLEGAL | `ten-ten` /ten.ten/ |
| 1000 | `thausand` | /thau.sand/ | /nd/ cluster — coda cluster | `ten-hun` /ten.hun/ or `tu-handrd` |
| 13–19 | `kwatrotin` etc. | /kwat.ro.tin/ | varies; some have /nt/ | already semi-regular but opaque |
| 20,30... | `twenti, thirti` | /twen.ti/ | /nt/ cluster (marginal) | `tu-ten, tri-ten` |

**Key insight**: Numbers are HIGH-FREQUENCY, EARLY-ACQUIRED vocabulary. A learner encounters "twelve" in lesson 1. If twelve violates the one rule they just learned — "every syllable ends in a vowel" — the rule is immediately delegitimized.

This is not a marginal exception. This is core vocabulary telling the learner: "the rules don't apply here."

#### Analogical Evidence

**Chinese**: 11 = shi-yi (ten-one), 12 = shi-er (ten-two), 20 = er-shi (two-ten), 100 = yi-bai (one-hundred), 1000 = yi-qian (one-thousand). Purely compositional, every element monosyllabic.

**Japanese**: 11 = juu-ichi (ten-one), 12 = juu-ni (ten-two), 20 = ni-juu (two-ten), 100 = hyaku, 1000 = sen. Japanese mixes atomic (`hyaku`, `sen`) with compounds — but even `hyaku` and `sen` are phonotactically regular (open syllables: [hja.ku], [seɴ] with moraic /n/).

**Finnish**: 11 = yksitoista (one-of-second-ten), 12 = kaksitoista, 20 = kaksikymmentä (two-tens). Fully agglutinative and transparent.

**Hawaiian**: 11 = `ʻumikūmākahi` (ten+one), 20 = `iwakālua`. All open syllables, compounds only.

VELA's `elevn` and `twelv` are inherited English-Germanic fossils. They are etymologically opaque ("eleven" from *ainlif*, "twelve" from *twalif*) and phonotactically toxic.

#### Recommended Number System Reform

| # | New Form | Phonotactics | Composition |
|---|----------|-------------|-------------|
| 0 | `zero` | /ze.ro/ | keep (vowel-final) |
| 1–10 | `wan, tu, tri, kwatro, faiv, siks, sevn, eit, nain, ten` | all (C)V or (C)VC + V | keep |
| 11 | `ten-wan` | /ten.wan/ | compound |
| 12 | `ten-tu` | /ten.tu/ | compound |
| 13–19 | `ten-tri, ten-kwatro, ten-faiv...` | all clean | replace opaque `-teen` |
| 20 | `tu-ten` | /tu.ten/ | compound |
| 30–90 | `tri-ten, kwatro-ten, faiv-ten...` | all clean | replace opaque `-ti` forms |
| 100 | `ten-ten` | /ten.ten/ | compound |
| 101 | `ten-ten-wan` | /ten.ten.wan/ | recursive compound |
| 200 | `tu-ten-ten` | /tu.ten.ten/ | recursive |
| 1000 | `ten-ten-ten` | /ten.ten.ten/ | recursive |
| 1,000,000 | `miliyun` /mi.li.yun/ | all open syllables | acceptable loan; or `big-ten-ten-ten` |

**Alternative 1000**: `handrd` could become `han` (borrowed `hundred` trimmed to /han/) if we want a dedicated root. But `ten-ten` is more principled.

**Stress implications**: All compounds receive penultimate accent:
- `ten-wan` = ten-WAN (accent on second syllable)
- `tu-ten` = TU-ten (accent on first syllable)
- `ten-ten-wan` = ten-TEN-wan (accent on middle syllable)
This is regular and predictable.

**Rating**: CRITICAL. The number system is learner-facing, high-frequency, and currently contains the most flagrant phonotactic violations in the lexicon. `twelv` ending in /v/ is an outright breach of the final-obstruent ban.

---

## Summary Table

| Issue | Phonotactic Risk | Stress/Prosody Risk | Learnability Risk | Recommended Reform |
|-------|-----------------|--------------------|--------------------|--------------------|
| 1. Atomic threshold | HIGH | LOW | HIGH | Fix roots to (C)V first, THEN compound; target ~200 atoms |
| 2. PROFIL homonymy | NONE | HIGH (identical contour) | MEDIUM | Change "profit" to `profeto` /pro.FE.to/ |
| 3. SE noun vs -se suffix | NONE | MEDIUM (identical in sandhi) | LOW-MEDIUM | Change "sea" to `mar` /mar/ |
| 4. Numbers | CRITICAL | LOW | CRITICAL | Full decimal compounding: `ten-wan, ten-tu, tu-ten, ten-ten` |

## Meta-Recommendation

The number system should be repaired **immediately** (Issue 4). It is the only standby issue that constitutes a direct template violation in high-frequency vocabulary. The atomic-word threshold (Issue 1) should be addressed by a root reform pass that normalizes all >6-letter atoms to (C)V, after which compounding becomes safe. Issues 2 and 3 are lexical disambiguation tasks with phonological dimensions; they should be resolved after the structural repairs are complete.

Priority order: **4 > 1 > 2 > 3**.

---
*Phonologist — Standby Issues Deliberation*
*Focus: phonotactic compliance, stress/syllable structure, learnability, articulatory ease*

---

## Profession Suffix Deliberation

### Candidates Evaluated

#### 1. `-er` /er/ (User's Preference)

| Example | Surface | Syllabification | Syllable Count | Verdict |
|---------|---------|-----------------|----------------|---------|
| `lern-er` | /ler.ner/ | [ler.ner] | 2 | LEGAL — /r/ final is permitted |
| `sik-fix-er` | /sik.fik.ser/ | [sik.fi.kser] → [sik.fi.ker] if /ks/ banned? Wait. | 3 | CONDITIONAL: requires profession root to already be (C)V |
| `food-mak-er` | /fud.ma.ker/ | [fu.dma.ker] or [fud.ma.ker] | 3 | ILLEGAL: /d/ is not a permitted final consonant; `food` needs reform first |

**Phonotactic Analysis**: The suffix `-er` itself is /er/, a vowel-initial syllable that attaches cleanly to any legal stem ending in /n, m, l, r/ or a vowel. The problem is NOT the suffix; it is the profession *roots* that may end in illegal consonants or contain internal clusters.

- `lern` /lern/ — illegal /rn/ coda. Would need reform to `leri` /le.ri/ or `lern` → `ler` /ler/ (legal final /r/). If stem is `ler`, then `ler-er` = /le.rer/ = 2 syllables, perfectly legal.
- `fix` — contains /ks/ cluster. VELA has no /x/ phoneme. Would need to be `fiksi` /fik.si/ first. Then `fiksi-er` = /fik.si.er/ = 3 syllables, legal.
- `masin` /ma.sin/ — legal final /n/. `masin-er` = /ma.si.ner/ = 3 syllables, legal.

**Length Concern**: 3–4 syllable compounds for professions. VELA's "shorter=better" rule is a *preference*, not a phonotactic law. `temperaturu` (5 syllables) was ruled phonotactically legal. Length is acceptable if every syllable is (C)V.

**Compound cluster risk**: The suffix attaches to the end. Internal clusters only arise if the profession root itself is unreformed. E.g., `masin-fix-er` where `fix` is unreformed → `masin-fiks-er` → internal /nf/ if boundary is unclear? In compounds, the boundary preserves syllable structure: [ma.sin.fi.ker]. No new clusters are created at the morpheme boundary because `-er` is vowel-initial.

**Rating**: ACCEPTABLE — provided all profession roots are pre-reformed to (C)V. The suffix itself is phonotactically clean.

---

#### 2. `-po` /po/

| Example | Surface | Syllabification | Syllable Count | Verdict |
|---------|---------|-----------------|----------------|---------|
| `lern-po` | /lern.po/ | [lern.po] | 2 | ILLEGAL: /rn/ coda in stem |
| `lerni-po` | /ler.ni.po/ | [ler.ni.po] | 3 | LEGAL after reform |
| `fiksi-po` | /fik.si.po/ | [fik.si.po] | 3 | LEGAL |

**Phonotactic Analysis**: Vowel-initial suffix, same as `-er`. No phonotactic risk from the suffix itself. The /p/ is an onset, not a coda. Identical boundary behavior to `-er`.

**Length**: Same as `-er` when attached to reform stems. No difference in syllable count.

**Rating**: ACCEPTABLE — but offers no phonotactic advantage over `-er`.

---

#### 3. `-ist` /isti/ and `-isti` /isti/

| Example | Surface | Syllabification | Syllable Count | Verdict |
|---------|---------|-----------------|----------------|---------|
| `lern-ist` | /ler.nist/ | [ler.nist] → [ler.nis.ti]? | 2 if /nist/ coda, else 3 | BORDERLINE: /nst/ is a CCC cluster, illegal |
| `lern-isti` | /ler.nis.ti/ | [ler.nis.ti] | 3 | LEGAL |

**Phonotactic Analysis**: If the suffix is monosyllabic /ist/ or /nst/ depending on syllabification, it creates a CCC cluster or at least a CC coda with /st/. /s/ and /t/ are obstruents, and /t/ is not a permitted final consonant. The cluster /nst/ violates the (C)V template.

If we force syllabification as [ler.nis.ti], we are essentially using a disyllabic suffix `-isti` /is.ti/. This is legal but adds a syllable compared to `-er` /er/.

**Comparison**: `ler-ner` (2 sy) vs `ler-nis-ti` (3 sy). `-er` is shorter and equally legal.

**Rating**: INFERIOR — requires longer form to be legal; shorter form violates template.

---

#### 4. `-or` /or/

| Example | Surface | Syllabification | Syllable Count | Verdict |
|---------|---------|-----------------|----------------|---------|
| `lern-or` | /ler.nor/ | [ler.nor] | 2 | LEGAL — /r/ final permitted |

**Phonotactic Analysis**: Identical to `-er` in every phonotactic dimension. Both are VC syllables that start with vowel /o/ vs /e/. No cluster risk, same length.

**Non-phonological concern**: User flags historical masculine gender marking in Romance. Phonologist does not rule on morphology/sociolinguistics, but notes that phonotactically `-or` = `-er` in quality.

**Rating**: ACCEPTABLE — phonotactic twin of `-er`. Tie-breaker must come from other disciplines.

---

#### 5. No Suffix

| Example | Surface | Syllabification | Syllable Count | Verdict |
|---------|---------|-----------------|----------------|---------|
| `lern` | /lern/ | [lern] | 1 | ILLEGAL: /rn/ coda |
| `leri` | /le.ri/ | [le.ri] | 2 | LEGAL after reform |

**Phonotactic Analysis**: Requires that *every* profession root ends in a vowel. Many current roots do not: `lern` /rn/, `teach` /tʃ/ or VELA-equivalent, `build` /ld/, etc. A mass reform would be needed.

**Length**: Potentially shorter (1–2 syllables vs 2–3 with suffix). But if reform forces addition of a final vowel, the gain is minimal. `lern` → `leri` (2 sy) vs `lern-er` → `ler-er` (2 sy). No length advantage in practice.

**Ambiguity risk**: Without a suffix, profession words are indistinguishable from verbs/roots in isolation. Phonologist notes that homophony between content words and grammatical roles is a standing concern (cf. Issue 3, SE noun vs -se suffix).

**Rating**: RISKY — requires massive root reform and creates ambiguity with verbs.

---

### Syllable-Count Comparison Table

| Strategy | Reform needed? | Avg syllables (post-reform) | Illegal clusters created? | Suffix itself legal? |
|----------|---------------|----------------------------|---------------------------|----------------------|
| `-er` /er/ | Medium (roots only) | 2–3 | No | Yes |
| `-po` /po/ | Medium (roots only) | 2–3 | No | Yes |
| `-ist` /isti/ | Medium (roots only) | 3 | No (if disyllabic) | Only as `-isti` |
| `-or` /or/ | Medium (roots only) | 2–3 | No | Yes |
| No suffix | High (all roots) | 1–2 | No (if reformed) | N/A |

---

### Meta-Assessment

**Key Question 1**: Does `-er` create acceptable compounds phonotactically?
> **Yes.** The suffix is vowel-initial and attaches transparently. The burden of legality falls on the profession roots, not on the suffix. Any profession root ending in /n, m, l, r/ or a vowel produces a legal compound. Roots ending in illegal consonants need reform *regardless* of which suffix is chosen (except "no suffix," which requires reform for ALL roots).

**Key Question 2**: Are 3–4 syllable profession words too long?
> **No.** Length is not a phonotactic violation. The "shorter=better" rule is a preference, not a template constraint. `temperaturu` (5 syllables) was explicitly ruled phonotactically legal in Issue 1. If VELA can tolerate 5-syllable atoms, it can tolerate 3-syllable compounds. Stress remains penultimate in compounds: `SIK-fi-ker` → /sik.FI.ker/ (accent on penult), regular and predictable.

**Key Question 3**: Does compound + suffix create internal clusters?
> **No new clusters are created at the morpheme boundary.** `-er` is vowel-initial /er/. The preceding syllable's coda is the coda of the profession root. If the root is legal, the boundary is legal. Example: `masin-fix-er` assumes `fix` is unreformed. If `fix` is reformed to `fiksi`, the compound is `masin-fiksi-er` → [ma.sin.fik.si.er], all (C)V. The problem is the root, not the suffix.

---

### Recommendation

**Rate**: `-er` / ★★★★★ | `-po` / ★★★★☆ | `-or` / ★★★★☆ | `-ist` / ★★☆☆☆ | No suffix / ★★☆☆☆

**Recommend: `-er` /er/**

**Phonological Evidence**:
1. Suffix is a single open syllable /er/ — fully (C)V compliant.
2. Vowel-initial attachment creates no boundary clusters.
3. Produces the shortest legal profession forms (2 syllables for reformed roots like `ler-er`, 3 for longer roots).
4. `-ist` requires disyllabic realization /is.ti/ to avoid CCC cluster, making it inherently longer.
5. `-po` and `-or` are phonotactic equivalents to `-er`; they neither help nor hurt. Tie must break elsewhere.
6. "No suffix" does not solve any phonotactic problem (roots still need reform) and introduces ambiguity.

**Caveat**: This recommendation is conditioned on a **pre-suffix root reform pass**. All profession roots must be normalized to (C)V before suffixation. If that precondition is not met, *all* suffix candidates degrade equally. The Phonologist strongly recommends that the root reform be decoupled from the suffix choice and treated as a prerequisite.

---
*Phonologist — Profession Suffix Deliberation*
*Focus: phonotactic compliance, syllable economy, compound boundary integrity*
