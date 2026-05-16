import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const DEFAULT_DICT_PATH = resolve(process.cwd(), 'packages/vela-tts-piper/data/vela-dictionary.json');

export async function loadVelaDictionary(dictPath = process.env.VELA_DICT_PATH ?? DEFAULT_DICT_PATH) {
  const raw = await readFile(dictPath, 'utf8');
  const parsed = JSON.parse(raw);
  return normalizeDictionary(parsed);
}

function normalizeDictionary(input) {
  const dict = new Map();
  for (const [key, value] of Object.entries(input ?? {})) {
    if (!key || !value) continue;
    dict.set(String(key).toLowerCase(), String(value).trim());
  }
  return dict;
}

export function lookupWord(word, dict) {
  return dict.get(String(word).toLowerCase()) ?? null;
}

export { DEFAULT_DICT_PATH };
