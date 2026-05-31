## Context

Plural marking and word-final phonotactics diverged across VELA docs/corpus due to historical evolution:
- Grammar historically documented plural `-s` (with case-order workarounds), while phonology preferred open syllables.
- Q1 permitted sonorant codas in practice, but this was not consistently codified or propagated.
- Fase 8 creative writing introduced additional plural forms and legacy examples.

Recent committee decision: adopt plural **-n/-en** and propagate repo-wide.

Constraints:
- Keep changes mechanical and reviewable (large repo sweep).
- Avoid parallel subagent spawning (MCP instability). Prefer single-pass scripted edits + verification.
- Preserve 200-atom ceiling constraints; do not introduce new atoms as part of normalization.

## Goals / Non-Goals

**Goals:**
- Define canonical plural morphology: `-n` after vowel-final roots, `-en` after consonant-final roots.
- Update grammar docs (tables/examples) and lexicon examples to match canonical plural.
- Sweep corpus texts to replace `X-s` plural occurrences with `X-n` or `X-en` per rule.
- Codify word-final coda policy in phonology docs (and explicitly state relationship to plural).
- Make voting workflow docs intercom-first with Agent fallback.

**Non-Goals:**
- Full refactor of legacy consonant-final lexicon to vowel-final (debt item; separate change).
- Changing case inventory beyond existing `-se` and `-to`.
- Introducing new plural classes (no irregular plural lexicon).

## Decisions

1) **Plural morphology = -n/-en**
- Rule: if surface singular ends in vowel → +`n`; else → +`en`.
- Case stacking: keep order `CASE → PL`; since `-se/-to` end in vowels, plural after case always surfaces as `-n`.

2) **Repo sweep strategy: scripted, deterministic**
- Use ripgrep to locate plural patterns (`\b[a-z]+-s\b`, `-se-s`, `-to-s`).
- Apply edits with a small script that:
  - Parses tokens and converts to `-n/-en` using a vowel-final heuristic.
  - Special-cases already-cased forms (`-se`, `-to`) to `-se-n`, `-to-n`.
  - Produces a report of changes for review.

3) **Phonology codas: document explicitly**
- Add a section clarifying legal word-final codas and how plural interacts.
- Explicitly state whether `-s` is permitted as a lexical coda (separate from plural).

4) **Voting workflow: intercom-first**
- Keep pi-teams as deprecated.
- Intercom sessions preferred; Agent tool remains fallback in constrained environments.

## Risks / Trade-offs

- **Risk:** Over-replacing lexical `-s` that is not plural (e.g., abbreviations, fixed forms) → **Mitigation:** restrict sweep scope to known corpora/examples; generate diff report; manual review for false positives.
- **Risk:** Heuristic `vowel-final → -n` may mis-handle tokens ending in `y` or punctuation → **Mitigation:** tokenization + strip punctuation before decision; keep punctuation after substitution.
- **Risk:** Large diff increases merge/review cost → **Mitigation:** stage work in phases (grammar, lexicon, texts, vote docs) and keep commits small.
- **Risk:** Phonology policy dispute (codas) blocks finalization → **Mitigation:** keep plural policy independent; document coda policy with clearly marked decision points.
