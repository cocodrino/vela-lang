# VELA Corpus — Palabras para Revisión del Comité

**Fecha**: 2026-05-28
**Corpus analizado**: 4 textos (`poem-laif-biutifl.txt`, `poem-pis-hope.txt`, `story-lumina-bridge.txt`, `story-song-teacher.txt`)

## Resumen

| Categoría | Cantidad |
|---|---|
| Palabras únicas totales | 167 |
| Ya en diccionario (necesitan corrección de fonemas solamente) | 23 |
**Nuevas / No en diccionario** | **144** |

## Palabras conocidas (23)

Estas ya están en `vela-dictionary.json` pero sus fonemas están mal formateados (pseudo-IPA). Se corregirán sin necesidad de comité:

`bat`, `biutifl`, `es`, `evri`, `go`, `halo`, `hop`, `in`, `ke`, `kin`, `la`, `laif`, `li`, `liv`, `man`, `mi`, `no`, `pis`, `sai`, `short`, `wan`, `wi`, `yu`

## Palabras nuevas (144)

Estas NO están en el diccionario y necesitan decisión del comité sobre **pronunciación IPA** antes de ser incluidas en el pipeline TTS:

### Del primer texto (La Laif Es Short Bat Biutifl)
`a`, `agen`, `alone`, `an`, `are`, `ask`, `become`, `before`, `bi`, `biuti`, `biutifl`, `brij`, `chalk`, `chans`, `class`, `clear`, `cut`, `dark`, `dat`, `dei`, `dem`, `desin`, `diferent`, `doctor`, `dor`, `dui`, `faal`, `fade`, `farmer`, `fear`, `first`, `for`, `frendship`, `from`, `gift`, `glow`, `grow`, `han`, `hart`, `heavy`, `hi`, `hir`, `hungr`, `if`, `joy`, `just`, `kam`, `kind`, `king`, `kri`, `lait`, `lamp`, `lav`, `law`, `lern-po`, `lisn`, `lit`, `long`, `luk`, `lumina`, `maker`, `market`, `metal`, `mit`, `moning`, `nait`, `nem`, `nord`, `old`, `on`, `one`, `open`, `over`, `pan`, `parent`, `pas`, `people`, `por`, `put`, `remember`, `rise`, `rivera`, `room`, `sed`, `sem`, `sevn`, `sher`, `si`, `silent`, `simple`, `singer`, `sink`, `siti`, `siti-to`, `ski`, `slowli`, `smiled`, `smol`, `sol`, `som`, `song`, `speech`, `stand`, `stept`, `stil`, `ston`, `stop`, `storm`, `student`, `sud`, `sun`, `tabel`, `taim`, `teach`, `thirty`, `tok`, `tri`, `true`, `tugeter`, `turn`, `un`, `voice`, `vois`, `vok`, `wal`, `war`, `warm`, `when`, `win`, `with`, `wod`, `wok`, `words`, `yer`, `yers`, `yes`, `yong`

### Observaciones para el comité
- Variantes morfológicas: `biuti` (raíz de `biutifl`?), `siti` / `siti-to` (sufijo `-to` = "pequeño/lugar"?), `bi-ed` (compuesto?)
- Compuestos: `lern-po` (aprender-persona = maestro?), `siti-to` (ciudad-pequeña?)
- Derivados: `slowli` (¿adverbio de `slow`?), `smiled` (¿pasado de `smile`?)

## Propuesta de decisión

**Opción A**: El comité revisa las 144 palabras y asigna fonemas IPA. Luego implementamos.
**Opción B**: Creamos un subconjunto mínimo (~50 palabras más frecuentes) para el MVP de audio, y el resto se revisa luego.
**Opción C**: El comité decide que algunas de estas palabras NO son VELA válido y se deben reescribir los textos del corpus.

---

*Generado automáticamente desde el análisis del corpus para el change `fix-vela-tts-pronunciation`.*
