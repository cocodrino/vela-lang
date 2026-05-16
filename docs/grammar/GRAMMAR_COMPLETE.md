# VELA Grammar — Complete Reference

> **Status:** COMPLETE ✅ — Phase 3 of the Roadmap  
> **Source:** `INITIAL_RESEARCH.md` + design decisions made 2025-04-13  
> **Language:** English (this document is written in English for maximum accessibility)

---

## Table of Contents

1. [Word Order — SVO](#1-word-order)
2. [Articles](#2-articles)
3. [Pronouns](#3-pronouns)
4. [Nouns and the Minimal Case System](#4-nouns-and-cases)
5. [Adjectives](#5-adjectives)
6. [Verbs — Core System](#6-verbs-core)
7. [Verbs — Aspect and Modality](#7-verbs-aspect-modality)
8. [Negation](#8-negation)
9. [Questions](#9-questions)
10. [Prepositions](#10-prepositions)
11. [Conjunctions](#11-conjunctions)
12. [Numbers and Time](#12-numbers-and-time)
13. [Adverbs](#13-adverbs)
14. [Word Formation — Affixes](#14-word-formation)
15. [Word Formation — Compounds](#15-compounds)
16. [Sentence Types — Full Paradigms](#16-sentence-types)

---

## 1. Word Order — SVO

**VELA is a strict SVO language.**

The subject always comes before the verb. The object always comes after the verb.

```
S     V      O
Mi   si      la film.         → I see the film.
Yu   lik     la sonj.         → You like the song.
Wi   liv     la siti.         → We live in the city.
Li   go      a la ofis.       → She goes to the office.
De   her     la vois.         → They hear the voice.
```

### 1.1 Why SVO?

- SVO is the most common word order in the world (about 45% of languages)
- It is intuitive for English, Spanish, Mandarin, Hindi, and many others
- SVO allows the case system to remain minimal — word order does the work of disambiguation
- VELA's goal: maximum clarity with minimum complexity. SVO achieves both.

### 1.2 Can elements be moved?

In formal or poetic VELA, elements can be fronted or topicalized for emphasis:

```
La film,  mi si.    → "As for the film, I see it."
Yu, la man si yu.   → "You — the man sees you."
```

**Note:** This is poetic/literary usage. In normal speech, always keep SVO order.

### 1.3 Object is always after the verb

```
❌ INCORRECT:  Mi la film si.     (object before verb)
✅ CORRECT:     Mi si la film.     (SVO)
```

---

## 2. Articles

VELA has **two articles** — a definite and an indefinite.

| Article | AFI | Use | Example |
|---------|-----|-----|---------|
| **la** | /la/ | Definite (the) | la man — the man |
| **un** | /un/ | Indefinite (a/an) | un man — a man |

### 2.1 Definite Article — **la**

Used for specific, known entities:

```
La sonj es nais.      → The song is nice.
Mi si la man.         → I see the man.
Yu hav la buk.        → You have the book.
```

### 2.2 Indefinite Article — **un**

Used for non-specific, first-mention entities:

```
Un man kom.            → A man comes.
Mi si un fil.         → I see a film.
Yu liv in un siti.    → You live in a city.
```

### 2.3 No article

Some contexts do not use an article:

```
Mi liv in siti.        → I live in (the) city.  (habitual)
Yu go hom.             → You go home.          (home is a fixed idea)
```

### 2.4 Articles and Cases

Articles do not change form for case. The noun after the article takes the case:

```
la man-se    → the man's     (la + man + se)
la siti-to  → in the city  (la + siti + te)
```

---

## 3. Pronouns

### 3.1 Subject Pronouns

| Pronoun | Person | AFI | English equivalent |
|---------|--------|-----|------------------|
| **mi** | 1st singular | /mi/ | I |
| **yu** | 2nd singular | /ju/ | you (singular) |
| **li** | 3rd singular | /li/ | he/she/it |
| **wi** | 1st plural | /wi/ | we |
| **de** | 2nd/3rd plural | /de/ | they / you (plural) |

### 3.2 Possessive Pronouns (short form)

These come before the noun, like English "my," "your":

| Possessive | AFI | English equivalent | From |
|-----------|-----|------------------|------|
| **mif** | /mif/ | my/mine | mi + f |
| **yuf** | /juf/ | your/yours | yu + f |
| **liz** | /liz/ | his/her/its | li + z |
| **wef** | /wef/ | our/ours | wi + f |
| **def** | /def/ | their/theirs | de + f |

```
Mif fren.          → My friend.
Yu si yuf buk.     → You see your book.
Li lik liz job.    → She likes her job.
```

### 3.3 Genitive Pronouns (full form)

These are the **-se** suffix form, used for genitive case on pronouns:

| Genitive | AFI | English equivalent | From |
|----------|-----|------------------|------|
| **mi-se** | /mi.se/ | my / of mine | mi + se |
| **yu-se** | /ju.se/ | your / of yours | yu + se |
| **li-se** | /li.se/ | his/her/its | li + se |
| **wi-se** | /wi.se/ | our / of ours | wi + se |
| **de-se** | /de.se/ | their / of theirs | de + se |

**Rule:** Use possessive (short form) for most sentences. Use genitive (-se) when emphasizing or when the pronoun is a noun phrase head:

```
Mi si mif fren.        → I see my friend.              (short: most common)
Mi si la fren mi-se.   → I see the friend of mine.   (genitive: emphasis)
Yu her li-se vois.     → You hear her voice.           (short)
Yu si la man-se buk.   → You see the man's book.    (genitive: noun + -se)
```

### 3.4 Locative Pronouns (full form)

These are the **-te** suffix form, used for locative case on pronouns:

| Locative | AFI | English equivalent |
|----------|-----|------------------|
| **mi-to** | /mi.te/ | at/to me |
| **yu-to** | /ju.te/ | at/to you |
| **li-to** | /li.te/ | at/to him/her/it |
| **wi-to** | /wi.te/ | at/to us |
| **de-to** | /de.te/ | at/to them |

```
Mi go mi-to.      → I go to my place.  (to where I am)
Yu liv yu-to.    → You live at your place.
```

### 3.5 Demonstrative Pronouns

| Pronoun | AFI | English equivalent | Notes |
|---------|-----|------------------|-------|
| **dis** | /dis/ | this | close to speaker |
| **dat** | /dat/ | that | far from speaker |
| **dese** | /de.se/ | these | plural of dis |
| **dase** | /da.se/ | those | plural of dat |

```
Dis man es big.    → This man is big.
Dat hous es nais.  → That house is nice.
```

### 3.6 Reflexive Pronoun

| Pronoun | AFI | Use |
|---------|-----|-----|
| **self** | /self/ | reflexive |

```
Mi her self.      → I hear myself.
Li si self.       → She sees herself.
```

---

## 4. Nouns and Cases

### 4.1 Noun Categories

All nouns end in a vowel in VELA. This is a consequence of the (C)V syllable rule.

| Category | Suffix | Example | Notes |
|----------|--------|---------|-------|
| Common nouns | — | man, siti, famili | No special suffix |
| Proper nouns | — | Karlos, Maria | Capitalized |

### 4.2 Plural

The plural suffix is **-s**:

```
man     → man-s         (men/people)
siti    → siti-s        (cities)
famili  → famili-s      (families)
```

### 4.3 The Minimal Case System

VELA has **two cases** — only marking what word order cannot express.

| Case | When to use | Suffix | Example |
|------|------------|--------|---------|
| **Nominative** | Subject of sentence | none | *Mi* si la film. |
| **Accusative** | Direct object | none | Yu si *mi*. |
| **Genitive** | Possessor of another noun | **-se** | la man-**se** buk |
| **Locative** | Location or time | **-te** | Mi liv la siti-**te**. |

**The key principle:** Word order (SVO) handles nominative and accusative. Only add a suffix when word order is insufficient.

### 4.4 Nominative — No Suffix

The subject of any sentence is in nominative. No suffix required.

```
Mi si la film.         → I see the film.        (mi = subject NOM)
Yu si la man.         → You see the man.        (yu = subject NOM)
La man si mi.         → The man sees me.        (man = subject NOM; mi = object ACC)
```

### 4.5 Accusative — No Suffix

The direct object is placed after the verb. No suffix required. SVO word order does all the work.

```
Yu si la man.         → You see the man.        (man = direct object ACC)
Mi si la siti.       → I see the city.         (siti = direct object ACC)
De her la sonj.      → They hear the song.     (sonj = direct object ACC)
```

### 4.6 Genitive — **-se**

Used when a noun possesses another noun. The -se noun comes before the possessed noun:

```
la man-se dog         → the man's dog
la famili-se hous     → the family's house
la Siti-to laibri     → the city's library
```

**Position:** The possessor (with -se) comes BEFORE the possessed noun. Order: **possessor-GEN + possessed**.

### 4.7 Locative — **-te**

Used for location, time, or state:

```
Mi liv la siti-to.     → I live in the city.      (habitual location)
Li es la ofis-to.    → She is at the office.   (location)
Wi wok la klas-to.   → We work in the class.  (location)
De kom la las dei-to. → They come on the last day. (time)
```

### 4.8 Full Noun Paradigm: man (person)

| Case | Singular | Plural |
|------|----------|--------|
| **Nominative** | man | man-s |
| **Accusative** | man | man-s |
| **Genitive** | man-**se** | man-s-**se** |
| **Locative** | man-**te** | man-s-**te** |

### 4.9 Case + Other Morphemes

When case combines with other suffixes, the order is always: **root → case → number**:

```
Case + Plural:    man-se-s        (the men's + plural = men's of multiple men)
Locative + Pl:   siti-te-s      (in the cities)
Genitive + Pl:   famili-se-s    (of the families)
```

### 4.10 Case and Prepositions

When a preposition already marks location/time, the -te suffix is **optional**:

```
Mi liv en la siti.      → I live in the city.          (en = in)
Mi liv la siti-to.     → I live in the city.          (-te alone)

Wi wok at la ofis.      → We work at the office.      (at = location)
Wi wok la ofis-to.     → We work at the office.       (-te alone)

Li kom from la lern-hous.    → She comes from the school.   (from = origin)
Li kom la lern-hous-to.     → She comes from the school.    (-te alone)
```

**Rule:** When a preposition marks the semantic role clearly, -te can be dropped. Without a preposition, -te is required.

---

## 5. Adjectives

### 5.1 Adjective Form

Adjectives are used as bare roots, placed before the noun:

| Base | Adjective | English |
|------|-----------|---------|
| big | big | big |
| strong | strong | strong |
| happi | hapi | happy |
| nais | nais | nice |
| simpli | simpli | simple |

### 5.2 Adjective Position

In VELA, the adjective comes **before the noun** it modifies:

```
Un big man.       → A big man.
La nais famili.  → The nice family.
La simpli idea.   → The simple idea.
```

### 5.3 Adjectives Do Not Take Case

Adjectives do not agree with the noun's case. They simply precede the noun:

```
NOM:  La big man si la film.         → The big man sees the film.
ACC:  Mi si la big man-a.           → I see the big man.      (man takes -a, not big)
GEN:  La big man-se hous.          → The big man's house.    (man takes -se, not big)
LOC:  Mi liv la big siti-to.       → I live in the big city. (siti takes -te)
```

### 5.4 Comparison

| Form | Structure | Example |
|------|-----------|---------|
| Positive | base | big |
| Comparative | **mor** + base | **mor** big |
| Superlative | **mos** + base | **mos** big |

```
La man es big.           → The man is big.
La man es mor big.     → The man is bigger.
Dat man es mos big.    → That man is the biggest.
```

### 5.5 Irregular Comparisons

Some comparisons are more common as phrases:

| English | VELA | Structure |
|---------|------|-----------|
| better | mor gud | more good |
| best | mos gud | most good |
| worse | mor bad | more bad |
| worst | mos bad | most bad |

---

## 6. Verbs — Core

### 6.1 The Three Tenses — Zero Irregular Verbs

This is VELA's most important grammatical feature. **Every verb follows the same three rules:**

| Tense | Suffix | Structure | Example | English |
|-------|--------|-----------|---------|---------|
| **Present** | **-a** | root + -a | liv-**a** | I live |
| **Past** | **-ed** | root + -ed | liv-**ed** | I lived |
| **Future** | **-wil** | root + -wil | liv-**wil** | I will live |

### 6.2 Full Paradigm of a Regular Verb: liv (to live)

| Person | Present | Past | Future |
|--------|---------|------|--------|
| mi | liv-**a** | liv-**ed** | liv-**wil** |
| yu | liv-**a** | liv-**ed** | liv-**wil** |
| li | liv-**a** | liv-**ed** | liv-**wil** |
| wi | liv-**a** | liv-**ed** | liv-**wil** |
| de | liv-**a** | liv-**ed** | liv-**wil** |

**There are no exceptions. No irregular verbs. No spelling changes.**

```
liv     liv-a     liv-ed     liv-wil
to live  I live   I lived    I will live

si      si-a      si-ed      si-wil
to see   I see     I saw      I will see

tok     tok-a     tok-ed     tok-wil
to speak I speak  I spoke    I will speak
```

### 6.3 The Verb "To Be" — bi

The verb **bi** (to be) is regular — unlike in English:

| Person | Present | Past | Future |
|--------|---------|------|--------|
| mi | bi-**a** | bi-**ed** | bi-**wil** |
| yu | bi-**a** | bi-**ed** | bi-**wil** |
| li | bi-**a** | bi-**ed** | bi-**wil** |

```
Mi es hapi.          → I am happy.           (present)
Mi es-ed hapi.       → I was happy.          (past — NOT "was")
Mi wil es hapi.      → I will be happy.      (future — NOT "will be" as separate)

NOT: Mi was hapi.     ❌ English irregular form
NOT: Mi es-wil hapi.  ❌ English hybrid form
YES: Mi es-ed hapi.   ✅ VELA regular form
```

### 6.4 Core Verb List

| VELA | English | Present | Past | Future |
|------|---------|---------|------|--------|
| bi | to be | bi-a | bi-ed | bi-wil |
| si | to see | si-a | si-ed | si-wil |
| go | to go | go-a | go-ed | go-wil |
| kom | to come | kom-a | kom-ed | kom-wil |
| tok | to speak | tok-a | tok-ed | tok-wil |
| liv | to live | liv-a | liv-ed | liv-wil |
| wok | to work | wok-a | wok-ed | wok-wil |
| her | to hear | her-a | her-ed | her-wil |
| fel | to feel | fel-a | fel-ed | fel-wil |
| luk | to look | luk-a | luk-ed | luk-wil |
| lik | to like | lik-a | lik-ed | lik-wil |
| lern | to learn | lern-a | lern-ed | lern-wil |
| hav | to have | hav-a | hav-ed | hav-wil |
| don | to do | don-a | don-ed | don-wil |
| nof | to know | nof-a | nof-ed | nof-wil |

---

## 7. Verbs — Aspect and Modality

### 7.1 Aspect — Progressive (-an)

The suffix **-an** marks ongoing action. It combines with tense:

| Aspect | Structure | Example |
|--------|-----------|---------|
| Present Progressive | root-**an** | liv-**an** — am living |
| Past Progressive | root-**ed** + **an** | liv-ed-**an** — was living |

```
Mi liv-an.        → I am living.           (present + progressive)
Mi liv-ed-an.     → I was living.          (past + progressive)
Li wok-an.        → She is working.         (present + progressive)
```

### 7.2 Modality — Three Core Modal Verbs

| Modal | AFI | English | Example |
|-------|-----|---------|---------|
| **kan** | /kan/ | can / to be able to | Yu kan si. → You can see. |
| **mas** | /mas/ | must / to have to | Wi mas wok. → We must work. |
| **wan** | /wan/ | to want to | Mi wan kom. → I want to come. |

**Modal + main verb:** Modal verb takes tense. Main verb is bare root (no suffix):

```
Mi kan si la film.     → I can see the film.       (kan takes -a)
Mi kan-ed si la film.  → I could see the film.    (kan takes -ed)
Li wan kom.            → She wants to come.        (wan takes -a)
De mas wok.            → They must work.            (mas takes -a)
```

---

## 8. Negation

### 8.1 Simple Negation — **no**

The word **no** comes before the verb:

```
Mi no wok.            → I don't work.
Yu no si la film.     → You don't see the film.
Li no liv la siti-to. → She doesn't live in the city.
```

### 8.2 Negation with Modal Verbs

**no** comes before the modal verb:

```
Mi no kan kom.        → I cannot come.
Yu no wan wok.        → You don't want to work.
De no mas si.         → They must not see.
```

### 8.3 Strong Negation — **nevr**

For absolute negation ("never," "not at all"):

```
Li no kom.            → She didn't come.       (past, no action)
Li nevr kom.          → She never comes.       (absolute: not ever)
Mi no fel nevr.      → I never feel this.     (strong: absolutely never)
```

### 8.4 Negation of "bi" (to be)

```
Mi no es hapi.       → I am not happy.
Li no es-ed hapi.    → She was not happy.
Wi no wil es big.    → We will not be big.
```

---

## 9. Questions

### 9.1 Yes/No Questions — **q**

Form a yes/no question by adding **q** at the end of the sentence:

```
Yu si la film.       → You see the film.     (statement)
Yu si la film q?    → Do you see the film?  (question)

Li kom-ed.          → She came.              (statement)
Li kom-ed q?        → Did she come?          (question)

Wi wok.             → We work.              (statement)
Wi wok q?           → Do we work?           (question)
```

### 9.2 Alternative Questions

Use **or** for alternative questions:

```
Yu wan kom or no?      → Do you want to come or not?
Li es-ed hapi or sad? → Was she happy or sad?
```

### 9.3 Wh-Questions

| Word | AFI | English | Used for |
|------|-----|---------|---------|
| **hu** | /hu/ | who | People |
| **wat** | /wat/ | what | Things |
| **wen** | /wen/ | when | Time |
| **wer** | /wer/ | where | Place |
| **hai** | /hai/ | how | Manner |
| **wai** | /wai/ | why | Reason |
| **hou** | /hou/ | how | Degree/extent |
| **wot** | /wot/ | which | Selection |

```
Hu yu si?              → Who do you see?
Wat yu lik?            → What do you like?
Wen de kom?           → When do they come?
Wer wi wok?           → Where do we work?
Hai yu fel?           → How do you feel?
Wai yu wok?           → Why do you work?
Hou big es la hous?  → How big is the house?
Wot kolor es la kar? → Which color is the car?
```

### 9.4 Answers

| Answer | VELA | English |
|--------|------|---------|
| Affirmative | **ye** | yes |
| Negative | **no** | no |
| I don't know | **mi nof no** | I don't know |

---

## 10. Prepositions

### 10.1 Core Prepositions

| Preposition | AFI | English | Example |
|-------------|-----|---------|---------|
| **a** | /a/ | to / at | Mi go a la siti. → I go to the city. |
| **in** | /in/ | in | Li liv in la hous. → She lives in the house. |
| **on** | /on/ | on | La buk es on la tebul. → The book is on the table. |
| **from** | /from/ | from | Wi kom from la siti. → We come from the city. |
| **for** | /for/ | for | Dis es for yu. → This is for you. |
| **wit** | /wit/ | with | Mi wok wit yu. → I work with you. |
| **at** | /at/ | at | Wi liv at la sentr. → We live at the center. |
| **of** | /of/ | of | La sentr of la siti. → The center of the city. |

### 10.2 Prepositions and the Case System

When a noun after a preposition is also marked with -te or -se, the noun's role is doubly marked (preposition + suffix):

```
Mi liv in la siti-to.      → I live in the city.    (in + LOC)
Yu wok at la ofis-to.      → You work at the office. (at + LOC)
Li kom from la lern-hous-se.    → She comes from school.  (from + GEN)
```

---

## 11. Conjunctions

### 11.1 Coordinating Conjunctions

| Conjunction | AFI | English | Example |
|-------------|-----|---------|---------|
| **and** | /and/ | and | Mi si la man and la wuman. → I see the man and the woman. |
| **or** | /or/ | or | Yu wan kom or no? → Do you want to come or not? |
| **bot** | /bot/ | but | Mi wok, bot mi es hapi. → I work, but I am happy. |

### 11.2 Subordinating Conjunctions

| Conjunction | AFI | English | Example |
|-------------|-----|---------|---------|
| **bikos** | /bikos/ | because | Mi wok bikos mi wan moni. → I work because I want money. |
| **if** | /if/ | if | If yu kom, mi es hapi. → If you come, I am happy. |
| **wen** | /wen/ | when | Wen yu kom, mi si yu. → When you come, I see you. |
| **den** | /den/ | then | If yu no kom, den mi go. → If you don't come, then I go. |
| **so** | /so/ | so / therefore | Mi es hapi, so mi tok. → I am happy, so I speak. |

### 11.3 Conditional

The conditional is formed with **if + clause + den + consequence**:

```
If yu kom,     den  mi es hapi.     → If you come, then I am happy.
If yu no kom,  den  mi go.          → If you don't come, then I go.
If li wok-ed,  den  li her-ed.      → If she had worked, then she would have heard.
```

---

## 12. Numbers and Time

### 12.1 Cardinal Numbers

| Number | VELA | AFI |
|--------|------|-----|
| 0 | zero | /zero/ |
| 1 | wan | /wan/ |
| 2 | tu | /tu/ |
| 3 | tri | /tri/ |
| 4 | for | /for/ |
| 5 | faiv | /faiv/ |
| 6 | siks | /siks/ |
| 7 | sevn | /sevn/ |
| 8 | eit | /eit/ |
| 9 | nain | /nain/ |

### 12.2 Tens and Hundreds

| Number | VELA | AFI |
|--------|------|-----|
| 10 | ten | /ten/ |
| 11 | ten-wan | /ten.wan/ |
| 12 | ten-tu | /ten.tu/ |
| 13 | ten-tri | /ten.tri/ |
| 14 | ten-for | /ten.for/ |
| 15 | ten-faiv | /ten.faiv/ |
| 16 | ten-siks | /ten.siks/ |
| 17 | ten-sevn | /ten.sevn/ |
| 18 | ten-eit | /ten.eit/ |
| 19 | ten-nain | /ten.nain/ |
| 20 | tu-ten | /tu.ten/ |
| 30 | zerti | /zerti/ |
| 40 | kwatro-ten | /kwa.tro.ten/ |
| 50 | faiv-ten | /faiv.ten/ |
| 60 | siks-ten | /siks.ten/ |
| 70 | sevn-ten | /sevn.ten/ |
| 80 | eit-ten | /eit.ten/ |
| 90 | nain-ten | /nain.ten/ |
| 100 | kent | /kent/ |
| 101 | kent-wan | /kent.wan/ |
| 1,000 | zausand | /zausand/ |
| 1,000,000 | milyun | /milyun/ |

**Rule:** Use hyphens between compound numbers.

### 12.3 Ordinal Numbers

Ordinal numbers add **-t** to the cardinal:

| Cardinal | Ordinal | VELA | English |
|---------|---------|------|---------|
| wan | wan-**t** | first |
| tu | tu-**t** | second |
| tri | tri-**t** | third |
| for | for-**t** | fourth |

### 12.4 Days of the Week

| Day | VELA | English |
|-----|------|---------|
| Monday | **Mondei** | Monday |
| Tuesday | **Tiuzdei** | Tuesday |
| Wednesday | **Wenzdei** | Wednesday |
| Thursday | **Terzdei** | Thursday |
| Friday | **Fraidei** | Friday |
| Saturday | **Satrdei** | Saturday |
| Sunday | **Sandei** | Sunday |

### 12.5 Months

| Month | VELA | English |
|-------|------|---------|
| January | **Januari** | January |
| February | **Februari** | February |
| March | **Marti** | March |
| April | **Aprim** | April |
| May | **Maji** | May |
| June | **Juni** | June |
| July | **Julai** | July |
| August | **Agost** | August |
| September | **Septembr** | September |
| October | **Octobr** | October |
| November | **Novembr** | November |
| December | **Decembr** | December |

### 12.6 Time Expressions

| Expression | VELA | English |
|-----------|------|---------|
| now | **nau** | now |
| then | **den** | then |
| today | **nau-dei** | today |
| tomorrow | **tomoro** | tomorrow |
| yesterday | **yestdei** | yesterday |
| before | **bifor** | before |
| after | **aft** | after |
| always | **oldei** | always |
| never | **nevr** | never |
| soon | **sun** | soon |
| late | **let** | late |
| early | **erli** | early |

---

## 13. Adverbs

### 13.1 Adverb Formation

Adverbs are formed with the suffix **-um** added to the adjective:

| Adjective | Adverb | English |
|-----------|--------|---------|
| happi | happi-**um** | happily |
| nais | nais-**um** | nicely |
| simpli | simpli-**um** | simply |
| strong | strong-**um** | strongly |

### 13.2 Common Adverbs

| Adverb | AFI | English |
|--------|-----|---------|
| **oldei** | /oldei/ | always |
| **nevr** | /nevr/ | never |
| **ofn** | /ofn/ | often |
| **somtaim** | /somtaim/ | sometimes |
| **rarli** | /rar.li/ | rarely |
| **nes** | /nes/ | nearly |
| **bai** | /bai/ | by (manner) |
| **wail** | /wail/ | while / during |

---

## 14. Word Formation — Affixes

### 14.1 Productive Prefixes

| Prefix | Meaning | Example | Result |
|-------|---------|---------|--------|
| **un-** | negation | un-gud | un-good = bad |
| **re-** | again | re-kom | re-come = return |
| **pre-** | before | pre-lern-hous | pre-school |
| **mis-** | error | mis-tok | mis-speak |
| **over-** | excess | over-hapi | over-happy |
| **under-** | deficiency | under-dev | under-developed |
| **self-** | reflexive | self-lov | self-love |
| **non-** | absence | non-topi | non-topi |
| **auto-** | self | auto-matik | automatic |
| **semi-** | half | semi-kol | semi-circle |
| **super-** | above | super-nais | super-nice |
| **inter-** | between | inter-nais | internationally nice |

### 14.2 Productive Suffixes

| Suffix | Meaning | Example | Result |
|--------|---------|---------|--------|
| **-er** | agent | wok-er | worker |
| **-ing** | action/continuous | wok-ing | working |
| **-ed** | past tense | wok-ed | worked |
| **-wil** | future tense | wok-wil | will work |
| **-a** | present tense | wok-a | works |
| *(none)* | adjective | nais | nice |
| **-um** | adverb | nais-um | nicely |
| **-nes** | abstract noun | happi-nes | happiness |
| **-ful** | full of | hope-ful | hopeful |
| **-les** | without | hope-les | hopeless |
| **-bl** | capable | understand-bl | understandable |
| **-ish** | resembling | child-ish | childish |
| **-skap** | condition/state | happi-skap | happiness/condition |

### 14.3 Verb-Related Suffixes

| Suffix | Meaning | Example |
|--------|---------|---------|
| **-if** | related to | simpi-if → simplif → simplify |
| **-fai** | to make | simpi-fai → simplifai → to simplify |

---

## 15. Compounds

### 15.0 The Atomic Word Ceiling

VELA has a **soft ceiling of 200 atomic words** (Tier 0: 50 closed + Tier 1: 150 open with Quality Gate). All remaining vocabulary is built via compounding and derivation. This ceiling ensures:

- **Learnability:** A learner memorizes ~200 roots, not 900+.
- **Derivational power:** Compounds become the productive engine.
- **Phonotactic integrity:** Over-creating atoms would force violations of (C)V.

> **Quality Gate for Tier 1 atoms:** A candidate atom must pass at least 3 of 4 tests: (1) Not infantile-decomposable, (2) Frequent across languages, (3) Short (1-2 syllables), (4) Semantically unique (not a transparent compound of existing roots). See `vote/topics/consensus/ATOM_CEILING_consensus.md` for the full deliberation.

### 15.1 Two-Root Compounds

Two-root compounds are written **together without space or hyphen**:

| Compound | From | Meaning |
|---------|------|---------|
| **sunlait** | sun + lait | sunlight |
| **hauskel** | haus + kel | household |
| **wok-er** | wok + er | worker |
| **wotc-man** | wotc + man | watchman |
| **self-lov** | self + lov | self-love |
| **strongmind** | strong + mind | strong-minded |
| **fainal** | fain + al | final |
| **over-hapi** | over + hapi | over-happy |

### 15.2 Three+ Root Compounds

For longer compounds, use hyphens between roots for clarity:

```
wotc-man-nes      → watchmanship (the quality of watching)
liv-siti          → city where one lives / dwelling
```

### 15.3 Compounds and Cases

When a compound noun takes a case suffix, the suffix goes on the **last root only**:

```
sunlait-se        → of the sunlight   (NOT: sun-la-se-it)
hauskel-s-se      → of the households
```

---

## 16. Sentence Types — Full Paradigms

### 16.1 Declarative Sentences

Standard SVO statements:

```
Mi              si       la film.         → I see the film.
Yu              lik      la sonj.          → You like the song.
La big man-se   her      la strong vois.   → The big man's voice is heard.
Wi              liv      la siti-to.       → We live in the city.
```

###
### 16.2 Negated Sentences

```
Mi no si la man.          → I don't see the man.
Yu no wan kom.            → You don't want to come.
Li no es-ed hapi.        → She wasn't happy.
Wi no kan wok.            → We can't work.
De nevr kom.              → They never come.
```

### 16.3 Questions

```
Yu si la film q?          → Do you see the film?
Hu yu si?                 → Who do you see?
Wat yu lik?               → What do you like?
Wen wi kom?               → When do we come?
Yu wan kom or no?         → Do you want to come or not?
Li her-ed q?              → Did she hear?
```

### 16.4 Imperative Sentences

Imperatives use the present tense verb form (no subject):

```
Si la film!               → See the film!       (order to you)
Kom tu mi!                → Come to me!
No wok!                    → Don't work!
Liv la siti-to!            → Live in the city!

With emphasis:
Yu mas si!                → You MUST see!
Wi mas wok!                → We MUST work!
```

### 16.5 Conditional Sentences

```
If yu kom, den mi es hapi.       → If you come, then I am happy.
If yu no kom, den mi go.         → If you don't come, then I go.
If li wok-ed, den li her-ed.     → If she had worked, then she would have heard.
```

### 16.6 Sentences with Cases

```
Nominative:
  La man si la film.              → The man sees the film.
  (man = subject NOM; film = object ACC)

Accusative:
  Yu si la man.                    → You see the man.
  (man = direct object after verb = ACC)

Genitive:
  Mi si la man-se hous.          → I see the man's house.
  (man-se = genitive; hous = possessed)

Locative:
  Mi liv la siti-to.              → I live in the city.
  (siti-to = locative)

Genitive + Locative:
  La man-se famili liv la siti-to. → The man's family lives in the city.
```

### 16.7 Sentences with Modal Verbs

```
Mi kan si la film.              → I can see the film.
Yu mas wok.                      → You must work.
Li wan kom.                      → She wants to come.
Wi no kan liv la siti-to.        → We cannot live in the city.
De mas no don dat.               → They must not do that.
```

---

## Summary — Grammar at a Glance

```
WORD ORDER:      SVO (strict)
ARTICLES:        la (the), un (a/an)
CASES:           NOM = order | ACC = order | GEN = -se | LOC = -te
PLURAL:          -s
ADJECTIVES:      base (before noun)
ADVERBS:         base-um
PRESENT TENSE:   root + -a
PAST TENSE:      root + -ed
FUTURE TENSE:    root + -wil
PROGRESSIVE:     root + -an
MODALS:          kan, mas, wan (followed by bare root)
NEGATION:        no + verb
YES/NO QUESTIONS: sentence + q
WH-QUESTIONS:     hu / wat / wen / wer / hai / wai / hou
COMPARISON:       mor + im (comp) | mos + im (superl)
CONJUNCTIONS:     and, or, bot, bikos, if, wen, den, so
PRONOUNS:         mi, yu, li, wi, de
POSSESSIVE:       mif, yuf, liz, wef, def
NUMBERS:          wan tu tri kwatro faiv siks sevn eit nain ten / tu-ten tri-ten...
DAYS:             Mondei Tiuzdei Wenzdei Terzdei Fraidei Satrdei Sandei
```

---

## Design Decision Log

| Decision | Date | Source |
|----------|------|--------|
| SVO word order | 2025-04-13 | Simplicity + accessibility |
| la/un articles | 2025-04-13 | INITIAL_RESEARCH.md |
| 5 pronouns (mi yu li wi de) | 2025-04-13 | Simplicity |
| Possessive -f / Genitive -se distinction | 2025-04-13 | Transparency |
| 2-case minimal system | 2025-04-13 | VELA Decision Framework |
| Noun case = NOM/ACC by order | 2025-04-13 | VELA Decision Framework |
| Adjective bare root before noun | 2025-04-13 | Simplified, word order disambiguates |
| Zero irregular verbs | 2025-04-13 | Core VELA feature |
| bi/bi-a/bi-ed/bi-wil for "to be" | 2025-04-13 | Regularity over English irregularity |
| Adverb -um suffix | 2025-04-13 | Systematic morphology |
| Wh-question words from English | 2025-04-13 | English as primary vocabulary source |
| Conditional: if... den... | 2025-04-13 | Clarity + simplicity |
| No grammatical gender | 2025-04-13 | Simplicity |

---

**GRAMMAR COMPLETE ✅**
