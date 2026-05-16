# @vela/tts-piper

Librería y CLI para generar audio local con Piper, incluyendo una capa de pronunciación para VELA (diccionario + G2P + prosodia básica).

## Qué incluye

- Wrapper de Piper: `src/piper.js`
- Pipeline VELA: `src/vela/*`
- CLI: `bin/vela-tts.mjs`
- Doctor: `scripts/doctor.mjs`
- Batch: `scripts/synthesize-library.mjs`
- Sync web audio: `scripts/sync-web-audio.mjs`

## Comandos (raíz del repo)

- `npm run tts:setup`
- `npm run tts:doctor`
- `npm run tts:vela:smoke`
- `npm run tts:vela:batch`
- `npm run tts:vela:sync-web-audio`
- `npm run tts:vela:batch-and-sync` ✅ recomendado para web-sample

## Flujo recomendado web-sample

```bash
set -a; source packages/vela-tts-piper/.env; set +a
npm run tts:vela:batch-and-sync
```

Genera WAVs en `packages/vela-tts-piper/output/library/` y los copia a `web-sample/public/audio/`.
