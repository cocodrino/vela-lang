# VELA Voting Process — Complete Reference

## Philosophy
VELA deliberations are not opinion polls. They are structured argumentation sessions where each model's unique training and reasoning patterns converge (or clash) over specific design decisions. The vote formalizes a consensus that already emerged from argumentation.

## The 6 Phases of Deliberation

### Phase 0: Graphify Context Extraction (MANDATORY)

**Before any topic is defined, the orchestrator MUST read the project knowledge graph.**

The project has a living knowledge graph at `graphify-out/GRAPH_REPORT.md` (auto-generated). This graph contains:
- **1036 nodes, 1046 edges** extracted from all project documents
- **25 detected communities** (e.g., "Case System Design", "Lexicon & Vocabulary")
- **God nodes** (highest centrality: README=40 edges, INITIAL_RESEARCH=29, ORTHOGRAPHY=23)
- **Betweenness centrality** scores showing cross-community bridges
- **Inferred edges** linking topics not obviously connected in raw text

**Why this is mandatory:** Graphify reveals relationships no single specialist would see. In the case system deliberation, graphify showed that "Case System Design" (34 nodes, 0.06 cohesion) had 30+ inferred edges to "Grammar Complete Reference" and "VELA Core Design" — proving the case system is a cross-cutting concern. This directly shaped the specialists' analyses.

**How to extract graphify insights:**
1. Read `graphify-out/GRAPH_REPORT.md`
2. Find the community matching your topic (Ctrl+F for keywords)
3. Note:
   - Community name and cohesion score
   - Cross-community connections (which other communities connect to this one)
   - God nodes linking into/out of this community
   - Any "surprising connections" flagged by the graph
4. Translate into linguistic insight: "Graphify: Case systems connect to {N} grammatical domains; central node is {X}; inferred edges suggest {Y}"

**Example from Case System deliberation:**
```
Graphify Insights:
- Community "Case System Design" (34 nodes, coheres with Grammar Complete Reference)
- 30 inferred edges from README ↔ case system cross-links
- Sound Symbolism community (53 nodes) peers with Case System in hierarchy
- Phonology Final Decisions (53 nodes) links into case design via VELA Core hub
```

These insights were embedded in EVERY specialist dossier.

---

### Phase 1: Topic Definition
**Orchestrator writes:** `vote/topics/current_topic.md`

Contains:
- Scope (one paragraph)
- Source files to embed in dossiers
- 3-5 focus questions
- Constraints (non-negotiable boundaries)
- **Graphify community identified** (e.g., "Case System Design")

**Example:** See `vote/templates/current_topic.md`

---

### Phase 2: Proposal Round (Parallel)
**5 specialists → 5 proposal files**

The orchestrator:
1. Reads all source files mentioned in `current_topic.md`
2. Reads `graphify-out/GRAPH_REPORT.md` for relevant communities
3. Builds 5 dossiers (one per specialist) with embedded source material + graphify insights
4. Launches all 5 specialists as **BACKGROUND** agents with `run_in_background: true`
5. Waits for all with `get_subagent_result(wait: true)`

**CRITICAL:** Subagents cannot use ANY file tools. All data must be in the prompt.

**Wait time:** 2-5 minutes (concurrency max 4)

**Output files:** `vote/topics/proposals/{phonologist,morphologist,lexicographer,semanticist,aestheticist}.md`

---

### Phase 3: Discussion Plan (Synthesis)
**Orchestrator reads all proposals and writes:** `vote/topics/discussion_plan.md`

For each distinct problem raised by ≥2 specialists:
- Assign a Discussion Point number
- Extract the common issue
- List all alternatives proposed
- Tag severity (use highest across agents)
- List source agents
- **Reference graphify connections** where relevant

**When to skip Phase 4:**
If proposals show STRONG convergence (≥3 agents identify the same 3-5 problems with similar alternatives), Phase 4 (individual point discussion) can be skipped and the orchestrator proceeds directly to Phase 5 (Consensus). This happened in the Case System deliberation.

---

### Phase 4: Point-by-Point Discussion (Conditional)
**Per point → 5 specialists argue**

For each Discussion Point where proposals disagreed:
1. Build a mini-dossier with: the point, all alternatives from Phase 2, and arguments FOR each alternative
2. Launch 5 specialists in parallel with prompt: "Given these alternatives, argue for your preferred option. Respond to other specialists' arguments."
3. Collect responses and write: `vote/topics/discussion/point_NN_{agent}.md`

