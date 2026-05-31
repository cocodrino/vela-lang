## ADDED Requirements

### Requirement: Repo-wide plural examples are normalized
All example sentences and corpus texts in-scope MUST use the canonical plural system (-n/-en) and MUST NOT use legacy plural -s.

#### Scenario: Grammar example normalization
- **WHEN** a grammar doc shows a plural noun example
- **THEN** it MUST use -n/-en

#### Scenario: Corpus text normalization
- **WHEN** a story/poem text contains a plural noun marker
- **THEN** it MUST be normalized to -n/-en

### Requirement: Normalization produces an auditable report
Normalization MUST produce an auditable list of changed files and the patterns changed.

#### Scenario: Reviewable sweep
- **WHEN** normalization is run
- **THEN** it MUST output a report of modifications for review
