# VELA Conlang Project: Lexicography Methods
## Research Document 8 — Building a 1,000+ Word Lexicon Without Sounding Like English

---

## 1. Introduction: The Vocabulary Challenge

The hardest part of conlang design is vocabulary. With phonology, you can lean on universal patterns. With grammar, you can follow typological research. But with vocabulary — where every word requires a creative decision — the risk of Anglocentrism is highest, the work is most tedious, and the results are most visible.

A naturalistic lexicon for VELA should:
- Have **internal coherence** (words feel related to each other systematically)
- Avoid **calquing English** (translating English words one-for-one)
- Reflect **cultural specificity** (world-relevant vocabulary, not English-relevant vocabulary)
- Be **efficient** (1000+ words covering semantic space without bloat)
- Feel **earned** (not random, but also not transparently derived from real languages)

This document provides systematic methods for building VELA's lexicon — from root creation algorithms to compounding strategies to semantic field organization.

---

## 2. Root Creation: The Foundation

### 2.1 What Is a Root?

A **root** is the most basic, indivisible form of a word — a morpheme that cannot be further analyzed. In VELA, roots will be the building blocks from which all other words are derived or compounded.

**Types of roots:**
1. **Free roots** — can stand alone as complete words (VELA nouns, verbs)
2. **Bound roots** — must attach to other morphemes (VELA affixes, derivational morphemes)
3. **Compounding roots** — specialized for use in compounds

**VELA approach:** Start with free roots (100-200) and derive/compound the rest.

### 2.2 Root Creation Algorithm

**Step 1: Define the Phonological Canvas**
- Define VELA's syllable structure, consonant/vowel inventory, and phonotactic constraints (from the Phonology document)
- Generate all possible CVCV syllables that fit the constraints
- For a 5-vowel, 17-consonant language with CV(C) syllable structure: ~1,700 possible 2-syllable combinations

**Step 2: Create the Semantic Canvas**
- List the 100-200 most essential concepts (see Section 4: Semantic Fields)
- Organize them into priority tiers:
  - **Tier 1 (Critical):** Pronouns, basic verbs (be, have, do, go, come), natural categories (water, fire, person, animal, sun, moon), body parts, basic actions
  - **Tier 2 (Important):** Extended categories, more verbs, adjectives, numbers
  - **Tier 3 (Rich):** Cultural vocabulary, abstract concepts, specialized terms

**Step 3: Assign Sound-Meaning Pairs Systematically**
- Apply the phonosemantic map from the Sound Symbolism document
- High vowels for small/close/precise concepts
- Low vowels for large/distant/broad concepts
- Fricatives for cutting/sharp/cold
- Nasals for continuous/dark/heavy
- Liquids for flowing/soft/curved

**Step 4: Check for Coincidental Resemblance**
- Ensure roots don't accidentally look like real language words that would create unwanted associations
- A VELA word that sounds like an English profanity or taboo term should be avoided
- But a VELA word that resembles a Latin or Greek root is acceptable and even desirable (it adds scholarly aesthetic)

### 2.3 Root Generation Tools

| Tool | Description | URL |
|------|-------------|-----|
| **Vulgar** | Conlang vocabulary and grammar generator, with sound-change simulation | https://vulgarlang.com/ |
| **Lexifer** | Root word generator with frequency simulation | https://github.com/TolkWotansWordsmith/Lexifer |
| **Awkwords** | Simple syllable-based root generator | https://akana.conlang.org/tools/awkwords/ |
| **edi** | Polyglot generator | https://www.zompist.com/edi.htm |
| **The Conlang Lexicon** | Dictionary creation tool | Various |

**VELA Recommendation:** Use Vulgar or Lexifer to generate a phonetic framework, then manually curate and assign meanings according to VELA's phonosemantic principles.

---

## 3. Derivation: Building Words from Roots

### 3.1 Affixation

