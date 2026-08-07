---
title: "Open rails for agentic commerce at Open Source Summit North America 2026"
authors:
  - name: Anurag Sinha
    affiliation: Universal Commerce Protocol (UCP)
publication: Google Open Source Blog
type: blog
date_published: 2026-06-16
date_added: 2026-06-23
source_url: https://opensource.googleblog.com/2026/06/open-rails-for-agentic-commerce-at-open-source-summit-north-america-2026.html?m=1
tags:
  - Agentic commerce
  - AI agents
  - Interoperability
  - Open standards
  - UCP
  - Universal Commerce Protocol
---

# Open rails for agentic commerce at Open Source Summit North America 2026

## Metadata

- **Author:** Anurag Sinha, Universal Commerce Protocol (UCP)
- **Publication:** Google Open Source Blog
- **Date:** Tuesday, June 16, 2026
- **Event:** Open Source Summit North America 2026

## Full Article

At Open Source Summit North America 2026, I shared why agentic commerce needs open rails.

As AI agents become more capable, the shopping journey is shifting from "show me" to "help me." Instead of browsing, comparing, clicking, and checking out step by step, people can increasingly ask an agent to help them decide what to buy and, in some cases, complete the purchase. Industry forecasts suggest agentic shopping could account for roughly 10% to 25% of U.S. e-commerce by 2030 (Bain), which points to a meaningful shift in how digital commerce will work. Watch the full keynote [here](#).

## Why shared rules matter

That shift also exposes a challenge. Commerce is still highly fragmented. Different businesses, payment providers, and platforms operate with their own rules, workflows, and business logic. Every new surface adds more integration work. Every bespoke connection creates more complexity. And that fragmentation makes it harder for AI systems to understand and perform commerce actions consistently across businesses. A shared language lowers that barrier for everyone.

**A common language for agentic commerce**

That is the problem Universal Commerce Protocol (UCP) is designed to solve.

We launched the Universal Commerce Protocol, or UCP, with industry leaders to establish an open standard for agentic commerce, built to work across the shopping journey. UCP creates a common language for agents and systems to operate together across consumer surfaces, businesses, and payment providers, so the ecosystem does not need a different bespoke integration for every new agent or platform.

Just as importantly, UCP is designed for the real world. Every business has its own way of selling. Checkout, fulfillment, loyalty, policy logic, shipping, and post-purchase flows can vary widely between a local shop, a marketplace, and a large retailer. UCP is built to support that reality.

UCP Architecture Diagram: The common language for platforms, agents and businesses. Central UCP framework containing modules for 'Shopping' and 'Common' services, flanked by 'Consumer platforms' on the left and 'Business platforms' on the right, with bidirectional arrows showing how they connect and communicate through the central protocol.

## A layered architecture for a shared commerce language

UCP uses a layered model to create a reusable shared language for commerce.

- **Services** — Organize domains like shopping and common.
- **Capabilities** — Define core actions such as checkout, catalog, cart, orders, and shared functions like identity linking.
- **Extensions** — Keep those capabilities configurable, so features like fulfillment can be modeled once and reused across multiple flows instead of being hardwired each time.
- **Transport layer** — UCP stays agnostic, supporting bindings like REST, Model Context Protocol (MCP), and Agent2Agent.

Together with capability discovery and payment handling, these layers help consumer platforms, agents, and businesses interoperate more consistently over time. They also let different participants advertise what they support, compose new behaviors, and communicate over the transport that works best for them.

## Built in the open

A standard for everyone should be shaped by everyone. Because UCP is open, merchants, developers, and community contributors can pressure-test real-world gaps, propose new capabilities and extensions, and help make sure the protocol reflects more than the needs of the largest players. That kind of participation is what keeps an ecosystem moving.

Since launch, UCP has continued to evolve through new capabilities, an expanded Tech Council, and new consumer experiences built on top of the protocol. That momentum matters because standards only work when the ecosystem uses them.

Agentic commerce is still evolving, and UCP is a foundational building block to support what's next in this new era.

## Resources

- **Full keynote:** [Open Source Summit North America 2026 presentation](#)
- **UCP documentation:** [UCP docs](#)
- **Community conversation:** [Discussion forum](#)
- **Contribute:** [Public repository](#)

---

# Summary and Analysis

## Key Claims

1. **Agentic commerce forecast:** Bain predicts agentic shopping could account for 10–25% of U.S. e-commerce by 2030.
2. **Fragmentation problem:** Commerce is highly fragmented across businesses, payment providers, and platforms — each with their own rules, workflows, and business logic.
3. **UCP as solution:** Universal Commerce Protocol provides an open standard for agentic commerce, creating a common language for agents and systems across consumer surfaces, businesses, and payment providers.
4. **Layered architecture:** Services → Capabilities → Extensions → Transport (REST, MCP, Agent2Agent agnostic).
5. **Built-in flexibility:** UCP designed for real-world diversity — local shops, marketplaces, and large retailers each have different checkout, fulfillment, loyalty, policy, shipping, and post-purchase flows.
6. **Governance model:** Open standard with expanded Tech Council, capability discovery, and community contribution to a public repository.

## Consumer Harm Relevance

| Dimension | Connection |
|---|---|
| **Platform power & lock-in** | Open standards (UCP) vs. proprietary commerce APIs directly relate to consumer choice and switching costs in agentic commerce |
| **Interoperability** | A shared commerce language could reduce platform vendor lock-in for both consumers and merchants |
| **Agentic shopping bias** | If UCP defines the "rails," who controls the standard matters for whether agents can compare across platforms impartially |
| **Market concentration** | Industry leaders co-launching a standard could entrench dominant players; "open" governance needs scrutiny |
| **Consumer transparency** | Protocol-level interoperability may affect whether consumers understand which platform/merchant their agent is purchasing from |
| **Payment data flows** | UCP's payment handling capabilities could centralize consumer payment data in ways that need regulatory scrutiny |

## Cross-References

- Related to [[ai-shopping-agents]] (AI agents making purchasing decisions)
- Related to [[agentic-commerce-deep-dive-fd-robonomics]] (commerce taxonomy, platform power)
- Related to [[agentic-commerce-deep-dive-ii-fd-robonomics]] (new digital tax, off-site purchasing squeeze)
- Related to [[algorithmic-collusion-pricing]] (protocol-level coordination risks)
- Related to [[conflict-of-interest-in-llm-deployment]] (who controls the rails controls the rails)
- Related to [[online-choice-architecture-and-dark-patterns-in-the-UK]] (open standards as consumer protection)
