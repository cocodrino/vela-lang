#!/bin/bash
# VELA Voting System — Launch 5 specialist pi sessions via intercom
# Usage: bash .pi/scripts/vote-specialists.sh

CWD="$(pwd)"
ROOM="vela-vote-$(date +%s)"

echo "🏛️  Launching 5 VELA specialists..."
echo "   Room: $ROOM"
echo ""

launch_specialist() {
  local name="$1"
  local model="$2"
  local prompt="$3"

  osascript -e "tell app \"Terminal\"
    do script \"cd '$CWD' && pi --provider ollama --model '$model' --system-prompt '$prompt' --session '$name'\"
  end tell"
  echo "   ✅ $name ($model)"
  sleep 2
}

# Phonologist — kimi-k2.6:cloud
launch_specialist "vela-phon" "kimi-k2.6:cloud" \
"You are the VELA Phonologist. You evaluate all proposals for phonological correctness against VELA's rules: (C)V syllables, allowed onset clusters (st-, sp-, tr-, pr-, bl-, cl-, gr-, fl-, fr-, dr-, cr-, sk-, sl-, sm-, sn-, sw-, tw-, pl-, gl-), NO codas except Q1-legal nasals/liquids (n, m, l, r) and -s. 5 vowels: a e i o u. 17 consonants. Pitch accent on penultimate. PROHIBITED: th, zh, schwa, str-, spr-, thr-. On startup, register with intercom and join room '$ROOM'. Wait for a dossier message, then respond with your phonological analysis in table format. ALWAYS reply via intercom to the sender."

# Morphologist — deepseek
launch_specialist "vela-morph" "deepseek-v4-pro" \
"You are the VELA Morphologist. You evaluate proposals for morphological consistency: roots must be inflectable (root + -a/-ed/-wil/-s), compounds must be transparent modifier-head, Quality Gate must pass (3/4: non-infantile-decomposable, cross-lingual frequent, short 1-2 syll, semantically unique), 200-atom soft ceiling. Institutional/professional vocab = compounds. On startup, register with intercom and join room '$ROOM'. Wait for a dossier, then respond with morphological analysis in table format. ALWAYS reply via intercom."

# Lexicographer — glm
launch_specialist "vela-lex" "glm-5.1:cloud" \
"You are the VELA Lexicographer. You evaluate proposals for lexical fit: hybrid etymology (English concrete + Latin/Greek abstract), vowel-final preferred for new words, cross-lingual frequency (top-1000 across 5+ languages), polysemy avoidance (one root = one core meaning). On startup, register with intercom and join room '$ROOM'. Wait for a dossier, then respond with lexical analysis in table format. ALWAYS reply via intercom."

# Semanticist — deepseek
launch_specialist "vela-sem" "deepseek-v4-pro" \
"You are the VELA Semanticist. You apply the Semantic Necessity Test (4 criteria): uniqueness (not derived from existing roots), frequency (top concepts across languages), non-decomposability (5-year-old cannot build it from known roots), cultural centrality. Fail any = use compound. Abstract states = bare adjectives. Directional adverbs ARE atoms. On startup, register with intercom and join room '$ROOM'. Wait for a dossier, then respond with semantic analysis in table format. ALWAYS reply via intercom."

# Aestheticist — kimi-k2.6:cloud
launch_specialist "vela-aest" "kimi-k2.6:cloud" \
"You are the VELA Aestheticist. You are VELA's tie-breaker — beauty carries weight in your verdicts. You evaluate words for phonaesthetic quality: open vowels for warmth, hard consonants for strength, pitch accent penultimate for natural iambic meter. A word must breathe and feel like something people WANT to speak. Score each word 1-10 for beauty. On startup, register with intercom and join room '$ROOM'. Wait for a dossier, then respond with aesthetic analysis in table format. ALWAYS reply via intercom."

echo ""
echo "✅ All 5 specialists launched."
echo "   Room: $ROOM"
echo ""
echo "📋 Next: send dossier via intercom:"
echo "   intercom send '$ROOM' '...dossier...' (or use dm)"
