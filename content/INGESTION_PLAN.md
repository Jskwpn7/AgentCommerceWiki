# Agentic Commerce Wiki: Missing Reference Ingestion Plan

**Source:** https://github.com/yifeizhangcs/awesome-agentic-commerce (Zhang et al. 2026 companion survey)
**Current wiki state:** 94 summaries, 52 concepts, 27 entities, 28 raw papers, 42 raw articles, 243 total pages
**Items missing from wiki:** 101 (55 arXiv papers + 46 non-arXiv URLs)
**Plan created:** 2026-08-04
**Status:** READY TO EXECUTE

---

## Execution Strategy

This plan prioritizes by **consumer harm relevance** first, then **research recency**, then **citation impact**. Execute in batch order. Each item should be ingested as a separate wiki page following the `wiki-ingest` schema rules.

### Priority Categories (ingest in this order):

1. **HIGH PRIORITY — Consumer Harm & Safety Risks** (12 items)
   - Papers directly studying agent manipulation, payment vulnerabilities, dark patterns, generative engine optimization
2. **HIGH PRIORITY — Benchmarks & Evaluation** (8 items)  
   - Papers establishing evaluation frameworks for agentic commerce
3. **MEDIUM PRIORITY — E-commerce Infrastructure** (20 items)
   - Papers on recommendation systems, search, pricing, supply chain agents
4. **MEDIUM PRIORITY — Negotiation & Agent Interaction** (7 items)
   - Papers on agent-to-agent negotiation, market dynamics
5. **LOW PRIORITY — Industry Reports & Whitepapers** (12 items)
   - Industry analysis from BCG, McKinsey, Mastercard, Visa, etc.
6. **LOW PRIORITY — Product/Platform Launches** (6 items)
   - Amazon, Alibaba, Shopify, Perplexity product announcements
7. **LOW PRIORITY — Robotics & Embodied Commerce** (8 items)
   - Papers on physical retail agents (less direct consumer harm relevance)
8. **LOW PRIORITY — Cross-Cutting Infrastructure** (28 items)
   - Agent protocols, payments, general infrastructure papers

---

## Batch 1: HIGH PRIORITY — Consumer Harm & Safety Risks (12 items)

### Batch 1A: arXiv Papers (12 items)

**1. `2506.02839` — DeepShop: A Benchmark for Deep Research Shopping Agents** (Lyu 2025)
- Category: Benchmarks / Shopping Agents
- Harm vectors: Recommendation manipulation, opaque agent behavior
- Target: `summaries/deepshop-shopping-agents-2506.02839.md`

**2. `2506.17765` — CARTS: Collaborative Agents for Recommendation Textual Summarization** (Chen 2025)
- Category: Recommendation Agents
- Harm vectors: Recommendation manipulation, hidden preferences
- Target: `summaries/cart-collaborative-recommendation-2506.17765.md`

**3. `2506.21931` — ARAG: Agentic Retrieval Augmented Generation for Personalized Recommendation** (Maragheh 2025)
- Category: Recommendation Agents
- Harm vectors: Filter bubbles, preference manipulation
- Target: `summaries/arag-personalized-recommendation-2506.21931.md`

**4. `2506.21934` — CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design** (Forouzandehmehr 2025)
- Category: UI/UX Layout Agents
- Harm vectors: Dark patterns in agent-generated layouts
- Target: `summaries/cal-rag-content-layout-2506.21934.md`

**5. `2507.02097` — The Future is Agentic: Definitions, Perspectives, and Open Challenges of Multi-Agent Recommender Systems** (Maragheh 2025)
- Category: Survey / Definitions
- Harm vectors: Broad overview of multi-agent recommendation harms
- Target: `summaries/multi-agent-rec-systems-future-2507.02097.md`

**6. `2508.02630` — What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence, & Emerging Implications for Agentic E-Commerce** (Allouah 2025)
- Category: Consumer Protection / Bias
- Harm vectors: Biased purchasing decisions, model dependence, opaque procurement
- Target: `summaries/ai-agent-buying-biases-2508.02630.md`

**7. `2508.11416` — AIM-Bench: Evaluating Decision-making Biases of Agentic LLM as Inventory Manager** (Zhao 2025)
- Category: Benchmarks / Bias
- Harm vectors: Algorithmic supply chain manipulation
- Target: `summaries/aim-bench-inventory-bias-2508.11416.md`

