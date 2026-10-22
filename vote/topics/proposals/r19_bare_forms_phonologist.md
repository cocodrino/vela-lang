# R19 round — Phonologist ruling (bare forms as free words)

**Date:** 2026-10-22 · **Engine:** Claude subagent (Agent tool), read-only · **Topic:** `vote/topics/current_topic.md`

**FINAL VOTE: A**

## Dossier verification — no false claims found

- R7 (`fase5_consensus.md:131`) legislates a SINGLE hard final consonant, not clusters.
- R8 table (`fase5_consensus.md:159-160`): header defines legal as {n,m,l,r,s,ng}, yet lists `tok`, `liv`. R8's own prose then classes /k/,/v/ as hard (`toka`, `luva`) — a leftover from pre-R7 drafting, not a carve-out.
- GRAMMAR §6.1 (lines 456-457, 512-519): `toka`, `livi` (Core Verb List), but `lern` still in the soft row.
- PHONOLOGY_FINAL §4 (line 160): clusters only at syllable onset — unconditional. §3.2 never licenses a final cluster.
- `validate_phonology.py:9-10` already enforces the general §4 ban, not R2's list.
- Lexicon examples use bare forms (`Mi tok wit yu`, `Wi liv la siti-to`, `Yu lern VELA`) — a drafting habit, not a deliberate class.
- Course Level 1 is inconsistent: line 342 `Mi maka fuda nau` (citation) vs 553/666/679/831 `Mi liv siti-to` (bare).

## Rulings

| Q | Position | Vote |
|---|---|---|
| 1 | Errata. Drop `tok`/`liv` from R8's legal row; align GRAMMAR. | approve |
| 2 | A — R2's list was a snapshot of broken clusters at the time; PHONOLOGY_FINAL §4 is the general rule. Migrate cluster-final words too; amend R2's text to say so. | approve |
| 3 | Reject C. | approve (rejecting C) |
| 4, 5 | Deferred to morphologist/aestheticist and lexicographer. | — |

## Learnability across L1s

- **Mandarin, Japanese:** ban almost all codas except a nasal; `liv` (single /v/) and `lern`/`old`/`bird` (clusters) are equally hard. Single-vs-cluster is not the line that matters.
- **Hindi, Arabic:** tolerate many final clusters; not specially hard.
- **Spanish:** codas mostly n/s/l/r/d; sonorant-first clusters (`-rn`, `-rm`, `-ld`) are less harsh than obstruent ones (`-st`, `-sk`, `-ft`), but all are clusters and all are banned by §4 as written.
- Frequency does not reduce articulatory difficulty, which also argues against C.

**Risk:** §4 may not have been meant to touch native roots inside compounds — but R7 already protects compound forms; R19 only concerns free words.
