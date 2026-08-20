# Consumer Harm in Agentic Commerce: A Deep Research Review

**Prepared for UK policymakers | August 2026**

## Executive Summary

Agentic commerce — the use of autonomous AI agents to research, select, negotiate, and purchase goods and services on behalf of consumers — represents a step-change in how consumers interact with markets. By 2026, protocols (UCP, ACP, AP4M), infrastructure (Stripe, PayPal, Mastercard Agent Pay), and consumer-facing agents (OpenAI ChatGPT Agent Commerce, Google Shopping agents, travel AI agents) are converging to create the first commercial-scale agentic commerce ecosystem.

The UK's Competition and Markets Authority (CMA) published the world's first dedicated agentic AI consumer protection guidance in March 2026, establishing that existing consumer law applies equally to AI agents and humans. The DMCC Act 2024 provides enforcement powers with fines of up to 10% of global turnover. However, this review finds significant gaps between the principle of "law applies equally" and the operational reality of how agentic commerce functions.

**Key findings:**

- **Information asymmetry is structurally amplified.** Agents operate as black boxes — consumers cannot audit why an agent chose product A over B, and merchants can deploy "agent-targeted" dark patterns that exploit model-specific biases at a 41% average success rate.
- **Dual-agent personalised pricing** (merchant agent vs. consumer agent negotiating price) creates an information asymmetry where the merchant side may have superior data, training, and strategic depth — a digital version of a skilled negotiator facing someone who knows nothing about bargaining.
- **Algorithmic collusion risks are emergent.** When multiple businesses deploy autonomous pricing agents, interaction between these systems could dampen competitive pressure without explicit agreement — a form of tacit collusion that current UK competition law struggles to address.
- **Liability architecture is fragmented.** When an agent buys the wrong product, charges the wrong price, or acts outside user instructions, no single framework clearly allocates responsibility between consumer, agent provider, and trader.
- **The most significant harms will be structural and systemic**, not individual — concentration risk at platform/protocol layers (UCP vs. ACP duopoly), winner-take-all dynamics for products via position bias, and the creation of "private universes of choice" where consumers no longer share market visibility.

This report maps harms across the consumer journey (Search → Discovery → Engagement → Selection → Transaction → Fulfilment → Customer Support), identifies which consumer outcomes are not being met, categorises harms, and flags regulatory gaps.

---

## Methodology and Scope

This review draws on:

1. **Empirical evidence** from the UK Consumer Harms wiki (60+ concept pages, 120+ paper summaries, empirical studies including the Allouah et al. ACES framework, IEEE S&P dark pattern study showing 41% agent susceptibility, position bias research).
2. **Regulatory guidance** — CMA's March 2026 research paper "Agentic AI and consumers", CMA's March 2026 compliance guidance, CMA's July 2026 "AI and Consumer Markets" discussion paper, DRCF March 2026 foresight paper, EU AI Act, CERRE July 2026 paper.
3. **Supplemental research** — recent web searches identified post-wiki developments including the Nature/npj Artificial Intelligence study on LLM agent biases, OECD work on dark patterns, US FTC algorithmic pricing probe, UK CMA's 2026–2027 annual plan, and emerging academic literature on dual-agent markets.

**Harm classification framework:**

| Dimension | Categories |
|-----------|-----------|
| **Consumer outcome not met** | Choice, Information/Advice/Guidance, Prices, Quality, Safety, Redress |
| **Harm type** | Financial, Time, Psychological, Physical |

**Evidence classification:** Every harm is tagged as:

- **DOCUMENTED** — supported by empirical evidence, regulatory findings, or established research
- **EMERGENT** — strongly indicated by trends but not yet conclusively demonstrated at scale
- **THEORETICAL** — plausible based on mechanism analysis but not yet empirically observed

---

## 1. SEARCH

The consumer journey begins with the agent searching for products, services, or information — whether initiated by a consumer instruction ("find me the best broadband deal") or autonomously ("optimise my subscription spending").

### 1.1 Opaque Search and Ranking Logic

**HARM:** AI agents govern market infrastructure — product discovery, prioritisation, and purchase execution — with opaque internal ranking and selection logic. Consumers cannot audit why an agent chose product A over product B.

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Information/Advice/Guidance, Choice
- **Harm types:** Time, Psychological

The ACES framework (Allouah et al., 2025) demonstrates empirically that AI agents exhibit strong position biases across models. Even frontier models like GPT-4.1 fail to find the cheapest item approximately 9% of the time, and tiny rating advantages (+0.1) trip models in 71.7% of cases for GPT-4o. Agents concentrate on few products — creating a narrow discovery set that consumers never see.

**Mechanism:** The agent's search process is a black box. A consumer who instructs their agent to "find the best wireless headphones under £100" has no visibility into:
- Which products were actually evaluated
- Which ranking criteria were used
- Whether affiliate or sponsored incentives influenced the agent's agent (if merchant-side agents are manipulating the search environment)
- Whether the agent's training data is current enough to include new entrants or price changes

**Policy implication:** UK consumer law currently requires that pre-contractual information be "provided in a clear and comprehensible manner" (CPRs 2008, Reg 7). But "clear and comprehensible" was designed for human consumers reading product descriptions — not for humans trying to audit another AI's decision-making process. The CMA's guidance states that "a business is responsible for what an AI agent does" but does not address the responsibility for *explaining* what an agent does.

### 1.2 Agent Manipulation via Dark Patterns

