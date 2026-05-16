## 1. Project Setup

- [ ] 1.1 Crear carpeta `web-sample/` con app React (Vite) y scripts de desarrollo/build.
- [ ] 1.2 Conectar `web-sample` al workspace del repo y validar instalación de dependencias.
- [ ] 1.3 Definir estructura base de carpetas (`src`, `public/content`, `public/audio`, `public/texts`).

## 2. Content Contract and Seed Data

- [ ] 2.1 Crear `public/content/index.json` con esquema mínimo (`id`, `title`, `type`, `textPath`, `audioPath`).
- [ ] 2.2 Cargar muestras iniciales de poemas y cuentos en archivos de texto consumibles por la app.
- [ ] 2.3 Añadir validación de carga/parseo del índice con fallback de error en UI.

## 3. Reading Experience

- [ ] 3.1 Implementar vista catálogo con listado de textos y etiqueta de tipo (`poem`/`story`).
- [ ] 3.2 Implementar vista de lectura con título, metadatos y cuerpo completo del texto seleccionado.
- [ ] 3.3 Implementar navegación entre textos sin recarga completa de página.

## 4. Audio Playback

- [ ] 4.1 Implementar reproductor HTML5 con controles play/pause y progreso.
- [ ] 4.2 Manejar estado “audio no disponible” cuando falta `audioPath` o falla la carga.
- [ ] 4.3 Detener reproducción anterior al cambiar de texto para evitar solapamiento.

## 5. Documentation and Verification

- [ ] 5.1 Documentar en `web-sample/README.md` cómo agregar nuevos textos y audios.
- [ ] 5.2 Ejecutar verificación manual: cargar catálogo, abrir textos, reproducir audio, manejar errores.
- [ ] 5.3 Registrar comandos de ejecución local y criterios de aceptación mínimos.
