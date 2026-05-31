## ADDED Requirements

### Requirement: Voting workflow defaults to intercom-first
The voting system documentation MUST define pi-intercom as the primary workflow for 5-specialist committee deliberations.

#### Scenario: Default workflow selection
- **WHEN** a new deliberation is initiated
- **THEN** docs MUST instruct intercom-first workflow

### Requirement: Agent-tool fallback is documented
Documentation MUST describe an Agent-tool fallback workflow for constrained environments, including:
- embedded dossier requirement
- sequential spawning requirement
- known model incompatibilities

#### Scenario: Fallback workflow
- **WHEN** intercom/pi-teams is unavailable
- **THEN** docs MUST provide Agent fallback steps
