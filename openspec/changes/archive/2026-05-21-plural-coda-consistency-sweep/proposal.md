## Why

VELA plural marking and word-final phonotactics are internally inconsistent (docs and corpus still contain `-s` plural forms and mixed coda assumptions). This blocks reliable text production, teaching, and future vocabulary work.

## What Changes

- Standardize plural system to **-n/-en** everywhere (grammar, lexicon examples, and texts).
- Formalize word-final coda policy in phonology (what codas are legal, and how this interacts with new word creation).
- Sweep corpus (`docs/texts/`, `docs/lexicon/`, `docs/grammar/`, `vote/`) to remove legacy plural patterns and align examples with current grammar.
- Update voting system docs to make the more robust workflow the default (pi-intercom-first; Agent fallback).

## Capabilities

### New Capabilities
- `plural-system-n-en`: Specifies the official plural morphology rule (-n after vowel-final roots, -en after consonant-final roots) and its interaction with case and compounds.
- `coda-policy`: Specifies the official word-final coda inventory and constraints for new atoms vs grandfathered forms.
- `corpus-normalization`: Defines repo-wide normalization rules for examples and narrative texts (plural forms, case order, hyphenation conventions).
- `voting-intercom-workflow`: Defines the default committee workflow using pi-intercom sessions, including failure modes and fallbacks.

### Modified Capabilities
- (none)

## Impact

- Docs: `docs/grammar/`, `docs/phonology/`, `docs/writing/`, `vote/docs/`
- Corpus: `docs/texts/`
- Lexicon examples: `docs/lexicon/LEXICON_BASE.md`
- Tooling: `.pi/scripts/`, voting workflow docs