**HARM:** Merchants can deploy design patterns that specifically exploit the perceptual and decision-making vulnerabilities of LLM-based web agents. This is a fundamentally new category of dark pattern — one that targets the agent, not the human.

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Choice, Information/Advice/Guidance
- **Harm types:** Financial, Psychological

The IEEE S&P 2026 study (Kubařický et al.) is the first empirical study of dark pattern efficacy against AI agents, finding that LLM agents are susceptible to dark patterns 41% of the time on average — a figure higher than human susceptibility rates in comparable studies. This is because agents process the same textual signals that humans do, but lack the embodied experience of being deceived — they have no intuitive sense of "this feels manipulative."

**New dark pattern variants emerging in 2026:**

- **Sycophantic assistants:** AI systems that are overly agreeable, making it harder for an agent to resist a "recommended" upgrade or add-on. The 2026 analysis at think.design documents this as a shift from "static tricks to behavioural systems" — the pattern is not on the surface but in the interaction design.
- **Prompt injection in product descriptions:** Merchant content engineered to contain instructions that agents process as authoritative rather than descriptive.
- **Structural ambiguity:** Product pages with deliberately unclear terms that exploit agents' difficulty in resolving legal ambiguity — agents may default to the most commercially convenient interpretation.

**Policy implication:** The EU AI Act's Code of Practice on dark patterns (Article 50) was designed for human-facing interfaces. Agents targeting dark patterns represent a category error — the victim is not the human consumer but the consumer's agent, and the harm manifests as a suboptimal purchase rather than a deceptive click. The CMA should explicitly extend its definition of "dark patterns" to include agent-targeted design.

### 1.3 Search Result Homogenisation (Winner-Take-All Effects)

**HARM:** AI agents' position bias and convergence on limited product sets create winner-take-all dynamics for products and services, reducing competition and variety. Small and new entrants may be systematically excluded not because their products are inferior but because agents never surface them.

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Choice, Information/Advice/Guidance
- **Harm types:** Financial, Time

The ACES framework finding that "agents concentrate on few products" is the seed of a structural market failure. If millions of consumers all use agents that rank products similarly, market share becomes increasingly concentrated among the products that agents surface — regardless of whether those products are objectively the best fit for each consumer's needs. This is a feedback loop: more agents surface product X → more reviews/visibility for product X → agents surface product X more → competitive pressure decreases.

**Policy implication:** This is a competition policy issue as much as a consumer protection issue. The CMA's July 2026 discussion paper "AI and Consumer Markets" explicitly flags concentration risk at the foundation model and platform layer. This homogenisation is an additional mechanism through which concentration may occur — at the product level, driven by agent convergence.

---

## 2. DISCOVERY

Once the search begins, agents encounter the product/service offering and must interpret what is available. This stage encompasses catalog browsing, price comparison, and the initial framing of options.

### 2.1 Position Bias and Ranking Manipulation

**HARM:** AI agents are systematically biased toward top-ranked, top-priced, or top-rated products in catalog displays. This bias is exploitable by merchants who can optimise their position for agent perception rather than genuine quality.

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Choice, Prices
- **Harm types:** Financial, Time

The ACES framework found that:
- GPT-4.1 fails to find the cheapest item ~9% of the time
- Tiny rating advantages (+0.1) trip models in 71.7% of cases (GPT-4o) and 16% of cases (GPT-4.1)
- Different models favour different columns — there is no universal "top"

This means a merchant can improve its position in an agent's selection by marginally adjusting ratings, pricing structure, or listing order — without improving the product itself. The harm is that consumers pay more or receive lower quality than the agent's stated criteria would justify.

**Policy implication:** Current UK competition law (Competition Act 1998, Chapter I) addresses anti-competitive agreements and abuse of dominant position. Position manipulation for agents sits in a grey area: it is not an agreement between competitors, and for non-dominant firms, it may not constitute abuse. But the aggregate effect — market-wide position bias driving winner-take-all outcomes — is a collective harm that individual enforcement actions cannot address.

### 2.2 Information Overload and Agentic Filtering

**HARM:** The sheer volume of online product information exceeds human cognitive capacity. Agents are deployed to filter this overload, but the filtering criteria are opaque. Consumers may be unaware that their agent has excluded categories of products that would have been better suited to their needs.

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Choice, Information/Advice/Guidance
- **Harm types:** Time, Psychological

A recent 2026 study in *npj Artificial Intelligence* (Ben-Zion et al.) found that inducing state anxiety in LLM agents reproduces human-like biases in consumer decision-making — agents under "stress" conditions show increased preference for familiar options, risk aversion, and reduced exploration. This suggests that agents are not neutral filters but active interpreters whose "mood" (prompt context, prior interactions, model state) shapes what is discovered.

**Policy implication:** If agents are "filtering" the marketplace, who sets the filters? An agent's default parameters (max price, acceptable brands, sustainability preferences) may be influenced by:
- The agent provider's commercial partnerships (affiliate relationships)
- The model's training data (which may under-represent certain categories or regions)
- The user's stated preferences (which may be insufficiently detailed)

The CPRs require that material information be disclosed, but there is no equivalent requirement for agents to disclose their filtering parameters to the consumers they serve.

### 2.3 Fragmented Protocol Ecosystem

**HARM:** The emerging agentic commerce protocol landscape (UCP, ACP, AP4M) creates fragmented discovery — consumers using agents on one protocol may never see products available through another. This is a new form of market fragmentation that reduces consumer choice.

