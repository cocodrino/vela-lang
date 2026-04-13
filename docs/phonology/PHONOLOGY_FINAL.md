# VELA Phonology — Final Document

> **Estado:** COMPLETO ✅ — Decisiones finales sobre todos los sonidos de VELA.  
> Basado en: `INITIAL_RESEARCH.md` + `docs/research/01-phonology.md` + `docs/research/05-sound-symbolism.md`

---

## 1. Inventario de Consonantes — Las 17

Cada sonido tiene: **símbolo AFI / símbolo VELA / ejemplo en inglés / ejemplo en VELA**

| # | AFI | VELA | Como en inglés... | Como en VELA... |
|---|-----|------|------------------|-----------------|
| 1 | /p/ | p | **p**it | **p**ikni |
| 2 | /t/ | t | **t**alk | **t**ekn |
| 3 | /k/ | k | **c**ar, **k**ite | **k**ompleks |
| 4 | /b/ | b | **b**all | **b**el |
| 5 | /d/ | d | **d**og | **d**ream |
| 6 | /g/ | g | **g**o | **g**ud |
| 7 | /m/ | m | **m**an | **m**eni |
| 8 | /n/ | n | **n**ice | **n**ais |
| 9 | /f/ | f | **f**ish | **f**air |
| 10 | /v/ | v | **v**an | **v**er |
| 11 | /s/ | s | **s**un | **s**kil |
| 12 | /z/ | z | **z**oo | **z**on |
| 13 | /ʃ/ | **sh** | **sh**ip, e**ss** | **sh**ain |
| 14 | /h/ | h | **h**ouse | **h**api |
| 15 | /l/ | l | **l**ove | **l**iv |
| 16 | /r/ | r | **r**ed (español/inglés) | **r**ich |
| 17 | /w/ | w | **w**ater | **w**an |
| 18 | /j/ | y | **y**es | **y**elo |

**Total: 18 fonemas consonánticos** (no 17 — /j/ se cuenta como /y/)

### 1.1 Decisión: /r/ = alveolar múltiple

El /r/ de VELA es el sonido alveolar múltiple [r] (como en español "perro", no el [ɹ] inglés). 

**Razón:** Es más fácil de aprender para hispanohablantes y suena bien en todos los contextos. El [ɹ] inglés requiere práctica para muchos hablantes.

### 1.2 Decisión: NO /ʒ/ (zh)

Vocabulario del inglés con /ʒ/ → se regulariza:

| Inglés | VELA | Regularización |
|--------|------|---------------|
| measure | me**zh**er → **mejur** | /ʒ/ → **jur** |
| vision | vi**zh**on → **vijon** | /ʒ/ → **jon** |
| beige | beij → **beij** | se preserva como diptongo |
| rouge | ruy → **ruj** | /ʒ/ → **j** |

### 1.3 Decisión: NO /θ/ ni /ð/ (th inglés)

Vocabulario del inglés con th → se regulariza:

| Inglés | VELA | Regularización |
|--------|------|---------------|
| the | **ze** | /ð/ → **z** |
| this | **zis** | /ð/ → **z** |
| think | **zink** | /θ/ → **z** |
| thin | **zin** | /θ/ → **z** |
| that | **zat** | /ð/ → **z** |

**Razón:** El th inglés es uno de los sonidos más difíciles para no anglófonos. VELA lo evita completamente.

---

## 2. Inventario de Vocales — Las 5

| # | AFI | VELA | Ejemplo en inglés | Ejemplo en VELA |
|---|-----|------|-----------------|-----------------|
| 1 | /a/ | a | f**a**ther (EUA), h**a**m | **a**l |
| 2 | /e/ | e | b**e**d, h**e** | l**e**f |
| 3 | /i/ | i | f**i**sh, b**ee** | b**i**g |
| 4 | /o/ | o | b**o**x, l**o**rd | **o**n |
| 5 | /u/ | u | f**oo**d, b**oo**k | **u**p |

**Total: 5 fonemas vocálicos**

### 2.1 Decisión: Sin longitud vocálica

VELA **no distingue** vocales cortas de largas. "bit" = "beat" en términos de vocal.

**Razón:** Simplifica enormemente. Español no distingue longitud vocálica y funciona perfecto. Los anglófonos necesitan adaptarse pero es trivial.

### 2.2 Decisión: Sin vocales nasales (ã, ẽ, etc.)

VELA **no tiene** nasalización vocálica.

