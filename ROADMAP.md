# VELA — ROADMAP

> Documento base: `INITIAL_RESEARCH.md`
> Principios: **Simplicidad → Transparencia → Belleza → Universalidad**
> Canon vigente: `docs/grammar/GRAMMAR_COMPLETE.md` + `vote/topics/consensus/fase5_consensus.md` (reglas R1–R18)

**Última actualización: 2026-10-22** — R18 ratificada y aplicada; validador en 0 errores.

---

## Estado en una tabla

```
Fase 0  → Investigación                    ✅
Fase 1  → Fonología Final                  ✅  (20 consonantes, no 17 — /tʃ/ /dʒ/ admitidas 2026-07-25)
Fase 2  → Sistema de Escritura             ✅
Fase 3  → Gramática Completa               ✅
Fase 4  → Léxico Base                      ✅  1005 formas
Fase 5  → Léxico Extendido (3000+)         ✅  2908 formas en léxicos · meta cruzada 2026-07-26
Fase 6  → Gramática de Referencia          ✅  GRAMMAR_COMPLETE.md, 18 secciones
Fase 7  → Diccionario                      ✅  2918 entradas + PDF bidireccional
Fase 8  → Textos y Muestras                ✅  benchmark + 5 poemas + 3 cuentos + 5 historias + 100 frases
Fase 9  → Audio y Pronunciación            🔶  pipeline TTS construido · 4 audios · libros SIN audio
Fase 10 → Comunidad y Evolución            🔶  landing GitHub Pages ✅ · comunidad ⬜
Fase 11 → Cursos y Pedagogía               ✅  5 cursos × 12 lecciones (60 lecciones)
```

Las fases ya no son estrictamente secuenciales: el trabajo de julio 2026 avanzó léxico, gramática y pedagogía en paralelo, y el canon se corrige hacia atrás vía reglas ratificadas (R1–R17).

---

## Decisiones de Diseño Vigentes

Esta sección **reemplaza** cualquier versión anterior. Donde una regla R la modifica, se indica.

```
FONOLOGÍA:
  ✅ 5 vocales: a, e, i, o, u (sin schwa, sin vocales reducidas)
  ✅ 20 consonantes  ← 17 originales + /tʃ/ (ch) y /dʒ/ (j), admitidas por comité 2026-07-25
     p t k b d g m n f v s z sh h l r w y ch j
  ❌ PROHIBIDO sin excepción: th (/θ/ /ð/), zh (/ʒ/), schwa
  ✅ Estructura silábica: (C)V — sílaba abierta
  ✅ Codas toleradas a final de palabra: {n, m, l, r, s}   ← +s respecto a la versión vieja
  ✅ Pitch accent (penúltima) — melodía, no percusión
  ✅ Clusters SOLO en onset, nunca en coda
  ❌ Clusters finales prohibidos (R2): -tm -mnt -sm -shn -bl -ks -st -rd -rs -tr -ns
     -nt -nd -kl -dl -lt -lf -nr -dr -kt -sk -pt -nkr

MORFOLOGÍA — la regla visual única (R17):
  ✅ GUION  → forma pelada     (compuestos: mak-tin, red-hous, big-fish)
  ✅ ESPACIO → forma de cita   (frases: un reda bol, La bol es reda)
  ✅ Alomorfía cita/composición (R7): raíz con coda dura tiene dos formas
     cita = raíz + -a  (maka, luka, aska, teacha)  → standalone y entrada de diccionario
     comp = raíz pelada (mak-, luk-, ask-)         → dentro de compuestos
     Palabras-función (at, of, and, if, wit, but, self) grandfathered: forma única.

GRAMÁTICA:
  ✅ Orden SVO · cero verbos irregulares (única excepción: bi → presente es)
  ✅ Presente = LA FORMA DE CITA, sin marca gramatical (R8)  ← ya NO es "raíz + -a"
     si, go, wan, tok, liv, lern  |  maka, hava, luva
  ✅ Pasado: raíz pelada + -ed   (si-ed, mak-ed → /ha.ved/)
  ✅ Futuro: raíz pelada + -wil
  ✅ Adjetivo INVARIABLE, siempre forma de cita (R17, deroga R10)
     un reda bol  ·  La bol es reda
  ✅ Comparativo: mor + adj · Superlativo: mos + adj
  ✅ Plural: -n (tras vocal) / -en (tras consonante)   ← el "-s" está DEROGADO (R6)
  ✅ Orden de morfemas: RAÍZ → NÚMERO → CASO  (man-en-se = "de los hombres") (R6)
  ✅ Casos: NOM y ACC por orden · Genitivo -se · Locativo -to
  ✅ Sin género gramatical — li = he/she/it (pronombre único)
  ✅ Artículos: la (the), un (a/an)
  ✅ Relativas (R12): palabra-pregunta tras el núcleo — hu / wat / wer / wen
     dat NO es relativizador (colisión con el demostrativo); es complementante tras
     verbos de mente: Mi tinka dat li es guda.
  ❌ SIN VOZ PASIVA (R12). Impersonal = sujeto genérico man-en + activa.

VOCABULARIO:
  ✅ Techo de átomos de DOS NIVELES (R1) — el techo único de ~200 era retroactivamente imposible
     Core: target blando ~200 átomos (no es conjunto cerrado)
     Registros de dominio (tech, ciencia, arte, abstracto): clase ABIERTA
     Todo préstamo de dominio debe llevar un compuesto transparente alternativo de ≤3 raíces
  ✅ Compuestos transparentes primero (R3): donde el préstamo también rompe fonotáctica,
     se reemplaza; si no, el compuesto es la forma preferida y el préstamo queda sinónimo de registro
  ✅ Profesiones: sufijo -po (gender-neutral)
  ✅ 'person' = person / pipol — man ya NO significa "persona" (R14)
  ✅ Vocal temática /a/ (R2): raíz o préstamo con coda ilegal recibe -a  (kod → koda, bug → buga)
  ✅ Números: 0-10 atómicos · 11-19 ten-N · 20-90 N-ten · 100 kent · 1000 mil
  ✅ Tags léxicos POETIC / PROSE (R4) para que la poesía evite préstamos de prosa
```

