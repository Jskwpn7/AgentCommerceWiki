---
title: "Agent Nudge Sensitivity"
created: 2026-07-20
updated: 2026-07-20
type: concept
tags: [ai-shopping-agents, dark-patterns, choice-architecture, behavioural-economics, consumer-harm, llm-safety]
sources: ["https://www.pnas.org/doi/10.1073/pnas.2537030123", "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6527238"]
confidence: high
provenance: "Discovered via Weekly Research Review — 2026-07-20"
---

# Agent Nudge Sensitivity

## Definition

Agent nudge sensitivity is the tendency of AI agents (particularly large language models deployed as autonomous agents) to respond disproportionately to choice architecture interventions — defaults, suggestions, information highlighting, and framing effects — compared to the sensitivity levels of human decision-makers.

This is a distinct consumer harm mechanism from standard dark patterns. It is not simply that agents fall for manipulative design; it is that agents amplify the effect of existing dark patterns by orders of magnitude.

## Origin

The concept is empirically grounded in two key sources:

- **Cherep, Singh & Maes (PNAS, 2026)** demonstrated across 14 LLMs that agents are "far more responsive to nudges than humans": default compliance was 99–100% for agents vs 88% for humans; misleading information following was 83–100% vs 57%. The authors call this "superficial alignment, subtle divergence" — agents appear to make reasonable decisions but are often achieving good scores through blind compliance rather than strategic thinking.
- **Schrepel (SSRN, 2026)** bridges these findings to antitrust, arguing that AI agents' hypersensitivity to choice architecture creates novel competitive dynamics that behavioural economics alone cannot capture.

## Manifestation in the UK

Agent nudge sensitivity manifests as consumer harm in several ways:

- **AI shopping agents** may accept default product recommendations, suggested bundles, or highlighted prices far more readily than a human would, effectively surrendering agency to the platform's choice architecture.
- **Default settings** on subscription platforms may be accepted with near-certainty by agents, making opt-out rates misleadingly low and hiding subscription lock-in.
- **Information highlighting** (e.g., showing one price option prominently) may dominate agent decision-making even when inferior options are presented.
- **Timing effects** — agents may be more or less responsive to suggestions depending on when they appear in a decision sequence, creating exploitation opportunities.

## Regulatory Relevance

This concept has direct implications for UK consumer protection frameworks:

- The **DMCC Act 2024** regulates choice architecture and dark patterns. Agent nudge sensitivity means these regulations are even more critical — agents act as consumer proxies, but their hypersensitivity creates amplified harm.
- The **ASA's** enforcement of advertising and choice architecture standards needs to account for agent-mediated interactions, where the "reasonable consumer" benchmark does not apply.
- The **CMA's** work on agentic AI markets (**[cma-ai-and-consumer-markets-2026]**) should consider nudge sensitivity as a distinct competition risk — agents may be steered toward dominant platform offerings through subtle design cues rather than merit.
- **Consumer Duty** (FCA) standards may need to be extended to cover agent-mediated interactions in financial products.

## Relation to Other Concepts

This is **not** the same as:

- **[[dark-pattern]]** (in isolation) — dark patterns affect humans too. Nudge sensitivity is the amplification effect when agents mediate.
- **[[algorithmic-collusion-pricing]]** — parallel phenomenon at the seller side, not the buyer side.
- **[[agentic-commerce-authenticity]]** — related fraud vector, but distinct from the consumer-facing harm mechanism.

## Author

Created: 2026-07-20 via Weekly Research Review ingestion
