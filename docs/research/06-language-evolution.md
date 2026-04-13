# VELA Conlang Project: Language Evolution
## Research Document 6 — Sound Changes, Grammaticalization, and Proto-Language Reconstruction

---

## 1. Introduction: Languages Are Always Changing

No natural language exists in a static form. Every language spoken today is the current point in a continuous chain of transformation stretching back tens of thousands of years. Languages change in their sounds (phonology), their word forms (morphology), their word order (syntax), and their meanings (semantics).

For the VELA conlang project, understanding language evolution is essential for three reasons:

1. **Naturalism:** Languages that never change feel artificial. VELA needs a history of change to feel like a living, organic system.
2. **Dialectal variation:** Different speech communities should evolve VELA in different directions over time.
3. **Proto-language design:** Creating a proto-language and deriving VELA's modern form from it is the single most effective technique for creating naturalistic phonology and morphology.

This document covers the mechanisms of language change and provides practical guidance for simulating evolution in VELA.

---

## 2. Sound Changes: The Engine of Phonological Evolution

### 2.1 What Is a Sound Change?

A sound change (phonological change) is a systematic shift in how a languagepronounces sounds over time. The key word is **systematic** — sound changes are not random substitutions but apply consistently wherever their structural conditions are met.

**Types of Sound Change:**

1. **Conditioned sound change** (phonologically conditioned):
   - A sound changes only in specific phonological environments
   - Example: In Old English, /k/ became /tʃ/ before front vowels (written as ⟨kǣr⟩ → /tʃɛər/, the origin of "church" from Old English *cirice*)

2. **Unconditioned sound change:**
   - A sound changes regardless of its environment
   - Example: The Great Vowel Shift in English, where all Middle English long vowels changed their quality

3. **Regular sound change:**
   - Applies without exception to all instances meeting its structural description
   - This is the basis of historical reconstruction

4. **Spelling pronunciation:**
   - Orthography influences pronunciation over time
   - Example: The /w/ in "write," "wrong" was once pronounced; the spelling preserved it after the sound was lost

### 2.2 Grimm's Law (First Germanic Sound Shift)

Perhaps the most famous sound change in historical linguistics is Grimm's Law, formulated by Jacob Grimm (of Brothers Grimm fame) in 1822.

**The Sound Shift:**
Proto-Indo-European voiceless stops became fricatives in Proto-Germanic:

| PIE | > Proto-Germanic | Example |
|-----|----------------|---------|
| /p/ | /f/ | Sanskrit *pitar* → English *father* |
| /t/ | /θ/ (later > /ð/) | Latin *tres* → English *three* |
| /k/ | /x/ (later > /h/) | Sanskrit *śvan* → English *hound* |

Additionally:
- PIE voiced stops /b/, /d/, /g/ → Proto-Germanic voiceless stops /p/, /t/, /k/
- PIE voiced aspirated stops /bh/, /dh/, /gh/ → Proto-Germanic voiced stops /b/, /d/, /g/

**Verner's Law (a complication):**
The fricatives created by Grimm's Law became voiced (/f/ → /v/, /θ/ → /ð/, /x/ → /ɣ/) when between voiced sounds, accounting for irregular correspondences like English "brother" vs. Sanskrit *bhrātar-*.

### 2.3 Major Categories of Sound Change

**Lenition (weakening):**
Sounds become "weaker" — stops become fricatives, fricatives become approximants:
- Latin *focus* → Italian *fuoco* (/k/ → /kw/) — but also *vīta* → *vita* → Italian *vita* (shortened)
- Spanish: Latin *octō* → *ocho* (/k/ > /tʃ/ > /k/)

**Fortition (strengthening):**
Sounds become "stronger" — fricatives become stops, approximants become fricatives (less common, often in specific environments):
- Latin *planus* → Spanish *llano* (no change in this direction actually; this is lenition)

**Assimilation:**
Sounds become more similar to neighboring sounds:
- *in- + lucid* → *lucid* (the /n/ assimilates to /l/)
- English: "cupboard" /kʌbərd/ — the /p/ and /b/ co-exist in an unusual cluster
- Common: nasal place assimilation (Latin *in- + bonus* → Italian *imbonire*)

**Dissimilation:**
Sounds become less similar to neighboring sounds:
- Latin *arbor* → Spanish *árbol* (/r/ → /l/) — dissimilation of /r/ in Latin *arbor*
- Italian: *quaderno* from Latin *quaternum* (dissimilation of /r/)

