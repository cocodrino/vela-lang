import { mkdir, readdir, copyFile } from 'node:fs/promises';
import { resolve } from 'node:path';

const sourceDir = resolve(process.env.VELA_LIBRARY_OUTPUT ?? 'packages/vela-tts-piper/output/library');
const targetDir = resolve(process.env.VELA_WEB_AUDIO_DIR ?? 'web-sample/public/audio');

await mkdir(targetDir, { recursive: true });

let files;
try {
  files = await readdir(sourceDir);
} catch (error) {
  console.error(`[sync-web-audio] Source not found: ${sourceDir}`);
  console.error('Run `npm run tts:vela:batch` first.');
  process.exit(1);
}

const wavs = files.filter((name) => name.endsWith('.wav'));
if (!wavs.length) {
  console.log(`[sync-web-audio] No WAV files found in ${sourceDir}`);
  process.exit(0);
}

for (const name of wavs) {
  await copyFile(resolve(sourceDir, name), resolve(targetDir, name));
}

console.log(`[sync-web-audio] Copied ${wavs.length} file(s) to ${targetDir}`);
for (const name of wavs) console.log(`- ${name}`);
