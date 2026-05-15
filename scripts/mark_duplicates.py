import re

# 1. Extract all existing words from LEXICON_BASE.md
with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

existing = set()
for match in re.finditer(r'\*\*(\w+)\*\*', content):
    existing.add(match.group(1).lower())

print(f"Existing unique words: {len(existing)}")

# 2. Read each block file and filter
blocks = {
    1: 'word_review/words_2026-05-14_nro_1.md',
    2: 'word_review/words_2026-05-14_nro_2.md',
    3: 'word_review/words_2026-05-14_nro_3.md',
    4: 'word_review/words_2026-05-14_nro_4.md',
    5: 'word_review/words_2026-05-14_nro_5.md',
    6: 'word_review/words_2026-05-14_nro_6.md',
}

for block_num, filepath in blocks.items():
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    dup_count = 0
    kept_count = 0
    
    for line in lines:
        match = re.search(r'\*\*(\w+)\*\*', line)
        if match and '|' in line:
            word = match.group(1).lower()
            if word in existing:
                dup_count += 1
                new_lines.append(line.rstrip() + ' 🔁DUPLICATE\n')
            else:
                kept_count += 1
                new_lines.append(line)
        else:
            new_lines.append(line)
    
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    
    print(f"Block {block_num}: {dup_count} duplicates marked, {kept_count} kept")

print("Done. All blocks updated with duplicate markers.")
