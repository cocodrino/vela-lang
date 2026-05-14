# Update to Consensus — Standby Issues Resolution (Revised)

## Number System Override (User Request)

**Revised Decision** (2026-05-13):

| # | Form | Type | Rationale |
|---|------|------|-----------|
| 0–10 | `zero, wan, tu, tri, kwatro, faiv, siks, sevn, eit, nain, ten` | **Atomic** | Primitives, universally recognized |
| 11–19 | `ten-wan, ten-tu, ten-tri, ten-kwatro, ten-faiv, ten-siks, ten-sevn, ten-eit, ten-nain` | **Compound** | `10 + N`, transparent, deducible |
| 20–90 | `tu-ten, tri-ten, kwatro-ten, faiv-ten, siks-ten, sevn-ten, eit-ten, nain-ten` | **Compound** | `N × 10`, transparent, deducible |
| 21–99 | `tu-ten-wan, tu-ten-tu...` | **Compound** | `(N×10) + M`, recursive |
| 100 | `kent` /kent/ | **ATOMIC** | Latin *centum*, 1 syllable, Romance: cien/cent/cento |
| 101–999 | `kent-wan, kent-tu...` | **Compound** | recursive |
| 1000 | `mil` /mil/ | **ATOMIC** | Latin *mille*, 1 syllable, Romance: mil/mille |
| 1001–999999 | `mil-wan, mil-kent...` | **Compound** | recursive |
| 1,000,000 | `miliyun` | **Atomic** | International loan, vowel-final |

### Reason for Override
The user ruled that `ten-ten` (100) and `ten-ten-ten` (1000) are **too verbose**. Milestone numbers (100, 1000) should have short atomic forms for pragmatic efficiency in formal/financial contexts. The lexicographer's original suggestion (`kent` / `mil`) is now the adopted standard.

---

## Open Issue — Profession Suffix

**Status**: Pending deliberation. User explicitly rejected `-man` for gender-inclusivity reasons.

**Queued for next deliberation**: What suffix should indicate "person who does X" in professions? The user suggests `X-person` or similar. Must be phonologically valid, gender-neutral, internationally recognizable, and short.

**Current candidates to deliberate**:
- `-po` (from "person", but needs international justification)
- `-pe` (from "person", 1 syllable, vowel-final)
- No suffix at all: context determines person (Japanese model: `sensei` = teacher without "person" marker)
- A different compounding pattern entirely: `lern-place`, `sik-fix-place`
- Latin-derived: `-or` (doctor→doktr, but not gender-neutral in many minds)

**Topic file**: `vote/topics/profession_suffix.md` (to be created)

---
*Consensus updated: 2026-05-13*
*Number system: user-overridden to atomic 100/1000*
*Profession suffix: deferred to next deliberation*