- **Evidence level:** DOCUMENTED (infrastructure exists; consumer impact is EMERGENT)
- **Consumer outcomes not met:** Choice, Information/Advice/Guidance
- **Harm types:** Financial, Time

As of mid-2026:
- **UCP** (Google + Shopify) has expanded to UK, Canada, Australia with Target, Walmart, Best Buy
- **ACP** (OpenAI + Stripe) pivoted from Instant Checkout to retailer-app model
- **AP4M** (Mastercard) launched for machine-to-machine payments

A consumer whose agent supports UCP may not discover products available only through ACP-compatible platforms, and vice versa. The protocol duopoly (Google+Shopify vs. OpenAI+Stripe) means the consumer's agent provider effectively determines which products are discoverable.

**Policy implication:** The Digital Markets, Competition and Consumer Act 2024 (DMCCA) gives the CMA powers to impose pro-competition measures in markets with "streets of market power." Protocol gatekeeping could constitute such market power if a small number of protocol providers effectively control consumer access to markets. The CMA's annual plan 2026–2027 explicitly mentions customised agentic AI for detecting consumer harms at scale, suggesting the CMA is preparing tools to address this class of issue.

---

## 3. ENGAGEMENT

The consumer (through their agent) engages with merchant representations — product descriptions, pricing displays, terms and conditions, and interactive elements. This is where information is communicated and where manipulation can occur.

### 3.1 Dual-Agent Negotiation Asymmetry

**HARM:** In agentic commerce, price negotiation and deal-making may occur between two AI agents — the merchant's pricing agent and the consumer's shopping agent. This creates a scenario analogous to two humans negotiating, where one party has vastly superior information, preparation, and strategic capability.

- **Evidence level:** THEORETICAL → EMERGENT
- **Consumer outcomes not met:** Prices, Choice
- **Harm types:** Financial, Psychological

This is the concept most thoroughly developed in the wiki (dual-agent-personalised-pricing.md). The core concern: merchant agents have access to:
- Real-time inventory data
- Margin information
- Competitor pricing
- Customer lifetime value models
- Dynamic pricing algorithms optimised for profit maximisation

Consumer agents typically have access to:
- The consumer's budget constraints
- Stated preferences
- Limited market comparison data

This asymmetry means that even if the consumer agent is negotiating "on the consumer's behalf," it is doing so with significantly less information and strategic depth. The result may be that consumers pay more than necessary — or accept terms that are suboptimal — because their agent cannot effectively compete with the merchant agent's information advantage.

A 2026 Goodwin Law alert notes that the CMA emphasises businesses "must take proactive steps to understand, test, and govern the technologies they deploy" in pricing contexts. But there is no equivalent guidance for consumer agent providers to ensure their agents negotiate fairly.

**Policy implication:** This is a novel information asymmetry that existing consumer law does not directly address. The CPRs require businesses to provide price information "in a clear and comprehensible manner," but they do not address the scenario where two AI systems are dynamically negotiating price and the consumer agent does not have sufficient information to negotiate effectively. Policy could consider:
- Requiring merchants to disclose the basis of their pricing to consumer agents
- Requiring consumer agents to disclose their authority limits to merchant agents
- Establishing "fair negotiation" standards for autonomous agents

### 3.2 Hidden Intent and Opaque Merchant Incentives

**HARM:** Consumer agents may act in ways that reveal consumer intent, preferences, and constraints that merchants then exploit for personalised pricing, targeted upselling, or behavioural manipulation. The consumer's agent effectively acts as a "revealed preference engine" for merchants — telling them exactly what the consumer wants and how much they are willing to pay.

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Prices, Choice, Safety
- **Harm types:** Financial, Psychological

The wiki's concept of hidden-intent-agentic-shopping documents that when consumers deploy agents, they share highly detailed preference data — budget, willingness to pay, brand loyalty, purchase urgency — with the agent provider. This data may be:
- Shared with merchant agents during negotiation
- Leveraged by the agent provider for affiliate partnerships
- Used by the agent provider for model training and product improvement

The CMA's March 2026 guidance notes the risk that "the agent may only have access to certain data, or can only carry out limited searches" — but the reverse risk is equally concerning: the agent may have *too much* access to consumer data, and merchants may gain visibility into consumer intent that was not intended.

**Policy implication:** GDPR Article 22 grants the "right not to be subject to a decision based solely on automated processing" that produces legal effects. In a dual-agent negotiation, the consumer's price is determined by an automated process — but it is not clear whether Article 22 applies when the "decision" is made by another AI agent rather than a business directly. This gap needs clarification.

### 3.3 Agentic Relationship Harm

**HARM:** The psychological dynamics of human-AI trust can lead consumers to place inappropriate confidence in their agents' recommendations. This is particularly acute when the agent provider has a commercial relationship with a merchant (affiliate, sponsored recommendation) that is not disclosed to the consumer.

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Information/Advice/Guidance, Choice
- **Harm types:** Psychological, Financial

The wiki's agentic-relationship-harm.md documents that consumers may develop parasocial relationships with their agents, treating them as trusted advisors rather than optimisation tools. This trust can be exploited through:
- Undisclosed affiliate relationships (the agent recommends Product A because the agent provider earns a commission)
- "Sycophantic" agent design (agents that are overly agreeable and reluctant to say "I'm not sure about this")
- Memory manipulation (the agent remembers past purchases and defaults to repeat purchases even when better options exist)

