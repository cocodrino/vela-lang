## ADDED Requirements

### Requirement: The app SHALL list available texts by type
The system SHALL display a navigable catalog of available texts and SHALL identify whether each item is a poem or story.

#### Scenario: Catalog loads successfully
- **WHEN** the app starts and content index is available
- **THEN** the UI shows a list with title and type for each text item

### Requirement: The app SHALL render full text content for a selected item
The system SHALL allow the user to open a text item and read its full content in a dedicated reading view.

#### Scenario: User opens a text
- **WHEN** the user selects one catalog item
- **THEN** the app shows the item title, metadata, and full text body

### Requirement: The app SHALL support switching between items without page reload
The system SHALL allow users to navigate among texts while preserving responsive interaction.

#### Scenario: User switches from one text to another
- **WHEN** the user selects a different catalog item
- **THEN** the app updates the reading view to the new item without full page reload
