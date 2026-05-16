#!/usr/bin/env node
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { synthesizeVelaText, synthesizeVelaFile, textToVelaPhonemes } from '../src/index.js';

const args = process.argv.slice(2);
const command = args[0];

if (!command || command === '--help' || command === '-h') {
  printHelp();
  process.exit(0);
}

try {
  if (command === 'synth') {
    const inPath = getArg('--in');
    const outPath = getArg('--out');
    if (!inPath || !outPath) throw new Error('synth requires --in and --out');
    await synthesizeVelaFile(resolve(inPath), resolve(outPath));
    console.log(`Generated: ${resolve(outPath)}`);
    process.exit(0);
  }

  if (command === 'synth-text') {
    const text = getArg('--text');
    const outPath = getArg('--out');
    if (!text || !outPath) throw new Error('synth-text requires --text and --out');
    await synthesizeVelaText(text, resolve(outPath));
    console.log(`Generated: ${resolve(outPath)}`);
    process.exit(0);
  }

  if (command === 'preview-phonemes') {
    const text = getArg('--text');
    const inPath = getArg('--in');
    const sourceText = text ?? (inPath ? await readFile(resolve(inPath), 'utf8') : null);
    if (!sourceText) throw new Error('preview-phonemes requires --text or --in');
    const phonemes = await textToVelaPhonemes(sourceText);
    console.log(phonemes);
    process.exit(0);
  }

  throw new Error(`Unknown command: ${command}`);
} catch (error) {
  console.error(`[vela-tts] ${error.message}`);
  process.exit(1);
}

function getArg(name) {
  const idx = args.indexOf(name);
  if (idx < 0) return null;
  return args[idx + 1] ?? null;
}

function printHelp() {
  console.log(`vela-tts usage:
  vela-tts synth --in <input.txt> --out <output.wav>
  vela-tts synth-text --text "..." --out <output.wav>
  vela-tts preview-phonemes --text "..."
  vela-tts preview-phonemes --in <input.txt>`);
}