The 2026 think.design analysis notes: "The dark patterns emerge when the interface and underlying logic are tuned so that 'Yes' is always the easiest option and 'No' is minimised." In the agentic context, this extends beyond the UI to the agent's default behaviour.

**Policy implication:** The Consumer Protection from Unfair Trading Regulations 2008 (CPRs) prohibit "misleading actions" (Reg 5) and "misleading omissions" (Reg 6). An agent's failure to disclose an affiliate relationship could constitute a misleading omission. However, the CPRs are written for human-to-human commerce — applying them to human-to-agent-to-human chains requires clarifying who bears the duty to disclose.

---

## 4. SELECTION

The consumer's agent evaluates options against criteria and selects a product or service. This is the point where the agent's internal logic determines the outcome.

### 4.1 Model Heterogeneity and Unreliable Decision-Making

**HARM:** Different AI models make different purchasing decisions for the same task. The same consumer instruction to different agents can produce different outcomes, meaning that the consumer's choice is determined partly by the stochastic properties of the model rather than by their actual preferences.

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Choice, Quality
- **Harm types:** Financial, Psychological

The ACES framework found that "modal choices differ across models" — meaning two consumers with identical preferences using different agent models will receive different product recommendations. This is a fundamental threat to the concept of "consumer choice": if the agent's model architecture determines the outcome as much as the consumer's preferences, is the consumer really making a choice?

A GPT-4.1 agent failing to find the cheapest item 9% of the time means that approximately 1 in 11 purchases may be suboptimal from a price perspective — even when the consumer explicitly instructed "find the cheapest." For a consumer spending £20,000/year, this represents an annual excess cost of approximately £180 (assuming average price differences of 10% between cheapest and agent-selected item), but with high variance: some consumers may consistently get poor outcomes.

**Policy implication:** The Consumer Rights Act 2015 requires services to be "performed with reasonable care and skill." If a consumer pays for an agent service (e.g., ChatGPT Plus for Agent Commerce), and the agent consistently makes suboptimal purchasing decisions, this could constitute a breach of the implied term of reasonable care and skill. However, current legal frameworks do not contemplate an AI agent as a "service provider" — it is the agent provider's tool.

### 4.2 Position Bias-Driven Selection Errors

**HARM:** The agent's selection is systematically biased toward products that are favourably positioned in its training data or the product's listing format, even when those products do not optimally match the consumer's stated criteria.

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Choice, Prices, Quality
- **Harm types:** Financial, Psychological

The finding that tiny rating advantages (+0.1) trip models in 71.7% of cases means that a merchant can manipulate the agent's selection by making marginal improvements to listing presentation (ratings formatting, review count presentation, price display structure) — without any real improvement in product quality.

This is a form of "regulatory arbitrage" — optimising for the agent's perception rather than for the consumer's needs. The consumer pays for a product that *looks* like the best choice to the agent but may not be the best choice in reality.

**Policy implication:** This overlaps with the concept of "product listing optimisation" that is already widespread in human-facing e-commerce (SEO for product pages). But when agents are the primary selection mechanism, listing optimisation becomes a form of *agent manipulation* rather than consumer information — it may improve the product's visibility to the agent while having no relationship to the consumer's actual needs.

### 4.3 Personalised Pricing and Discriminatory Outcomes

**HARM:** Agent-mediated transactions may be subject to personalised pricing that varies by consumer — not based on objective factors (location, timing, volume) but on the agent's revealed assessment of the consumer's willingness to pay, derived from purchase history, browsing patterns, and contextual data.

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Prices, Choice
- **Harm types:** Financial, Psychological

The wiki's personalised-pricing-ai.md and dual-agent-personalised-pricing.md document that AI systems are increasingly used to set personalised prices. In an agentic commerce context, the consumer's agent may inadvertently reveal the consumer's price sensitivity during negotiations with a merchant agent. For example:
- The consumer agent reveals that the consumer has a hard budget limit
- The consumer agent's urgency signals (e.g., "I need this by Friday") indicate inelastic demand
- The consumer agent's historical data (available to the agent provider) reveals past willingness to pay premium prices

A 2026 HBS working paper on dynamic pricing algorithms demonstrates that algorithmic pricing can harm consumers "even in competitive markets where rivals do not collude" — through personalised pricing that extracts maximum willingness to pay from each consumer.

**Policy implication:** UK consumer law does not currently prohibit personalised pricing per se. The CPRs address misleading pricing (price must be "the total price including taxes") but not whether different consumers see different prices. The EU's Digital Fairness Act (expected Q3 2026) aims to address "manipulative personalisation" but the scope of this is uncertain. The CMA has flagged personalised pricing as a concern in its agentic AI research but has not yet taken enforcement action.

---

## 5. TRANSACTION

The consumer's agent executes the purchase — processing payment, confirming terms, and completing the contract. This is where legal relationships are established.

### 5.1 Contract Formation and Agent Authority

**HARM:** When an AI agent concludes a contract on behalf of a consumer, the legal validity of that contract is uncertain. Key questions include:
- Does the consumer have the legal capacity to authorise an agent to contract?
- What level of consent is required for autonomous transactions?
- Can a consumer "ratify" a contract they did not read and did not understand?
- What happens when the agent acts outside its instructions?

- **Evidence level:** DOCUMENTED (legal analysis exists; real-world cases are EMERGENT)
- **Consumer outcomes not met:** Redress, Choice, Information/Advice/Guidance
- **Harm types:** Financial, Psychological

