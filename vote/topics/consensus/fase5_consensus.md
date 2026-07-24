# VELA Committee Consensus — Fase 5 Full Lexicon Review

**Date:** 2026-07-24
**Status:** ✅ RATIFIED — 5 specialist reviews + 3-agent consensus ballot
**Scope:** All ~246 words in `docs/lexicon/LEXICON_EXTENDED.md` (23 domains)
**Method:** Multi-agent deliberation over the NATS bridge. 3 Pi agents, distinct models, each acting as a specialist across two rounds.

---

## Participants

| Specialist | Agent | Round |
|-----------|-------|-------|
| Phonologist | pi-73824 | 1 |
| Lexicographer | pi-75181 | 1 |
| Semanticist | pi-78143 | 1 |
| Morphologist | pi-75181 | 2 |
| Aestheticist | pi-73824 | 2 |

Full individual reviews in `vote/topics/proposals/fase5_{phonologist,lexicographer,semanticist,morphologist,aestheticist}.md`.

Orchestration + synthesis: Claude Code (claude-code-64205).

---

## Resolutions

### R1 — Atom ceiling: TWO-TIER (adopted, amended)

The 200-atom soft ceiling is retroactively impossible: Phases 1–4 already hold ~350–400 atoms. Resolution:

- **Core tier** — a soft *target* of ~200 atoms (not a closed set).
- **Domain registers** — tech, science, arts, abstract — are an **open class**.
- **Every loan in a domain register must carry a ≤3-root transparent compound alternative** (or be flagged for future compound development).

*Vote: pi-73824 APPROVE, pi-78143 APPROVE, pi-75181 AMEND (soft ceiling, compound-alternative requirement — adopted).*

### R2 — Phonotactics: thematic vowel /a/ + cluster bans (adopted)