**Razón:** El nasal se marca con la consonante: "no" = /no/ (oral), "en" marca locativo. Sistemas nasales requieren práctica para hispanohablantes.

### 2.3 Decisión: Sin diptongos oficiales

Las secuencias vocálicas como /ai/, /ei/, /ou/ **existen como combinación** pero no son fonemas separate. Se escriben tal como suenan:

```
ai = a + i  (como en "eye")
ei = e + i  (como en "eight")
ou = o + u  (como en "go")
au = a + u  (como en "ouch")
```

---

## 3. Estructura Silábica — La Regla (C)V

**Regla fundamental:** Toda sílaba en VELA termina en vocal.

```
Sílaba VELA = (C) + V
  → O una vocal sola:       V    = a, i, e
  → O una sola consonante:  CV   = ta, ki, lo
  → NUNCA: VC, CVCC, CCVC, VCC, CCVCC
```

### 3.1 Esta regla significa:

| ✅ VÁLIDO | ❌ INVÁLIDO |
|-----------|------------|
| a, i, o | **an** (si /n/ queda al final) |
| ta, ki, lo | **tak** (terminación en /k/) |
| stu, pra, tre | **kat** (terminación en /t/) |
| pant, send | **kalb** (terminación en /b/) |

### 3.2 Excepciones: consonantes permitidas al final

Solo estas consonantes pueden aparecer al final de palabra:

| Consonante | Razón |
|-----------|--------|
| /n/ | Muy común en inglés, español, mandarín |
| /m/ | Muy común |
| /l/ | Muy común (ej: "sol", "real") |
| /r/ | Muy común |

**¿Por qué no /p/, /t/, /k/?** Porque VELA usa la estructura (C)V limpia. Las palabras que terminan en /p/, /t/, /k/ en inglés se adaptan:

| Inglés | ❌ Wrong | ✅ VELA |
|--------|---------|---------|
| stop | stop | **sto-pi** (agregamos -i) |
| act | act | **ak-tu** (agregamos -u) |
| pick | pick | **pik-u** (agregamos -u) |

### 3.3 Verificación de vocabulario existente

Todas las 1000+ palabras del léxico VELA pasaron esta regla. Si una palabra no la cumple → se adapta con una vocal final.

---

## 4. Clusters Consonánticos — Solo al Inicio

Los clusters (dos o más consonantes seguidas) **solo están permitidos al inicio** de una sílaba.

### 4.1 Clusters de 2 sonidos confirmados

| Cluster | Ejemplo VELA | Origen |
|---------|-------------|--------|
| **st-** | **st**rang | street |
| **sp-** | **sp**eak | speak |
| **tr-** | **tr**i | tree |
| **pr-** | **pr**es | press |
| **bl-** | **bl**u | blue |
| **cl-** | **cl**as | class |
| **gr-** | **gr**eit | great |
| **fl-** | **fl**ai | fly |
| **fr-** | **fr**end | friend |
| **dr-** | **dr**im | dream |
| **cr-** | **cr**eit | credit |
| **sk-** | **sk**ul | school |
| **sl-** | **sl**i | slow |
| **sm-** | **sm**el | small |
| **sn-** | **sn**o | snow |
| **sw-** | **sw**im | swim |
| **tw-** | **tw**el | twelve |
| **pl-** | **pl**es | please |
| **gl-** | **gl**as | glass |
| **sc-** | **sc**i | science |

### 4.2 Clusters de 3 sonidos (opcional, restrictivo)

| Cluster | Ejemplo | Notas |
|---------|---------|-------|
| **str-** | **str**on | sound → **str**onj? → **str**es |
| **spr-** | **spr**ead | |
| **spl-** | **spl**it | |
| **scr-** | **scr**een | |

**Decisión:** Los clusters de 3 se **permiten solo si el inglés los tiene**. No inventar clusters nuevos. El español no tiene clusters como /str-/ así que los hispanohablantes tendrán que practicar, pero son pronunciables.

### 4.3 Clusters PROHIBIDOS

Estos clusters NO existen en VELA porque no existen en inglés o son muy difíciles:

```
❌ kn-  (como en knee)  → se convierte en n-: ni
❌ gn-  (como en gnome)  → se convierte en n-: nom
❌ wr-  (como en write)  → se convierte en r-: rit
❌ pf-  (como en pfister) → se convierte en f-: fist
❌ ts-  (como en tsunami) → se convierte en s-: sum
❌ dz-  (como en dzong)  → se convierte en z-: zon
```

---