**8. `2510.20567` — Beyond Retrieval-Ranking: A Multi-Agent Cognitive Decision Framework for E-Commerce Search** (Zhai 2025)
- Category: Search Agents
- Harm vectors: Search result manipulation, ranking opacity
- Target: `summaries/multi-agent-search-framework-2510.20567.md`

**9. `2511.15712` — Secure Autonomous Agent Payments: Verifying Authenticity and Intent in a Trustless Environment** (Acharya 2025)
- Category: Payment Security
- Harm vectors: Payment vulnerabilities, transaction manipulation
- Target: `summaries/secure-agent-payments-2511.15712.md`

**10. `2605.11781` — Five Attacks on x402 Agentic Payment Protocol** (Li 2026)
- Category: Payment Security / Attacks
- Harm vectors: Payment protocol attacks, transaction forgery
- Target: `summaries/five-attacks-x402-payment-2605.11781.md`

**11. `2606.17698` — EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent** (Du 2026)
- Category: Benchmarks
- Harm vectors: Hidden intent, opaque long-horizon decision chains
- Target: `summaries/ecomagentbench-shopping-agents-2606.17698.md`

**12. `2606.28356` — SafeGEO: Understanding Generative Engine Optimization Risks in Recommendation Agents** (Wen 2026)
- Category: Consumer Protection / GEO
- Harm vectors: Generative engine optimization, search manipulation
- Target: `summaries/safegeo-geo-risks-2606.28356.md`

---

## Batch 2: HIGH PRIORITY — Benchmarks & Evaluation (8 items)

**13. `2506.02839` — DeepShop: A Benchmark for Deep Research Shopping Agents** (Lyu 2025)
- [Already listed in Batch 1A — cross-reference only]

**14. `2508.11416` — AIM-Bench: Evaluating Decision-making Biases** (Zhao 2025)
- [Already listed in Batch 1A — cross-reference only]

**15. `2510.13291` — Higher Satisfaction, Lower Cost: A Technical Report on How LLMs Revolutionize Meituan's Intelligent Interaction Systems** (Cheng 2025)
- Category: Industry Benchmark
- Harm vectors: Scale of consumer impact (Meituan platform)
- Target: `summaries/meituan-llm-interaction-2510.13291.md`

**16. `2511.23366` — Agentic AI Framework for Smart Inventory Replenishment** (Syed 2025)
- Category: Supply Chain / Inventory
- Harm vectors: Inventory manipulation, supply chain opacity
- Target: `summaries/agentic-inventory-replenishment-2511.23366.md`

**17. `2512.03025` — LORE: A Large Generative Model for Search Relevance** (Lu 2025)
- Category: Search / Relevance
- Harm vectors: Search result manipulation
- Target: `summaries/lore-search-relevance-2512.03025.md`

**18. `2512.08868` — EcomBench: Towards Holistic Evaluation of Foundation Agents in E-commerce** (Min 2026)
- Category: Benchmarks
- Harm vectors: Evaluation gaps in agentic commerce
- Target: `summaries/ecombench-foundation-agents-2512.08868.md`

**19. `2605.08334` — CustomerSim: Benchmarking and Aligning Multimodal Language Models as Retail User Simulators** (Pruksachatkun 2025)
- Category: Benchmarks / User Simulation
- Harm vectors: User simulation reliability, alignment gaps
- Target: `summaries/customersim-retail-simulators-2605.08334.md`

**20. `2606.31693` — $\tau$-Rec: A Verifiable Benchmark for Agentic Recommender Systems** (Narasimhan 2025)
- Category: Benchmarks / Verification
- Harm vectors: Verification of recommendation outcomes
- Target: `summaries/tau-rec-verified-recommendation-2606.31693.md`

---

## Batch 3: MEDIUM PRIORITY — E-commerce Infrastructure (20 items)

**21. `2411.10184` — Agentic LLMs in the Supply Chain: Towards Autonomous Multi-Agent Consensus-Seeking** (Jannelli 2024)
- Category: Supply Chain
- Harm vectors: Supply chain transparency, multi-agent coordination
- Target: `summaries/agentic-supply-chain-consensus-2411.10184.md`

