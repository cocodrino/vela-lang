export function normalizeVelaText(input) {
  return String(input ?? '')
    .replace(/\r\n/g, '\n')
    .replace(/[“”]/g, '"')
    .replace(/[‘’]/g, "'")
    .replace(/\t/g, ' ')
    .replace(/ +/g, ' ')
    .trim();
}

export function tokenizeVelaText(input) {
  const normalized = normalizeVelaText(input);
  if (!normalized) return [];

  const tokens = [];
  const regex = /([a-zA-Z'-]+|[0-9]+|\n|[.,;:!?])/g;
  let match;
  while ((match = regex.exec(normalized)) !== null) {
    tokens.push(match[0]);
  }
  return tokens;
}
