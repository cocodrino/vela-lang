# VELA Case System — Decision: Option 3 (Minimal Design)

> **Design decision: 2025-04-13** — Based on VELA's founding principles.
> **Method:** Apply the VELA Decision Framework first — only mark what cannot be inferred.
> **Updated: 2026-05-13** — Following multi-agent deliberation. Changes: locative -te → -to, plural suffix changed -s → -n/-en, possessive pronouns unified.

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

## The 2-Case System: Option 3 (Updated)

VELA marks **only** what word order cannot express:

| Case | When to use | Suffix | Why needed |
|------|------------|--------|-----------|
| **Genitive** | Possession, origin, relationship | **-se** | Word order cannot distinguish "the man's dog" from "the dog bites the man" |
| **Locative** | Location, time | **-to** | "in the city" vs "the city" — prepositions alone are ambiguous in complex sentences |

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

### Locative — suffix **-to**

Used for location or time. Replaces prepositions like "in", "at", "on", "from" when those mark location or time.

```
Mi liv la siti-to.        → I live in the city.
Li es la klas-to.         → She is in class.     (location)
De kom la las dei-to.    → They come on the last day. (time)
Wi wok la ofis-to.        → We work at the office. (location)
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

The case suffix precedes the plural suffix for clearer pronunciation and prosody:

```
 GEN-SG:  la man-se dog    → The man's dog
 GEN-PL:  la man-se-n dog  → The men's dogs

 LOC-SG:  la siti-to       → In the city
 LOC-PL:  la siti-to-n     → In the cities
```

Order: **ROOT → CASE → PLURAL**

This prevents coda stacking (e.g., man-se-n)`) and preserves prosodic clarity, ensuring the case morpheme stays closest to its root.

---

## Interaction with Adjectives

Adjectives **do not take case suffixes** — they agree with the noun's case by position:

```
GEN: La big man-se hous    → The big man's house
     big (adjective) modifies man, which is genitive

LOC: Mi liv la big siti-to → I live in the big city
     big (adjective) modifies siti, which is locative
```

The adjective precedes the noun it modifies, regardless of case.

---

## Interaction with Prepositions

Prepositions already mark semantic role. When a preposition is present, the locative suffix is **optional**:

```
Mi liv en la siti.       → I live in the city.      (en = in)
Mi liv la siti-to.        → I live in the city.      (LOC suffix alone)

Mi wok at la ofis.        → I work at the office.
Mi wok la ofis-to.        → I work at the office.    (equivalent)
```

**Rule:** In the presence of a preposition, the locative suffix can be dropped. Without a preposition, `-to` is required to mark location/time.

---

## Case + The Verb "bi" (to be)

With `bi` (to be), the locative suffix marks location only. For state or condition, use the bare adjective:

```
Mi es la siti-to.         → I am in the city.        (location)
```

For states and conditions, the bare adjective is the standard form:
```
Mi es hapi.              → I am happy.
Li es strong.            → She is strong.
Wi es nais.              → We are nice.
```

The bare adjective is the preferred form. The old stative use of `-to` (e.g., `strong-to`, `hapi-to`) has been retired to preserve monosemy — `-to` marks spatial/temporal location only.

---

## Full Paradigm: man (person)

| Case | Singular | Plural |
|------|----------|--------|
| **Nominative** | man | man-en |
| **Accusative** | man | man-en |
| **Genitive** | man-**se** | man-**se**-**s** |
| **Locative** | man-**to** | man-**to**-**s** |

---

## Possession — Unified with Genitive **-se**

All possession, whether the possessor is a pronoun or a noun, uses the genitive suffix **-se**:

```
Mi-se dog.              → My dog.
Yu-se buk.              → Your book.
Li-se kar.              → His/her car.
Wi-se hous.             → Our house.
De-se siti.             → Their city.
```

**Rule:** Possessor + `-se` = possession. Always. No exception, no alternate pronoun paradigm.

The old short possessive forms (`mif`, `yuf`, `liz`, `wef`, `def`) have been retired.

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
| Locative: **-to** | 2026-05-13 | Multi-agent deliberation (Phonologist + Aestheticist convergence) |
| No accusative suffix | 2025-04-13 | SVO order handles it without morphology |
| No nominative suffix | 2025-04-13 | Always the pre-verbal noun, no ambiguity |
| Plural + case order: case → plural | 2026-05-13 | Multi-agent deliberation; prevents sibilant stacking |
| Preposition overrides locative suffix | 2025-04-13 | Avoids double-marking; simpler |
| Possession: unified under **-se** | 2026-05-13 | Multi-agent deliberation; eliminates dual system |
| State: bare adjective only | 2026-05-13 | Multi-agent deliberation; preserves monosemy of -to |

---

## Sound Check

Both suffixes follow VELA's phonotactic rules perfectly:

| Suffix | Ends in V? | Distinct? | Passes (C)V? |
|--------|-----------|----------|--------------|
| **-se** | ✅ vowel /e/ | Distinct from -to | ✅ |
| **-to** | ✅ vowel /o/ | Distinct from -se | ✅ |

**No phonotactic violation. Both are clearly distinct from all root-final sounds, and the vowel contrast (/e/ vs /o/) maximizes perceptual salience.**

---

## Example Sentences — Full System in Action

```
NOM:  Mi            si       la film.
      [subject-NOM] [verb]    [direct object]

ACC:  La man        si        mi.
      [subject-NOM] [verb]   [direct object-ACC by position]

GEN:  Mi            si        la man-se         hous.
      [subject]     [verb]    [possessor-GEN + noun]

LOC:  Mi            liv       la siti-to.
      [subject]     [verb]    [noun-LOC by suffix]

GEN+LOC:  La man-se    famili    es     la vilaj-to.
          [man-GEN]    [family]  [be]   [village-LOC]
          → The man's family is in the village.

STATE:  Li            es        strong.
        [subject]     [be]      [adjective — no suffix]
        → She is strong.
```
