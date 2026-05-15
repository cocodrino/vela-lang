# VELA Deliberation Process

## Overview
This folder contains the **automated multi-agent deliberation system** for VELA language construction.

Five specialist agents (each running on a different Ollama Cloud model) analyze language design decisions, deliberate on alternatives, vote, and produce a final consensus document.

## ⚠️ CRITICAL: Ask User Before Every Deliberation

**Before starting any multi-agent review, you MUST ask the user:**

> "This topic requires a committee review. Should I use **pi-teams** (agents in terminal panes with full tools + mailbox) or **Agent tool** (background agents, more reliable but isolated)? Note: pi-teams requires interactive terminal (Warp, iTerm, tmux)."

**Use `ask_terminal` with `mode: confirm` for this question.**

### If user says YES to pi-teams:
- Check if user is in interactive terminal (Warp, iTerm, tmux, Zellij)
- If YES: Use `team_create`, `spawn_teammate`, `broadcast_message`, `read_inbox`
- If NO: Explain limitation, fall back to Agent tool
- See `vote/docs/TOOLS_AUDIT.md` for full pi-teams requirements

### If user says NO to pi-teams:
- Use `Agent` tool with `run_in_background: true`
- Parent orchestrator does ALL file I/O
- Subagents read files via `read_file` (Serena MCP) and return analysis as text
- See "Agent Tool Workflow" below

---

## Why Ask? Two Different Architectures

| Feature | pi-teams | Agent Tool |
|---------|----------|------------|
| Agent communication | ✅ Mailbox between agents | ❌ Isolated |
| Agent tool access | ✅ Full (read, write, bash) | ⚠️ read_file only |
| Requires terminal | ✅ Yes (tmux/Zellij/Warp) | ❌ No |
| Works in MCP | ❌ No | ✅ Yes |
| Setup complexity | Medium (create team, spawn) | Low (just launch) |
| File I/O | Agents write their own files | Parent writes all files |

**Key limitation discovered:** pi-teams crashes in MCP with "Extension ctx is stale after session replacement or reload." It requires an interactive TTY.

**Full audit:** `vote/docs/TOOLS_AUDIT.md`

---

## Agents

| Agent | Model | Specialty | Role |
|-------|-------|-----------|------|
| `vela_phonologist` | ollama/kimi-k2.6:cloud | Phonology, phonotactics, beauty of sound | Specialist |
| `vela_morphologist` | ollama/deepseek-v4-pro | Grammar, morphology, case systems | Specialist |
| `vela_lexicographer` | ollama/glm-5.1:cloud | Vocabulary, etymology, compounds | Specialist |
| `vela_semanticist` | ollama/deepseek-v4-pro | Logic, semantics, consistency | Specialist |
| `vela_aestheticist` | ollama/kimi-k2.6:cloud | Beauty, cadence, speaker experience | Specialist |
| `vela_orchestrator` | ollama/deepseek-v4-pro | Pipeline coordination, synthesis | Leader |

All agent definitions live in `.pi/agents/`.

---

## How to Run a Deliberation (Agent Tool — Default)

### Phase 0: Extract Graphify Context (MANDATORY)

Before writing the topic, read the project knowledge graph:
```
read_file({ relative_path: "graphify-out/GRAPH_REPORT.md" })
```

Extract community data, god nodes, cross-community connections. See `vote/docs/VOTING_PROCESS.md` for Phase 0 details.

### Phase 1: Define the Topic

Create `vote/topics/current_topic.md` with scope, source files, focus questions, constraints, and graphify context.

### Phase 2: Launch Specialists

Launch all 5 specialists in parallel via `Agent` with `run_in_background: true`.

**CRITICAL prompt instruction:** Tell subagents to use `read_file` (Serena MCP) to read documents. NEVER tell them to use native tools (`read`, `write`, `edit`, `bash`).

**Wait for all with `get_subagent_result(wait: true)`**

### Phase 3: Collect Results

The orchestrator (you) reads all responses and writes:
- `vote/topics/proposals/*.md` — archival copies
- `vote/topics/discussion_plan.md` — synthesized conflicts
- `vote/topics/consensus/consensus.md` — final decisions
- `vote/SUMMARY.md` — executive overview
- `vote/docs/CHANGE_LOG.md` — appended entry

---

## Memory Architecture (Filesystem as Shared State)

Since subagents cannot share memory directly, the filesystem acts as the shared workspace:

```
vote/topics/
  current_topic.md          ← Topic definition
  proposals/
    phonologist.md           ← Each agent writes here (via parent)
    morphologist.md
    lexicographer.md
    semanticist.md
    aestheticist.md
  discussion_plan.md        ← Orchestrator synthesizes this
  discussion/               ← Point-by-point arguments (if needed)
  votes/                    ← Explicit votes (if needed)
  consensus/
    consensus.md             ← Final decisions
```

This lets any agent (or human) inspect the full reasoning chain at any time.

---

## Tool Restrictions for Subagents

**Subagents launched via Agent tool CANNOT use:**
- `read`, `edit`, `write`, `bash` (native tools)
- `grep`, `find`, `ls` (native tools)
- `create_text_file`, `replace_content` (Serena write tools fail in subagents)

**Subagents CAN use:**
- `read_file` (Serena MCP) — for reading source documents
- `search_for_pattern` (Serena) — for finding content
- `get_symbols_overview` (Serena) — for code analysis

**Parent (you) must do ALL file writing.** The dossier pattern is: parent builds prompts with file paths, subagents read and analyze, parent collects text responses and writes all output files.

---

## Voting Rules
- Each specialist gets **one vote** per discussion point.
- Majority wins. In case of a tie, the aestheticist breaks it (beauty principle prevails).
- Abstentions are recorded but do not count toward or against.

---

## Adding a New Topic
1. Ask user: pi-teams or Agent tool?
2. Run graphify: `read_file({ relative_path: "graphify-out/GRAPH_REPORT.md" })`
3. Write a new `vote/topics/current_topic.md` (include graphify context).
4. Launch 5 specialists.
5. Synthesize and write consensus.

---

## Troubleshooting
- **Model not found**: Verify the model name matches your Ollama Cloud configuration.
- **Missing proposals**: An agent may have timed out. Continue with available voices (minimum 3).
- **Tied votes**: Check responses and manually review, or rerun with clearer alternatives.
- **Stale graphify**: If docs changed, run `graphify update .` before deliberation.
- **Agent stuck / no output**: Agent attempted to use disabled tools. Re-launch with explicit "use read_file only" instruction.

---

## Philosophy
This system embodies VELA's own principles: **logical** (structured process), **simple** (one file per task), and **beautiful** (each model brings a distinct voice, creating a richer consensus than any single model alone).

The documented architecture allows both pi-teams (when terminal is available) and Agent tool (fallback) — maximum flexibility with clear decision points.
