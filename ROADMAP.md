# 🗺️ VELA — Roadmap Completo

> Cada fase debe estar completa antes de avanzar a la siguiente.  
> Documento base: `INITIAL_RESEARCH.md`  
> Principios: **Simplicidad → Transparencia → Belleza → Universalidad**

---

## Decisiones de Diseño YA Fijadas ⚙️

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
      Locativo: -te  (ubicación, tiempo)

VOCABULARIO:
  ✅ Basado en inglés, regularizado fonéticamente
  ✅ Compuestos transparentes: raíces + afijos = palabras nuevas
  ✅ Categorías por terminación: -a (verbo), -i (sustantivo), -im (adjetivo), -um (adverbio)
```

---

## Resumen de Fases

```
Fase 0  → Investigación ✅
Fase 1  → Fonología Final       ← ACTUAL
Fase 2  → Sistema de Escritura
Fase 3  → Gramática Completa
Fase 4  → Léxico Base (1000 palabras)
Fase 5  → Léxico Extendido (3000+ palabras)
Fase 6  → Gramática de Referencia
Fase 7  → Diccionario
Fase 8  → Textos y Muestras
Fase 9  → Audio y Pronunciación Estándar
Fase 10 → Comunidad y Evolución
```

---

## Fase 1 — Fonología Final ✅ COMPLETA

**Objetivo:** Documentar cada sonido, regla y patrón de VELA. Generar 300+ palabras de prueba. Que suene bien.

### 📋 Checklist

- [x] **1.1 Inventario de consonantes** — 18 fonemas: p, t, k, b, d, g, m, n, f, v, s, z, sh, h, l, r, w, y
- [x] **1.2 Inventario de vocales** — 5 vocales: a, e, i, o, u
- [x] **1.3 Reglas alofónicas** — /t/→[tʲ] ante /i/, /n/→[ŋ] ante /k/, /r/→[ɾ] entre vocales
- [x] **1.4 Estructura silábica** — Confirmar (C)V. Solo /n/m/l/r/ al final. Clusters: st-, tr-, pr- etc.
- [x] **1.5 Pitch accent** — Penúltima sílaba = tono ALTO. Melodía, no percusión.
- [x] **1.6 Tono vs. acento** — Confirmado: NO hay tonos léxicos, solo pitch accent
- [x] **1.7 Palabras prohibidas** — NO th, zh, schwa, clusters inválidos
- [x] **1.8 Lista de prueba** — 300+ palabras generadas y verificadas
- [x] **1.9 Ajuste fonológico** — /θ/→/z/, /ð/→/z/, /ʒ/→/jur//jon/
- [x] **1.10 Test de pronunciabilidad** — /v/ /z/ /r/ requieren práctica (documentado)

**Entregable:** ✅ `docs/phonology/PHONOLOGY_FINAL.md`

---

## Fase 2 — Sistema de Escritura ✅ COMPLETA

**Objetivo:** Crear la versión escrita de VELA. Alfabeto latino adaptado.

### 📋 Checklist

- [x] **2.1 Alfabeto confirmado** — 24 letras. Sin c, q, x, ç, ñ, ü. Una letra = un sonido siempre.
- [x] **2.2 sh = /ʃ/ confirmado** — Solo un digrafo: sh. No hay ch, zh, th, ph.
- [x] **2.3 Mayúsculas** — Solo primera letra de oración + nombres propios
- [x] **2.4 Puntuación** — . , ? ! : ; "..." + guiones (-) y raya (—)
- [x] **2.5 Dirección** — LTR confirmada (izquierda a derecha)
- [x] **2.6 Espacio entre palabras** — Confirmado: siempre hay espacio
- [x] **2.7 Números** — Dígitos arábigos (1-9) + palabras: wan, tu, tri... + sistema decimal
- [x] **2.8 Versión manuscrita** — Guía de cursiva VELA con letras conectadas
- [x] **2.9 Ortografía morfológica** — Confirmado: guiones entre morfemas (liv-ed, man-se, mor-im)
- [x] **2.10 Práctica de escritura** — 50+ palabras para práctica, guía de cursive

**Entregable:** ✅ `docs/writing/ORTHOGRAPHY.md`

---

## Fase 3 — Gramática Completa

**Objetivo:** Documentar toda la gramática de VELA con ejemplos.

### 📋 Checklist

**3.1 Sustantivos**
- [ ] Plural: -s confirmado
- [ ] Casos: NOM (orden), ACC (orden), GEN (-se), LOC (-te)
- [ ] Artículo: la (the), un (a/an)
- [ ] Sustantivos常用: terminación -i

**3.2 Verbos**
- [ ] Presente: raíz + -a
- [ ] Pasado: raíz + -ed
- [ ] Futuro: raíz + -wil
- [ ] Aspecto: ¿perfectivo (-ed) es suficiente o se necesita progresivo (-an)?
- [ ] Modalidad: kan (poder), mas (deber), wan (querer)
- [ ] Negación: no + verbo
- [ ] Preguntas: ¿partícula q? ¿inversión?

**3.3 Pronombres**
- [ ] Sujetos: mi, yu, li, wi, de
- [ ] Posesivos: mif, yuf, liz, wef, def
- [ ] Genitivos: mi-se, yu-se, li-se, wi-se, de-se
- [ ] Locativos: mi-te, yu-te, li-te, wi-te, de-te
- [ ] Demostrativos: dis, dat, dese, dase
- [ ] Indefinidos: som, eni, non, evri

**3.4 Adjetivos**
- [ ] Terminación: -im
- [ ] Comparativo: mor + adj-im / mos + adj-im
- [ ] Superlativo: mos + adj-im

**3.5 Preposiciones**
- [ ] Core: a (en/hacia), in (dentro), on (sobre), from (desde), for (para), wit (con), to (a)
- [ ] wit (with): confirmar que no choca con sh
- [ ] en (in): confirmar que no choca con -en locativo

**3.6 Oraciones**
- [ ] Orden SVO: confirmado
- [ ] Preguntas sí/no: ¿verbo primero? ¿partícula q?
- [ ] Preguntas con wh-: hu, wat, wen, wer, hai, wai, hou
- [ ] Oraciones compuestas: and, bot, or, so, bikos (because)
- [ ] Condicionales: if... den... / if... wud...

**3.7 Tiempo y calendario**
- [ ] Días de la semana: Mondei, Tiuzdei, Wenzdei, Terzdei, Fraidei, Satrdei, Sandei
- [ ] Meses: nombrar los 12 meses
- [ ] Expresiones de tiempo: nau (now), den (then), bifor (before), aft (after)

**Entregable:** `docs/grammar/GRAMMAR_COMPLETE.md`

---

## Fase 4 — Léxico Base (1000 palabras)

**Objetivo:** Construir el vocabulario fundamental. Las palabras más frecuentes del inglés, traducidas y regularizadas fonéticamente.

### 📋 Checklist

**4.1 Palabras frecuentes (Top 500)**
- [ ] Pronombres y determinantes
- [ ] Verbos常用 (top 100)
- [ ] Sustantivos常用 (top 200)
- [ ] Adjetivos常用 (top 100)
- [ ] Preposiciones y conjunciones

**4.2 Sistema de afijos**
- [ ] Prefijos productivos: un-, re-, pre-, mis-, over-, under-, self-, non-, auto-, semi-, super-, inter-
- [ ] Sufijos productivos: -er, -ing, -li, -nes, -ful, -les, -bl, -ish, -skap
- [ ] Probar: generar 20 palabras nuevas con los afijos

**4.3 Compuestos básicos**
- [ ] Compuestos de 2 raíces: hauskel, sunlait, wotcman
- [ ] Compuestos de 3+ raíces
- [ ] Verificar: todos los compuestos respetan (C)V

**4.4 Validación fonológica**
- [ ] Todas las 1000 palabras terminan en vocal o líquida (l, r)
- [ ] Ninguna palabra tiene th, schwa, zh, clusters prohibidos
- [ ] Leer las 1000 palabras: ¿suenan naturales?

**4.5 Validación semántica**
- [ ] Cada palabra puede deducirse de sus componentes
- [ ] Ninguna palabra es traducción directa del inglés sin adaptación

**Entregable:** `lexicon/vela_1000_words.json`

---

## Fase 5 — Léxico Extendido (3000+ palabras)

**Objetivo:** Expandir a todos los campos semánticos importantes.

### 📋 Checklist

**5.1 Tecnología y computing**
- [ ] Software, hardware, internet, AI, data, cloud, algorithm, network...

**5.2 Ciencia**
- [ ] Biología, química, física, medicina, anatomía...

**5.3 Artes y cultura**
- [ ] Música, pintura, literatura, cine, theater, dance...

**5.4 Conceptos abstractos**
- [ ] Filosofía, ética, política, derecho, religión...

**5.5 Emociones (distinciones finas)**
- [ ] tristeza vs melancolía vs duelo vs frustración
- [ ] alegría vs serenidad vs euforia vs satisfacción
- [ ] miedo vs ansiedad vs preocupación vs pánico

**5.6 Sistema de prêtamos**
- [ ] Regla: adaptar fonéticamente al sistema VELA
- [ ] Ejemplo: computer → kompiutr

**5.7 Idiomatismos**
- [ ] Crear 20 expresiones que no existan en inglés
- [ ] Estas dan carácter cultural a VELA

**Entregable:** `lexicon/vela_extended.json`

---

## Fase 6 — Gramática de Referencia

**Objetivo:** Consolidar TODA la gramática en un solo documento de referencia.

### 📋 Checklist

- [ ] Consolidar fonología, escritura, morfología, sintaxis en un documento
- [ ] Formato: manual de referencia (no-tutorial)
- [ ] Un paradigma para cada clase de palabra
- [ ] Un ejemplo para cada regla
- [ ] Índice completo

**Entregable:** `docs/vela_reference_grammar.md`

---

## Fase 7 — Diccionario

**Objetivo:** Crear el diccionario oficial de VELA.

### 📋 Checklist

- [ ] Formato: palabra VELA → pronunciación IPA → categoría → definición → ejemplos → compuestos
- [ ] Mínimo: 1000 entradas
- [ ] Meta: 3000+ entradas
- [ ] Etymología: de qué raíz deriva cada palabra compuesta
- [ ] Equivalentes en español e inglés para cada entrada

**Entregable:** `lexicon/vela_dictionary.md`

---

## Fase 8 — Textos y Muestras

**Objetivo:** VELA existe en el mundo a través de textos reales.

### 📋 Checklist

**8.1 El texto benchmark**
- [ ] *"Go forth in peace to love and serve the Lord."* en VELA

**8.2 Textos fundacionales**
- [ ] 5 poemas originales en VELA
- [ ] 1 cuento corto (500-1000 palabras)
- [ ] Traducción de un cuento infantil clásico

**8.3 Documentación de decisiones**
- [ ] Para cada texto: por qué se tradujo así
- [ ] Trade-offs encontrados al traducir
- [ ] Decisiones gramaticales tomadas en contexto

**Entregable:** `texts/` (carpeta con todos los textos)

---

## Fase 9 — Audio y Pronunciación Estándar

**Objetivo:** Crear el estándar de pronunciación audible de VELA.

### 📋 Checklist

- [ ] Grabar audio: las 17 consonantes y 5 vocales
- [ ] Grabar audio: 100 palabras de ejemplo
- [ ] Grabar audio: pitch accent en acción (penúltima sílaba)
- [ ] Grabar audio: 5 frases de ejemplo
- [ ] Texto fonético IPA para cada grabación
- [ ] ¿Cómo suena VELA? Documentar el "carácter" fonético

**Entregable:** `audio/` (carpeta con grabaciones + IPA transcriptions)

---

## Fase 10 — Comunidad y Evolución

**Objetivo:** VELA deja de ser un proyecto y se convierte en un lenguaje vivo.

### 📋 Checklist

- [ ] Crear comunidad online (sitio web, foro, Discord)
- [ ] VELA Wikipedia (VELA describe VELA)
- [ ] Primer traductor voluntario: crear cuenta y traducir
- [ ] Literatura original en VELA (poesía, narrativa)
- [ ] Eventos: translation challenges, language exchanges
- [ ] Decidir: ¿VELA evoluciona? ¿Se crea una proto-VELA histórica?
- [ ] Resolver disputes de vocabularios (comité o democrático)

**Entregable:** `community/` (guía de comunidad, código de conducta)

---

## Checklist Maestro — Progreso Total

```
Fase 0  → Investigación                ✅
Fase 1  → Fonología                    ✅ COMPLETA
Fase 2  → Sistema de Escritura         ✅ COMPLETA
Fase 3  → Gramática Completa            ✅ COMPLETA
Fase 4  → Léxico Base (1000)           ⬜
Fase 5  → Léxico Extendido (3000+)     ⬜
Fase 6  → Gramática de Referencia      ⬜
Fase 7  → Diccionario                  ⬜
Fase 8  → Textos y Muestras             ⬜
Fase 9  → Audio y Pronunciación        ⬜
Fase 10 → Comunidad y Evolución         ⬜
```

---

## Orden de trabajo recomendado

```
INMEDIATO:
→ Fase 1: Fonología Final ← AHORA

ESTA SEMANA:
→ Fase 1 completa
→ Comenzar Fase 2 (escritura — rápido)

ESTE MES:
→ Fases 1-4 completas

PRÓXIMOS 3 MESES:
→ Fases 5-8 completas

FUTURO:
→ Fases 9-10 (comunidad, audio)
```

---

*Última actualización: 2025-04-13*
*Basado en INITIAL_RESEARCH.md + investigación profunda*
