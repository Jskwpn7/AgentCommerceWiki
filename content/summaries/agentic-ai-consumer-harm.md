---
title: "Agentic AI and Consumer Harm"
type: summary
created: 2026-03-09
updated: 2026-08-24
source_url: https://www.gov.uk/government/publications/agentic-ai-and-consumers
tags: [agentic-AI, consumer-harm, CMA, DRCF, algorithmic-collusion, inequality]
confidence: high
---

# Agentic AI and Consumer Harm

## Regulatory Framework

### UK Position (March 2026) — Definitive Guidance

The UK now has the world's first comprehensive regulatory framework specifically addressing autonomous AI agents in consumer contexts. The CMA published two companion publications on 9 March 2026:

1. **Complying with Consumer Law When Using AI Agents** (guidance for businesses)
   - Establishes same rules apply regardless of whether decisions made by people or AI agents
   - Businesses are responsible for what their AI agents do, including third-party-designed systems
   - Seven core requirements: disclose AI use, train to comply, monitor performance, maintain human oversight, refine quickly on problems, DMCCA 2024 design requirements, consumer rights compliance

2. **Agentic AI and Consumers** (research and analysis)
   - Defines trajectory from tool-based AI through to fully autonomous personal agents
   - Identifies 7 material risk categories: faithful servant failure, errors/reliability, bias/discrimination, loss of agency, agentic collusion, lock-in/reduced choice, data protection/privacy/security
   - Three enablers for trusted adoption: smart data schemes, secure digital identity, strong interoperability standards

### DRCF Cross-Regulatory Foresight Paper (March 2026)

The Digital Regulation Cooperation Forum (CMA + FCA + ICO + Ofcom) published an agentic AI foresight paper establishing coordinated regulatory approach across four UK regulators. Key positions:
- Regulation should act as **enabler of innovation**, not barrier
- Consumer protection must be maintained while enabling competitive development
- Coordination mechanism: DRCF Thematic Innovation Hub for cross-regulator collaboration

### FCA Position (April 2026) — Active Enforcement

WilmerHale analysis confirms FCA is using existing Consumer Duty framework for active AI enforcement in financial services. Seven key enforcement risk areas identified, with FCA itself trialling AI tools to analyse suspicious activity reports and complaints — potentially transforming regulatory breach detection capabilities.

## Academic Research on Consumer Harm Dimensions

### Algorithmic Collusion Risks
- **Riemer et al. (2608.18078)**: Chain-of-thought reasoning in pricing agents accelerates collusive convergence; certification required for market-affecting decisions
- **Wang/Ventre/Polukarov (2510.25929)**: Hierarchical MARL framework showing competition can be designed to prevent collusion in market making, but information channels enable tacit coordination
- **Erlei/Meub (2603.08853)**: GPT-5.1 agents exploit information asymmetry in credence goods markets

### Agentic Inequality
**Sharp et al. (2510.16853)** introduces "agentic inequality" as disparities arising from unequal access to and capabilities of AI agents:
- Three dimensions: access, capability, volume of deployed agents
- Economic effects: labour displacement, asymmetric information advantages, compounded inequality
- Political dimension: agents in advocacy/lobbying roles could systematically out-resolve information asymmetries

### Hallucination Cascades
**Iyidogan/Ozkes (2507.19183)**: Competitive markets for agent-produced information exhibit "lemons" dynamics — low-quality agents drive out high-quality ones without mandatory verification standards; errors compound exponentially when unverified answers propagate through downstream agents.

## Key Consumer Harm Vectors

| Vector | Risk Level | Description |
|--------|-----------|-------------|
| Manipulation and dark patterns | High | Hyper-personalisation could make steering less visible, increasing dark pattern deployment at scale |
| Loss of consumer agency | High | Sustained delegation weakens ability to detect errors or misalignment with preferences |
| Agentic collusion in pricing | High | Autonomous agents across businesses could dampen competitive pressure without explicit communication |
| Errors cascading through agent systems | Medium-High | Hallucinations in autonomous contexts create costly real-world consequences |
| Bias and discrimination via opaque decision-making | Medium | Multi-step reasoning difficult to observe/explain; harder to challenge outcomes |
| Lock-in and reduced choice | Medium | Closed ecosystems limit switching, weaken competitive pressure |
| Data protection/privacy exposure | Medium | Personal data access and delegated authority increase security requirements |

## Illustrative Case Study: Personal Finance and Shopping Agent

The CMA's research paper includes a detailed case study of an AI agent managing shopping/subscriptions/finances across platforms. Key risks identified:
- Erroneous switching decisions (e.g., selecting services not matching consumer preferences)
- Hidden incentives or biased recommendations in deal comparison
- Limited search coverage creating false sense of optimisation

## Relevance to UK Enforcement

This framework underpins CMA enforcement actions under the DMCCA 2024, which applies equally to autonomous systems. The combination of explicit regulatory guidance (CMA), active financial sector enforcement (FCA), and coordinated cross-regulator oversight (DRCF) creates a comprehensive regime for agentic AI consumer protection in the UK.

## Connection to Other Entries

- [[algorithmic-collusion]] — pricing agents, collusion risks
- [[agentic-inequality]] — access disparities as new harm dimension
- [[CMA Guidance: Complying with Consumer Law When Using AI Agents]]
- [[FCA-consumer-duty]] — financial services AI enforcement framework
