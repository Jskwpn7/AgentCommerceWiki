---
source_url: https://agenticplug.ai/current-state-of-agentic-commerce
ingested: 2026-06-26
tags: [agentic-ai, digital-platforms, retail]
---

# State of Agentic Commerce: Protocol Tracker 2026

Agentic commerce operates on two distinct layers: the commerce protocols (transactions) and the agent infrastructure protocols (agent capabilities).

## Commerce Protocols (Transaction Layer)
- **Universal Commerce Protocol (UCP):** An open standard for agentic commerce with a layered architecture (Services → Capabilities → Extensions → Transport). Designed to solve fragmentation.
- **Agent Payments Protocol (AP2):** Handles agent-led payments. Donated to the FIDO Alliance in April 2026. Includes "Human-Not-Present" support (v0.2).
- **Machine Payments Protocol (MPP):** Specifically for machine-to-machine (M2M) agent payments. Includes a Visa Card-Based MPP spec & SDK (March 2026) that extends MPP to existing card rails.
- **x402 Protocol:** Based on the HTTP 402 (Payment Required) status code. When a resource is requested, the server responds with a 402 and a price; the agent then resends the request with payment included.
- **Agentic Commerce Protocol (ACP):** OpenAI's protocol for agent-led commerce.

## Infrastructure Protocols
- **Model Context Protocol (MCP):** While primarily for tool/data access, it is used as a foundation for agents to interact with endpoints that may eventually trigger commerce flows.

## Market Projection
Bain forecasts that 10–25% of U.S. e-commerce could be agentic by 2030.

## Notes
The proliferation of competing protocols (UCP vs ACP vs x402) suggests a fragmented early market. The "Human-Not-Present" support in AP2 is a critical technical shift toward full autonomy.
