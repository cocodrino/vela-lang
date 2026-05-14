# Example Deliberation Run

## Topic
VELA Case System Re-evaluation (see `vote/topics/current_topic.md`)

## How It Was Launched
```
Agent({
  subagent_type: "vela_orchestrator",
  prompt: "Execute the full deliberation pipeline for the current topic.",
  description: "Case system deliberation",
  run_in_background: true
})
```

## Expected Timeline
1. Phase 1 (Proposals): ~5 minutes (5 parallel agents)
2. Phase 2 (Discussion Plan): ~1 minute (orchestrator synthesis)
3. Phase 3 (Deliberation): ~15 minutes (5 points × 5 agents)
4. Phase 4 (Voting): ~5 minutes
5. Phase 5 (Consensus): ~2 minutes
6. Phase 6 (Summary): ~1 minute

**Total: ~30 minutes for a full run.**

## Expected Outputs
- `vote/topics/proposals/phonologist.md` → 3 problems with alternatives
- `vote/topics/proposals/morphologist.md` → grammatical issues
- `vote/topics/proposals/lexicographer.md` → vocabulary/loan impacts
- `vote/topics/proposals/semanticist.md` → logical ambiguities
- `vote/topics/proposals/aestheticist.md` → beauty concerns
- `vote/topics/discussion_plan.md` → consolidated points
- `vote/topics/discussion/point_01_*.md` → agent arguments per point
- `vote/topics/votes/point_01_*.md` → explicit votes
- `vote/topics/consensus/consensus.md` → decisions with implementation
- `vote/SUMMARY.md` → final table of changes

## Example Output Snippet (projected)
| Change | Reason | Implementation | Priority |
|--------|--------|---------------|----------|
| Swap plural-case order | Reduces parsing ambiguity | `man-se-s` instead of `man-s-se` | High |
| Make `-te` optional always | Prepositions cover locative meaning | Update docs to show both forms as valid | Medium |
