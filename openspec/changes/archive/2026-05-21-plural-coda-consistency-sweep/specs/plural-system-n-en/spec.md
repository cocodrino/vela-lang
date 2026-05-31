## ADDED Requirements

### Requirement: Plural formation uses -n/-en
The language specification MUST define plural formation as:
- If the surface singular noun ends in a vowel (a/e/i/o/u), plural MUST be formed by suffixing **-n**.
- Otherwise, plural MUST be formed by suffixing **-en**.

#### Scenario: Vowel-final noun plural
- **WHEN** noun is `siti`
- **THEN** plural MUST be `siti-n`

#### Scenario: Consonant-final noun plural
- **WHEN** noun is `man`
- **THEN** plural MUST be `man-en`

### Requirement: Case stacking order is CASE → PLURAL
The specification MUST define morpheme order for nouns with case + plural as:
`ROOT → CASE → PLURAL`.

#### Scenario: Genitive plural
- **WHEN** noun is `man` with genitive `-se` and plural
- **THEN** form MUST be `man-se-n`

#### Scenario: Locative plural
- **WHEN** noun is `siti` with locative `-to` and plural
- **THEN** form MUST be `siti-to-n`
