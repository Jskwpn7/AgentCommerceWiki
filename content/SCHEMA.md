# Wiki Schema

## Domain
UK Consumer Harms Research — unfair trading practices, predatory business models, regulatory failures, and documented cases of consumer exploitation in the United Kingdom. Covers financial services, energy, telecoms, digital platforms, housing, and broader market failures.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `energy-price-cap-harms.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]] (wikilinks)` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]` at the end of paragraphs whose claims come from a specific source.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

## Tag Taxonomy

**Sectors:** financial-services, energy, telecoms, digital-platforms, housing, retail, healthcare, transport, insurance, pension

**Harm Types:** misleading-practice, hidden-fee, lock-in, dark-pattern, price-gouging, planned-obsolescence, data-abuse, monopoly, false-scarcity, bait-and-switch, choice-architecture, gatekeeping, agent-liability, protocol-competition
**Regulatory Bodies:** cma (competition-and-markets-authority), fca (financial-conduct-authority), ofgem, ofcom, fos (financial-ombudsman-service), consumer-rights, dmcc-act, dmcc-act-2024, ftc, eu-commission, nist, gdpr
**Themes:** cost-of-living, vulnerability, digital-consumer, corporate-accountability, regulatory-failure, cross-sector, policy-research

**Meta:** comparison, timeline, controversy, prediction, report, investigation, person, academic, research, methodology, methodology-critique, agentic-ai

Rule: every tag on a page must appear in this taxonomy. If a new tag is needed, add it here first, then use it.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (company, regulator, report, investigation, policy). Include:
- Overview / what it is
- Key dates and facts
- Documented harms or failures
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- How it manifests in the UK
- Examples and evidence
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