**Skip condition:** If Phase 2 proposals already show convergence, skip to Phase 5.

---

### Phase 5: Voting Round
**Per point → 5 explicit votes**

For each discussion point:
1. Build a vote prompt with: the point, all alternatives, and previous arguments
2. Each specialist responds with EXACT format:
   ```
   VOTE: [A/B/C/current]
   Justification: [one sentence]
   ```
3. Orchestrator tallies votes

**Voting rules:**
- One vote per specialist per point
- Majority wins (3+ out of 5)
- Tie (2-2-1 or 2-3 split): Aestheticist preference breaks the tie (beauty principle prevails)
- Orchestrator casts a casting vote if the point is safety-critical

**Output:** `vote/topics/votes/point_NN_{agent}.md` (optional; can be embedded in consensus directly)

---

### Phase 6: Consensus & Summary
**Orchestrator writes:**
- `vote/topics/consensus/consensus.md` — decisions with implementation instructions
- `vote/SUMMARY.md` — executive overview with table of changes
- Appends `vote/docs/CHANGE_LOG.md`

---

## File Flow Diagram

```
graphify-out/GRAPH_REPORT.md
    │
    ▼
vote/topics/current_topic.md
    │
    ▼
┌─────────────────────────────────────────┐
│  Phase 2: 5 parallel specialist agents│
│  (background, dossier-embedded)         │
│  Each dossier includes graphify context │
└─────────────────────────────────────────┘
    │
    ▼
vote/topics/proposals/*.md
    │
    ▼
vote/topics/discussion_plan.md
    │
    ├─ If convergent ─┬─► vote/topics/consensus/consensus.md
    │                  │   vote/SUMMARY.md
    │                  │   vote/docs/CHANGE_LOG.md
    │                  │
    └─ If contested ──► Phase 4 (discussion) ──► Phase 5 (voting)
                               │
                               ▼
                    vote/topics/discussion/*.md
                    vote/topics/votes/*.md
                               │
                               ▼
                    vote/topics/consensus/consensus.md
                    vote/SUMMARY.md
                    vote/docs/CHANGE_LOG.md
```

## Vote Tallying Example

**Point 2: Plural+Case Order**
| Specialist | Vote |
|------------|------|
| Phonologist | A (man-se-s) |
| Morphologist | A (man-se-s) |
| Lexicographer | A (man-se-s) |
| Semanticist | A (man-se-s) |
| Aestheticist | B (vowel plural) |

**Tally:** A = 4, B = 1 → **Decision: A**

But wait — the aestheticist had a strong argument for B. The orchestrator notes this in the consensus:
- "Decision: A (root-case-plural) — 4/5 votes"
- "Dissent: Aestheticist advocated vowel plural `-a`; acknowledged but deferred to parsimony"
- "Graphify context: Sound Symbolism community suggests vowel-based marking could reinforce phonaesthetic goals; deferred to future phonology topic"

## Special Cases

### Agent Failure
If a specialist fails (0 output, timeout, error), the orchestrator:
1. Records the failure in `vote/SUMMARY.md`
2. Proceeds with available voices (minimum 3 needed for meaningful consensus)
3. For critical analysis areas, may supplement manually or rerun with simplified prompt

### Strong Convergence
When 3+ agents independently identify the same problems, the orchestrator can skip Phase 4 (discussion) and synthesize directly from proposals into consensus. This is not a shortcut — it's evidence that the problems genuinely exist across reasoning paradigms.

### Contradiction Between Aesthetic and Logical Arguments
When the aestheticist contradicts the logical/morphological consensus:
- **Default rule:** Logical consistency wins unless the aesthetic cost is catastrophic
- **But:** If all 4 logical specialists agree and aestheticist alone dissents, the aestheticist's concerns are noted as "future design considerations" rather than blockers
- **Exception:** If the aestheticist is the ONLY one defending a view and it's about VELA's core identity (beauty), the orchestrator may table the decision for a future dedicated aesthetic deliberation

## Quality Checklist
Before declaring a deliberation complete, verify:
- [ ] `graphify-out/GRAPH_REPORT.md` was consulted (not stale: run `graphify update .` if docs changed)
- [ ] `vote/SUMMARY.md` exists and has ≥1 approved change
- [ ] Each change has: what changed, why, exact implementation, priority
- [ ] Consensus cites which specialists agreed/disagreed
- [ ] No critical tool errors in any agent
- [ ] CHANGE_LOG.md was appended
- [ ] Source files are listed for implementation
