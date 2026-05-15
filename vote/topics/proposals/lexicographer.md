# Proposal — VELA Lexicographer (ollama/glm-5.1:cloud)

**Date:** 2026-05-14
**Topic:** Blocks 1-6 Word Review (186 new words)
**Agent:** vela_lexicographer
**Model:** glm-5.1:cloud

## Overall Quality Score: 5.2 / 10

### Summary
The proposed 186 words suffer from three systemic problems:
1. ~70% end in consonants, violating the vowel-final convention
2. ~40% are English-only with no Romance/Greek/Latin crossover
3. 7 critical semantic collisions with major world languages

### Critical Collisions (MUST FIX)
| Word | English | Problem | Suggested Replacement |
|------|---------|---------|----------------------|
| **pis** | peace | = "piss" (vulgar) in French | **paco** |
| **bon** | bone | = "good" in Romance | **osto** |
| **los** | loss | = "the" (plural) in Spanish | **perdo** |
| **saut** | south | = "leap" in French | **sudo** |
| **ist** | east | = "is" in German | **esto** |
| **naif** | knife | = "naïve" in French | **kuchilo** |
| **so** | saw | = conjunction in English/German | **segilo** |

### Top 20 Most Recognizable (Keep/Minor Fix)
| # | Word | English | Score |
|---|------|---------|-------|
| 1 | moskito | mosquito | HIGH ✓ |
| 2 | koala | koala | HIGH ✓ |
| 3 | panda | panda | HIGH ✓ |
| 4 | gorila | gorilla | HIGH ✓ |
| 5 | umbrela | umbrella | HIGH ✓ |
| 6 | zebra | zebra | HIGH ✓ |
| 7 | vidio | video | HIGH ✓ |
| 8 | kamera | camera | HIGH ✓ |
| 9 | foto | photo | HIGH ✓ |
| 10 | bateri | battery | HIGH ✓ |
| 11 | sandali | sandals | HIGH ✓ |
| 12 | dolfin | dolphin | HIGH (add vowel) |
| 13 | pengwin | penguin | HIGH (add vowel) |
| 14 | kamal | camel | HIGH (add vowel) |
| 15 | jiraf | giraffe | HIGH (add vowel) |
| 16 | elefant | elephant | HIGH (add vowel) |
| 17 | krokodail | crocodile | HIGH (add vowel) |
| 18 | ekonomi | economy | HIGH ✓ |
| 19 | aidia | idea | HIGH ✓ |
| 20 | medi | media | HIGH ✓ |

### 20 Least Recognizable (Need Replacement)
| # | Word | English | Issue | Better Form |
|---|------|---------|-------|-------------|
| 1 | **pis** | peace | French vulgar | **paco** |
| 2 | **bon** | bone | Romance "good" | **osto** |
| 3 | **los** | loss | Spanish article | **perdo** |
| 4 | **saut** | south | French "leap" | **sudo** |
| 5 | **ist** | east | German "is" | **esto** |
| 6 | **to** | toe | Infinitive marker | **pied-digito** |
| 7 | **so** | saw | Conjunction | **segilo** |
| 8 | **naif** | knife | French "naïve" | **kuchilo** |
| 9 | **erkweik** | earthquake | Opaque portmanteau | **sismo** |
| 10 | **niaz** | news | Unrecognizable | **novajo** |
| 11 | **raba** | rubber | No etymological link | **kauchuo** |
| 12 | **sil** | seal | 3-letter collision | **foko** |
| 13 | **igol** | eagle | No resemblance | **akwilo** |
| 14 | **auk** | owl | Wrong animal name! | **buho** |
| 15 | **dak** | duck | Unrecognizable | **anaso** |
| 16 | **shart** | shirt | English vulgar slang | **shirto** |
| 17 | **ap** | up | 2-letter collision | **supra** |
| 18 | **bilou** | below | Opaque spelling | **infra** |
| 19 | **andar** | under | Hindi collision | **subo** |
| 20 | **our** | hour | English possessive | **horo** |

### Major Recommendations
1. **Fix 7 critical collisions immediately**
2. **Add terminal -o to ~130 words** ending in illegal consonants
3. **Replace English-only animal names** with Latin roots (ber→urso, wulf→lupo, foks→vulpo, dir→cervo)
4. **Replace direction terms** with international forms (nort→nordo, ap→supra, daun→infra)
5. **Eliminate opaque abbreviations** (hai.po→hipopotamo, erkweik→sismo)

### Full Per-Word Analysis
See full transcript for all 186 words evaluated.
