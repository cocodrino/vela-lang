## 1. Discovery & Validation

- [ ] 1.1 Extract all unique words from the 4 corpus texts (`web-sample/public/texts/*.txt`)
- [ ] 1.2 Define the espeak-ng `en-US` phoneme whitelist (consonants, vowels, diphthongs)
- [ ] 1.3 Create `scripts/validate-phonemes.mjs` that checks dictionary/G2P output against the whitelist
- [ ] 1.4 Run validation on current dictionary — confirm failures match expected

## 2. Expand VELA Dictionary

- [ ] 2.1 Map each unique corpus word to correct espeak-ng IPA (space-separated phonemes)
- [ ] 2.2 Update `data/vela-dictionary.json` with all new entries and corrected old entries
- [ ] 2.3 Run `validate-phonemes.mjs` on updated dictionary — all entries must pass
- [ ] 2.4 Verify `loadVelaDictionary()` still loads the JSON correctly

## 3. Rewrite G2P Engine

- [ ] 3.1 Update `src/vela/g2p.js` digraph list: `sh`, `ch`, `th`, `ng`, `zh`, `ai`, `ei`, `au`, `ou`, `ea`, `ee`, `oo`, `ph`, `wh`
- [ ] 3.2 Ensure G2P falls back to single-letter map for unmatched digraphs
- [ ] 3.3 Add `validateG2POutput()` helper that rejects unknown phoneme tokens
- [ ] 3.4 Unit-test G2P with sample VELA words (laif, short, biutifl, etc.)

## 4. Regenerate Audio

- [ ] 4.1 Run `npm run tts:vela:batch-and-sync` to regenerate all 4 WAV files
- [ ] 4.2 Play each generated audio and verify pronunciation is correct
- [ ] 4.3 If any audio is wrong, adjust dictionary/G2P and repeat 4.1–4.2
- [ ] 4.4 Commit regenerated WAVs to `web-sample/public/audio/`

## 5. Cleanup & Documentation

- [ ] 5.1 Update `packages/vela-tts-piper/README.md` with new digraph rules and dictionary size
- [ ] 5.2 Add a note in `web-sample/README.md` about audio regeneration process
- [ ] 5.3 Archive change with `openspec archive change fix-vela-tts-pronunciation`
