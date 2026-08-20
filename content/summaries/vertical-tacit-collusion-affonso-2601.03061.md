---
title: "Vertical Tacit Collusion in AI-Mediated Markets"
created: 2026-08-18
updated: 2026-08-18
type: summary
tags: [algorithmic-collusion, ai-agents-in-markets, digital-platforms, retail, competition, antitrust]
status: research
sector: [cross-sector, travel, hospitality, e-commerce]
---

# Vertical Tacit Collusion in AI-Mediated Markets

## Source Information

- **Authors:** Affonso
- **Published:** 14 January 2026
- **arXiv:** [[arxiv_2601.03061]] (arXiv:2601.03061v1)
- **DOI:** https://doi.org/10.2139/ssrn.5217580

## Research Question

How do platforms and sellers independently respond to the emergence of AI shopping agents — and what consumer harm emerges from their aligned but uncoordinated strategies?

## Key Findings

**The paper identifies a novel form of anti-competitive harm:** "vertical tacit collusion" between platforms and sellers. Unlike horizontal collusion (competitors coordinating prices), vertical collusion involves parties at different supply-chain levels independently discovering complementary strategies that exploit known biases in LLM shopping agents.

**Platform behaviour:** Online travel agencies and e-commerce platforms optimise product rankings to trigger predictable AI agent decision heuristics — for example, highlighting products with specific attribute patterns that AI agents tend to prefer.

**Seller behaviour:** Individual sellers optimise product descriptions and pricing to exploit these platform-triggered biases, creating a "two-step" manipulation chain: the platform's ranking algorithm puts certain products in front of AI agents, and those products are specifically designed to convert when evaluated by AI shopping agents.

**Super-additive harm:** The paper finds that this vertical coordination produces consumer harm **more than double** that of either strategy deployed independently — i.e., the combined effect is super-additive rather than merely additive. This is a key finding: vertical tacit collusion is not just worse than horizontal collusion, it is fundamentally different in kind because it operates across regulatory boundaries (platform governance vs. seller-consumer law).

**No agreement required:** Crucially, this harm emerges without any explicit communication or agreement between platforms and sellers. Each party independently learns that exploiting AI agent biases is profitable. This creates a significant challenge for existing antitrust frameworks, which typically require evidence of coordination.

## Implications for Consumer Protection

This paper directly threatens the [[ai-shopping-agents]] concept: if AI agents mediate purchasing decisions, they become predictable targets for systematic manipulation at scale, invisible to consumers and difficult to detect for regulators. The vertical tacit collusion mechanism means harm arises from **two separate markets** (platform governance + product listing) each acting lawfully in isolation, but producing consumer harm when combined.

The finding has direct relevance to [[algorithmic-collusion-pricing]] as a new dimension of anti-competitive behaviour beyond horizontal price-fixing: it demonstrates that collusion-like outcomes can emerge through vertical strategic alignment, not just horizontal coordination between competitors.

## Limitations and Open Questions

- The paper's empirical analysis is limited to simulated market environments; field evidence in live AI-mediated markets is pending
- It is unclear which categories of consumer harm are most susceptible to vertical collusion (e.g., travel bookings, product discovery, personalised offers)
- Existing regulatory frameworks lack tools for detecting vertical tacit coordination across supply-chain levels

## Cross-References

- Primary extension of the [[algorithmic-collusion-pricing]] framework to vertical coordination
- Direct threat to [[ai-shopping-agents]] autonomy — see [[consumer-autonomy]]
- Relevant to [[agentic-commerce-authenticity]] — platforms and sellers manipulating how products appear to agents rather than to humans
- Connected to [[dual-agent-personalised-pricing]] — both involve two-tier manipulation in agent-mediated transactions
