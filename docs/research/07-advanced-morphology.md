# VELA Conlang Project: Advanced Morphology
## Research Document 7 — Polysynthesis, Alignment, Switch-Reference, and the Encoding of Perspective

---

## 1. Introduction: Morphology as Cognitive Architecture

Morphology is the system by which languages build words and encode grammatical relationships. While basic morphology (plurals, past tense) is familiar to English speakers, the world's languages exhibit extraordinary diversity in how much grammatical information can be packed into single words, how that information is encoded, and what it reveals about how different cultures conceptualize events, participants, and perspective.

VELA's morphological system will be one of its most defining features. This document surveys the full range of morphological possibilities and provides guidance for VELA's design.

---

## 2. Polysynthesis: Building Sentence-Words

### 2.1 What Is Polysynthesis?

Polysynthesis is a morphological type characterized by the ability to combine many morphemes into single, complex words — often producing "sentence-words" that would require an entire clause in a less synthetic language.

**Classic example from Inuktitut:**
- *tusaarqunngittuallangit-qaanga* 
- (hear-not-future-1sg.3sg.- REPORTATIVE-he said)
- "he said he would not hear it"

Or from Central Alaskan Yup'ik:
- *angyaghllakaghyugtuaghma*
- (boat-big-want.there.going.to.be-when-1sg.)
- "when I was going to get a big boat" (literally: "boat-big-wanted-being-when-I")

### 2.2 Defining Characteristics

Polysynthetic languages typically have:
1. **Incorporation:** Nouns can be incorporated into verbs
2. **Polypersonal agreement:** Verbs agree with multiple arguments (subject, object, indirect object)
3. **Extensive derivation:** Rich system of derivational morphemes creating new word classes
4. **Word-level prosody:** The entire word is a single phonological and prosodic unit

### 2.3 Famous Polysynthetic Languages

**Mohawk (Iroquoian):**
- *wanohkwawiya'stha'ke'*
- (table-CAUS-benefit-again-FUT-3PL)
- "they will benefit again from a table"

**Navajo (Athabaskan):**
- *yí-w-į́į́h*
- (3SUBJ-3OBJ-see-PAST)
- "he saw him"

**Chukchi (Chukotko-Kamchatkan):**
- *gygy-kym-gtər-qe-t-ylgjqen* 
- (NEG-NEG-can-do-PAST-1PL.EX-3PL.ABS)
- "we couldn't do it"

### 2.4 Incorporation

**Noun incorporation** is a key feature of polysynthetic languages — a noun root can be incorporated into a verb:

**Carib:**
- *nino-bana* = "I see a man"
- *no-bana* = "I man-see" = "I hunt" (man incorporated into the verb)

**Inuktitut:**
- *qimmiq-mik-nngit-tuq* = "it is not a dog" (qimmiq = dog, incorporated)
- But also: *qimmiiq-apiq-mmat-qqau-tuq* = "it bit the dog" (non-incorporated, with a different verb)

**VELA Recommendation:** VELA could have limited noun incorporation — specifically for common objects that form tight conceptual units with verbs:
- "fish" + "eat" → "to fish" (eat-fish)
- "water" + "drink" → "to drink" (drink-water) — but "water" is incorporated
- This creates efficient, natural compound verbs

---

## 3. Verb Serialization

### 3.1 What Is Verb Serialization?

Verb serialization is a syntactic phenomenon where two or more verbs appear in a single clause without overt marking of subordination or coordination. The construction functions as a single predicate describing a complex event.

**Types of Serial Verb Constructions (SVCs):**

1. **Coordinate SVCs:** Two independent events in sequence
   - Mandarin: *tā zǒu jìn chūfáng chīfàn* (he walk-enter kitchen eat-meal) = "He went into the kitchen and ate"

2. **Nuclear SVCs:** Shared argument structure; the verbs share arguments
   - Ewe: *e le wo do* (he PRF book read) = "He has read the book" — *le* marks perfective, *do* is the verb
   - Mandarin: *wǒ chī fàn* (I eat meal) = "I eat rice/a meal" — both verbs share the subject

