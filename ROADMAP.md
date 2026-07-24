> Cada fase debe estar completa antes de avanzar a la siguiente.
> Documento base: `INITIAL_RESEARCH.md`
> Principios: **Simplicidad → Transparencia → Belleza → Universalidad**

---

## Decisiones de Diseño YA Fijadas

```
FONOLOGÍA:
  ✅ 5 vocales: a, e, i, o, u (sin schwa, sin vocales reducidas)
  ✅ 17 consonantes: p, t, k, b, d, g, m, n, f, v, s, z, sh, h, l, r, w, y
  ❌ PROHIBIDO: th, schwa, zh, clusters difíciles (str-, spr-, thr-)
  ✅ Estructura silábica: (C)V — toda sílaba termina en vocal
  ✅ Pitch accent (penúltima) — melodía, no percusión
  ✅ Clusters permitidos solo al inicio: st-, sp-, tr-, pr-, bl-, cl-, gr-, fl-, fr-, dr-, cr-, sk-, sl-, sm-, sn-, sw-, tw-, pl-, gl-

GRAMÁTICA:
  ✅ Orden SVO
  ✅ Cero verbos irregulares
  ✅ Presente: raíz + -a | Pasado: raíz + -ed | Futuro: raíz + -wil
  ✅ Sin género gramatical — li = he/she/it
  ✅ Un artículo: la (the), un (a/an)
  ✅ Morfología aglutinante — cada morfema = un significado
  ✅ Sistema de casos MÍNIMO:
      Nominativo: orden SVO
      Acusativo: orden SVO
      Genitivo: -se  (posesión, origen)
      Locativo: -to  (ubicación, tiempo) ← CAMBIADO por consenso (era -te)
  ✅ Adjetivo = raíz bare (sin sufijo) — ELIMINADO -im por consenso
  ✅ Posesivos unificados: mi-se, yu-se, li-se, wi-se, de-se (eliminado -f)
  ✅ Plural: -n (tras vocal) / -en (tras consonante) — CONSENSO 2026-07-24
  ✅ Plural + caso: ROOT-PLURAL-CASE (ej: man-en-se) — corregido por consenso 2026-07-24

VOCABULARIO:
  ✅ ~200 palabras atómicas soft ceiling (Tier 0: 50 cerradas, Tier 1: 150 abiertas con Quality Gate)
  ✅ Compuestos transparentes: raíces + afijos = palabras nuevas
  ✅ Profesiones: sufijo -po (gender-neutral) — CONSENSO 2026-05-13
  ✅ Números:
      0-10: atómicos (wan, tu, tri...)
      11-19: ten-N (ten-wan, ten-tu...)
      20-90: N-ten (tu-ten, tri-ten...)
      100: kent (atómico, latín)
      1000: mil (atómico, latín)
  ✅ Sistema de deliberación multi-agente con 5 especialistas (véase README)
```

---

## Resumen de Fases

```
Fase 0  → Investigación                ✅
Fase 1  → Fonología Final              ✅
Fase 2  → Sistema de Escritura         ✅
Fase 3  → Gramática Completa           ✅
Fase 4  → Léxico Base (1004/1000)      ✅ COMPLETA
Fase 5  → Léxico Extendido (3000+)     🔶 EN CURSO (246 palabras, consenso aplicado 2026-07-24)
Fase 6  → Gramática de Referencia      ✅ COMPLETA (18 secciones + FAQ + excepciones, canon reconciliado)
Fase 7  → Diccionario                  ⬜
Fase 8  → Textos y Muestras            ✅ COMPLETA (5 poemas + 1 cuento + 1 cuento clásico + 5 historias + 100 frases + benchmark)
Fase 9  → Audio y Pronunciación        ⬜
Fase 10 → Comunidad y Evolución        ⬜
```

---

## Fase 1 — Fonología Final ✅ COMPLETA

**Entregable:** `docs/phonology/PHONOLOGY_FINAL.md`

