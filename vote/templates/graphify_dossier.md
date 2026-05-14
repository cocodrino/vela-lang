# Graphify Dossier Template

## Purpose
This template shows how to extract and format graphify insights for embedding in specialist dossiers.

## Step 1: Read the Graph Report

```
read_file({ relative_path: "graphify-out/GRAPH_REPORT.md" })
```

## Step 2: Find Your Topic's Community

Search for keywords related to your topic:
- Case system: "Case System", "Genitive", "Locative"
- Phonology: "Phonology", "Sound", "Vowel"
- Lexicon: "Vocabulary", "Lexicon", "Word"
- Grammar: "Grammar", "Morphology", "Syntax"

## Step 3: Extract Core Data

### Community Identification
```markdown
**Community**: [exact name from graph report]
**Nodes**: [number of concepts]
**Cohesion**: [score, 0.02–0.22]
```

### Cross-Community Connections
```markdown
**Connected to**:
- [Community name 1] — [how it connects, e.g., "via god node README"]
- [Community name 2] — [connection description]
```

### God Nodes
```markdown
**Central nodes**:
- [Node name] ([edge count] edges, betweenness [score])
  — [why this node matters to your topic]
```

### Inferred Edges
```markdown
**Inferred connections**: [number] inferred edges
- [Description of most surprising or relevant inferred connection]
```

## Step 4: Format for Dossier

Combine into a single block for embedding:

```markdown
### GRAPHIFY PROJECT KNOWLEDGE GRAPH

The VELA project has [N] concepts across [N] communities. Relevant to your analysis:

- **[Community Name]** community: [N] nodes, cohesion [score]
  - Connected to: [Community 1], [Community 2], [Community 3]
  - Central node: [God node] (betweenness [score])
  - [N] inferred edges linking this community to broader [domain]

- **[Related Community]** community: [N] nodes
  - Cross-link: [This domain] → [Your topic] via [hub node]
  - [Specific insight, e.g., "Sound Symbolism links vowel quality /e/ to semantic domains"]

**Surprising connection**: [Most unexpected or valuable inferred relationship]
```

## Example (From Case System Deliberation)

```markdown
### GRAPHIFY PROJECT KNOWLEDGE GRAPH

The VELA project has 1036 concepts across 25 communities. Relevant to your analysis:

- **Case System Design** community: 34 nodes, cohesion 0.06
  - Connected to: Grammar Complete Reference, VELA Core Design, Sound Symbolism
  - Central node: README (40 edges, betweenness 0.178)
  - 30 inferred edges linking case system to broader grammar

- **Sound Symbolism** community: 53 nodes
  - Cross-link: Sound Symbolism → Case System via VELA Core hub
  - Vowel quality /e/ mapped to "small/delicate" in sound-meaning system

- **Phonology Final Decisions** community: 53 nodes
  - Peers with Case System in hierarchy via VELA Core Design hub

**Surprising connection**: Sound symbolism and case system are structurally co-equal in the knowledge graph (both 53 nodes), suggesting phonoaesthetic considerations are as structurally important as grammatical ones.
```

## Step 5: Embed in Each Specialist's Dossier

Every specialist — regardless of domain — receives the same graphify block plus their domain-specific sources. This ensures they all understand the project-wide context.

## Staleness Check

Before each deliberation, verify graphify freshness:
1. Check `graphify-out/` timestamps vs. latest doc edits
2. If docs were edited after graphify generation, run `graphify update .`
3. If graphify is stale, note it in the dossier: "Graphify may be stale — recent edits to [file] not reflected"

## When Graphify Has Nothing Relevant

Sometimes your topic is too new or too specific for graphify to have detected a community:
1. Search for individual terms in `graphify-out/GRAPH_REPORT.md`
2. Look at the "Suggested Questions" section for connections
3. Extract from the nearest community
4. If truly no match exists, note: "No specific graphify community detected; analyzing from first principles"
