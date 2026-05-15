import re
import glob

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

existing = set()
for match in re.finditer(r'\*\*(\w+)\*\*', content):
    existing.add(match.group(1).lower().replace('.', ''))

new_words = []
for f in sorted(glob.glob('word_review/words_2026-05-14_nro_*.md')):
    with open(f, 'r') as rf:
        text = rf.read()
    for line in text.split('\n'):
        if '| **' in line:
            match = re.search(r'\*\*(\S+)\*\*.*?\| /(\S+)/ \| (.*?) \|', line)
            if match:
                word = match.group(1).lower().replace('.', '')
                a = match.group(2)
                eng = match.group(3)
                if word not in existing and len(word) > 1 and '🔁' not in line:
                    new_words.append((word, a, eng))

print(f"Total unique new words: {len(new_words)}")
for w, a, e in new_words:
    print(f"  {w} = {e}")
