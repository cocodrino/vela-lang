=== VELA TTS PHONEME ASSIGNMENT DOSSIER ===
Date: 2026-05-28
Task: Assign espeak-ng IPA phonemes to 144 new VELA words from the corpus.

=== CONTEXT ===
VELA is an international auxiliary constructed language (conlang). It uses a simplified English-like orthography but needs proper IPA phoneme mapping for TTS synthesis via Piper (espeak-ng phoneme input).

Current dictionary has 23 entries with WRONG pseudo-phonemes (e.g., "laif": "laif" instead of "l aɪ f").

=== ESPEAK-NG EN-US PHONEME INVENTORY ===
CONSONANTS: p b t d k g m n ŋ f v θ ð s z ʃ ʒ h tʃ dʒ r l j w
VOWELS: ɪ i ɛ æ ɑ ɔ oʊ ʊ u ʌ ə ɜ ɚ
DIPHTHONGS: aɪ aʊ ɔɪ ɪə ɛə ʊə
STRESS: ˈ (primary) ˌ (secondary)

=== CORPUS TEXTS ===

--- poem-laif-biutifl.txt ---
La laif es short bat biutifl.
Mi luk la sun, mi hir la win.
Evri dei es a gift,
evri vok es a chans por lav.

Yu go, yu faal, yu rise agen.
In la dark, a lit stil glow.
La laif es short, yes,
bat la hart kin si la biuti.

--- poem-pis-hope.txt ---
Mi hop ke evri man kin liv in pis.
No war, no fea, no silent kri.

Wi bild brij, no wal.
Wi sher pan, no hungr nait.

Yu an mi, diferent vois,
bat un song in la sem ski:
Pis por yu,
pis por mi,
pis por al.

--- story-lumina-bridge.txt ---
Lumina liv la nord siti-to.
Rivera liv la sud siti-to.
For long taim, la dui siti no tok.

Un dei, a yong maker nem Sol desin a smol brij.
Hi sed: "If wi kin wok tugeter, wi kin tok tugeter."

People kam, han bi han.
Ston, wod, metal, song.
After sevn dei, la brij stand.

Lumina first stept over.
Rivera smiled.
No big speech, no king, no law.
Just un simple vok: "Halo."

From dat dei, market grow,
frendship grow,
and la old fear slowli fade.

--- story-song-teacher.txt ---
Li bi-ed a lern-po for thirty yer.
Evri moning li open la dor,
put chalk on la tabel,
and ask: "Sai yu?"

Som student kam with joy,
som with heavy hart.
Li lisn before li teach.

One nait, storm cut la lait.
Class no stop.
Li lit tri smol lamp,
and la room turn warm.

"Words are boats," li sed.
"If yu sher dem, no wan sink alone."

Yers pas.
Student become doctor, farmer, singer, parent.
Bat when dem mit agen,
dem stil remember la voice:
"Tok clear. Tok kind. Tok true."

=== WORD LIST ===

KNOWN (23 words - need phoneme correction):
bat, biutifl, es, evri, go, halo, hop, in, ke, kin, la, laif, li, liv, man, mi, no, pis, sai, short, wan, wi, yu

NEW (144 words - need phoneme assignment):
a, after, agen, al, alone, an, and, are, ask, become, before, bi, bi-ed, big, bild, biuti, boats, brij, chalk, chans, class, clear, cut, dark, dat, dei, dem, desin, diferent, doctor, dor, dui, faal, fade, farmer, fea, fear, first, for, frendship, from, gift, glow, grow, han, hart, heavy, hi, hir, hungr, if, joy, just, kam, kind, king, kri, lait, lamp, lav, law, lern-po, lisn, lit, long, luk, lumina, maker, market, metal, mit, moning, nait, nem, nord, old, on, one, open, over, pan, parent, pas, people, por, put, remember, rise, rivera, room, sed, sem, sevn, sher, si, silent, simple, singer, sink, siti, siti-to, ski, slowli, smiled, smol, sol, som, song, speech, stand, stept, stil, ston, stop, storm, student, sud, sun, tabel, taim, teach, thirty, tok, tri, true, tugeter, turn, un, voice, vois, vok, wal, war, warm, when, win, with, wod, wok, words, yer, yers, yes, yong

=== COMPOUNDS / DERIVATIVES TO NOTE ===
- lern-po (lern + po = teacher?)
- siti-to (siti + to = small city?)
- bi-ed (bi + ed = ?)
- biutifl (biuti + fl? or root)
- slowli (slow + li = adverbial?)
- smiled (smile + d = past tense?)
- stept (stept = stepped?)
- biutifl vs biuti (root vs derived)

=== RULES FOR PHONEME ASSIGNMENT ===
1. Use ONLY the espeak-ng en-US phoneme inventory above.
2. Output format: word → space-separated phonemes (e.g., "laif → l aɪ f")
3. For digraphs in VELA orthography: sh→ʃ, ch→tʃ, th→θ, ng→ŋ, zh→ʒ, ai→aɪ, ei→eɪ, au→aʊ, ou→oʊ, ea→iː, ee→iː, oo→uː, ph→f, wh→w
4. c→k, y-vowel→i, y-consonant→j, x→ks, q→k, j→dʒ
5. If a sound does not exist in English, map to closest equivalent.
6. Stress: mark primary stress ˈ on first syllable unless reason otherwise.
7. Use space-separated tokens. Piper needs this format.