Affixation is the process of adding prefixes, suffixes, or infixes to roots to create new words. VELA should have a rich derivational morphology:

**Example VELA derivational suffixes:**

| Suffix | Category | Meaning | Example |
|--------|---------|---------|---------|
| *-li* | Verb-forming | Abstract action | *sāra* (river) → *sārali* (to flow) |
| *-ki* | Noun-forming | Person/agent | *kēmi* (knowledge) → *kēmiki* (knower, scholar) |
| *-ra* | Adjective-forming | Related to | *nocha* (night) → *nocherā* (nocturnal) |
| *-vo* | Noun-forming | Place/location | *kēmi* (knowledge) → *kēmivo* (school, place of knowledge) |
| *-te* | Verb-forming | Instrument | *sēka* (cut) → *sēkate* (blade, tool for cutting) |
| *-me* | Noun-forming | Result of action | *thaki* (break) → *thakime* (fragments, debris) |

### 3.2 Compounding

Compounding is combining two or more roots to create a new word. It is the most efficient way to expand vocabulary.

**Compounding strategies:**

**1. Endocentric compounds** (head-final or head-initial):
- The last/first element determines the overall category and meaning
- VELA: *novo-sāra* (new-river) = new river (literally "new" modifies "river")

**2. Exocentric compounds** (body part → whole):
- The meaning is not contained in either element
- English: *pickpocket* (person who picks pockets → the person)
- VELA could include these for culturally important concepts

**3. Appositional compounds:**
- Both elements contribute equally to the meaning
- VELA: *mēsa-tēka* (earth-sky) = world, landscape (earth AND sky)

**4. Coordinate compounds:**
- Two elements of equal status, connected by an implied "and"
- English: *mother-daughter* (mother and daughter)
- VELA: *ata-ama* (father-mother) = parents

**Compound Stress and Vowel Reduction:**
- In many languages, compounds have a distinctive stress pattern: primary stress on the first element, secondary on the last
- Vowels in non-final elements may reduce or shorten
- This is naturalistic and should be implemented in VELA

### 3.3 Conversion (Zero-Derivation)

Many languages allow conversion between word classes without morphological change:
- English: "to water" (verb) / "water" (noun) — same form
- VELA could allow: *sāra* (river, noun) → *sāra* (to flow, verb) with context determining the category

This is less common in agglutinative languages but attested in some.

---

## 4. Semantic Field Organization

### 4.1 What Are Semantic Fields?

A semantic field is a group of words that share a conceptual domain. The classic example is color terms — all colors belong to the "color" field. But semantic fields exist for every conceptual domain: kinship, body parts, weather, emotions, movement, etc.

**Why organize by semantic field?**
- Ensures coverage: if you start with "body parts," you'll automatically think of parts you might have missed (elbow, knuckle, shin)
- Detects gaps: if English has 10 words for a concept and you've only created 3, you know you need more
- Creates systematicity: words within the same field should follow consistent derivational patterns

### 4.2 Priority Semantic Fields for VELA

**Tier 1: Core Vocabulary (150-250 words)**

**Body (körper, soma):**
- Head, hair, eye, ear, nose, mouth, lip, tooth, tongue, chin, cheek, forehead, neck, shoulder, arm, elbow, hand, finger, thumb, nail, chest, heart, lung, stomach, liver, intestine, back, spine, hip, leg, knee, foot, heel, toe, skin, bone, blood, flesh, muscle

**Nature:**
- Sun, moon, star, sky, cloud, rain, snow, wind, storm, fire, water, river, lake, sea, ocean, mountain, hill, valley, forest, tree, leaf, root, seed, flower, grass, earth, soil, sand, stone, rock, metal, mountain, cave

**People:**
- Person, man, woman, child, mother, father, sibling, grandmother, grandfather, friend, enemy, king, slave, warrior, healer, hunter, speaker, listener

