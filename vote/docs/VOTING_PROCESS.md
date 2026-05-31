# VELA Voting Process — Complete Reference (pi-teams Architecture)

## Philosophy
VELA deliberations are not opinion polls. They are structured argumentation sessions where each model's unique training and reasoning patterns converge (or clash) over specific design decisions. The vote formalizes a consensus that already emerged from argumentation.

**New with pi-teams:** Teammates have full tool access and can communicate via shared mailbox. This eliminates the dossier pattern — agents read source files directly and respond to each other's arguments in real time.

---

## The 7 Phases of Deliberation

### Phase 0: Graphify Context Extraction (MANDATORY)

**Before any topic is defined, the orchestrator (Leader) MUST read the project knowledge graph.**

The project has a living knowledge graph at `graphify-out/GRAPH_REPORT.md` (auto-generated). This graph contains:
- **Nodes and edges** extracted from all project documents
- **Detected communities** (e.g., "Case System Design", "Lexicon & Vocabulary")
- **God nodes** (highest centrality)
- **Betweenness centrality** scores showing cross-community bridges
- **Inferred edges** linking topics not obviously connected in raw text

**Why this is mandatory:** Graphify reveals relationships no single specialist would see. In the case system deliberation, graphify showed that "Case System Design" had 30+ inferred edges to "Grammar Complete Reference" and "VELA Core Design" — proving the case system is a cross-cutting concern.

**How to extract graphify insights:**
1. Read `graphify-out/GRAPH_REPORT.md`
2. Find the community matching your topic (Ctrl+F for keywords)
3. Note:
   - Community name and cohesion score
   - Cross-community connections (which other communities connect to this one)
   - God nodes linking into/out of this community
   - Any "surprising connections" flagged by the graph
4. Translate into linguistic insight

---

### Phase 1: Topic Definition & Task Creation

**Orchestrator (Leader) writes:** `vote/topics/current_topic.md`

Contains:
- Scope (one paragraph)
- Source files relevant to the discussion
- 3-5 focus questions
- Constraints (non-negotiable boundaries)
- **Graphify community identified**

Then the Leader **creates a task** in the pi-teams task board:
```
task_create({ team_name: "vela", subject: "VELA Deliberation: [Topic Name]", description: "[Brief description + link to current_topic.md]" })
```

The task is shared with all 5 teammates.

---

### Phase 2: Proposal Round (Parallel)

**Orchestrator (Leader) broadcasts a message to the team:**
```
broadcast_message({ team_name: "vela", summary: "New deliberation started", content: "New deliberation: [Topic]. Please read vote/topics/current_topic.md and the listed source files, then post your initial proposal to the mailbox with hashtag #proposal." })
```

**How it works with pi-teams:**
1. Each teammate reads `vote/topics/current_topic.md` directly (no dossier needed — they have file access)
2. Each teammate reads the relevant source files directly
3. Each teammate posts their structured analysis to the **team mailbox** with tag `#proposal`
4. All teammates can see each other's proposals as they arrive

**Wait time:** 2-5 minutes (teammates run in parallel)

**No more dossiers!** Teammates use `read_file` to access source material directly.

---

### Phase 3: Synthesis & Discussion Plan

**Leader reads all mailbox proposals and writes:** `vote/topics/discussion_plan.md`

For each distinct problem raised by ≥2 specialists:
- Assign a Discussion Point number
- Extract the common issue
- List all alternatives proposed
- Tag severity (use highest across agents)
- List source agents

**Leader broadcasts to team:**
```
broadcast_message({ team_name: "vela", summary: "Discussion plan published", content: "Discussion plan published: vote/topics/discussion_plan.md. Review other agents' positions and prepare arguments for conflicting points." })
```

---

### Phase 4: Point-by-Point Deliberation (Conditional)

**For each Discussion Point where proposals disagreed:**

1. Leader posts to mailbox:
```
broadcast_message({ team_name: "vela", summary: "Deliberation Point N", content: "POINT N: [Issue summary]. Alternatives: A) [option], B) [option]. Please argue for your preferred option and respond to other specialists. Tag: #deliberation-N" })
```

2. Each teammate posts their arguments to the mailbox with the point tag
3. Teammates can **directly respond** to each other's arguments (reply-to threading)
4. Leader reads the threaded discussion via `read_inbox`

**Skip condition:** If Phase 2 proposals already show strong convergence (≥3 agents agree), skip to Phase 5.

---

### Phase 5: Voting Round

**Leader updates the task status:**
```
task_update({ team_name: "vela", task_id: "[id]", status: "voting" })
```

**Leader broadcasts:**
```
broadcast_message({ team_name: "vela", summary: "VOTING ROUND Point N", content: "VOTING ROUND for Point N: [issue]. Options: A) [desc], B) [desc]. Vote with EXACT format: VOTE: [A/B/C/current] Justification: [one sentence]. Tag: #vote-N" })
```

**Each specialist posts their vote to the mailbox with the vote tag.**

**Voting rules:**
- One vote per specialist per point
- Majority wins (3+ out of 5)
- Tie (2-2-1 or 2-3 split): Aestheticist preference breaks the tie (beauty principle prevails)
- Leader casts a casting vote if the point is safety-critical

