import re

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

existing_words = set()
for match in re.finditer(r'\*\*(\w+)\*\*', content):
    word = match.group(1).lower()
    existing_words.add(word)

print(f"Existing words: {len(existing_words)}")

test_words = ['need', 'try', 'start', 'lion', 'tiger', 'shirt', 'phone', 'circle', 'justice']
for w in test_words:
    print(f"{w}: {'EXISTS' if w in existing_words else 'NEW'}")
