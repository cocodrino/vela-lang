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

---

## R7 — Alomorfía Cita/Composición (Opción D, ratificada unánime 2026-07-26)

Toda raíz de CONTENIDO con coda dura word-final (consonante fuera de {n,m,l,r,s,ng}) tiene **dos formas**:

- **Forma de CITA** (standalone / entrada de diccionario): raíz + vocal epentética `/a/` → `maka` (make), `luka` (look), `aska` (ask), `teacha` (teach). Vocal-final = pronunciable en aislamiento para cualquier hablante (hispano/asiático/etc.).
- **Forma de COMPOSICIÓN** (dentro de compuestos): raíz **bare** (sin la `-a`) → `mak-tin`, `luk-for`, `tok-tin`. La coda queda interna, acústicamente enmascarada por el ritmo del compuesto.

**Regla del aprendiz (una línea):** en composición, quita la `-a` de la forma de cita.

**Palabras FUNCIÓN** (at, of, and, if, wit, but, self…) quedan **grandfathered con forma única** — son monosílabos hiper-frecuentes tolerados en todo idioma natural; no reciben forma de cita.

Precedentes naturales de la alternancia: español (e-epéntesis: estado), latín (rex/reg-), japonés (人 jin/nin), turco (ev/ev-e), portugués (água/agua-).

Aplicado 2026-07-26: 273 raíces de contenido normalizadas a forma de cita; compuestos intactos; validador actualizado para reconocer las formas de composición bare.

---

## R8 — El presente = la forma de cita (ratificada unánime 2026-07-26)

**Conflicto detectado:** GRAMMAR_COMPLETE.md §6.1 declaraba presente = raíz + `-a` sin excepción (`liv-a`, `si-a`), pero TODO el corpus (PHRASES_100, poemas, cuentos, ejemplos del diccionario) usa la raíz pelada en presente (`Mi wan la dis`, `Mi luv mi-se mat`, `Mi hav a child`, `Wi si la starz`). El pasado sí es consistente (raíz+`-ed`).

**Voto:** ronda 1 → B, B, A (2-1). El fonólogo (A) detectó que bajo B puro `mak` /k/, `hav` /v/, `luv` /v/ son **codas ilegales** como palabra suelta — justo lo que R7 resolvió. Ronda 2 → síntesis **Opción C**, ratificada **C-sí unánime** (pi-29881 morfólogo, pi-26905 fonólogo, pi-34067 semantista).

**Regla:** el presente **no lleva marca gramatical propia**. El presente ES la forma de cita (R7). La `-a` de `maka`/`hava` no es marca de presente: es la vocal de cita que solo aparece donde la fonotáctica la exige.

| Tipo de raíz | Cita = Presente | Pasado | Futuro |
|---|---|---|---|
| Legal suelta (vocal-final o coda ∈ {n,m,l,r,s,ng}) | `si`, `go`, `wan`, `tok`, `liv`, `lern` | `si-ed` | `si-wil` |
| Coda dura (k,v,t,p,g,b,d,f,z,…) | `maka`, `hava`, `luva` | `mak-ed`, `hav-ed` (/ha.ved/) | `mak-wil` |

**Consecuencias:**
- `bi` (to be) mantiene su presente irregular `es` (única excepción, ya canónica).
- Pasado/futuro se unen a la raíz **pelada**; la coda dura queda en onset de la sílaba siguiente (`hav-ed` → /ha.ved/, legal).
- "maka = to make = makes" NO es homonimia: es identidad cita↔presente, como esp. "hablo", alemán "mache=ich mache".
- **Migración de corpus pendiente:** ejemplos con presente de coda dura pelado (`Mi mak…`, `Mi luv…`, `Mi hav…`) → forma de cita (`Mi maka…`, `Mi luva…`, `Mi hava…`). Raíces legales (`si/go/wan/tok`) quedan intactas. Afecta ~200 ejemplos + el generador de ejemplos del diccionario.

**Argumentos clave:** presente no marcado = default translingüístico (inglés/mandarín/criollos) y SVO ya desambigua (semantista); R7 y presente pasan a ser UN sistema en vez de dos reglas (morfólogo); todo presente queda (C)V-legal sin reintroducir codas duras (fonólogo).

---

## R9 — Acuñación de 6 palabras-función + fix de números (ratificada 2026-07-28)

El curso Learning-VELA nivel-1 reveló huecos en vocabulario-función básico. El comité (pi-29881, pi-26905, pi-34067) acuñó 6 palabras tras dos rondas de voto:

| English | VELA | AFI | Voto | Nota |
|---|---|---|---|---|
| here | **hier** | /hi.er/ | unánime | ya atestiguada en corpus ("Mi wok hier", "far from hier") — formalizada |
| there | **dar** | /dar/ | 2-1 | átomo corto para deíctico; "der" rechazado (colisión auditiva con `de`=they); "dat-ples" rechazado por longitud |
| many | **meni** | /me.ni/ | unánime | vocal-final, sin coda dura |
| some | **som** | /som/ | 2-1 | partitivo, función propia no cubierta por un+plural |
| very | **veri** | /ve.ri/ | 2-1 | intensificador moderado; distinto de reduplicación (big-big = extremo/scorching) |
| too/also | **alo** | /a.lo/ | unánime | "olso" rechazado (coda /l/ interna ilegal); "tu" rechazado (homonimia triple con 2/you) |

