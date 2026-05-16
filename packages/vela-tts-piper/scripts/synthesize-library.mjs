import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { resolve, dirname } from 'node:path';
import { synthesizeVelaText } from '../src/index.js';

const indexPath = resolve(process.env.VELA_LIBRARY_INDEX ?? 'web-sample/public/content/index.json');
const outDir = resolve(process.env.VELA_LIBRARY_OUTPUT ?? 'packages/vela-tts-piper/output/library');

const raw = await readFile(indexPath, 'utf8');
const items = JSON.parse(raw);
if (!Array.isArray(items)) throw new Error('Index JSON must be an array of entries');

await mkdir(outDir, { recursive: true });

const manifest = [];

for (const item of items) {
  const id = item?.id;
  const title = item?.title ?? id;
  const textPath = item?.textPath;

  if (!id || !textPath) {
    manifest.push({ id: id ?? null, title, status: 'error', error: 'missing id or textPath' });
    continue;
  }

  try {
    const absTextPath = resolveTextPath(indexPath, textPath);
    const text = await readFile(absTextPath, 'utf8');
    const outPath = resolve(outDir, `${id}.wav`);
    await synthesizeVelaText(text, outPath);

    manifest.push({
      id,
      title,
      status: 'ok',
      audioPath: outPath,
      source: absTextPath
    });

    console.log(`✅ ${id} -> ${outPath}`);
  } catch (error) {
    manifest.push({ id, title, status: 'error', error: error.message });
    console.error(`❌ ${id}: ${error.message}`);
  }
}

const manifestPath = resolve(outDir, 'manifest.json');
await writeFile(manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
console.log(`\nManifest: ${manifestPath}`);

function resolveTextPath(indexFilePath, textPath) {
  if (textPath.startsWith('/')) {
    const publicRoot = resolve(dirname(indexFilePath), '..');
    return resolve(publicRoot, `.${textPath}`);
  }
  return resolve(dirname(indexFilePath), textPath);
}
