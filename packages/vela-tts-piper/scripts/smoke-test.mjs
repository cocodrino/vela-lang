import { mkdir } from 'node:fs/promises';
import { resolve } from 'node:path';
import { synthesizeVelaText } from '../src/index.js';

const outDir = resolve(process.cwd(), 'output');
const outFile = resolve(outDir, 'smoke-test.wav');

await mkdir(outDir, { recursive: true });

await synthesizeVelaText('Halo! Mi hop ke evri man kin liv in pis.', outFile);
console.log(`Audio generado: ${outFile}`);