**Fix de datos en LEXICON_BASE:**
- `tri` estaba glosado como "tired (short)" en la sección de emociones — ERROR. `tired` = `tireda`. `tri` = **three** (número), como ya lo usaban los compuestos `tri-ten`=30, `tri-taim`, `tri-korner`.
- Números **1 (`wan`)** y **3 (`tri`)** faltaban como entrada suelta en la tabla (solo existían dentro de compuestos). Añadidos, más `ten-wan`=11, `ten-tri`=13.
- Homonimia resultante `wan` (1 / to want) es tolerada por R8 (contexto desambigua, cf. inglés two/too/to). El generador la reporta como duplicado esperado.

Validación: 0 errores fonotácticos, 2896 entradas.

---

## R10 — Alomorfía del adjetivo: atributivo pelado / predicativo cita (ratificada unánime 2026-07-28)

Extensión natural de R7 (compuestos) y R8 (verbos) a los ADJETIVOS con coda dura. Votada R10-sí por unanimidad (pi-29881, pi-26905, pi-34067).

**Regla:**
- **Atributivo** (antes del sustantivo, posición prosódica NO-final, ligada como compuesto) → raíz **pelada**: `big famili`, `gud man`, `smol childa`, `old man`.
- **Predicativo** (tras `es`, palabra libre prosódicamente final) → forma de **cita** (raíz+vocal): `Li es biga`, `La man es guda`, `La fater es olda`, `La dei es veri hota`, `Mi es tireda`.
- **Vocal-final o coda blanda {n m l r s ŋ}**: invariable en toda posición (`hapi`, `smol`, `angri`, `yong`, `kol`, `new`).

**Fundamento:** la posición sintáctica determina la saliencia prosódica (fonólogo). Atributivo = no-final, la coda queda protegida por el sustantivo siguiente. Predicativo = final, la coda dura exige la vocal de cita para ser (C)V-legal — el mismo mecanismo de R7/R8. Precedentes: alemán (groß/großer), ruso (forma corta/larga).

**Sustantivos** siguen R7 directamente: forma de cita (= entrada de diccionario) cuando van solos como sujeto/objeto (`Mi si la buka`, `un smol childa`); forma pelada dentro de compuestos (`buk-…`, `child-taim`). Esto garantiza que ninguna palabra de contenido standalone quede con coda dura ilegal.

**Regla única del aprendiz (unifica R7+R8+R10):** *libre → con la vocal de cita; ligado (atributivo, compuesto, o base de pasado/futuro) → pelado.*

Ejemplos migrados del corpus pre-R7: `es sik`→`es sika`, `es afred`→`es afreda`, `La fater es old`→`La fater es olda`.

### R9 addendum — `kolor` (colour) formalizado (2026-07-28)

Voto 2-1: **kolor** /ko.lor/ (morfólogo + semantista) sobre `kala` (fonólogo, temía confusión con `kolar`=collar). Decisivo: `kolor` YA se usaba en decenas de ejemplos del léxico ("Wat kolor es la kar?", "La flaga hav tri kolor", "Sorta la klota bai kolor", "vivida kolor") sin entrada propia — igual que `hier`, solo faltaba formalizarlo (R8: corpus manda). Coda /r/ blanda → sin alternancia cita/composición. Compuestos: `kolor-ful`, `no-kolor`. Añadido a LEXICON_BASE §Nature.

## R11 — `werka` (to work), resolviendo la colisión walk/work (ratificada 2-1, 2026-07-28)

Descubierto al escribir Learning-VELA: `woka` = to WALK (única entrada), pero "to work" no tenía palabra propia — el corpus usaba `wok` para AMBOS (`Mi wok la parke-to`=walk; `De wok la ofis-to`=work) y compuestos `wok-po`/`hom-wok`=worker/homework. Homónimo inaceptable para dos verbos de la misma clase (morfólogo).

Voto 2-1: **werka** /wer.ka/ (morfólogo + fonólogo) sobre `labora` (semantista, más internacional pero 3 sílabas y cercana a woka). El fonólogo refutó el temor de confusión: /e/ vs /o/ se distinguen sin esfuerzo; `werka` (2 sílabas) es eficiente.

Aplicado: `werka` añadido a LEXICON_BASE (`werk-a/werk-ed/werk-wil`). Compuestos de WORK realineados `wok-→werk-`: `werk-po` (worker), `hom-werk` (homework), `werk-moni` (salary), `werk-grup` (union), `werk-fren` (colleague), `werk-end` (retirement), `werk-tebul` (desk). Se mantienen intactos `woka` (walk) y `wok-rod` (sidewalk, walk+road). Learning-VELA L1 corregido (`werka lern-hous-to`, `werk-ed ol la dei`).