- [x] 1.1 Inventario de consonantes — 17 fonemas
- [x] 1.2 Inventario de vocales — 5 vocales, sin schwa
- [x] 1.3 Reglas alofónicas — /t/→[tʲ], /n/→[ŋ], /r/→[ɾ]
- [x] 1.4 Estructura silábica — (C)V confirmado
- [x] 1.5 Pitch accent — penúltima = ALTO
- [x] 1.6 Palabras prohibidas — NO th, zh, schwa
- [x] 1.8 Lista de prueba — 300+ palabras
- [x] 1.9 Ajustes fonológicos — /θ/→/z/, /ð/→/z/, /ʒ/→/jur//jon/
- [x] 1.10 Test pronunciabilidad — /v/ /z/ /r/ documentados

**Último cambio**: Reforma fonotáctica aplicada — palabras que violaban (C)V fueron corregidas (stop→topi, draw→rava, build→maki, etc.). Véase `vote/docs/CHANGE_LOG.md`.

---

## Fase 2 — Sistema de Escritura ✅ COMPLETA

**Entregable:** `docs/writing/ORTHOGRAPHY.md`

- [x] 2.1 Alfabeto confirmado — 24 letras
- [x] 2.2 sh = /ʃ/ — único digrafo
- [x] 2.3 Mayúsculas — solo oración + nombres propios
- [x] 2.4 Puntuación — . , ? ! : ; "..." — raya —
- [x] 2.5 Dirección LTR
- [x] 2.7 Números — sistema decimal reformado
- [x] 2.9 Ortografía morfológica — guiones entre morfemas

**Último cambio**: Eliminado `-im` de adjetivos. Ahora adjetivo = raíz bare. Comparativos: `mor big`, `mos big`.

---

## Fase 3 — Gramática Completa ✅ COMPLETA

**Entregable:** `docs/grammar/GRAMMAR_COMPLETE.md`

### 3.1 Sustantivos
- [x] Plural: `-s`
- [x] Casos: NOM (orden), ACC (orden), GEN (`-se`), LOC (`-to`)
- [x] Artículo: `la` (the), `un` (a/an)

### 3.2 Verbos
- [x] Presente: raíz + `-a`
- [x] Pasado: raíz + `-ed`
- [x] Futuro: raíz + `-wil`
- [x] Modalidad: `kan`, `mas`, `wan`
- [x] Negación: `no` + verbo
- [x] Preguntas: partícula `q`

### 3.3 Pronombres
- [x] Sujetos: `mi, yu, li, wi, de`
- [x] Posesivos: `mi-se, yu-se, li-se, wi-se, de-se`
- [x] Locativos: `mi-to, yu-to, li-to, wi-to, de-to`
- [x] Demostrativos: `dis, dat, dese, dase`
- [x] Indefinidos: `som, eni, non, evri`

### 3.4 Adjetivos
- [x] Terminación: **raíz bare (sin sufijo)** — `-im` ELIMINADO por consenso
- [x] Comparativo: `mor` + adj
- [x] Superlativo: `mos` + adj

### 3.5 Preposiciones
- [x] Core: `a, in, on, from, for, wit, to`

### 3.6 Oraciones
- [x] Orden SVO
- [x] Preguntas sí/no: `q`
- [x] Preguntas WH: `hu, wat, wen, wer, hai, wai, hou`
- [x] Conjunciones: `and, bot, or, so, bikos`
- [x] Condicionales: `if... den...`

### 3.7 Tiempo y calendario
- [x] Días: Mondei, Tiuzdei, Wenzdei, Terzdei, Fraidei, Satrdei, Sandei
- [x] Meses: Januari, Februari, Mart, Apri, Mei, Juni, Juli, Ogust, Septembr, Oktobr, Novembr, Desembr

**Últimos cambios por consenso**:
- Locativo: `-te` → `-to`
- Posesivos unificados: eliminado sistema dual (`-f` y `-se`), ahora solo `-se`
- Orden plural+caso: `man-se-s` (ROOT-CASE-PLURAL)
- Adjetivos sin sufijo: word order distingue atributivo vs predicativo

