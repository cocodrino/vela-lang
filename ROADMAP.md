# 🗺️ Roadmap — Desarrollo del Lenguaje VELA

> Roadmap completo para construir VELA desde cero hasta un idioma funcional y documentado.  
> Cada etapa debe estar terminada y documentada antes de avanzar a la siguiente.

---

## Visión General — 7 Etapas

```
Etapa 1  → Fonología (2-4 semanas)
Etapa 2  → Sistema de Escritura (2-3 semanas)
Etapa 3  → Morfología y Gramática (4-6 semanas)
Etapa 4  → Sintaxis (2-4 semanas)
Etapa 5  → Léxico Base — Raíces fundamentales (4-8 semanas)
Etapa 6  → Léxico Extendido — Derivaciones y compuestos (4-8 semanas)
Etapa 7  → Textos, Historia y Documentación Completa (ongoing)
```

**Total estimado:** 6-12 meses de trabajo para un idioma completo de nivel básico-intermedio.

---

## Etapa 1 — Fonología

**Objetivo:** Definir TODOS los sonidos del idioma, cómo se combinan, y cómo se pronuncian.

### 1.1 Inventario de Consonantes

**Pasos:**
- [ ] Elegir qué sonidos tendrá VELA (inventario inicial: 15-30 sonidos)
- [ ] Documentar cada sonido con símbolo IPA: `[p]`, `[b]`, `[t]`, etc.
- [ ] Definir qué sonidos NO tendrá (tan importante como los que SÍ)
- [ ] Escribir reglas de correlación: si existe `/p/` → probablemente `/b/`, `/t/`, `/d/`, `/k/`, `/g/`
- [ ] Nombrar cada sonido con el nombre del alfabeto de VELA (ej: `/a/` = "alfa", `/b/` = "beta")

**Entregable:** `docs/phonology/phoneme_inventory.md`

### 1.2 Inventario de Vocales

**Pasos:**
- [ ] Elegir vocales: básicas (a, e, i, o, u) o más complejas (ɨ, y, etc.)
- [ ] Definir si hay vocales nasales (ã, ẽ, etc.) o no
- [ ] Definir diptongos y triptongos (cuáles, cómo se forman)
- [ ] Definir si hay longitud vocálica (vocal corta vs. larga)

**Entregable:** `docs/phonology/vowel_inventory.md`

### 1.3 Fonotáctica — Reglas de Combinación

**Pasos:**
- [ ] Definir estructura silábica: ¿Cuántas consonantes puede haber juntas?
  - CV (consonante + vocal) — simple
  - CVC, CCVC, CVCC — complejas
- [ ] Definir qué consonantes pueden iniciar sílaba
- [ ] Definir qué consonantes pueden terminar sílaba
- [ ] Definir combinaciones prohibidas (nunca aparecen juntas)
- [ ] Definir si hay diptongos obligatorios o evitables

**Entregable:** `docs/phonology/phonotactics.md`

### 1.4 Prosodia — Acento y Tono

**Pasos:**
- [ ] Definir tipo de acento: fijo (siempre en X sílaba) o móvil (varía)
- [ ] Si fijo: ¿en qué sílaba? (1ª, 2ª, penúltima, última)
- [ ] Definir reglas de alternancia acentual (si el acento cambia en conjugation)
- [ ] ¿El idioma usa tonos (melodía)? Si sí: cuántos, cuáles, cómo funcionan

**Entregable:** `docs/phonology/prosody.md`

### 1.5 Tests de Consistencia

- [ ] Generar 200+ palabras con las reglas fonológicas
- [ ] Verificar que ninguna palabra viola las reglas
- [ ] Ajustar reglas si algo suena artificial o inconsistente
- [ ] Leer la lista de palabras en voz alta: ¿suena natural?

**Entregable:** `docs/phonology/word_list_sample.md` (lista de prueba)

---

## Etapa 2 — Sistema de Escritura

**Objetivo:** Crear un sistema de escritura funcional y documentado para VELA.

### 2.1 Diseño del Alfabeto

