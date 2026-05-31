#!/usr/bin/env python3
"""
VELA TTS — Phoneme Surgery approach.

For each word in the VELA text:
  1. English model phonemizes the sentence → natural prosody + stress structure
  2. Each word's English phonemes are replaced with VELA dictionary phonemes
  3. Fallback for unknown words: apply vowel/consonant substitutions to English phonemes

This gives English-quality prosody with VELA-correct phonemes.

Usage:
  echo "Mi hop ke evri man." | python synthesize-phonemes.py \
    --model voices/en_US-lessac-medium.onnx \
    --vela-dict data/vela-dictionary.json \
    --output out.wav
"""
import argparse, json, os, re, sys, wave
import numpy as np

# ---------------------------------------------------------------------------
# Substitutions applied to English phonemes when word is NOT in VELA dict
# ---------------------------------------------------------------------------
# Single-phoneme substitutions
SINGLE_SUB = {
    'ɹ': 'r',   # English retroflex → VELA alveolar
    'ɪ': 'i',   # lax high front → pure /i/
    'ʊ': 'u',   # lax high back  → pure /u/
    'ɛ': 'e',   # lax mid front  → pure /e/
    'ʌ': 'a',   # mid central    → /a/
    'æ': 'a',   # low front      → /a/
    'ɑ': 'a',   # low back       → /a/
    'ɒ': 'o',   # rounded low    → /o/
    'ɔ': 'o',   # mid back       → /o/
    'ə': 'a',   # schwa          → /a/
    'ɚ': 'r',   # rhotic schwa   → /r/
    'ɐ': 'a',   # near-open      → /a/
    'ː': None,  # length mark    → drop
    'ʲ': None,  # palatalization → drop
}
# Sequences to collapse (processed left-to-right AFTER single subs)
SEQ_COLLAPSE = [
    (['e', 'i'], ['e']),   # eɪ → e (English "ay" → VELA /e/)
    (['o', 'u'], ['o']),   # oʊ → o (English "oh" → VELA /o/)
]

def apply_substitutions(phonemes):
    # Step 1: single substitutions
    out = []
    for p in phonemes:
        sub = SINGLE_SUB.get(p, p)
        if sub is not None:
            out.append(sub)
    # Step 2: sequence collapses
    for seq, replacement in SEQ_COLLAPSE:
        result = []
        i = 0
        while i < len(out):
            if out[i:i+len(seq)] == seq:
                result.extend(replacement)
                i += len(seq)
            else:
                result.append(out[i])
                i += 1
        out = result
    return out

AFFRICATES = {'tʃ': ['t', 'ʃ'], 'dʒ': ['d', 'ʒ']}

def parse_vela_entry(entry_str, r_phone='r'):
    """Parse a VELA dictionary entry like 'k r ˈi' → ['k', 'r', 'ˈ', 'i'].
    Drops '.' (syllable boundaries) and expands affricates tʃ/dʒ.
    r_phone: the actual phoneme to use for VELA /r/ ('r' for Spanish, 'ɹ' for English model).
    """
    result = []
    for t in entry_str.split():
        if t == '.':
            continue
        if t in AFFRICATES:
            result.extend(AFFRICATES[t])
        elif t == 'r':
            result.append(r_phone)
        else:
            result.append(t)
    return result

def split_by_word_boundary(phoneme_list):
    """Split a flat phoneme list by ' ' (word boundary) into per-word lists."""
    groups = []
    current = []
    for p in phoneme_list:
        if p == ' ':
            if current:
                groups.append(current)
                current = []
        else:
            current.append(p)
    if current:
        groups.append(current)
    return groups

def tokenize_vela(text):
    """Extract word tokens from VELA text (lowercase, no punctuation)."""
    return re.findall(r"[a-zA-Z']+(?:-[a-zA-Z']+)*", text.lower())