**22. `2503.04830` — Cite Before You Speak: Enhancing Context-Response Grounding in E-commerce Conversational LLM-Agents** (Zeng 2025)
- Category: Conversational Agents
- Harm vectors: Misleading claims, lack of citation accountability
- Target: `summaries/cite-before-speak-grounding-2503.04830.md`

**23. `2503.07997` — A Survey of Challenges and Sensing Technologies in Autonomous Retail Systems** (Rukundo 2025)
- Category: Survey / Autonomous Retail
- Harm vectors: Privacy, surveillance in retail
- Target: `summaries/autonomous-retail-sensing-2503.07997.md`

**24. `2503.23303` — SalesRLAgent: A Reinforcement Learning Approach for Real-Time Sales Conversion Prediction and Optimization** (M 2025)
- Category: Sales Optimization
- Harm vectors: Manipulative sales tactics, exploitation of behavioral biases
- Target: `summaries/salesrlagent-conversion-2503.23303.md`

**25. `2504.16902` — Building A Secure Agentic AI Application Leveraging A2A Protocol** (Habler 2025)
- Category: Agent-to-Agent Protocol
- Harm vectors: Agent security, inter-agent trust
- Target: `summaries/secure-agentic-a2a-2504.16902.md`

**26. `2507.02698` — Multi-Agent Reinforcement Learning for Dynamic Pricing in Supply Chains: Benchmarking Strategic Agent Behaviours** (Hazenberg 2025)
- Category: Dynamic Pricing
- Harm vectors: Algorithmic price collusion, predatory pricing
- Target: `summaries/marl-dynamic-pricing-2507.02698.md`

**27. `2507.05788` — Flippi: End To End GenAI Assistant for E-Commerce** (Rajasekar 2025)
- Category: E-commerce Assistant
- Harm vectors: End-to-end automation opacity
- Target: `summaries/flippi-ecommerce-assistant-2507.05788.md`

**28. `2507.13311` — FashionPose: Text to Pose to Relight Image Generation for Personalized Fashion Visualization** (Shi 2025)
- Category: Fashion Tech
- Harm vectors: Misleading product representation
- Target: `summaries/fashionpose-visualization-2507.13311.md`

**29. `2507.18884` — MindFlow+: A Self-Evolving Agent for E-Commerce Customer Service** (Gong 2025)
- Category: Customer Service
- Harm vectors: Automated customer service deception, lack of human recourse
- Target: `summaries/mindflow-customer-service-2507.18884.md`

**30. `2509.03811` — Rethinking Supply Chain Planning: A Generative Paradigm** (Yin 2025)
- Category: Supply Chain Planning
- Harm vectors: Supply chain opacity
- Target: `summaries/generative-supply-chain-2509.03811.md`

**31. `2509.03890` — FaMA: LLM-Empowered Agentic Assistant for Consumer-to-Consumer Marketplace** (Yan 2025)
- Category: C2C Marketplace
- Harm vectors: C2C marketplace manipulation
- Target: `summaries/fama-c2c-marketplace-2509.03890.md`

**32. `2510.17797` — Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics** (Prabhakar 2025)
- Category: Enterprise Research
- Harm vectors: Enterprise decision opacity
- Target: `summaries/enterprise-deep-research-2510.17797.md`

**33. `2511.12133` — AI-Salesman: Towards Reliable Large Language Model Driven Telemarketing** (Zhang 2025)
- Category: Telemarketing
- Harm vectors: Automated telemarketing, consumer harassment
- Target: `summaries/ai-salesman-telemarketing-2511.12133.md`

**34. `2601.20048` — Insight Agents: An LLM-Based Multi-Agent System for Data Insights** (Bai 2026)
- Category: Data Analytics
- Harm vectors: Data interpretation opacity
- Target: `summaries/insight-agents-analytics-2601.20048.md`

**35. `2602.21698` — E-comIQ-ZH: A Human-Aligned Dataset and Benchmark for Fine-Grained Evaluation of E-commerce Posters** (Sun 2026)
- Category: Benchmarks / E-commerce Marketing
- Harm vectors: Marketing deception, misleading product imagery
- Target: `summaries/ecomiq-poster-evaluation-2602.21698.md`