3. **Light verb constructions:** One verb is semantically light, the other carries the main meaning
   - English: *take a walk*, *give a look*, *do the cooking*
   - Japanese: *tabemono wo suru* (food ACC do) = "to eat" (lit. "do food")
   - Chinese: *qǐ lù* (rise road) = "to set out" (lit. "rise road")

### 3.2 Serial Verb Languages

Verb serialization is particularly common in:
- **West Africa:** Ewe, Yoruba, Igbo (Niger-Congo)
- **Southeast Asia:** Mandarin, Thai, Vietnamese, Khmer (Austroasiatic)
- **Papua New Guinea:** Many Papuan languages
- **Oceania:** Many Austronesian languages

### 3.3 VELA Recommendation

VELA could include light verb constructions (a restricted form of serialization):
- A general "do/make" verb that combines with nouns to create event verbs
- This is attested even in European languages and adds expressive economy
- Example: VELA *fa-kos* (do-thing) = "to do/make something" → contextual interpretation

---

## 4. Switch-Reference Systems

### 4.1 What Is Switch-Reference?

Switch-reference (SR) is a grammatical system that uses markers on verbs to indicate whether the subject of one clause is the same as or different from the subject of an adjacent clause. This is a clause-level morphological system found in many languages, especially in Australia and the Americas.

**How it works:**
- **Same-subject (SS) marker:** The subjects of two adjacent clauses are co-referential
- **Different-subject (DS) marker:** The subjects are different

**Example from Amurdag (Australian language):**
- *bala=yang* (come=1SG.SUBJ) — "I come"
- *bala=yang-ga* (come=1SG.SUBJ-SS) — "I come and ___"
- *bala=yang-gin* (come=1SG.SUBJ-DS) — "I come and he/she/they ___"

### 4.2 Purposes of Switch-Reference

SR systems serve several discourse functions:
1. **Avoiding ambiguity:** In languages with flexible word order, SR markers clarify who is doing what
2. **Discourse coherence:** SS marking creates discourse cohesion; DS marking flags new discourse participants
3. **Narrative structure:** SS markers often indicate backgrounded, sequential events; DS markers indicate foregrounded events or changes

### 4.3 Switch-Reference in Practice

**Mandan (Siouan):**
- SS marker = *-e*
- DS marker = *-a*
- *wathpí-ka xé-ʔé-ki* (man.DEF see-SS-3PL) = "The men saw each other" (same subject within clause)
- *wathpí-ka xé-ʔá-ki* (man.DEF see-DS-3PL) = "The men saw them (other people)" (different subjects)

**Wambaya (Australian):**
- SS = *-ni*
- DS = *-ji*

### 4.4 VELA Recommendation

VELA could implement a simple switch-reference system in narrative/historical registers:
- Two clause-chaining suffixes:
  - **-ma** = SS (same subject in next clause)
  - **-ta** = DS (different subject in next clause)
- Example: *Mi veni-ma, lo kanti.* (I come-SS.SEQ, he sing.PST) = "I came and he sang" (I came; then he sang — SS linking, sequential events)
- Example: *Mi veni-ta, me kanta.* (I come-DS.SEQ, you.NOM sing.PST) = "I came and you sang" (different subjects)

This would add a distinctly narrative, literary flavor to VELA's morphology.

---

## 5. Alignment Systems

### 5.1 The Problem of Grammatical Relations

In a transitive clause, there are two core arguments: the subject (A) and the object (O). In an intransitive clause, there is one core argument (S). How these three are treated morphologically defines the language's **alignment**.

**Three Major Alignment Types:**

### 5.2 Nominative-Accusative Alignment

**Pattern:** The subject of an intransitive verb (S) is treated the same as the subject of a transitive verb (A). Both receive **nominative** case/marking. The object (O) receives **accusative** marking.

