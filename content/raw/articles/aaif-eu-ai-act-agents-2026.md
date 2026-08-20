---
title: "The EU AI Act and the New Rules for Building AI Agents"
type: raw
source_url: https://aaif.io/blog/the-eu-ai-act-and-the-new-rules-for-building-ai-agents
ingested: 2026-08-19
tags: [regulation, eu-ai-act, ai-agents, corporate-accountability]
---

# The EU AI Act and the New Rules for Building AI Agents

Source: https://aaif.io/blog/the-eu-ai-act-and-the-new-rules-for-building-ai-agents
Author: Angie Jones (VP, Agentic AI Foundation)
Published: August 2, 2026
Tags: EU AI Act, Regulatory Compliance, AI Agents, Governance

## TL;DR

The EU AI Act applies separate rules to general models and to the agent systems built with them. The duties for an agent system depend on its intended use. A company using a compliant foundation model can still have its own duties as the provider or deployer of an agent. Teams should map the agent's actions and access, then make its controls and records part of the production system.

## Start with the agent's job

While the AI Act distinguishes between general AI models and the AI systems built with them, it does not create a separate legal category for AI agents. Its definition of an AI system is broad enough to include systems that operate with different levels of autonomy and produce decisions or content that affect digital or physical environments.

Begin by writing down the agent's intended job. Record who will use it, who could be affected, what data it can access, what actions it can take, and where its outputs will be used. Legal and engineering teams can use that description to check for prohibited uses and classify the agent's risk. They can then identify any transparency or data protection duties.

### Check agent's level of risk

It's worth noting that using a powerful model does not make the agent high risk on its own. The level of risk depends on what the agent does and where it is used. An agent that summarizes internal documents may have few duties under the AI Act, while one that screens job applicants or decides whether someone can receive an essential service may be high risk.

And the classification can change when the agent's job changes. For example, connecting a document summarizer to hiring records and asking it to rank applicants creates a different use case. Teams should review the classification whenever they change the agent's purpose, data access, tools, or affected users.

### Check where the output will be used

The rules can also apply to companies outside Europe. Under the Act's scope rules, a provider or deployer can be within scope when its system's output is used in the European Union, even if the company is based elsewhere. When documenting the agent's job, include where its output will be used.

### Check for prohibited uses

Determine whether the agent's intended use is prohibited. Prohibited uses include certain forms of harmful manipulation and social scoring. It also covers emotion recognition in workplaces or schools, with limited exceptions. Companies should check the prohibited list before spending time on any other classification work.

### Tell people when they are interacting with AI

Agents that interact with customers also have a transparency requirement. From August 2, 2026, a provider must design an interactive AI system so people know when they are talking to AI, unless the interaction is already obvious.

The European Commission's Article 50 guidance names AI agents and chatbots as examples. It also includes AI avatars, such as digital people that speak and respond to users. In each case, the notice must appear at the start of the first interaction.

An agent that only talks to another machine falls outside the direct interaction rule. However, the exception only applies to that notice. Other requirements may still apply if the agent is used for a high risk purpose, processes personal data, or generates content covered by Article 50's marking rules.

## Separate the model from the agent

Many companies will use a model from another provider and add instructions, memory, business data, tools, etc. The AI Act treats the general model and the finished system as different parts of the value chain.

Several leading model providers now publish compliance material. OpenAI, Anthropic, Google, Microsoft, Amazon, Mistral, and Cohere have signed the EU's voluntary General Purpose AI Code of Practice. The code gives model providers a common way to address documentation and copyright duties. Providers of the most capable models also use it to address safety and security duties.

A model provider's compliance work does not cover the downstream company's agent. A company that develops an agent and puts it into service under its own name may be the provider of the agent system. A company that uses an agent under its authority is normally a deployer. And a deployer can become a provider when it substantially changes a high risk system or changes the system's purpose so it becomes high risk.

The distinction affects contracts as well as technical work. Agent builders need enough information from model and tool providers to test the full system. For high risk systems, the Act's value chain rules require written agreements that address the information and technical help the system provider needs for compliance.

## Build the evidence into production

Agentic systems create a hard record keeping problem because the important event is often an action rather than an answer. A useful record needs to show what the agent requested and what actually happened. It should also identify the model and policy version that were active at the time.

For high risk systems, Article 12 requires automatic logging that supports traceability during the system's lifetime. Deployers must generally keep the logs under their control for at least six months under Article 26. Providers also need risk management and post market monitoring processes.

Teams can support these requirements by building the necessary evidence into the production system from the start and combining technical controls with ongoing governance.

* Map each agent. Record its intended purpose, owner, model, data access, tools, and affected people. Include agents that teams installed without a central purchasing process.
* Limit what it can do. Give the agent only the credentials it needs. Require human approval before an action that could affect a person's rights, money, employment, or access to a service.
* Keep useful records. Record tool requests and results. Keep the active model and policy version with the record, and protect records from later changes.
* Review every material change. Recheck the risk classification when a team changes the model, system instructions, tools, permissions, or intended users.

### Make the controls portable with open standards

Open standards can make the same controls work across more than one model or agent framework. A shared record format can preserve the evidence when a company changes vendors, and a shared identity method can help a tool determine which agent is making a request and which organization is responsible for it.

Following an open specification does not automatically prove legal compliance, but open specifications can still reduce duplicate work and give auditors a consistent record to examine.

Builders can bring these production requirements to the Agentic AI Foundation's Governance, Risk & Regulatory Alignment Working Group, which is examining how open standards can support agent governance and regulatory alignment.

## Use the extra time to prepare

The EU changed the schedule shortly before the main August 2026 deadline. The Digital Omnibus on AI moved the rules for standalone high risk systems to December 2, 2027. Rules for high risk AI in regulated products now apply on August 2, 2028.

The delay does not cover the main transparency requirements. Interactive AI disclosure and many rules for AI generated content apply on August 2, 2026. Providers of some generative systems that were already on the market receive until December 2, 2026 to add the required machine readable marks to outputs.

Companies should use the longer high risk schedule to build the system records and controls now. The work takes time because it crosses product, engineering, legal, and security teams. It also depends on vendor contracts and on decisions about who has authority to stop an agent.

## Conference sessions (AGNTCon and MCPCon Europe, Sep 17-18, Amsterdam)

* Legal Implications Under EU Law When Deploying AI Agents — Mirela Takacs
* Six Months of Proof, Independently Verifiable Records for Agent Actions Under the EU AI Act — Steven Mih (Agent Action Capsule project)
* Governance You Can Run, Checkable Properties for Production Agents — Seshu Tolety and Ayush Bhardwaj (Siemens), maps checks to EU AI Act and ISO/IEC 42001 with GDPR controls

***This article provides general information and is not legal advice.***
