import re

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

def read_block_data(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    data_rows = []
    for line in lines:
        if line.startswith('| **'):
            data_rows.append(line)
    return ''.join(data_rows)

# Block 1: Verbs Extended
block1_data = read_block_data('word_review/insert_block_1.md')
# Find the Verbs section and its ending
idx = content.find('### Verbs — Extended Set')
if idx >= 0:
    # Find next section after Verbs
    next_idx = content.find('### Nature', idx)
    # Actually Verbs is the LAST section, so find EOF pattern
    # Let's insert after the last ``` in Verbs section
    pos = content.find('```', idx)
    if pos > 0:
        pos = content.find('\n', pos) + 1
        content = content[:pos] + '\n' + block1_data + '\n' + content[pos:]
        print("Block 1 (Verbs) inserted")

# Block 2: Animals — find Nature and Environment end
block2_data = read_block_data('word_review/insert_block_2.md')
idx = content.find('### Nature and Environment')
if idx >= 0:
    next_idx = content.find('\n### Food', idx)
    if next_idx > 0:
        content = content[:next_idx] + '\n' + block2_data + '\n' + content[next_idx:]
        print("Block 2 (Animals) inserted")

# Block 3: Clothing — new section after Professions
block3_header = "\n### Clothing, Materials and Textures\n\n"
block3_data = read_block_data('word_review/insert_block_3.md')
idx = content.find('### Professions — All Compound, Gender-Neutral')
if idx >= 0:
    next_idx = content.find('\n### The Home', idx)
    if next_idx > 0:
        content = content[:next_idx] + block3_header + block3_data + '\n' + content[next_idx:]
        print("Block 3 (Clothing) inserted")

# Block 4: Technology — insert into Technology and Tools (continued)
block4_data = read_block_data('word_review/insert_block_4.md')
idx = content.find('### Technology and Tools (continued)')
if idx >= 0:
    next_idx = content.find('\n### Transportation', idx)
    if next_idx > 0:
        content = content[:next_idx] + '\n' + block4_data + '\n' + content[next_idx:]
        print("Block 4 (Technology) inserted")

# Block 5: Shapes/Directions — new section after Abstract and Emotional
block5_header = "\n### Shapes, Directions, Space and Measures\n\n"
block5_data = read_block_data('word_review/insert_block_5.md')
idx = content.find('### Abstract and Emotional Concepts')
if idx >= 0:
    next_idx = content.find('\n### Verbs', idx)
    if next_idx > 0:
        content = content[:next_idx] + block5_header + block5_data + '\n' + content[next_idx:]
        print("Block 5 (Shapes/Directions) inserted")

# Block 6: Abstract — insert into Abstract and Emotional Concepts
block6_data = read_block_data('word_review/insert_block_6.md')
idx = content.find('### Abstract and Emotional Concepts')
if idx >= 0:
    next_idx = content.find('\n### Shapes', idx)
    if next_idx < 0:
        next_idx = content.find('\n### Verbs', idx)
    if next_idx > 0:
        content = content[:next_idx] + '\n' + block6_data + '\n' + content[next_idx:]
        print("Block 6 (Abstract) inserted")

with open('docs/lexicon/LEXICON_BASE.md', 'w') as f:
    f.write(content)

print("\nLEXICON_BASE.md updated with all 6 blocks!")