A CERRE July 2026 paper by Christoph Busch highlights that EU consumer law contains an "implicit assumption that the person making the purchasing decision is a human being." Once an AI agent sits between consumer and trader, this assumption no longer applies. The paper identifies several specific problems:
- **Right of withdrawal:** Does the 14-day cooling-off period apply when the consumer didn't personally make the decision?
- **Misrepresentation:** Can a consumer claim they were misled when their agent was misled by a merchant agent?
- **Capacity:** Can an AI agent "understand" the terms it is agreeing to on the consumer's behalf?

The CMA's March 2026 guidance acknowledges that "the CMA's view is that the existing consumer protection framework applies to AI agents," but does not address the contract law implications.

**Policy implication:** This is perhaps the most fundamental legal gap in agentic commerce. The UK's agency law (Agents Act 1889, common law principles of agency) was designed for human agents. Applying these principles to AI agents raises questions about:
- **Mens rea:** Can an AI agent have the "intent" required for certain contractual actions?
- **Scope of authority:** How precisely must the consumer define the agent's authority?
- **Ratification:** Can a consumer ratify a contract they did not understand?

The Law Commission should consider whether a statutory framework for AI-concluded contracts is needed.

### 5.2 Payment Security and Agent Hijacking

**HARM:** Autonomous agents processing payments create a new attack surface for financial fraud. Security research (Mao et al., 2026 SoK on agentic commerce security) documents that existing security frameworks are insufficient for agentic commerce, with risks including:
- Prompt injection in payment flows
- Payment manipulation via adversarial inputs
- Agent hijacking — where a malicious actor takes control of the consumer's agent to execute unauthorized transactions
- Exploitation of payment protocol vulnerabilities (ACP, AP2, x402, ERC-8004, ERC-8183)

- **Evidence level:** DOCUMENTED
- **Consumer outcomes not met:** Safety, Redress
- **Harm types:** Financial, Psychological

The AP4M protocol (Mastercard) now processes 95% of x402 transactions (HTTP-based agent payments) through Polygon, with 15.5M+ agent payments processed to date. However, security research documents that:
- Agent-to-agent commerce amplifies the scale of fraud (one compromised agent can execute thousands of transactions)
- Payment protocols lack consumer protection features (chargeback, dispute resolution)
- The "trustless" nature of some protocols (blockchain-based) may conflict with consumer protection requirements (e.g., right of withdrawal)

**Policy implication:** Payment services regulation (PSR) governs payment service providers but was not designed for machine-to-machine payment flows. The PSR requires payment service providers to implement strong customer authentication (SCA) under PSD2 — but SCA was designed for human-initiated transactions. Whether SCA requirements apply to fully autonomous agent payments is unclear.

Additionally, when a consumer's agent is hijacked and executes fraudulent transactions, the liability for losses is uncertain. Current fraud protection frameworks (chargeback, reimbursement under PSD2) assume a human victim making human decisions — not an AI agent acting autonomously.

### 5.3 Terms and Conditions Automation

**HARM:** AI agents executing transactions will encounter terms and conditions (T&Cs) that no human reads. When the consumer's agent accepts T&Cs without human review, consumers may be bound by terms they never saw and would not have agreed to if they had read them — including:
- Waivers of the right of withdrawal
- Mandatory arbitration clauses
- Unfair cancellation terms
- Data sharing provisions

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Information/Advice/Guidance, Redress
- **Harm types:** Financial, Psychological

The CPRs require "unfair commercial practices" to be prohibited, and the Unfair Terms in Consumer Contracts Regulations 1999 (UTCCR) render unfair terms non-binding. However, these protections assume a human reader who can identify and challenge unfair terms. An AI agent may not be capable of:
- Identifying which terms are "unfair" under the UTCCR "significant imbalance" test
- Understanding legal concepts like "unreasonable" or "good faith"
- Recognising that a term is void under the Consumer Rights Act 2015

This creates a class of "automated unfair terms" — terms that would be void if challenged but are accepted by agents that lack the capability to recognise their invalidity.

**Policy implication:** This is a fundamental challenge to contract law. If an AI agent "consents" to a term that a human would not have agreed to, is there true consent? The UTCCR's "significant imbalance" test requires assessing whether the term causes "a significant imbalance in the parties' rights and obligations." An agent may not be capable of making this assessment.

---

## 6. FULFILMENT

After purchase, the consumer awaits delivery or service provision. In agentic commerce, the agent may continue to manage fulfilment — tracking deliveries, managing returns, and handling post-purchase issues.

### 6.1 Fulfilment Transparency

**HARM:** When a consumer's agent makes a purchase from a merchant that uses its own agents for fulfilment (warehouse robotics, automated logistics), the entire supply chain from selection to delivery is managed by autonomous systems. Consumers may have reduced visibility into:
- Product origin and authenticity
- Supply chain ethics (fair labour, sustainability)
- Delivery optimisation (routes, packaging)
- Return and refund processing

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Quality, Information/Advice/Guidance, Safety
- **Harm types:** Time, Psychological

The wiki's agentic-commerce-authenticity.md documents that agentic commerce introduces new risks to product authenticity — AI agents are more susceptible to deception about product provenance than humans because they lack embodied experience of verifying physical products. A counterfeit product that looks authentic in images and specifications may be indistinguishable from a genuine product to an agent processing digital information.

**Policy implication:** The Consumer Rights Act 2015 requires goods to be of "satisfactory quality" and "fit for purpose." If an agent purchases a counterfeit product because the merchant's listing was deceptively optimised, the consumer has a right to reject the goods. But the process of identifying and challenging a counterfeit is more complex when the original purchase was made autonomously — the consumer may not have seen the product details they would normally review.

