## Context

El repositorio contiene contenido lingüístico y literario de VELA, pero no existe una app web demostrativa para lectura + escucha. Ya se inició un subproyecto TTS con Piper para generación de audio, por lo que la muestra web debe consumir audios pre-generados y no bloquearse por pipeline de síntesis en tiempo real.

Restricciones clave:
- Mantener la app simple, local-first y portable.
- Evitar backend nuevo para el MVP.
- Permitir que nuevos textos/audios se agreguen sin tocar lógica React.

## Goals / Non-Goals

**Goals:**
- Crear `web-sample/` con React para listar poemas y cuentos.
- Permitir lectura completa de cada texto con metadatos básicos.
- Reproducir audio asociado por texto con controles mínimos (play/pause/progreso).
- Definir contrato de contenido (JSON) para mapear texto ↔ audio.

**Non-Goals:**
- No se implementa generación TTS en runtime desde la UI.
- No se implementa autenticación, multiusuario ni backend persistente.
- No se busca editor de textos ni CMS.

## Decisions

1. **Frontend stack: React + Vite (JavaScript)**
   - **Why**: arranque rápido, DX simple, mínimo overhead para sample.
   - **Alternatives considered**:
     - Next.js: más pesado para un MVP estático.
     - Vanilla JS: menos mantenible para vistas y estado de reproducción.

2. **Modelo de datos estático en `public/content/index.json` + archivos de texto/audio**
   - **Why**: permite publicar sin backend y mantener ingestión manual clara.
   - **Alternatives considered**:
     - Parseo directo de markdown del repo en runtime: complejidad extra y dependencias.
     - API server local: agrega superficie innecesaria para muestra.

3. **Reproductor nativo HTML5 audio con control React**
   - **Why**: confiable, accesible, sin dependencia externa pesada.
   - **Alternatives considered**:
     - Librerías de audio completas (wavesurfer/react-player): sobre-dimensionado para MVP.

4. **Estructura por tipo de texto (`poem`, `story`) con rutas uniformes**
   - **Why**: facilita filtros en UI y expansión futura.
   - **Alternatives considered**:
     - Taxonomía libre por etiquetas solamente: menos predecible para navegación inicial.

## Risks / Trade-offs

- **[Riesgo] Audios faltantes o rutas inválidas** → **Mitigación**: validación de índice al cargar y estado UI “audio no disponible”.
- **[Riesgo] Contenido inconsistente (metadata incompleta)** → **Mitigación**: esquema mínimo obligatorio (`id`, `title`, `type`, `textPath`, `audioPath`).
- **[Trade-off] Sin backend no hay sincronización automática con nuevos textos del repo** → **Mitigación**: script de actualización posterior en iteración siguiente.

## Migration Plan

1. Crear `web-sample/` con estructura React/Vite.
2. Definir contrato JSON de contenido y cargar muestras existentes.
3. Implementar lista, detalle de lectura y reproductor.
4. Documentar flujo de añadir nuevos textos y audios.
5. Validar UX local y dejar listo para evolución (por ejemplo ingestión automática).

Rollback: eliminar carpeta `web-sample/` y referencias de workspace/scripts si el experimento no cumple objetivos.

## Open Questions

- ¿Qué textos exactos del repo se consideran “fuente oficial” para el índice inicial?
- ¿Se desea autoplay al abrir un texto o reproducción manual únicamente?
- ¿Se incorporará resaltado por línea/sincronía texto-audio en una fase posterior?
