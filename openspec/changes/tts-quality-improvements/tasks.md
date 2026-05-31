## 1. Descargar modelo español

- [x] 1.1 Descargar `es_MX-claude-high.onnx` y `es_MX-claude-high.onnx.json` a `packages/vela-tts-piper/voices/`
- [x] 1.2 Verificar que el modelo carga correctamente con `PiperVoice.load()`

## 2. Verificar compatibilidad de fonemas

- [x] 2.1 Imprimir el `phoneme_id_map` del modelo español y comparar con los símbolos IPA que usa VELA (`a e i o u p t k b d ɡ m n f v s z h l r w j ʃ tʃ dʒ ˈ .`)
- [x] 2.2 Identificar cualquier símbolo que no esté en el mapa del modelo español y definir el sustituto más cercano
- [x] 2.3 Actualizar `VELA_TO_IPA` en `g2p.js` si hay ajustes necesarios

## 3. Síntesis por oración

- [x] 3.1 Actualizar `synthesize-phonemes.py`: dividir por `|||` (oración) dentro de cada bloque de párrafo (`||||`)
- [x] 3.2 Cada oración → llamada separada a `phoneme_ids_to_audio`, concatenar con silencio de 0.3s
- [x] 3.3 Silencio entre párrafos: 0.6s

## 4. Configuración

- [x] 4.1 Actualizar `PIPER_MODEL` en `.env.example` para apuntar a `voices/es_MX-claude-high.onnx`
- [x] 4.2 Regenerar `vela-dictionary.json` con los fonemas validados del paso 2

## 5. Validación de audio

- [x] 5.1 Regenerar los 4 audios del corpus con el modelo español
- [ ] 5.2 Escuchar y verificar que las vocales suenan puras (especialmente `e`, `o`, `i`)
- [ ] 5.3 Verificar que `kri` suena "krée" y `pis` suena "pís"
- [x] 5.4 Copiar audios a `web-sample/public/audio/` con `tts:vela:sync-web-audio`
