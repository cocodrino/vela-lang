import re
from datetime import datetime

with open('docs/lexicon/LEXICON_BASE.md', 'r') as f:
    content = f.read()

existing_words = set()
for match in re.finditer(r'\*\*(\w+)\*\*', content):
    word = match.group(1).lower()
    existing_words.add(word)

# All proposed words organized by block
blocks_data = [
    ("BLOQUE 1 — Verbos Esenciales Extendidos", [
        ("niid", "to need", "Mi niid help."),
        ("trai", "to try", "Mi trai mi best."),
        ("fini", "to finish", "Mi fini la wok."),
        ("begin", "to begin", "La klas begin."),
        ("end", "to end", "La film end."),
        ("open", "to open", "Mi open la dor."),
        ("klos", "to close", "Mi klos la windo."),
        ("wosh", "to wash", "Mi wosh la dishi."),
        ("klin", "to clean", "Mi klin la rum."),
        ("kat", "to cut", "Mi kat la bred."),
        ("hit", "to hit", "La bal hit la wal."),
        ("push", "to push", "Mi push la dor."),
        ("pul", "to pull", "Mi pul la rop."),
        ("throu", "to throw", "Mi throu la bal."),
        ("katch", "to catch", "Mi katch la bal."),
        ("fol", "to fall", "La lef fol."),
        ("klaim", "to climb", "Wi klaim la tri."),
        ("jump", "to jump", "La kat jump."),
        ("ran", "to run", "Mi ran fast."),
        ("wok", "to walk", "Wi wok tu la park."),
        ("sit", "to sit", "Mi sit hier."),
        ("stand", "to stand", "Mi stand up."),
        ("lai", "to lie down", "Mi lai on la bed."),
        ("slip", "to sleep", "La child slip."),
        ("weik", "to wake", "Mi weik erli."),
        ("dai", "to die", "La old man dai."),
        ("kil", "to kill", "Yu mas no kil."),
        ("fait", "to fight", "De fait for la kantri."),
        ("win", "to win", "Wi win la geim."),
        ("luz", "to lose", "Mi luz la kei."),
        ("send", "to send", "Mi send la letr."),
        ("risiv", "to receive", "Mi risiv la paki."),
        ("pei", "to pay", "Mi pei la bil."),
        ("bai", "to buy", "Mi bai bred."),
        ("sel", "to sell", "De sel ka."),
        ("chuz", "to choose", "Yu chuz wan."),
        ("disaid", "to decide", "Wi disaid nau."),
        ("plan", "to plan", "Mi plan la trip."),
        ("pripar", "to prepare", "Mi pripar la food."),
        ("weit", "to wait", "Mi weit for yu."),
        ("hari", "to hurry", "Mi hari up."),
        ("stei", "to stay", "Mi stei hier."),
        ("liv", "to leave", "Mi liv nau."),
        ("entar", "to enter", "Mi entar la hous."),
        ("eksit", "to exit", "Mi eksit nau."),
        ("ritan", "to return", "Mi ritan tumoro."),
        ("vizit", "to visit", "Mi vizit mi fren."),
        ("kol", "to call", "Mi kol yu."),
        ("invait", "to invite", "Mi invait yu."),
    ]),
    ("BLOQUE 2 — Animales", [
        ("lai.on", "lion", "La lai.on es strong."),
        ("tai.gar", "tiger", "La tai.gar es fast."),
        ("e.le.fant", "elephant", "La e.le.fant es big."),
        ("mon.ki", "monkey", "La mon.ki plei."),
        ("go.ri.la", "gorilla", "La go.ri.la es strong."),
        ("ber", "bear", "La ber sleep in winter."),
        ("wulf", "wolf", "La wulf hau."),
        ("foks", "fox", "La foks es smart."),
        ("dir", "deer", "La dir run fast."),
        ("ra.bit", "rabbit", "La ra.bit jump."),
        ("maus", "mouse", "La maus es smol."),
        ("rat", "rat", "La rat es dirty."),
        ("frog", "frog", "La frog liv in la pond."),
        ("tar.tl", "turtle", "La tar.tl es slo."),
        ("kro.ko.dail", "crocodile", "La kro.ko.dail es dangerus."),
        ("shark", "shark", "La shark liv in la mar."),
        ("weil", "whale", "La weil es big."),
        ("dol.fin", "dolphin", "La dol.fin es smart."),
        ("pen.gwin", "penguin", "La pen.gwin es nais."),
        ("i.gl", "eagle", "La i.gl flai hait."),
        ("hok", "hawk", "La hok katch mous."),
        ("aul", "owl", "La aul flai at nait."),
        ("krou", "crow", "La krou es blak."),
        ("spa.rou", "sparrow", "La spa.rou es smol."),
        ("ba.ta.flai", "butterfly", "La ba.ta.flai es biju."),
        ("bi", "bee", "La bi mak honi."),
        ("ant", "ant", "La ant wok hard."),
        ("spai.dar", "spider", "La spai.dar mak web."),
        ("mos.ki.to", "mosquito", "La mos.ki.to bite."),
        ("flai", "fly (insect)", "La flai es pest."),
        ("worm", "worm", "La worm liv in la soil."),
        ("sneil", "snail", "La sneil es slo."),
        ("li.zard", "lizard", "La li.zard es cold."),
        ("ka.mal", "camel", "La ka.mal liv in dese."),
        ("ji.raf", "giraffe", "La ji.raf es tall."),
        ("ze.bra", "zebra", "La ze.bra hav stripe."),
        ("rai.no", "rhinoceros", "La rai.no es big."),
        ("hi.po", "hippopotamus", "La hi.po liv in watre."),
        ("kan.ga.ru", "kangaroo", "La kan.ga.ru jump."),
        ("ko.a.la", "koala", "La ko.a.la eat lef."),
        ("pan.da", "panda", "La pan.da eat bamboo."),
        ("skwi.ral", "squirrel", "La skwi.ral klim tri."),
        ("hej.hog", "hedgehog", "La hej.hog es smol."),
        ("bat", "bat (animal)", "La bat flai at nait."),
        ("sil", "seal", "La sil liv in mar."),
        ("o.tar", "otter", "La o.tar plei in watre."),
        ("got", "goat", "La got giv milk."),
        ("dak", "duck", "La dak swim."),
        ("gus", "goose", "La gus flai."),
    ]),
]

