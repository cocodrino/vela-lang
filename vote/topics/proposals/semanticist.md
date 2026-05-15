# Proposal — VELA Semanticist (ollama/deepseek-v4-pro)

**Date:** 2026-05-14
**Topic:** Blocks 1-6 Word Review (186 new words)
**Agent:** vela_semanticist
**Model:** deepseek-v4-pro

## Statistical Summary

| Metric | Count |
|--------|-------|
| Total words evaluated | 186 |
| **CRITICAL: form unacceptable** | 7 |
| **SEVERE: needs multiple lexemes** | 11 |
| **HIGH existing collision** | 3 |
| **QUESTIONABLE: eliminate** | 16 |
| **Clean/acceptable** | ~149 |

## 🔴 CRITICAL REJECTIONS — 7 Words

| Word | English | Problem | Replacement |
|------|---------|---------|-------------|
| **to** | toe | English preposition "to" — most frequent word | **pedi** or **digi** |
| **so** | saw | English conjunction "so" | **saa** or **saga** |
| **our** | hour | English possessive "our" | **hor** or **hora** |
| **but** | boot | English conjunction "but" | **bota** or **buta** |
| **pis** | peace | Phonetically "piss" (vulgar) | **pas** or **pat** |
| **shart** | shirt | English vulgar slang | **shat** or **shurt** |
| **auk** | owl | Wrong animal — "auk" is a real bird taxon | **ulu** (onomatopoeic) |

## 🟠 SEVERE POLYSEMY — 11 Words Need Splitting

| VELA Form | English | Must Split Into |
|-----------|---------|-----------------|
| **nail** | nail | (1) fingernail → **neil**; (2) metal fastener → **klav** |
| **fan** | fan | (1) blower → **fan**; (2) enthusiast → **suporta** |
| **left** | left | (1) direction → **left**; (2) departed → from **liv** |
| **ring** | ring | (1) jewelry → **ring**; (2) sound → **son** |
| **wotch** | watch | (1) timepiece → **wotch**; (2) observe → **obzerv** |
| **bank** | bank | (1) financial → **bank**; (2) riverside → **riv-bord** |
| **bil** | bill | (1) invoice → **bil**; (2) beak → **bik**; (3) law → compound |
| **sil** | seal | (1) animal → separate; (2) close → **klos-sig** |
| **tai** | tie | (1) necktie → **tai**; (2) fasten → **fiks** |
| **kap** | cap | (1) headwear → **kap**; (2) lid → **kovril**; (3) limit exists |
| **ber** | bear | (1) animal → **ber**; (2) carry → **kari**; (3) endure → **toler** |

## 🟡 EXISTING COLLISIONS — 3 Words

| Proposed | Conflict | Detail |
|----------|----------|--------|
| **lak** (luck) | **luk** (look/luck) | Redundant — "luk" already covers luck |
| **rait** (right-dir) | **rait** (right/write/white) | Already triple-loaded |
| **dir** (deer) | potential "dear" | Near-future collision |

## 🟢 QUESTIONABLE — 16 Words to Eliminate/Defer

**Exotic animals (10):** kamal, jiraf, kaigaru, koala, panda, skwiral, otar, gorila, krokodail, hai.po
**Non-core (6):** elefant, zebra, uniform, kostum, seramik, antisipashon

## Key Theoretical Insight

The recurring pattern: **English homonymy imported into VELA.** When English uses one form for multiple unrelated meanings, VELA inherits the ambiguity. This violates monosemy.

**Recommendation:** For every English source word with multiple unrelated senses, assign ONE sense to the borrowed form and create new roots or compounds for the others.

## Full Per-Word Analysis

See agent transcript for complete 186-word evaluation with CLARITY/COLLISION/POLYSEMY/NEEDED ratings.
