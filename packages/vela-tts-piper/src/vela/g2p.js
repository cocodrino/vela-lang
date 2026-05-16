const DIGRAPHS = [
  ['sh', 'ʃ'],
  ['ch', 'tʃ'],
  ['ng', 'ŋ'],
  ['zh', 'ʒ'],
  ['th', 'θ']
];

const LETTER_MAP = {
  a: 'a',
  b: 'b',
  c: 'k',
  d: 'd',
  e: 'e',
  f: 'f',
  g: 'g',
  h: 'h',
  i: 'i',
  j: 'dʒ',
  k: 'k',
  l: 'l',
  m: 'm',
  n: 'n',
  o: 'o',
  p: 'p',
  q: 'k',
  r: 'r',
  s: 's',
  t: 't',
  u: 'u',
  v: 'v',
  w: 'w',
  x: 'ks',
  y: 'j',
  z: 'z',
  "'": ''
};

export function g2pWord(word) {
  let rest = String(word ?? '').toLowerCase();
  const out = [];

  while (rest.length > 0) {
    const digraph = DIGRAPHS.find(([graph]) => rest.startsWith(graph));
    if (digraph) {
      out.push(digraph[1]);
      rest = rest.slice(digraph[0].length);
      continue;
    }

    const ch = rest[0];
    const mapped = LETTER_MAP[ch] ?? ch;
    out.push(mapped);
    rest = rest.slice(1);
  }

  return out.join(' ');
}
