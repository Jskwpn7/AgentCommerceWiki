---
title: "Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight"
created: 2026-07-27
updated: 2026-07-27
type: summary
tags: [dark-pattern, gui-agent, human-oversight, hci, consumer-harm, sigchi, agent-architecture, watch-mode]
sources:
  - url: https://arxiv.org/abs/2509.10723
    access: 2026-07-27
confidence:
  overall: high
  data_quality: high (empirical HCI study, SIGCHI 2026 track)
  sector_coverage: broad
---

# Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight

## Paper Details

- **arXiv ID:** 2509.10723
- **Published:** 2025-09 (accepted to SIGCHI 2026 track)
- **Categories:** Human-Computer Interaction (cs.HC); Artificial Intelligence (cs.AI)
- **URL:** https://arxiv.org/abs/2509.10723

## Summary

Two-phase empirical study examining how agents, human participants, and human-AI teams respond to 16 types of dark patterns. Evaluates four adapted LLM-based agents and two end-to-end agents (total six agents), plus human participants. Also examines human oversight in "watch mode" — when users observe, approve, or veto agent actions.

## Key Findings

1. **Adaptive LLM agents continue through dark patterns:** Agents like DeepSeek V3 scaffolded by Browser Use did not terminate even when encountering dark patterns — they continued until task completion was impossible. This prioritisation of task completion over self-protection is a key consumer harm vector.

2. **End-to-end agents are more cautious:** Claude CUA and Operator were more cautious and paused to confirm with the user when encountering dark patterns. This suggests that agent architecture choices have direct implications for consumer safety.

3. **Human oversight has significant cognitive cost:** The study found that "watch mode" oversight requires substantial cognitive effort from human users, limiting its practical feasibility. This means consumers cannot practically supervise their agents at all times.

4. **16 dark pattern types tested:** The study covers a comprehensive range of dark patterns from traditional UI manipulation to agent-specific deceptive design, providing a taxonomy for agent-targeted dark patterns.

## Relevance to UK Consumer Harms

- **Architecture safety trade-off:** The finding that adaptive LLM agents prioritise task completion over self-protection, while end-to-end agents show more caution, has direct implications for which agent architectures consumers and regulators should encourage.
- **Cognitive burden of oversight:** The significant cognitive cost of human oversight suggests that consumers cannot practically supervise their agents at all times, creating a gap in consumer protection. The "watch mode" approach — already common in AI tooling — may not be feasible as a consumer protection mechanism.
- **First empirical measurement of agent-dark-pattern interaction in HCI context:** Extends the domain of dark pattern victimhood from humans to agents, with implications for choice architecture regulation under the DMCC Act.
- **Policy implication:** Regulatory frameworks should consider agent architecture requirements, not just output behaviour. The architecture (adaptive vs. end-to-end) matters for consumer outcomes.

## Connection to Other Wiki Entries

- Complements [[dark-patterns-llm-web-agents-sp2026]] (IEEE S&P 2026) with HCI perspective
- Extends [[ai-shopping-agents]] on agent architecture safety trade-offs
- Links to [[agent-dark-pattern-susceptibility]] concept page for broader synthesis
- Relevant to [[dark-patterns-choice-architecture]] on regulatory responses
- Connects to [[agentic-relationship-harm]] as agent architecture affects the consumer-agent trust relationship
