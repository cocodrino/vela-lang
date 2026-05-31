---
name: vela-deliberation
description: Run a structured VELA multi-agent deliberation workflow for language-design decisions, choosing between pi-teams and Agent tool based on user/runtime constraints.
---

# VELA Deliberation

## When to use
When a VELA language design decision requires multi-perspective analysis. Any of these triggers:
- Grammar changes (case, word order, new particles)
- Phonology changes (new sounds, syllable rules)
- Vocabulary changes (new words, compound rules)
- Semantic/logic issues (ambiguity, collisions)

## ⚠️ CRITICAL: Ask User Before Choosing Architecture

**Before any deliberation, you MUST ask the user:**

> "This topic requires a multi-agent committee review. Should I use **pi-teams** (agents in terminal panes with full tools + mailbox communication) or **Agent tool** (background agents, more reliable but isolated)? Note: pi-teams requires you to be running in an interactive terminal (Warp, iTerm, tmux)."

**Use ask_terminal with mode: confirm for this question.**

### If user chooses YES (pi-teams):
- Check: Is the user in an interactive terminal? (tmux, Zellij, Warp, iTerm)
- If YES: Use `team_create`, `spawn_teammate`, `broadcast_message`, `read_inbox`
- If NO: Explain that pi-teams requires a terminal, fall back to Agent tool

### If user chooses NO (Agent tool):
- Use `Agent` tool with `run_in_background: true`
- Parent orchestrator does ALL file I/O
- Subagents read files via `read_file` (Serena) and return analysis as text
- See "Agent Tool Workflow" below

---

## Tool Availability (READ THIS)

**Native tools (read, write, edit, bash, grep, find, ls):**
- ✅ Available to parent (you)
- ❌ NOT available to subagents launched via Agent tool
- Subagents attempting to use native tools will fail silently or produce no output

**Serena MCP tools (read_file, search_for_pattern, get_symbols_overview):**
- ✅ Available to both parent and subagents
- Subagents CAN use `read_file` to read source documents
- Subagents CANNOT use `create_text_file`, `replace_content`, `replace_lines` (write-restricted)

**pi-teams tools (team_create, spawn_teammate, broadcast_message, read_inbox):**
- ✅ Available to parent in interactive terminal
- ❌ NOT available in MCP headless environment
- Error: "Extension ctx is stale after session replacement or reload"

**Full audit:** See `vote/docs/TOOLS_AUDIT.md`

---

## Architecture A: pi-teams (When User Chooses YES + Terminal Available)

### Setup (one-time)
```
team_create({ team_name: "vela", description: "VELA language construction committee" })
spawn_teammate({ team_name: "vela", name: "vela_phonologist", prompt: "...", cwd: "." })
# ... etc for all 5 specialists
```

### Deliberation Flow
1. **Phase 0 (Leader/you)**: Read graphify, write `vote/topics/current_topic.md`
2. **Phase 1**: Create task + broadcast to team
3. **Phase 2 (Teammates)**: Read files directly, post #proposal to mailbox
4. **Phase 3 (Leader)**: Read mailbox, synthesize discussion plan
5. **Phase 4 (Teammates, conditional)**: Deliberate on conflicts via mailbox
6. **Phase 5 (Teammates)**: Vote via mailbox
7. **Phase 6 (Leader)**: Tally votes, write consensus
8. **Phase 7**: Write summary, update CHANGE_LOG

---

## Architecture B: Agent Tool (When User Chooses NO or No Terminal)

### Deliberation Flow
1. **Phase 0 (You)**: Read graphify, write `vote/topics/current_topic.md`
2. **Phase 1 (You)**: Launch 5 specialists via `Agent` with `run_in_background: true`
3. **Phase 2 (Subagents)**: Read files via `read_file`, analyze, return text
4. **Phase 3 (You)**: Collect all responses, write `vote/topics/discussion_plan.md`
5. **Phase 4 (You + Subagents, conditional)**: If conflicts exist, re-launch for point-by-point discussion
6. **Phase 5 (You + Subagents)**: Re-launch for explicit voting
7. **Phase 6 (You)**: Write `vote/topics/consensus/consensus.md`
8. **Phase 7 (You)**: Write `vote/SUMMARY.md`, append `vote/docs/CHANGE_LOG.md`

### Critical Rules
- **You do ALL file writing.** Subagents cannot write files.
- **Embed file paths in prompts.** Tell subagents exactly which `read_file` calls to make.
- **Never tell subagents to use native tools.** No `read`, `write`, `edit`, `bash`, `grep`.
- **Collect with `get_subagent_result`.** Wait for all 5 before synthesizing.

---

## Agent Types
- `vela_phonologist` — Phonology, phonotactics
- `vela_morphologist` — Grammar, morphology
- `vela_lexicographer` — Vocabulary, etymology
- `vela_semanticist` — Logic, semantics
- `vela_aestheticist` — Beauty, cadence
- `vela_orchestrator` — Leader (you or a subagent you launch)

---

## Quality Checklist
Before declaring a deliberation complete:
- [ ] Asked user about pi-teams vs Agent tool
- [ ] `graphify-out/GRAPH_REPORT.md` was consulted
- [ ] `vote/SUMMARY.md` exists with ≥1 approved change
- [ ] Each change has: what, why, exact implementation, priority
- [ ] Consensus cites which specialists agreed/disagreed
- [ ] No critical tool errors in any agent
- [ ] CHANGE_LOG.md was appended
- [ ] All specialists responded (or failure documented)