---

## Registro de Reglas Ratificadas (R1–R18)

Fuente única: `vote/topics/consensus/fase5_consensus.md`. Una regla ratificada es canon y gana sobre cualquier documento más viejo.

| # | Regla | Fecha | Voto |
|---|-------|-------|------|
| R1 | Techo de átomos de dos niveles (core ~200 + dominios abiertos) | 2026-07-24 | aprobada, enmendada |
| R2 | Fonotáctica: vocal temática /a/ + prohibición de clusters finales | 2026-07-24 | unánime |
| R3 | Sobrecarga de préstamos: compuesto primero | 2026-07-24 | aprobada, enmendada |
| R4 | Emociones: se conserva la arquitectura de compuestos + tags POETIC/PROSE | 2026-07-24 | unánime |
| R5 | Correcciones puntuales de belleza y ortografía (-shon estandarizado) | 2026-07-24 | unánime |
| R6 | Bug de canon del plural: -n/-en único · orden raíz-número-caso | 2026-07-24 | unánime |
| R7 | Alomorfía cita/composición (Opción D) — 273 raíces normalizadas | 2026-07-26 | unánime |
| R8 | **El presente = la forma de cita** (no lleva marca propia) | 2026-07-26 | unánime (ronda 2) |
| R9 | 6 palabras-función acuñadas (hier, dar, meni, som, veri, alo) + fix de números · addendum `kolor` | 2026-07-28 | 2 rondas |
| R10 | ~~Alomorfía del adjetivo (atributivo pelado / predicativo cita)~~ | 2026-07-28 | **DEROGADA por R17** |
| R11 | `werka` (to work) resuelve la colisión walk/work | 2026-07-28 | 2-1 |
| R12 | Cláusulas relativas (hu/wat/wer/wen) + **política de no-pasiva** | 2026-07-28 | unánime |
| R13 | Batch de vocabulario B2 + política de estilo indirecto | 2026-07-28 | aprobada |
| R14 | Neutralidad de género: person/pipol reemplazan man="persona" | 2026-07-28 | aprobada |
| R15 | Embellecimiento fonoestético (pipol, nera, jir, louda, tun, pisi) | 2026-07-28 | auditoría del fonólogo |
| R16 | Sistema de pronombres indefinidos (eni/otra/evri) + palabras C1 | 2026-07-28 | aprobada |
| R17 | **Adjetivos invariables** — una sola regla visual: guion=pelado, espacio=cita | 2026-07-29 | unánime |
| R18 | Las 13 palabras sin acuñar del corpus (`yeta`, `abau`, `auta`, `stika` + 9 existentes/compuestos) · `aut-` única ortografía de /au/ | 2026-10-22 | 5 especialistas; 2 desempates del esteticista, 2 decisiones del usuario |

---

