## ADDED Requirements

### Requirement: Dictionary covers all corpus words
The system SHALL provide an IPA phoneme entry in `data/vela-dictionary.json` for every unique word present in the VELA corpus texts under `web-sample/public/texts/`.

#### Scenario: Complete coverage
- **WHEN** a script enumerates all unique words across `poem-laif-biutifl.txt`, `poem-pis-hope.txt`, `story-lumina-bridge.txt`, and `story-song-teacher.txt`
- **THEN** every enumerated word SHALL have a non-empty string value in the dictionary

### Requirement: Dictionary entries use valid espeak-ng IPA
Every dictionary value SHALL consist exclusively of space-separated phonemes from the espeak-ng `en-US` phoneme inventory. No pseudo-phonemes (e.g., `laif`, `biu.ti.fl`) are permitted.

#### Scenario: Invalid entry rejected
- **WHEN** a validation script inspects the entry `"laif": "laif"`
- **THEN** it SHALL flag `laif` as an invalid phoneme because `l` `a` `i` `f` are separate tokens and `a` `i` together do not represent the diphthong /aɪ/

#### Scenario: Valid entry accepted
- **WHEN** a validation script inspects the entry `"laif": "l aɪ f"`
- **THEN** it SHALL accept the entry because `l`, `aɪ`, and `f` are all valid espeak-ng phonemes

### Requirement: Dictionary remains JSON loadable
The file SHALL remain valid JSON and loadable by `src/vela/dictionary.js` without modification to the loader.

#### Scenario: Loader compatibility
- **WHEN** `loadVelaDictionary()` reads the expanded dictionary
- **THEN** it SHALL return a Map with all entries accessible via `lookupWord()`

## REMOVED Requirements

### Requirement: Pseudo-phoneme entries
**Reason**: The original dictionary used orthographic strings as phonemes, which Piper misinterprets. All entries must now be genuine IPA.
**Migration**: Replace every old entry with its correct espeak-ng IPA equivalent during this change.
