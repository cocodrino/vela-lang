# VELA Committee Deliberation — FULL FASE 5 LEXICON REVIEW

**Date:** 2026-05-31
**Status:** OPEN — pending 5 specialist reviews
**Proposed by:** Claude (Fase 5 lexicon team)
**Scope:** ALL 232 words in `docs/lexicon/LEXICON_EXTENDED.md`
**Method:** Domain-level group verdicts (NOT word-by-word)

---

## Instructions for Specialists

Read `docs/lexicon/LEXICON_EXTENDED.md` using `read_file`. Then deliver a **domain-level verdict** for each of the 23 domains, classifying every word in that domain into one of three buckets:

| Bucket | Action |
|--------|--------|
| **TIER A — Approve** | Phonotactically valid, semantically transparent, follows VELA constraints. No issues. |
| **TIER B — Approve with adjustment** | Concept is right, but form needs minor fix (orthography, AFI, hyphenation, root swap). Specify exact fix. |
| **TIER C — Reject / Propose alternative** | Violates hard constraint OR better alternative exists. Suggest replacement compound or atom. |

---

## Critical Constraints to Enforce

1. **200-atom soft ceiling** — loans count toward atoms. Are there too many?
2. **Quality Gate for Tier 1 atoms** — must pass ≥3 of 4 tests. Loans need justification.
3. **Compound length rule** — max 3 roots. Flag any 4+ root compounds.
4. **Phonotactic inventory** — VELA has no /θ/, /ð/, /ʒ/. Loans must be nativized.
5. **Structural homonymy** — avoid forms that clash with existing morphemes (e.g., `wil` = future suffix).
6. **`-nes` suffix** — established for abstract nouns (`tru-nes`). Is it applied consistently?
7. **`-po` suffix** — established for profession (`vote-po`). Is it applied consistently?
8. **Hyphenation** — `self-` prefix = hyphenated; root+root = currently hyphenated in practice (despite §15.1).

---

## Domain List (23)

| # | Domain | Words | Loan % | Key Concerns |
|---|--------|-------|--------|-------------|
| 1 | Software Development | 17 | ~82% | kod, bug, loop, branch as atoms? |
| 2 | Hardware | 9 | ~55% | brain-chip, piktur-chip = 3 roots? |
| 3 | Internet/Networks | 11 | ~64% | lowd-in/lowd-up pattern consistency |
| 4 | Artificial Intelligence | 10 | ~50% | ai-instruk = acronym+root? |
| 5 | Data | 9 | ~78% | kript, sinkr, kash = loans |
| 6 | Biology | 15 | ~73% | selu = Latin loan justified? |
| 7 | Chemistry | 10 | ~80% | atom = international, kompound = loan |
| 8 | Physics | 14 | ~79% | fol-fors = gravity (existing); fors/enrji = loans |
| 9 | Astronomy | 13 | ~77% | far-si-tool = 3 roots (max allowed) |
| 10 | Medicine — Extended | 12 | ~83% | anti-bodik = 2 roots; kron-sik = 2 roots |
| 11 | Music | 16 | ~69% | big-muzik-grup = 3 roots; muzik-mak-po = 3 roots + -po |
| 12 | Visual Arts | 10 | ~90% | All loans except art-hous |
| 13 | Literature | 13 | ~85% | All loans except long-stor, buk-part, poem-lain, non-fikshn |
| 14 | Film and Theater | 8 | ~88% | film-rul-po = 3 roots + -po; all others loans |
| 15 | Philosophy | 12 | ~67% | self-nof, fri-chuz, tru-nes, nof-nes, dep-nof = compounds ✅ |
| 16 | Ethics and Morality | 10 | ~100% | ALL loans — is this justified? |
| 17 | Politics and Society | 11 | ~100% | ALL loans except vote-po |
| 18 | Religion and Spirituality | 10 | ~90% | god-ador = compound; rest loans |
| 19 | Sadness Cluster | 5 | ~0% | dep-sad, los-pain, blok-angri, past-luv-pain, loili-sad |
| 20 | Joy Cluster | 4 | ~0% | kwaiat-hapi, top-hapi, enuf-hapi, warm-hapi |
| 21 | Fear Cluster | 4 | ~0% | futur-afred, tot-afred, big-afred, dep-afred |
| 22 | Love Cluster | 5 | ~20% | luv = atom; warm-fel, strong-luv, dep-luv = compounds; kea = loan |
| 23 | Wonder and Curiosity | 4 | ~75% | wundr, kurius, inspir = loans; wait-hapi = compound |

---

## Key Systemic Questions

1. **Loan overload:** 145 of 232 words (62%) are loans. Does this violate VELA's compound-first philosophy?
2. **Emotion fine distinctions:** 18 new emotion compounds. Are they too granular? Do they all pass transparency tests?
3. **`-nes` consistency:** `tru-nes`, `nof-nes` use `-nes`. Should more abstract nouns use this suffix?
4. **`-po` consistency:** `muzik-mak-po`, `film-rul-po`, `vote-po`. Is the profession suffix applied correctly?
5. **`luv` status:** Listed as "atomic — cross-ref Phase 4" AND in "Phase 4 Errata — Missing Atomics". Is it approved or pending?
6. **`kea`** — what language is this from? What does it mean exactly?

---

## Deliverable

Write your analysis to your designated proposal file. Format:

```
# [Specialist] Review: Fase 5 Full Lexicon

## Executive Summary
[Overall verdict: how many domains approved, how many flagged]

## Domain-by-Domain Verdicts

### 1. Software Development (17 words)
**Verdict:** APPROVE / FLAG / REJECT [domain]
- **TIER A (Approve):** word1, word2, ...
- **TIER B (Adjust):** word3 → [exact fix], word4 → [exact fix]
- **TIER C (Reject):** word5 → [suggest alternative]
**Rationale:** [2-3 sentences]

### 2. Hardware (9 words)
...

[Continue for all 23 domains]

## Systemic Issues
[List cross-domain problems discovered]

## Recommendations
[Top 3-5 actionable recommendations]
```

⚠️ **You do NOT have access to native file tools (bash, grep, write, edit).** You CAN use `read_file` via Serena to read the lexicon file. Write your output using available tools.
