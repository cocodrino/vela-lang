# VELA Conlang Project: Phonology Deep Dive
## Research Document 1 — Sound Systems, Phonotactics & Natural Classes

---

## 1. Introduction: What Makes a Phonology Feel "Natural"?

A phonology is the system of distinctive sounds (phonemes) in a language and the rules governing how they combine. When we describe a phonology as feeling **organic** or **natural**, we mean it exhibits patterns that are common across human languages, avoids improbable or marked structures, and has internal consistency — its phonotactic constraints follow from its phoneme inventory rather than contradicting it.

By contrast, **constructed** phonologies often suffer from:
- Perfect symmetry in consonant/vowel ratios that never occurs in natural languages
- Unmotivated consonant clusters that violate sonority principles
- Invented phonemes with no natural class membership
- Phonotactics that don't follow from the inventory (e.g., complex codas but no complex onsets)

This document surveys how natural languages design their sound systems and extracts principles for building VELA's phonology.

---

## 2. The Sound Inventory: What Segments Do Languages Use?

### 2.1 Consonant Inventories

The UCLA Phonological Segment Inventory Database (UPSID) catalogs phoneme inventories across 451 languages. Key findings:

**Common Consonants (found in 50%+ of languages):**
| Phoneme | Description | Approx. % of languages |
|---------|-------------|----------------------|
| /a/ as vowel | open vowel | ~90% |
| /m/, /n/ | nasals | ~90% |
| /k/, /p/, /t/ | voiceless stops | ~85% |
| /s/ | voiceless alveolar fricative | ~75% |
| /l/ | lateral approximant | ~70% |
| /w/, /j/ | glides | ~65% |

**Rare or Absent Consonants:**
- Click consonants: limited to Khoisan and some Bantu languages
- Pharyngeals (ħ, ʕ): rare, associated with Semitic languages
- Lateral fricatives (ɬ, ɮ): uncommon
- Voiced uvular stop /ɢ/: very rare
- Bilabial fricative /ɸ/ and /β/: uncommon outside Japanese and Ewe

**The "Implicational Universal" Pattern:**
If a language has a rare sound (e.g., /ɬ/), it almost always also has more common sounds from the same natural class (e.g., /s/). This is called **harmonic inventory expansion**.

**VELA Recommendation:** Build a consonant inventory that expands from common sounds outward. Start with the "core" (p, t, k, m, n, s, l, w, j) and only add more exotic segments if motivated by aesthetic goals. Avoid rare segments without good reason.

### 2.2 Vowel Inventories

Vowel inventories are generally smaller and more constrained than consonant inventories.

**Vowel Size Correlations:**
- **2-vowel systems** (i, u, sometimes a): very common in small inventories (Rotokas, Chuukese)
- **3-vowel systems** (i, u, a — the "universal" triangle): extremely common (Swahili, Quechua, Turkish)
- **5-vowel systems** (i, e, a, o, u or i, ɪ, e, æ, ɑ, ə): common in European languages
- **6-10 vowel systems**: occur but less common; often involve vowel length or diphthongs

**Vowel Height Hierarchy:** Languages almost universally distinguish vowel height (high vs. non-high) before distinguishing frontness (front vs. back). A language with /e/ and /o/ but no /i/ and /u/ is essentially unattested.

**VELA Recommendation:** A 5-vowel system (i, e, a, o, u) is a safe, naturalistic choice that avoids the sterility of a 3-vowel system while remaining tractable. If VELA's aesthetic calls for something more unusual, consider a **vowel length distinction** (short/long pairs) rather than adding more vowel qualities.

### 2.3 Cross-Linguistic Survey: 20+ Languages