**36. `2603.14864` — Shopping Companion: Benchmarking and Training LLM Agents for Long-Horizon Preference-Grounded E-Commerce Tasks** (Yu 2026)
- Category: Benchmarks / Shopping Agents
- Harm vectors: Long-horizon preference manipulation
- Target: `summaries/shopping-companion-long-horizon-2603.14864.md`

**37. `2604.14051` — Enhancing Local Life Service Recommendation with Agentic Reasoning in Large Language Model** (Cao 2026)
- Category: Local Services
- Harm vectors: Local service recommendation manipulation
- Target: `summaries/local-life-recommendation-2604.14051.md`

**38. `2605.13909` — TERMS-Bench: Diagnosing LLM Negotiation Agents Beyond Deal Rate** (Zhang 2026)
- Category: Benchmarks / Negotiation
- Harm vectors: Negotiation exploitation, unfair deals
- Target: `summaries/terms-bench-negotiation-2605.13909.md`

**39. `2605.14205` — SimPersona: Learning Discrete Buyer Personas from Raw Clickstreams for Grounded E-Commerce Agents** (Foumani 2025)
- Category: User Simulation
- Harm vectors: Persona manipulation, privacy
- Target: `summaries/simpersona-buyer-personas-2605.14205.md`

**40. `2605.18805` — RecoAtlas: From Semantic Plausibility to Set-Level Utility in LLM Recommendation Agents** (Aouali 2025)
- Category: Recommendation Agents
- Harm vectors: Recommendation utility measurement gaps
- Target: `summaries/reco-atlas-recommendation-2605.18805.md`

---

## Batch 4: MEDIUM PRIORITY — Negotiation & Agent Interaction (7 items)

**41. `2509.21501` — LLM Agent Meets Agentic AI: Can LLM Agents Simulate Customers to Evaluate Agentic-AI-based Shopping Assistants?** (Sun 2025)
- Category: Agent Simulation
- Harm vectors: Agent evaluation reliability
- Target: `summaries/llm-agent-simulate-customers-2509.21501.md`

**42. `2510.25779` — Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets** (Bansal 2025)
- Category: Marketplace Simulation
- Harm vectors: Market manipulation research
- Target: `summaries/magentic-marketplace-2510.25779.md`

**43. `2511.23366` — Agentic AI Framework for Smart Inventory Replenishment** (Syed 2025)
- [Already listed in Batch 2 — cross-reference only]

**44. `2605.11781` — Five Attacks on x402 Agentic Payment Protocol** (Li 2026)
- [Already listed in Batch 1A — cross-reference only]

**45. `2606.05671` — QueryAgent-R1: Bridging Query Generation and Product Retrieval for E-Commerce Query Recommendation** (Sun 2026)
- Category: Search / Query Optimization
- Harm vectors: Query manipulation, product retrieval opacity
- Target: `summaries/queryagent-r1-search-2606.05671.md`

**46. `2606.08790` — RAILS: Verification-Native Clearing For Agentic Commerce** (de Valois-Franklin 2026)
- Category: Payment / Verification
- Harm vectors: Payment verification gaps
- Target: `summaries/rails-verification-clearing-2606.08790.md`

**47. `2606.10156` — $\tau$-Rec: A Verifiable Benchmark for Agentic Recommender Systems** (Narasimhan 2025)
- [Already listed in Batch 2 — cross-reference only]

---

## Batch 5: LOW PRIORITY — Industry Reports & Whitepapers (6 items)

These 6 items are the ones that had **URL-based matches** in the wiki. Skip ingestion — they are already cross-referenced.

The 3 items that had **NO match** (URL-based) are:
1. Perplexity — "Shop like a Pro." (`https://perplexity.ai`)
2. Amazon 2025 — "Buy for Me." (`https://www.aboutamazon.com/news/retail/amazon-things-to-buy-help-me-decide-gen-ai`)
3. Alibaba Cloud 2025 — "Intelligent Cockpits..." (`https://www.alibabacloud.com/blog/...`)

**48. Perplexity — Shop like a Pro.**
- Source: `https://perplexity.ai`
- Category: Consumer Product
- Harm vectors: AI-powered shopping assistance opacity
- Target: `summaries/perplexity-shop-assistant-2025.md`

**49. Amazon 2025 — Buy for Me.**
- Source: `https://www.aboutamazon.com/news/retail/amazon-things-to-buy-help-me-decide-gen-ai`
- Category: Consumer Product
- Harm vectors: AI-powered purchasing on Amazon
- Target: `summaries/amazon-buy-for-me-2025.md`

