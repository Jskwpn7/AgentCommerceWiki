---
title: "Lessons from Building Claude Code: How We Use Skills"

created: 2026-06-10
updated: 2026-06-10
type: summary
tags: [agentic-ai]
sources: [raw/articles/lessons-from-building-claude-code-skills-shihipar-2026.md]
confidence: high
---

# Lessons from Building Claude Code: How We Use Skills

## Paper Details

- **Author:** Thariq Shihipar
- **Published:** March 18, 2026
- **Source:** [LinkedIn Pulse](https://www.linkedin.com/pulse/lessons-from-building-claude-code-how-we-use-skills-thariq-shihipar-iclmc) / [X Thread](https://x.com/trq212/status/2033949937936085378)
- **Type:** Engineering guide / practical lessons
- **Engagement:** 6.9M views on X thread, ~16K likes

## Summary

Thariq Shihipar shares Anthropic's hands-on experience building and managing skills for Claude Code, covering the 9 categories of skills they've identified in practice and practical tips for creation, organization, and distribution.

The article catalogs hundreds of Anthropic's own skills into a taxonomy, then distills patterns and best practices for making skills effective and maintainable.

## Key Findings / Arguments

### 9 Categories of Claude Code Skills

1. **Library & API Reference** — Explaining correct usage of libraries/CLIs/SDKs, with reference code snippets and gotcha lists (e.g., internal billing library with edge cases)
2. **Product Verification** — How to test and verify code output, often paired with tools like Playwright or tmux; "can be worth having an engineer spend a week just making your verification skills excellent"
3. **Data Fetching & Analysis** — Connecting agents to data/monitoring stacks with credentials, dashboard IDs, and workflow instructions
4. **Business Process & Team Automation** — Automating repetitive workflows into single commands; uses log files for consistency across runs
5. **Code Scaffolding & Templates** — Generating framework boilerplate with natural-language requirements baked in
6. **Code Quality & Review** — Enforcing org-level standards via deterministic scripts; can run automatically in hooks or GitHub Actions
7. **CI/CD & Deployment** — Fetching, pushing, and deploying code; may reference other skills to collect data
8. **Runbooks** — Taking a symptom (Slack alert, error signature) and walking through multi-tool investigation to produce structured reports
9. **Infrastructure Operations** — Routine maintenance with guardrails for destructive actions (orphan cleanup, dependency management, cost investigation)

### Key Engineering Patterns

- **Gotchas are highest-signal content** — Built up from common failure points over time, not from first principles
- **File system as context engineering** — Skills are folders, not just markdown; progressive disclosure via `references/`, `assets/`, `scripts/` subdirectories
- **Avoid railroading** — Skills should provide information with flexibility, not over-specified instructions
- **Config-driven setup** — `config.json` for user-provided context (e.g., Slack channel); `AskUserQuestion` for structured input
- **Description field is a trigger** — Not a summary; tells the model *when* to activate the skill, not what it does
- **Memory via file logs** — Skills can maintain state (e.g., `standups.log`) across invocations; stable folder (`${CLAUDE_PLUGIN_DATA}`) for data that shouldn't be deleted on skill upgrade
- **On-demand hooks** — Session-scoped hooks like `/careful` (blocking destructive commands in prod) or `/freeze` (restricting edits to debug directories)
- **Organic curation over centralized control** — Skills gain traction organically; sandbox → PR → marketplace workflow; warns "quite easy to create bad or redundant skills"
- **Measuring via PreToolUse hooks** — Logging skill activation rates to find undertriggered or overused skills

## Relevance to UK Consumer Harms

This article is tangentially relevant — it documents how one major AI company structures agent tool-use skills and the engineering patterns behind them. While not directly about consumer harm, it provides:

- **A taxonomy of agent skills** that can inform how consumer-facing AI agents might be structured, tested, and regulated
- **Insights into agent behavior control** — hooks, verification skills, and railroading avoidance are relevant to understanding how agents can be constrained (or over-constrained)
- **Evidence of industry practice** — demonstrates that at least one AI company is actively investing in skill-based agent customization, with implications for market standardization and competitive dynamics

## Connection to Other Wiki Entries

- [[agentic-ai-workflows-guide-bandara-2025]] — Complementary engineering guide; Bandara et al. covers 9 best practices for production-grade agentic workflows; Shihipar covers 9 skill *types* and organizational patterns
- [[memory-in-the-age-of-ai-agents-hu-2025]] — Shihipar's "memory via file logs" pattern maps to the experiential memory taxonomy (case memory, skill memory) and append-only log patterns
- [[delegation-nation-comprehensive-research]] — Skills are the mechanism through which Advanced AI Assistants are customized and constrained; this article is a practitioner's guide to the infrastructure layer beneath delegation

## Notes

- Published on LinkedIn Pulse (JavaScript-rendered) and shared as an X Article
- No academic peer review; primary value is practitioner knowledge and lived experience at Anthropic
- The 9-type taxonomy could serve as a reference for categorizing skills in other agent frameworks
- The "organic curation" model (sandbox → PR → marketplace) is worth comparing to the Hermes Agent skill catalog approach documented in the existing skills list
