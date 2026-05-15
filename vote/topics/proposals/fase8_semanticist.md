# Proposal — VELA Semanticist (ollama/deepseek-v4-pro)

**Date:** 2026-05-14
**Topic:** Fase 8 Gap Words (12 proposals)
**Agent:** vela_semanticist
**Model:** deepseek-v4-pro

## Summary

| Verdict | Count |
|---------|-------|
| APPROVED | 11 |
| AMENDED | 1 |
| REJECTED | 0 |

## Verdicts

| # | Word | Verdict | Issue |
|---|------|---------|-------|
| 1 | **forti** | ✅ APPROVED | Slight `for` overlap, acceptable across grammatical categories |
| 2 | **pasi** | ✅ APPROVED | Clean. Monosemous: absence of conflict |
| 3 | **servi** | ✅ APPROVED | Distinct from `help`: servi = duty-bound action for superior; help = need-based assistance |
| 4 | **Loru** | ✅ APPROVED | Proper noun / title borrowing. Not a productive common noun |
| 5 | **nait** | ✅ APPROVED | Clean. Temporal interval |
| 6 | **erth** | ✅ APPROVED | Specify: **ground/soil** (not world). `Erth` (capitalized) = planet name |
| 7 | **flaur** | ✅ APPROVED | Clean. Single meaning |
| 8 | **glas** | ✅ APPROVED | External false-friend only. Internally monosemous |
| 9 | **green** | ✅ APPROVED | Clean. Color property |
| 10 | **werld** | ✅ APPROVED | Crucial distinction from `erth`: werld = totality/existence; erth = physical soil |
| 11 | **tugeter** | ✅ APPROVED | Atomic adverb. No internal morpheme boundaries |
| 12 | **morne** | ⚠️ AMENDED → **sunap** | Collision with `mor` = more. Shared [mor] onset creates structural homonymy |

## Semantic Boundary Specifications

### servi vs help
| | **help** | **servi** |
|---|---|---|
| Trigger | Beneficiary has need/incapacity | Agent has role/duty toward beneficiary |
| Power relation | Symmetric possible | Asymmetric (serve ⇒ superior) |
| Formal entailment | `¬can-do(y, e)` | `obligated-to(x, y)` |

### erth vs werld
- **erth** ⊆ physical-objects (soil, ground)
- **werld** ⊈ physical-objects (totality, abstract domain)

### Loru
- Proper noun / closed class of titles
- Does NOT participate in compounding or derivation
- Future native "ruler/master" must be a distinct root

## Critical Finding: morne → sunap

`mor` = MORE and `morne` = MORNING share onset [mor-] with zero semantic relationship.

Recommended replacement: **sunap** = `sun` + `ap` (sun-up)
- Compositional, transparent
- Uses existing VELA roots
- Zero collision risk

## Convergence with Other Specialists

| Word | Semanticista | Fonólogo | Morfólogo | Lexicógrafo | Convergencia |
|------|-------------|----------|-----------|-------------|-------------|
| forti | ✅ | ✅ | ✅ | ✅ | **5/5** |
| pasi | ✅ | ✅ | ✅ | 📝 paci | 4/5 |
| servi | ✅ | ✅ | ✅ | 📝 serv | 4/5 |
| Loru | ✅ | ✅ | ✅ | ❌ Dominu | 4/5 |
| nait | ✅ | ✅ | ✅ | ✅ | **5/5** |
| erth | ✅ | 📝 erti | 📝 ert | ✅ | Disputa |
| flaur | ✅ | ✅ | ✅ | ✅ | **5/5** |
| glas | ✅ | 📝 glasa | 📝 gras | ❌ gras | Disputa |
| green | ✅ | 📝 grini | 📝 grin | 📝 gren | Disputa |
| werld | ✅ | ✅ | ✅ | ✅ | **5/5** |
| tugeter | ✅ | 📝 tugete | ❌ tugede | 📝 togeder | Disputa |
| morne | 📝 sunap | ✅ | ✅ | 📝 morn | Disputa |

**Semanticista is the most permissive specialist: 11/12 approved, only 1 amended.**