## Fase 1 — Fonología Final ✅

**Entregable:** `docs/phonology/PHONOLOGY_FINAL.md`

- [x] Inventario de consonantes — **20 fonemas** (§1)
- [x] Inventario de vocales — 5, sin schwa
- [x] Reglas alofónicas — /t/→[tʲ], /n/→[ŋ], /r/→[ɾ]
- [x] Estructura silábica (C)V + codas toleradas {n,m,l,r,s}
- [x] Pitch accent penúltima
- [x] /θ/ /ð/ /ʒ/ excluidos, sin grandfathering
- [x] Validador automatizado: `scripts/validate_phonology.py` — **2908 palabras, 0 errores**

**Cambio de inventario (2026-07-25):** se admitieron /tʃ/ y /dʒ/ como fonemas #19-20. ~74 palabras ya las usaban (`chipa`, `teacha`, `chuz`, `oranja`, `imaj`) y mapearlas fuera creaba colisiones fatales (chip→ship, jen→zen). Voto unánime: el inventario estaba subespecificado.

---

## Fase 2 — Sistema de Escritura ✅

**Entregable:** `docs/writing/ORTHOGRAPHY.md`

- [x] Alfabeto latino, LTR
- [x] `sh` = /ʃ/ · `ch` = /tʃ/ · `j` = /dʒ/
- [x] Mayúsculas: oración + nombres propios
- [x] Puntuación: `. , ? ! : ; "…" —`
- [x] Guion entre morfemas de un compuesto (§6.3, confirmado por comité)
- [x] Sufijo `-shon` estandarizado (R5)

---

## Fase 3 — Gramática Completa ✅

**Entregable:** `docs/grammar/GRAMMAR_COMPLETE.md`

- [x] Sustantivos: plural `-n/-en`, orden raíz-número-caso, casos NOM/ACC/GEN(`-se`)/LOC(`-to`), artículos `la`/`un`
- [x] Verbos: presente = cita (R8), pasado `-ed`, futuro `-wil`, modales `kan/mas/wan`, negación `no`, pregunta `q`
- [x] Pronombres: `mi yu li wi de` + genitivos `-se` + locativos `-to` + demostrativos `dis/dat/dese/dase` + indefinidos (R16)
- [x] Adjetivos: invariables, forma de cita (R17); `mor`/`mos`
- [x] Preposiciones core: `a in on from for wit to`
- [x] Oraciones: SVO, WH (`hu wat wen wer hai wai hou`), conjunciones, condicionales `if… den…`
- [x] Relativas y no-pasiva (R12)
- [x] Días y meses (codas de cluster corregidas en R15)

---

## Fase 4 — Léxico Base ✅

**Entregable:** `docs/lexicon/LEXICON_BASE.md` — **1005 formas** validadas.

- [x] AFI, inglés y ejemplos por entrada
- [x] Validación fonológica automatizada (0 errores)
- [x] Sistema de afijos productivos
- [x] Profesiones con `-po`
- [x] Números completos
- [x] Limpieza de duplicados y homónimos (pre-expansión, 2026-07-25)
- [x] Normalización de duplicados de ortografía base: 111 conceptos, −120 entradas redundantes

---

## Fase 5 — Léxico Extendido ✅

**Entregables:** `docs/lexicon/LEXICON_EXTENDED.md` (241) + `docs/lexicon/LEXICON_EXPANSION.md` (1662).

La meta de 3000 se cruzó el 2026-07-26 (`chore(lexicon): add final batch — crosses 3000`). El total actual de formas en los tres léxicos es **2908** tras las deduplicaciones y normalizaciones posteriores; el diccionario generado tiene **2918 entradas**.

- [x] Tecnología y computing · ciencia · artes y cultura · conceptos abstractos
- [x] Emociones: arquitectura de 18 compuestos transparentes conservada (R4)
- [x] Sistema de préstamos documentado (R3: compuesto primero)
- [x] Reforma fonotáctica aplicada (R2): vocal temática + clusters finales restructurados
- [x] Alomorfía cita/composición aplicada a 273 raíces (R7)
- [ ] **Idiomatismos: 20 expresiones propias de VELA** ← único pendiente real de esta fase

---

## Fase 6 — Gramática de Referencia ✅

**Entregable:** `docs/grammar/GRAMMAR_COMPLETE.md` — 18 secciones, TOC, un paradigma por clase, FAQ (§17), excepciones y clases cerradas (§18), tabla "Grammar at a Glance" (§ final).