- **Thematic vowel rule:** any loan or root ending in an illegal single coda consonant (/d g p t k s f v ʃ/) receives a default **/a/** to close the syllable (`kod → koda`, `bug → buga`). Fixes ~70% of violations (~115 words).
- **Banned final clusters** (must be restructured, not merely suffixed): `-tm -mnt -sm -ʃn -bl -ks -st -rd -rs -tr -ns -nt -nd -kl -dl -lt -lf -nr -dr -kt -sk -pt -nkr`. ~32 words affected.
- **Grandfathered Phase 4 roots** with illegal codas (`fors, art, self, god`) evolve to `forsa, arta, sela, goda` in new compounds, with a **2-release deprecation window**.

*Vote: unanimous APPROVE. /θ ð ʒ/ inventory confirmed clean.*

### R3 — Loan overload: compound-first (adopted, both amendments merged)

62% of Phase 5 words were loans; Ethics, Politics, and Arts were ~100% loans — a violation of VELA's compound-first philosophy. Resolution combines the lexicographer's pragmatism with the semanticist's harder push:

- Where a word is **also phonotactically broken**, replace it outright.
- Otherwise, the **transparent compound becomes the preferred form** and the loan is retained as a domain-register synonym (this is R1 in action).

Semanticist replacements adopted:

| Loan | Preferred compound | Gloss |
|------|--------------------|-------|
| `moral` | `rait-rong-sistam` | right-wrong-system |
| `etik` | `rait-rong-lern` | right-wrong-study |
| `harm` | `bada-mak` | bad-make |
| `responsibil` | `du-nob` | duty-bound |
| `parlamnt` | `rul-mak-hous` | rule-make-house (also fixes /mnt/) |

*Vote: pi-75181 APPROVE, pi-73824 APPROVE, pi-78143 AMEND (push harder — adopted).*

### R4 — Emotion clusters: keep the architecture (adopted)

The 18 compound emotions are VELA's gold standard (transparent, 0% loans). Kept as canonical. The 5 forms the aestheticist flagged as "clinical" (`blok-angri`, `enuf-hapi`, `big-afred`…) stay — the semanticist confirmed they are semantically precise. The aestheticist may add **poetic synonyms** on top; these do not replace the transparent compounds. A lightweight **POETIC / PROSE lexical tag** is adopted to let poets avoid prose-only loans.

*Vote: unanimous APPROVE.*

### R5 — Targeted fixes (adopted)

- `pilgrimage → pilgrimej` (worst un-nativized loan)
- `-shon` spelling **always** standardized: `fikshn → fikshon`, `non-fikshn → non-fikshon`, etc.
- Beauty swaps (aestheticist): `tretmnt → kura`, `govrnr → rul-po`, `varibl → chanj-tip`, `vershn → edi-shon`, `ekshibishon → shou-hous`.

*Vote: unanimous APPROVE.*

### R6 — Canon plural bug: resolved (adopted)

`GRAMMAR_COMPLETE.md` contradicted itself. Resolution:

- **Suffix:** `-n` after vowel-final, `-en` after consonant-final is the **single canonical rule**. All `-s` plural statements (line ~993 and `ROADMAP.md`) are deleted.
- **Morpheme order:** **root → NUMBER → case** (`man-en-se` = "of the men"). Number is inner/stem-level morphology; case is outer/syntactic. Cross-linguistic evidence: German `Mann-e-n`, Latin stem+number+case. The `man-se-n` form in §4.9 is the error and is removed.

*Vote: unanimous APPROVE (morpheme-order verdict by morphologist pi-75181).*

---

## Systemic findings — reviewed 2026-07-24

1. **Homonymy clashes — resolved by the Fase 5 changes, no action needed.** The lexicographer's "7 clashes" were mostly overtaken by R2/R5:
   - `fors → forsa`, `spid → spida` (R2 thematic vowel) — no longer collide.
   - `bit` (computing) vs music beat — already resolved: beat is `muzika-bita`.
   - `masa` (mass) vs `mas` (must-modal) — **not homonyms**; distinct forms.
   - `stap` (step) vs `stop` — no clash; `stop` is `topi`.
   - `tip` — related polysemy (type / to type), same as English; acceptable.
   - `kor` (choir) — the only **latent** risk: no `core`/`center` word exists yet, but if added it may not reuse `kor`. **Reserved form.** If `core` is later needed, `choir` can move to a transparent compound (e.g. `sing-grupa`) to free `kor`.
2. **Locative `-te` vs `-to` — FIXED 2026-07-24.** Prior consensus had decided `-to`; `GRAMMAR_COMPLETE.md` was only half-applied (rules/AFI said `-te`, examples said `-to`). All `-te` locatives standardized to `-to`. Also fixed a stale `mor/mos + im` comparison line (the `-im` suffix was eliminated by prior consensus).
3. **Poet's vocabulary is starved** (aestheticist): Phase 6 should prioritize sensory/atmosphere atoms (dawn, dusk, mist, silence). Carried to Fase 6.
4. **8 idioms rated masterpieces** (aestheticist): river, bird/sky, dark room, quiet water, sea/beach — the strongest of the 20.

---

## Amendment — 2026-07-24 (automated validator + R2 scope)

An automated validator (`scripts/validate_phonology.py`, built from `PHONOLOGY_FINAL.md` §3.2) revealed that R2, read literally, conflicts with compounding from VELA's consonant-final native roots (`lern`, `mak`, `sad`, `nof`…). You cannot build `masin-lern` and end in a vowel without re-voweling the entire core + corpus.

**Resolution — both specialists (pi-73824, pi-75181) voted A:**

- **The thematic-vowel rule applies to LOANS and genuinely new roots only.** Native roots stay grandfathered inside compounds (`masin-lern`, `bada-mak`, `dep-nof` are correct as-is).
- **Legal root inventory = all `LEXICON_BASE.md` headwords + the errata roots** (`art, net, sav, tip, stap, grup, bit, kod, wei, taim`). Anything outside that inventory must be vowel-final.
- **Diphthong endings** (`-y`, `-w` after a vowel: `deploy`, `sey`, `bow`) are vowel-final, not codas.
- **6 genuinely-new coinages fixed:** `chanj-tip → chanja-tip`, `du-nob → du-noba`, `kolaj → kolaja`, `pilgrimej → pilgrimeja`, `paraiz → paraiza` (`deploy` kept — already vowel-final).

After the amendment, `LEXICON_EXTENDED.md` validates with **0 errors**.

**`th` = /θ ð/ nativization — DONE 2026-07-24.** 9 legacy `LEXICON_BASE.md` words used `th`, a phoneme absent from VELA's inventory (no grandfathering — the sound does not exist). Fixed with `/θ/ → /t/`, `/ð/ → /d/` (the convention already applied in their own AFI: `thick` was already /tik/, `thin` /tin/, `smooth` /smud/, `theory` /teori/ — only the spelling lagged): `think→tink, thick→tik, thin→tin, smooth→smud, helthi→helti, month→mont, lethr→leder, theory→teori, throu→trou`. `throu→trou` (throw) keeps the `/ou/` diphthong, avoiding a clash with `tru` (true). Note: `zh` was rejected as an alternative — it spells /ʒ/, also absent from the inventory. Corpus (poems, stories) swept for the VELA-side old forms. Validator: 0 errors across 1439 words.

## Applied

- `docs/lexicon/LEXICON_EXTENDED.md` — R1–R5 word forms, AFI, examples, plurals.
- `docs/grammar/GRAMMAR_COMPLETE.md` — R6 plural rule + morpheme order.
- `vote/docs/CHANGE_LOG.md` — dated entry.
- `ROADMAP.md` — Fase 5 status + plural note.
