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
| Semanticist | ollama/qwen2.5-coder | Logic & meaning |
| Aestheticist | ollama/kimi-k2.6:cloud | Beauty & cadence |
| Orchestrator | ollama/deepseek-v4-pro | Coordination |

## Quick Start
1. Write a topic in `vote/topics/current_topic.md`
2. Run the orchestrator (see `vote/docs/PROCESS.md`)
3. Read the final summary in `vote/SUMMARY.md`

## Files
- `vote/docs/PROCESS.md` — How to run deliberations
- `vote/docs/CHANGELOG.md` — History of approved changes
- `vote/templates/` — Templates for topics, plans, and consensus
- `vote/topics/` — Working directory for active deliberations
- `vote/SUMMARY.md` — Final deliverable of the latest run

## Skill
Also registered as a pi skill at `.pi/skills/vela-deliberation/` for autoloading.
