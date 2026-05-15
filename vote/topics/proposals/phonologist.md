# Proposal — VELA Phonologist (ollama/kimi-k2.6:cloud)

**Date:** 2026-05-14
**Topic:** Blocks 1-6 Word Review (186 new words)
**Agent:** vela_phonologist
**Model:** kimi-k2.6:cloud

## Summary

| Category | Count |
|----------|-------|
| Total proposed words | 186 |
| APPROVED | 62 |
| AMENDED | 94 |
| REJECTED | 30 |

## Rejected Words (30)

| Word | Reason | Suggested Fix |
|------|--------|---------------|
| wulf | Final /f/ not permitted; coda cluster /lf/ | wulo |
| foks | Final /s/ not permitted; coda cluster /ks/ | foki |
| mous | Invalid vowel /ou/; final /s/ not permitted | mau |
| fraug | Final /g/ not permitted | frau |
| tartl | Internal coda /r/; syllable "tl" lacks vowel | tatu |
| batn | Coda cluster /tn/ phonotactically invalid | batu |
| bakpak | Internal coda /k/ in "bak"; final /k/ not permitted | bapaku |
| sutkes | Internal coda /t/ in "sut"; final /s/ not permitted | sutike |
| soul | Invalid vowel /ou/ | soli |
| akount | Invalid vowel /ou/; final cluster /nt/ | akau |
| lengt | Coda cluster /ngt/; no clear nucleus | len |
| widt | Coda cluster /dt/; final /t/ not permitted | widi |
| niaz | Ambiguous nucleus; final /z/ not permitted | niasi |
| lethr | Syllable "thr" lacks vowel; /th/ not in inventory | lera |
| masl | Coda cluster /sl/ | masil |
| ovn | Vowel-initial with coda cluster /vn/; no valid syllable | ovu |
| ovr | Vowel-initial with coda cluster /vr/ | ovar |

## ⚠️ CRITICAL DISCOVERY: ~30 Existing Words Violate Phonotactics

The phonologist flagged these **existing** VELA words as phonotactically invalid under strict (C)V rules:

**Final consonant violations:** ok(/k/), nos(/s/), nek(/k/), dog(/g/), kat(/t/), haid(/d/), maut(/t/), fud(/d/), buk(/k/), eat(/t/), wok(/k/), want(/nt/), help(/lp/), think(/nk/), tung(/ng/), leg(/g/), fut(/t/), hed(/d/), brid(/d/), hors(/s/), fish(/sh/), hous(/s/), drink(/nk/), sleep(/lp/)

**Internal coda violations:** boksi(/k/), forki(/r/), porki(/r/), shou(/ou/), nou(/ou/)

**Ambiguous/flagged:** ear(/ea/), arm(/rm/), water(/r/)

**Implication:** The existing VELA lexicon contains ~30 words that violate strict (C)V phonotactics. Either:
1. The phonotactic rules are more permissive than stated (e.g., word-final /d,t,k,g,s,p,f,sh/ are actually allowed in practice)
2. The existing lexicon needs systematic phonotactic reform
3. The (C)V rule applies only to syllable structure, not word-final position

This requires clarification before approving new words.

## Top 5 Most Beautiful (corrected forms)

1. baflai (9) — liquid diphthong glide, perfect (C)V.(C)V cadence
2. koala (8) — triple hiatus melody, very euphonious
3. dureshon (8) — sonorant-final, flowing open syllables
4. hai.po (8) — crisp diphthong + open vowel contrast
5. vidio (8) — clear (C)V.(C)V structure, pleasant vowel alternation
