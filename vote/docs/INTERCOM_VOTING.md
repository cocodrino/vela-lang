# Intercom Voting System — pi-intercom

**Status:** ✅ Primary voting method  
**Replaces:** pi-teams (unreliable in MCP/terminal environments)  
**Requires:** `pi-intercom` extension installed

---

## Architecture

```
┌──────────────────────────────────────────┐
│           COORDINATOR (your session)      │
│  • Sends dossier to all 5 specialists    │
│  • Collects individual analyses          │
│  • Synthesizes consensus document        │
│  • Writes results to vote/topics/        │
└──────┬──────┬──────┬──────┬──────┘
       │      │      │      │
       ▼      ▼      ▼      ▼      ▼
   ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐
   │P   │ │M   │ │L   │ │S   │ │A   │
   └────┘ └────┘ └────┘ └────┘ └────┘

Each specialist = FULL pi session
• All native tools (read, write, edit, grep, bash)
• Reads project files directly
• No EPIPE, no stalls, no "starting" freeze
• Asynchronous — analysis runs in parallel
```

## Why intercom beats pi-teams

| Issue | pi-teams | pi-intercom |
|-------|----------|-------------|
| **Subagent tool access** | `read`/`write` disabled | ✅ All native tools |
| **Spawning reliability** | Panes stall at `starting` | ✅ Full pi sessions |
| **Parallel execution** | EPIPE crash with 5+ spawns | ✅ True parallelism |
| **Model compatibility** | kimi crashes, glm works | ✅ All models work |
| **File I/O** | Must embed dossiers in prompt | ✅ Reads files directly |
| **Output format** | "No output" common | ✅ Full text responses |
| **Shutdown** | Must explicitly `team_shutdown` | ✅ Sessions close naturally |

## Quick Start

### 1. Launch the 5 specialists

```bash
bash .pi/scripts/vote-specialists.sh
```

This opens 5 Terminal windows, each running a pi session with:
- Correct model (deepseek for P/M/S/A, glm for L)
- Specialist system prompt
- Auto-registration on intercom room `vela-vote-<timestamp>`

### 2. Send the dossier

From your coordinator session, create a room and send:

```bash
# Create room and invite
intercom create_room vela-vote-coda public

# Send dossier to the room
intercom send --room vela-vote-coda --content "dossier contents..."
```

Or use the Pi agent tools:
```
agent_comms create_room vela-vote-coda public "Coda deliberation"
agent_comms send vela-vote-coda "Dossier: ..."
```

### 3. Collect responses

Each specialist replies via intercom. Read the room:

```bash
intercom read_room vela-vote-coda
```

Or with Pi tools:
```
agent_comms read_room vela-vote-coda
```

### 4. Synthesize consensus

The coordinator (your Pi agent) collects all 5 analyses and:
1. Creates a consensus table with per-specialist votes
2. Identifies unanimous, strong consensus, and conflicted items
3. Writes `vote/topics/consensus/<TOPIC>_consensus.md`
4. Applies approved changes

## Specialist Models

| Specialist | Model | Session Name |
|-----------|-------|--------------|
| Phonologist | `kimi-k2.6:cloud` | `vela-phon` |
| Morphologist | `deepseek-v4-pro` | `vela-morph` |
| Lexicographer | `glm-5.1:cloud` | `vela-lex` |
| Semanticist | `deepseek-v4-pro` | `vela-sem` |
| Aestheticist | `kimi-k2.6:cloud` | `vela-aest` |

## Dossier Format

Dossiers should be markdown files in `vote/topics/`. The coordinator reads the file and sends it as a message body to all specialists.

Template: `vote/templates/graphify_dossier.md`

## Voting Workflow

```
1. [User] Identifies topic for deliberation
2. [Coordinator] Creates dossier in vote/topics/dossier_<topic>.md
3. [Coordinator] Launches specialists via script or intercom
4. [Coordinator] Sends dossier to all 5 via intercom room
5. [Specialists] Read dossier, analyze from their perspective, reply with table
6. [Coordinator] Collects all 5 replies
7. [Coordinator] Synthesizes consensus → vote/topics/consensus/<TOPIC>_consensus.md
8. [Coordinator] Presents results to user for tie-breaking
9. [User] Resolves conflicts
10. [Coordinator] Applies changes to relevant project files
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Specialists don't respond | Check `intercom list` — sessions may need restart |
| Model not found | Verify `pi --models` lists the expected models |
| Intercom not connected | Run `pi` and check `intercom status` |
| Room not receiving messages | Verify all 5 joined the same room |
| EPIPE crash | Doesn't happen! Each session is independent |
