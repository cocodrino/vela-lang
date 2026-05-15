import re
from collections import Counter

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

words = re.findall(r'\*\*(\w+)\*\*', content)
counts = Counter(w.lower() for w in words)

dups = [(w, c) for w, c in counts.items() if c > 1]
print(f"Total entries: {len(words)}")
print(f"Unique words: {len(counts)}")
print(f"Duplicates: {len(dups)}")

if dups:
    for w, c in sorted(dups)[:30]:
        print(f"  {w}: {c} times")
