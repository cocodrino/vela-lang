const BREAK_MAP = {
  ',': ' | ',
  ';': ' || ',
  ':': ' || ',
  '.': ' ||| ',
  '!': ' ||| ',
  '?': ' ||| ',
  '\n': ' |||| '
};

export function applyProsody(tokens) {
  const out = [];

  for (const token of tokens) {
    if (BREAK_MAP[token]) {
      out.push(BREAK_MAP[token]);
      continue;
    }

    out.push(token);
  }

  return out.join(' ').replace(/\s+/g, ' ').trim();
}
