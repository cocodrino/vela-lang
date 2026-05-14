# VELA Deliberation Skill

## When to Use
- When a language design decision in VELA needs structured multi-perspective evaluation.
- When you want more than one AI opinion before committing to a grammatical or lexical change.
- When the topic spans multiple subsystems (sound, grammar, vocabulary, meaning, beauty).

## When NOT to Use
- For trivial edits (fixing typos, formatting).
- When speed is more important than thoroughness.

## CRITICAL: Agent Tool Restrictions

Subagents spawned by pi-subagents **cannot access Serena tools** (`read_file`, `create_text_file`, etc.) and **cannot use native tools** (`read`, `bash`, `write`, `edit`, `grep`, `find`, `ls`). ALL of these tools return errors for subagents.

### What This Means
- ❌ Do NOT instruct subagents to "read files" or "write files"
- ❌ Do NOT instruct subagents to use `bash`, `ls`, or any filesystem commands
- ❌ Do NOT instruct subagents to use `edit` or `write`
- ✅ Instead: **Embed ALL source material directly in the prompt** (dossier approach)
- ✅ Subagents should ONLY return structured text responses
- ✅ The parent orchestrator handles ALL file I/O

## The Dossier Pattern (Required)

Because subagents cannot read files, you must embed the relevant content:

```
Agent({
  subagent_type: "vela_phonologist",
  prompt: `
    You are the VELA Phonologist.
    
    ## SOURCE MATERIAL (embedded — do NOT use file tools)
    [PASTE relevant sections here]
    
    ## GRAPHIFY INSIGHTS (embedded — extracted by orchestrator)
    [PASTE community data here]
    
    ## YOUR TASK
    [Specific question]
    
    Return your analysis in this EXACT format:
    ## PROBLEMS IDENTIFIED
    ### Problem 1: [title]
    - Severity: critical/high/medium/low
    - Description: [2-3 sentences]
    - Proposed Alternatives:
      - A: [description]
      - B: [description]
    - Justification: [reference]
  `,
  description: "VELA topic analysis",
  run_in_background: true,
  model: "ollama/kimi-k2.6:cloud"  // or whichever specialist
})
```

## MANDATORY Phase 0: Graphify Context Extraction

Every deliberation MUST begin with graphify analysis. The project has a living knowledge graph at `graphify-out/GRAPH_REPORT.md`.

### Why Graphify is Mandatory
- Graphify connects topics across documents that humans (or individual models) might miss
- It reveals **cross-community dependencies**: "Case System Design" connects to "Phonology", "Grammar", "Lexicon"
- It surfaces **unexpected connections**: README's high betweenness centrality means design decisions radiate outward
- It prevents specialists from analyzing problems in isolation

### How to Extract Graphify Insights

**Step 1:** Read `graphify-out/GRAPH_REPORT.md`

**Step 2:** Find your topic's community:
```
Ctrl+F for keywords like "Case", "Phonology", "Lexicon", "Morphology"
```

**Step 3:** Extract these fields:
| Field | What to look for |
|-------|-----------------|
| **Community name** | e.g., "_COMMUNITY_Case System Design" |
| **Cohesion** | Higher = more tightly connected (0.02–0.22 range) |
| **Node count** | How many concepts in this community |
| **Cross-community links** | Which other communities connect to this one |
| **God nodes** | Highest-centrality nodes bridging communities |
| **Inferred edges** | Model-reasoned connections (may need verification) |

**Step 4:** Include in EVERY dossier. Each specialist should see:
- The community relevant to their domain
- Cross-domain connections that affect their analysis
- The overall project structure (from god nodes)

**Example graphify block for a dossier:**
```markdown
### GRAPHIFY PROJECT KNOWLEDGE GRAPH
The VELA project has 1036 concepts across 25 communities. Relevant to your analysis:

- **Case System Design** community: 34 nodes, cohesion 0.06
  - Connected to: Grammar Complete Reference, VELA Core Design, Sound Symbolism
  - Central node: README (betweenness 0.178) — all design decisions radiate outward
  - 30 inferred edges linking case system to broader grammar

- **Phonology Final Decisions** community: 53 nodes, peers with Case System in hierarchy
  - Cross-link: Phonology → Case System via VELA Core hub
  - Sound symbolism links vowel quality (/e/ = small/delicate) to semantic domains
```

### Graphify Staleness Warning
If documents were edited since `GRAPH_REPORT.md` was generated, the graph may be stale.
- Check `.graphify_detect.json` for last generation date
- Regenerate if needed: `graphify update .`
- For the case system deliberation, graphify was generated 2026-05-13 (same day) and was current

## Procedure

### Step 1: Prepare the Topic
Write `vote/topics/current_topic.md` using the template in `vote/templates/current_topic.md`.

### Step 2: Graphify Context (MANDATORY)
1. Read `graphify-out/GRAPH_REPORT.md`
2. Identify the community matching your topic
3. Extract cross-community connections, god nodes, inferred edges
4. Build a graphify summary block for all dossiers

