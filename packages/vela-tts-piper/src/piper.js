import { spawn } from 'node:child_process';
import { readFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PHONEME_SCRIPT = resolve(__dirname, '../scripts/synthesize-phonemes.py');
const DEFAULT_DICT   = resolve(__dirname, '../data/vela-dictionary.json');

export function resolvePiperConfig(overrides = {}) {
  const config = {
    piperBin: overrides.piperBin ?? process.env.PIPER_BIN,
    model: overrides.model ?? process.env.PIPER_MODEL,
    config: overrides.config ?? process.env.PIPER_CONFIG,
    speaker: overrides.speaker ?? process.env.PIPER_SPEAKER,
    inputMode: overrides.inputMode ?? process.env.PIPER_INPUT_MODE ?? 'text',
    pythonBin: overrides.pythonBin ?? process.env.PYTHON_BIN,
  };

  if (!config.piperBin) throw new Error('Missing PIPER_BIN');
  if (!config.model) throw new Error('Missing PIPER_MODEL');

  return config;
}

export async function synthesizeText(text, outputPath, options = {}) {
  const cfg = resolvePiperConfig(options);
  await runPiper({ text, outputPath, ...cfg });
}

export async function synthesizeTextFile(inputTextPath, outputPath, options = {}) {
  const text = await readFile(inputTextPath, 'utf8');
  await synthesizeText(text, outputPath, options);
}

// synthesizePhonemes now accepts raw VELA text and does phoneme surgery internally
export async function synthesizePhonemes(velaText, outputPath, options = {}) {
  const cfg = resolvePiperConfig({ ...options, inputMode: 'phoneme' });
  const dictPath = options.velaDictPath ?? process.env.VELA_DICT_PATH ?? DEFAULT_DICT;
  await runPiperPhonemes({ text: velaText, outputPath, dictPath, ...cfg });
}

function runPiperPhonemes({ text, outputPath, piperBin, model, config, speaker, pythonBin, dictPath }) {
  const python = pythonBin ?? piperBin.replace(/\/piper$/, '/python3');
  return new Promise((resolve, reject) => {
    const args = [PHONEME_SCRIPT, '--model', model, '--output', outputPath,
                  '--vela-dict', dictPath];
    if (config) args.push('--config', config);
    if (speaker) args.push('--speaker', String(speaker));

    const child = spawn(python, args, { stdio: ['pipe', 'pipe', 'pipe'] });
    let stderr = '';
    child.stderr.on('data', (chunk) => { stderr += String(chunk); });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) return resolve();
      reject(new Error(`phoneme synthesis failed (code ${code}): ${stderr.trim()}`));
    });
    child.stdin.write(text);
    child.stdin.end();
  });
}

function runPiper({ text, outputPath, piperBin, model, config, speaker }) {
  return new Promise((resolve, reject) => {
    const args = ['--model', model, '--output_file', outputPath];

    if (config) args.push('--config', config);
    if (speaker) args.push('--speaker', String(speaker));

    const child = spawn(piperBin, args, { stdio: ['pipe', 'pipe', 'pipe'] });
    let stderr = '';

    child.stderr.on('data', (chunk) => {
      stderr += String(chunk);
    });

    child.on('error', reject);

    child.on('close', (code) => {
      if (code === 0) return resolve();
      reject(new Error(`Piper failed with code ${code}: ${stderr.trim()}`));
    });

    child.stdin.write(text);
    child.stdin.end();
  });
}
