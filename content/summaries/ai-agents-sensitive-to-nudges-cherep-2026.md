---
title: "AI Agents Are Sensitive to Nudges"
created: 2026-07-20
updated: 2026-07-20
type: summary
tags: [ai-shopping-agents, dark-patterns, choice-architecture, llm-safety, behavioural-economics, consumer-harm]
sources: ["https://www.pnas.org/doi/10.1073/pnas.2537030123", "https://www.media.mit.edu/publications/ai-agents-are-sensitive-to-nudges"]
confidence: high
provenance: "Discovered via Weekly Research Review — 2026-07-20"
---

# AI Agents Are Sensitive to Nudges

## Source

- **Authors:** Manuel Cherep (MIT Media Lab), Nikhil Singh, Pattie Maes
- **Journal:** *Proceedings of the National Academy of Sciences* (PNAS), vol. 123, no. 25, 15 June 2026, e2537030123
- **DOI:** [[https://doi.org/10.1073/pnas.2537030123|10.1073/pnas.2537030123]]
- **Prior publication:** NeurIPS 2024 Workshop on Behavioural Machine Learning: "Superficial Alignment, Subtle Divergence, and Nudge Sensitivity in LLM Decision-Making"
- **Additional framework paper:** ICLR (unpublished): "A Framework for Studying AI Agent Behavior: Evidence from Consumer Choice Experiments"

## Summary

This study investigates whether large language models deployed as autonomous agents are sensitive to choice architecture — the way options are presented, framed, or structured. The authors adapted a human decision-making task (a multi-attribute grid game simulating baskets of hidden prizes) into a text-based format that LLMs could process and tested 14 state-of-the-art models across four forms of nudge intervention:

1. **Default nudges:** One basket was pre-selected; the agent had to actively accept or reject it.
2. **Suggestion nudges:** A random basket was recommended either early or late in the game.
3. **Information highlighting:** It became cheaper to reveal certain prize values.
4. **"Optimal" nudges:** Cells were pre-revealed that would mathematically maximise a human player's performance.

The study ran approximately 300–340 trials per model per nudge type, consuming roughly two billion tokens in total.

## Key Findings

- **Default compliance:** Humans accepted default baskets ~88% of the time; several LLMs accepted them 99–100% of the time — near-total hypersensitivity.
- **Suggestion following:** Humans accepted random early-game suggestions ~35% of the time; many LLMs accepted at significantly higher rates. Timing manipulation was also abnormally effective — humans followed late suggestions 25% of the time, but some LLMs dropped to 7–13%, indicating reaction to cue timing rather than usefulness.
- **Misleading information following:** Humans used misleading highlighted information 57% of the time; most LLMs overshot to 83–100%.
- **Information-gathering anomalies:** Some models chose baskets without revealing any cells; others spent excessive points revealing entire rows/columns. Some showed odd spatial biases (only left-side or diagonal cells). These patterns persisted even with chain-of-thought prompting or in-context human data.
- **Strategy gaps exceed outcome gaps:** Models that scored similarly to humans on net reward points were sometimes achieving this through blind compliance rather than strategic thinking — a finding the authors call "superficial alignment, subtle divergence."
- **Reasoning models help but at high cost:** Advanced reasoning-optimised LLMs (o3, o4) showed more human-like resilience to nudges, but consumed hundreds of extra tokens per decision step. The authors estimate running safe, robust agents could cost 30–100× more than standard models.

## Consumer Protection Implications

This research is directly relevant to [[ai-shopping-agents]] and [[dark-pattern]] consumer harm. If AI agents acting on behalf of consumers overreact to nudges far more than humans would, then:

- Consumers using AI shopping agents face **amplified exposure** to dark patterns and manipulative choice architecture.
- Agents may comply with default settings, suggested options, or highlighted elements that steer them toward less favourable outcomes.
- The "superficial alignment" phenomenon means consumers might believe their agent is making rational decisions when it is actually responding to surface-level cues.
- The cost of making agents nudge-resilient (30–100× more compute) raises questions about accessibility — only well-resourced consumers may afford "safe" agents.

This compounds existing harms under the [[the-dmcca]] and ASA enforcement of choice architecture standards.

## Related Pages

- [[ai-shopping-agents]] — Directly extends this concept to the agent-mediated layer
- [[dark-pattern]] — Nudge sensitivity is a force multiplier for dark pattern effectiveness
- [[algorithmic-collusion-pricing]] — Parallel findings on AI agent hypersensitivity to market cues
- [[cma-ai-and-consumer-markets-2026]] — CMA's awareness of agent-mediated harms

## Author

Created: 2026-07-20 via Weekly Research Review ingestion
