// IPA phoneme symbols — must match the model's phoneme_id_map exactly
const DIGRAPHS = [
  ['sh', 'ʃ'],
  ['ch', 'tʃ']   // kept as unit; split to [t,ʃ] at synthesis time
];

const VELA_TO_IPA = {
  a: 'a', e: 'e', i: 'i', o: 'o', u: 'u',
  p: 'p', t: 't', k: 'k', b: 'b', d: 'd', g: 'ɡ',  // ɡ = U+0261
  m: 'm', n: 'n', f: 'f', v: 'v', s: 's', z: 'z',
  h: 'h', l: 'l', r: 'r', w: 'w',
  y: 'j',    // palatal approximant /j/
  j: 'dʒ',   // affricate /dʒ/ — split to [d,ʒ] at synthesis time
  c: 'k',    // English loanwords: c → /k/
};

// Alias for external callers that still reference VELA_TO_ESPEAK
const VELA_TO_ESPEAK = VELA_TO_IPA;

const VOWELS = new Set(['a', 'e', 'i', 'o', 'u']);

export function g2pWord(word) {
  let rest = String(word ?? '').toLowerCase();
  const phonemes = [];

  while (rest.length > 0) {
    const digraph = DIGRAPHS.find(([graph]) => rest.startsWith(graph));
    if (digraph) {
      phonemes.push(digraph[1]);
      rest = rest.slice(digraph[0].length);
      continue;
    }

    const ch = rest[0];
    phonemes.push(VELA_TO_ESPEAK[ch] ?? ch);
    rest = rest.slice(1);
  }

  return insertSyllableBoundaries(phonemes, true);
}

function insertSyllableBoundaries(phonemes, addStress = false) {
  const isVowelPhone = (p) => p === 'a' || p === 'e' || p === 'i' || p === 'o' || p === 'u';

  // Find vowel group spans [start, end] — consecutive vowels = diphthong (one group)
  const groups = [];
  let i = 0;
  while (i < phonemes.length) {
    if (isVowelPhone(phonemes[i])) {
      const start = i;
      while (i < phonemes.length && isVowelPhone(phonemes[i])) i++;
      groups.push([start, i - 1]);
    } else {
      i++;
    }
  }

  if (groups.length <= 1) {
    if (addStress && groups.length === 1) {
      // Monosyllabic: insert ˈ before the single vowel group
      const result = [];
      for (let j = 0; j < phonemes.length; j++) {
        if (j === groups[0][0]) result.push('ˈ');
        result.push(phonemes[j]);
      }
      return result.join(' ');
    }
    return phonemes.join(' ');
  }

  // For each pair of adjacent groups, boundary goes before the last consonant
  // that precedes the next group (i.e. the onset of the next syllable).
  // This gives: dan.ki, ha.lo, tu.ge.ter, ev.ri — matching VELA phonotactics.
  const boundaryBefore = new Set();
  for (let g = 0; g < groups.length - 1; g++) {
    const nextStart = groups[g + 1][0];
    boundaryBefore.add(nextStart - 1);
  }

  // Insert primary stress (ˈ) before the first vowel group
  const firstVowelIdx = groups.length > 0 ? groups[0][0] : -1;

  const result = [];
  for (let j = 0; j < phonemes.length; j++) {
    if (boundaryBefore.has(j)) result.push('.');
    if (addStress && j === firstVowelIdx) result.push('ˈ');
    result.push(phonemes[j]);
  }
  return result.join(' ');
}
