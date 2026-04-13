# VELA Case System — Decision: Option 3 (Minimal Design)

> **Design decision: 2025-04-13** — Based on VELA's founding principles.
> **Method:** Apply the VELA Decision Framework first — only mark what cannot be inferred.

---

## The VELA Decision Framework Applied

When designing a case system, the first question is:

> *"What does VELA really need to mark?"*

English manages with **zero noun case marking** — word order does the job. Spanish marks some possession with `de` and direct object with `a`. Esperanto adds the accusative `-n`. But VELA's goal is the **minimum necessary** — not the maximum expressible.

**VELA Principle 1: Simplicity First.**
If word order can express it → don't add a suffix.

**VELA Principle 2: Transparency Always.**
If we do add a suffix → it means exactly one thing.

**VELA Principle 3: Beauty.**
The fewer suffixes, the more euphonic the language sounds.

---

## The 2-Case System: Option 3

VELA marks **only** what word order cannot express:

| Case | When to use | Suffix | Why needed |
|------|------------|--------|-----------|
| **Genitive** | Possession, origin, relationship | **-se** | Word order cannot distinguish "the man's dog" from "the dog bites the man" |
| **Locative** | Location, time, state | **-te** | "in the city" vs "the city" — prepositions alone are ambiguous in complex sentences |

**Nominative and Accusative are FREE** — determined entirely by SVO word order.

This is **radically simple**: 2 suffixes instead of 4-8.

---

## How It Works

### Genitive — suffix **-se**

Used when a noun modifies another noun (possession, origin, relationship).

```
La man-se dog.            → The man's dog.
Yu her la sun-se lait.   → You hear the sunlight. (the light OF the sun)
Mi lik la famili-se prien. → I like the family's friend.
```

The noun after `-se` modifies the noun before it. Simple and transparent.

### Locative — suffix **-te**

Used for location, time, or state. Replaces prepositions like "in", "at", "on", "from" when those mark location or time.

```
Mi liv la siti-te.        → I live in the city.
Li es la klas-te.         → She is in class.     (location)
De kom la las dei-te.    → They come on the last day. (time)
Wi wok la ofis-te.        → We work at the office. (location)
```

### Nominative — no suffix

The subject of any sentence.

```
Mi si la film.            → I see the film.
Yu lik la sonj.           → You like the song.
La man si mi.             → The man sees me.      ← word order does the job
```

### Accusative — no suffix

Direct object, placed after the verb.

```
Yu si la man.             → You see the man.    ← subject-object clear by position
La man si mi.            → The man sees me.    ← no suffix needed
De si la siti.           → They see the city.
```

---

## Interaction with Plurals

The plural suffix **-s** goes after the case suffix:

```
 GEN-SG:  la man-se dog    → The man's dog
 GEN-PL:  la man-s-se dog  → The men's dogs

 LOC-SG:  la siti-te       → In the city
 LOC-PL:  la siti-s-te     → In the cities
```

Order: **ROOT → CASE → PLURAL**

This is the most transparent order — case first, then plurality, closest to the root.

---

## Interaction with Adjectives

Adjectives **do not take case suffixes** — they agree with the noun's case by position:

```
GEN: La big man-se hous    → The big man's house
     big (adjective) modifies man, which is genitive

LOC: Mi liv la big siti-te → I live in the big city
     big (adjective) modifies siti, which is locative
```

The adjective precedes the noun it modifies, regardless of case.

---

## Interaction with Prepositions

Prepositions already mark semantic role. When a preposition is present, the locative suffix is **optional**:

```
Mi liv en la siti.       → I live in the city.      (en = in)
Mi liv la siti-te.        → I live in the city.      (LOC suffix alone)

Mi wok at la ofis.        → I work at the office.
Mi wok la ofis-te.        → I work at the office.    (equivalent)
```

**Rule:** In the presence of a preposition, the locative suffix can be dropped. Without a preposition, `-te` is required to mark location/time.

---

## Case + The Verb "bi" (to be)

With `bi` (to be), the locative suffix marks state or location:

```
Mi es la siti-te.         → I am in the city.        (location)
Li es strong-te.           → She is in strength.      (state)
Wi es hapi-te.            → We are in happiness.     (state)
```

The bare adjective is also valid:
```
Mi es hapi.              → I am happy.              (equally valid)
Li es strong.            → She is strong.            (equally valid)
```

Both are correct. `-te` adds emphasis on the state as a condition.

---

## Full Paradigm: man (person)

| Case | Singular | Plural |
|------|----------|--------|
| **Nominative** | man | man-s |
| **Accusative** | man | man-s |
| **Genitive** | man-**se** | man-s-**se** |
| **Locative** | man-**te** | man-s-**te** |

---

## Genitive -se vs Possessive Pronouns

The possessive pronouns already cover most possession cases:

| Pronoun | Possessive (short) | Genitive (full) |
|---------|-------------------|-----------------|
| my | mif | mi-**se** |
| your | yuf | yu-**se** |
| his/her/its | liz | li-**se** |
| our | wef | wi-**se** |
| their | def | de-**se** |

```
Mi si mif dog.        → I see my dog.              (possessive pronoun)
Mi si la man-se dog.  → I see the man's dog.       (genitive noun)
```

**Rule:** Use the possessive pronoun when the possessor is a pronoun. Use `-se` when the possessor is a full noun phrase.

---

## Why NOT more cases?

| More cases would add... | But VELA doesn't need them because... |
|------------------------|---------------------------------------|
| Accusative `-a` | SVO word order handles subject/object distinction clearly |
| Dative `-de` | `a la man` or word order disambiguates |
| Instrumental | `wit` (with) preposition covers it |
| Ablative | `from` preposition covers it |

**VELA's principle: if a preposition or word order can do the job, a case suffix is not needed.**

---

## Design Decision Log

| Decision | Date | Source |
|----------|------|--------|
| 2-case system (not 4) | 2025-04-13 | VELA Decision Framework: minimal necessary |
| Genitive: **-se** | 2025-04-13 | Phonetically distinct; marks possession clearly |
| Locative: **-te** | 2025-04-13 | Marks time/space; very distinct from -se |
| No accusative suffix | 2025-04-13 | SVO order handles it without morphology |
| No nominative suffix | 2025-04-13 | Always the pre-verbal noun, no ambiguity |
| Plural + case order: case → plural | 2025-04-13 | Closest to root = most specific first |
| Preposition overrides locative suffix | 2025-04-13 | Avoids double-marking; simpler |
| `bi` + LOC: both forms valid | 2025-04-13 | Flexibility without ambiguity |

---

## Sound Check

Both suffixes follow VELA's phonotactic rules perfectly:

| Suffix | Ends in V? | Distinct? | Passes (C)V? |
|--------|-----------|----------|--------------|
| **-se** | ✅ vowel /e/ | Distinct from -te | ✅ |
| **-te** | ✅ vowel /e/ | Distinct from -se | ✅ |

**No phonotactic violation. Both are clearly distinct from all root-final sounds.**

---

## Example Sentences — Full System in Action

```
NOM:  Mi            si       la film.
      [subject-NOM] [verb]    [direct object]

ACC:  La man        si        mi.
      [subject-NOM] [verb]   [direct object-ACC by position]

GEN:  Mi            si        la man-se         hous.
      [subject]     [verb]    [possessor-GEN + noun]

LOC:  Mi            liv       la siti-te.
      [subject]     [verb]    [noun-LOC by suffix]

GEN+LOC:  La man-se    famili    es     la vilaj-te.
          [man-GEN]    [family]  [be]   [village-LOC]
          → The man's family is in the village.
```
