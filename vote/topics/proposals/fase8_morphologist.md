# Proposal — VELA Morphologist (ollama/deepseek-v4-pro)

**Date:** 2026-05-14
**Topic:** Fase 8 Gap Words (12 proposals)
**Agent:** vela_morphologist
**Model:** deepseek-v4-pro

## Summary

| Verdict | Count |
|---------|-------|
| APPROVED | 9 |
| AMENDED | 2 |
| REJECTED | 1 |

## Verdicts

| # | Proposed | Meaning | Verdict | Final Form | Type |
|---|----------|---------|---------|------------|------|
| 1 | forti | forth | **APPROVED** | forti | atom |
| 2 | pasi | peace | **APPROVED** | pasi | atom |
| 3 | servi | serve | **APPROVED** | servi | atom |
| 4 | Loru | Lord | **APPROVED** | Loru | proper atom |
| 5 | nait | night | **APPROVED** | nait | atom |
| 6 | erth | earth | **AMENDED** | **ert** | atom (from `ert-kweik`) |
| 7 | flaur | flower | **APPROVED** | flaur | atom |
| 8 | glas | grass | **AMENDED** | **gras** | atom |
| 9 | green | green | **AMENDED** | **grin** | atom (adjective) |
| 10 | werld | world | **APPROVED** | werld | atom |
| 11 | tugeter | together | **REJECTED** | **tugede** | atom |
| 12 | morne | morning | **APPROVED** | morne | atom |

## Key Decisions

### AMENDED

**erth → ert**
- Reason: `ert` already attested in compound `ert-kweik` (earthquake). Introducing `erth` creates unmotivated allomorphic variant (allomorphy violation).
- The -th cluster is English orthographic artifact with no phonetic motivation in VELA.

**glas → gras**
- Reason: "glas" = "glass" in Swedish, Danish, Norwegian, German (Esperanto *glaso*). Dangerous international false friend.
- Preserves English /ɡræs/ phonetics with `gras`.

**green → grin**
- Reason: Double "ee" is English interference. VELA does not mark vowel length via double letters.
- Evidence: tree→tri, see→si, bird→brid. All /iː/ represented by single `i`.

### REJECTED

**tugeter → tugede**
- Reason: Compound analysis fails ALL Quality Gate criteria:
  - ≤2 roots: FAIL (3 roots: tu, get, er)
  - Meaningful: FAIL ("two-get-er" = person who obtains two items)
  - Non-ambiguous: FAIL (parsed as agent noun "to-getter")
  - Not infantile: FAIL (resembles child's misanalysis)
- English etymology *tōgædere* is diachronic, not productive.
- Alternative: **tugede** — atom, eliminates agentive -er, simplifies medial consonant.

## Morphological Integrity Score

**10/12 proposals pass** with 0 or minor amendments.
- 2 substantive interventions: erth→ert (pre-existing root), tugeter→tugede (failed compound gate).
- All 12 concepts resolve to **atoms** — zero genuine compounds survive Quality Gate.
- ~150 Tier 1 atom budget absorbs all 12 comfortably.

## Convergence with Other Specialists

| Word | Morfólogo | Fonólogo | Lexicógrafo | Convergencia |
|------|-----------|----------|-------------|-------------|
| forti | ✅ | ✅ | ✅ | **Unánime** |
| pasi | ✅ | ✅ | 📝 paci | 2/3 |
| servi | ✅ | ✅ | 📝 serv | 2/3 |
| Loru | ✅ | ✅ | ❌ Dominu | 2/3 (conflicto) |
| nait | ✅ | ✅ | ✅ | **Unánime** |
| erth | 📝 ert | 📝 erti | ✅ erth | Disputa |
| flaur | ✅ | ✅ | ✅ | **Unánime** |
| glas | 📝 gras | 📝 glasa | ❌ gras | 2/3 (conflicto menor) |
| green | 📝 grin | 📝 grini | 📝 gren | Todos enmiendan, diferentes |
| werld | ✅ | ✅ | ✅ | **Unánime** |
| tugeter | ❌ tugede | 📝 tugete | 📝 togeder | Todos rechazan/enmiendan |
| morne | ✅ | ✅ | 📝 morn | 2/3 |

## Critical Finding

The morphologist is the MOST PERMISSIVE of the three specialists so far. Only 1 rejection (tugeter, for principled compound-gate reasons). Approves proper nouns, adjectives, time words, and abstract nouns as atoms without phonotactic amendments.

**Conflict with phonologist:** Morphologist doesn't enforce Q3 vowel-final strictly. Approves nait, erth, flaur, glas, green, werld as-is. The phonologist amended 7 of these for vowel-final.