def surgery(sentence_text, voice, vela_dict, r_phone='r'):
    """
    Phonemize sentence_text with the model, replace each word's phonemes
    with VELA dictionary entries. Returns flat phoneme list for synthesis.
    r_phone: 'ɹ' for English models (retroflex, audible), 'r' for Spanish.
    """
    en_sentences = voice.phonemize(sentence_text)
    if not en_sentences or not en_sentences[0]:
        return []

    en_phonemes = en_sentences[0]
    en_word_groups = split_by_word_boundary(en_phonemes)
    vela_words = tokenize_vela(sentence_text)

    if len(en_word_groups) != len(vela_words):
        flat = apply_substitutions([p for p in en_phonemes if p != ' '])
        return flat

    result = []
    for i, (en_grp, vela_word) in enumerate(zip(en_word_groups, vela_words)):
        parts = vela_word.split('-')
        word_phonemes = []
        for j, part in enumerate(parts):
            if part in vela_dict:
                word_phonemes.extend(parse_vela_entry(vela_dict[part], r_phone))
            else:
                word_phonemes.extend(apply_substitutions(en_grp))
            if j < len(parts) - 1:
                word_phonemes.append(' ')

        result.extend(word_phonemes)
        if i < len(en_word_groups) - 1:
            result.append(' ')

    return result

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--model',    required=True)
    p.add_argument('--config',   default=None)
    p.add_argument('--vela-dict',required=True, dest='vela_dict')
    p.add_argument('--output',   required=True)
    p.add_argument('--speaker',  type=int, default=None)
    return p.parse_args()

def write_wav(path, chunks, sample_rate):
    data = np.concatenate(chunks)
    pcm16 = (np.clip(data, -1.0, 1.0) * 32767).astype(np.int16)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1); wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(pcm16.tobytes())

def main():
    args = parse_args()
    import piper

    voice = piper.PiperVoice.load(args.model, config_path=args.config)
    syn_config = piper.SynthesisConfig(speaker_id=args.speaker) if args.speaker is not None else None
    sample_rate = voice.config.sample_rate

    with open(args.vela_dict) as f:
        vela_dict = json.load(f)

    # English models need ɹ (retroflex) — alveolar 'r' is inaudible in them
    model_name = os.path.basename(args.model)
    r_phone = 'ɹ' if model_name.startswith('en_') else 'r'

    raw_text = sys.stdin.read().strip()

    # Split on newlines to get paragraph-level structure
    # Within each paragraph, split on sentence-ending punctuation
    SENTENCE_RE = re.compile(r'(?<=[.!?])\s+')
    PARA_SEP = re.compile(r'\n+')

    paragraphs = PARA_SEP.split(raw_text)

    audio_chunks = []
    silence_sentence = np.zeros(int(sample_rate * 0.35), dtype=np.float32)
    silence_paragraph = np.zeros(int(sample_rate * 0.6),  dtype=np.float32)

    for p_idx, paragraph in enumerate(paragraphs):
        paragraph = paragraph.strip()
        if not paragraph:
            audio_chunks.append(silence_paragraph)
            continue

        sentences = SENTENCE_RE.split(paragraph)

        for s_idx, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if not sentence:
                continue

            phonemes = surgery(sentence, voice, vela_dict, r_phone)
            if not phonemes:
                continue

            try:
                audio = voice.phoneme_ids_to_audio(
                    voice.phonemes_to_ids(phonemes), syn_config
                )
                audio_chunks.append(audio)
            except Exception as e:
                print(f'[warn] synthesis failed: {e}', file=sys.stderr)

            if s_idx < len(sentences) - 1:
                audio_chunks.append(silence_sentence)

        if p_idx < len(paragraphs) - 1:
            audio_chunks.append(silence_paragraph)

    if not audio_chunks:
        print('No audio generated', file=sys.stderr)
        sys.exit(1)

    write_wav(args.output, audio_chunks, sample_rate)
    print(f'[ok] {args.output}', file=sys.stderr)

if __name__ == '__main__':
    main()