**Animals:**
- Dog, horse, cattle, bird, fish, snake, worm, insect, fly, bee, spider, mouse, wolf, bear, fox, deer, rabbit, eagle, crow, owl, frog, lizard

**Actions (basic):**
- Be, have, do, go, come, give, take, see, hear, smell, taste, touch, eat, drink, sleep, wake, live, die, kill, hit, cut, break, burn, pour, wash, dress, undress, speak, listen, think, know, want, fear, love, hate

**Objects:**
- Stone, knife, axe, fire, rope, pot, house, door, window, bed, chair, table, plate, cup, spoon, bag, basket, cloth, clothing, shoe, hat, medicine

**Space and time:**
- Here, there, near, far, up, down, in, out, on, under, before, after, today, tomorrow, yesterday, night, day, morning, evening, year, month, moon, season

**Quality (adjectives):**
- Big, small, long, short, thick, thin, heavy, light, hot, cold, wet, dry, clean, dirty, new, old, good, bad, sick, healthy, strong, weak, fast, slow, loud, quiet, bright, dark, red, white, black, green, yellow

---

**Tier 2: Extended Vocabulary (250-500 words)**

**Kinship (expanded):**
- Cousin (maternal/paternal distinction), nephew, niece, uncle, aunt, grandchild, in-laws, step-parent, half-sibling, twin

**Emotions (expanded):**
- Happy, sad, angry, afraid, surprised, disgusted, ashamed, proud, jealous, lonely, excited, bored, content, frustrated, hopeful, despair, envy, shame, guilt, gratitude, compassion, loneliness, nostalgia

**Nature (expanded):**
- Fog, mist, dew, frost, hail, thunder, lightning, tide, wave, swamp, desert, island, beach, shore, cliff, waterfall, spring (water source), pond, creek, stream

**Actions (expanded):**
- Push, pull, carry, lift, throw, drop, tie, untie, open, close, cover, hide, seek, find, lose, steal, buy, sell, trade, build, destroy, plant, harvest, hunt, cook, weave, sew, paint, carve, sing, dance, play, laugh, cry, shout, whisper, read, write, count, measure, weigh

**Properties (expanded):**
- Sharp, dull (not sharp), smooth, rough, soft, hard, round, square, flat, deep, shallow, narrow, wide, tall, high, low, steep, straight, curved, crooked, bitter, sour, sweet, salty

---

**Tier 3: Cultural/Aesthetic Vocabulary (300+ words)**

This is where VELA's cultural identity emerges most strongly. The words here should NOT map one-to-one with English vocabulary — they should reflect VELA's unique cultural preoccupations.

**Example cultural vocabulary (inspired by hypothetical VELA culture):**

| English concept | VELA word | Note |
|----------------|-----------|------|
| Honor (specifically military) | *dhēra* | Related to the root for "fire/flame" — honor is the warrior's fire |
| Hospitality ritual | *nakhōmi* | Compound: guest-water-food; the word means the whole ritual |
| Forbidden knowledge | *velēki* | vel- (hidden) + -ēki (sacred); sacred hidden things |
| A particular type of grief | *mōrani* | Specifically the grief of losing a homeland; refugee grief |
| Skill-wisdom | *sērakhi* | Practical knowledge that comes from doing, not books |

### 4.3 Words VELA Should NOT Have (Yet)