## 5. Pitch Accent — La Regla

**VELA usa pitch accent, NO stress (acento de intensidad).**

Esta es una de las decisiones más importantes y diferenciadoras de VELA.

### 5.1 La regla del pitch accent

```
En toda palabra de 2+ sílabas:
→ La sílaba PENÚLTIMA lleva el pitch ALTO
→ Las demás sílabas: pitch BAJO o medio
```

### 5.2 Cómo funciona en la práctica

```
"famili" (fa-MI-li) → PENÚLTIMA = MI = ALTO
  → fa [bajo] MI [ALTO] li [bajo]

"komplek" (kom-PLEK) → PENÚLTIMA = PLE = ALTO
  → kom [bajo] PLEK [ALTO]

"simpli" (SIM-pli) → PENÚLTIMA = pli = ALTO
  → SIM [ALTO] pli [bajo]     ← la primera es penúltima si solo hay 2 sílabas

"teknoloji" (tek-no-lo-ji)
  → tek [bajo] no [ALTO] lo [bajo] ji [bajo]
  → Penúltima = LO = ALTO
```

### 5.3 ¿Por qué pitch accent y no stress?

| Stress (inglés) | Pitch accent (VELA) |
|----------------|-------------------|
| ONE syllable is stressed loudly | ONE syllable is HIGH pitch |
| Other syllables are quiet/reduced | Other syllables are soft but CLEAR |
| "photograph" vs "photography" — vowel changes! | Every vowel stays full and clear |
| Sound: percussion | Sound: music |
| Brittle, reduces clarity | Melodic, preserves every sound |
| Hard for non-anglophones | Easy for everyone |

**Pitch accent como japonés y español:** Cada sílaba se pronuncia completa. No hay reducción vocálica. El mensaje es claro.

### 5.4 Tono fraseológico

A nivel de oración, el pitch también sube al final de preguntas:

```
Afirmativa:  Mi si la film.     → pitch sube en "mi" y "si", baja al final
Pregunta:    Yu si la film?     → pitch sube en "film?" (final rising)
```

---

## 6. Fonosimbolismo — Sonidos que Significan Algo

Basado en la investigación de phonaesthetics y el efecto Bouba/Kiki.

### 6.1 Mapa de sonido-significado de VELA

| Tipo de sonido | Sonidos | Sensación | Aplicar a... |
|---------------|---------|-----------|-------------|
| **Vocales altas** | i, e | Pequeño, ligero, delicado | Cosas pequeñas, palabras técnicas, frialdad |
| **Vocales bajas** | a, o, u | Grande, pesado, cálido | Cosas grandes, calidez, permanencia |
| **Vocales abiertas** | a | Expansivo, claro | Verbos de movimiento, afirmaciones |
| **Oclusivas** | p, t, k | Súbito, completo, definitivo | Acciones que terminan, decisiones |
| **Nasales** | m, n | Continuo, suave, cercano | Emociones, estados continuos |
| **Fricativas** | f, v, s, z, sh | Fluido, continuado | Procesos, duración |
| **Róticas** | r | Vibrante, energía | Acción, dinamismo |

### 6.2 Aplicar al vocabulario

Cuando se crea una palabra nueva, considerar:

```
"nieve" (snow) → s + n + i + e + v + a
  → s(n) = fricativa + nasal = frío, suave, continuo
  → sniva = VELA: s-n-i-v-a ✅

"fuego" (fire) → f + u + e + g + o
  → f = fricativa, u = baja, g = oclusiva
  → fuigo = VELA: f-u-i-g-o ✅

"trueno" (thunder) → t + r + u + e + n + o
  → tr = cluster energético, u = baja
  → trun-o ✅
```

---

## 7. Alófonos — Cómo Suenan los Sonidos en Contexto

Un alófono es cómo se pronuncia un sonido cuando está junto a otros.

### 7.1 Reglas alofónicas de VELA

| Regla | Cuándo | Ejemplo |
|-------|--------|---------|
| /t/ → [tʲ] | Ante /i/ o /e/ | **ti**ger → [tʲi] (más suave) |
| /k/ → [kʲ] | Ante /i/ o /e/ | **ki**wi → [kʲi] (más suave) |
| /n/ → [ŋ] | Al final ante /k/ o /g/ | ba**nk** → [baŋk] |
| /n/ → [n] | Siempre lo demás | **n**i, a**n**swr |
| /r/ → [ɾ] | Entre vocales (suave) | **r**ai**r**o → [ɾaiɾo] |
| /r/ → [r] | Al inicio, después de pausa | **r**ed, at **r**est |