Reconciliado con el canon a 2026-07-29: R8 (presente=cita), R14 (person/pipol), R16 (§3.7 indefinidos), R12 (§11.4 relativas), R17 (§5.1 adjetivo invariable).

---

## Fase 7 — Diccionario ✅

**Entregables:**

| Archivo | Contenido |
|---------|-----------|
| `docs/dictionary/DICTIONARY.md` | 2918 entradas — VELA \| IPA \| categoría \| definición \| etimología \| compuestos \| ejemplo |
| `docs/dictionary/INDEX_EN_VELA.md` | índice inverso inglés → VELA |
| `books/VELA-Dictionary.pdf` | PDF imprimible a 2 columnas, bidireccional |
| `books/VELA-Dictionary.typ` | fuente Typst |

Generado por `scripts/generate_dictionary.py` desde los léxicos (0 palabras nuevas). El generador es header-aware (~13 layouts de tabla), deriva etimología y compuestos, y actúa como auditoría. Re-ejecutable: se regenera cuando cambian los léxicos.

---

## Fase 8 — Textos y Muestras ✅

- [x] Texto benchmark analizado — `docs/texts/BENCHMARK.md`
- [x] 100 frases cotidianas — `docs/texts/PHRASES_100.md`
- [x] 5 poemas — `POEMS_COLLECTION.md` + `POEM_01_SUN_AND_MOON.md`
- [x] 2 cuentos originales — `SHORT_STORY_BIRD.md`, `STORIES_SET_01.md` (5 historias)
- [x] 1 cuento clásico traducido — "Tri Smol Pigi" (`SHORT_STORY_THREE_PIGS.md` + `CLASSIC_STORY_THREE_PIGS.md`)
- [x] Decisiones de traducción documentadas en `BENCHMARK.md`

⚠️ **El corpus no está migrado a R8/R17.** Véase *Deudas conocidas*.

---

## Fase 9 — Audio y Pronunciación 🔶 EN CURSO

**El motor ya está construido.** `packages/vela-tts-piper/` es un paquete funcional:

| Pieza | Archivo |
|-------|---------|
| Wrapper de Piper | `src/piper.js` |
| Pipeline VELA (normalize → G2P → prosodia) | `src/vela/*.js` |
| Diccionario de pronunciación | `data/vela-dictionary.json` |
| CLI | `bin/vela-tts.mjs` |
| Doctor / diagnóstico | `scripts/doctor.mjs` |
| Batch de biblioteca | `scripts/synthesize-library.mjs` |
| Sync a web | `scripts/sync-web-audio.mjs` |
| Síntesis de fonemas | `scripts/synthesize-phonemes.py` |

Comandos: `npm run tts:setup` · `tts:doctor` · `tts:vela:smoke` · `tts:vela:batch` · `tts:vela:batch-and-sync`.

**Hecho:**
- [x] Pipeline TTS local con Piper, sin servicio externo
- [x] G2P + prosodia (pitch accent penúltima)
- [x] 4 audios generados: 2 poemas + 2 cuentos → `web-sample/public/audio/`
- [x] Índice de biblioteca con audio en `web-sample/public/content/index.json`

**Pendiente:**
- [ ] Audio de los 25 fonemas (20 consonantes + 5 vocales; `synthesize-phonemes.py` existe, sin ejecutar en la biblioteca)
- [ ] Audio de las ~60 lecciones de los cursos
- [ ] **Botones de reproducción en los 5 libros** — hoy los cursos tienen 0 audio (`rg -l audio books/` → sin resultados)
- [ ] Audio de las 100 frases y del pitch accent en contraste
- [ ] Transcripción IPA emparejada con cada grabación
- [ ] Documentar el "carácter" fonético de VELA

**Bloqueador de calidad:** los textos de `web-sample/public/texts/` son pre-R8/R17. Sintetizar más audio antes de migrar el corpus produce audio que enseña canon derogado.

---

## Fase 10 — Comunidad y Evolución 🔶

- [x] Landing page en GitHub Pages — `index.html` (cursos, diccionario, referencia, repo)
- [x] Sitio de muestra con audio — `web-sample/` (React)
- [x] Proceso de evolución definido: comité de 5 especialistas + reglas R ratificadas y fechadas
- [ ] Foro / Discord
- [ ] VELA Wikipedia (VELA describiendo VELA)
- [ ] Primer traductor voluntario
- [ ] Literatura original más allá del corpus fundacional
- [ ] Translation challenges

---

## Fase 11 — Cursos y Pedagogía ✅

