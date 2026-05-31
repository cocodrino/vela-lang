## MODIFIED Requirements

### Requirement: Pipeline sintetiza oración por oración
El script `synthesize-phonemes.py` SHALL dividir el string de fonemas por el marcador `|||` (fin de oración) y sintetizar cada oración en una llamada separada a `phoneme_ids_to_audio`. El audio de cada oración SHALL concatenarse con un silencio de 0.3s entre oraciones. El split por `||||` (párrafo) SHALL producir un silencio de 0.6s entre párrafos.

#### Scenario: Cada oración es una llamada independiente
- **WHEN** el string de fonemas contiene `m i WB h o p WB ||| n o WB w a r WB ||||`
- **THEN** el script SHALL realizar DOS llamadas a `phoneme_ids_to_audio` (una por oración)
- **THEN** el audio final SHALL contener ambas oraciones separadas por silencio de 0.3s

#### Scenario: Párrafos separados por silencio de 0.6s
- **WHEN** el string contiene `|||` seguido de `||||`
- **THEN** el silencio entre los bloques SHALL ser >= 0.5s

#### Scenario: Oración vacía no genera llamada de síntesis
- **WHEN** después del split por `|||` o `||||` queda un chunk vacío o solo con whitespace
- **THEN** ese chunk SHALL ser ignorado (no se llama a `phoneme_ids_to_audio`)
