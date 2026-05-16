import { spawn } from 'node:child_process';
import { readFile } from 'node:fs/promises';

export function resolvePiperConfig(overrides = {}) {
  const config = {
    piperBin: overrides.piperBin ?? process.env.PIPER_BIN,
    model: overrides.model ?? process.env.PIPER_MODEL,
    config: overrides.config ?? process.env.PIPER_CONFIG,
    speaker: overrides.speaker ?? process.env.PIPER_SPEAKER,
    inputMode: overrides.inputMode ?? process.env.PIPER_INPUT_MODE ?? 'text',
    forcePhonemeInput: overrides.forcePhonemeInput ?? false
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

export async function synthesizePhonemes(phonemeText, outputPath, options = {}) {
  const cfg = resolvePiperConfig({ ...options, inputMode: 'phoneme' });
  await runPiper({ text: phonemeText, outputPath, ...cfg });
}

function runPiper({ text, outputPath, piperBin, model, config, speaker, inputMode, forcePhonemeInput }) {
  return new Promise((resolve, reject) => {
    const args = ['--model', model, '--output_file', outputPath];

    if (config) args.push('--config', config);
    if (speaker) args.push('--speaker', String(speaker));

    if (inputMode === 'phoneme') {
      if (forcePhonemeInput) {
        args.push('--phoneme_input');
      } else {
        console.warn('[vela-tts] PIPER_INPUT_MODE=phoneme set. If your Piper build supports it, enable forcePhonemeInput=true to pass --phoneme_input. Falling back to text mode args by default.');
      }
    }

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
