## ADDED Requirements

### Requirement: Sistema usa modelo español de Piper
El pipeline TTS SHALL usar el modelo `es_MX-claude-high` como voz por defecto. El archivo del modelo SHALL residir en `packages/vela-tts-piper/voices/`. El `.env.example` SHALL apuntar a este modelo en `PIPER_MODEL`.

#### Scenario: El modelo español existe en voices/
- **WHEN** se ejecuta `npm run tts:vela:batch`
- **THEN** el sistema SHALL cargar el modelo desde `packages/vela-tts-piper/voices/es_MX-claude-high.onnx`
- **THEN** la síntesis SHALL completar sin error

#### Scenario: Las vocales VELA suenan puras
- **WHEN** se sintetiza `p i s` (IPA de "pis")
- **THEN** la vocal SHALL sonar como /i/ pura, no como el diptongo inglés /ɪ/

#### Scenario: Fonemas VELA están en el phoneme_id_map del modelo
- **WHEN** se llama `voice.phonemes_to_ids(['a','e','i','o','u','p','t','k','b','d','r','l','m','n','s','f','v','h','w','j','ʃ','ˈ'])` con el modelo español
- **THEN** NINGÚN símbolo SHALL mapearse a ID 0 (`_`, silencio/padding)

### Requirement: Mapa IPA es compatible con el modelo español
El mapa `VELA_TO_IPA` en `g2p.js` SHALL producir únicamente símbolos IPA presentes en el `phoneme_id_map` del modelo español. Si algún símbolo no existe en el modelo, SHALL usarse el equivalente más cercano que sí esté en el mapa.

#### Scenario: g2pWord no produce símbolos ausentes del modelo
- **WHEN** se procesa cualquier palabra VELA con `g2pWord`
- **THEN** cada símbolo en el output SHALL tener un ID válido (> 0) en el phoneme_id_map del modelo español
