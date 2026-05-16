## Why

Necesitamos una muestra funcional que demuestre el valor práctico de VELA: leer poemas y cuentos del repositorio y escucharlos con audio. Esto acelera validación de UX, pruebas de pronunciación y reutilización del subproyecto TTS.

## What Changes

- Crear `web-sample/` como app React para explorar textos de VELA.
- Mostrar listado de poemas y cuentos con vista de lectura por ítem.
- Incluir reproductor de audio por texto (play/pause/progreso) usando archivos generados externamente.
- Definir formato de contenido y metadatos para mapear texto + audio.
- Documentar flujo local para ejecutar la app con contenido y audios.

## Capabilities

### New Capabilities
- `web-sample-reading-library`: Navegación y lectura de poemas/cuentos desde contenido del proyecto.
- `web-sample-audio-playback`: Reproducción de audio asociado a cada texto con controles básicos.
- `web-sample-content-index`: Índice estructurado de textos y rutas de audio consumible por la app.

### Modified Capabilities
- Ninguna.

## Impact

- Nuevos archivos en `web-sample/` (app React, componentes, estilos, configuración).
- Nuevos archivos de contenido/índice para poemas y cuentos (por ejemplo bajo `web-sample/public/` o `texts/`).
- Integración de dependencia React/tooling (Vite o equivalente).
- Documentación de uso en README del subproyecto y/o raíz.
