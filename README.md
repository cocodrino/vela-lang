# VELA

An experimental constructed language whose design rules were proposed, argued and voted on by a committee of AI agents, with a human steering. The project is **archived**: this README says plainly what it produced, what it got right, and where it falls short.

Website: https://cocodrino.github.io/vela-lang/

---

## What VELA is and what it is not

**It is** a regularized, English-based language with phonetic spelling. One letter is one sound, verbs have no irregular forms, there is no grammatical gender, and many words are built by joining smaller ones (`lern-hous`, learn + house, "school").

**It is** a record of an experiment: 21 design rounds in which AI agents in specialist roles (phonologist, morphologist, lexicographer, semanticist, aestheticist) wrote proposals and voted. Every dossier, proposal and vote is in [`vote/`](vote/).

**It is not** a universal language. Most of the vocabulary is English respelled, so it is easiest for English and Romance-language speakers. An adversarial review estimated that around 70% of the root words are close to their English source; that figure was not independently re-checked. The sound inventory drops the hardest English sounds (`th`, `zh`, schwa) but keeps others, such as final `l`, `r`, `s`, that are hard for Mandarin speakers.

**It is not** proven to be learnable "in weeks". Nobody has learned it. There are no learners, no tests and no timing data.

**It is not** better than the existing alternatives for real use. If you want an auxiliary language with people who speak it, look at [Esperanto](https://en.wikipedia.org/wiki/Esperanto) (since 1887, an active worldwide community). If you want one that draws its vocabulary from many language families instead of mostly one, look at [Globasa](https://www.frathwiki.com/Globasa) or [Lingwa de Planeta](https://en.wikipedia.org/wiki/Lingwa_de_planeta).

## What exists

| Resource | Notes |
|---|---|
| [Courses, Levels 1–5](https://cocodrino.github.io/vela-lang/books/Learning-VELA-Level1.html) | 60 lessons. Written by AI, never tested with a learner. |
| [Dictionary (PDF)](https://cocodrino.github.io/vela-lang/books/VELA-Dictionary.pdf) | 2,928 entries, generated from [`docs/lexicon/`](docs/lexicon/). |
| [Reference book](https://cocodrino.github.io/vela-lang/books/VELA-The-Universal-Conlang.html) | Sounds and grammar overview. Its title predates this README. |
| [`docs/grammar/GRAMMAR_COMPLETE.md`](docs/grammar/GRAMMAR_COMPLETE.md) | Full grammar. See the known issues below. |
| [`vote/topics/consensus/fase5_consensus.md`](vote/topics/consensus/fase5_consensus.md) | The ratified rules, R1–R21. Where a rule and another document disagree, the rule is the canon. |
| [`scripts/validate_phonology.py`](scripts/validate_phonology.py) | Checks the lexicon and the texts against the sound rules. |

## The language in brief

- 5 vowels (a e i o u), 20 consonants, one sound per letter.
- A word ends in a vowel or in a single `n`, `m`, `l`, `r`, `s`. A closed list of short grammar words (`if`, `at`, `wit`, `of`…) is the exception.
- Stress always falls on the second-to-last syllable.
- Word order is subject, verb, object.
- The dictionary form of a verb is its present: `maka` "make, makes". Past and future add a suffix to the short root: `mak-edo` "made", `mak-wil` "will make". "To be" works the same way: `es`, `es-edo`, `es-wil`.
- Plural `-n` / `-en`, possessive `-se`, location `-to`, professions `-po`.
- Adjectives have one form as separate words (`un reda bol`, `La bol es reda`). Inside a compound they use the short root (`red-hous`), the way English tells a greenhouse from a green house.

## How the committee worked, honestly

- Rounds R1–R17 were configured to use agents on other models (Kimi, DeepSeek, GLM; see `vote/docs/PROCESS.md`). In the largest of them, three agents covered the five roles (`fase5_consensus.md`).
- Rounds R18–R21 used five instances of a single model (Claude). The earlier claim that every specialist runs on a different model is not true for those rounds.
- The committee mostly ratified the options the dossier presented. In R21 the dossier listed only some candidate forms; a second round was held after the owner asked about an option it had left out, and the result changed.
- Several real errors were not caught by the committee. A Reddit reader found that the old past suffix `-ed` broke the word-ending rule and that "no irregular verbs" sat next to an irregular verb. Both were fixed in R21.

## Known issues

These are open, measured on the current repo.

- **196 compound words end in a consonant the sound rules forbid** (for example `moring-fud`). The rule "a hyphen joins the short root" and the rule about word endings contradict each other at the end of a compound. Fixing it is a canon decision that was never made.
- **Two words have no settled form:** `net` (network) and `bit` (computing). The committee rejected merging them with `neta` (fishing net) and `bita` (bitter) but did not choose replacements.
- **The validator fails** on the 198 issues above (`FAIL — 198 error(s)`). Until this cleanup it reported "0 errors" because every dictionary entry was treated as legal by definition. That bug is fixed; the errors it now shows were always there.
- **The grammar document disagrees with itself and with the texts in places.** For example, the yes/no question particle `q` it describes is never used in any text or lesson.
- **Many words in the stories and courses are English words that never entered the dictionary** (`make`, `walk`, `quiet`…). The validator lists them as notes.
- **`web-sample/` and the text-to-speech dictionary** still use the pre-R21 past suffix `-ed`.

## Repository layout

```
vela-lang/
├── index.html                 landing page (GitHub Pages)
├── books/                     courses, reference book, dictionary PDF
├── docs/
│   ├── phonology/             sound rules
│   ├── grammar/               grammar reference
│   ├── lexicon/               the three source lexicons
│   ├── dictionary/            generated dictionary and English index
│   ├── texts/                 stories, poems, 100 phrases
│   └── research/              background research
├── vote/                      committee dossiers, proposals, votes, consensus
├── scripts/                   validator, corpus migrator, dictionary generators
└── ROADMAP.md                 project history and debts
```

## Running the checks

```
python3 scripts/validate_phonology.py          # lexicon + texts
python3 scripts/generate_dictionary.py         # rebuild docs/dictionary/
python3 scripts/generate_dictionary_pdf.py     # rebuild the PDF (needs typst)
```
