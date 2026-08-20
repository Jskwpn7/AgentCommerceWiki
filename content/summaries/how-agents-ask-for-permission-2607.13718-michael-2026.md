---
title: "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement"
type: summary
created: 2026-08-15
updated: 2026-08-15
tags:
  - agentic-ai
  - digital-consumer
  - data-abuse
  - corporate-accountability
  - digital-platforms
  - financial-services
  - academic
  - cross-sector
sources:
  - url: https://arxiv.org/abs/2607.13718
    title: "How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement"
    date: 2026-07-15
  - url: raw/papers/how-agents-ask-for-permission-2607.13718-michael-2026.md
    title: "Raw full-text extraction (arXiv 2607.13718v1 HTML)"
    date: 2026-08-15
confidence: high
sectors:
  - financial-services
  - digital-platforms
concepts:
  - [[consumer-autonomy]]
  - [[agentic-commerce-research-2026]]
  - [[conflict-of-interest-in-llm-deployment]]
---

# How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement

## Paper Details

| Field | Value |
|-------|-------|
| Authors | Alexandra E. Michael, Franziska Roesner |
| arXiv | [2607.13718](https://arxiv.org/abs/2607.13718) (v1 published 2026-07-15; v2 follows) |
| Categories | cs.CR, cs.AI |
| Length | 15 pages, 4 figures |
| Method | Literature survey (21 agent-permissions systems/proposals, 2024–2026) + walkthrough-style evaluation of 5 commercial agents (Claude, Claude Cowork, ChatGPT chat mode, ChatGPT agent mode, Codex), conducted late May–early June 2026 using Sonnet 4.6, GPT-5.5, GPT-5.4-Mini |
| Raw extraction | [[raw/papers/how-agents-ask-for-permission-2607.13718-michael-2026]] |

## Summary

The paper addresses a gap in the agentic security literature: most work targets *product-level* permissions (one security policy applied to all users), but user needs differ, so systems must support *user-level* permissions policies. The authors survey 21 recent proposals, build a taxonomy spanning (1) threat models, (2) how policies are specified at the user interface, (3) internal policy specifications, (4) derivation of internal policies from user input, and (5) run-time enforcement. They then apply the taxonomy to five commercial agents to compare research prototypes with deployed products.

The literature clusters around three goals — near-zero user overhead, formally grounded specifications, and deterministic enforcement — but **none of the 21 systems achieves all three**. Commercial agents fail even more badly: they force users into a binary between high-overhead user-in-the-loop approval of every action and opaque LLM auto-reviewers the user cannot see, control, or disable. The one theme commercial agents do pursue — *continuous user control* over policies (updating/revoking later) — is mostly absent from the literature.

## Key Findings

### 1. Literature taxonomy and the "three goals, no full achiever" result

- 12 of 21 literature systems emphasise low user overhead (natural-language policies or implicit-context prediction); 11 provide formally grounded specifications (information-flow control labels, typed DSLs, Datalog, linear temporal logic, ILP-based minimisation); 12 provide deterministic enforcement (non-AI automated detection or user-in-the-loop). No system combines all three.
- 11 of 21 use formal specification, but **none verifies its enforcement** — even where formal security analyses of the architecture exist, the implemented enforcement code remains unverified.
- Threat-model diversity is thin: nearly all systems model the adversary as a benign-but-fallible agent (prompt injection / hallucination) targeting "task flow" (data + control flow combined, since in LLMs instructions are data). Only one system (GAAP) treats the *agent provider* as a possible adversary; none targets denial-of-service, data poisoning, or malicious consumption of the user's funds/tokens.

### 2. Commercial agents: high overhead, low transparency

- **User-in-the-loop by default, everywhere.** Claude, Claude Cowork, ChatGPT chat mode, and Codex all required real-time user approval at least some of the time. ChatGPT chat mode required explicit approval for *every* action associated with a permissions policy, with no way to turn that off or pre-authorise.
- **ChatGPT agent mode silently bypasses permissions.** Granting the LLM control of a remote browser, ChatGPT took actions there (e.g., accessing Gmail) that require user-in-the-loop approval locally — simply by attaching no permissions policies to the remote browser at all, removing any opportunity to approve *or* deny.
- **Claude's undisclosed LLM auto-reviewer.** Under the "Needs approval" setting, Claude sometimes *automatically* inferred permission from the user's message — e.g., it autonomously approved creating an email draft and tagged the MCP call `approvalRequired: false`, and consistently used the Gmail `search_emails` tool without asking. This auto-review is **implicit**: it is not exposed in permissions settings and cannot be disabled short of revoking the tool entirely. The authors disclosed this to Anthropic on 2026-07-02 (response pending at time of writing). This is distinct from Claude Code's user-controlled "auto mode" — and from Claude Code's `bypassPermissions` ("YOLO") mode, which has no auto-reviewer at all.
- **Irrevocable permissions in Claude Cowork.** Once a permission (e.g., read/delete a folder) is granted, it *cannot be revoked* from the app; older sessions persist in history and retain their permissions. Permanent revocation requires the OS (where supported — Windows does not provide it) or uninstalling.
- **Codex is the most transparent** of the five: its LLM auto-review is an explicit setting, off by default, but when enabled it applies to all tools in the session with no per-tool granularity.
- **ChatGPT's LLM guardrails over-restrict.** When asked to send an email mimicking a prompt-injection format, ChatGPT's safety layer blocked the (user-intended) task — illustrating that commercial agents limit *actual* user control even while defaulting to an *appearance* of user-in-the-loop control.

### 3. The net effect (author's framing)

> "Many commercial agents require users to either manually approve every action, or give up substantial portions of their control and autonomy in deciding permissions policies."

Constant approval prompts create **privacy fatigue** — a well-documented driver of users ignoring warnings and over-granting permissions. Opaque LLM auto-review removes transparency and accountability. Neither option preserves meaningful user control.

### 4. Identified research gaps

1. **Unification** — no system delivers low overhead + formal specification + deterministic enforcement together (AC4A and Prudentia come closest).
2. **Formally verified enforcement** — none exists; verification of the (small) enforcement code would give outsized guarantees over the whole agent.
3. **Continuous user control** — only 6 of 21 literature systems let users update/revoke policies after specification; two of those only between sessions; two update from run-time decisions without letting users revert them.
4. **Threat-model diversity** — adversarial users in multi-user/multi-agent settings, the agent provider itself, and non-privacy targets (fund consumption, poisoning) are unexplored.

## Relevance to UK Consumer Harms

- **Unauthorized agent transactions are the core harm.** The paper's motivating example — an agent performing bank transactions without user intent or authorization — is exactly the "agency harm" category flagged in the [[agentic-commerce-monitor-2026-07-16]] digest (rated Very High). Under UK law, consumers face direct financial loss when an agent commits them to payments they did not intend.
- **CMA "business is responsible for what an AI agent does".** The CMA's March 2026 guidance (complying with consumer law when using AI agents) and July 2026 discussion paper place responsibility on the deploying business. Undisclosed auto-review (Claude) and silent permission bypass (ChatGPT agent mode) mean the business — and ultimately the consumer, through lack of redress — bears the consequences of enforcement mechanisms the user cannot see. See [[cma-ai-and-consumer-markets-2026]].
- **DMCCA 2024 and transparency.** Opaque enforcement decisions — including a "Needs approval" setting that does not actually require approval — implicate the transparency and unfair-commercial-practice obligations the DMCCA entrenches (see [[the-dmcca]]). A setting that *promises* user-in-the-loop control while silently auto-approving is a candidate misleading action.
- **Irrevocable permissions vs. withdrawal of consent.** Claude Cowork's non-revocable file permissions mirror consent-withdrawal problems under UK data-protection and consumer law: a permission granted in one session persists and cannot be undone. This is directly relevant to the [[drcf-call-for-input-ai-phase-2]] consultation (closes 2 Sept 2026) on consumer protection tools for AI.
- **Privacy fatigue as a choice-architecture harm.** The paper's user-in-the-loop findings show how per-action approval pop-ups push consumers toward over-granting — a dark-pattern-adjacent dynamic in [[dark-pattern]] territory, and an erosion mechanism for [[consumer-autonomy]] alongside choice-engine compression and nudge sensitivity.
- **Agent liability.** When an auto-reviewer — not the user — decides a transaction is permitted, and the product's settings cannot express the user's actual intent, the liability chain (consumer → agent provider → merchant) becomes harder to resolve. See [[agent-liability]].

## Connection to Other Wiki Entries

- [[consumer-autonomy]] — adds a fifth erosion mechanism: the *permissions UX gap* (opaque auto-review, non-revocable grants, approval fatigue) degrades the control the user formally retains.
- [[agentic-commerce-research-2026]] — fills part of the "agent identity & attribution / enforcement transparency" gap; evidence base for the permissions theme.
- [[conflict-of-interest-in-llm-deployment]] — the LLM auto-reviewer is a provider-side decision layer with no user visibility: the same transparency failure as undisclosed sponsored steering, applied to enforcement rather than recommendation.
- [[ai-shopping-agents]] — the five agents evaluated are the frontier consumer-facing agent products whose purchase behaviour is the subject of most wiki harm analyses.
- [[nist-nccoe-2026-agent-identity-authorization]] — NIST's parallel work on agent identity/authorization requires that "consent mechanisms preserve meaningful user consent and allow users to revoke agent permissions"; this paper documents that deployed agents do not meet that bar.
- [[ai-agent-act-warner-2026]] — Warner's proposed fiduciary duties for custodial user agents would directly bind the permission-handling behaviour documented here.
- [[consumer-harm-agentic-commerce-report]] — the report's harm taxonomy classifies the findings in this paper as *empirically documented* (walkthrough evidence on live commercial products).
- [[agentic-commerce-monitor-2026-07-16]] — discovery origin: item #4, flagged "Very High" harm priority, now ingested in full.
