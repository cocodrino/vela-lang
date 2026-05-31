## ADDED Requirements

### Requirement: Word-final coda policy is explicit
The phonology specification MUST explicitly enumerate which word-final consonants are permitted as codas and whether the policy applies to:
- new atoms
- grandfathered legacy forms
- inflectional suffixes (plural, tense)

#### Scenario: Reader can determine legality
- **WHEN** a word ends in a consonant
- **THEN** documentation MUST state whether it is legal, deprecated-but-grandfathered, or illegal

### Requirement: Plural suffix legality is documented
The phonology specification MUST explicitly state that the plural system (-n/-en) is legal under the coda policy.

#### Scenario: Plural suffix in phonology
- **WHEN** plural system is referenced
- **THEN** it MUST be documented as phonotactically legal
