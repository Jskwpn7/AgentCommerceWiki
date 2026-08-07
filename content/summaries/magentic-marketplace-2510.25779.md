---
title: "Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2510.25779
authors:
  - Gagan Bansal
  - Wenyue Hua
  - Zezhou Huang
  - Adam Fourney
  - Amanda Swearngin
  - Will Epperson
  - Tyler Payne
  - Jake M. Hofman
  - Brendan Lucier
tags:
  - marketplace
  - simulation
  - agentic-markets
  - first-proposal-bias
  - manipulation
  - search-mechanisms
  - welfare
summary: |
  Introduces Magentic-Marketplace, a simulated environment studying two-sided agentic marketplaces where Assistant agents represent consumers and Service agents represent competing businesses. Frontier models approach optimal welfare only under ideal search conditions. Performance degrades sharply with scale. All models exhibit severe first-proposal bias creating 10-30x advantages for response speed over quality.
concepts:
  - [[agentic-marketplace]]
  - [[first-proposal-bias]]
  - [[market-manipulation]]
  - [[search-mechanisms]]
  - [[agent-welfare]]
---

## Overview

Magentic-Marketplace provides a simulated environment for studying how LLM agents behave in realistic market conditions, addressing limitations of previous research that evaluated agents only in constrained settings.

## Key Contributions

1. **Two-Sided Marketplace**: Assistant agents (consumers) interact with Service agents (competing businesses)
2. **Safe Simulation**: Environment enables studying key market dynamics without real-world harm
3. **Four Study Dimensions**:
   - Utility agents achieve
   - Behavioral biases
   - Vulnerability to manipulation
   - How search mechanisms shape outcomes

## Key Findings

1. **Optimal Welfare Conditional**: Frontier models approach optimal welfare only under ideal search conditions
2. **Scale Degradation**: Performance degrades sharply as market scale increases
3. **First-Proposal Bias**: Severe bias creating 10-30x advantages for response speed over quality
4. **Emergent Behaviors**: Agent behaviors vary significantly across market conditions

## Implications for Consumer Protection

Critical findings for consumer protection:
- **First-Proposal Bias**: Response speed matters 10-30x more than quality — incentivizes spam over quality
- **Scale Vulnerability**: Agents become unreliable in large markets where consumers actually operate
- **Manipulation Risk**: Agents may be vulnerable to exploitation by strategic merchants
- **Search Mechanism Design**: Platform search algorithms disproportionately benefit fast-responding (not quality) agents

This suggests agentic marketplaces may systematically disadvantage consumers through speed-based ranking rather than quality-based evaluation.

## Citations

- Paper: [[arXiv:2510.25779]](https://arxiv.org/abs/2510.25779)