---

## Fase 4 — Léxico Base (1000 palabras) ✅ COMPLETA

**Entregable:** `docs/lexicon/LEXICON_BASE.md` (~780 palabras documentadas)

### Estado actual

- [x] ~780 palabras documentadas con AFI, inglés, ejemplos
- [x] Validación fonológica: todas terminan en vocal o /n,m,l,r/
- [x] Sistema de afijos productivos documentado
- [x] Profesiones: 23 compuestos con `-po` completos
- [x] Números: sistema decimal completo (0-10 atómicos, 11-99 compuestos, 100=kent, 1000=mil)
- [x] Tier 0 (50 palabras atómicas core, cerradas): completado
- [x] Tier 1 (~150 palabras atómicas frecuentes, soft ceiling con Quality Gate): en progreso
- [ ] Tier 2+ (compuestos): en progreso

### Checklist pendiente

**4.1 Completar top 500 frecuencias**
- [ ] Verificar cobertura de Swadesh list (207 conceptos básicos)
- [ ] Añadir sustantivos abstractos faltantes (time, year, way, day, world, government, problem, fact, education, research, policy, process, market, society, economy, technology, community, quality, organization, analysis, standard, etc.)

**4.2 Tecnología básica**
- [ ] móvil / celular
- [ ] pantalla
- [ ] aplicación / app
- [ ] red / network
- [ ] contraseña
- [ ] email / e-letr
- [ ] wifi

**4.3 Emociones (Tier 1)**
- [ ] happy, sad, angry, afraid, surprised, disgusted, trust, anticipation

**4.4 Colores**
- [ ] Confirmar lista completa: red, blu, gryn, yelo, orange, purpl, pink, brown, gray, blak, wite

**4.5 Cuerpo humano**
- [ ] Verificar si faltan partes menores: finger, toe, nail, muscle, bone, blood vessel

**4.6 Validación final**
- [ ] Script: contar palabras exactas (excluyendo explicaciones)
- [ ] Confirmar: 0 palabras con th, schwa, zh
- [ ] Confirmar: todas terminan en vocal o líquida
- [ ] Confirmar: todos los compuestos son transparentes

**Bloqueado por deliberación futura:**
- Sistema de emociones finas (Fase 5)
- Léxico tecnológico extendido (Fase 5)

---

## Fase 5 — Léxico Extendido (3000+ palabras) ⬜

**Depende de:** Fase 4 completa + benchmark text funcionando

### 5.1 Tecnología y computing
- [ ] Software: program, code, bug, debug, compile, runtime, API, framework
- [ ] Hardware: CPU, memory, storage, display, keyboard, mouse, battery, cable
- [ ] Internet: website, browser, URL, server, client, cloud, upload, download, stream
- [ ] AI: artificial intelligence, machine learning, neural network, model, training, prompt, LLM
- [ ] Data: database, query, table, row, column, backup, encryption

### 5.2 Ciencia
- [ ] Biología: cell, DNA, evolution, species, ecosystem, adaptation
- [ ] Química: element, molecule, reaction, acid, base, organic
- [ ] Física: energy, gravity, quantum, relativity, particle, wave
- [ ] Astronomía: planet, galaxy, orbit, telescope, constellation
- [ ] Medicina: diagnosis, symptom, treatment, immunity, vaccine, virus, bacteria

### 5.3 Artes y cultura
- [ ] Música: instrument, orchestra, melody, rhythm, composer, concert
- [ ] Visual: sculpture, photography, gallery, exhibition, portrait, landscape
- [ ] Literatura: novel, poetry, chapter, verse, metaphor, genre
- [ ] Cine/TV: director, screenplay, scene, genre

