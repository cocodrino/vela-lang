## Context

The VELA TTS pipeline lives in `packages/vela-tts-piper/`. It takes VELA text, converts it to phonemes via dictionary lookup + G2P fallback, then feeds those phonemes to Piper with `--phoneme_input`. The current dictionary (`data/vela-dictionary.json`) has ~25 entries but the corpus has ~100+ unique words. The G2P (`src/vela/g2p.js`) is a naive letter-by-letter mapper that does not understand VELA digraphs (`ai`, `ou`, `sh`, `ch`, etc.), producing broken IPA that Piper mispronounces.

Piper uses espeak-ng IPA phonemes. Valid phonemes for the `en_US-lessac-medium` voice include consonants like `p b t d k g m n ŋ f v θ ð s z ʃ ʒ h tʃ dʒ r l j w` and vowels/diphthongs like `ɪ i ɛ æ ɑ ɔ oʊ ʊ u ʌ ə ɜ aɪ aʊ ɔɪ ɪə ɛə ʊə`. The current "dictionary" stores strings like `"laif": "laif"` which Piper treats as 4 separate phonemes (`l` `a` `i` `f`) instead of `l aɪ f`.

## Goals / Non-Goals

**Goals:**
- Every word in the 4 corpus texts has correct IPA in the dictionary.
- The G2P engine handles all VELA digraphs and produces valid espeak-ng IPA.
- A validation script catches invalid phonemes before synthesis.
- Regenerated audio sounds natural and accurate.

**Non-Goals:**
- Adding new corpus texts (only fix existing ones).
- Changing the web-sample React UI.
- Training a custom Piper voice model.
- Real-time streaming synthesis.
- Prosody/intonation beyond basic punctuation pauses.

## Decisions

1. **IPA format: space-separated phoneme tokens**
   - Why: Piper's `--phoneme_input` expects space-separated espeak-ng phonemes.
   - Alternative: continuous IPA string — rejected because Piper needs explicit boundaries.

2. **Dictionary stores full IPA strings per word**
   - Why: Gives exact control per word, avoids G2P ambiguity for common words.
   - Alternative: derive everything from G2P — rejected because VELA orthography has irregularities that need human curation.

3. **G2P as fallback, not primary source**
   - Why: Dictionary covers known corpus words; G2P handles future/new words.
   - G2P will be improved with digraph rules so it produces reasonable output for unknown words.

4. **espeak-ng IPA subset, not full IPA**
   - Why: Piper was trained on espeak-ng phonemes. Using random IPA symbols may not map to the model's embedding space.
   - We will stick to the phoneme inventory that espeak-ng uses for `en-US`.

5. **Validation via whitelist**
   - A script will split dictionary entries and G2P outputs by spaces and check each token against a known list of valid espeak-ng phonemes. Any unknown token = error.

## Risks / Trade-offs

- **Risk: espeak-ng IPA is not exhaustively documented** → Mitigation: use espeak-ng CLI to verify phonemes for tricky words, cross-reference with espeak-ng source.
- **Risk: Some VELA sounds may not exist in English phoneme inventory** → Mitigation: map to closest English equivalent (e.g., VELA `r` as English /r/, `y` as /j/).
- **Risk: Dictionary size grows** → Mitigation: JSON is fine for <1000 entries; if it scales beyond that, consider a compiled format later.
- **Risk: Regenerating audio may overwrite manually curated files** → Mitigation: batch script already writes to `output/library/` then syncs; manual files should not live there.

## Migration Plan

1. Run validation script on current dictionary — expect failures.
2. Expand dictionary with correct IPA for all corpus words.
3. Update G2P with digraph rules.
4. Run validation script again — expect all pass.
5. Run `npm run tts:vela:batch-and-sync` to regenerate WAVs.
6. Play each audio in web-sample to verify pronunciation.
7. If any audio is wrong, adjust dictionary/G2P and repeat.

## Open Questions

- Should the G2P handle stress markers (`ˈ`, `ˌ`) or leave that to prosody?
- Should we add a `vela-phoneme-preview` CLI command to preview phonemes without generating audio?