**Examples:**
- **English:** "She (S) slept" / "She (A) saw him (O)" — "she" nominative, "him" accusative (though case marking is lost)
- **German:** *sie* (she/nominative) vs. *sie* (they/nominative) vs. *sie* (them/accusative — same form but only for 3PL)
- **Latin:** *puella dormit* (girl.nom sleeps) / *puella puerum videt* (girl.nom boy.acc sees)
- **Turkish:** Case-marked nominative (ø) for S and A, accusative (-i) for O

**Universal distribution:** ~70% of languages

### 5.3 Ergative-Absolutive Alignment

**Pattern:** The subject of an intransitive verb (S) is treated the same as the object of a transitive verb (O). Both receive **absolutive** case/marking. The subject of a transitive verb (A) receives **ergative** case/marking.

**Why "ergative"?** The ergative case often derives historically from a word meaning "doing" or "agent," while the absolutive often derives from a word meaning "thing" or "patient."

**Examples:**
- **Basque:** *Emazumea etorri da* (woman.abs arrived aux) / *Gizona ikusi du* (man.erg see aux) — the woman is absolutive in both (intransitive subject and transitive object); the man is ergative (transitive subject)
- **Georgian:** Complex split-ergative system
- **Dyirbal (Australian):** Famous for its "Mother-in-law language" category
- **Inuktitut:** Ergative-absolutive

**Logical intuition:** In ergative systems, S and O are both "undergoers" (something happens to them), while A is the "actor." This makes semantic sense — S and O are both affected or involved without initiating the event.

### 5.4 Active-Stative (Split-S) Alignment

**Pattern:** The single argument of an intransitive verb (S) is sometimes treated like A (agent-like = **active**) and sometimes like O (patient-like = **stative**), depending on its semantic properties.

**The split is typically based on:**
- Volitionality (did the subject choose to do this?)
- Control (does the subject have control?)
- Affectedness (is the subject affected by the event?)
- Animacy/humanity

**Examples:**
- **Spanish (in the past tense):**
  - *Yo corrí* (I ran) — active/transitive past of "to run" (volitional)
  - *Yo me caí* (I fell.REFL) — stative/secausative (not volitional)
  
- **Georgian:**
  - Transitive: *gogh威* (I wrote) — A is marked ergative
  - Intransitive verbs split:
    - Active (volitional): *gipova* (I slept) — A-type marking
    - Stative (involuntary): *gizdis* (I got sick) — S/O-type marking

- **Russian (partial):**
  - Some intransitive verbs take *byt'* (to be) as auxiliary (perfective past), some take *byt'* as "was/were" with the participle
  - The split is lexically determined: *rabotat'* (to work, active) vs. *boleet'* (to hurt, stative)

**VELA Recommendation:** VELA could use **split-S alignment** with a systematic split:
- **Agentive intransitive verbs** (run, walk, speak, work): marked like transitive A (active case)
- **Stative intransitive verbs** (be sick, fall, die, sleep): marked like O (absolutive case)
- This adds great semantic richness with relatively low morphological cost
- The split could be conditioned by volitionality: [+volitional] verbs → active; [-volitional] → stative

---

## 6. Tripartite Alignment

### 6.1 What Is Tripartite Alignment?

In tripartite alignment, all three arguments — S, A, and O — receive **distinct case marking**. There is no grouping of S with either A or O.

**Pattern:** S = X | A = Y | O = Z

**Examples:**
- **Hindi (partially):** Some pronouns maintain tripartite marking:
  - S: *vo āyā* (he came) 
  - A: *us-ne* (he-ERG)
  - O: *us-ko* (he-ACC)
  
- **Nez Perce (Sahaptin):**
  - S: *naqípxam* (I stood)
  - A: *naqípxa-ni* (I-Kicked him) — A marked with subject suffix
  - O: *naqípxa-ci*ʔ (he-Kicked me) — O cross-referenced differently

**Rarely applied consistently** across all nouns — usually restricted to pronouns or certain noun classes.

---

## 7. How Languages Encode Perspective and Empathy

### 7.1 Subject Marking and Empathy

Languages differ in which participant is encoded as the grammatical subject:

