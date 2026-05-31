## Why

The VELA TTS pipeline currently produces audio with poor pronunciation because the phoneme dictionary only covers ~25 words (out of 100+ in the corpus) and the G2P fallback maps letters one-by-one without understanding VELA digraphs like `ai`, `ou`, `sh`, `ch`. This makes the generated audio sound robotic and wrong for a constructed language meant to be read aloud.

## What Changes

- Expand `data/vela-dictionary.json` with proper IPA phonemes for every unique word across all 4 corpus texts (~100+ entries).
- Rewrite `src/vela/g2p.js` to handle VELA digraphs (`sh`, `ch`, `th`, `ng`, `ai`, `ei`, `au`, `ou`, `ea`, `ee`, `oo`, `ph`, `wh`) and produce valid espeak-ng IPA phonemes.
- Add validation tooling to verify that every dictionary entry and every G2P output is a valid phoneme string that Piper can consume.
- Regenerate all 4 WAV audio files in `web-sample/public/audio/` using the fixed pipeline.
- (No breaking changes to the web-sample app itself — only audio quality improves.)

## Capabilities

### New Capabilities
- `vela-dictionary-expansion`: Complete IPA dictionary for all corpus words with validation tooling.
- `vela-g2p-digraphs`: Grapheme-to-phoneme engine with VELA-specific digraph rules and espeak-ng IPA output.

### Modified Capabilities
<!-- No existing specs to modify -->

## Impact

- `packages/vela-tts-piper/data/vela-dictionary.json` — expanded entries, IPA format
- `packages/vela-tts-piper/src/vela/g2p.js` — rewritten with digraph support
- `packages/vela-tts-piper/src/vela/dictionary.js` — may add validation helpers
- `packages/vela-tts-piper/scripts/` — may add validate-dictionary script
- `web-sample/public/audio/*.wav` — regenerated with correct pronunciation
- Piper CLI invocation remains unchanged (`npm run tts:vela:batch-and-sync`)