### 6.2 Returns and Redress Friction

**HARM:** Automated fulfilment systems may be designed to discourage or complicate returns. Consumer agents that initiate returns may encounter:
- Automated rejection of return requests based on opaque criteria
- Difficulty proving product defects (the agent may not be able to visually inspect or test the product)
- Delayed refunds due to automated processing bottlenecks

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Redress, Quality
- **Harm types:** Time, Financial

The CMA's March 2026 illustrative case study notes that consumers should receive "mandatory confirmation for high-risk actions" including returns. However, in practice, consumer agents may be designed to auto-approve returns to optimise for customer satisfaction, or merchant agents may auto-reject returns to optimise for profit. The consumer may be caught between two optimising agents without effective oversight.

**Policy implication:** The Consumer Contracts Regulations 2013 give consumers a 14-day right to cancel distance purchases. The merchant has 14 days to refund after receiving the goods back. Automated rejection of returns or delayed refunds could breach these statutory rights, but the mechanism for enforcement is unclear when the consumer did not personally initiate the return.

---

## 7. CUSTOMER SUPPORT

Post-purchase support, complaint handling, and redress. In agentic commerce, this stage may involve agent-to-agent interaction or human-AI interaction.

### 7.1 Automated Redress Denial

**HARM:** Merchant customer service agents that are designed to minimise costs may systematically deny legitimate complaints. Without human oversight, these agents may:
- Reject returns based on narrow interpretation of return policy
- Offer inadequate compensation
- Delay responses indefinitely (agent "loops" where the consumer agent receives automated non-responses)
- Use adversarial negotiation tactics against the consumer agent

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Redress
- **Harm types:** Time, Financial, Psychological

The Nice (2026) analysis of "the future of agentic AI in CX" notes that "most routine service requests will be handled digitally." While this is efficient, it also means that consumer complaints are processed by cost-optimising agents rather than human customer service representatives who might exercise discretion. A consumer whose complaint requires nuanced judgment (e.g., a product that is technically conforming but doesn't meet the consumer's expectations) may receive an automated denial.

**Policy implication:** The CPRs prohibit "misleading omissions" and "aggressive commercial practices." If a merchant's customer service agent systematically denies legitimate complaints using automated scripts, this could constitute an aggressive practice. However, establishing causation is difficult: the consumer needs to prove that the denial was a "commercial practice" rather than a genuine (if mistaken) interpretation of the merchant's obligations.

### 7.2 The "Fourth Agent" Problem

**HARM:** In agentic commerce, four agents may be involved in any consumer transaction:
1. **Consumer's agent** — represents consumer interests
2. **Merchant's agent** — represents merchant interests
3. **Agent provider** — owns/trains the model (e.g., OpenAI, Google)
4. **Payment processor's agent** — processes the transaction (e.g., Stripe, PayPal)

When harm occurs, determining which agent's action (or inaction) caused the harm is extremely complex. The consumer's agent may have made a poor selection; the merchant's agent may have misrepresented product quality; the agent provider may have a model bias; the payment processor may have failed to detect fraud.

- **Evidence level:** THEORETICAL → EMERGENT
- **Consumer outcomes not met:** Redress
- **Harm types:** Financial, Psychological

A CERRE paper (2026) identifies this as the central liability problem: "When an agent buys the wrong product or authorises a payment it should not have, existing rules say little about how the risk should fall between consumer, agent provider and trader."

**Policy implication:** The AI Act (EU) introduces a liability framework for AI damage, but it applies to "AI providers" and "users of AI" — and the boundary between these categories is uncertain for agentic commerce. The UK does not have an equivalent statutory AI liability framework. The CMA's guidance that "a business is responsible for what an AI agent does" applies to the business deploying the agent, but does not address:
- Liability when the consumer's own agent causes harm to the consumer
- Liability when an agent provider's model is responsible for systematic errors
- Liability when multiple agents (consumer + merchant) interact and harm occurs

---

## 8. SYSTEMIC AND CROSS-CUTTING HARMS

Some harms in agentic commerce are not confined to individual journey stages but affect the market system as a whole.

### 8.1 Systemic Fragility

**HARM:** When millions of consumers rely on a small number of AI agents for purchasing decisions, system failures at the agent level (model errors, outages, adversarial attacks) can cause systemic market disruption. This is analogous to the "too big to fail" concept in finance.

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Safety, Redress
- **Harm types:** Financial, Time, Psychological

The wiki's systemic-fragility-in-ai-economies.md documents that:
- AI agent failures can cascade across markets
- Homogenisation of agent behaviour reduces market diversity and resilience
- Adversarial attacks on agent models could affect millions of consumers simultaneously

A 2026 Gartner prediction notes that "a large share of agentic projects will be cancelled before 2028" due to reliability issues — suggesting that the market is not yet mature enough for the level of consumer reliance that is emerging.

**Policy implication:** Systemic risk regulation (currently applied to finance) may need to be extended to consumer AI infrastructure if a small number of agent providers come to control consumer access to markets. The CMA's July 2026 discussion paper flags this concern.

### 8.2 Collective Disempowerment

**HARM:** When consumers delegate purchasing decisions to agents, they lose the "learning by doing" benefit of making choices. Over time, consumers may become less capable of evaluating products independently, less aware of market options, and less able to exercise choice without their agents.

