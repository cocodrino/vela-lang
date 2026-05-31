## ADDED Requirements

### Requirement: G2P handles VELA digraphs
The G2P engine SHALL recognize and correctly map the following VELA digraphs to espeak-ng IPA before falling back to single-letter mapping: `sh`→`ʃ`, `ch`→`tʃ`, `th`→`θ`, `ng`→`ŋ`, `zh`→`ʒ`, `ai`→`aɪ`, `ei`→`eɪ`, `au`→`aʊ`, `ou`→`oʊ`, `ea`→`iː`, `ee`→`iː`, `oo`→`uː`, `ph`→`f`, `wh`→`w`.

#### Scenario: Digraph decomposition
- **WHEN** `g2pWord("biutifl")` is called
- **THEN** it SHALL produce `b ju t i f l` because the digraph `ui` is not in the rule set and falls through to `u`→`u`, `i`→`i`

#### Scenario: Digraph `sh` mapped
- **WHEN** `g2pWord("short")` is called
- **THEN** it SHALL produce `ʃ oʊ r t` because `sh` is mapped to `ʃ` and `ou` to `oʊ`

#### Scenario: Digraph `ai` mapped
- **WHEN** `g2pWord("laif")` is called and it is NOT in the dictionary
- **THEN** it SHALL produce `l aɪ f` because `ai` maps to `aɪ`

### Requirement: G2P output passes phoneme validation
Every string returned by `g2pWord()` SHALL be splittable by spaces into tokens that are all members of a whitelist of valid espeak-ng phonemes. Any unknown token SHALL cause the caller to throw or log an error.

#### Scenario: Unknown token caught
- **WHEN** `g2pWord("xyz")` produces tokens containing a character not in the whitelist
- **THEN** the pipeline SHALL reject the output and surface the invalid token to the user

### Requirement: G2P preserves non-letter tokens
The G2P engine SHALL pass through punctuation tokens (`.`, `,`, `;`, `:`, `!`, `?`, `\n`) unchanged so that prosody processing can apply pauses.

#### Scenario: Punctuation passthrough
- **WHEN** `g2pWord(".")` is called
- **THEN** it SHALL return `"."` without modification
