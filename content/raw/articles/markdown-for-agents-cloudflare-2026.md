---
title: "Introducing Markdown for Agents"
created: 2026-07-24
updated: 2026-07-24
type: raw_article
tags: [markdown-for-agents, cloudflare, ai-crawlers, token-efficiency, content-negotiation, seo, ai-discovery, html-conversion, agent-economy]
sources: ["https://blog.cloudflare.com/markdown-for-agents/"]
confidence: high
provenance: "Manual ingestion — blog.cloudflare.com"
---

# Introducing Markdown for Agents

**Authors:** Celso Martinho, Will Allen
**Date:** 2026-02-12
**Source:** https://blog.cloudflare.com/markdown-for-agents/

## Content

The way content and businesses are discovered online is changing rapidly. In the past, traffic originated from traditional search engines, and SEO determined who got found first. Now the traffic is increasingly coming from AI crawlers and agents that demand structured data within the often-unstructured Web that was built for humans.

As a business, to continue to stay ahead, now is the time to consider not just human visitors, or traditional wisdom for SEO-optimization, but start to treat agents as first-class citizens.

## Why markdown is important

Feeding raw HTML to an AI is like paying by the word to read packaging instead of the letter inside. A simple `## About Us` on a page in markdown costs roughly 3 tokens; its HTML equivalent – `<h2 class="section-title" id="about">About Us</h2>` – burns 12-15, and that's before you account for the `<div>` wrappers, nav bars, and script tags that pad every real web page and have zero semantic value.

`## About Us`
`<h2 class="section-title" id="about">About Us</h2>`
`<div>`

This blog post you're reading takes 16,180 tokens in HTML and 3,150 when converted to markdown. **That's a 80% reduction in token usage**.

Markdown has quickly become the lingua franca for agents and AI systems as a whole. The format's explicit structure makes it ideal for AI processing, ultimately resulting in better results while minimizing token waste.

The problem is that the Web is made of HTML, not markdown, and page weight has been steadily increasing over the years, making pages hard to parse. For agents, their goal is to filter out all non-essential elements and scan the relevant content.

The conversion of HTML to markdown is now a common step for any AI pipeline. Still, this process is far from ideal: it wastes computation, adds costs and processing complexity, and above all, it may not be how the content creator intended their content to be used in the first place.

What if AI agents could bypass the complexities of intent analysis and document conversion, and instead receive structured markdown directly from the source?

## Convert HTML to markdown, automatically

Cloudflare's network now supports real-time content conversion at the source, for enabled zones using content negotiation headers. Now when AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for text/markdown in the request. Our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

To fetch the markdown version of any page from a zone with Markdown for Agents enabled, the client needs to add the **Accept** negotiation header with `text/markdown` as one of the options. Cloudflare will detect this, fetch the original HTML version from the origin, and convert it to markdown before serving it to the client.

Here's a curl example with the Accept negotiation header requesting a page from our developer documentation:

```
curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \
-H "Accept: text/markdown"
```

Or if you're building an AI Agent using Workers, you can use TypeScript:

```typescript
const r = await fetch(
  "https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/",
  {
    headers: {
      Accept: "text/markdown, text/html",
    },
  },
);
const tokenCount = r.headers.get("x-markdown-tokens");
const markdown = await r.text();
```

We already see some of the most popular coding agents today – like Claude Code and OpenCode – send these accept headers with their requests for content. Now, the response to this request is formatted in markdown. It's that simple.

Example response headers:
```
HTTP/2 200
date: Wed, 11 Feb 2026 11:44:48 GMT
content-type: text/markdown; charset=utf-8
content-length: 2899
vary: accept
x-markdown-tokens: 725
content-signal: ai-train=yes, search=yes, ai-input=yes
```

Note: we include an `x-markdown-tokens` header with the converted response that indicates the estimated number of tokens in the markdown document. You can use this value in your flow, for example to calculate the size of a context window or to decide on your chunking strategy.

## Content Signals Policy

During our last Birthday Week, Cloudflare announced Content Signals — a framework that allows anyone to express their preferences for how their content can be used after it has been accessed.

When you return markdown, you want to make sure your content is being used by the Agent or AI crawler. That's why Markdown for Agents converted responses include the `Content-Signal: ai-train=yes, search=yes, ai-input=yes` header signaling that indicates content can be used for AI Training, Search results and AI Input, which includes agentic use. Markdown for Agents will provide options to define custom Content Signal policies in the future.

## Other ways to convert to Markdown

If you're building AI systems that require arbitrary document conversion from outside Cloudflare or Markdown for Agents is not available from the content source, Cloudflare provides other ways to convert documents to Markdown for your applications:

1. **Workers AI `AI.toMarkdown()`** — Supports multiple document types, not just HTML, and summarization.
2. **Browser Rendering `/markdown` REST API** — Supports markdown conversion if you need to render a dynamic page or application in a real browser before converting it.

## Tracking markdown usage

Anticipating a shift in how AI systems browse the Web, Cloudflare Radar now includes content type insights for AI bot and crawler traffic, both globally on the AI Insights page and in the individual bot information pages.

The new `content_type` dimension and filter shows the distribution of content types returned to AI agents and crawlers, grouped by MIME type category.

You can also see the requests for markdown filtered by a specific agent or crawler. Here are the requests that return markdown to OAI-Searchbot, the crawler used by OpenAI to power ChatGPT's search.

This new data will allow us to track the evolution of how AI bots, crawlers, and agents are consuming Web content over time. As always, everything on Radar is freely accessible via the public APIs and the Data Explorer.

## Start using today

To enable Markdown for Agents for your zone, log into the Cloudflare dashboard, select your account, select the zone, look for Quick Actions and toggle the Markdown for Agents button to enable. This feature is available today in Beta at no cost for Pro, Business and Enterprise plans, as well as SSL for SaaS customers.

## Relevance to UK Consumer Harms Research

This article documents a significant shift in how AI agents discover and consume web content. For consumer protection research, it raises several concerns:

1. **Agent-mediated content discovery:** As AI agents increasingly browse the web on behalf of consumers (e.g., for price comparison, product research), the content they consume may be shaped by how sites format and signal their content to agents vs humans. This creates a divergence between what consumers see and what their agents see.

2. **Token efficiency as a business incentive:** The 80% token savings from markdown conversion creates strong incentives for businesses to optimise for AI agents. This could concentrate discovery toward sites that are agent-friendly, potentially marginalising smaller businesses that lack the resources to implement agent-optimised content formats.

3. **Content Signals as a transparency mechanism:** Cloudflare's Content Signals framework gives content creators explicit control over AI training, search, and agent access. For consumer protection, this could either improve transparency (consumers know how their agents access content) or worsen opacity (agents access content under different terms than humans).

4. **SEO evolution:** As SEO shifts from traditional search to AI agent optimisation, businesses may prioritise different content signals for agents vs humans, creating two different versions of their online presence.
