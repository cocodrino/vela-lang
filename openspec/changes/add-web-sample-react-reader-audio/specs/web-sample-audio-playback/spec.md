## ADDED Requirements

### Requirement: The app SHALL provide playback controls for available audio
The system SHALL provide play/pause controls and current time/progress for the selected text when an audio file is configured.

#### Scenario: Audio is available
- **WHEN** the selected text has a valid audio path
- **THEN** the app shows an audio player with play/pause and progress information

### Requirement: The app SHALL handle missing audio gracefully
The system SHALL show a clear non-blocking message when audio is not available for a text.

#### Scenario: Audio is missing
- **WHEN** the selected text has no audio path or audio loading fails
- **THEN** the app shows “audio no disponible” state and keeps text reading functional

### Requirement: The app SHALL stop previous playback when switching texts
The system SHALL avoid overlapping audio when the user changes the selected text.

#### Scenario: User switches text during playback
- **WHEN** one text is currently playing and user opens another text
- **THEN** previous playback stops and player context updates to the new text
