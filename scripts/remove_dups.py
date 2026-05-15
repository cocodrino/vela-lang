import re

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

# Find all words and their first occurrence position
words_found = {}
lines = content.split('\n')
new_lines = []

for line in lines:
    match = re.search(r'\*\*(\w+)\*\*', line)
    if match and '|' in line and 'Word | AFI' not in line:
        word = match.group(1).lower()
        if word in words_found:
            # This is a duplicate - skip it
            continue
        words_found[word] = True
    new_lines.append(line)

print(f"Removed {len(lines) - len(new_lines)} duplicate lines")

with open('docs/lexicon/LEXICON_BASE.md', 'w') as f:
    f.write('\n'.join(new_lines))

print("Duplicates removed!")
