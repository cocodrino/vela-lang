import { readFile } from 'node:fs/promises';
import { loadVelaDictionary, lookupWord } from './dictionary.js';
import { g2pWord } from './g2p.js';
import { tokenizeVelaText, normalizeVelaText } from './normalize.js';
import { applyProsody } from './prosody.js';
import { synthesizeText, synthesizePhonemes } from '../piper.js';

export async function textToVelaPhonemes(text, options = {}) {
  const dictionary = options.dictionary ?? (await loadVelaDictionary(options.dictionaryPath));
  const normalized = normalizeVelaText(text);
  const tokens = tokenizeVelaText(normalized);

  const phonemeTokens = tokens.map((token) => {
    if (/^[.,;:!?\n]$/.test(token)) return token;
    if (!/[a-zA-Z]/.test(token)) return token;
    const dictHit = lookupWord(token, dictionary);
    // WB = word boundary marker; consumed by phoneme synthesizer (ID 3 = space)
    return ((dictHit ?? g2pWord(token)) + ' WB');
  });

  return applyProsody(phonemeTokens);
}

export async function synthesizeVelaText(text, outPath, options = {}) {
  const mode = options.inputMode ?? process.env.PIPER_INPUT_MODE ?? 'text';

  if (mode === 'phoneme') {
    // Pass original VELA text — Python script handles phoneme surgery internally
    await synthesizePhonemes(text, outPath, options);
    return { outPath, mode: 'phoneme' };
  }

  const phonemes = await textToVelaPhonemes(text, options);
  await synthesizeText(normalizeVelaText(text), outPath, options);
  return { outPath, mode: 'text', phonemes };
}

export async function synthesizeVelaFile(inPath, outPath, options = {}) {
  const text = await readFile(inPath, 'utf8');
  return synthesizeVelaText(text, outPath, options);
}
