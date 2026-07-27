---
title: "Introducing Markdown for Agents"
created: 2026-07-24
updated: 2026-07-24
type: summary
tags: [markdown-for-agents, cloudflare, ai-crawlers, token-efficiency, content-negotiation, ai-discovery, agent-economy, content-signals]
sources: ["https://blog.cloudflare.com/markdown-for-agents/"]
confidence: high
provenance: "Manual ingestion — Cloudflare blog"
---

# Markdown for Agents: Cloudflare's Real-Time HTML-to-Markdown Conversion

**Source:** Cloudflare Blog — Celso Martinho, Will Allen (2026-02-12)
**Link:** https://blog.cloudflare.com/markdown-for-agents/

## Summary

Cloudflare has introduced **Markdown for Agents**, a feature that automatically converts HTML pages to markdown on-the-fly for AI agents and crawlers using content negotiation. When a client sends an `Accept: text/markdown` header, Cloudflare's network fetches the origin HTML, converts it to markdown, and serves the markdown version — returning an `x-markdown-tokens` header indicating estimated token count.

The blog post demonstrates an **80% token reduction**: a 16,180-token HTML article becomes 3,150 tokens in markdown. This is achieved through Cloudflare's CDN-level conversion, avoiding the need for downstream HTML-to-markdown conversion tools.

## Key Features

1. **Real-time conversion at the CDN layer** — Content is fetched from origin HTML, converted to markdown on-the-fly, and served with `Content-Type: text/markdown`.
2. **Content Signals headers** — Converted responses include `Content-Signal: ai-train=yes, search=yes, ai-input=yes`, indicating how the content can be used. Cloudflare plans to support custom Content Signal policies.
3. **Token estimation** — The `x-markdown-tokens` header gives AI systems an estimate of context window usage, enabling better chunking and cost management.
4. **Agent adoption** — Major coding agents like Claude Code and OpenCode already send `Accept: text/markdown` headers by default.
5. **Additional conversion tools** — Workers AI `AI.toMarkdown()` for multi-document conversion and Browser Rendering `/markdown` REST API for dynamic page rendering.
6. **Cloudflare Radar tracking** — New `content_type` dimension in AI Insights tracks markdown delivery to AI bots/crawlers by content type and user agent.

## Consumer Harm Relevance

This article documents a significant architectural shift in how AI agents consume web content, with several implications for consumer protection:

1. **Agent vs human content divergence:** Businesses may optimise content differently for agents vs humans, creating two different online experiences. This could mean AI agents recommend products based on different content than what consumers would see browsing directly.

2. **Agent-friendly SEO concentration:** Sites that invest in Markdown for Agents gain 80% token savings — a structural advantage in agent-mediated discovery. Smaller businesses may lack resources to implement this, potentially concentrating agent-driven traffic toward larger sites.

3. **Content Signals transparency:** The Content Signals framework gives content creators explicit control over AI usage. For consumer protection, this could improve transparency but may also fragment content availability — some sites may allow agent access while blocking training data, or vice versa.

4. **Agent-mediated shopping implications:** As [[ai-shopping-agents]] become more prevalent, the content format they consume (markdown vs HTML) will shape product recommendations. If agents receive structured, token-efficient content, they may make different recommendations than if they received the full HTML experience.

## Connection to Other Wiki Entries

- [[ai-shopping-agents]] — As shopping agents consume more web content, content format directly affects their recommendations
- [[agent-nudge-sensitivity]] — Structured markdown content may be more easily manipulated by choice architecture
- [[dark-pattern.md]] — If agents receive different content formats than humans, dark patterns may operate differently against AI agents vs human users
- [[conflict-of-interest-in-llm-deployment]] — Businesses optimising for agent-friendly content may prioritise commercially beneficial signals
- [[ai-discovery]] — SEO is shifting from search engines to AI agents as the primary content discovery mechanism