**50. Alibaba Cloud 2025 — Intelligent Cockpits...**
- Source: `https://www.alibabacloud.com/blog/alibaba-unveils-intelligent-cockpits-enterprise-partnerships-and-ai-glasses-at-waic-2025_602409`
- Category: Consumer Product
- Harm vectors: AI glasses, enterprise AI integration
- Target: `summaries/alibaba-intelligent-cockpits-2025.md`

---

## Batch 6: LOW PRIORITY — Product/Platform Launches (6 items)

The 30 URLs that had **URL-based matches** in the wiki. Skip ingestion — they are already cross-referenced.

The remaining 3 product/platform items that had **NO match**:
1. Amazon "Help Me Decide" (`https://www.aboutamazon.com/news/retail/amazon-things-to-buy-help-me-decide-gen-ai`)
2. Amazon "Buy for Me" (`https://www.aboutamazon.com/news/retail/amazon-shopping-app-buy-for-me-brands`)
3. Amazon Robotics fulfillment (`https://www.aboutamazon.com/news/operations/amazon-robotics-robots-fulfillment-center`)

**51. Amazon — Help Me Decide: AI-powered product comparison**
- Source: `https://www.aboutamazon.com/news/retail/amazon-things-to-buy-help-me-decide-gen-ai`
- Category: Product Launch
- Target: `summaries/amazon-help-me-decide-2025.md`

**52. Amazon — Buy for Me: AI-powered shopping**
- Source: `https://www.aboutamazon.com/news/retail/amazon-shopping-app-buy-for-me-brands`
- Category: Product Launch
- Target: `summaries/amazon-buy-for-me-2025.md`

**53. Amazon — Things to Buy: Gen AI-powered shopping**
- Source: `https://www.aboutamazon.com/news/retail/amazon-things-to-buy-help-me-decide-gen-ai`
- Category: Product Launch
- Target: `summaries/amazon-things-to-buy-2025.md`

---

## Batch 7: LOW PRIORITY — Robotics & Embodied Commerce (8 items)

These are papers on physical retail robots, logistics, and embodied AI. Lower direct consumer harm relevance but worth documenting for completeness.

**54. `2307.15818` — RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** (Brohan 2023)
- Category: Robotics / Vision-Language
- Harm vectors: Physical retail automation opacity
- Target: `summaries/rt2-vision-language-robotics-2307.15818.md`

**55. `2307.16644` — NEON: Living Needs Prediction System in Meituan** (Lan 2023)
- Category: Robotics / Prediction
- Harm vectors: Consumer behavior prediction
- Target: `summaries/neon-living-needs-prediction-2307.16644.md`

**56. `2308.16505` — Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations** (Huang 2023)
- Category: Recommendation / LLM
- Harm vectors: Interactive recommendation opacity
- Target: `summaries/recommender-ai-agent-2308.16505.md`

**57. `2312.06677` — Intelligent Virtual Assistants with LLM-based Process Automation** (Guan 2023)
- Category: Virtual Assistants
- Harm vectors: Automated customer service deception
- Target: `summaries/intelligent-virtual-assistants-2312.06677.md`

**58. `2403.12965` — Wear-Any-Way: Manipulable Virtual Try-on via Sparse Correspondence Alignment** (Chen 2024)
- Category: Virtual Try-on
- Harm vectors: Misleading product representation
- Target: `summaries/wear-any-way-virtual-tryon-2403.12965.md`

**59. `2404.09911` — ChatShop: Interactive Information Seeking with Language Agents** (Chen 2024)
- Category: Information Seeking
- Harm vectors: Misleading information retrieval
- Target: `summaries/chatshop-interactive-2404.09911.md`

**60. `2409.08069` — TravelAgent: An AI Assistant for Personalized Travel Planning** (Chen 2024)
- Category: Travel Agents
- Harm vectors: Travel booking manipulation
- Target: `summaries/travelagent-personalized-2409.08069.md`

**61. `2501.06243` — Agent TCP/IP: An Agent-to-Agent Transaction System** (Muttoni 2025)
- Category: Agent Protocol
- Harm vectors: Inter-agent transaction security
- Target: `summaries/agent-tcp-ip-transaction-2501.06243.md`

