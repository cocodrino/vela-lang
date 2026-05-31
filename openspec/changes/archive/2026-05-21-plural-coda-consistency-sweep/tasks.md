## 1. Inventory & Guardrails

- [x] 1.1 Run repo scan for legacy plural markers (`\b[a-z]+-s\b`, `-se-s`, `-to-s`) and capture list of hits
- [x] 1.2 Define sweep scope and exclusions (avoid false positives: abbreviations, code blocks if any)

## 2. Grammar Spec Implementation

- [x] 2.1 Update `docs/grammar/GRAMMAR_COMPLETE.md` plural section to -n/-en with examples
- [x] 2.2 Update `docs/grammar/03-case-system.md` to reflect `CASE → PL` with -n/-en examples (`man-se-n`, `siti-to-n`)
- [x] 2.3 Update `docs/writing/ORTHOGRAPHY.md` plural notation and combination table

## 3. Lexicon & Corpus Sweep

- [x] 3.1 Update `docs/lexicon/LEXICON_BASE.md` example plurals to -n/-en (remove `*-s` plural entries)
- [x] 3.2 Sweep `docs/texts/` for `X-s` plural tokens and convert to `X-n` vs `X-en` per rule
- [x] 3.3 Sweep `vote/` docs/examples to align plural examples (`man-se-n` etc.)

## 4. Phonology Policy Finalization

- [x] 4.1 Update `docs/phonology/PHONOLOGY_FINAL.md` with explicit coda inventory + statement that plural -n/-en is legal
- [x] 4.2 Add note on new-atom policy vs grandfathered legacy codas (if applicable)

## 5. Voting Workflow Robustness

- [x] 5.1 Ensure `.pi/scripts/vote-specialists.sh` uses original specialist models (kimi for phon/aest; deepseek/glm for others)
- [x] 5.2 Add `vote/docs/INTERCOM_VOTING.md` and update `vote/SKILL.md` to intercom-first + Agent fallback

## 6. Verification

- [x] 6.1 Re-run repo scan to confirm no remaining legacy `-s` plural patterns in docs/texts (except marked historical notes)
- [x] 6.2 Spot-check 3–5 texts for readability after sweep
- [x] 6.3 Run formatting/lint/test commands (if any) and ensure no build regressions