**Transitivity and affectedness:**
- In transitive events, the subject (A) is the agent — the one doing something to someone else
- The more **affected** the object (O) is, the more transitive the event feels
- Languages often have special morphology for high-transitivity events (perfective aspect, agentive case)

**The Empathy Hierarchy:**
Talmy's (1988) principle: speakers tend to identify with participants higher on the animacy/humanity hierarchy:
- 1st person > 2nd person > 3rd person > human > animate > inanimate

This affects:
- **Word order:** The more empathetic participant tends to come first
- **Voice choice:** Active vs. passive (English passive promotes the object to subject position)
- **Person marking:** 1st person singular often has unique markers

### 7.2 The Passive and Its Alternatives

English passive: *"The cake was eaten (by John)"* — the object becomes the subject.

**Other languages avoid the passive or use it differently:**
- **Japanese:** Uses the *-rare* causative/passive suffix; also uses *-te* constructions
- **Russian:** Uses verbal adverbs and reflexive forms
- **Polynesian languages:** Often use **Actor-Emphatic constructions** instead of passives

**Inverse systems** ( Algonquian languages, Athabaskan languages):
- The verb marks whether the subject outranks the object on the empathy hierarchy
- If A > O (1st > 2nd, human > object): DIRECT
- If O > A (object > subject): INVERSE marker
- Example: *Nīmīc-iw* = "He sees me" (I < him, direct)
- *Nīmīc-ik* = "I see him" (I > him, inverse)

**VELA Recommendation:** VELA could include an **inverse alignment** system in its verb morphology — a suffix marking when the object outranks the subject on the animacy hierarchy. This would be:
- **Direct (DIR):** A > O (agent outranks patient in animacy/person)
- **Inverse (INV):** O > A (patient outranks agent)
- Example: *mi-ven-i* = "I see him" (1>3 direct)
- *mi-ven-ak* = "him sees me" (3>1 inverse)

### 7.3 The Symmetry of Person Marking

Many languages mark person/number of both subject and object on the verb:
- **Zapotec:** Full person/number marking of both A and O
- **Algonquian:** Both A and O cross-referenced, with the inverse marking O>A relations

This is called **polypersonal agreement** and is found in:
- Basque, Georgian, and many polysynthetic languages (subject AND object agreement)
- The Romance verb "I give it to him" involves agreement with subject + indirect object (IO): *lo doy* — "it I-give"

---

## 8. Case Systems: Types and Functions

### 8.1 Major Case Types

**Core cases** (typically 2-3):
- **Nominative:** Subject of transitive/intransitive verbs (S, A)
- **Accusative:** Direct object of transitive verb (O)
- **Ergative:** Subject of transitive verb (A) in ergative languages
- **Absolutive:** Subject of intransitive verb + object of transitive verb (S, O) in ergative languages

**Secondary cases** (language-specific, 5-20+):
- **Genitive:** Possessor (noun + noun)
- **Dative:** Indirect object / beneficiary
- **Locative:** Location (in, on, at)
- **Instrumental:** Tool, means, accompaniment
- **Ablative:** Source, separation, cause
- **Allative:** Direction toward
- **Vocative:** Direct address
- **Comitative:** Accompaniment ("with")

### 8.2 Case Systems Across Languages

| Language | Cases | Notable |
|----------|-------|---------|
| Finnish | 15 | Rich system, no gender |
| Hungarian | 18-20 | Complex, many spatial cases |
| Turkish | 6 (nouns) + suffixes | Agglutinative, regular |
| Georgian | 7 | Ergative, complex verb agreement |
| Sanskrit | 8 | Classic Indo-European system |
| Latin | 6 | Nominative, Genitive, Dative, Accusative, Ablative, Vocative |
| German | 4 | Nominative, Genitive, Dative, Accusative |
| Russian | 6 | Prepositional as 6th case |
| Basque | Absolute + Ergative + Dative | Minimal cases, rich morphology |

### 8.3 How Cases Derive (Grammaticalization)

