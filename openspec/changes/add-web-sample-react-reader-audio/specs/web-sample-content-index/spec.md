## ADDED Requirements

### Requirement: The app SHALL consume a structured content index
The system SHALL load a machine-readable index that defines each text item with stable identity and asset paths.

#### Scenario: Valid index entry
- **WHEN** an index item contains `id`, `title`, `type`, `textPath`, and optional `audioPath`
- **THEN** the app can render and navigate the item without hardcoded routes

### Requirement: The index SHALL constrain supported text types
The system SHALL recognize `poem` and `story` as canonical types for the MVP.

#### Scenario: Supported type entry
- **WHEN** an index item has type `poem` or `story`
- **THEN** the app includes it in the corresponding filtered view

### Requirement: The app SHALL validate index load errors
The system SHALL report index parse/load failures with user-visible fallback messaging.

#### Scenario: Invalid index file
- **WHEN** index JSON cannot be fetched or parsed
- **THEN** the app shows an error state and avoids rendering broken content controls