---

## Batch 8: LOW PRIORITY — Cross-Cutting Infrastructure (28 items)

These are papers on general agent infrastructure, payments, benchmarks, and cross-cutting topics that don't fit cleanly into other categories.

**62. `2503.23303` — SalesRLAgent: A Reinforcement Learning Approach for Real-Time Sales Conversion** (M 2025)
- [Already listed in Batch 3 — cross-reference only]

**63. `2506.07982` — $\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment** (Barres 2025)
- Category: Benchmarks / Conversational
- Harm vectors: Conversational agent evaluation gaps
- Target: `summaries/tau2-bench-conversational-2506.07982.md`

**64. `2506.17765` — CARTS: Collaborative Agents for Recommendation Textual Summarization** (Chen 2025)
- [Already listed in Batch 1A — cross-reference only]

**65. `2507.02698` — Multi-Agent RL for Dynamic Pricing** (Hazenberg 2025)
- [Already listed in Batch 3 — cross-reference only]

**66. `2507.18884` — MindFlow+: Self-Evolving Agent for E-Commerce Customer Service** (Gong 2025)
- [Already listed in Batch 3 — cross-reference only]

**67. `2509.21842` — DeepTravel: An End-to-End Agentic Reinforcement Learning Framework for Autonomous Travel Planning Agents** (Ning 2025)
- Category: Travel Agents
- Harm vectors: Automated travel planning manipulation
- Target: `summaries/deeptravel-autonomous-2509.21842.md`

**68. `2509.26490` — VitaBench: Benchmarking LLM Agents with Versatile Interactive Tasks in Real-world Applications** (He 2025)
- Category: Benchmarks
- Harm vectors: Real-world agent evaluation gaps
- Target: `summaries/vitabench-interactive-tasks-2509.26490.md`

**69. `2510.20567` — Beyond Retrieval-Ranking: Multi-Agent Cognitive Decision Framework for E-Commerce Search** (Zhai 2025)
- [Already listed in Batch 1A — cross-reference only]

**70. `2511.12133` — AI-Salesman: Towards Reliable LLM Driven Telemarketing** (Zhang 2025)
- [Already listed in Batch 3 — cross-reference only]

**71. `2511.15712` — Secure Autonomous Agent Payments** (Acharya 2025)
- [Already listed in Batch 1A — cross-reference only]

**72. `2512.03025` — LORE: A Large Generative Model for Search Relevance** (Lu 2025)
- [Already listed in Batch 2 — cross-reference only]

**73. `2601.20048` — Insight Agents: LLM-Based Multi-Agent System for Data Insights** (Bai 2026)
- [Already listed in Batch 3 — cross-reference only]

**74. `2602.21698` — E-comIQ-ZH: Human-Aligned Dataset for E-commerce Posters** (Sun 2026)
- [Already listed in Batch 2 — cross-reference only]

**75. `2603.14864` — Shopping Companion: Benchmarking LLM Agents for Long-Horizon Tasks** (Yu 2026)
- [Already listed in Batch 3 — cross-reference only]

**76. `2604.14051` — Enhancing Local Life Service Recommendation** (Cao 2026)
- [Already listed in Batch 3 — cross-reference only]

**77. `2605.08334` — CustomerSim: Benchmarking Retail User Simulators** (Pruksachatkun 2025)
- [Already listed in Batch 2 — cross-reference only]

**78. `2605.11781` — Five Attacks on x402 Payment Protocol** (Li 2026)
- [Already listed in Batch 1A — cross-reference only]

**79. `2605.13909` — TERMS-Bench: Diagnosing LLM Negotiation Agents** (Zhang 2026)
- [Already listed in Batch 4 — cross-reference only]

**80. `2605.14205` — SimPersona: Learning Buyer Personas from Clickstreams** (Foumani 2025)
- [Already listed in Batch 3 — cross-reference only]

**81. `2605.18805` — RecoAtlas: Semantic Plausibility to Set-Level Utility in Recommendation** (Aouali 2025)
- [Already listed in Batch 3 — cross-reference only]

**82. `2606.05671` — QueryAgent-R1: Bridging Query Generation and Product Retrieval** (Sun 2026)
- [Already listed in Batch 4 — cross-reference only]

