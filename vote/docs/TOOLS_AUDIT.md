# VELA Tools Audit — What Works, What Doesn't

**Date:** 2026-05-15
**Context:** Multi-agent deliberation system for VELA language construction
**Purpose:** Document which tools are available to agents and how to use them correctly

---

## Tool Availability Matrix

| Tool | Parent (You) | Subagent (Agent tool) | Teammate (pi-teams) | Notes |
|------|-------------|----------------------|---------------------|-------|
| `read` (native) | ✅ | ❌ | N/A | Native tools disabled for subagents |
| `write` (native) | ✅ | ❌ | N/A | |
| `edit` (native) | ✅ | ❌ | N/A | |
| `bash` (native) | ✅ | ❌ | N/A | |
| `grep` (native) | ✅ | ❌ | N/A | |
| `find` (native) | ✅ | ❌ | N/A | |
| `ls` (native) | ✅ | ❌ | N/A | |
| `read_file` (Serena) | ✅ | ✅ | ✅ | Primary file reading tool |
| `create_text_file` (Serena) | ✅ | ✅? | ✅ | File writing via Serena |
| `replace_content` (Serena) | ✅ | ✅? | ✅ | |
| `replace_lines` (Serena) | ✅ | ✅? | ✅ | |
| `search_for_pattern` (Serena) | ✅ | ✅? | ✅ | |
| `get_subagent_result` | ✅ | ❌ | N/A | Only parent can check subagents |
| `Agent` (spawn) | ✅ | ❌ | N/A | Only parent spawns subagents |
| `team_create` | ✅ | ❌ | N/A | Requires interactive terminal |
| `spawn_teammate` | ✅ | ❌ | N/A | Requires tmux/Zellij/Warp |
| `broadcast_message` | ✅ | ❌ | N/A | Requires active team |
| `read_inbox` | ✅ | ❌ | N/A | |
| `send_message` | ✅ | ❌ | N/A | |
| `task_create` | ✅ | ❌ | N/A | |

---

## Native Tools (read, write, edit, bash)

**Status: PARENT ONLY**

Subagents launched via `Agent` tool with `run_in_background: true` **CANNOT** use native tools (`read`, `write`, `edit`, `bash`, `grep`, `find`, `ls`). These are disabled by the MCP environment.

**What happens when a subagent tries:**
- Tool call fails with "Tool is disabled" or similar error
- Agent wastes turns retrying
- Eventually produces no output or incomplete output

**Workaround for file reading:**
- Use `read_file` (Serena MCP) — this IS available to subagents
- Verified: the phonologist used 22 `read_file` calls successfully

**Workaround for file writing:**
- Subagents CANNOT write files directly (both native `write` and Serena `create_text_file` fail in practice)
- Parent orchestrator must write all files
- Subagents return analysis as text in final response; parent captures and writes to disk

---

## Serena MCP Tools (read_file, create_text_file, etc.)

**Status: AVAILABLE TO BOTH PARENT AND SUBAGENTS**

The Serena MCP server (`http://127.0.0.1:7437`) provides file tools that work in the MCP environment.

**Verified working:**
- `read_file` — all 5 subagents used this successfully to read LEXICON_BASE.md, GRAMMAR_COMPLETE.md, etc.

**Verified NOT working in subagents:**
- `create_text_file` — subagent attempts return "Tool is disabled"
- `replace_content` — same issue
- `replace_lines` — same issue

**Why the discrepancy:**
The MCP environment restricts file-mutating tools for safety. Read-only tools (`read_file`, `search_for_pattern`, `get_symbols_overview`) are allowed. Write tools require explicit approval that subagents don't have.

---

## pi-teams Extension

**Status: INCOMPATIBLE WITH MCP ENVIRONMENT**

pi-teams (`npm:pi-teams` or `@vadimcomanescu/pi-teams`) requires:
1. Interactive terminal (tmux, Zellij, iTerm2, WezTerm, or Windows Terminal)
2. Real TTY for spawning teammate panes/windows
3. Active extension context that persists across turns

**What happens in MCP:**
```
Error: This extension ctx is stale after session replacement or reload.
    at ExtensionRunner.assertActive (runner.js:297)
```

**Root cause:**
pi-teams polls for idle status using `setTimeout` callbacks. When the MCP session resets between turns, the captured context becomes stale. This is a fundamental architectural mismatch — pi-teams is designed for interactive REPL sessions, not stateless RPC calls.

**When it DOES work:**
- Inside Warp, iTerm2, or any terminal with tmux/Zellij installed
- When the user runs pi directly (not via agent tool)
- Full team lifecycle: create → spawn → broadcast → read_inbox → shutdown

---

## Agent Tool (run_in_background)

**Status: WORKS, WITH LIMITATIONS**

The `Agent` tool launches background subagents that:
- ✅ Can read files via `read_file` (Serena)
- ✅ Can analyze and return structured text
- ✅ Run in parallel (up to 4 concurrent)
- ✅ Can be monitored via `get_subagent_result`
- ❌ Cannot write files
- ❌ Cannot edit files
- ❌ Cannot run bash commands
- ❌ Cannot use native tools (read, write, grep, etc.)
- ❌ Cannot communicate with other subagents

**Practical workflow:**
1. Parent writes topic file and dossier
2. Parent launches 5 subagents with prompts containing file paths to read
3. Subagents read files directly, analyze, return text
4. Parent collects responses via `get_subagent_result`
5. Parent writes all proposal/consensus/summary files

**This is the ONLY viable architecture for VELA deliberations in the MCP environment.**

---

## Recommended Architecture Decision Tree

```
When a deliberation is suggested:
│
├─ Ask user: "Use pi-teams? (requires terminal)" [yes/no]
│
├─ If YES:
│   └─ Check: Is user in interactive terminal (Warp/iTerm/tmux)?
│      ├─ YES → Use pi-teams: team_create → spawn_teammates → broadcast → read_inbox
│      └─ NO  → Explain: pi-teams requires tmux/Zellij/Warp. Fallback to Agent tool.
│
└─ If NO:
   └─ Use Agent tool with run_in_background:
      1. Parent writes topic file
      2. Parent launches 5 specialists in parallel
      3. Parent collects text responses
      4. Parent writes all output files
      5. Parent synthesizes consensus
```

---

## Key Files for Documentation

| File | Purpose |
|------|---------|
| `.pi/skills/vela-deliberation/SKILL.md` | Skill definition — which architecture to use |
| `vote/docs/PROCESS.md` | Full deliberation process documentation |
| `vote/docs/VOTING_PROCESS.md` | Voting mechanics and flow |
| `vote/docs/TOOLS_AUDIT.md` | This file — tool availability reference |

---

## Lessons Learned

1. **Native tools are parent-only.** Never instruct subagents to use `read`, `write`, `edit`, `bash`, `grep`, `find`, `ls`.

2. **Serena read_file works for subagents.** Use this for file access in prompts: "Use read_file to access the source documents."

3. **Serena write tools fail for subagents.** Parent must do ALL file writing. Build the dossier pattern into the orchestrator's role.

4. **pi-teams requires interactive terminal.** It cannot work in the MCP agent environment. Only use it when the user is running pi directly in Warp/iTerm.

5. **Agent tool is the reliable fallback.** It works in all environments but requires the parent to be the file I/O hub.

6. **Always ask the user first.** Before choosing an architecture, ask whether they want pi-teams (powerful but needs terminal) or Agent tool (reliable but limited).