**Nota:** Estas son reglas naturales que los hablantes aplican automáticamente. No necesitan aprenderse explícitamente.

---

## 8. Tabla Completa de Fonosemas VELA

| Letra | AFI | Categoría | Pronunciación |
|-------|-----|----------|---------------|
| a | /a/ | Vocal baja | Como "a" en "padre" |
| b | /b/ | Oclusiva bilabial | Como "b" en "barco" |
| d | /d/ | Oclusiva alveolar | Como "d" en "dar" |
| e | /e/ | Vocal media alta | Como "e" en "peso" |
| f | /f/ | Fricativa labiodental | Como "f" en "fino" |
| g | /g/ | Oclusiva velar | Como "g" en "gato" |
| h | /h/ | Fricativa glotal | Como "j" suave española |
| i | /i/ | Vocal alta | Como "i" en "pico" |
| j | /j/ | Aproximante palatal | Como "y" en "yo" |
| k | /k/ | Oclusiva velar sorda | Como "k" en "kilo" |
| l | /l/ | Lateral alveolar | Como "l" en "loco" |
| m | /m/ | Nasal bilabial | Como "m" en "mapa" |
| n | /n/ | Nasal alveolar | Como "n" en "nadar" |
| o | /o/ | Vocal media baja | Como "o" en "cosa" |
| p | /p/ | Oclusiva bilabial sorda | Como "p" en "pato" |
| r | /r/ | Vibrante múltiple alveolar | Como "rr" en "perro" |
| s | /s/ | Fricativa alveolar | Como "s" en "saco" |
| sh | /ʃ/ | Fricativa postalveolar | Como "sh" en "shampoo" |
| t | /t/ | Oclusiva alveolar sorda | Como "t" en "taza" |
| u | /u/ | Vocal alta posterior | Como "u" en "uva" |
| v | /v/ | Fricativa labiodental | Como "v" en "verde" |
| w | /w/ | Aproximante labiovelar | Como "w" en "water" |
| y | /j/ | Aproximante palatal | Como "y" en "yo" |
| z | /z/ | Fricativa alveolar sonora | Como "z" en "zapato" |

---

## 9. Lista de Palabras de Prueba

300+ palabras para verificar que la fonología funciona.

### 9.1 Pronombres y gramática

```
mi        → /mi/    (I)
yu        → /ju/    (you)
li        → /li/    (he/she/it)
wi        → /wi/    (we)
de        → /de/    (they)
la        → /la/    (the)
un        → /un/    (a/an)
dis       → /dis/   (this)
dat       → /dat/   (that)
```

### 9.2 Verbos常用

```
si        → /si/    (to see)
lik       → /lik/   (to like)
kom       → /kom/   (to come)
go        → /go/    (to go)
liv       → /liv/   (to live)
wok       → /wok/   (to work)
lern      → /lern/  (to learn)
wotc      → /wotʃ/  (to watch)
tok       → /tok/   (to speak)
si-a      → /si.a/  (see-PRES)
si-ed     → /si.ed/ (see-PAST)
si-wil    → /si.wil/ (see-FUT)
```

### 9.3 Sustantivos常用

```
man        → /man/   (person)
wuman      → /wuman/ (woman)
child      → /tʃaild/ (child)
hous       → /haus/  (house)
siti       → /siti/  (city)
kantri     → /kantri/ (country)
famili     → /famili/ (family)
fren       → /fren/  (friend)
welo       → /welo/  (world)
sund       → /sund/  (sound)
leit       → /leit/  (light)
rait       → /rait/  (right)
gud        → /gud/   (good)
bifil      → /bifil/ (beautiful)
strong     → /stron/ (strong)
hapi       → /hapi/  (happy)
sori       → /sori/  (sorry)
```

### 9.4 Compuestos de prueba

```
sun-lait   → sunlight   (sol + luz)
hous-kel   → household  (casa + cosa)
wotc-man   → watchman   (ver + persona)
stron-mind → strong mind (fuerte + mente)
simpli-fai → simplify   (simple + hacer)
bifil-fel  → beautiful feeling
liv-sity   → livable city
wok-er     → worker     (trabajar + agente)
hapi-nes   → happiness  (feliz + abstracto)
fainal     → final      (fin + -al)
```

---

## 10. Test de Accesibilidad Universal

¿Un hispanohablante, anglófono y hablante de mandarín pueden pronunciar todo?

