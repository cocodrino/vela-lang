# Deliberation Topic — Gender-Neutral Profession Suffix

## Background
The user explicitly rejected the `-man` suffix for professions due to gender inclusivity concerns. "man" carries masculine connotation that feels exclusionary.

**USER PREFERENCE STATED**: The user personally likes **`-er`** as the suffix, citing it as their preferred form. They are open to alternatives if the specialists find strong reasons against it, but `-er` is the starting point.

## Current State
In `vote/topics/propose.md`, the profession compounding system used `-man` and `-wuman`:
- `lern-man` = teacher
- `sik-fix-man` = doctor
- `food-mak-man` = chef
- `nors` → `sik-help-wuman` was used as "nurse"

This pattern has been rejected.

## Core Requirements
1. **Gender-neutral**: Must not default to masculine or imply binary gender
2. **Phonologically valid**: Must work with (C)V template — vowel-final or /n,m,l,r/
3. **Internationally recognizable**: Recognizable across language families
4. **Short**: Single syllable if possible; compounding already adds length
5. **Composable**: Must attach cleanly to any profession compound

## Candidate Suffixes to Evaluate

### USER'S PREFERENCE: `-er`
- `lern-er` = teacher
- `sik-fix-er` = doctor
- `food-mak-er` = chef
- `masin-fix-er` = engineer
- 1 syllable, ends in /r/ (legal coda)
- Internationally: English teacher/singer/writer, French -eur, Spanish -ero, German -er
- **Question**: Is it TOO English-centric? Does it feel masculine to non-English speakers?

### Option A: No suffix at all — context determines person
- Pattern: `lern` = teacher (profession = person who learns/teaches?)
- But VELA uses `lern` as "learn" verb. Ambiguous.
- How does one say "the teacher" vs "the learning"?

### Option B: `-po` / `-po` — from "person"
- `lern-po` = teach-person
- 1 syllable, vowel-final, phonotactically clean
- "Person" = /ˈpɜːrsn/ in English, /pɛʁ.sɔ̃/ in French, /perˈso.na/ in Spanish/Italian
- Not recognizable as "person" standalone without context

### Option C: `-ist` / `-isti`
- `lern-isti` = teacher (learn-ist)
- 2 syllables, vowel-final if `-isti`
- Recognizable: English scientist, artist; French artiste; Spanish/Italian -ista
- Latin *-ista*
- But 2 syllables is long

### Option D: Latin-derived `-or` / `-or`
- `lern-or` = teacher (learn-er?)
- `doktr` = doctor already ends in /r/
- But Romance `-or` is classically masculine in connotation (actor, doctor, professor)
- Not ideal for gender neutrality

### Option E: Esperanto-style (no suffix, root itself)
- Esperanto: `instruisto` = teacher
- But VELA prefers compounds over invented roots

### Option F: Suffix based on semantic role
- `-ant` / `-anti` — Latin present participle + person
- `lern-anti` = learning-one = learner/teacher
- 2 syllables if `-anti`
- Latin *amans* → French *amant*

### Option G: `-pe` — shorter, from "people"
- `lern-pe` = teach-people?
- Very short, 1 syllable
- Problem: "pe" might be confused with Spanish "pe" (initial of Pedro)

## Special Challenges for the Agents

### The "-er is too English" challenge
English `-er` is globally known (teacher, worker, singer). But is it international ENOUGH for VELA's standards? French uses `-eur`, Spanish `-ero`, German `-er`. The form is recognizable but not universal. Does this violate Rule 5 (not just respelled English)?

### The "profession = verb" challenge
If `lern` = "to learn" AND `lern-er` = "teacher", `sik-fix` = "to fix sick[ness]" AND `sik-fix-er` = "doctor" — the profession is derived from the action. This is semantically transparent but creates a system where every profession is a compound + suffix. Is that better than atomic roots?

### The "no suffix at all" challenge
Japanese avoids profession suffixes entirely: `sensei` = teacher, `isha` = doctor, ` untenshu` = driver. The context (social role, workplace) disambiguates. Can VELA do this?

## Data for Agents
Existing profession words in current LEXICON_BASE.md:
- `techer` = teacher
- `doktor` = doctor
- `drever` = driver
- `kuk` = cook
- `injinir` = engineer
- `artis` = artist
- `driver` = driver (duplicate?)
- `polis` = police (officer?)
- `lavyr` = lawyer (misspelled as lafyer in examples)
- `nors` = nurse
- `jornalist` = journalist
- `aktor` = actor
- `singa` = singer

Proposed transparent compounds (from propose.md, before -man rejection):
- `lern` → `lern-er` (user preference)
- `sik-fix` → `sik-fix-er`
- `food-mak` → `food-mak-er`
- `plant-grow` → `plant-grow-er`
- `word-mak` → `word-mak-er`
- `biju-mak` → `biju-mak-er`
- `masin-fix` → `masin-fix-er`
- `law-keep` → `law-keep-er`
- `war-fajt` → `war-fajt-er`
- `sik-help` → `sik-help-er` (nurse)
- `law-speak` → `law-speak-er` (lawyer)
- `news-tak` → `news-tak-er` (journalist)
- `rol-play` → `rol-play-er` (actor)
- `song-mak` → `song-mak-er` (singer)

## Voting rules
Start from USER PREFERENCE: `-er`. Evaluate whether there are strong reasons to reject it. If yes, propose the best alternative with justification.