**83. `2606.08790` — RAILS: Verification-Native Clearing For Agentic Commerce** (de Valois-Franklin 2026)
- [Already listed in Batch 4 — cross-reference only]

**84. `2606.10156` — $\tau$-Rec: Verifiable Benchmark for Agentic Recommender Systems** (Narasimhan 2025)
- [Already listed in Batch 2 — cross-reference only]

**85. `2606.12924` — Iterating Toward Better Search: Two-Agent Simulation Framework for Agentic Search Architectures** (Duraj 2026)
- Category: Search Architecture
- Harm vectors: Search architecture transparency
- Target: `summaries/two-agent-search-2606.12924.md`

**86. `2606.17698` — EComAgentBench: Benchmarking Shopping Agents** (Du 2026)
- [Already listed in Batch 1A — cross-reference only]

**87. `2606.28356` — SafeGEO: Understanding Generative Engine Optimization Risks** (Wen 2026)
- [Already listed in Batch 1A — cross-reference only]

---

## Execution Summary

**Total unique items to ingest:** 87
**Already in wiki (cross-reference only):** ~14 items
**New pages to create:** 73

### Files to create:
- `summaries/*.md` — 73 new summary pages (actually created 152 total with existing + new)

### Files to update:
- `index.md` — Add 73 new entries to Summaries section, update counts
- `log.md` — Append ingestion record with full cross-references

### Schema compliance checklist for each new page:
- [x] YAML frontmatter with: `title`, `type`, `date`, `source_url`, `authors`, `tags`
- [x] Type: `summary` (for research papers), `product` (for industry reports)
- [x] Consumer harm vectors documented in body
- [x] Cross-references: `[[]]` wikilinks to existing wiki entities
- [x] Source traceability: full arXiv/URL in frontmatter and body

---

## Completion Status: ✅ COMPLETE

All batches ingested. Final wiki state: 152 summary files.

### Batches completed:
- ✅ Batch 1A (12 items) — HIGH PRIORITY consumer harm/safety papers
- ✅ Batch 2 (5 items) — HIGH PRIORITY benchmarks
- ✅ Batch 3 (20 items) — MEDIUM PRIORITY e-commerce infrastructure
  - 10 plan IDs verified as e-commerce, 10 bad IDs replaced with verified papers from awesome-agentic-commerce repo
  - 10 bad IDs rejected (resolved to particle physics, quantum computing, pure math, bicycle-sharing)
- ✅ Batch 4 (7 items with cross-refs) — MEDIUM PRIORITY negotiation/interaction
- ✅ Batch 5 (3 items) — LOW PRIORITY industry reports / URL-based
- ✅ Batch 6 (3 items) — LOW PRIORITY product launches (consolidated into Amazon AI shopping suite)
- ✅ Batch 7 (8 items) — LOW PRIORITY robotics & embodied commerce
- ✅ Batch 8 (28 items, mostly cross-refs) — LOW PRIORITY cross-cutting infrastructure

### Corrections made during ingestion:
- Batch 2: ID 2606.31693 resolved to ShopX (not τ-Rec); τ-Rec created from correct ID 2606.10156
- Batch 3: 10 IDs from plan resolved to non-e-commerce content; replaced with verified e-commerce papers from awesome-agentic-commerce GitHub repo
- Batch 4: ID 2506.18805 was a typo (math paper); correct RecoAtlas ID is 2605.18805

### Sources used:
- awesome-agentic-commerce GitHub repo (https://github.com/yifeizhangcs/awesome-agentic-commerce) — authoritative ID verification
- arXiv API for paper metadata
- Web extraction for URL-based content

---

## Recommended Execution Order

1. **Batch 1A** (12 items) — HIGH PRIORITY consumer harm/safety papers
2. **Batch 2** (5 new items) — HIGH PRIORITY benchmarks
3. **Batch 3** (20 items) — MEDIUM PRIORITY e-commerce infrastructure
4. **Batch 4** (2 new items) — MEDIUM PRIORITY negotiation/interaction
5. **Batch 5-8** (6 items) — LOW PRIORITY industry reports, products, robotics, infrastructure
6. **Post-ingest verification** — Check all `[[]]` wikilinks resolve
7. **Update index.md** — Add entries, recalculate counts
8. **Update log.md** — Full ingestion record
