## Why

El pipeline TTS de VELA genera audio con pronunciación inglesa porque Piper recibe el texto crudo sin conversión fonémica activa. El modo `phoneme` existe en el código pero está desactivado por defecto, y aun cuando se activa, el diccionario y el G2P emiten formatos incompatibles con lo que Piper realmente espera (espeak-ng notation).

## What Changes

- **Activar modo fonémico por defecto**: cambiar `PIPER_INPUT_MODE` default de `text` a `phoneme`
- **Reescribir `g2p.js`**: emitir espeak-ng phoneme notation en lugar de IPA estándar (e.g. `ʃ` → `S`, `tʃ` → `tS`, `ŋ` → `N`)
- **Migrar `vela-dictionary.json`**: convertir valores de notación silábica (`ha.lo`) a espeak-ng phonemes (`h a . l o`)
- **Expandir el diccionario**: el corpus tiene 168 palabras únicas; el diccionario actual cubre solo 29
- **Definir mapa canónico VELA → espeak-ng**: documento de referencia con los 18 fonemas consonánticos y 5 vocálicos de VELA mapeados a sus equivalentes espeak-ng

## Capabilities

### New Capabilities
- `vela-phoneme-map`: Mapa canónico de los 23 fonemas de VELA a espeak-ng notation, derivado de `PHONOLOGY_FINAL.md`
- `vela-g2p-espeak`: G2P reescrito que emite espeak-ng phonemes válidos para Piper `--phoneme_input`
- `vela-dictionary-espeak`: Diccionario expandido (~168 palabras) en formato espeak-ng

### Modified Capabilities
- `corpus-normalization`: el pipeline de síntesis cambia su output format de texto plano a espeak-ng phonemes

## Impact

- `packages/vela-tts-piper/src/vela/g2p.js` — reescritura completa del motor G2P
- `packages/vela-tts-piper/data/vela-dictionary.json` — migración de formato + expansión
- `packages/vela-tts-piper/.env.example` — `PIPER_INPUT_MODE=phoneme` como default
- `packages/vela-tts-piper/src/vela/pipeline.js` — sin cambios estructurales; el default de modo se mueve al `.env`
- `docs/phonology/PHONOLOGY_FINAL.md` — sin cambios; es la fuente de verdad del mapa fonémico
- Sin breaking changes en la API pública del pipeline (`synthesizeVelaText`, `synthesizeVelaFile`)
