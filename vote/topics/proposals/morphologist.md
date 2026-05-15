# Proposal — VELA Morphologist (ollama/deepseek-v4-pro)

**Date:** 2026-05-14
**Topic:** Blocks 1-6 Word Review (186 new words)
**Agent:** vela_morphologist
**Model:** deepseek-v4-pro

## Verdict Counts

| Group | ATOM_OK | COMPOUND_PREFERRED | REJECT | Total |
|-------|---------|-------------------|--------|-------|
| B1 — Animals | 5 | 32 | 1 | 38 |
| B2 — Clothing | 5 | 25 | 0 | 30 |
| B3 — Abstract | 6 | 18 | 2 | 26 |
| B4 — Time/Measure | 7 | 14 | 1 | 22 |
| B5 — Tools/Materials | 7 | 20 | 1 | 28 |
| B6 — Body/Tech/Directions | 16 | 26 | 0 | 42 |
| **TOTAL** | **46** | **135** | **5** | **186** |

- Atoms approved: 46 (24.7%)
- Compounds preferred: 135 (72.6%)
- Rejected: 5 (2.7%)

## Rejected Words (5)

| Word | Reason | Fix |
|------|--------|-----|
| `hai.po` | Dot `.` invalid; `-po` = profession suffix; hippo ≠ profession | `wotr-hors` (water-horse) |
| `fri.dom` | Dot `.` invalid; `dom` ambiguous | `fri-stat` (free-state) |
| `los` | Allomorphy: `lus` (lose) ↔ `los` (loss). One root = one form | Use `lus` nominally |
| `dep` | Allomorphy: `dip` (deep) ↔ `dep` (depth) | Use `dip` nominally |
| `erkweik` | Over-fused compound; obscures `ert` + `weik` roots | `ert-weik` (earth-shake) |

## Critical Observations

1. **Allomorphy violations (6+ cases)**: `los`/`lus`, `dep`/`dip`, `long`/`lengt`, `waid`/`widt`, `hai`/`hait`, `hevi`/`weit`
   - VELA forbids vowel alternation nominalization. One root = one form.

2. **Dot notation misuse (2 cases)**: `hai.po` and `fri.dom` use `.` instead of `-`

3. **Over-fusion (5 cases)**: `erkweik`, `inside`, `autsaid`, `bitwin`, `araund` obscure roots

4. **Length vs frequency mismatch**: `informashon` (4 syllables), `antisipashon` (5 syllables), `krokodail`, `elefant`, `tradishon` too long for atom budget

5. **Atom budget**: 46 atoms consumed → 104 slots remaining for core vocabulary

## Atoms Approved (46)

**Tier 0 Primitives**: ap, daun, left, rait, ovr, andar, nort, saut, ist, west, spes, ples, mind
**Tier 1 Animals**: ber, mous, rat, got, dak
**Tier 1 Clothing**: shart, shu, hat, pant, ring
**Tier 1 Abstract**: pis, wor, soul, sistam, moni, bank
**Tier 1 Time/Measure**: minut, our, niaz, sais, limit
**Tier 1 Tools/Materials**: naif, snow, ais, wul, klei, sand, solt
**Tier 1 Body/Tech**: bon, blod, skin, brein, hart, fon

## Compounds Needed (135)

See full analysis for transparent compound suggestions for all 135 words.