**Deletion:**
Sounds are lost:
- English: /k/ in "knight," /g/ in "gnat" — historical clusters where the first consonant was lost
- Spanish: Latin *octō* → *ocho* (the /t/ deleted)

**Epenthesis:**
Sounds are inserted:
- English: "empty" /ˈɛmti/ has a /p/ that historically was part of the word; "something" /ˈsʌmθɪŋ/ has epenthetic /θ/
- Japanese: syllable-final /n/ emerged from historical vowels

**Metathesis:**
Sounds swap positions:
- English: "brid" → "bird" (though this may be a spelling pronunciation); Old English *ācwestre* → "ask" (the /kw/ cluster was reordered)

### 2.4 VELA Application: Creating a Proto-Language

The most effective technique for creating a naturalistic conlang phonology is to:

1. **Design a proto-language** with a relatively simple phonology
2. **Apply systematic sound changes** to derive the modern language
3. **Create dialectal variation** by applying different changes in different regions

**Example VELA Proto-Language → Modern VELA:**

**Proto-VELA inventory:**
- Consonants: p, t, k, b, d, g, m, n, ŋ, s, h, l, r, w, j
- Vowels: a, i, u, e, o (5-vowel system)
- Syllable structure: CV, CVC

**Sound changes applied:**

1. **Intervocalic /s/ → /h/ → deleted:**
   - *asa* → *aha* → *a* (something → breath → gone)

2. **/k/ before front vowel → /tʃ/ (palatalization):**
   - *aki* → *atʃi* → "water"

3. **Final vowels deleted in polysyllabic words (final vowel syncope):**
   - *sulo* → *sul* (fire)

4. **Word-initial /g/ → /w/ (lenition):**
   - *gara* → *wara* (mountain)

5. **/r/ → /ɾ/ between vowels (tap):**
   - *para* → *paɾa* (city)

**Modern VELA phonology:**
- Consonants: p, t, k, b, d, g, m, n, ŋ, s, h, l, r, ɾ, w, j, tʃ
- Vowels: a, i, u, e, o
- Additional allophony: /k/ → [c] before front vowels; /t/ → [ɾ] between vowels

---

## 3. Grammaticalization Paths

### 3.1 What Is Grammaticalization?

**Grammaticalization** is the process by which content words (lexical items with concrete meaning) become grammatical markers (functional items expressing grammatical relationships). This is one of the most important and well-documented processes in language change.

**The Canonical Path:**
```
Content word → Grammatical word → Clitic → Affix (inflectional)
```

### 3.2 Classic Examples

**"Go" → Future Marker:**
- Old English: *willan* 'to want, to wish' (full verb)
- Middle English: *wollen* as auxiliary (I wollen go = I want to go)
- Modern English: *will* as future tense auxiliary ("I will go")

**"Have" → Perfect Marker:**
- Latin: *habēre* 'to have' (full verb)
- Romance languages: auxiliary use with past participles
- English: "I have eaten" — "have" grammaticalized from possession to perfect marker

**"Going to" → Future ("gonna"):**
- English *going to* (intention → future) → *gonna* (phonetically reduced)
- This is an ongoing grammaticalization visible in real time

**Postpositions → Case Markers:**
- Latin *-um* (direction) in *romam* (to Rome) ← *-om* (direction suffix)
- Many languages' case systems derive from older postpositions

**Demonstratives → Definite Articles:**
- Latin *ille* 'that (far)' → French *le* (definite article)
- English "the" from Proto-Germanic *þe* (demonstrative)

**Full Verb → Auxiliary:**
- English "have" in perfects, "be" in progressives, "do" in questions
- Each of these was once a full lexical verb

### 3.3 Mechanisms of Grammaticalization

**Semantic bleaching:** The specific meaning is lost, leaving only the grammatical function:
- "going to" (physical movement + intention) → future (no movement involved)

**Phonetic erosion:** The grammaticalized form becomes shorter and less prominent:
- *going to* → *gonna* (reduction)
- *want to* → *wanna*

**Coalescence:** The grammatical marker fuses with the host:
- Unstressed grammatical morphemes merge phonologically with the preceding or following content word

**Persistence:** Even after grammaticalization, traces of the original meaning can influence usage:
- English "will" still carries connotations of volition/intention

### 3.4 Grammaticalization in VELA

VELA's grammatical markers should feel as if they derive from older lexical sources:

