# web-sample

App React (Vite) para leer poemas/cuentos VELA y escuchar audio por texto.

## Ejecutar

```bash
npm --prefix web-sample install
npm run web:dev
```

Build:

```bash
npm run web:build
npm run web:preview
```

## Contenido

El índice está en `public/content/index.json` y cada item usa:

- `id`
- `title`
- `type` (`poem` | `story`)
- `description`
- `textPath`
- `audioPath` (opcional)

## Conectar audios de Piper

Flujo recomendado (desde raíz):

```bash
set -a; source packages/vela-tts-piper/.env; set +a
npm run tts:vela:batch-and-sync
```

Esto:
1. genera WAVs desde el índice,
2. y los copia automáticamente a `web-sample/public/audio/`.

Si no existe audio, la app sigue funcionando en modo lectura y muestra "audio no disponible".
