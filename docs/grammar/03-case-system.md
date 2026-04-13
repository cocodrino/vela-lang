# VELA Case System — 4 Cases

> Based on `INITIAL_RESEARCH.md` + deep research in morphology, alignment, and typology.  
> Status: **DESIGN DECISION MADE** — to be implemented in Stage 3.

---

## Why VELA Needs a Case System

English has lost most of its case system (only pronouns retain it: I/me/my). This forces fixed word order — English relies on SVO to know who did what to whom. 

Spanish has noun-adjective agreement and some case-like prepositions (a, de) but no noun case inflection.

VELA takes the **agglutinative path**: transparent suffixes, one meaning each, never fused.

**The goal:** Maximum clarity with minimum complexity. 4 cases is the sweet spot.

---

## The 4 Cases of VELA

### 1. Nominative — (no suffix)

The subject of the sentence. Who does the action.

```
Mi si la film.          → I see the film.        (mi = NOM)
Yu lik la sonj.         → You like the song.     (yu = NOM)
La man si la film.      → The man sees the film. (man = NOM)
```

### 2. Accusative — suffix **-a**

The direct object. Who receives the action.

```
Yu si la man-a.         → You see the man.        (man → man-a)
Mi her la vois-a.      → I hear the voice.       (vois → vois-a)
De watc la siti-a.     → They watch the city.    (siti → siti-a)
```

### 3. Genitive — suffix **-de**

Possession, origin, relationship.

```
La man-de hous.         → The man's house.
Yu her la sun-de lait.  → You hear the sunlight. (the light OF the sun)
Mi lik la famili-de mi fren. → I like my friend's family.
```

### 4. Locative — suffix **-en**

Location (place), time (when), or state.

```
La man es in la siti-en.  → The man is in the city.       (location)
La miti-en es long.        → The meeting is long.          (state)
Mi liv in la siti-en.     → I live in the city.          (habitual location)
De kom at las dei-en.    → They come at the last day.    (time)
```

---

## Interaction with Plurals

The plural suffix comes AFTER the case suffix:

```
 Singular:  la man     (NOM)  |  la man-a    (ACC)
 Plural:    la man-s   (NOM)  |  la man-s-a  (ACC)
              ↑plural     ↑case      ↑plural     ↑case
```

This follows the **agglutinative principle**: more specific meaning (plural) goes closer to the root.

### Full Paradigm: man (person)

| Case | Singular | Plural |
|------|----------|--------|
| **Nominative** | man | man-s |
| **Accusative** | man-a | man-s-a |
| **Genitive** | man-de | man-s-de |
| **Locative** | man-en | man-s-en |

---

## Interaction with Adjectives

Adjectives agree in case with the noun they modify (agglutinative, transparent):

```
NOM:  La big man si la film.
ACC:  Mi si la big man-a.
GEN:  La big man-de hous es nais.
LOC:  La big man-en in la siti es priud.
```

Adjective endings: -im (adjective) → -im-a (acc), -im-de (gen), -im-en (loc).

---

## Interaction with Pronouns

Pronouns also take case suffixes (transparently):

| Pronoun | NOM | ACC | GEN | LOC |
|---------|-----|-----|-----|-----|
| I | mi | **mi-a** | **mi-de** | **mi-en** |
| you | yu | yu-a | yu-de | yu-en |
| he/she/it | li | li-a | li-de | li-en |
| we | wi | wi-a | wi-de | wi-en |
| they | de | de-a | de-de | de-en |

### Examples:
```
NOM:  Mi go a la siti.         → I go to the city.
ACC:  Yu si mi-a.             → You see me.
GEN:  La man her mi-de vois.  → The man heard my voice.
LOC:  Wi liv in la siti-en.    → We live in the city.
```

**Note:** `mi-de` (my) is common enough that it contracts:
- `mi-de` → `mid` (optional, acceptable in speech)
- `yu-de` → `yud`
- `li-de` → `lid`

---

## Case + Prepositions

Prepositions take the noun in **locative case** by default:

```
in  la siti-en   → in the city (location)
at  la stori-en  → at the story / at the moment (time/state)
on  la trak-en   → on the track (on)
from  la forst-en → from the forest (origin)
to  la plas-en   → to the place (direction)
```

When a preposition is present, the locative suffix can optionally simplify — but keeping it is always correct.

```
Mi liv in la siti-en.     → I live in the city.       (correct)
Mi liv in la siti.         → I live in the city.       (also correct — preposition already marks location)
```

---

## Case + The Verb "To Be" (bi)

With `bi` (to be), the locative marks state/location:

```
Mi es in la siti-en.       → I am in the city.    (location)
La man es strong-en.       → The man is in strength / is strong. (state)
Li es hapi-en.             → She is in happiness / is happy. (state)
```

The bare adjective form (without -en) is also acceptable:
```
Mi es hapi.               → I am happy.           (equivalent)
La man es strong.         → The man is strong.   (equivalent)
```

Both are grammatically correct. Use whichever sounds better.

---

## Systematic Sound Check

All case suffixes follow VELA's phonotactic rules:

| Suffix | Ends in | Valid (C)V? | Example |
|--------|---------|-------------|---------|
| **-a** (ACC) | vowel | ✅ V | man → man-**a** |
| **-de** (GEN) | vowel | ✅ V | man → man-**de** |
| **-en** (LOC) | vowel | ✅ V | siti → siti-**en** |

All follow **(C)V** — they end in vowel, which is perfect. No case suffix ever breaks the syllable rule.

---

## Cases NOT Included (Why 4 is enough)

| Case | Language example | Rejected because |
|------|-----------------|-----------------|
| **Dative** | German: *Ich gebe dem Mann* | Preposition `a` covers it: *Mi giv a la man.* |
| **Instrumental** | Russian: *s knigoy* | Preposition `wit` covers it: *Mi rit wit la pen.* |
| **Ablative** | Latin: *a casa* | Preposition `from` covers it: *Mi kom from la hous.* |
| **Vocative** | Spanish: *¡Juan!* |intonation covers it: *Halo Juan!* |
| **Partitive** | Finnish: *sataa* | Context or `som` covers it: *som la risn* |

**VELA's principle:** If a preposition can do the job, don't add a case suffix. Keep it simple.

---

## Design Decision Log

| Decision | Date | Source |
|----------|------|--------|
| 4 cases (NOM, ACC, GEN, LOC) | 2025-04-13 | Deep research + INITIAL_RESEARCH.md |
| Accusative: -a | 2025-04-13 | Phonotactic fit + Esperanto comparison |
| Genitive: -de | 2025-04-13 | Clear sound, doesn't clash with words |
| Locative: -en | 2025-04-13 | Spanish/Esperanto -en similarity for learnability |
| Case + plural: suffix order = case THEN plural | 2025-04-13 | Aglutinative principle |
| Prepositions + case: preposition overrides case suffix | 2025-04-13 | Simplicity — avoid double-marking |
| `bi` + LOC = state: both forms acceptable | 2025-04-13 | Flexibility without ambiguity |

---

## Implementation Checklist

```
□ Add NOM/ACC/GEN/LOC paradigm to every noun in core lexicon
□ Add case suffixes to all pronouns
□ Add adjective case agreement (-im → -im-a, -im-de, -im-en)
□ Test 100 sentences: do cases feel natural or forced?
□ Verify: no case suffix ever breaks (C)V rule
□ Add case examples to reference grammar
□ Update ROADMAP Stage 3 with this document
```