**Example: Progressive aspect marker -sa-**
1. Start with a lexical verb meaning "to stay, to remain"
2. Grammaticalize to an auxiliary: *Mi sa-veni* → "I PROG-come" = "I am coming"
3. Fuse and erode: *Miveni* (from *Mi sa-veni*) — the progressive marker coalesces into a prefix

**Example: Future tense marker -lo-**
1. Start with a noun meaning "tomorrow" or "time ahead"
2. Grammaticize to a suffix: *Mi ven-lo* → "I come-FUT" = "I will come"
3. Shorten: *Mi venlo*

**Example: Evidential suffix -na- (visual evidence)**
1. Start with a verb "to see"
2. Grammaticalize to a clitic: *Mi veni-na* → "I come-see(EVD)" = "I saw it coming"
3. Fuse to become suffix: *Mivena*

---

## 4. Creating a Language Family from a Proto-Language

### 4.1 The Comparative Method

Historical linguists reconstruct proto-languages using the **comparative method** — identifying regular sound correspondences among related languages and working backward to the ancestral form.

For VELA, this means:
1. Design Proto-VELA (the ancestor)
2. Apply different sets of changes to create daughter languages
3. Document the sound correspondences between Proto-VELA and each daughter
4. Use the same correspondences to create the illusion of genetic relationship

### 4.2 Creating Daughter Languages

**Proto-VELA** → **Velite-I** (Northern dialect) + **Velite-II** (Southern dialect) + **Velite-III** (Eastern dialect)

| Change | Northern | Southern | Eastern |
|--------|----------|----------|---------|
| /s/ → /h/ intervocalic | Applied | Applied | Applied |
| /k/ → /tʃ/ before front vowels | Applied | → /ts/ | Unchanged |
| /r/ → /l/ between vowels | → /ɾ/ | → /l/ | → /r/ |
| Final -a deleted | Applied | Applied | Applied in monosyllables |
| /g/ → /w/ initial | → /ɣ/ | → /w/ | Unchanged |
| Vowel harmony in suffixes | Introduced | Not introduced | Introduced |

**Resulting Vocabulary Divergence:**

| Proto-VELA | Northern (Velite-I) | Southern (Velite-II) | Eastern (Velite-III) |
|-----------|--------------------|--------------------|--------------------|
| *para* (city) | *paɾa* | *pala* | *para* |
| *sara* (star) | *haha* | *saha* | *sara* |
| *gira* (river) | *wiɾa* | *wira* | *gira* |
| *kisa* (person) | *tʃiha* | *tsiːa* | *kisa* |

This creates the impression of three related but distinct languages — all derived from the same proto-language.

### 4.3 Dialectal Variation Within VELA

Even within a single VELA-speaking community, the following variations are naturalistic:
- **Sociolectal variation:** Upper classes vs. commoners pronouncing certain sounds differently
- **Generational change:** Younger speakers have a slightly different vowel system than elders
- **Regional variation:** The eastern provinces preserve /g/ while the western provinces lenite it
- **Register variation:** Formal speech preserves older forms; colloquial speech innovates

---

## 5. Specific Sound Change Patterns for VELA

### 5.1 Patterns That Add Naturalism

**1. Fortition in stressed syllables:**
- Vowels in stressed syllables resist reduction
- Vowels in unstressed syllables reduce to schwa /ə/ or delete entirely
- This is universal in languages with lexical stress

**2. Lenition in intervocalic position:**
- Consonants between vowels weaken: stops → fricatives → approximants → deletion
- This accounts for many vowel-final forms and consonant clusters

**3. Palatalization before /i/, /j/:**
- Velar /k/ → /tʃ/ before front vowels or glides
- Alveolar /t/ → /ts/ or /tʃ/ before /i/
- Very common sound change, attested in Romance, Slavic, and many other families

**4. Loss of final consonants:**
- Many languages lose word-final obstruents
- English: /t/ and /d/ lost in "last," "hand" in some dialects before consonants
- Spanish: Latin *occlūdere* → *cerrar* (completely different, but final -r reflects earlier forms)

**5. Vowel harmony in suffixes:**
- Umlaut/Harmony in Germanic, Turkic, Finnish, Mongolian
- Suffixes copy the vowel quality of the root's stem
- Adds elegant systematicity to morphology

**6. Nasal assimilation:**
- A nasal consonant takes on the place of articulation of a following consonant
- Latin *in- + bonus* → *imber* (actually different)
- English: *in-* + *possible* → *impossible* (partial assimilation of /n/)

### 5.2 Creating the Appearance of Age

