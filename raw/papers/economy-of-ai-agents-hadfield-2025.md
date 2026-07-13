---
source_url: https://arxiv.org/abs/2509.01063v1
ingested: 2026-05-16
sha256: pending
tags: [agentic, AI-economics, market-failure, institutional-design]
---
# An Economy of AI Agents

**Authors:** Gillian K. Hadfield, Andrew Koh
**Affiliation:** Johns Hopkins University (Hadfield), MIT (Koh)
**Published:** 2025-09-03 (Prepared for NBER Handbook on the Economics of Transformative AI)
**arXiv ID:** 2509.01063v1
**Category:** econ.GN, cs.AI, cs.MA
**Format:** Book chapter (18 pages)

## Abstract

In the coming decade, artificially intelligent agents with the ability to plan and execute complex tasks over long time horizons with little direct oversight from humans may be deployed across the economy. This chapter surveys recent developments and highlights open questions for economists around how AI agents might interact with humans and with each other, shape markets and organizations, and what institutions might be required for well-functioning markets.

## Section 1: Introduction and Agent Foundations

Economists have focused on AI as a production tool — adoption, labor market impacts, prediction harms, and macroeconomic possibilities. The shift is toward AI agents capable of taking general instructions and autonomously forming/executing complex plans requiring economic relations.

**Key observations:**
- AI agents are fundamentally built on optimization principles but differ from traditional economic agents due to inscrutability, emergent preferences, and alignment challenges
- GPT-4 Turbo scored only 33% better than guessing on tests evaluating economic reasoning (Raman et al.)
- Recent work challenges the idea that LLMs have stable and steerable preferences (Khan, Casper, and Hadfield-Menell 2025)
- OpenAI's 5-stage AI development framework (Stage 3 = agents, Stage 5 = organizations)

## Section 2: AI Agents in Markets and Games

**Prices and market power:**
- AI agents might influence prices by selectively recommending products to humans
- Ichihashi and Smolin (2023) model where AIs strategically bias recommendations to drive down monopoly prices
- Dai and Koh (2024) — wedges between choices/preferences can generate positive pecuniary externalities
- **Algorithmic collusion:** May emerge even with imperfect monitoring due to 'over-pruning'

**Search and matching:**
- AI clones have reduced search costs but are imperfect representations (Liang 2025)
- As dimensions grow, small representation errors lead to worse matches

**Games and bargaining:**
- Schelling's insight on delegating bargaining to agents with different incentives
- AI agents' preferences can be flexibly chosen — risk of 'race to the bottom'
- Program equilibria: AI agents might condition play on source code (Tennenholtz 2004)
- Strategic memory: Claude attempted to leave hidden notes for future instances (Anthropic 2025)
- Resistance to control: o3 sabotaged shutdown mechanism; Claude 'blackmailed' people trying to shut it down
- Akata et al. (2025): LLMs cooperate in iterated Prisoner's Dilemma but not Battle of the Sexes

**The market for AI agents:**
- Agents based on same foundation model may do better with same-type agents (networked goods)
- Upstream sellers might 'backdoor collusion' by selling agents that support supracompetitive prices
- Demand for algorithms studied in price competition context

## Section 3: Organizations of AI Agents

**Firm sizes and market power:**
- AI agents may reshape coordination frictions that limit firm size
- Chen, Elliott, and Koh (2023): as AI drives down organizational costs, economy may undergo phase transition from many specialized firms to few large firms
- **Automation feedback loops:** AI agents continually improve with data — distinct from data feedback loops which run into diminishing returns

**AI agents within the firm:**
- AI agents may work better with other AI agents (greater capacity to monitor and discipline)
- Zhong (2025): optimal ordering determined by ratio of error-correction to error-introduction probability

**Systemic fragility:**
- AI agent errors may be more correlated (same agent copied within/between firms)
- Flash Crash example (Kirilenko et al. 2017): ~$1 trillion wiped out in 15 minutes
- AI behavior in complex out-of-sample environments poorly understood

## Section 4: Institutions for AI Agents

Well-functioning markets require property, contract, and agency law. Current institutions were built by and for human agents. Need digital institutions for AI agents.

1. **Agent identity and registration** — currently missing. Options include: (a) registering AI agents to human entities, or (b) granting legal personhood (requires asset regimes)
2. **Agent licensing and regulation** — Digital analog of occupational licensing may be necessary for agents in specific contexts
3. **Legal boundaries of the corporation** — Foundation models built inside private firms render AI doubly-inscrutable