**Pasos:**
- [ ] Contar cuántos grafemas necesitas (igual al número de fonemas + opcionalmente más)
- [ ] Investigar inspiraciones: Ogham, Rúnico, Ge'ez, Cuneiforme, etc.
- [ ] Diseñar cada carácter:
  - Inspiración en qué escritura real
  - Número de trazos (15-50)
  - Cómo se distingue de otros caracteres
- [ ] Definir la categorías de cada grafema (consonante, vocal, modificador)
- [ ] Crear versión manuscrita (cursiva) de cada carácter
- [ ] Verificar que no se confunde con números o letras del alfabeto romano

**Entregable:** `docs/writing/alphabet_design.md` +手绘 sketches

### 2.2 Sistema de Vocales en la Escritura

**Pasos:**
- [ ] Si usas abjad (solo consonantes): cómo se escriben las vocales
  - Diacríticos (tildes sobre letras)
  - Letters dedicated (matres dicendi)
  - Alfabeto completo (vocales como letras independientes)
- [ ] Definir cómo se marca la nasalización
- [ ] Definir cómo se marca la longitud vocálica

**Entregable:** `docs/writing/vowel_notation.md`

### 2.3 Convenciones de Escritura

**Pasos:**
- [ ] Definir dirección: LTR, RTL, o alternativa
- [ ] Definir puntuación: qué símbolos usas (inventar originales o adaptar)
- [ ] Definir capitalización (si existe)
- [ ] Definir cómo se escriben números
- [ ] Definir spacing (espacios entre palabras: sí/no)
- [ ] Definir escritura de palabras extranjeras (si aplica)

**Entregable:** `docs/writing/writing_conventions.md`

### 2.4 Fonts y Tipografía (Opcional)

- [ ] Crear o mandar a hacer una font para VELA
- [ ] Definir versión bold, italic, etc.
- [ ] Probar en distintos tamaños y contextos

**Entregable:** `fonts/vela-alphabet.ttf` (si se hace)

### 2.5 Práctica de Escritura

- [ ] Escribir 50 palabras a mano en el nuevo alfabeto
- [ ] Verificar que cada grafema es legible y fácil de escribir
- [ ] Ajustar 1-2 caracteres problemáticos

---

## Etapa 3 — Morfología y Gramática

**Objetivo:** Definir cómo se estructuran las palabras y cómo cambian.

### 3.1 Sistema Morfológico

**Pasos:**
- [ ] Elegir el tipo de lengua:
  - ¿Aislante? → palabras simples sin flexión
  - ¿Aglutinante? → afijos claros y separables
  - ¿Fusional? → terminaciones que combinan múltiples significados
  - ¿Mixto? → algunos aspectos aislantes, otros fusionales
- [ ] Documentar la decisión y justificar por qué refleja la cultura imaginada

**Entregable:** `docs/grammar/morphological_system.md`

### 3.2 Sistema Nominal (Sustantivos)

**Pasos:**
- [ ] **Número:** ¿Cómo marca plural? ¿dual? ¿paucal?
  - Sufijo: -s, -im
  - Reduplicación: palabra-palabra
  - Cambio interno: foo → fey
  - Sin marca (aislante)
- [ ] **Caso:** ¿Cuántos casos tiene?
  - Mínimo: Nominativo + Acusativo
  - Promedio: 4-6 casos (N, A, G, D, L, I)
  - Máximo: 20+ casos (húngaro, finlandés)
- [ ] **Género:** ¿Tiene género gramatical?
  - Si sí: cuántos (2, 3, 4+), cómo se marca
  - Si no: Neutro, o ausencia total
- [ ] **Artículos:** ¿Tiene? ¿Definido (el) vs. indefinido (un)?
- [ ] **Clasificación nominal:** ¿Clases de sustantivos que afectan la conjugación?

**Entregable:** `docs/grammar/nominal_system.md`

### 3.3 Sistema Verbal (Verbos)

