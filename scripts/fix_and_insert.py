import re

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

# Find and remove the inserted sections (they have specific patterns)
# Remove "### Clothing, Materials and Textures" section
clothing_start = content.find('### Clothing, Materials and Textures')
if clothing_start > 0:
    # Find next section after this
    next_section = content.find('### ', clothing_start + 10)
    if next_section > 0:
        content = content[:clothing_start] + content[next_section:]
        print("Removed Clothing section")

# Remove "### Shapes, Directions, Space and Measures" section
shapes_start = content.find('### Shapes, Directions, Space and Measures')
if shapes_start > 0:
    next_section = content.find('### ', shapes_start + 10)
    if next_section > 0:
        content = content[:shapes_start] + content[next_section:]
        print("Removed Shapes section")

# Now find the duplicate words that were added to existing sections
# We need to remove lines that contain duplicate entries from blocks 1-6
# This is risky - let's be conservative and just remove obvious patterns

# Save the cleaned file
with open('docs/lexicon/LEXICON_BASE.md', 'w') as f:
    f.write(content)

print("LEXICON cleaned. Removed inserted sections.")

# Now insert the 6 corrected blocks
blocks = [
    ('word_review/words_2026-05-14_nro_1_CORREGIDO.md', '### Nature and Environment'),
    ('word_review/words_2026-05-14_nro_2_CORREGIDO.md', '### Professions — All Compound, Gender-Neutral'),
    ('word_review/words_2026-05-14_nro_3_CORREGIDO.md', '### Abstract and Emotional Concepts'),
    ('word_review/words_2026-05-14_nro_4_CORREGIDO.md', '### Abstract and Emotional Concepts'),
    ('word_review/words_2026-05-14_nro_5_CORREGIDO.md', '### Technology and Tools (continued)'),
    ('word_review/words_2026-05-14_nro_6_CORREGIDO.md', '### Verbs — Extended Set (with example sentences)'),
]

import re

def get_block_table(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    # Extract table rows
    rows = []
    in_table = False
    for line in text.split('\n'):
        if line.startswith('| **'):
            rows.append(line)
    return '\n'.join(rows)

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

for block_file, section_anchor in blocks:
    table = get_block_table(block_file)
    if not table.strip():
        continue
    
    # Find section and insert after it
    section_start = content.find(section_anchor)
    if section_start > 0:
        # Find end of this section
        next_section = content.find('\n### ', section_start + len(section_anchor))
        if next_section > 0:
            # Insert before the next section
            content = content[:next_section] + '\n' + table + '\n' + content[next_section:]
            print(f"Inserted {block_file} before {section_anchor}")

with open('docs/lexicon/LEXICON_BASE.md', 'w') as f:
    f.write(content)

print("All corrected blocks inserted!")
