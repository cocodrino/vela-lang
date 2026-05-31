## 1. Canonical phoneme map

- [x] 1.1 Definir constante `VELA_TO_ESPEAK` en `g2p.js` con los 23 fonemas (18 consonantes + 5 vocales) mapeados a espeak-ng según `design.md` tabla D1
- [x] 1.2 Definir lista `DIGRAPHS` ordenada por longitud descendente: `sh → S`, `ch → tS` (digrafos antes que letras simples)

## 2. Reescribir G2P

- [x] 2.1 Reescribir `g2pWord` para emitir phonemes espeak-ng separados por espacio usando `VELA_TO_ESPEAK`
- [x] 2.2 Eliminar todos los símbolos IPA del output (`ʃ`, `tʃ`, `ŋ`, `ʒ`, `θ`, `dʒ`) — validar con test manual
- [x] 2.3 Agregar lógica de syllable boundary ` . ` entre sílabas (regla: insertar `.` después de cada vocal que no sea la última del token)

## 3. Migrar diccionario

- [x] 3.1 Convertir las 29 entradas existentes en `vela-dictionary.json` de formato silábico (`ha.lo`) a espeak-ng (`h a . l o`)
- [x] 3.2 Ejecutar G2P sobre las 168 palabras únicas del corpus para generar entradas automáticas
- [x] 3.3 Revisar manualmente y corregir las entradas G2P-generadas que sean fonológicamente incorrectas
- [x] 3.4 Escribir el diccionario expandido en `vela-dictionary.json` (las 29 originales + las nuevas, sin duplicados)

## 4. Configuración de entorno

- [x] 4.1 Actualizar `.env.example`: setear `PIPER_INPUT_MODE=phoneme` como default
- [x] 4.2 Agregar comentario en `.env.example` explicando que `text` sigue funcionando como fallback explícito

## 5. Validación de audio

- [x] 5.1 Regenerar `poem-laif-biutifl.wav` con el nuevo pipeline y verificar que la pronunciación es VELA (no inglés)
- [x] 5.2 Regenerar `poem-pis-hope.wav` y verificar
- [x] 5.3 Regenerar `story-lumina-bridge.wav` y verificar
- [x] 5.4 Regenerar `story-song-teacher.wav` y verificar
- [x] 5.5 Copiar los WAVs actualizados a `web-sample/public/audio/` con `tts:vela:sync-web-audio`