# Generate review files and lexicon insertions
date_str = datetime.now().strftime("%Y-%m-%d")

for block_num, (block_name, words) in enumerate(blocks_data, 1):
    # Filter out duplicates
    new_words = [(v, e, ex) for v, e, ex in words if v.lower().replace('.', '') not in existing_words]
    
    # Create review file
    review_content = f"# {block_name}\n\n"
    review_content += f"**Date:** {date_str}  \n"
    review_content += f"**Block:** {block_num}  \n"
    review_content += f"**Total proposed:** {len(words)}  \n"
    review_content += f"**New (non-duplicate):** {len(new_words)}  \n"
    review_content += f"**Duplicates filtered:** {len(words) - len(new_words)}  \n\n"
    review_content += "| VELA | AFI | English | Example |\n"
    review_content += "|------|-----|---------|---------|\n"
    
    for vela, eng, ex in words:
        dup_marker = " 🔁" if vela.lower().replace('.', '') in existing_words else ""
        review_content += f"| **{vela}** | /{vela}/ | {eng}{dup_marker} | {ex} |\n"
    
    review_content += "\n## Notes for Committee Review\n\n"
    review_content += "- Please verify phonotactic compliance: (C)V structure, final vowel or /n,m,l,r/\n"
    review_content += "- Please verify compounds are transparent\n"
    review_content += "- Please verify international recognizability\n"
    review_content += "- 🔁 = already exists in LEXICON_BASE.md\n"
    
    with open(f'word_review/words_{date_str}_nro_{block_num}.md', 'w') as f:
        f.write(review_content)
    
    print(f"Created: word_review/words_{date_str}_nro_{block_num}.md ({len(new_words)} new words)")

print("\nReview files generated!")