### 5.4 Conceptos abstractos
- [ ] Filosofía: existence, consciousness, free will, morality, truth, knowledge
- [ ] Ética: right, wrong, duty, virtue, justice, harm, consent
- [ ] Política: democracy, freedom, equality, rights, citizenship, governance
- [ ] Religión: belief, faith, worship, sacred, prayer, soul, spirit

### 5.5 Emociones (distinciones finas) — REQUIERE DELIBERACIÓN
- [ ] tristeza vs melancolía vs duelo vs frustración
- [ ] alegría vs serenidad vs euforia vs satisfacción
- [ ] miedo vs ansiedad vs preocupación vs pánico
- [ ] amor vs cariño vs pasión vs devoción

**Nota**: Tema perfecto para deliberación de especialistas (semanticist + aestheticist).

### 5.6 Sistema de préstamos
- [ ] Regla: adaptar fonéticamente al sistema VELA
- [ ] Documentar: ¿cuándo aceptar préstamos? ¿cuándo crear compuestos?

### 5.7 Idiomatismos
- [ ] Crear 20 expresiones que no existan en inglés
- [ ] Documentar: proceso creativo con deliberación

---

## Fase 6 — Gramática de Referencia ✅ COMPLETA

**Objetivo:** Consolidar TODA la gramática en un solo documento de referencia (no tutorial).

**Entregable:** `docs/grammar/GRAMMAR_COMPLETE.md` (18 secciones).

- [x] Índice completo con links (TOC, 18 secciones)
- [x] Un paradigma por clase de palabra (sustantivo §4.8, verbo §6.2, bi §6.3...)
- [x] Un ejemplo por regla
- [x] Tablas de referencia rápida (Summary — Grammar at a Glance)
- [x] Lista de excepciones atómicas justificadas (§18 Exceptions & Closed Classes)
- [x] FAQ gramatical (§17)

**Reconciliación de canon (2026-07-24)**: se corrigieron inconsistencias que arrastraba el boceto — plural `-s`→`-n/-en`, orden de morfemas raíz-número-caso, locativo `-te`→`-to`, comparativo `+im`→`+base`, y la regla de compuestos (§15.1: guion entre morfemas, confirmado por comité + ORTHOGRAPHY §6.3). Techo de átomos actualizado a dos niveles (Fase 5 R1).

---

## Fase 7 — Diccionario ⬜

**Objetivo:** Diccionario oficial VELA → IPA → español/inglés.

**Formato planeado:**

| Campo | Descripción |
|-------|-------------|
| VELA | palabra |
| IPA | pronunciación |
| Categoría | sustantivo, verbo, adjetivo, adverbio |
| Definición | español + inglés |
| Etimología | raíz(es) + notas |
| Compuestos | palabras derivadas |
| Ejemplo | frase en VELA + traducción |

**Volumen**: 1000 entradas mínimo, 3000+ meta.

**Herramienta**: Posible script Python para generar desde LEXICON_BASE.md

---

## Fase 8 — Textos y Muestras ✅ COMPLETA

### 8.1 Texto benchmark (PRIMERA TAREA)

> "Go forth in peace to love and serve the Lord."

**Decisiones que este texto obliga a resolver:**
- ¿Cómo se conjuga "serve" en imperativo?
- ¿"forth" = adverbio locativo? ¿o preposición?
- ¿"the Lord" = nombre propio con mayúscula? ¿o común reverenciado?
- ¿"in peace" = locativo `-to` o preposición `in`?
- ¿"to love" = infinitivo o propósito?

### 8.2 Frases cotidianas (100 frases)
- [x] Saludos, despedidas, cortesías
- [x] Compras, restaurante, transporte
- [x] Emergencias, salud, ayuda
- [x] Trabajo, reunión, presentación

### 8.3 Textos fundacionales
- [x] 5 poemas originales en VELA
- [x] 1 cuento corto (500-1000 palabras)
- [x] Traducción de cuento infantil clásico: "Tri Smol Pigi" (Los Tres Cerditos) — 2 gap words identificados (blo, chimni)