### Step 3: Build Dossiers
For each specialist, read the relevant source files via `read_file` (Serena tools), then build a single prompt containing:
1. **Graphify insights** (see Phase 0 above)
2. The agent's role description
3. Embedded source material from current_topic.md and relevant docs
4. Specific tasks and output format

### Step 4: Launch Specialists in Parallel
Launch all 5 specialists simultaneously as BACKGROUND agents with `run_in_background: true`. Each gets its own dossier (including the same graphify block + domain-specific sources).

### Step 5: Collect Results
Use `get_subagent_result({ agent_id, wait: true, verbose: true })` for each agent. The parent orchestrator manually handles file I/O.

### Step 6: Write Proposals
The orchestrator extracts structured output from each agent's response and writes to `vote/topics/proposals/{agent}.md`.

### Step 7: Synthesize Discussion Plan
The orchestrator reads all proposals and writes `vote/topics/discussion_plan.md` with consolidated points.

### Step 8: Point-by-Point Discussion (Optional)
For complex or contested points, relaunch specialists with the discussion point + previous arguments. Use dossiers with embedded context.

### Step 9: Voting Round
For each point, prompt each specialist to vote: "Vote for ONE option: A, B, or keep current. Return ONLY 'VOTE: [letter]' followed by one sentence justification."

### Step 10: Write Consensus
The orchestrator tallies votes (majority wins; aestheticist has tie-break authority) and writes `vote/topics/consensus/consensus.md`.

### Step 11: Final Summary
Write `vote/SUMMARY.md` with executive overview and table of changes.

## Pipeline Command Reference

**Phase 0 — Graphify (mandatory):**
```javascript
// Orchestrator reads graphify-out/GRAPH_REPORT.md
// Extracts community data into graphifySummary variable
```

**Phase 1 — Proposals (parallel):**
```javascript
Agent({ subagent_type: "vela_phonologist", prompt: graphifySummary + dossier_phonology, description: "VELA proposals", run_in_background: true })
Agent({ subagent_type: "vela_morphologist", prompt: graphifySummary + dossier_morphology, description: "VELA proposals", run_in_background: true })
Agent({ subagent_type: "vela_lexicographer", prompt: graphifySummary + dossier_lexicon, description: "VELA proposals", run_in_background: true })
Agent({ subagent_type: "vela_semanticist", prompt: graphifySummary + dossier_semantics, description: "VELA proposals", run_in_background: true })
Agent({ subagent_type: "vela_aestheticist", prompt: graphifySummary + dossier_aesthetics, description: "VELA proposals", run_in_background: true })
```

**Phase 2 — Synthesis** (parent agent manually):
```javascript
// Read all proposal files
// Include graphify connections in discussion_plan.md
// Write discussion_plan.md
```

**Phase 3-4 — Discussion & Voting** (parallel per point):
```javascript
for (point in discussion_plan) {
  Agent({ subagent_type: "vela_phonologist", prompt: `Point ${point}: vote A/B/C. Context: [embedded]`, description: "Vote", run_in_background: true })
  Agent({ subagent_type: "vela_morphologist", prompt: `Point ${point}: vote A/B/C. Context: [embedded]`, description: "Vote", run_in_background: true })
  // ... etc
}
```

## Voting Rules
- One vote per specialist per discussion point
- Majority wins
- In case of tie: aestheticist's preference breaks it (beauty is VELA's tie-breaker)
- Abstentions recorded but do not count
- Orchestrator can override if safety/logic is compromised

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Subagent "Tool disabled" errors | Subagent tried to use Serena/native tools explicitly | Ensure prompt says "Do NOT use file tools" and dossier contains all data |
| Subagent 0% output, 0 tools | Model did not understand the request or tools are misconfigured | Simplify prompt; remove tool instructions; use shorter format |
| qwen2.5-coder/gpt-5.1 fails | Known issue with some models in Ollama | Replace with deepseek-v4-pro (tested and reliable) |
| Long deliberation time | Each agent takes ~60-120s; 5 agents = slow | Run in parallel (max 4 concurrent); batch discussion points |
| Convergent proposals | All agents found same problems | Skip Phase 3-4; synthesize directly into consensus (as happened for case system) |
| Graphify graph seems old | graphify-out/ was generated before recent doc edits | Run `graphify update .` to regenerate |
| Graphify community not found | Topic uses different terminology than graph | Search for synonyms; graphify may have named it differently |

## Verification
After a run, check:
- `graphify-out/GRAPH_REPORT.md` was consulted (not stale)
- `vote/SUMMARY.md` exists and has ≥1 approved change
- `vote/topics/consensus/consensus.md` has implementation instructions per point
- No agent reported critical tool errors

## Models Currently in Use
| Agent | Model | Status |
|-------|-------|--------|
| Phonologist | ollama/kimi-k2.6:cloud | ✅ Reliable |
| Morphologist | ollama/deepseek-v4-pro | ✅ Reliable |
| Lexicographer | ollama/glm-5.1:cloud | ✅ Reliable |
| Semanticist | ollama/deepseek-v4-pro | ✅ Reliable |
| Aestheticist | ollama/kimi-k2.6:cloud | ✅ Reliable |