**Pasos:**
- [ ] **Tiempo:** ¿Cuántos? ¿Simples o compuestos?
  - Mínimo: Pasado, Presente, Futuro
  - Promedio: Agregar Recent Future, Far Past, etc.
  - Compound tenses: "I have seen" = have + seen (para perfect, progressive)
- [ ] **Aspecto:** ¿Perfectivo, Imperfectivo, Perfecto, Progresivo?
- [ ] **Modalidad:**
  - Realis vs. Irrealis (posibilidade y necesidad)
  - Imperativo (órdenes)
  - Optativo (deseos)
  - Condicional (si... entonces...)
  - Dubitativo (incertidumbre)
- [ ] **Voz:** ¿Activo, Pasivo, Medio, Causativo?
- [ ] **Persona/Número:** ¿Conjugación por persona?

**Entregable:** `docs/grammar/verbal_system.md`

### 3.4 Pronombres

**Pasos:**
- [ ] Inventario de pronombres: 1ª, 2ª, 3ª persona
- [ ] Singular, Plural, Dual (si aplica)
- [ ] ¿Pronombres inclusivos/exclusivos (nosotros=yo+tú vs. yo+otros)?
- [ ] Pronombres posesivos
- [ ] Pronombres demostrativos (este/ese/aquel)
- [ ] Pronombres relativos e interrogativos

**Entregable:** `docs/grammar/pronouns.md`

### 3.5 Adjetivos y Adverbios

**Pasos:**
- [ ] ¿Los adjetivos se flexionan? ¿Dónde se colocan?
- [ ] Comparativos y superlativos: cómo se forman
- [ ] Adverbios: cómo se forman desde adjetivos

### 3.6 Sistema de Numerales

**Pasos:**
- [ ] Sistema numérico: decimal (10), vigesimal (20), otro
- [ ] Construir 1-100 en VELA
- [ ] Construir 100, 1000, 1000000
- [ ] Números ordinales
- [ ] Abreviaciones comunes

### 3.7 Preposiciones y Posposiciones

- [ ] ¿Usa preposiciones (antes del nombre) o posposiciones (después)?
- [ ] Inventario de preposiciones/posposiciones con significado

### 3.8 Conjunciones y Oraciones Compuestas

- [ ] Y, O, PERO, porque, si, que, cuando, etc.
- [ ] Reglas para oraciones compuestas

---

## Etapa 4 — Sintaxis

**Objetivo:** Definir cómo se combinan las palabras en oraciones.

### 4.1 Orden Básico

**Pasos:**
- [ ] Elegir orden fundamental: SVO, SOV, VSO, VOS, OSV, OVS
- [ ] Documentar la decisión
- [ ] Crear 50 oraciones de ejemplo para probar que funciona
- [ ] Verificar que la sintaxis no requiere reformulaciones absurdas

**Entregable:** `docs/syntax/basic_word_order.md`

### 4.2 Orden en Oraciones Especiales

**Pasos:**
- [ ] **Preguntas sí/no:** ¿Partícula, inversión, entonación?
- [ ] **Preguntas con Q-word (qué, quién, cómo):** ¿Orden especial?
- [ ] **Negación:** ¿Dónde va "no"? ¿Una palabra o más?
- [ ] **Órdenes/Imperativos:** ¿Orden especial?
- [ ] **Exclamaciones:** ¿Se marca con partícula o con entonación?

**Entregable:** `docs/syntax/special_sentences.md`

### 4.3 Cláusulas Relativas

- [ ] ¿Cómo se construyen? ¿Con pronombre relativo, partícula, o head-final?
- [ ] Definir 5 ejemplos de cláusulas relatives

### 4.4 Estilo y Registros

- [ ] ¿Diferencia entre registro formal e informal?
- [ ] ¿Tú vs. usted equivalents?
- [ ] ¿Jerga o dialectos sociales?

---

## Etapa 5 — Léxico Base

**Objetivo:** Construir las raíces fundamentales del idioma (~200-500 raíces).

### 5.1 Método de Construcción

