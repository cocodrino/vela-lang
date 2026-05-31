## ADDED Requirements

### Requirement: g2pWord emits espeak-ng phoneme strings
The `g2pWord` function in `packages/vela-tts-piper/src/vela/g2p.js` SHALL emit espeak-ng phoneme notation suitable for Piper's `--phoneme_input` mode. Phonemes MUST be space-separated. Syllable boundaries SHALL be represented by ` . ` (space-dot-space).

#### Scenario: Single-syllable word produces space-separated phonemes
- **WHEN** `g2pWord("man")` is called
- **THEN** the output SHALL be `m a n`

#### Scenario: Multi-syllable word includes syllable boundary
- **WHEN** `g2pWord("halo")` is called
- **THEN** the output SHALL be `h a . l o`

#### Scenario: Digraph sh is converted to espeak-ng S
- **WHEN** `g2pWord("shain")` is called
- **THEN** the output SHALL be `S a i n`

#### Scenario: Digraph ch is converted to espeak-ng tS
- **WHEN** `g2pWord("chek")` is called
- **THEN** the output SHALL be `tS e k`

#### Scenario: y grapheme maps to espeak-ng j (palatal approximant)
- **WHEN** `g2pWord("yelo")` is called
- **THEN** the output SHALL be `j e . l o`

#### Scenario: Unknown grapheme passes through unchanged
- **WHEN** `g2pWord` encounters a character not in the phoneme map
- **THEN** the character SHALL be included in the output as-is (passthrough, no error)

### Requirement: g2pWord does not emit IPA symbols
The `g2pWord` function SHALL NOT emit Unicode IPA characters (e.g. `ʃ`, `tʃ`, `ŋ`, `ʒ`, `θ`, `dʒ`) in its output. These are invalid for Piper `--phoneme_input`.

#### Scenario: Old IPA symbols are absent from output
- **WHEN** any VELA word is processed by `g2pWord`
- **THEN** the returned string SHALL NOT contain any of the characters: `ʃ ʒ θ ŋ dʒ tʃ ɹ`
