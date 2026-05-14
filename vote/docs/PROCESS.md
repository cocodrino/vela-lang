# VELA Deliberation Process

## Overview
This folder contains the **automated multi-agent deliberation system** for VELA language construction.

Five specialist agents (each running on a different Ollama Cloud model) analyze language design decisions, deliberate on alternatives, vote, and produce a final consensus document.

**Every deliberation MUST begin with graphify context extraction.** The project has a living knowledge graph at `graphify-out/GRAPH_REPORT.md` that connects topics across all documents. See Phase 0 below.

## Agents

| Agent | Model | Specialty |
|-------|-------|-----------|
| `vela_phonologist` | ollama/kimi-k2.6:cloud | Phonology, phonotactics, beauty of sound |
| `vela_morphologist` | ollama/deepseek-v4-pro | Grammar, morphology, case systems |
| `vela_lexicographer` | ollama/glm-5.1:cloud | Vocabulary, etymology, compounds |
| `vela_semanticist` | ollama/deepseek-v4-pro | Logic, semantics, consistency |
| `vela_aestheticist` | ollama/kimi-k2.6:cloud | Beauty, cadence, speaker experience |
| `vela_orchestrator` | ollama/deepseek-v4-pro | Pipeline coordination, synthesis |

All agent definitions live in `.pi/agents/`.

## How to Run a Deliberation

### Phase 0: Extract Graphify Context (MANDATORY)

Before writing the topic, read the project knowledge graph:

```
read_file({ relative_path: "graphify-out/GRAPH_REPORT.md" })
```

Extract:
1. The community matching your topic (e.g., search "Case System" or "Phonology")
2. Node count and cohesion score
3. Cross-community connections
4. God nodes linking into/out of this community

**Why mandatory:** Graphify reveals hidden connections. The case system deliberation found that "Case System Design" had 30+ inferred edges to other grammatical communities — proving the case system is a cross-cutting concern that specialists must account for.

**If graphify seems stale** (older than your latest doc edits), regenerate:
```bash
graphify update .
```

### Phase 1: Define the Topic
Create or edit `vote/topics/current_topic.md`.

Example:
```markdown
# Topic: Phonological Inventory Re-evaluation

## Scope
Review the current consonant inventory for accessibility and beauty.

## Source files to analyze
- docs/phonology/PHONOLOGY_FINAL.md
- README.md (phonology section)

## Focus questions
1. Are 17 consonants truly minimal yet complete?
2. Does the absence of /ʃ/ (sh) vs /s/ create recognizability issues?
3. Is the (C)V syllable structure too restrictive for loanwords?

## Graphify context
- Community: "Phonology Final Decisions" (53 nodes, 0.04 cohesion)
- Cross-links: Phonology → "VELA Core Design" → "Sound Symbolism" (53 nodes)
- Key node: README (40 edges, highest betweenness centrality)
- Inferred edge: Phonology research → Phonology final decisions
```

### Phase 2: Launch the Specialists

The orchestrator reads all source files, builds dossiers with graphify context embedded, and launches specialists:

```
Agent({
  subagent_type: "vela_phonologist",
  prompt: dossier_with_graphify,
  description: "VELA phonology analysis",
  run_in_background: true
})
```

Then wait for notification, or check with:
```
get_subagent_result({ agent_id: "...", wait: true, verbose: false })
```

### Phase 3: Collect Results
The orchestrator produces:
- `vote/SUMMARY.md` — final summary of all changes
- `vote/topics/consensus/consensus.md` — detailed consensus per point
- `vote/docs/CHANGE_LOG.md` — appended changelog entry

## Memory Architecture (Filesystem as Shared State)

Since subagents do not share memory directly, the filesystem acts as the shared workspace:

```
vote/topics/
  current_topic.md          ← Topic definition (includes graphify context)
  proposals/
    phonologist.md         ← Each agent writes here
    morphologist.md
    lexicographer.md
    semanticist.md
    aestheticist.md
  discussion_plan.md        ← Orchestrator synthesizes this
  discussion/
    point_01_overview.md
    point_01_phonologist.md
    point_01_morphologist.md
    ...
  votes/
    point_01_phonologist.md
    ...
  consensus/
    consensus.md             ← Final decisions
```

This lets any agent (or human) inspect the full reasoning chain at any time.

## Voting Rules
- Each specialist gets **one vote** per discussion point.
- Majority wins. In case of a tie, the aestheticist breaks it (beauty principle prevails).
- Abstentions are recorded but do not count toward or against.

## Adding a New Topic
1. Run graphify: `read_file({ relative_path: "graphify-out/GRAPH_REPORT.md" })`
2. Write a new `vote/topics/current_topic.md` (include graphify context).
3. Optionally clear `vote/topics/proposals/`, `vote/topics/discussion/`, and `vote/topics/votes/` if you want a clean run.
4. Launch 5 specialists in parallel.

## Customizing a Run
- Edit `.pi/agents/vela_orchestrator.md` to change the pipeline.
- Edit individual specialist `.md` files to adjust their analytical focus.
- Change models in frontmatter if you want different providers.
- **Graphify is mandatory** — never skip Phase 0. It prevents specialists from analyzing in isolation.

## Troubleshooting
- **Model not found**: Verify the model name matches your Ollama Cloud configuration.
- **Missing proposal files**: An agent may have timed out. The orchestrator continues with available voices.
- **Tied votes**: Check `vote/topics/votes/` and manually review, or rerun the point with clearer alternatives.
- **Stale graphify**: If docs changed since `GRAPH_REPORT.md` was generated, run `graphify update .` before the next deliberation.

## Philosophy
This system embodies VELA's own principles: **logical** (structured process), **simple** (one file per task), and **beautiful** (each model brings a distinct voice, creating a richer consensus than any single model alone).