### 8.4 Documentación de decisiones
- [x] Para cada texto: por qué se tradujo así — documentado en BENCHMARK.md
- [x] Trade-offs encontrados — documentados en deliberaciones del comité
- [x] Decisiones gramaticales tomadas en contexto real — en progreso (pendiente integrar a GRAMMAR_COMPLETE.md)

---

## Fase 9 — Audio y Pronunciación Estándar ⬜

**Depende de:** Fase 8 (necesitas textos antes de audio)

- [ ] Grabar: 17 consonantes + 5 vocales
- [ ] Grabar: 100 palabras de ejemplo
- [ ] Grabar: pitch accent en acción
- [ ] Grabar: 20 frases de ejemplo
- [ ] Transcripción IPA para cada grabación
- [ ] Documentar "carácter" fonético de VELA

---

## Fase 10 — Comunidad y Evolución ⬜

**Futuro lejano.** Necesitas hablantes antes de comunidad.

- [ ] Sitio web / landing page
- [ ] Foro / Discord
- [ ] VELA Wikipedia (VELA describiendo VELA)
- [ ] Primer traductor voluntario
- [ ] Literatura original
- [ ] Translation challenges
- [ ] ¿Cómo evoluciona VELA? ¿Comité o democrático?

---

## Sistema de Deliberación — Estado Actual

El sistema de consenso multi-agente está **operativo y probado**.

| Componente | Estado |
|------------|--------|
| 5 agentes especialistas | ✅ Funcionando |
| Orchestrator | ✅ Funcionando |
| Graphify (fase 0) | ✅ Integrado |
| Vote infrastructure | ✅ Completo |
| CHANGE_LOG.md | ✅ Acumulativo, fechado |

**Últimas deliberaciones completadas**:
1. Caso sistema reforma (locativo -te → -to)
2. Lexicon Quality Audit (15 cambios aprobados)
3. Standby Issues (4 issues resueltos)
4. Number Override (kent + mil)
5. Profession Suffix (-po elegido)

**Archivos de consenso**:
- `vote/topics/consensus/consensus.md`
- `vote/topics/consensus/NUMBER_OVERRIDE.md`
- `vote/topics/consensus/PROFESSION_SUFFIX.md`
- `vote/SUMMARY.md`

---

## Checklist Maestro — Progreso Total

```
Fase 0  → Investigación                ✅
Fase 1  → Fonología                    ✅
Fase 2  → Sistema de Escritura         ✅
Fase 3  → Gramática Completa           ✅
Fase 4  → Léxico Base (1004/1000)      ✅ COMPLETA
Fase 5  → Léxico Extendido (3000+)     🔶 EN CURSO (246 palabras, consenso aplicado 2026-07-24)
Fase 6  → Gramática de Referencia      ✅ COMPLETA (18 secciones + FAQ + excepciones, canon reconciliado)
Fase 7  → Diccionario                  ⬜
Fase 8  → Textos y Muestras            ✅ COMPLETA (5 poemas + 1 cuento + 1 cuento clásico + 5 historias + 100 frases + benchmark)
Fase 9  → Audio y Pronunciación        ⬜
Fase 10 → Comunidad y Evolución        ⬜
```

---

## Decisiones Pendientes de Deliberación Futura

| # | Tema | Fase afectada | Prioridad |
|---|------|---------------|-----------|
| 1 | Sistema de emociones finas | Fase 5 | Media |
| 2 | Léxico tecnológico extendido | Fase 5 | Alta |
| 3 | Imperativo verbal | Fase 8 (textos) | Alta |
| 4 | Reglas de mayúsculas en títulos/nombres | Fase 2 | Media |
| 5 | Texto benchmark — traducción y análisis | Fase 8 | 🎯 CRÍTICA |
| 6 | Validación fonológica automatizada | Fase 4 | Media |
| 7 | Exportar léxico a JSON/diccionario | Fase 7 | Baja |

---

*Última actualización: 2026-05-14*
*Sistema de deliberación: operativo*