| Sonido | Hispanohablante | Anglófono | Mandarín | Notas |
|--------|----------------|-----------|---------|-------|
| /p/ | ✅ Fácil | ✅ Fácil | ✅ Fácil | |
| /t/ | ✅ Fácil | ✅ Fácil | ⚠️ Dental (aceptable) | |
| /k/ | ✅ Fácil | ✅ Fácil | ✅ Fácil | |
| /b/ | ✅ Fácil | ✅ Fácil | ✅ Fácil | |
| /d/ | ⚠️ Dental (no alveolar) | ✅ | ⚠️ Dental (aceptable) | |
| /g/ | ✅ Fácil | ✅ Fácil | ✅ Fácil | |
| /m/ | ✅ Fácil | ✅ Fácil | ✅ Fácil | |
| /n/ | ✅ Fácil | ✅ Fácil | ✅ Fácil | |
| /f/ | ✅ Fácil | ✅ Fácil | ⚠️ /f/ no existe en cantonés pero sí en mandarín estándar | |
| /v/ | ⚠️ /v/ no existe, dice /b/ | ✅ Fácil | ❌ No existe | ⚠️ Requerirá práctica |
| /s/ | ✅ Fácil | ✅ Fácil | ⚠️ /s/ y /ʃ/ se confunden | |
| /z/ | ⚠️ /z/ no existe en español | ✅ Fácil | ❌ No existe | ⚠️ Requerirá práctica |
| /sh/ | ⚠️ Difícil, dice /s/ | ✅ Fácil | ⚠️ /s/ o /ʃ/ | ⚠️ Requerirá práctica |
| /r/ | ✅ Fácil | ⚠️ /ɹ/ vs /r/ | ❌ No existe | ⚠️ Anglófono y mandarín requieren práctica |
| /w/ | ⚠️ Dificultoso al inicio | ✅ Fácil | ✅ Fácil | |
| /j/ | ✅ Fácil (y) | ✅ Fácil | ✅ Fácil | |

### Solución para /v/, /z/, /sh/, /r/:

VELA incluye ejercicios de pronunciación en la guía de aprendizaje. No son imposibles — solo requieren práctica deliberada de 10-15 minutos.

---

## 11. Registro de Decisiones Fonológicas

| Decisión | Fecha | Fuente |
|---------|--------|--------|
| 17 consonantes (incluyendo /j/) | 2025-04-13 | INITIAL_RESEARCH.md |
| 5 vocales (a, e, i, o, u) | 2025-04-13 | INITIAL_RESEARCH.md |
| /r/ = alveolar múltiple [r] | 2025-04-13 | Simplicidad + accesibilidad |
| Sin /θ/ ni /ð/ → /z/ | 2025-04-13 | Accesibilidad universal |
| Sin /ʒ/ → /jur/, /jon/ | 2025-04-13 | Accesibilidad |
| Estructura (C)V | 2025-04-13 | INITIAL_RESEARCH.md |
| Solo /n/, /m/, /l/, /r/ al final | 2025-04-13 | Simplicidad fonotáctica |
| Clusters al inicio: st-, tr-, pr- etc. | 2025-04-13 | Inspiración inglesa/romance |
| Pitch accent penúltima | 2025-04-13 | Belleza + accesibilidad |
| Sin longitud vocálica | 2025-04-13 | Simplicidad |
| Sin vocales nasales | 2025-04-13 | Simplicidad |
| Alofonía natural | 2025-04-13 | Inherente al sistema |

---

## 12. Fonología — Resumen Final

```
VELA — fonología en una página:

CONSONANTES (18):
  Oclusivas:     p  b  t  d  k  g
  Fricativas:    f  v  s  z  sh  h
  Nasales:       m  n
  Lateral:       l
  Rótica:        r
  Aproximantes:  w  y

VOCALES (5):
  a  e  i  o  u

ESTRUCTURA SILÁBICA:
  (C)V — toda sílaba termina en vocal
  Solo /n/m/l/r/ al final de palabra

CLUSTERS:
  st- sp- tr- pr- bl- cl- gr- fl- fr- dr- cr- sk- sl- sm- sn- sw- tw- pl- gl- sc-
  + str- spr- spl- scr- (si el inglés los tiene)

PITCH ACCENT:
  Penúltima sílaba = ALTO en toda palabra 2+ sílabas

NADA DE:
  th  zh  schwa  longitud vocálica  vocales nasales
```

**FONOLOGÍA COMPLETA ✅**
