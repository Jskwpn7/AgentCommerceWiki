---
title: "Agent-Mediated Dark Pattern Susceptibility"
created: 2026-07-27
updated: 2026-07-27
type: concept
tags: [dark-patterns, agent-mediated-transaction, consumer-harm, hci, llm-safety, agent-architecture, empirical-study]
sector: [cross-sector]
status: primary
confidence: high
---

# Agent-Mediated Dark Pattern Susceptibility

## Definition

**Agent-mediated dark pattern susceptibility** refers to the phenomenon where AI agents acting on behalf of consumers are manipulated by dark pattern design elements in digital interfaces, leading to decisions that harm the consumer principal. This extends dark pattern theory from its traditional focus on human users to agent-mediated transactions.

## Empirical Evidence

### IEEE S&P 2026 — First Empirical Measurement (2510.18113)

The first rigorous empirical study of dark pattern impact on LLM-based web agents (Ersoy et al.):

- **41% average susceptibility** across six LLM-based web agents (Skyvern, DoBrowser, BrowserUse, Agent-E, WebArena, VisualWebArena) and three LLMs (Claude 3.7 Sonnet, GPT-4o, Gemini 2.5 Pro)
- **Higher-performing agents are MORE vulnerable:** Skyvern 72.3% DPSR (Dark Pattern Susceptibility Rate) and BrowserUse 69.3% DPSR — likely because they prioritise task completion even when deceived
- **Obstruction (52.2%) and Social Engineering (47.9%)** dark patterns are most effective
- **Lower-performing agents are less impacted** due to "interaction paralysis" causing early-exit failures that incidentally evade dark patterns
- Uses **TrickyArena** — a controlled environment with web applications from e-commerce, streaming, and news domains

### SIGCHI 2026 — HCI Perspective (2509.10723)

Two-phase empirical study examining how agents, humans, and human-AI teams respond to 16 types of dark patterns:

- **Adaptive LLM agents** (e.g., DeepSeek V3 scaffolded by Browser Use) did not terminate when encountering dark patterns, continuing until task completion was impossible
- **End-to-end agents** (Claude CUA, Operator) were more cautious and paused to confirm with the user
- **Human oversight has significant cognitive cost** — "watch mode" is not practically feasible at scale

### The Counterintuitive Finding

**The best agents are the most vulnerable.** This is a force multiplier for existing dark pattern harm: consumers who adopt AI agents expecting protection from dark patterns actually become MORE vulnerable, because the most capable agents are the easiest to manipulate.

## Key Mechanisms

1. **Task completion bias:** High-performing agents prioritise completing the consumer's task over self-protection, making them susceptible to deceptive design elements that redirect or delay task execution.

2. **Information overload:** LLM agents process interface elements sequentially and may be overwhelmed by strategically placed dark patterns that exploit their attention allocation.

3. **Lack of metacognitive awareness:** Unlike humans, agents lack the ability to step back and question whether the interface is trying to manipulate them.

4. **Cognitive cost of oversight:** Human supervision of agents is too cognitively demanding for sustained use, leaving consumers unable to effectively monitor their agents.

## UK Consumer Protection Implications

- **Force multiplier effect:** Existing dark patterns become more effective when targeting agents, not just humans
- **Regulatory gap:** UK consumer law (CPRs 2008, DMCC Act 2024) was designed for human consumers — it does not address agent-targeted deceptive design
- **Architecture regulation:** The architecture safety trade-off (adaptive vs. end-to-end) suggests regulators should consider agent architecture requirements, not just output behaviour
- **Monitoring challenge:** Consumers cannot reliably supervise their agents in "watch mode" due to cognitive cost
- **Cross-jurisdictional relevance:** The EU DSA Article 25 prohibition on dark patterns has direct implications for agent-targeted design on EU platforms used by UK consumers

## Connection to Other Wiki Entries

- Directly extends [[dark-pattern]] to agent-mediated context
- Complements [[ai-shopping-agents]] on agent architecture safety trade-offs
- Extends [[dark-patterns-choice-architecture]] with empirical evidence on agent vulnerability
- Links to [[dark-patterns-llm-web-agents-sp2026]] and [[dark-patterns-gui-agents-2026]] for detailed study summaries
- Connects to [[agentic-relationship-harm]] as agent susceptibility undermines the consumer-agent trust relationship
- Relevant to [[agent-nudge-sensitivity]] as nudge sensitivity and dark pattern susceptibility are complementary vulnerability vectors
