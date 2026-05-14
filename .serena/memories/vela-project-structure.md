## VELA Language Project Onboarding

**Project:** VELA — An international auxiliary language (IAL/bridge language)
**Tech Stack:** Markdown documentation, JSON lexicography files, graphify knowledge graph
**No programming language stack** — this is a linguistic design project

### Project Structure
```
vela-lang/
├── README.md — Main project overview and design philosophy
├── docs/ — Core documentation
│   ├── grammar/ — Case system, verb conjugation, syntax
│   ├── phonology/ — Sound inventory, phonotactics, pitch accent
│   ├── lexicon/ — Core vocabulary (1,000+ words)
│   ├── writing/ — Orthography
│   └── research/ — Deep linguistic research
├── vote/ — Multi-agent deliberation system
│   ├── docs/ — Procedure documentation
│   ├── templates/ — Deliberation templates
│   └── topics/ — Working directory for active deliberations
├── .pi/agents/ — Custom specialist agent definitions
└── graphify-out/ — Knowledge graph (auto-generated)
```

### No Testing/Build Commands
This is NOT a software project. No npm, no Makefile, no tests. Changes are verified by:
1. Reading the affected documents
2. Checking consistency across docs
3. Manual grammatical verification

### Key Commands for Agent System
To run a deliberation:
1. Write `vote/topics/current_topic.md`
2. Spawn specialist agents:
   ```
   Agent({ subagent_type: "vela_orchestrator", prompt: "Run deliberation", description: "VELA topic", run_in_background: true })
   ```
3. Collect results from `vote/SUMMARY.md`

### Naming Conventions
- Agent files: `.pi/agents/vela_{specialty}.md`
- Deliberation files: `vote/topics/proposals/{agent}.md`
- Consensus: `vote/topics/consensus/consensus.md`
- Summary: `vote/SUMMARY.md`

### Design Decision Framework
Every decision must pass three filters:
1. LÓGICO — Can the rule be explained in one sentence?
2. SIMPLE — One morpheme = one meaning. No exceptions.
3. BELLO — Sounds melodic, musical, pleasant.
