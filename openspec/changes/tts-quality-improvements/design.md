## Context

El pipeline actual usa `en_US-lessac-medium`. Aunque le pasamos IPA correcto, el vocoder del modelo inglés está entrenado para producir los formantes del inglés americano, lo que distorsiona las vocales VELA (especialmente `e`, `o`, `u`). Un modelo español usa los mismos formantes vocálicos que VELA por construcción.

El split por oración resuelve el problema de prosodia plana: `phoneme_ids_to_audio` en una sola llamada con 100+ fonemas produce entonación monótona. Llamadas más cortas (una por oración) permiten al modelo generar curvas de F0 naturales.

**Modelo elegido**: `es_MX-claude-high`
- Español mexicano neutro — sin rasgos regionales marcados
- Calidad `high` (mayor que `medium`)
- Disponible en `rhasspy/piper-voices` en HuggingFace

## Goals / Non-Goals

**Goals:**
- Vocales VELA (`a e i o u`) suenan puras, no como diptongos ingleses
- `r` suena alveolar, no retrofleja
- Cada oración se sintetiza como unidad independiente (mejor prosodia)
- El pipeline sigue siendo el mismo para el usuario (`npm run tts:vela:batch-and-sync`)

**Non-Goals:**
- Entrenar una voz custom para VELA
- Cambiar la arquitectura del pipeline de Node.js
- Soportar múltiples voces simultáneas

## Decisions

### D1: Modelo `es_MX-claude-high`

**Por qué**: Calidad alta, español mexicano neutral. Las vocales `/a e i o u/` y consonantes son las más cercanas a VELA entre los modelos disponibles.

**Alternativas consideradas**:
- `es_AR-daniela-high`: alta calidad pero acento rioplatense puede sonar distante del VELA neutro
- `es_ES-davefx-medium`: calidad media, acento peninsular (ceceo)
- `es_MX-ald-medium`: misma región pero menor calidad

### D2: Split por `|||` — síntesis oración por oración

**Por qué**: El marcador `|||` es producido por `prosody.js` al final de cada oración (`.`, `!`, `?`). Sintetizar cada oración por separado permite al modelo TTS generar la curva de F0 correcta (descenso al final, subida en pregunta, etc.).

**Implementación**: en `synthesize-phonemes.py`, antes del split por `||||` (párrafo), split por `|||` (oración). Cada chunk → llamada separada a `phoneme_ids_to_audio`. Entre oraciones: silencio de 0.3s. Entre párrafos: silencio de 0.6s.

### D3: Verificar phoneme_id_map del modelo español antes de asumir compatibilidad

**Por qué**: El mapa de fonemas puede diferir entre modelos. Antes de generar audios, verificar que los símbolos IPA que usamos (`a e i o u r l m n...`) están presentes en el mapa del modelo español descargado.

Si algún símbolo no está, hacer el ajuste mínimo necesario en `g2p.js` o en el script Python.

## Risks / Trade-offs

- **[Riesgo] El modelo español puede tener acento marcado en VELA** → Mitigation: evaluar con los 4 audios del corpus antes de commitear como default. Si suena mal, probar `es_ES-sharvard-medium` como alternativa.
- **[Riesgo] El phoneme_id_map del modelo español puede no incluir todos los símbolos VELA** → Mitigation: task explícita de verificación antes de regenerar audios.
- **[Trade-off] Modelo `high` es más pesado (~65MB) que `medium` (~32MB)** → Aceptable; está en `.gitignore` y se descarga localmente.

## Migration Plan

1. Descargar `es_MX-claude-high` a `voices/`
2. Verificar phoneme_id_map del nuevo modelo
3. Ajustar `g2p.js` si algún símbolo IPA no está en el mapa
4. Actualizar `synthesize-phonemes.py`: split por `|||`
5. Actualizar `.env.example` con el nuevo `PIPER_MODEL`
6. Regenerar los 4 audios del corpus y escuchar
7. Rollback: cambiar `PIPER_MODEL` de vuelta al modelo inglés en `.env`
