## MODIFIED Requirements

### Requirement: Pipeline synthesizes VELA text using phoneme mode by default
The synthesis pipeline SHALL use `PIPER_INPUT_MODE=phoneme` as the default mode. The `.env.example` file SHALL set `PIPER_INPUT_MODE=phoneme`. The fallback `'text'` default in `pipeline.js` SHALL remain as a safety net for environments where phoneme mode is explicitly disabled.

#### Scenario: Default mode produces phoneme-mode audio
- **WHEN** `synthesizeVelaText` is called without an explicit `inputMode` option
- **AND** `PIPER_INPUT_MODE` env var is set to `phoneme` (as per `.env.example`)
- **THEN** Piper SHALL be invoked with `--phoneme_input` flag
- **THEN** the returned result object SHALL have `mode: "phoneme"`

#### Scenario: Text mode fallback still works when explicitly set
- **WHEN** `synthesizeVelaText` is called with `options.inputMode = "text"`
- **THEN** Piper SHALL be invoked WITHOUT `--phoneme_input` flag
- **THEN** the returned result object SHALL have `mode: "text"`

#### Scenario: Phoneme pipeline output is valid espeak-ng for all corpus texts
- **WHEN** any of the 4 corpus texts is processed by `textToVelaPhonemes`
- **THEN** the returned phoneme string SHALL contain only ASCII characters and valid espeak-ng phoneme symbols
- **THEN** the returned phoneme string SHALL NOT contain Unicode IPA characters
