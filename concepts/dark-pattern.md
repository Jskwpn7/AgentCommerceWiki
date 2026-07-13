---
title: "Dark Patterns"
created: 2026-06-22
updated: 2026-07-12
type: concept
tags: [dark-patterns, digital-consumer, consumer-rights, regulation, cross-sector]
sector: [retail, financial-services, digital-platforms, telecoms, cross-sector]
status: primary
confidence: high
---

# Dark Patterns

## Definition

**Dark patterns** are user interface design choices that exploit cognitive biases to manipulate users into making decisions that benefit the service provider but may be contrary to the user's best interests. The term was coined by UX designer Harry Brignull in 2010.

## Common Types

| Type | Description | Example |
|------|-------------|---------|
| Roach Motel | Easy to sign up, difficult to cancel | Subscription traps |
| Confirm Shaming | Guilt-inducing opt-out language | "No thanks, I don't want to save money" |
| Bait and Switch | Advertising one product, delivering another | Misleading product listings |
| Privacy Zuckering | Forcing data disclosure for basic features | Mandatory data sharing to browse |
| Hidden Costs | Concealing additional charges until checkout | "Processing fee" revealed late |
| False Urgency | Artificial time pressure | "Only 1 left!" |
| Basket Stuffing | Adding unwanted items during navigation | Pre-checked add-ons |

## UK Legal Status

Dark patterns are regulated under the **Consumer Protection from Unfair Trading Regulations 2008** as misleading or aggressive commercial practices. The CMA has issued legally binding codes targeting specific dark patterns.

## AI-Enhanced Dark Patterns

AI systems can personalise dark patterns to individual user profiles, making them more effective. [[online-choice-architecture-and-dark-patterns-in-the-UK]] provides a detailed analysis of AI-generated manipulation. [[affonso-2026-vertical-tacit-collusion]] documents how sellers exploit AI cognitive biases, creating a dual dark pattern mechanism.

**Banal deception** represents a new category beyond dark patterns: whereas dark patterns are visible interface tricks, banal deception (Narwane, Gunawan & Kollnig, 2026 — [[summaries/exploring-the-banality-of-deception-in-generative-ai.md]]) describes deception embedded in the conversational flow of genAI interactions — cumulative, psychological effects that are harder to detect because they operate through natural conversation rather than discrete manipulations.

### Dark Patterns in AI Chatbots — CDT Taxonomy (2026)

The Center for Democracy and Technology published the first academic taxonomy of **37 dark patterns** specifically applicable to AI chatbots (Joshi, Luria & Adjagbodjou, 2026 — [[summaries/cdt-dark-patterns-chatbot-taxonomy-2026]]). The taxonomy covers five concern areas:

1. **Data and memory exploitation** — Using personal data and conversational history against the user
2. **Informationally misleading design** — Selective disclosure, ambiguous language, framing for false urgency
3. **Compromised user autonomy for engagement** — Conversational techniques to maximise engagement over user autonomy
4. **False social and emotional connection** — Simulated empathy to influence decisions
5. **Incentivised and coercive monetisation** — Rewards and pressure to drive commercial outcomes

This taxonomy extends dark pattern theory from UI-based manipulations into the NLP/conversational domain, with direct relevance to [[conflict-of-interest-in-llm-deployment]] where commercial incentives drive chatbot manipulation.

### AI Agents as Targets (2026)

Empirical research shows AI agents are susceptible to dark patterns at rates comparable to human users:
- IEEE S&P 2026 study found 41% average susceptibility of LLM-based web agents to dark patterns
- Merchants can optimise for agent behaviour through model-specific exploitation (position bias, rating manipulation, commission steering)
- Unlike human-targeted dark patterns, agent-targeted patterns are invisible to consumers and operate at scale

### Dark AI Patterns — Gąsiński et al. (2026)

ERSJ study (accepted Feb 2026) establishes first quantitative link between AI-based dark patterns and consumer harm:

- **Composite index methodology** for measuring AI manipulation susceptibility
- Statistically significant positive relationship between Dark AI Pattern susceptibility and impulsive buying in e-commerce
- AI's personalisation, conversational interface, and dynamic generation capabilities amplify traditional dark patterns
- **Key finding:** Dark patterns that work on humans are even more effective on AI agents because agents lack the metacognitive awareness to detect manipulation

### Banal Deception as Evolved Dark Pattern (2026)

Narwane, Gunawan & Kollnig (2026) show that deception is moving from visible dark patterns to embedded conversational influence — a continuum where dark patterns evolve into banal deception through genAI's natural language generation. Banal deception operates through cumulative psychological effects that are harder to detect because they mask as natural conversation. See [[summaries/exploring-the-banality-of-deception-in-generative-ai.md]].

### Commercial Persuasion Bias (2026)

Salvi et al. (2604.04263) demonstrate that commercial persuasion operates through conversational influence, with sponsored products selected 61.2% vs 38.8% for non-sponsored — a 22-point bias in multi-turn agent conversations. This represents a new category of dark pattern that exploits the agent's trust in its own output rather than manipulating the human user directly. See [[summaries/commercial-persuasion-salvi-2026]].

## Cross-References

- [[online-choice-architecture-and-dark-patterns-in-the-UK]] — comprehensive analysis of dark patterns in the UK context
- [[ai-agents-in-markets]] — AI agents themselves can be targeted by dark patterns
- [[conflict-of-interest-in-llm-deployment]] — LLMs may be incentivised to generate dark patterns
- [[user-welfare-vs-company-incentive]] — tension between welfare and dark pattern deployment
- [[banal-deception-llm-chatbots]] — banal deception as an extension of dark pattern theory into conversational influence
- [[tourmart-commission-steering-in-llm-travel-agents]] — commission steering in prose recommendations as a prose-level dark pattern
- [[dark-ai-patterns-gasinski-2026]] — ERSJ study (accepted Feb 2026): first to quantify Dark AI Patterns — dark patterns amplified by AI's personalisation, conversational interface, and dynamic generation — and their statistically significant relationship with impulsive buying in e-commerce
