# From Craft to Constitution: A Governance-First Paradigm for Principled Agent Engineering

**arXiv:2510.13857v1 [cs.SE]** — 12 Oct 2025

## Authors

Qiang Xu, Xiangyu Wen, Changran Xu, Zeju Li, Jianyuan Zhong

## Abstract

The advent of powerful Large Language Models (LLMs) has ushered in an "Age of the Agent," enabling autonomous systems to tackle complex goals. However, the transition from prototype to production is hindered by a pervasive "crisis of craft," resulting in agents that are brittle, unpredictable, and ultimately untrustworthy in mission-critical applications. This paper argues this crisis stems from a fundamental paradigm mismatch—attempting to command inherently probabilistic processors with the deterministic mental models of traditional software engineering. To solve this crisis, we introduce a governance-first paradigm for principled agent engineering, embodied in a formal architecture we call ArbiterOS.

This paradigm provides control by introducing the Agentic Computer, a mental model that reframes the LLM as a "Probabilistic CPU." A neuro-symbolic Hardware Abstraction Layer (HAL) that decouples durable agent logic from the underlying model manages this volatile hardware, which is governed by the formal Agent Constitution Framework (ACF) instruction set and continuously verified by the rigorous Evaluation-Driven Development Lifecycle (EDLC).

Ultimately, ArbiterOS provides a coherent blueprint to move beyond the craft of prompting and begin the discipline of principled agent engineering. Through its governance-first architecture, it provides the foundations for building agents that are not only reliable, auditable, and secure, but also portable, compliant by design, and organizationally scalable—transforming fragile prototypes into robust, production-ready systems.

## Key Concepts

### The "Crisis of Craft"

The paper documents a systemic engineering problem: even state-of-the-art models (Gemini-2.5-Pro, GPT-4o) achieved only 30% success rate on consequential real-world tasks like trip planning and online shopping. The failure manifests as:
- **Brittleness**: agents shatter when faced with slight variations from their training data
- **Unpredictability**: non-deterministic behaviors that turn debugging into guesswork
- **Unmaintainability**: formal safety guarantees impossible; regulatory compliance becomes speculation
- **Insecurity**: exposure to prompt injection and poorly understood attack surfaces

The root cause: reliance on natural language as the primary programming interface introduces ambiguity and instability absent in formal programming languages, leading to "prompt drift" where minor prompt changes cause catastrophic failures.

### Three Pillars of ArbiterOS

**1. Mental Model — The Agentic Computer**

Reframes the LLM as a "Probabilistic CPU" — inherently non-deterministic hardware. This allows reasoning about agent reliability as a systems management problem, applying classical computer architecture principles to probabilistic computation.

**2. Formal Architecture — ArbiterOS (Neuro-Symbolic OS)**

A kernel-based architecture with three key components:

- **Symbolic Governor (Kernel)**: A deterministic symbolic layer that acts as the system's trusted OS kernel, providing fine-grained intra-agent governance — imposing rules and safety checks directly on the agent's workflow. This establishes a "Kernel-as-Governor" paradigm, distinct from the "Kernel-as-Scheduler" approach of broader AIOS frameworks.

- **Hardware Abstraction Layer (HAL)**: A universal adapter for the volatile LLM. Decouples the agent's core logic from the specific, ever-changing details of the underlying model, ensuring portability and maintainability.

- **Agent Constitution Framework (ACF)**: A formal instruction set architecture (ISA) for governance. Provides a clear, machine-readable rulebook that the Governor uses to enforce reliability and safety policies.

**3. Rigorous Discipline — EDLC (Evaluation-Driven Development Lifecycle)**

A cyclical discipline centered on improving agent performance against version-controlled benchmarks. Transforms reliability from a vague aspiration into a measurable, data-driven engineering goal.

### Comparison with Existing Frameworks

The paper positions ArbiterOS against:
- **LangChain/LangGraph**: Lacks explicit governance mechanism; relies on developer to correctly apply governance nodes
- **OpenAI AgentKit**: Enforcement is a configurable part of the workflow, not a separate guaranteed architectural layer
- **Microsoft Agent Framework**: Lacks a formal governance ISA; governance implemented via code/middleware
- **Google Gemini/ADK**: Governance not enforced by a distinct kernel

All existing frameworks address the "how" of execution but not the "what" of guaranteed, reliable behavior.

### Future Frontiers

The paper identifies three directions for extending the ACF:
1. Overcoming the machine bottleneck via automated optimization
2. Overcoming the human bottleneck via an automated evaluation lifecycle
3. Extending the ACF for the "era of experience" — enabling autonomous agents to learn safely and continually from experience

## Tags

tags: [academic, agentic-ai]

## Notes

- This is a systems/architecture paper in computer science (cs.SE), not consumer research. It provides engineering foundations for building reliable agents but does not discuss consumer harm, regulation, or UK markets.
- The "probabilistic CPU" mental model and HAL abstraction are novel contributions that could influence how future agent systems are designed.
- The paper references Wang et al. 2024 benchmark (30% success rate on real-world tasks) — this empirical data point is independently useful for wiki entries discussing agent reliability gaps.
- Cross-references: The governance-first philosophy has indirect implications for [[ai-agents-in-markets]] (governance gaps could enable harmful agent behavior) and [[systemic-fragility-in-ai-economies]] (governance failures as systemic risk).
- The paper was published October 2025, making it an early contribution to the agent governance space.