| Language | Consonants | Vowels | Notable Features |
|----------|-----------|--------|-----------------|
| **English** | ~26 phonemes | ~14-20 (diphthongs) | Complex onset/clusters, 3 latch consonants (ŋ missing word-initially) |
| **Spanish** | 17 | 5 (a,e,i,o,u) | No /ʃ/, /dʒ/,voiced fricatives except /β/ and /ɣ/ |
| **Japanese** | 14 | 5 (a,i,u,e,o) | No consonant clusters; syllable-timed |
| **Hawaiian** | 8 | 5 | Very small inventory; ʻokina (glottal stop) |
| **Mandarin** | 21 | 6 (with tones) | Retroflex series, aspirated stops |
| **Arabic** | 28 | 3 (a,i,u) + diphthongs | Emphatic consonants (pharyngealized), no /p/, /v/ |
| **Korean** | 19 | 10 (monophthongs + tense/aspirated) | Three-way stop contrast (plain/tense/aspirated) |
| **Georgian** | 28 | 5 | Extensive consonant clusters, ejectives, uvulars |
| **Inuktitut** | ~15 | ~3 | Long polysynthetic words, postbases |
| **Hausa** | ~32 | 5 (with gemination) | Tonal language, implosives |
| **Thai** | 21 | 18 (with register) | Five-way stop distinction, tones |
| **Mãori** | 10 | 5 | No /s/ (historically), simplified clusters |
| **Turkish** | 24 | 8 (including 3 rounded front) | Vowel harmony, no clusters |
| **Quechua** | 16 | 3 (a,i,u) | Three-vowel system, evidentiality |
| **Finnish** | ~17 | ~16 (including length) | Long/short vowel pairs, no voiced fricatives |
| **Amharic** | 31 | 7 | Ethiopic script, ejectives, pharyngeals |
| **Navajo** | ~31 | 4 | Tonal, complex verb morphology |
| **Fijian** | 16 | 5 | No /s/, prenasalized stops |
| **Mongolian** | 26 | 14 (including length) | Vowel harmony, uvulars |
| **Greek** | 13 | 5 | Rich consonant cluster system |
| **Czech** | 20 | 10 | Complex clusters, ř (raised alveolar) |
| **Rotokas** (Papua) | 6 | 5 | One of smallest inventories |
| **Ubykh** (extinct) | 81 | 2 | Largest known consonant inventory |
| **L普通话** | 22 | 10 | Tonal, retroflex series |

---

## 3. Natural Classes of Sounds

A **natural class** is a set of phonemes that share distinctive features and behave similarly in phonological processes.

### 3.1 Major Natural Classes

**Obstruents:** Stops + fricatives (produced with turbulent airflow). In phonological rules, these often pattern together vs. sonorants (m, n, l, r, w, j).

**Sonorants:** Produced with a more open vocal tract, include nasals, liquids, glides, and vowels. They function as syllable nuclei in languages without vowel-less syllables.

**Coronals:** Sounds produced with the tongue blade or tip (t, d, s, z, n, l, r). Cross-linguistically, coronals are the most unmarked class — they often substitute for other classes in phonological processes, and languages are more likely to *lack* non-coronal sounds than to lack coronals.

**Labials:** Sounds produced with the lips (p, b, m, f, v, w). Often pattern together in sound changes and phonotactic constraints.

**Dorsals:** Sounds produced with the back of the tongue (k, g, ŋ, x, ɣ). Include velar and sometimes uvular.

**Gutturals/Pharyngeals:** Sounds from the throat region (ħ, ʕ, h, ʔ). Strongly associated with Semitic languages; their presence often co-occurs with vowel reduction in neighboring sounds.

### 3.2 How Natural Classes Behave

Natural classes participate in **phonological processes** together. For example:
- In English, /t/ and /s/ are both coronals, and /t/ deletes before /s/ ("outs," "let's play")
- In Japanese, the labial /m/ blocks the nasal substitution of /n/ before /p/ and /b/
- In languages with "vowel harmony," only vowels of a certain height or backness can co-occur in a word

**VELA Recommendation:** Design VELA's phonotactics so that rules reference natural classes, not individual phonemes. For instance, if fricatives are prohibited in coda position, apply to the whole class rather than listing each fricative. This will make the language's sound patterns feel systematic and naturalistic.

---

## 4. Phonotactics: How Sounds Combine

Phonotactics governs which sound sequences are permitted in a language. This is one of the most powerful tools for giving a language its distinctive "feel."

### 4.1 Syllable Structure

**The Sonority Hierarchy** is a cross-linguistic ranking of segment types by " openness":

```
Vowels (highest sonority) > Glides > Liquids > Nasals > 
Voiced fricatives > Voiceless fricatives > 
Voiced stops > Voiceless stops (lowest sonority)
```

Syllables universally tend to exhibit **rising sonority** toward the nucleus and **falling sonority** away from it:

- **CV** (most universal): rising from consonant to vowel
- **CVC**: rising then falling — natural
- **VC**: falling into vowel — less marked
- **CCVC**: cluster must not violate rising sonority within the onset (*str-* works, *rtl-* doesn't)
- **CVCC**: codas with falling sonority toward the end — natural

**Languages with Simple Syllables:**
- Japanese: mostly CV, with limited VC
- Hawaiian: CV and V only (no closed syllables)
- Rotokas: only CV syllables

**Languages with Complex Syllables:**
- English: CCVCCCC in "strengths" (CCVCCC also exists in words like "text")
- Georgian: clusters of up to 8 consonants (gvprtskvni = "to be stripped")
- Polish: CCVCC, CCVCCC

### 4.2 Onset and Coda Preferences

- **Onsets:** Nearly universal (no known language prohibits all onsets, though some have none)
- **Codas:** More variable; about 30% of languages lack closed syllables entirely. Languages with complex codas often have complex onsets too, though not always.

**Implicational:** If a language allows complex codas, it tends to also allow complex onsets. The reverse is not always true.

### 4.3 Consonant Clusters

Not all clusters are equal. Clusters must respect:
1. **Sonority sequencing** (no sudden drops in sonority)
2. **Co-articulation** (sounds with similar place/manner of articulation cluster more naturally)
3. **Place of articulation** (coronal + labial is more natural than velar + labial in clusters)

Examples of natural clusters:
- /pl/, /pr/, /tr/, /kr/, /kl/ — stop + liquid (very common)
- /st/, /sp/, /sk/ — fricative + stop (common)
- /ŋg/, /nd/ — nasal + voiced stop (natural in codas)

Examples of unnatural clusters (rare or unattested):
- /ŋl/ — velar nasal + liquid (very rare)
- /xm/ — fricative + nasal
- /tl/ — voiceless alveolar stop + lateral (though it exists in some Athabaskan languages)

### 4.4 Phonotactic Patterns Across Languages

| Language | Onset Max | Coda Max | Notable Pattern |
|----------|-----------|----------|----------------|
| Japanese | 1 (C) | 1 (C) | No consonant clusters |
| Hawaiian | 1 | 0 | Open syllables only |
| English | 3 (CCV...) | 4 (...VCCC) | Complex clusters |
| Czech | 4 (CCCV) | 4 | Complex clusters |
| Georgian | 8 | 8 | Massive clusters |
| Korean | 2 (C+glide/liquid) | 2 | No /sC/ clusters |

### 4.5 Vowel Harmony and Co-occurrence Restrictions

Many languages restrict which vowels can co-occur within a word through **vowel harmony**:
- **Turkish:** Vowels must agree in frontness and roundedness (e.g., *ev-ler* "house-PL" but *oda-lar* "room-PL")
- **Finnish:** Two harmony systems: back/front and a/ä
- **Hungarian:** Vowel harmony with suffix allomorphy
- **Mongolian:** Vowel harmony with rounding

**VELA Recommendation:** VELA could adopt a vowel harmony system to add phonological elegance and create interesting derivational patterns. A simple front/back harmony (Turkish-style) would add naturalism without excessive complexity.

---

## 5. What Makes a Phonology Feel "Organic" vs. "Constructed"?

### 5.1 Hallmarks of Constructed Phonologies

1. **Perfect symmetry:** Equal numbers of voiced/voiceless pairs, equal vowel triangles — real inventories are always a bit irregular
2. **Arbitrary phoneme choices:** No natural class coherence
3. **No phonotactic motivation:** Complex clusters without sonority-based explanation
4. **No allophonic variation:** Natural languages almost always have predictable phonetic variation (e.g., English /t/ is aspirated at the start of stressed syllables, unreleased at the end, flapped in the middle)
5. **No syllable structure implications:** No relationship between what onsets and codas are possible

### 5.2 Hallmarks of Organic Phonologies

1. **Slight asymmetry:** Not perfectly mirror-image inventories
2. **Natural classes drive the system:** Rules and constraints reference classes
3. **Phonotactics follow from inventory:** You can explain *why* certain clusters don't exist
4. **Allophonic patterns:** Complementary distribution of variants
5. **Historical plausibility:** The inventory could plausibly derive from a previous state through attested sound changes

### 5.3 Strategies for Organic Feel

- **Add allophonic rules:** /k/ → [kʲ] before front vowels, [kʰ] word-initially
- **Add phonotactic constraints** that aren't just "every combination is allowed"
- **Add co-occurrence restrictions** (e.g., /s/ cannot appear before /r/)
- **Create a proto-language** and derive VELA's phonology from it (see Language Evolution document)
- **Add a sub-phonemic dimension:** gemination (length), aspiration, nasalization, or tone

---

## 6. Tonal Systems

Tone is a suprasegmental feature found in ~60-70% of the world's languages.

### 6.1 Types of Tone Systems

- **Register tones** (Level tones): High, Mid, Low — e.g., Yoruba (3 tones), Standard Chinese (4 tones)
- **Contour tones:** Rising, Falling, Rising-Falling — e.g., Thai (5 tone levels + contours)
- **Dot-writers accent** (pitch accent): One syllable in the word gets special prominence (Japanese, Swedish)

### 6.2 Tone and Other Features

Tonal languages often reduce the complexity of their consonant and vowel systems (smaller inventories) — a trade-off called **tonal compensation**. This is one reason East Asian languages often have smaller consonant inventories than European languages.

**VELA Recommendation:** If VELA uses tone, keep the inventory smaller to compensate. A 2-tone (High/Low) system on a 5-vowel, 17-consonant inventory would be more naturalistic than 4 tones on a complex inventory. Alternatively, a pitch-accent system (like Japanese) gives the flavor of tone without full tonal complexity.

---

## 7. Suprasegmentals: Stress, Length, and Weight

### 7.1 Stress Systems

- **Fixed stress:** Always on the same syllable (Penultimate in Polish, antepenultimate in Finnish, initial in Welsh)
- **Free stress:** Varies by word, often predictable from syllable weight
- **Weight-sensitive:** Stress goes to heavy syllables (those with long vowels or codas)

### 7.2 Gemination (Consonant Length)

Gemination is a distinctive feature in many languages:
- **Italian:** /ˈfatto/ vs /ˈfato/ (distinguishes "done" from "fate")
- **Japanese:** /hatta/ vs /hata/ (different words)
- **Finnish:** /tuli/ vs /tuːli/ (fire vs. came)
- **Hungarian:** Long consonants and vowels

Gemination often arises from consonant clusters simplifying or from loanword adaptation.

---

## 8. VELA-Specific Recommendations

### 8.1 Recommended Phoneme Inventory

Based on the research above, VELA should consider:

**Consonants (17-20 phonemes):**
- Stops: p, t, k (and possibly voiced b, d, g)
- Fricatives: s, ʃ, x or f, v, z (keep small — 2-3 fricatives)
- Nasals: m, n (consider ŋ in coda only)
- Liquids: l, r (consider tap/flap as allophone of r)
- Glides: w, j
- Optionally: voiced counterparts or ejectives depending on aesthetic

**Avoid:** θ, ð (English "th" sounds) — these are rare cross-linguistically and difficult for most speakers. Also avoid pharyngeals unless specifically motivated.

**Vowels (5 phonemes):**
- i, e, a, o, u — the universal vowel triangle

**Optional:** 
- Vowel length distinction (short/long pairs)
- Nasalized vowels
- Two-tone system

### 8.2 Recommended Phonotactics

- **Syllable structure:** CV, CVC, with CVCC possible in codas (maximum 2 consonants)
- **Onsets:** Up to 2 consonants (CC), no clusters violating sonority
- **Codas:** Up to 2 consonants (CVC, CVCC), prefer natural clusters (nasal+stop, fricative+stop)
- **No clusters across syllable boundaries** that are phonetically impossible
- **Vowel harmony:** Simple front/back harmony in derivational suffixes

### 8.3 Recommended Allophonic Rules

1. Voiceless stops: aspirated word-initially before stressed vowels
2. /t/ → [ɾ] between vowels (tap/flap)
3. Velar /k/ → [c] before front vowels
4. Nasal + voiceless stop at coda: the vowel is partially nasalized
5. Vowel lengthened in stressed open syllables

### 8.4 Phonological "Signature"

To make VELA feel distinctive, add ONE unusual feature that is attested in natural languages:
- **Ejectives** (found in ~20% of languages: Georgian, Quechua, Amharic, Navajo)
- **Tone** (very common globally)
- **Gemination** (Italian, Japanese, Finnish)
- **Vowel harmony** (Turkish, Finnish, Mongolian)
- **Glottal stop** as a phoneme (Hawaiian, Arabic)
- **Labial-velar approximants** (w before front vowels shifts to ɥ)

---

## 9. Sources & Further Reading

- Maddieson, I. (1984). *Patterns of Sounds*. Cambridge University Press. [UPSID basis]
- Mielke, J. (2008). *The Emergence of Distinctive Features*. Oxford University Press.
- Hayes, B. (2009). *Introductory Phonology*. Wiley-Blackwell.
- Ladefoged, P. & Johnson, K. (2014). *A Course in Phonetics* (7th ed.). Cengage.
- PHOIBLE Online: https://phoible.org/
- WALS (World Atlas of Language Structures): https://wals.info/
- Crystal, D. (2010). *The Cambridge Encyclopedia of Language* (3rd ed.).

---

*Document prepared for the VELA Conlang Project*
*Author: Deep Research Subagent*
*Version: 1.0*