---

### Phase 6: Consensus & Summary

**Orchestrator (Leader) writes:**
- `vote/topics/consensus/consensus.md` — decisions with implementation instructions
- `vote/SUMMARY.md` — executive overview with table of changes
- Appends `vote/docs/CHANGE_LOG.md`

**Leader broadcasts completion:**
```
broadcast_message({ team_name: "vela", summary: "Deliberation complete", content: "Deliberation complete. Consensus published: vote/SUMMARY.md. Task status: completed." })
```

**Leader updates task:**
```
task_update({ team_name: "vela", task_id: "[id]", status: "completed" })
```

---

## File Flow Diagram

```
graphify-out/GRAPH_REPORT.md
    │
    ▼
vote/topics/current_topic.md  ← Leader creates
    │
    ▼
┌─────────────────────────────────────────┐
│  Phase 2: 5 parallel teammate agents  │
│  (read files directly, no dossiers)     │
│  Post proposals to team mailbox         │
└─────────────────────────────────────────┘
    │
    ▼
vote/topics/proposals/ (archived)  ← Leader may copy from mailbox
    │
    ▼
vote/topics/discussion_plan.md  ← Leader writes
    │
    ├─ If convergent ─┬─► vote/topics/consensus/consensus.md
    │                  │   vote/SUMMARY.md
    │                  │   vote/docs/CHANGE_LOG.md
    │                  │   Team mailbox: #completed
    │                  │
    └─ If contested ──► Phase 4 (mailbox deliberation)
                               │
                               ▼
                    Team mailbox: #deliberation-N
                               │
                               ▼
                    Phase 5 (mailbox voting): #vote-N
                               │
                               ▼
                    vote/topics/consensus/consensus.md
                    vote/SUMMARY.md
                    vote/docs/CHANGE_LOG.md
                    Team mailbox: #completed
```

---

## Vote Tallying Example

**Point 2: Plural+Case Order**
| Specialist | Vote |
|------------|------|
| Phonologist | A (man-se-n) |
| Morphologist | A (man-se-n) |
| Lexicographer | A (man-se-n) |
| Semanticist | A (man-se-n) |
| Aestheticist | B (vowel plural) |

**Tally:** A = 4, B = 1 → **Decision: A**

Leader notes in consensus:
- "Decision: A (root-case-plural) — 4/5 votes"
- "Dissent: Aestheticist advocated vowel plural `-a`; acknowledged but deferred to parsimony"

---

## Special Cases

### Agent Failure
If a teammate fails (0 output, timeout, error):
1. Leader records the failure in `vote/SUMMARY.md`
2. Proceeds with available voices (minimum 3 needed for meaningful consensus)
3. For critical analysis areas, may supplement manually or rerun with simplified prompt
4. Check teammate status with: `check_teammate({ team_name: "vela", agent_name: "vela_phonologist" })`

### Strong Convergence
When 3+ agents independently identify the same problems, the Leader can skip Phase 4 (discussion) and synthesize directly from proposals into consensus.

### Contradiction Between Aesthetic and Logical Arguments
When the aestheticist contradicts the logical/morphological consensus:
- **Default rule:** Logical consistency wins unless the aesthetic cost is catastrophic
- **But:** If all 4 logical specialists agree and aestheticist alone dissents, the aestheticist's concerns are noted as "future design considerations"
- **Exception:** If the aestheticist is the ONLY one defending a view and it's about VELA's core identity (beauty), the Leader may table the decision

---

## pi-teams Workflow Quick Reference

```
# 1. Create team (one-time setup)
team_create({ team_name: "vela", description: "VELA language construction committee" })

# 2. Spawn teammates
spawn_teammate({ team_name: "vela", name: "vela_phonologist", prompt: "...", cwd: "." })
spawn_teammate({ team_name: "vela", name: "vela_morphologist", prompt: "...", cwd: "." })
# ... etc for all 5 specialists

# 3. Create task
task_create({ team_name: "vela", subject: "VELA: Case System Review", description: "..." })

# 4. Broadcast message
broadcast_message({ team_name: "vela", summary: "New deliberation", content: "..." })

# 5. Read mailbox
read_inbox({ team_name: "vela" })

# 6. Check teammate status
check_teammate({ team_name: "vela", agent_name: "vela_phonologist" })

# 7. Update task
task_update({ team_name: "vela", task_id: "[id]", status: "completed" })

# 8. Shutdown
team_shutdown({ team_name: "vela" })
```

---

## Quality Checklist
Before declaring a deliberation complete, verify:
- [ ] `graphify-out/GRAPH_REPORT.md` was consulted (not stale)
- [ ] `vote/SUMMARY.md` exists and has ≥1 approved change
- [ ] Each change has: what changed, why, exact implementation, priority
- [ ] Consensus cites which specialists agreed/disagreed
- [ ] No critical tool errors in any teammate
- [ ] CHANGE_LOG.md was appended
- [ ] Task board shows status = completed
- [ ] All teammates responded (or failure documented)
