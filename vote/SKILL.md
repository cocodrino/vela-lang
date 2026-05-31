# VELA Deliberation System

## What This Is
A fully automated, multi-model deliberation pipeline for VELA language design decisions.

Five specialist agents — each running a **different Ollama Cloud model** — analyze, debate, vote, and consensus-build on any language feature.

## Models in Use
| Agent | Model | Role |
|-------|-------|------|
| Phonologist | ollama/kimi-k2.6:cloud | Sound & phonotactics |
| Morphologist | ollama/deepseek-v4-pro | Grammar & cases |
| Lexicographer | ollama/glm-5.1:cloud | Vocabulary & roots |
| Semanticist | ollama/deepseek-v4-pro | Logic & meaning |
| Aestheticist | ollama/kimi-k2.6:cloud | Beauty & cadence |
| Orchestrator | ollama/deepseek-v4-pro | Coordination |

## Voting Methods (preferred order)

### 1) pi-intercom (PRIMARY)
Run 5 **full pi sessions** (one per specialist) and coordinate via intercom messaging.
- Reliable in MCP + terminal environments
- Specialists can read project files directly
- True parallelism, no EPIPE

See: `vote/docs/INTERCOM_VOTING.md`
Launch helper: `.pi/scripts/vote-specialists.sh`

### 2) Agent tool (FALLBACK)
Use `Agent` subagents sequentially with embedded dossiers.
- Dossier MUST be inline (subagents cannot read files)
- Avoid kimi model as subagent (often yields no output)

### 3) pi-teams (DEPRECATED)
Terminal-pane spawning can stall; use only if proven stable.

## Quick Start
1. Write topic: `vote/topics/current_topic.md`
2. Launch specialists via intercom: `bash .pi/scripts/vote-specialists.sh` (or manual sessions)
3. Send dossier + collect responses (see `vote/docs/INTERCOM_VOTING.md`)
4. Write consensus to `vote/topics/consensus/`

## Files
- `vote/docs/PROCESS.md` — How to run deliberations
- `vote/docs/CHANGELOG.md` — History of approved changes
- `vote/templates/` — Templates for topics, plans, and consensus
- `vote/topics/` — Working directory for active deliberations
- `vote/SUMMARY.md` — Final deliverable of the latest run

## Skill
Also registered as a pi skill at `.pi/skills/vela-deliberation/` for autoloading.