Some English concepts don't belong in a natural language at low frequency:
- **Technology-specific:** computer, internet, electricity, algorithm (unless VELA's culture has these)
- **Western philosophical abstractions:** democracy, capitalism, philosophy (unless VELA's culture has them)
- **Non-applicable categories:** "week" (7-day cycle is arbitrary — may not fit VELA's calendar)
- **Western calendar:** "January," "Monday" (named after Roman gods/JW planets) — VELA may have different temporal divisions

---

## 5. Avoiding Anglocentrism in Lexicon Design

### 5.1 The Problem of False Friends

When creating words for VELA, be careful not to produce **false friends** — VELA words that look or sound like English words but have different meanings (attractive as lexical choices, but confusing).

**Examples to avoid:**
- VELA /bata/ sounding like English "batter" → unintended association
- VELA /filo/ sounding like "philo-" → unintended philosophical associations
- VELA /novo/ sounding like English "nova" → unintended association

### 5.2 Cultural-Specific vs. Universal Concepts

Not all concepts are universal. Design VELA's core vocabulary around **universal concepts** (time, space, body, nature) and give VELA-specific vocabulary for culturally specific domains.

**Universal concepts (expect rich vocabulary):**
- Body parts (universal anatomy)
- Natural elements (water, fire, earth, air — though air may not be as salient in landlocked cultures)
- Kinship (family structure may differ but the concept is universal)
- Basic emotions (happy, sad, angry, afraid — basic emotions may be universal)

**Potentially culturally specific (handle with care):**
- Legal concepts: guilt, innocence, crime, punishment — these vary by culture
- Property: ownership is conceptualized differently in nomadic vs. settled cultures
- Social hierarchy terms: these vary enormously
- Technology: obviously varies

### 5.3 "Untranslatable" Words

VELA should have words that don't map cleanly to English — **untranslatables** that reveal the language's unique worldview. These are the most rewarding words to create:

- *dhēsuli* — the specific tiredness that comes from traveling, not from labor
- *velakhō* — the feeling of recognizing a place you've never been (déjà vu but for places)
- *mērama* — the sadness of an abandoned home
- *sēvikhi* — the wisdom of choosing the difficult right over the easy wrong
- *thokēni* — the sensation of forgetting something important

### 5.4 Loanwords and Borrowing

Natural languages constantly borrow vocabulary, especially for:
- New concepts (electricity, telephone)
- Prestigious cultural items (Sanskrit words borrowed into Japanese)
- Foreign foods, plants, animals
- Taboo subjects (some languages borrow taboo terms from other languages)

VELA should have a borrowing policy:
1. Decide whether VELA has had contact with other languages
2. If so, some loanwords may exist for foreign cultural items
3. Borrowing should follow VELA's phonotactics — foreign words are "nativized"

---

## 6. Number Systems

### 6.1 Types of Number Systems

Number systems vary enormously across languages:

**Quinary (base-5):** Counting on one hand
- Most common in indigenous Australian languages, some African languages

**Decimal (base-10):** Counting on both hands
- Most European languages, many worldwide

**Vigesimal (base-20):** Counting on fingers and toes
- Basque, Danish (partially), Mayan, Aztec (Nahuatl)

**Binary (base-2):** Found in some Papua New Guinea languages
- Very rare

**Body-part tally systems:**
- Some languages count using specific body parts in sequence, producing unusual bases

### 6.2 VELA Number System Recommendation

VELA should use a **quinary-decimal hybrid** — base-5 for the counting of small discrete objects, with extensions to base-10 for larger numbers:

| Number | VELA |
|--------|------|
| 1 | *wan* |
| 2 | *du* |
| 3 | *tre* |
| 4 | *ke* |
| 5 | *pan* |
| 6 | *pan-wan* (five-one) |
| 7 | *pan-du* |
| 10 | *des* |
| 11 | *des-wan* |
| 20 | *vīg* (base 20, optionally) |
| 100 | *hon* (10×10) |

Numbers above 5 should combine 5s and units:
- 6 = *pan wan* (five one)
- 7 = *pan du* (five two)
- 8 = *pan tre*
- 9 = *pan ke*
- 10 = *des*

---

## 7. Pronoun Systems

### 7.1 Pronoun Inventory

Pronouns are one of the most universal and culturally revealing parts of a lexicon.

**Minimal pronoun system (3 pronouns):**
- 1st person (I), 2nd person (you), 3rd person (he/she/it)

**Extended systems:**
- **1st person plural exclusive** (*we but not you*) vs. **inclusive** (*we and you*): Attested in many languages (Australian, Papuan, Oceanic, some African)
- **Dual number** (two of something): Attested in many languages
- **Trial number** (three of something): Found in some Oceanic languages

**Example pronoun systems:**

| Language | System |
|----------|--------|
| English | 1, 2, 3 + PL |
| Spanish | 1, 2, 3 + PL |
| Japanese | 1, 2, 3 + PL + polite forms |
|clus | 1, 2, 3 + PL + CL (clusive vs. inclusive) |
| Gilbertese | 1, 2, 3 + PL + DL + TR (trial) + PGL (paucal) |
|clus |
| Basque | 1, 2, 3 + PL + ergative/absolutive distinction |

### 7.2 Social/Politeness Distinctions

Pronoun systems often encode social relationships:
- **T-V distinction** (French *tu/vous*, German *du/Sie*, Spanish *tú/Usted*): Distinguishes intimate vs. formal address
- **Japanese:** *watashi/watakushi* (formal I), *boku* (casual masculine), *ore* (rough masculine), *washi* (elderly masculine)
- **Korean:** *jeo/na* (I, varying formality), *neo/nua* (you), with honorific register affecting all pronouns

**VELA could include:**
- A T-V distinction (intimate *-i* vs. formal *-u* endings on verbs)
- Respect markers for 2nd person when addressing elders
- Humble forms for 1st person in formal contexts

### 7.3 Demonstratives (This/That)

Demonstrative systems (this, that, these, those) vary in:
- **Distance distinctions:** 2-way (near/far: *this/that*), 3-way (+ remote), 4-way (+ visible/invisible)
- **Reference type:** Pointing to location, pointing to discourse referent, pointing to time
- **Case marking:** Demonstratives may carry case suffixes like nouns

**VELA demonstrative system:**
- *li-* (proximal: this, here, now) — speaker's immediate space/time
- *ka-* (medial: that near you, there) — addressee's space
- *vo-* (distal: that far, yonder) — beyond both speaker and addressee

With case marking: *li-nom* (this-NOM), *li-acc* (this-ACC), *li-gen* (this-GEN)

---

## 8. Quality Control: Making Words Feel Natural

### 8.1 The 80/20 Rule for Vocabulary

You don't need 1,000 perfect words to have a usable conlang. You need:
- **50-100 words for basic communication** (Toki Pona territory)
- **200-300 words for storytelling and simple texts**
- **500-700 words for rich literary and philosophical expression**
- **1,000+ words for a complete-feeling dictionary**

Prioritize the Tier 1 vocabulary and expand organically.

### 8.2 Avoiding the "Dictionary Feel"

The biggest danger in conlang lexicon creation is producing words that feel like a list rather than a living vocabulary:

**Avoid:**
- Every noun ending in the same vowel
- Too perfect symmetry in derivational patterns
- Words that are obviously translated from English word-for-word
- All words having the same syllable length

**Do:**
- Allow some irregularity (different syllable counts in roots)
- Vary the derivational patterns (some words derived, some compound, some loan)
- Let some words be shorter (ancient, core vocabulary) and some longer (derived, compound)
- Include onomatopoeia and ideophonic words

### 8.3 Word Frequency and Zipf's Law

In natural languages, word frequency follows **Zipf's Law** — the most common word is used about twice as often as the second most common, three times as often as the third, etc.

This means:
- The 10 most common words will account for ~25% of all word usage
- The 100 most common words will account for ~50% of all usage
- The long tail of rare words makes up a small percentage of actual usage

**VELA implication:** Spend the most effort on the 100-200 most common concepts. The 500th word will rarely be used and doesn't need to be perfect.

### 8.4 Testing VELA's Lexicon

**Translation test:** Take a well-known text (Pangram, Lord's Prayer, excerpts from familiar literature) and translate it into VELA. Note:
- Where did you run out of vocabulary?
- Which words felt forced or unnatural?
- Which translations felt like English in disguise?

**Etymology test:** Write a brief etymological sketch for 10 VELA words. Can you trace them back to roots? Do the derivations make sense? This reveals gaps in the morphological system.

**Community test:** Have someone else try to learn and use VELA's vocabulary. Where do they get confused? What feels intuitive vs. arbitrary?

---

## 9. Sample VELA Root Lexicon (100 Core Words)

### 9.1 Nouns

| VELA | Meaning |
|------|---------|
| *āmi* | water |
| *sāra* | river |
| *dhara* | fire |
| *mēsa* | earth, ground |
| *tēka* | sky |
| *kēri* | sun |
| *lēna* | moon |
| *vēthi* | star |
| *thōni* | person, human |
| *nōma* | man |
| *sīma* | woman |
| *kēma* | child |
| *āta* | mother |
| *āma* | father |
| *dhēsa* | house |
| *thōri* | stone |
| *pēla* | tree |
| *sēka* | wood |
| *nēki* | animal |
| *kēli* | dog |
| *vōna* | bird |
| *tēri* | fish |
| *dhōki* | eye |
| *nēma* | ear |
| *mōha* | mouth |
| *sēra* | tooth |
| *kēpa* | hand |
| *pōda* | foot |
| *dhēki* | heart |
| *sōri* | blood |

### 9.2 Verbs

| VELA | Meaning |
|------|---------|
| *es-ā* | to be (existential) |
| *ven-ī* | to come |
| *lo-ā* | to go |
| *dō-ī* | to give |
| *sē-ī* | to take |
| *thak-ī* | to see |
| *dhēv-ī* | to hear |
| *kēl-ī* | to eat |
| *nōk-ī* | to drink |
| *mēr-ī* | to sleep |
| *tēn-ī* | to speak |
| *dhēn-ī* | to know |
| *vēs-ī* | to want |
| *pēk-ī* | to be afraid |
| *sēn-ī* | to love |
| *thōk-ī* | to kill |
| *dēv-ī* | to die |
| *kēs-ī* | to burn |
| *pēt-ī* | to cut |
| *dhōl-ī* | to break |

### 9.3 Adjectives

| VELA | Meaning |
|------|---------|
| *nōva* | big |
| *pīka* | small |
| *dhēli* | good |
| *mōri* | bad |
| *kētha* | red |
| *vōna* | white |
| *tēki* | black |
| *sōra* | green |
| *pēna* | yellow |
| *dhēka* | hot |
| *mēla* | cold |
| *kēli* | long |
| *tōpa* | short |
| *vēra* | new |
| *nōma* | old |
| *sēvi* | fast |
| *dhōka* | slow |
| *pēki* | strong |
| *mēki* | weak |

---

## 10. Sources & Further Reading

- Swadesh, M. (1952). "Lexicostatistic Dating of Prehistoric Ethnic Contacts." *Proceedings of the American Philosophical Society* 96(4).
- Bowern, S. (2012). *Linguistic Fieldwork: A Practical Guide* (2nd ed.). Cambridge University Press.
- Goddard, C. (2011). *Semantic Analysis: A Practical Introduction* (2nd ed.). Oxford University Press.
- Cruse, D.A. (1986). *Lexical Semantics*. Cambridge University Press.
- Heijkant, M. (2010). *Conlanging: The Language Building Workshop*. Createspace.
- Peterson, D.J. (2015). *The Art of Language Invention*. Penguin.
- Okrand, M. (1992). *The Klingon Dictionary*. Pocket Books.
- The Conlangery Podcast and Conlangery Lexicon Challenge
- The Language Construction Kit by Mark Rosenfelder (https://www.zompist.com/kit.htm)
- Wikipedia: Semantic field, Lexicography, Zipf's law, Swadesh list

---

*Document prepared for the VELA Conlang Project*
*Author: Deep Research Subagent*
*Version: 1.0*
