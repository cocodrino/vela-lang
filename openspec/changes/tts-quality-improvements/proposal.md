## Why

Los audios generados con `en_US-lessac-medium` suenan artificiales porque el modelo inglés produce diptongos (`o→oʊ`, `e→eɪ`) y una `r` retrofleja que no existen en VELA. La fonología española (5 vocales puras, `r` alveolar) es casi idéntica a la de VELA. Además, sintetizar párrafos enteros en una sola llamada produce prosodia plana; dividir por oración permite al modelo generar curvas de entonación naturales.

## What Changes

- **Modelo español**: reemplazar `en_US-lessac-medium` por `es_ES-mls-medium` (o similar) en `.env.example` y documentación
- **Mapa de fonemas**: ajustar `VELA_TO_IPA` en `g2p.js` para que los símbolos IPA coincidan con el phoneme_id_map del modelo español
- **Síntesis por oración**: dividir el string de fonemas por `|||` (fin de oración) y sintetizar cada oración en una llamada separada a `phoneme_ids_to_audio`, concatenando el audio resultante con silencios apropiados
- **Actualizar diccionario**: regenerar `vela-dictionary.json` con los fonemas IPA compatibles con el nuevo modelo
- **Regenerar todos los audios** del corpus con el nuevo pipeline

## Capabilities

### New Capabilities
- `vela-tts-spanish-model`: configuración y mapa de fonemas para el modelo español de Piper

### Modified Capabilities
- `corpus-normalization`: el sintetizador ahora procesa oraciones individualmente en lugar de párrafos completos

## Impact

- `packages/vela-tts-piper/src/vela/g2p.js` — ajuste de mapa IPA al modelo español
- `packages/vela-tts-piper/data/vela-dictionary.json` — regeneración con nuevos fonemas
- `packages/vela-tts-piper/scripts/synthesize-phonemes.py` — lógica de split por oración
- `packages/vela-tts-piper/.env.example` — `PIPER_MODEL` apunta al modelo español
- `packages/vela-tts-piper/voices/` — descarga del modelo español `.onnx` + `.json`
- `web-sample/public/audio/` — 4 audios regenerados
