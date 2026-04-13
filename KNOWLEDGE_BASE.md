# 🧠 Knowledge Base — Construcción de Lenguajes

> **La guía más completa para construir un lenguaje artificial.**  
> Basada en *The Language Construction Kit* (LCK) de Mark Rosenfelder, con дополнения de conlanging.org, Wikibooks, y comunidades de conlangs.

---

## Tabla de Contenidos

1. [Fundamentos: Por Dónde Empezar](#1-fundamentos)
2. [Fonología — Los Sonidos del Idioma](#2-fonología)
3. [Escritura — Sistemas de Representación](#3-sistemas-de-escritura)
4. [Morfología — La Estructura de las Palabras](#4-morfología)
5. [Sintaxis — Cómo se Ordenan las Palabras](#5-sintaxis)
6. [Semántica — El Significado](#6-semántica)
7. [Léxico — Construir el Vocabulario](#7-léxico)
8. [La Genealogía de los Lenguajes](#8-genealogía-y-evolución)
9. [Recursos Adicionales](#9-recursos)

---

## 1. Fundamentos

### Lo que necesitas antes de traducir

Antes de poder escribir "Go forth in peace" en tu idioma, necesitas:

```
1. Decidir los SONIDOS del idioma
2. Crear el LÉXICO (vocabulario)
3. Crear la GRAMÁTICA
4. Diseñar un ALFABETO
5. Decidir cómo se escribe en manuscrito (cursiva)
6. TRADUCIR el texto deseado
```

**Importante:** Trabajar en este orden es fundamental. Trabajar al revés (crear un texto y luego inventar la gramática para que funcione) genera un idioma incoherente. Un mal ejemplo: el Syldavian de Hergé — inventado por partes, imposible crear una fonología o morfología consistente.

### Modelos de Lenguajes

Tu lenguaje puede parecerse a cualquier lengua natural:

| Tipo | Características | Ejemplos |
|------|----------------|---------|
| **Aislante** | Una palabra = un morpheme. Sin flexión. | Chino mandarín, Vietnamita |
| **Aglutinante** | Prefijos y sufijos separados. Cada afijo = un significado. | Turco, Swahili, Coreano |
| **Fusional** | Una terminación = múltiples significados. | Español, Latín, Hindi |
| **Polisintético** | Palabras largas compuestas por muchos afijos. | Inuktitut, Cherokee |
| **Prefijante** | La mayoría de la flexión va al inicio de la palabra. | Árabe, Hebreo |
| **Sufijante** | La mayoría de la flexión va al final. | Japonés, Turco |

### Paso 1: Define tu Proto-idioma (Avanzado)

**El método avanzado:** Crear una protolengua — una lengua antigua de la cual derivan dialectos modernos con evolución orgánica.

Esto es lo que hace J.R.R. Tolkien con sus idiomas élficos. Requiere:
- Crear la protolengua primero
- Derivar las lenguas "modernas" con cambios fonéticos regulares
- Mantener un registro de los cambios: qué sonido se convirtió en qué

**El método básico (recomendado para empezar):** Crear una sola lengua sin derivaciones históricas.

---

## 2. Fonología

### Qué es la Fonología

La fonología es el inventario de sonidos de tu idioma — qué sonidos tiene y cuáles no. Es lo primero que necesitas definir.

### El Alfabeto Fonético Internacional (AFI/IPA)

Usa el IPA para documentar los sonidos. Cada sonido = un símbolo entre corchetes: `[p]`, `[a]`, `[θ]` (inglés "th"), etc.

**Categorías de sonidos:**

```
CONSONANTES:
  Oclusivas:     p  b     t  d     k  g     ʔ (glottal stop, "uh-oh")
  Fricativas:    f  v     θ  ð     s  z     ʃ  ʒ     x  ɣ     h
  Nasales:       m  n     ɲ (español "ñ")  ŋ (inglés "ng")
  Laterales:     l  ʎ (español "ll")      ɬ (galés "ll")
  Róticas:       r  ɾ (español "rr")     ʀ (francés "r")
  Aproximantes:  w  ʋ (holandés "w")     j (español "y")
  Africadas:     tʃ (español "ch")      ts (español "z")      dʒ (inglés "j")

VOCALES:
  Altas:         i  ɨ (rumano "ă")     u
  Medias:        e  ə (schwa, "a" en "about")  o
  Bajas:         ɛ (inglés "e" en "bed")  ɔ (inglés "o" en "law")  a
  Diptongos:     ai  au  oi  ei  etc.

DIPTONGOS Y TRIPTONGOS:
  Sonidos que combinan dos o tres vocales en una sola sílaba.
```

### Reglas para una Fonología Naturalista

**1. Elige un subconjunto del IPA, no todos los sonidos**

Los idiomas naturales usan entre 11-85 fonemas. Para un conlang:
- **Mínimo:** ~12-15 sonidos (lenguaje simple)
- **Promedio:** ~20-30 sonidos
- **Complejo:** ~40+ sonidos (para idiomas muy expresivos)

**2. Define tus categorías (qué sonidos tienes y cuáles NO)**

Ejemplo — Lenguaje sin `/p/` ni `/v/`:
```
Tiene:   /b/ /d/ /g/ /k/ /s/ /z/ /f/ /t/ /m/ /n/ /l/ /r/
No tiene: /p/ /v/ /ʃ/ /ʒ/ /θ/ /ð/
```

Esto crea un sonido distintivo. No copies el inglés.

**3. Los sonidos correlacionan en patrones**

Los idiomas tienen patrones: si tienes `/p/` y `/b/`, típicamente también tienes `/t/` y `/d/`, y `/k/` y `/g/`. Los idiomas tiende a ser simétricos.

**4. Define qué combinaciones de sonidos son válidas**

Esto se llama **fonotáctica** (phonotactics).

```
Reglas de ejemplo:
- Ninguna palabra termina en /s/
- No hay dos consonantes seguidas al inicio
- /ŋ/ solo aparece en posición final
```

### Sistema de Acentuación

Define:
- ¿Dónde cae el acento? (primera sílaba, última, o variable)
- ¿Es fijo o móvil? (móvil = cambia según la forma de la palabra)
- ¿El idioma tiene tones (melodía)? (como chino, tailandés)
  - Si usas tonos: ¿cuántos? ¿cómo funcionan?

### Definiendo los Sonidos de VELA (ejemplo)

```
CONSONANTES (a definir):
  Oclusivas: p, b, t, d, k, g, q, ʔ
  Fricativas: f, v, θ, ð, s, z, ʃ, h
  Nasales: m, n, ɲ, ŋ
  Laterales: l, ʎ
  Róticas: r, ɾ
  Aproximantes: w, j

VOCALES:
  Puras: i, e, a, o, u
  Nasalizadas: ã, ẽ, ĩ, õ, ũ

REGLAS FONOTÁCTICAS:
  - No hay /ŋ/ al inicio
  - /ʎ/ solo entre vocales
  - Contras final de palabra: /n/, /m/, /l/, /r/, /s/
  - Acento: siempre en la penúltima sílaba

TONOS: No (sin tono melódico)
```

---

## 3. Sistemas de Escritura

### Tipos de Sistemas

| Tipo | Cómo funciona | Ejemplos |
|------|-------------|---------|
| **Alfabético** | Un grafema = un sonido | Latín, Griego, Español |
| **Silábico** | Un grafema = una sílaba | Hiragana, Katakana |
| **Logográfico** | Un grafema = una palabra/morfema | Chino, Jeroglíficos |
| **Abjad** | Un grafema = una consonante (sin vocales) | Árabe, Hebreo |
| **Alfabeto con vocales** | Alfabeto + marcas de vocales | Coreano Hangul, Tifinagh |
| **Mnemonic/Runic** | Alfabeto inventado con propósito específico | Tengwar, Klingon |

### Diseñando un Alfabeto Original

**Pasos:**

1. **Cuántos sonidos tienes?** Divide en categorías.
2. **Busca inspiración** en alfabetos reales:
   - Latino, Griego, Cirílico, Armenio, Ge'ez, Ogham, Rúnico
3. **Dibuja los caracteres.** Cada uno debe:
   - Ser distinguible de los demás
   - Ser fácil de escribir a mano
   - Tener entre 15-50 trazos (no más, no menos)
   - No confundir con números o letras del alfabeto romano

4. **Crea un orden del alfabeto.** Esto importa para diccionarios, listas, etc.

### Sistema de Vocales en Alfabetos

Problema: los alfabetos consonantivos (árabe, hebreo) omiten vocales. Soluciones:

```
SOLUCIÓN 1: Alfabeto completo (latino, griego)
  → Cada vocal tiene su letra

SOLUCIÓN 2: Matres dicendi (semíticos)
  → /a/ = 'alef, /i/ = yod, /u/ = vav
  → Las vocales se marcan con letras dedicadas

SOLUCIÓN 3: Diacríticos (latín con cantidad, sánscrito)
  → Las vocales se marcan con tildes/puntos sobre la consonante

SOLUCIÓN 4: Abugida (sánscrito, etíope)
  → Cada símbolo base = consonante + /a/
  → Modificadores cambian la vocal
```

### Normas de Escritura

Define para tu sistema de escritura:

```
1. Dirección: LTR, RTL, o Boustrophedon (como griego antiguo)?
2. Puntuación: commas, periods, quotes, ¿símbolos originales?
3. Mayúsculas/Minúsculas: sí o no
4. Números: cómo se escriben
5. Espacio entre palabras: sí o no (el chino no usa espacios)
6. Escritura manuscrita vs. impresa: ¿difieren significativamente?
```

---

## 4. Morfología

### Morfología = Estructura de las Palabras

Las palabras se construyen con **morfemas** — la unidad mínima con significado.

```
3 tipos de morfemas:

1. RAÍZ: El núcleo de significado
   "cantar" → la idea de canto

2. AFUJO (AFFIX): Se añade a la raíz
   Prefix:  pre- + ver → prever
   Suffix:  cantar + -dor → cantante (el que canta)
   Infix:   k-put →kiput (entagled) (no existe en español)
   Circumfix: em- + -ar → em + bestyar → embestyar

3. PALABRA COMPUESTA: Dos raíces juntas
   English: "keyboard" = key + board
   Español: "sacacorchos" = saca + corchos
```

### Sistemas Morfológicos

**Sistema 1: Aislamiento (palabras simples, sin cambios)**

```
"hombre bueno" = dos palabras separadas
"yo voy" = dos palabras separadas
No hay flexión de verbos ni conjugaciones
```

**Sistema 2: Aglutinación (muchos afijos claros)**

```
Turco: gel-ecek-di
  gel = venir
  -ecek = futuro
  -di = pasado
  = "él vendrá" (pero se divide清清楚楚)
```

**Sistema 3: Fusión (una terminación = múltiples significados)**

```
Español: "cantaste"
  cant = raíz
  -aste = 2ª persona + singular + pretérito
  → Una terminación = 3 significados fused together
```

### Número, Caso y Género

**Número:** Singular / Plural (a veces Dual, Trial, Paucal)

```
Singular: 1 objeto
Plural:   más de 1
Dual:     exactamente 2 (griego, árabe, sloveno)
Paucal:   unos pocos (3-10)
Greater Plural: más de lo normal (hebreo)
```

**Caso:** La función gramatical de un sustantivo (quién hace qué)

```
Nominativo:  Sujeto ("él CORRE")
Acusativo:   Objeto Directo ("veo A ÉL")
Genitivo:    Posesivo ("la casa DE ÉL")
Dativo:      Objeto Indirecto ("dio A ÉL")
Vocativo:    Llamar ("¡JUAN!")
Locativo:    Ubicación ("en casa")
Instrumental: Con qué ("con EL MARTILLO")
Ablativo:    De dónde ("desde LA MONTAÑA")
```

**Género:** Clasificación de sustantivos

```
Género natural:  Solo macho/hembra (inglés: he/she)
Gênero gramatical: 3 géneros sin relación con sexo
  Masculino: la luna
  Femenino:   el sol
  Neutro:      lo demás
No género:      chino, indonesio
```

### Tiempo, Aspecto y Modalidad (TAM)

**Tiempo (Tense):** CUÁNDO ocurre (pasado, presente, futuro)

**Aspecto:** CÓMO ocurre
```
Perfectivo:   Verbo como un todo completado
  "LEÍ el libro" (lo terminé)
Imperfectivo: Verbo en progreso
  "LEÍA el libro" (lo estaba leyendo)
Perfecto:     Pasado con relevancia actual
  "HE LEÍDO" (ya lo terminé, y es relevante)
Progresivo:   En proceso de ocurrir
  "ESTOY LEYENDO"
```

**Modalidad:** Si algo es real, posible, necesario, deseado, etc.

```
Realis:    "El caballo ESTÁ en el prado" (hecho real)
Irrealis:  "Si el caballo ESTUVIERA en el prado..." (condicional)
Dubitativo:"El caballo quizás ESTÉ en el prado" (duda)
Desiderativo:"Quiero que el caballo ESTÉ en el prado" (deseo)
Imperativo: "¡ESTÁ en el prado!" (orden)
```

### Sistema Verbal

Define para cada verbo:
- Tiempo (pasado, presente, futuro — ¿todos o solo algunos?)
- Aspecto (perfectivo, imperfectivo, progresivo)
- Modalidad (realis, irrealis, etc.)
- Persona/Número (1ª, 2ª, 3ª + singular/plural)
- Voz (activo, pasivo, medio, causativo)
- Estado (estativo vs. dinámico)

---

## 5. Sintaxis

### Sintaxis = Orden de las Palabras

Define el **orden básico** de tu idioma:

```
Orden SVO (Sujeto-Verbo-Objeto):
  "Yo como manzanas" — Español, Inglés, Chino
  Sujeto primero, verbo después

Orden SOV (Sujeto-Objeto-Verbo):
  "Yo manzanas como" — Japonés, Hindi, Latín
  Verbo al final

Orden VSO:
  "Como yo manzanas" — Irlandés, Tagalo, Hebreo bíblico

Orden VOS:
  "Como manzanas yo" — Malgache

Orden OSV:
  "Manzanas yo como" — Yoda-speak,台山话

Orden OVS:
  "Manzanas como yo" —few languages
```

### Orden en Frases Subordinadas

El orden de la frase principal ≠ orden en subordinadas.

### Preguntas

```
Sí/No preguntas:
  1. Partícula interrogativa: Lakota "He PANI ye?" — el "ye" al final marca pregunta
  2. Inversión sujeto/verbo: Alemán "Kommst du?" (vienes tú?)
  3. Entación rising: (no hay cambio, solo entonación)
  4. Marcador de pregunta: Español "¿Vienes?"

Wh-questions (pregunta con palabra):
  - Pregunta word se queda en posición normal: Inglés "What you SEE?"
  - Wh-word se mueve al inicio: Español "¿Qué ves?"
  - Partícula especial: Japonés "Nani o MITE-ru ka?"
```

### Negación

Define cómo negar:

```
NEGACIÓN SIMPLE:
  Partícula:    Español "no", Japonés "-nai", Inglés "not"
  Doble negación: Español "No tengo NADA" (doble = positivo)

NEGACIÓN FRASE COMPLETA:
  Negación Special word: "It's not raining" (no es una_lluvia)
  vs. "N没有下雨" (no/hay lluvia)
```

### Cláusulas Relativas

"el hombre QUE VIÓ el perro"

```
1. Con pronombre relativo: Inglés "that/who/which"
   "the man [who saw the dog]"

2. Con partícula: Japonés "no"
   "inu o mita otoko" = hombre [perro vío]-no

3. head-final: Verbo al final con sumark
   "the man dog saw"
```

---

## 6. Semántica

### Significado y Contexto

**Problemas semánticos comunes en conlangs:**

1. **Vaguedad:** ¿Tu palabra para "árbol" incluye arbustos? ¿hierba?
2. **Sobreespecificación:** Una palabra para cada tipo específico cuando necesitas generalizar
3. **Gaps:** No tienes palabra para algo importante en tu cultura
4. **Ambigüedad:** Una palabra = muchos significados sin contexto

### Metaphor y Cultura

Los idiomas codifican la cultura de sus hablantes:

```
Inglés: "He's under the WEATHER" (meteorológico = emocional)
Español: "Estar con el ánimo BAJADO" (arriba/abajo espacial = emocional)
Japonés: "Kuki ga amui" (espacio = estado de ánimo)
```

Tu conlang debe reflejar la cultura de los hablantes que imaginaste.

---

## 7. Léxico — Construir el Vocabulario

### El Método Root-and-Affix (Raíz + Afijo)

**Más importante y más difícil.**

Un idioma natural tiene 50-200 raíces de las cuales deriva miles de palabras.

```
Ejemplo Español:
  pan- (latín PANIS)
  ├── panadería (lugar de pan)
  ├── panecillo (diminutivo)
  ├── panificadora (donde se hace pan)
  └── empanar (cubrir con pan rallado)

Ejemplo Klingon:
  ghitlhugh (batalla espacial)
  ├── ghitl' (nave de batalla)
  ├── ghetlh (combatiente)
  └── 'ugh (pelear)
```

### Cómo crear raíces que no parezcan inglés

**Errores comunes:**
- Traducir palabras inglés directamente
- Usar fonología inglesa
- Copiar patrones inglés

**Método 1: Word Association Map**

Para cada concepto, haz un mapa de asociaciones antes de inventar la palabra:

```
CONCEPTO: AGUA
  → Líquido, vital, río, mar, beber, bañarse, H2O, etc.
  → La raíz de agua debeevocar TODAS estas conexiones en tu idioma.
```

**Método 2: Sound Symbolism**

Algunos sonidos se sienten "redondos" o "puntiagudos":

```
/d/ /b/ /l/ → sonidos suaves, orgánicos
/gl/ /kl/ → sonidos ásperos, duros
/m/ /n/ → sonidos pequeños
/p/ /t/ /k/ + /r/ → sonidos grandes
```

No es una ciencia pero sí ayuda a que el idioma se sienta coherente.

**Método 3: Derivar de otra lengua**

Crea raíces basadas en otra lengua (latín, finés, swahili) pero transformadas:

```
Latín: PATER → derivar en tu idioma → PADRE
Cambios regulares: p→f, t→s, r→r
FISRE = padre en tu idioma
```

### El Problema del Anglocentrismo

**Evita:**
- Tener una palabra para cada concepto inglés
- Usar "/θ/" (th inglés) si tu idioma no lo tiene
- Copiar los "falsos amigos" del inglés

**Pero en VELA específicamente:**

VELA tiene un sesgo intencional hacia anglófonos — es EL DISEÑO, no un error.

```
Regla VELA: El idioma debe ser lo MÁS FÁCIL para anglófonos.
             Y lo suficientemente simple para que cualquier otro lo aprenda rápido.

Si una palabra es fácil para anglófonos y difícil para hispanos → aún aceptable
Si una palabra es fácil para TODOS → IDEAL, usarla siempre
```

**Pregunta constantemente:**
"¿Un anglófono reconocería esto instantáneamente?"
"¿Un hispanohablante/chino/coreano puede aprenderlo en 1 semana?"

### Las 5 Reglas del Vocabulario VELA

```
REGLA 1: Si una palabra latina/internacional es recognoscible para
         anglófonos Y hispanohablantes → USAR LATÍN

REGLA 2: Si la palabra latina NO es recognoscible para nadie →
         usar la palabra más simple fonéticamente

REGLA 3: Si palabra inglesa y latina son igualmente válidas →
         preferir la más corta y simple

REGLA 4: NUNCA elegir una palabra solo porque es "inglesa"
         NUNCA elegir una palabra solo porque es "latina"

REGLA 5: La identidad de VELA NO es "Esperanto renacido"
         NI "Inglés con ortografía regular"
         → Es una lengua moderna, bella y neutral
```

**Ejemplos:**

| Concepto | English | Latin | VELA | Por qué |
|-----------|---------|-------|------|---------|
| familia | famili | familia | **familia** | Latin = recogn. para ambos |
| mundo | world | mundo | **mundo** | Latin = recogn. para ambos + idéntico español |
| sol | sun | sol | **sol** | Identical en todos |
| libro | buk | libro | **libro** | Latin = recogn. para ambos |
| grande | big | grand | **grand** | Ambos claros → más corta: grand |
| hablar | tok | vok | **tok** | Ninguno reconoce "vok" → más simple: tok |

---

## 8. Genealogía y Evolución

### Cómo Funciona la Evolución Lingüística

Los idiomas cambian predeciblemente:

```
Lengua madre: PATER
  ↓
Hija 1 (Latín): PATER
  ↓
Hija 2 (Español): PADRE (p→b, t→d, r→r)
Hija 2 (Francés): PÈRE    (p→p, t→d, r→r)
Hija 2 (Italiano): PADRE  (p→p, t→d, r→r)
```

**Cambios fonéticos comunes:**

```
p → b, t → d, k → g (lenición/sonorización)
f → h → nada ( wegfall delfh)
s → h → θ → f (rotacismo)
kw → p (latín QUATTUOR → CATOR)
ai → ei → e → i (monoptongación)
```

### Para qué sirve en un Conlang

Crear una genealogía te permite:
- Crear dialectos coherentes de la misma lengua
- Hacer que el idioma se sienta "orgánico" con historia
- Crear familias de palabras con raíces compartidas

---

## 9. Recursos

### Libros Fundacionales

| Libro | Autor | Link |
|-------|-------|------|
| **The Language Construction Kit** | Mark Rosenfelder | https://www.zompist.com/kit.html |
| **Advanced Language Construction** | Mark Rosenfelder | Amazon (Yonagu Books) |
| **The Conlanger's Lexipedia** | Mark Rosenfelder | Amazon |
| **The Syntax Construction Kit** | Mark Rosenfelder | Amazon |
| **Conlanging 101** | Sai Emrys | https://conlang.org/cl101.pdf |
| **The Language of the Night** | Francis P. L. Cotnam | (fuera de print) |

### Recursos en Línea

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **Zompist.com** | https://www.zompist.com | Artículos, herramientas, LCK |
| **Conlang Wikibooks** | https://en.wikibooks.org/wiki/Conlang | Guía colaborativa completa |
| **Conlang.org** | https://conlang.org | Comunidad y recursos |
| **TV Tropes: Create a Conlang** | https://tvtropes.org/pmwiki/pmwiki.php/SoYouWantTo/CreateAConlang | Guía práctica |
| **LinguaVirtua** | https://linguavirtua.com | Tutoriales y tips |
| **r/conlangs** | https://reddit.com/r/conlangs | Comunidad activa |
| **Phonetic Symbols Guide** | https://jakubmarian.com/phonetic-symbols-guide/ | Guía IPA visual |

### Comunidades

- **r/conlangs** — Reddit, la más activa
- **Zompist Forums** — Foros de Mark Rosenfelder
- **Discord Conlangery** — Server de Discord de podcasts y comunidad
- **Fandom Conlangs Wiki** — Wiki colaborativa

### Herramientas

| Herramienta | URL | Uso |
|------------|-----|-----|
| **Zompist Lexifer** | https://www.zompist.com/lexifer.html | Generador de vocabulario |
| **Zompist Spelward** | https://www.zompist.com/spelward.html | Generador de sistemas de escritura |
| **Vulcan Language Creator** | (varios fansites) | Ejemplo de creación de alien languages |
| **PolyMath TTS** | polyanthum.com | Text-to-speech para conlangs |
| **Forvo** | forvo.com | Pronunciación de idiomas naturales |

---

## 10. Errores Comunes a Evitar

```
1. ❌ Construir antes de tener fonología completa
     → Terminas reescribiendo todo

2. ❌ Inventar palabras copiando el inglés
     → El idioma suena inglés con máscara

3. ❌ No definir qué combinaciones de sonidos son válidas
     → Fonotáctica inconsistente

4. ❌ Crear un idioma sin un propósito cultural
     → Lenguaje vacío, sin alma

5. ❌ No tener suficientes palabras compuestas
     → Idioma que no puede expresar ideas complejas

6. ❌ Usar el mismo sistema gramatical que el inglés
     → Si tu cultura es diferente, el idioma debe reflejarlo

7. ❌ Inventar la gramática al mismo tiempo que traduces
     → Inconsistencias garantías

8. ❌ Copiar la fonología de un idioma real sin cambios
     → Esto es aceptable si es intencional (por ejemplo,
       un idioma de Klingon que es klingon, pero un conlang
       derivado del inglés no tiene excusa)
```

---

---

### Principio Japonés — Palabras Compuestas Transparentes

Inspirado en la construcción de palabras del japonés: **si una palabra puede formarse de dos raíces simples y cortas, es MEJOR que una palabra única oscura.**

```
REGLA: Si puedes expresar un concepto con DOS raíces simples (1-2 sílabas cada una)
       Y el significado se entiende instantáneamente al verla
       → USA EL COMPUESTO.

Ejemplos IDEALES:
  watchman  = wotc-man   → ya sabes qué significa sin buscarlo ✅
  household = haus-kel  → transparente ✅
  sunlight  = sun-lait  → transparente ✅

Contra-ejemplos (palabras simples pero opacas):
  polise    → no hint de lo que significa para un nuevo hablante ⚠️
  ofis      → solo alguien que sepa VELA entiende
  student   → requiere memorización completa de memoria ❌

Excepciones válidas:
  Palabras muy frecuentes ( >5x por día): usar forma corta aunque sea opaca
    mi, yu, li, wi, de, la, un, bi, si, go, wok, kom, her, fel, luk
```

**¿Por qué esto importa?**
- Reduce la carga de memorización global
- Hace el idioma predecible: "puedo adivinar palabras nuevas"
- Los compuestos VELA suenan naturales y lógicos
- Personas encuentran satisfacción en descifrar compuestos

**Límites del principio:**
- Máximo 2 raíces por defecto en compuesto
- Máximo 4 sílabas totales en un compuesto
- Si excede → abreviar o buscar alternativa
- Orden del compuesto: concepto general primero, modificador después
  - wotc-man (man que watches) ← correcto
  - man-wotc ← confuso

**Las excepciones son las palabras de alta frecuencia** (los 20-30 pronombres, verbos y artículos más comunes): estas ya son cortas y se memorizan rápido, no necesitan ser compuestas.

*Esta Knowledge Base fue compilada usando The Language Construction Kit © Mark Rosenfelder (zompist.com), Conlanging 101 (conlang.org), Wikibooks Conlang, y recursos de comunidades de conlangs.*