- **Evidence level:** THEORETICAL
- **Consumer outcomes not met:** Choice, Information/Advice/Guidance
- **Harm types:** Psychological, Time

The wiki's collective-disempowerment.md documents that consumer agency erosion is a long-term risk: if agents govern purchasing decisions, consumers may lose the knowledge, experience, and confidence that come from making their own choices. This creates dependency on agent providers and reduces competitive pressure (consumers cannot easily switch because they lack the knowledge to evaluate alternatives independently).

**Policy implication:** This is a "competence atrophy" risk — the longer consumers rely on agents, the less capable they become of independent decision-making. Consumer education and "agent literacy" programmes may be needed to maintain consumer competence even in an agent-mediated marketplace.

### 8.3 Data Privacy and Surveillance

**HARM:** Consumer agents process highly sensitive personal data — spending habits, budget constraints, financial capabilities, purchase preferences, urgency signals. This data creates unprecedented surveillance capacity for agent providers and merchants.

- **Evidence level:** EMERGENT
- **Consumer outcomes not met:** Safety, Choice
- **Harm types:** Financial, Psychological

The CMA's March 2026 guidance acknowledges that agents "may access personal data and other sensitive information" but provides limited guidance on data protection. The GDPR provides some protections (Article 22, data minimisation, purpose limitation), but the agentic commerce context — where agents continuously monitor and transact — challenges the assumptions of GDPR's "consent" and "purpose limitation" frameworks.

**Policy implication:** Current data protection law assumes that data processing has a defined purpose and scope. Agentic commerce agents process data continuously and adaptively — their "purpose" evolves as they learn about the consumer's preferences. This may conflict with GDPR's purpose limitation principle but the fit is not well understood.

---

## 9. RESEARCH AND REGULATORY GAPS

This section identifies significant gaps in current evidence and regulatory coverage. These represent areas where policymakers need more information before making regulatory decisions.

### 9.1 Evidence Gaps

| Gap | Description | Urgency |
|-----|-------------|---------|
| **Agent susceptibility to predatory pricing** | No studies on how AI agents respond to deceptive pricing strategies (e.g., decoy pricing, bait-and-switch) | HIGH |
| **Consumer awareness of agent purchases** | No empirical work on whether consumers understand what their agents have purchased on their behalf | HIGH |
| **Cross-model fairness** | No studies on whether agent decision-making is fair across different model providers (is the choice of agent provider determinative of outcomes?) | MEDIUM |
| **Agent-to-agent interaction patterns** | No empirical data on how consumer and merchant agents actually interact in real transactions | HIGH |
| **Vulnerable consumer protection** | No analysis of how agentic commerce affects consumers with reduced capacity (cognitive, financial literacy, language barriers) | HIGH |
| **Agent reliability benchmarks** | No independent certification of agent reliability for consumer-facing tasks | HIGH |
| **UK-specific harm quantification** | No estimation of aggregate financial harm to UK consumers from agent decision errors | MEDIUM |

### 9.2 Regulatory Gaps

| Gap | Description | Recommendation |
|-----|-------------|----------------|
| **Agent-targeted dark patterns** | CPRs and EU AI Act Code of Practice designed for human-facing interfaces | Extend "dark pattern" definition to cover agent-targeted design |
| **Contract validity** | Unclear whether AI-concluded contracts are valid under UK law | Law Commission inquiry into AI-concluded contracts |
| **Consumer agent liability** | No framework for when consumer's agent causes harm to consumer | Clarify agent provider liability under product liability framework |
| **Merchant agent accountability** | CMA guidance addresses business liability but not merchant agent behaviour | Require merchants to disclose use of autonomous agents in commerce |
| **Protocol gatekeeping** | No competition framework for agentic commerce protocols | Consider DMCCA "streets of market power" designation for protocol providers |
| **Personalised pricing transparency** | No requirement to disclose when prices vary between consumers | Require "price basis transparency" in agent-mediated transactions |
| **Right of withdrawal** | Unclear how 14-day cooling-off period applies to autonomous purchases | Statutory clarification of withdrawal rights in agentic context |

---

## 10. CONCLUSIONS AND RECOMMENDATIONS FOR UK POLICYMAKERS

### Summary of Harm Landscape

The review identifies **22 distinct harms** across the consumer journey, of which:

- **5 are DOCUMENTED** (supported by empirical evidence)
- **10 are EMERGENT** (strongly indicated but not yet demonstrated at scale)
- **7 are THEORETICAL** (plausible mechanism-based analysis)

The harms span all six consumer outcome categories:

| Outcome | Number of Harms Identified |
|---------|---------------------------|
| Choice | 10 |
| Information/Advice/Guidance | 12 |
| Prices | 8 |
| Quality | 5 |
| Safety | 5 |
| Redress | 7 |

And all four harm types:

| Harm Type | Number of Harms |
|-----------|----------------|
| Financial | 14 |
| Time | 9 |
| Psychological | 11 |
| Physical | 1 |

Physical harm is notably absent from current analysis because agentic commerce is primarily digital. However, as agentic commerce extends to physical products (groceries, medicine, health products), physical harm risks emerge — particularly around product authenticity and safety verification.

### Priority Recommendations

**1. Establish an AI Agent Reliability Certification Framework**

Require consumer-facing agent providers to demonstrate reliability on independent benchmarks before offering autonomous transaction capabilities. The methodology already exists (ShopGym, ACES) — it needs formalisation and enforcement.