No existía en el roadmap original; es trabajo real completado entre el 2026-07-26 y el 2026-07-29.

| Curso | Lecciones | Contenido |
|-------|-----------|-----------|
| `books/Learning-VELA-Level1.html` | 12 | Del primer "Helo!" a conversación básica |
| `books/Learning-VELA-Level2.html` | 12 | Aspecto, modales, comparación, unir ideas, formación de palabras |
| `books/Learning-VELA-Level3.html` | 12 | Relativas (R12), condicionales, causativos, poemas y folktales |
| `books/Learning-VELA-Level4.html` | 12 | Estilo indirecto (R13), modalidad fina, contraste, lenguaje figurado |
| `books/Learning-VELA-Level5.html` | 12 | Word-craft, indefinidos (R16), registro, metáfora, traducción, ensayo |

**60 lecciones en total.** Los 5 tienen menú de navegación nativo (popover), paleta propia y están enlazados desde la landing y el README.

**Libro de referencia:** `books/VELA-The-Universal-Conlang.{md,html,pdf}` — manifiesto + filosofía + sonidos + gramática.

Los 5 cursos fueron propagados con R14, R15, R16 y R17.

---

## Validación del corpus — cerrada 2026-08-07

`scripts/validate_phonology.py` ahora cubre **léxicos + corpus**: los 3 léxicos (2908 headwords) más `docs/texts/*.md` y los 5 cursos HTML (4704 tokens VELA). Antes solo miraba los léxicos, así que el corpus nunca se había validado.

Cómo lee prosa bilingüe sin confundir idiomas:

| Fuente | Cómo se delimita el VELA |
|--------|--------------------------|
| Léxicos | filas de tabla `\| **word** \| /afi/ \|` |
| `docs/texts/*.md` | bloques `**VELA:**`, secciones `## …VELA…`, bloques cercados, columna `VELA` de tablas |
| `books/*.html` | `<span class="vela">…</span>` (770 spans) |

Reglas de canon que el validador aplica y antes no:

- **Resilabificación (R7/R8).** Con sufijo o dentro de compuesto la coda pasa al onset siguiente: `hav-ed` = /ha.ved/ es legal, y `dans-ed` = /dan.sed/ también. Sin esto cada pasado era un falso positivo.
- **Alomorfía cita/composición (R7).** La forma pelada `luv` se deriva del headword `luva`, así que no se reporta como off-canon.
- **Diacríticos de pitch accent.** `fórti`, `Lòrd` se normalizan antes de analizar.
- **Filtro de idioma** en párrafos sueltos dentro de regiones VELA, que es el único sitio donde el inglés se filtra. Se reportan los párrafos descartados: hoy 2.

Comandos: `--lexicons` · `--corpus` · sin flags escanea todo.

### Resultado de la migración

`scripts/migrate_corpus.py` aplicó **118 correcciones en 6 archivos** de `docs/texts/`. Reescribe solo dentro de regiones VELA (reusa el mismo walker que el validador), así que ninguna traducción al inglés se tocó — verificado: 0 líneas cambiadas fuera de región VELA, y en las tablas la celda inglesa quedó idéntica byte a byte.

| | Antes | Después |
|---|-------|---------|
| Errores en corpus | 90 | **17** |
| Errores en los 5 cursos | 0 | **0** |
| Violaciones de `th` | 5 | **1** |

Los cursos ya estaban limpios: se escribieron en julio, después de la reforma. El daño estaba concentrado en el corpus de Fase 8 (mayo 2026), escrito antes de R2/R7/R15.

Arreglados con formas que ya existían en el léxico: `throt`→`trota`, `erth`→`erda`, `path`→`wei`, `third`→`terda`, `nid`→`needa`, `laik`→`liki`, `musik`→`muzika`, `hart`→`herta`, `voys`→`vois`, `dans`→`dansi` y 49 más. Los sufijos se re-derivan al cambiar la raíz (`leaf-en`→`folia-n` por R6, `break-ed`→`brak-ed` por R8).

---

## Deudas conocidas (verificadas 2026-08-07)