**Archaisms:** Forms that are etymological correct but no longer phonologically productive:
- English: "knight" and "knee" once had pronounced /k/ and /g/; the spelling preserves an old pronunciation
- VELA can retain spellings or occasional forms that reflect older phonology

**Diglossia:** A language has two varieties — a "high" literary register preserving older forms, and a "low" colloquial register that has undergone more change:
- Classical Arabic vs. Colloquial Arabic dialects
- Latin vs. Romance languages
- VELA can have a Classical/formal variant with older phonology and morphology

---

## 6. Morphosyntactic Change

### 6.1 Word Order Changes

Languages can shift their basic word order over time. The most common shifts:

- **SOV → SVO** (very common): This is the most frequent shift. Proto-Indo-European was SOV; many daughter languages (English, Romance languages) became SVO
- **SVO → VSO** (less common): Celtic languages, Hawaiian
- **Rigid order emerges:** Languages with freer word order (due to case marking) often become more rigid as case systems erode

**What drives word order change?**
- **Prosodic pressure:** Languages develop rhythmic patterns that favor certain orders
- **Information structure:** Discourse patterns can favor certain orders
- **Contact:** Language contact can trigger order changes

### 6.2 Case Loss and Revival

Languages often lose case systems over time (English lost most of its case system by Middle English) and regain rigidity through prepositions or fixed word order.

However, languages can also **regain** case through grammaticalization:
- Definite articles develop from demonstratives
- Postpositions develop into case suffixes
- This creates a cycle of case → no case → new case

### 6.3 VELA's Morphosyntactic Evolution

VELA could undergo the following changes over its history:
1. **Stage 1:** VELA-I had a full case system (6-8 cases) and flexible SOV word order
2. **Stage 2:** As the case system eroded, word order became more fixed (SOV)
3. **Stage 3:** New grammatical markers (postpositions → clitics → suffixes) arose to compensate for lost case distinctions
4. **Stage 4:** Modern VELA has a reduced case system (4 cases) + fixed SOV order + agglutinative suffixes

This cyclical pattern is attested in language after language and would give VELA great historical depth.

---

## 7. Semantic Change

### 7.1 Types of Semantic Change

**1. Narrowing (specialization):**
- Old meaning is broader, new meaning is narrower
- *Deer* (any wild animal → just the specific animal)
- *Meat* (any food → specifically flesh)
- *Hound* (any dog → specific type of dog)

**2. Broadening (generalization):**
- Old meaning is narrow, new meaning is broader
- *Girl* (young female of any species → specifically human young female)
- *Dog* (specific breed → all dogs)
- *Voyage* (specifically a sea journey → any journey)

**3. Metaphorical extension:**
- *Head* (body part → front of something, leader of a group, etc.)
- *Foot* (body part → base of a mountain, unit of measurement)
- *Light* (illumination → not heavy, not serious)

**4. Melioration (improvement):**
- *Knight* (boy, servant → mounted warrior, honored title)
- *Pretty* (cunning, sly → attractive)

**5. Pejoration (worsening):**
- *Silly* (blessed, innocent → foolish)
- *Awful* (inspiring awe → terrible)
- *Gay* (happy → homosexual (change of connotation, now reclaimed))

### 7.2 VELA Semantic Change

VELA should show evidence of semantic change:
- **False friends:** Some words have drifted from their original meanings
- **Metaphorical extensions** from concrete to abstract domains
- **Semantic narrowing** in some fields (especially cultural concepts)
- **Semantic broadening** in others (especially borrowed words)

---

## 8. Sources & Further Reading

- Lass, R. (1997). *Historical Linguistics and Language Change*. Cambridge University Press.
- Campbell, L. (1998). *Historical Linguistics: An Introduction*. MIT Press.
- McMahon, A.M.S. (1994). *Understanding Language Change*. Cambridge University Press.
- Hock, H.H. & Joseph, B.D. (1996). *Language History, Language Change, and the Evolutionary Relationship of the Indo-European Languages*. John Benjamins.
- Bybee, J. (2015). *Language Change*. Cambridge University Press.
- Hopper, P.J. & Traugott, E.C. (2003). *Grammaticalization* (2nd ed.). Cambridge University Press.
- Lehmann, C. (2015). *Thoughts on Grammaticalization* (3rd ed.). eLaborate.
- The Stanford Historical Linguistics Manual: https://history-of-language.fandom.com/

---

*Document prepared for the VELA Conlang Project*
*Author: Deep Research Subagent*
*Version: 1.0*