**Pasos:**
- [ ] Elegir método principal:
  - a) Root-and-affix: raíces con prefijos/sufijos productivos
  - b) Word-compounding: composición de raíces
  - c) Mixt: ambos
- [ ] Definir qué tipo de sonido = qué tipo de concepto (sound symbolism)
- [ ] Crear el mapeo semántico de raíces

**Entregable:** `docs/lexicon/root_method.md`

### 5.2 Léxico de Emergencia (Core Vocabulary)

Empezar con las ~100 palabras más fundamentales:

```
PRONOMBRES: yo, tú, él/ella/ello, nosotros, vosotros, ellos
PARENTESCOS: madre, padre, hijo, hermano, hermana, hijo, esposo, esposa
CUERPO: cabeza, ojo, oreja, nariz, boca, mano, pie, corazón
ANIMALES: perro, gato, pájaro, pez, caballo, lobo, oso, serpiente
NATURALEZA: agua, fuego, tierra, aire, sol, luna, estrella, nube, lluvia
TIEMPO: día, noche, mañana, año, mes, ahora, después, antes
NÚMEROS: 1-10 mínimo, idealmente 1-100
VERBOS BÁSICOS: ser, estar, tener, hacer, ir, venir, decir, ver, querer, poder
CONCEPTOS: grande, pequeño, bueno, malo, nuevo, viejo, caliente, frío, bonito, feo
```

### 5.3 Expansión del Léxico

```
TRANSPORTE: carro, caballo, barco, avión, camino, puente
ALIMENTOS: pan, carne, verdura, fruta, sal, azúcar, agua, leche
VESTIMENTA: ropa, camisa, pantalón, zapato, sombrero
CONSTRUCCIÓN: casa, puerta, ventana, pared, techo, calle
SOCIEDAD: rey, ciudad, pueblo, guerra, paz, ley
EMOCIONES: amor, odio, miedo, alegría, tristeza, esperanza
RELIGIÓN/MITOLOGÍA: (específico del worldbuilding del idioma)
```

### 5.4 Reglas de Derivación

**Pasos:**
- [ ] Definir prefijos productivos: ¿cuáles? ¿cuándo se usan?
- [ ] Definir sufijos produktifivos: -dor, -ción, -mente, etc.
- [ ] Definir palabras compuestas regulares
- [ ] Crear 10 ejemplos de cada regla de derivación

**Entregable:** `lexicon/derivational_rules.md`

---

## Etapa 6 — Léxico Extendido

**Objetivo:** Expandir a 1000-3000 palabras con derivaciones ricas.

### 6.1 Campos Semánticos Especializados

- [ ] Léxico de emociones finas (no solo "triste" — específico para tipo de tristeza)
- [ ] Léxico de la cultura del mundo imaginado
- [ ] Léxico técnico si el worldbuilding lo requiere (magia, tecnología, etc.)

### 6.2 Familias de Palabras

- [ ] Para cada raíz importante: crear 5-10 derivaciones
- [ ] Verificar que todas las derivaciones respetan fonotáctica
- [ ] Verificar coherencia semántica

### 6.3 Léxico de Préstamos

- [ ] ¿El idioma toma préstamos de otras lenguas?
- [ ] Cómo adapta los sonidos extranjeros
- [ ] ¿Mantiene la ortografía original o la adapta?

### 6.4 Validación del Léxico

- [ ] Traducir un texto estándar (ver Etapa 7) y ver si hay gaps
- [ ] Rellenar gaps con vocabulario nuevo
- [ ] Repetir hasta que el texto fluya sin problemas

---

## Etapa 7 — Textos, Historia y Documentación

**Objetivo:** El idioma cobra vida con textos reales, historia y documentación completa.

### 7.1 Textos de Prueba

**Pasos:**
- [ ] Traducir textos de referencia:
  - La oración "Go forth in peace to love and serve the Lord" (benchmark estándar de conlangs)
  - El Poema del Destierro (poema fundacional)
  - 3-5 textos adicionales en el idioma
- [ ] Documentar cada decisión de traducción
- [ ] Verificar que la gramática funciona en textos reales

