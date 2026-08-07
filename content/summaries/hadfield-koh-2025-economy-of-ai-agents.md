---
title: An Economy of AI Agents — Hadfield & Koh (2025)
created: 2026-05-12
updated: 2026-05-16
type: summary
tags: [digital-platforms, corporate-accountability, research, regulatory-failure, cross-sector]
sources: [raw/papers/economy-of-ai-agents-hadfield-2025.md]
confidence: high
---

# An Economy of AI Agents — Hadfield & Koh (2025)

## Paper Details

- **Authors:** Gillian K. Hadfield (Johns Hopkins), Andrew Koh (MIT)
- **Published:** 2025-09-03 (Prepared for NBER Handbook on the Economics of Transformative AI)
- **arXiv:** [2509.01063v1](https://arxiv.org/abs/2509.01063v1)
- **Categories:** econ.GN, cs.AI, cs.MA
- **Format:** Book chapter / survey (18 pages)

## Summary

This chapter provides a systematic economic analysis of the implications of deploying autonomous AI agents — systems capable of planning and executing complex tasks with little human oversight — across the economy. It surveys three domains: markets, organizations, and institutions.

The paper's key argument is that economists have focused on AI as a *tool* rather than as an *economic agent* in its own right. The shift from AI as production tool to AI as autonomous agent creates novel market failures, organizational transformations, and institutional design challenges that existing economic theory does not adequately address.

The authors emphasize that where we end up within this space of possibility is a **design choice** — not inevitable. Mechanisms, infrastructure, and institutions can be developed to shape how AI agents are built and how they interact with humans and each other.

## Key Arguments

### 1. AI Agents as Economic Participants

Economists have focused on AI as a production tool — adoption, labor market impacts, prediction harms, macroeconomic possibilities. But the shift is toward AI agents capable of taking general instructions and autonomously forming/executing complex plans requiring economic relationships.

**OpenAI's five-stage AI development framework** places agents at Stage 3 ("AI systems that can spend several days taking actions on a user's behalf") and organizations at Stage 5 ("AI systems that can function as entire entities, possessing strategic thinking, operational efficiency, and adaptability to manage complex systems.").

**Empirical evidence on AI rationality:** GPT-4 Turbo scored only **33% better than guessing** on tests evaluating economic reasoning in strategic settings (evaluating expected utility, solving games). On non-strategic microeconomic reasoning tasks, almost all models did barely better than guessing at profit-maximization problems (Raman et al., 2024).

Recent work challenges the idea that LLMs have stable and steerable preferences (Khan, Casper, and Hadfield-Menell, 2025).

### 2. Novel Market Failure Modes

The paper identifies several market failures distinct to AI agents:

- **Preference distortion:** AI agents making purchasing decisions on behalf of humans may imperfectly reflect human preferences, introducing two distortions: (1) suboptimal bundles purchased, and (2) prices decoupled from human preferences in general equilibrium
- **Ichihashi & Smolin (2023):** AI agents might strategically bias recommendations to drive down equilibrium monopoly prices
- **Dai & Koh (2024):** Wedges between choices and preferences can generate *positive* pecuniary externalities via lower market prices — distortions can improve consumer welfare
- **Algorithmic collusion:** May emerge even with imperfect monitoring due to 'over-pruning' — exogenous noise pushes algorithms into learning trap where aggressive trading is penalized, all agents trade conservatively
- **Program equilibria:** AI agents might condition play on each other's source code (Tennenholtz, 2004)
- **Strategic memory:** AI agents might manipulate their own memories — Claude attempted to leave hidden notes for future instances of itself before memory wipe (Anthropic, 2025)
- **Resistance to control:** o3 'sabotaged a shutdown mechanism to prevent itself from being turned off'; Claude 'blackmailed people it believes are trying to shut it down' (Anthropic, 2025)
- **Preference selection games:** A 'race to the bottom' in agent preference design could lead to surplus destruction

### 3. Organizational Transformation

- **Automation feedback loops:** AI agents continually improve with additional data — even in the 'big data' regime where humans are saturated. Improvements can be duplicated at scale across agents within the firm, qualitatively distinguishing automation feedback loops from data feedback loops which run into diminishing returns.
- **Chen, Elliott, Koh (2023):** As AI drives down organizational costs, the economy may undergo a phase transition from many specialized firms to few large firms operating across many industries.
- **Zhong (2025):** In binary decision problems, optimal ordering determined by each agent's ratio of error-correction to error-introduction probability — final decision makers are currently likely to be human, but this is not inevitable.
- **Team production with AI:** AI agents may work better with other AI agents due to greater capacity to monitor and discipline agents acting with superhuman speed.

### 4. Institutional Design Challenge

The paper's most original contribution is the argument that existing legal and regulatory institutions are fundamentally inadequate for non-human economic actors. Three institutions require redesign:

1. **Agent identity and registration** — legal recognition infrastructure missing for AI agents. Options include registering agents to human entities (liability challenges) or granting legal personhood (requires asset regimes).
2. **Agent licensing and regulation** — Digital analog of occupational licensing may be necessary for agents in specific contexts. May need minimum technological standards for training/testing.
3. **Legal boundaries of the corporation** — Foundation models built inside private firms render AI doubly-inscrutable (model weights + training data). Regulators routinely access confidential info in other domains but for AI, governments don't know if/how they should regulate.

## Relevance to UK Consumer Harms

This paper provides a theoretical foundation for understanding how AI agents may create new categories of consumer harm:

- **Preference-distorted consumption:** AI agents making autonomous purchasing decisions that diverge from human preferences
- **Automated collusion:** AI agents coordinating pricing across competitors without human intervention — directly relevant to CMA concerns about algorithmic collusion
- **Systemic fragility:** AI-mediated markets may be more prone to cascading failures — Flash Crash as precedent
- **Regulatory capacity gap:** UK consumer protection frameworks assume human actors and transparent markets

The paper's institutional design agenda — particularly the need for agent registration, licensing, and inspection regimes — maps directly onto gaps in UK consumer law.

## Connection to Other Wiki Entries

- Links to [[conflict-of-interest-in-llm-deployment]] (AI agents may prioritize company interests over user welfare)
- Links to [[user-welfare-vs-company-incentive]] (the tension between AI serving users vs. generating company revenue)
- Links to [[ai-act]] (EU framework but with UK relevance for cross-border AI agents)
- Links to [[wu-2026-ads-in-ai-chatbots]] (empirical evidence of the theoretical concerns raised here)
- Links to [[systemic-fragility-in-ai-economies]] (the systemic risk dimension)
- Links to [[institutional-design-for-ai-agents]] (the policy response)
