import re
with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()
words = re.findall(r'\*\*(\w+)\*\*', content)
print(f"TOTAL WORDS: {len(words)}")
print(f"UNIQUE WORDS: {len(set(w.lower() for w in words))}")
