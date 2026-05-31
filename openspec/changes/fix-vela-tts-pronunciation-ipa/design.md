## Context

VELA usa Piper TTS con el modelo `en_US-lessac-medium`. Piper soporta dos modos de entrada:
- **text mode**: Piper fonematiza el texto internamente usando espeak-ng con el idioma del modelo (en_US). Esto produce pronunciación inglesa para palabras VELA.
- **phoneme mode** (`--phoneme_input`): Piper recibe directamente una cadena en espeak-ng phoneme notation y la pasa al vocoder sin fonematización interna.

El código ya tiene soporte para ambos modos (`synthesizePhonemes` / `synthesizeText`). El problema es que:
1. El modo default es `text`
2. El diccionario tiene valores en notación silábica (`ha.lo`), no fonemas
3. El G2P emite IPA (`ʃ`, `tʃ`), no espeak-ng (`S`, `tS`)

La fuente de verdad fonológica está en `docs/phonology/PHONOLOGY_FINAL.md`: 18 consonantes + 5 vocales + reglas de diptongos.

## Goals / Non-Goals

**Goals:**
- VELA words are pronounced with VELA phonology, not English phonology
- `g2p.js` emits valid espeak-ng phoneme strings for all VELA graphemes
- `vela-dictionary.json` stores espeak-ng phonemes (not syllabified text)
- `PIPER_INPUT_MODE=phoneme` is the default in `.env.example`
- Dictionary covers all 168 unique words found in the corpus texts
- The 23-phoneme → espeak-ng mapping is documented as a canonical reference

**Non-Goals:**
- Training a custom Piper voice model for VELA
- Prosody/intonation improvements beyond what espeak-ng phonemes allow
- Adding new words beyond the 168 corpus words (committee review process handles that)
- Changing the public API of `synthesizeVelaText` or `synthesizeVelaFile`

## Decisions

### D1: espeak-ng notation, not raw IPA

**Decision**: G2P output format is espeak-ng phoneme notation (what Piper `--phoneme_input` expects), not standard IPA.

**Why**: Piper internally uses espeak-ng. The `--phoneme_input` flag bypasses espeak-ng's G2P but still expects espeak-ng's own phoneme alphabet. Passing IPA symbols causes Piper to either fail silently or fall back to English phonology.

**Mapping (VELA phoneme → espeak-ng)**:

| VELA | IPA | espeak-ng |
|------|-----|-----------|
| a    | /a/ | `a` |
| e    | /e/ | `e` |
| i    | /i/ | `i` |
| o    | /o/ | `o` |
| u    | /u/ | `u` |
| p    | /p/ | `p` |
| t    | /t/ | `t` |
| k    | /k/ | `k` |
| b    | /b/ | `b` |
| d    | /d/ | `d` |
| g    | /g/ | `g` |
| m    | /m/ | `m` |
| n    | /n/ | `n` |
| f    | /f/ | `f` |
| v    | /v/ | `v` |
| s    | /s/ | `s` |
| z    | /z/ | `z` |
| sh   | /ʃ/ | `S` |
| h    | /h/ | `h` |
| l    | /l/ | `l` |
| r    | /r/ | `r` (alveolar, not ɹ) |
| w    | /w/ | `w` |
| y    | /j/ | `j` |
| ch   | /tʃ/ | `tS` |

**Alternatives considered**: Use IPA directly and convert at Piper call boundary → rejected because Piper's IPA support is inconsistent across voices and versions.

### D2: Syllable boundaries use `.` in espeak-ng output

**Decision**: Keep syllable boundary markers (`.`) in espeak-ng phoneme strings, e.g. `h a . l o` for `halo`.

**Why**: espeak-ng honors `.` as syllable boundaries for prosody. Removing them produces monotone output on polysyllabic words.

### D3: Dictionary-first, G2P as fallback (unchanged)

**Decision**: Keep existing lookup priority: dictionary hit → use dictionary value; miss → g2p.

**Why**: Dictionary allows hand-tuned pronunciations for irregular words. G2P handles new words automatically. This is the right architecture for a constructed language where rules are regular but exceptions may appear.

### D4: Migrate dictionary values in-place

**Decision**: Convert all 29 existing entries in `vela-dictionary.json` from syllabified text to espeak-ng and expand to cover all 168 corpus words.

**Why**: Single source of truth. No parallel data files to maintain.

## Risks / Trade-offs

- **[Risk] Piper `--phoneme_input` format may vary across Piper versions** → Mitigation: Document the tested Piper version in `.env.example` comments. The `piper.js` `runPiper` function logs stderr; phoneme parse errors will surface there.
- **[Risk] 144 corpus words without committee-approved phonemes** → Mitigation: G2P handles them automatically. Words with irregular pronunciation can be added to the dictionary after committee review. The G2P rules are regular enough for VELA that automatic G2P should be correct for most words.
- **[Risk] English model voice quality for non-English phonemes** → Mitigation: espeak-ng phoneme passthrough gives us direct control over what phonemes are synthesized. The lessac-medium model has reasonable coverage of the IPA phones VELA uses. A custom voice would be ideal long-term but is out of scope here.

## Migration Plan

1. Update `g2p.js` — no external API change
2. Migrate `vela-dictionary.json` values to espeak-ng format
3. Expand dictionary with remaining 139 corpus words (G2P-generated, spot-checked)
4. Update `.env.example` with `PIPER_INPUT_MODE=phoneme`
5. Regenerate all 4 corpus audio files and compare with previous output
6. Rollback: revert `.env` to `PIPER_INPUT_MODE=text` to restore previous behavior instantly

## Open Questions

- None. Phoneme map is fully defined by `PHONOLOGY_FINAL.md`. espeak-ng notation is stable for these phonemes.
