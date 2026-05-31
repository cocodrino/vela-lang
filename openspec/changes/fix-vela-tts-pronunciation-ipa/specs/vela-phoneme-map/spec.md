## ADDED Requirements

### Requirement: Canonical VELA-to-espeak-ng phoneme map exists
The system SHALL maintain a canonical mapping from every VELA grapheme to its espeak-ng phoneme symbol. This map MUST cover all 18 consonants and 5 vowels defined in `docs/phonology/PHONOLOGY_FINAL.md`. The map SHALL be implemented as a constant in `g2p.js` and SHALL be the single source of truth for both the G2P engine and any dictionary migration tooling.

#### Scenario: Every VELA consonant grapheme has an espeak-ng mapping
- **WHEN** the canonical phoneme map is loaded
- **THEN** all 18 consonant graphemes (`p t k b d g m n f v s z sh h l r w y`) SHALL be present as keys with valid espeak-ng phoneme values

#### Scenario: Every VELA vowel grapheme has an espeak-ng mapping
- **WHEN** the canonical phoneme map is loaded
- **THEN** all 5 vowel graphemes (`a e i o u`) SHALL be present as keys with valid espeak-ng phoneme values

#### Scenario: Digraphs are matched before single letters
- **WHEN** the G2P engine processes the string `"sha"`
- **THEN** the output SHALL be `S a` (digraph `sh` → `S`, not `s` + `h`)

#### Scenario: The /r/ phoneme maps to alveolar, not English approximant
- **WHEN** the G2P engine processes the grapheme `r`
- **THEN** the output SHALL be `r` (espeak-ng alveolar trill), not `r\` (retroflex approximant)