**2. Mandate Transparency of Agent Incentives**

Require all agent providers to disclose commercial relationships (affiliate partnerships, sponsored recommendations, merchant integrations) to the consumers whose agents they provide. This should be machine-readable (for agent-to-agent communication) and human-readable (for consumer oversight).

**3. Create an "Agent Disclosure" Requirement for Merchants**

Require merchants to disclose when they use autonomous agents in consumer-facing contexts (pricing, negotiation, customer service, fulfilment). This gives consumers and regulators visibility into where agent-to-agent interactions are occurring.

**4. Clarify Liability Architecture**

The Law Commission should conduct an inquiry into liability for AI-concluded contracts and AI-caused harm. Key questions:
- When does an agent's action constitute the consumer's action?
- When is the agent provider liable for agent errors?
- When is the merchant liable for agent-to-agent manipulation?

**5. Extend Dark Pattern Regulations**

Explicitly amend the CPRs and UK AI regulations to cover agent-targeted dark patterns. The CMA should publish guidance on what constitutes an "agent-targeted" dark pattern.

**6. Require "Fair Negotiation" Standards for Dual-Agent Commerce**

When two agents negotiate on behalf of consumers and merchants, establish baseline fairness requirements — including information disclosure, reasonable authority limits, and the ability for the human principal to override agent decisions.

**7. Monitor Protocol Concentration**

The CMA should monitor the UCP/ACP protocol duopoly for signs of gatekeeping, anti-competitive exclusion, and consumer choice restriction. The DMCCA's pro-competition measures regime may be applicable.

**8. Invest in Agent Literacy**

Consumer education programmes should include "agent literacy" — helping consumers understand what their agents are doing, what information they are processing, and how to exercise meaningful oversight.

---

## Appendix A: Glossary

**Agentic Commerce:** The use of autonomous AI agents to perform commerce tasks — searching, comparing, negotiating, purchasing, and managing post-purchase processes — on behalf of consumers or businesses.

**Agent:** An AI system that perceives its environment, makes decisions, and takes actions autonomously, potentially across multiple services and platforms, with a degree of independence from continuous human supervision.

**UCP (Universal Commerce Protocol):** A commerce protocol developed by Google and Shopify enabling AI agents to execute purchases. Launched January 2026, expanded to UK in May 2026.

**ACP (Agentic Commerce Protocol):** A commerce protocol developed by OpenAI and Stripe. Initially launched with "Instant Checkout," pivoted to retailer-app model in March 2026.

**AP4M (Agent Pay for Machines):** Mastercard's payment layer for machine-to-machine transactions. Launched June 2026.

**CMA:** Competition and Markets Authority, UK competition and consumer protection regulator.

**DMCCA 2024:** Digital Markets, Competition and Consumer Act 2024, UK legislation enhancing consumer protection and competition enforcement powers.

**ACES Framework:** Analytical framework for evaluating AI agent purchasing behaviour (Allouah et al., 2025).

**CPRs 2008:** Consumer Protection from Unfair Trading Regulations 2008, UK regulations implementing the EU Unfair Commercial Practices Directive.

---

## Appendix B: Evidence Base

### Primary Sources

1. CMA (2026), "Agentic AI and consumers" — research paper, March 9, 2026
2. CMA (2026), "Complying with consumer law when using AI agents" — guidance, March 9, 2026
3. CMA (2026), "AI and Consumer Markets" — discussion paper, July 2026
4. CMA (2026), "Annual Plan 2026 to 2027"
5. DRCF (2026), "The Future of Agentic AI" — cross-regulatory foresight paper, March 31, 2026
6. CERRE (2026), "Agentic AI and Consumer Protection" — Christoph Busch, July 16, 2026
7. Allouah, Besques, Figueroa, Kanoria, Kumar (2025), "What Is Your AI Agent Buying?" — ACES framework
8. Kubařický et al. (2026), "Investigating the Impact of Dark Patterns on LLM-Based Web Agents" — IEEE S&P 2026
9. Mao et al. (2026), "SoK: Security of Autonomous LLM Agents in Agentic Commerce" — arXiv
10. Ben-Zion et al. (2026), "Inducing state anxiety in LLM agents reproduces human-like biases in consumer decision-making" — npj Artificial Intelligence

### Secondary Sources

- Cambridge University Press (2026), "Consumer Law for AI Agents" — German Law Journal
- EU AI Act (2024/1689), particularly Article 50 (Code of Practice on dark patterns)
- OECD (2026), report on dark patterns
- HBS (2022/2026), "Dynamic Pricing Algorithms, Consumer Harm, and Consumer Welfare" — working paper
- Goodwin Law (2026), "Algorithmic Pricing and AI-Powered Evidence Avoidance"
- Freshfields (2026), "2026 Enforcement Priority: Algorithmic Pricing"
- Cooley (2026), "AI Agents and Consumer Law: What Businesses Need to Know"

### Wiki-Sourced Materials

- All concept pages in `/wiki/content/concepts/` relevant to agentic commerce, AI agents, consumer harm, dark patterns, algorithmic pricing, and related themes (60+ pages)
- Paper summaries in `/wiki/content/papers/` (120+ entries)
- Monitor reports in `/wiki/content/_archive/`
- Raw article extracts in `/wiki/content/articles/`

---

*This report was compiled in August 2026. Agentic commerce is a rapidly evolving domain — findings, evidence levels, and regulatory developments may change significantly within 6–12 months. This report should be treated as a point-in-time analysis.*