| # | Deuda | Evidencia | Impacto |
|---|-------|-----------|---------|
| 1 | ✅ **RESUELTA 2026-10-22 (R18)** — validador en 0 errores. Era: **13 palabras sin forma canónica** — bloqueaban los 17 errores restantes. Acuñarlas es decisión de comité (`vote/docs/PROCESS.md`), no de un script: `breath`, `much`, `life`, `still`, `about`, `lost`, `ahead`, `breakfast`, `solitude`, `behind`, `just` (sentido "meramente"), `out`, `stick` | `validate_phonology.py --corpus` | Alto: incluye la última violación de `th` (`breth-ed`) |
| 2 | **Corpus sin migrar a R8** — presente con coda dura sigue pelado (`Mi hav`, `Mi luv` en vez de `Mi hava`, `Mi luva`); R8 estimó ~200 ejemplos | `docs/texts/PHRASES_100.md` líneas 83, 99, 101, 141, 157 | Alto: los textos enseñan canon derogado |
| 3 | **Los poemas necesitan pasada del esteticista** — la migración cambió sílabas (`nait`→`noita`, `hart`→`herta`), así que métrica y rima de `POEMS_COLLECTION.md` y `POEM_01_SUN_AND_MOON.md` quedaron sin revisar | diff de 2026-08-07 | Medio: es criterio de belleza, competencia del esteticista (precedente R4/R15) |
| 4 | ✅ **RESUELTA en `bc9d87b`** — Era: **La landing anunciaba "the passive" en Level 4** — R12 ratificó que VELA no tiene pasiva, y el libro correctamente no la enseña | `index.html`, tarjeta de Level 4 | Medio: contradice el canon en la cara pública |
| 5 | **Los textos de `web-sample` son pre-R8/R17** y ya tienen audio generado | `web-sample/public/texts/` | Medio: bloquea ampliar Fase 9 con calidad |
| 6 | **160 gap words** — palabras usadas en textos y cursos que no están en el léxico, todas legales fonotácticamente (`hau`, `morne`, `tanke`, `ten`, `an`…) | `validate_phonology.py --corpus`, sección NOTES | Medio: el diccionario no cubre lo que los cursos enseñan |
| 7 | 85 headwords duplicados detectados por el generador de diccionario | salida de `scripts/generate_dictionary.py` | Bajo: limpieza de léxico |
| 8 | Idiomatismos de Fase 5 (20 expresiones propias) sin empezar | — | Bajo: no bloquea nada |

---

## Próximos pasos recomendados

1. ~~Comité para las 13 palabras faltantes (deuda #1)~~ — hecho (R18, 2026-10-22). **Nuevo:** `docs/texts/STORIES_SET_01.md` no lo lee el validador (0 tokens escaneados) y tiene formas pre-reforma (`kloth`, `path`, `hart`, `leaf`). Arreglar el lector antes de dar el corpus por limpio.
2. **Migración R8 del corpus (deuda #2)** — mecánica y guionizable con el mismo `migrate_corpus.py`: presente de coda dura pelado → forma de cita. Debe pasar antes de generar más audio.
3. **Pasada del esteticista sobre los poemas (deuda #3)** — la migración priorizó canon sobre métrica; alguien tiene que recuperar el ritmo.
4. **Terminar Fase 9** — fonemas + audio de lecciones + botones ▶ en los 5 cursos. VELA tiene pitch accent; un curso que no se puede oír enseña la mitad de la lengua.
5. ~~Deuda #4~~ — hecho en `bc9d87b`.

Poner `python3 scripts/validate_phonology.py` en CI ahora tiene sentido: falla solo con ERRORs, así que las 160 gap words y los warnings de legado no bloquean.

---

## Sistema de Deliberación — Estado

Operativo y probado. 17 reglas ratificadas hasta ahora.

| Componente | Estado |
|------------|--------|
| 5 agentes especialistas (morfólogo, fonólogo, semantista, lexicógrafo, esteticista) | ✅ |
| Orchestrator | ✅ |
| Graphify (fase 0) | ✅ integrado |
| Infraestructura de voto | ✅ |
| `vote/docs/CHANGE_LOG.md` | ✅ acumulativo y fechado |

**Archivos de consenso principales:**
- `vote/topics/consensus/fase5_consensus.md` — **R1–R17, fuente única del canon vigente**
- `vote/topics/consensus/DECISIONS_MASTER.md`
- `vote/topics/consensus/consensus.md`, `NUMBER_OVERRIDE.md`, `PROFESSION_SUFFIX.md`, `PLURAL_SYSTEM_consensus.md`, `ATOM_CEILING_consensus.md`
- `vote/topics/consensus/fri-chuz_consensus.md`, `self-nof_consensus.md`
- `vote/SUMMARY.md`

---

*Regla de oro: si este documento y `fase5_consensus.md` se contradicen, gana la regla R ratificada — y este documento tiene un bug que hay que arreglar.*