Cases almost always derive from older **postpositions** (after-position words):
- Latin *-um* (accusative) ← *-om* (direction postposition)
- Sanskrit *-asya* (genitive) ← *asya* (demonstrative pronoun)
- Turkish cases ← Ural-Altaic postpositional system

**VELA Recommendation:** Design VELA's case system by starting with a few core spatial postpositions and allowing them to grammaticalize into case suffixes:
1. Design 6-8 postpositions for spatial relationships
2. Allow them to fuse with nouns over time → case suffixes
3. Some postpositions remain lexical (as adverbs or conjunction-equivalents)

---

## 9. VELA Morphological Design Recommendations

### 9.1 Overall Morphological Type

**Recommended type: Fusional-Agglutinative hybrid**

- Moderate fusional morphology (single morpheme encodes multiple features)
- Agglutinative derivational morphology (clean morpheme boundaries in derived words)
- Moderate synthesis (2-4 morphemes per word on average)

This is similar to: Basque, Georgian, Quechua — languages that are naturalistic without being Ithkuil-level complex.

### 9.2 Recommended Morphological Features

**Noun Morphology:**
- **4 noun cases:** Nominative, Accusative, Genitive, Locative + instrumental/dative as suffixes
- **2 noun classes:** Sapient/human vs. non-human (marked on nouns and adjectives)
- **Number:** Singular, Plural, with a **paucal** (few) form for small numbers

**Verb Morphology:**
- **Polypersonal agreement:** Subject + object (direct) agreement on the verb
- **Inverse system:** For when O outranks A on animacy/person hierarchy
- **Aspect:** Perfective vs. Imperfective (two-way aspect)
- **Tense:** Present, Past (future expressed periphrastically)
- **Evidentiality:** Visual vs. Non-visual vs. Reported (three-way)
- **Switch-reference:** SS vs. DS clause chaining in narrative register

**Derivation:**
- **Causative suffix:** -es- (make/cause to do)
- **Applicative suffix:** -il- (do with/for)
- **Incorporation:** Limited noun incorporation for common object verbs
- **Nominalization:** Verbal nouns with -a or -o suffixes

### 9.3 Sample Paradigm

**Noun: *sāra* (river)**

| Case | Form | Usage |
|------|------|-------|
| Nominative | *sāra* | Subject |
| Accusative | *sāra-m* | Direct object |
| Genitive | *sāra-ko* | Possessor |
| Locative | *sāra-vel* | In/at river |
| Instrumental | *sāra-gen* | With/by river |

**Verb: *tʃivi* (to see)**

| Category | Form |
|----------|------|
| 1SG subject, 2SG object | *a-tʃiv-i* (I-see-DIR) |
| 1SG subject, 3SG object | *a-tʃiv-i* |
| 3SG subject, 1SG object | *o-tʃiv-ak* (him-see-INV) |
| 3SG subject, 3SG object | *o-tʃiv-i* |
| Perfective | *o-tʃiv-ī* |
| Imperfective | *o-tʃiv-a* |

---

## 10. Sources & Further Reading

- Baker, M.C. (1988). *Incorporation: A Theory of Grammatical Role Changing*. University of Chicago Press.
- Mithun, M. (1999). "Verb Incorporation and Language Contact." *International Journal of Comparative Sociology*.
- Aikhenvald, A.Y. (2012). *The Language of Assessment*. Mouton.
- Dixon, R.M.W. (1979). *Ergativity*. Cambridge University Press.
- Dixon, R.M.W. (1994). *Ergativity*. Cambridge University Press.
- Silk, D. (ed.) (2018). *Ergativity, Valency and Voice*. Mouton.
- Mithun, M. (1990). "On the Relativity of Syntactic Systems." *Language* 66(3).
- Comrie, B. (1989). *Language Universals and Linguistic Typology* (2nd ed.). University of Chicago Press.
- Croft, W. (2003). *Typology and Universals* (2nd ed.). Cambridge University Press.
- WALS Ch. 48-58 (Morphology) and Ch. 98-115 (Grammatical categories)

---

*Document prepared for the VELA Conlang Project*
*Author: Deep Research Subagent*
*Version: 1.0*
