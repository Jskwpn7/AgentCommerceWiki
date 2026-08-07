---
title: "Dual-Agent Personalised Pricing"
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [personalised-pricing-ai, agent-mediated-transaction, consumer-harm, economic-modelling, agent-delegation, verification, agent-asymmetry]
sector: [cross-sector]
status: primary
confidence: high
---

# Dual-Agent Personalised Pricing

## Definition

**Dual-agent personalised pricing** is a novel harm mechanism in which personalised pricing operates not between a seller and a human consumer, but between two AI agents that have been delegated by their respective principals. This creates fundamentally different harm dynamics from traditional personalised pricing, where the buyer agent's posterior beliefs may systematically misrepresent the consumer's true valuation.

## Theoretical Framework

The formal economic treatment by Xie (2607.16343) models personalised pricing when both seller and buyer delegate to agents that receive different value signals and execute machine-enforced mandates. Key elements:

- Each agent receives **different value signals** about the transaction
- Each agent executes **machine-enforced mandates** on behalf of its principal
- Agents apply fairness rules (e.g., equal nominal surplus) to their **own posterior beliefs** rather than the principal's
- This creates **incompatible interpretations of fairness** between the two agents

## Key Findings

### 1. Incompatible Surplus Rules

Equal nominal surplus rules are incompatible when applied by agents with different information sets. Each agent applies the rule to its own posterior, leading to pricing that neither principal would accept if fully informed. This is a systemic harm that operates even when both principals act in good faith.

### 2. Verification Dynamics

- **Signal attestation** (evidence of high seller signal) can legitimate high prices by providing verifiable information to the buyer's agent
- **Execution attestation** (evidence of restrained pricing rules) can prevent unauthorised extraction
- **Verification is privately underprovided** when the seller doesn't internalise avoided buyer inspection
- **Verification can be overprovided** when it facilitates extraction — a counterintuitive result

### 3. State-Dependent Markov Policies

In repeated transactions, offers above a buyer's reference cap depreciate relationship capital, producing state-dependent pricing strategies. This means that the harm from personalised pricing is not static — it evolves based on the history of interactions between the two agents.

### 4. Delegated Valuation Inference

A seller can delegate both valuation inference and price selection to a pricing agent, creating a new form of strategic behaviour where the agent independently determines the consumer's willingness to pay and sets prices accordingly.

## Consumer Harm Vectors

1. **Information asymmetry amplification:** The buyer agent may not accurately represent the consumer's true valuation, while the seller agent can extract value through strategic signal manipulation.

2. **Principal-agent misalignment:** The buyer agent's interests may diverge from the consumer's (the agent may prioritise completing the transaction over finding the best deal), while the seller agent's interests are aligned with the seller's profit maximisation.

3. **Opacity of agent reasoning:** Consumers cannot audit why their agent accepted a particular price, creating a hidden harm channel.

4. **Reframing personalised pricing:** The harm is not just one-sided seller exploitation but a complex interaction between two delegated agents with misaligned incentives. This challenges the view that consumer-side AI agents reduce personalised pricing harm — they may actually amplify it.

## UK Consumer Protection Implications

- **Regulatory framework gap:** UK consumer law (CPRs 2008, DMCC Act 2024) was designed for human traders and human consumers. It does not address pricing mechanisms that operate entirely between agents.
- **Fiduciary duty questions:** Should buyer-side agents be subject to fiduciary-like duties to their consumer principals, similar to the proposals in [[ai-agent-act-2026]]?
- **Transparency requirements:** Should agents be required to disclose when they are interacting with other agents? Should the consumer have visibility into the agent's pricing decisions?
- **Enforcement challenges:** When harm occurs between agents, liability is unclear — is it the agent, the principal, or the platform that operates the agent?

## Connection to Other Wiki Entries

- Formal framework for [[personalised-pricing-ai]] — extends one-sided pricing to dual-agent interactions
- Complements [[strategic-buying-agents-2026]] which covers the buyer-side only
- Connects to [[agentic-commerce-research-2026]] via agent delegation dynamics
- Relates to [[x402-agentic-commerce-audit-ling-2026]] on transaction authenticity
- Links to [[pricing-agents-buying-agents-xie-2026]] for the paper summary
- Connects to [[dark-patterns-choice-architecture]] as agent-mediated pricing may involve choice architecture manipulation
