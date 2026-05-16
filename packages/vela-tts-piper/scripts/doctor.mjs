import { access } from 'node:fs/promises';
import { constants } from 'node:fs';
import { spawnSync } from 'node:child_process';

const checks = [];

async function checkPath(label, value, mode = constants.F_OK) {
  if (!value) {
    checks.push({ label, ok: false, detail: 'missing' });
    return;
  }
  try {
    await access(value, mode);
    checks.push({ label, ok: true, detail: value });
  } catch {
    checks.push({ label, ok: false, detail: value });
  }
}

const piperBin = process.env.PIPER_BIN;
const model = process.env.PIPER_MODEL;
const config = process.env.PIPER_CONFIG;

await checkPath('PIPER_BIN', piperBin, constants.X_OK);
await checkPath('PIPER_MODEL', model, constants.R_OK);
if (config) await checkPath('PIPER_CONFIG', config, constants.R_OK);

if (piperBin) {
  const result = spawnSync(piperBin, ['--help'], { encoding: 'utf8' });
  checks.push({
    label: 'Piper executable responds',
    ok: result.status === 0 || result.status === 1,
    detail: `exit=${result.status}`
  });
}

const failed = checks.filter((c) => !c.ok);
for (const c of checks) {
  console.log(`${c.ok ? '✅' : '❌'} ${c.label}: ${c.detail}`);
}

if (failed.length) {
  console.error(`\nDoctor found ${failed.length} issue(s).`);
  process.exit(1);
}

console.log('\nDoctor OK: Piper setup appears ready.');
