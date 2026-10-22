# Decisions — fix/corpus-canon-migration

## Motor del comité para la ronda de las 13 palabras
- date: 2026-10-22
- decided_by: user
- chosen: B
- files: vote/topics/current_topic.md

### Context
Quedan 17 errores del validador y todos vienen de 13 palabras inglesas sin forma VELA. Acuñar palabras es decisión del comité (`vote/docs/PROCESS.md`), y ese documento obliga a preguntar con qué motor se corre la deliberación.

### Options
#### A — Agentes Pi por el bridge NATS
Igual que R1–R17: 3 agentes Pi con modelos distintos, 2 rondas, Claude sintetiza.
- Pro: modelos distintos, más desacuerdo real entre voces; coherente con la historia del comité.
- Con: requiere tener los paneles Pi abiertos en cmux.
#### B — Subagentes Claude (Agent tool)
5 especialistas en segundo plano, uno por rol, solo lectura; el orquestador escribe todos los archivos.
- Pro: arranca ya, sin preparación, más confiable.
- Con: todos son la misma familia de modelos, menos diversidad de criterio.

### Reason
El usuario eligió B para arrancar de inmediato. La recomendación era A, por la diversidad de modelos y por coherencia con R1–R17. Se acepta el costo: menos desacuerdo real entre las voces.

## "still" en R18: yeta en vez de stil
- date: 2026-10-22
- decided_by: user
- chosen: B
- files: vote/topics/discussion_plan.md

### Context
La ronda R18 quedó 2-2 para "still" (todavía): `stil` (fonólogo, morfólogo) contra `yeta` (semantista, esteticista); el lexicógrafo propuso `jeta`. Por las reglas, el empate lo rompe el esteticista, que votó `yeta`.

### Options
#### A — stil
Anular el desempate y corregir solo la ortografía del corpus (`still` → `stil`).
- Pro: cero palabras nuevas; `stil` ya se usa con ese sentido en `LEXICON_EXPANSION.md:552` y `:889`; `/l/` es coda blanda, así que no choca con `stila` (robar).
- Con: pasa por encima de la regla de desempate.
#### B — yeta
Respetar el desempate al pie de la letra.
- Pro: aplica las reglas de `PROCESS.md` sin excepción; forma abierta y simétrica con `olredi`.
- Con: palabra nueva; hay que reescribir los ejemplos del léxico que usan `stil`; los votos por `yeta` se apoyaban en un choque con `stila` que dos especialistas mostraron inexistente.

### Reason
El usuario eligió B. La recomendación era A, porque la premisa de los votos por `yeta` estaba refutada y `stil` ya existía en el léxico.

## "solitude" en R18: alon-nes
- date: 2026-10-22
- decided_by: user
- chosen: A
- files: vote/topics/discussion_plan.md

### Context
"solitude" no tuvo mayoría en R18: `alon-nes` 2 votos (semantista, morfólogo), y `sola-taim`, `sola-nes` y `solituda` 1 cada una. No era un empate, así que la regla del esteticista no lo resolvía.

### Options
#### A — alon-nes
- Pro: la más votada; cero raíces nuevas (`alon` ya está en `STORIES_SET_01.md:8` y `SHORT_STORY_BIRD.md:75`, `-nes` es productivo); formaliza "alone" de paso.
- Con: el esteticista prefería una palabra de un solo átomo para el poema.
#### B — solituda
- Pro: mejor sonido al cierre del poema, según el esteticista.
- Con: agrega una raíz nueva al núcleo (R1).
#### C — Otra ronda
- Pro: mayoría real.
- Con: unos 5 minutos más y otra ronda de agentes.

### Reason
El usuario eligió A, que era la recomendación: es la más votada y no gasta raíces nuevas.

## Motor del comité para R19 (formas peladas sueltas)
- date: 2026-10-22
- decided_by: user
- chosen: A
- files: vote/topics/dossier_r19_bare_forms.md, vote/topics/current_topic.md

### Context
La migración R8 se detuvo en 308 tokens porque el canon se contradice (tabla de R8 vs R7/léxico). El usuario pidió llevarlo al comité; `PROCESS.md` exige preguntar el motor antes de cada ronda.

### Options
#### A — Subagentes Claude
Igual que R18: 5 especialistas en segundo plano, solo lectura.
- Pro: arranca ya, sin preparación.
- Con: misma familia de modelos, menos desacuerdo real.
#### B — Pi por bridge
- Pro: modelos distintos, como R1–R17.
- Con: requiere abrir los paneles Pi en cmux.

### Reason
El usuario eligió A, que era la recomendación esta vez: R18 funcionó con ese motor y no hay que preparar nada.

## Aplicar R19 en dos tandas
- date: 2026-10-22
- decided_by: user
- chosen: A
- files: scripts/migrate_corpus.py, books/Learning-VELA-Level1.html, docs/texts/STORIES_SET_01.md, docs/grammar/GRAMMAR_COMPLETE.md

### Context
R19 resultó más grande de lo previsto: además de los 308 tokens de corpus y cursos, los ejemplos del propio léxico usan formas peladas (~1.500-1.900 tokens estimados), y el migrador no lee bien las tablas del léxico (13 formatos, celdas en inglés, homógrafos como `not`, `mat`).

### Options
#### A — Dos tandas
Ahora corpus, cursos y gramática con el migrador actual; los ejemplos del léxico después, tras enseñarle al migrador a leer esas tablas.
- Pro: entrega rápida de lo que ya es seguro; el léxico se hace con la herramienta adecuada.
- Con: el diccionario sigue mostrando ejemplos pelados un tiempo.
#### B — Todo de una vez
- Pro: el canon queda coherente en un solo paso.
- Con: riesgo alto de reescribir celdas en inglés u homógrafos en ~1.400 filas sin una herramienta que distinga columnas.

### Reason
El usuario eligió A, que era la recomendación.