**Entregable:** `texts/`
  - `vela_first_sentence.md` — Oración benchmark
  - `vela_poetry.md` — Poemas
  - `vela_narrative.md` — Narrativa corta
  - `vela_dialogue.md` — Diálogos

### 7.2 Genealogía (Opcional pero Recomendado)

- [ ] Crear protolengua (si aplica)
- [ ] Definir cambios fonéticos de protolengua → VELA moderno
- [ ] Crear 1-2 dialectos con derivaciones propias
- [ ] Crear historia lingüística (cuándo cambió qué)

**Entregable:** `docs/evolution/genealogy.md`

### 7.3 Gramática de Referencia Completa

- [ ] Consolidar todos los documentos gramaticales en UN documento
- [ ] Incluye: fonología, escritura, morfología, sintaxis, léxico
- [ ] Escribir en formato de referencia (no tutorial)
- [ ] Ejemplos para cada regla

**Entregable:** `docs/vela_reference_grammar.md`

### 7.4 Diccionario

- [ ] Formato: entrada por palabra + pronunciación (IPA) + clase + definición + ejemplos
- [ ] Incluir derivaciones
- [ ] Incluir etimología

**Entregable:** `lexicon/vela_dictionary.md`

### 7.5 Materiales de Aprendizaje (Opcional)

- [ ] Guía para aprender VELA desde cero
- [ ] Lista de vocabulario por tema
- [ ] Ejercicios de práctica
- [ ] Respuestas

---

## Métricas de Éxito

Al final de cada etapa, verificar:

```
□ ¿Puedo generar 50 palabras nuevas que respeten todas las reglas?
□ ¿Puedo traducir oraciones sin ambiguity gramatical?
□ ¿Las palabras nuevas se sienten "del idioma" y no como traducciones del inglés?
□ ¿Puedo leer texto en voz alta usando solo las reglas fonológicas?
□ ¿El idioma tiene suficiente flexibilidad para expresiones imprevistas?
□ ¿La gramática se siente orgánica, no arbitraria?
□ ¿Hay gaps obvios que necesiten rellenarse?
```

---

## Orden Recomendado de Trabajo

```
1. Etapa 1 (Fonología) — COMPLETA
   ↓
2. Etapa 2 (Escritura) — mientras escuchas palabras pronunciadas
   ↓
3. Etapa 3 (Gramática) — sobre papel, genera paradigmas completos
   ↓
4. Etapa 4 (Sintaxis) — testea con 50 oraciones
   ↓
5. Etapa 5 (Léxico base) — empieza con core vocabulary
   ↓
6. Etapa 4 (Sintaxis) — revisa con vocabulario real
   ↓
7. Etapa 3 (Gramática) — ajusta con lo aprendido en etapas 5-6
   ↓
8. Etapa 6 (Léxico extendido) — sobre textos reales
   ↓
9. Etapa 7 (Textos + Documentación)
```

**Nota importante:** Las etapas 3-6 no son completamente secuenciales. Volverás a ajustar la gramática mientras construyes el léxico. Esto es normal y esperado.

---

## Puntos de Decisión Abiertos para VELA

(Lista a llenar conforme avance el proyecto)

```
□ Tipo de lengua: ¿Aislante, aglutinante, fusional o mixto?
□ Orden sintáctico: ¿SVO, SOV, VSO?
□ Sistema de casos: ¿Cuántos?
□ Tonos: ¿Sí o no?
□ Género: ¿Sí o no?
□ Pronombres: ¿Inclusivo/exclusivo?
□ Préstamos: ¿Se permiten?
□ Dialectos: ¿Uno o varios?
□ Protolengua: ¿Se crea historia?
□ Familia lingüística: ¿Derivada de otra o aislada?
```

---

*Este roadmap fue creado como guía para el desarrollo del lenguaje VELA, basado en The Language Construction Kit (Mark Rosenfelder), recursos de r/conlangs, y mejores prácticas de la comunidad de conlanging.*
