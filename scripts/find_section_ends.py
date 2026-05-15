with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    lines = f.readlines()

sections = [
    "Professions — All Compound, Gender-Neutral",
    "Nature and Environment", 
    "Technology and Tools (continued)",
    "Abstract and Emotional Concepts",
    "Verbs — Extended Set (with example sentences)"
]

for s in sections:
    for i, l in enumerate(lines):
        if f'### {s}' in l:
            for j in range(i+1, len(lines)):
                if lines[j].startswith('### '):
                    print(f"{s}: starts {i+1}, ends before {j+1}")
                    for k in range(max(i, j-4), j):
                        print(f"  {k+1}: {lines[k].rstrip()}")
                    break
            else:
                print(f"{s}: starts {i+1}, ends at EOF {len(lines)}")
            print()
            break
