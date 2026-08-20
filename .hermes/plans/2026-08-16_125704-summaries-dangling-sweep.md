# Summaries Dangling-Link Sweep (299)

**Goal:** take `summaries/` from 299 dangling-wikilink errors to 0, using the same redirect-to-closest-page pattern as the chen-2025 fix — no mass concept-page creation.

**Context (verified 2026-08-16):** linter `scripts/wiki_health_check.py --full` → 299 errors, all `dangling-wikilink`, all in `summaries/` (75 files, 257 unique slugs). `concepts/`+`entities/` backbone already at 0. Vault: `/home/bob/Hermes/Work_Folder/wiki` (no git — log.md append via `cat >>`).

## Pattern breakdown (from `--full` analysis)

| Bucket | Count (approx) | Disposition |
|---|---|---|
| A. Obvious wrong-slug / case-variant / title-variant → real page exists | ~30 links, 17 slugs | Redirect (deterministic) |
| B. Self-references (link to the page's own source, e.g. `[[x402]]` in `x402-measurement-2607.12575.md`) | ~3 | De-wikilink to plain text |
| C. External URLs in wiki-brackets (`[[github.com/…]]`, `[[vitabench.github.io]]`) + syntax-example `[[page]]` in a monitor page | ~3 | Convert to plain `[text](url)` or de-wikilink |
| D. Title-form / regulator / never-ingested slugs needing a context call | ~45 links, ~30 slugs | Context review per occurrence (Phase 2) |
| E. One-off broad-concept slugs (`hallucination`, `marl`, `tool-use`, …) — no page, never will | ~210 links, ~190 slugs | De-wikilink to plain text, per `dangling-link-remediation.md` judgement table |

## Phase 0 — Decision menu (need Bob's call, 3 items)

1. **Concept-page exception:** a handful of *repeated, on-domain* slugs would genuinely benefit from a real page instead of 2–8 broken links each: `platform-agent-asymmetry` (8 files), `recommendation-manipulation` (4), `search-manipulation` (3), `user-simulation` (3), `personalization` (3). Options: (a) create up to 2–3 new concept pages (respects the ≤3 rule), (b) de-wikilink all. **Recommendation: (a) for `platform-agent-asymmetry` + `recommendation-manipulation` only; (b) for the rest.**
2. **`[[dsa]]` ×3** (weekly-review-2026-07-27, means EU Digital Services Act — a real regulatory doc, no entity page): create `entities/dsa.md` (thin entity page, matches `entities/ai-act.md` precedent) vs redirect to `concepts/dsa-vs-ai-act-overlap`. **Recommendation: create the entity page.**
3. **Never-ingested arXiv papers:** found during the sweep, any paper referenced by a never-ingested slug gets added to a **Future Ingest Candidates** list in the log entry — NOT auto-ingested (approval-gate rule).

## Phase 1 — Deterministic redirects (~30 links)

Every target **verified to exist on disk today** (all 16 returned OK on `find`):

| Dangling slug (occurrences) | → Target |
|---|---|
| `dark-patterns` (2) | `concepts/dark-pattern` |
| `eu-ai-act` (1) | `entities/ai-act` |
| `agent-liability-gap` (1) | `concepts/agent-liability` |
| `the-mills-review-summary` (1) | `entities/the-mills-review` |
| `agentic-web-requires-new-normative-infrastructure` (2) | `summaries/the-agentic-web-requires-new-normative-infrastructure` |
| `ecomagentbench-shopping-agents` (1, in `llm-agent-simulate-customers-2509.21501`) | `summaries/ecomagentbench-shopping-agents-2606.17698` |
| `UCP` (1) | `entities/universal-commerce-protocol-ucp` |
| `hidden-intent` (1) | `concepts/hidden-intent-agentic-shopping` |
| `llm-recommender` (2) | `summaries/llm-recommender-survey-2502.10050` |
| `algorithmic-pricing` (1) | `summaries/hotel-algorithmic-pricing-investigation` |
| `fairness` (1, in marl-dynamic-pricing) | `concepts/eu-digital-fairness-act` |
| `agentic-marketplace` (1) | `summaries/magentic-marketplace-2510.25779` |
| `dynamic-pricing` + `marl` (2, both in `marl-dynamic-pricing-2507.02698` — self-ref) | de-wikilink (bucket B) |
| `needs-prediction` (1) | `summaries/neon-living-needs-prediction-2307.16644` |
| `customer-service` (1) | `summaries/mindflow-customer-service-2507.18884` |
| `dual-control` (1) | `summaries/t2-bench-dual-control-2506.07982` |
| `virtual-assistants` (1) | `summaries/intelligent-virtual-assistants-2312.06677` |

Steps:
1. `python3 scripts/wiki_health_check.py --json > /tmp/dangling.json` — single source of truth.
2. For each mapping: `grep -n` the occurrence, read the line, confirm the redirect **reads naturally in sentence** (awkward → fall back to plain text).
3. Patch: `replace_all` where a slug repeats in a file; one `write_file` per file if ≥3 edits. Short unique `old_string` (token + few words), not full sentences — em-dash patch failures are a known pitfall.
4. Re-run linter; confirm each touched file drops out of findings.

## Phase 2 — Context review bucket (~45 links)

Per occurrence, apply the judgement table (`skills/wiki-ingest/references/dangling-link-remediation.md`):
- Regulators with no entity page — `CMA`, `FTC`, `Payment Systems Regulator`, `CRM`, `non-CRM`, `Tred`, `California Management Review`: **de-wikilink to plain text** (CMA/FTC have multiple investigation pages but no entity hub; linking one arbitrarily is wrong).
- `Consumer Protection from Unfair Trading Regulations 2008`: check `entities/` for a CPTUR page; else plain text.
- `DMCC-Act-2024`: check for a DMCCA entity page (`[[the-dmcca]]` resolves elsewhere in the vault — grep the actual slug); use it if on-topic, else plain text.
- `amazon` (2), `meituan` (1), `jd-com` (1), `amazon-rufus` (1): no company entity pages → plain text (or one `entities/amazon.md` if Bob opts in under Phase 0).
- `agentic-ai` (2), `agentic AI` (2), `AI commerce` (2), `consumer protection` (2), `EU consumer law` (2): these sit in monitor-report pages as *topic headers*, not wiki references → de-wikilink (headers stay as bold markdown).
- `supply-chain-opacity` (2), `algorithmic-price-collusion` (2), `opaque-procurement` (2), `cross-retail-purchasing` (2), `payment-vulnerabilities` (2), `multi-agent-systems` (2), `agentic-rl` (2), `generative-engine-optimization` (2), `travel-planning` (2), `benchmark` (2), `ranking-opacity` (2), `tool-use` (2), `llm-judge` (2), `consumer-protection` (1), `consumer-protection-uk-eu` (1): de-wikilink to plain text unless Phase 0 grants a page.
- `cais-agentic-ai-ecosystem-2026` (1): never-ingested framework — plain text + add to Future Ingest Candidates.

## Phase 3 — Bulk de-wikilink of one-off broad slugs (~210 links, ~190 slugs)

The long tail (`hallucination`, `marl`, `rag`, `benchmark`, `grounding`, `personalization` ×1-offs, etc.):
1. Script the mechanical part: throwaway Python in `/tmp` that, per file, replaces `[[slug]]` → `slug` (or `**slug**` inside "Related concepts" bullets to preserve list styling) **only for slugs on the de-wikilink list** — never blanket-regex.
2. De-wikilink list = everything in the `--json` findings **minus** Phase 1 mappings **minus** Phase 2 redirect targets. Generate it, eyeball it once (this is the only judgment-free bulk step, but the list must be explicit — no wildcards).
3. Preserve frontmatter `concepts:` entries: if a dangling slug is also listed in the page's own frontmatter as a plain tag, leave the tag (linter only checks wikilinks) — do not "fix" tags.
4. Batch: ≤5 files per write, verify each file after writing (frontmatter intact, closing `---` present, ≥200 chars).

## Phase 4 — Bookkeeping + final verify

1. `cat >> content/log.md` one entry: `## [2026-08-16] maintenance | summaries dangling-link sweep (299 → 0)` — counts by bucket, any new pages from Phase 0, **Future Ingest Candidates** list.
2. If Phase 0 created pages: add to `index.md` + recount totals from disk (`find … | wc -l` per dir — never from memory).
3. `python3 scripts/wiki_health_check.py` → **0 errors** expected; 130 warnings remain (all `raw/` frontmatter + low-outbound-links — separate deferred backlog, out of scope).
4. Spot-check 3 random fixed pages in Obsidian-style reading: links resolve, sentences read naturally.

## Files that will change

- `content/summaries/*.md` — 75 files (link fixes only; no body rewrites)
- Possibly: `content/entities/dsa.md` (new, Phase 0), 1–2 new `content/concepts/*.md` (Phase 0), `content/index.md`, `content/log.md`
- No changes to `scripts/wiki_health_check.py` (resolver validated 2026-08-15/16)

## Pitfalls (from prior sessions — do not repeat)

- **Verify every redirect target on disk before mapping** — 8 of 17 guessed slugs didn't exist last time. The Phase 1 table above is verified; anything added later must be `find`-checked.
- **Self-references are bugs**, not redirects (e.g. `[[x402]]` inside the x402 paper's own page).
- **Awkward phrasing after redirect = wrong target** → plain text instead.
- **`patch` fails on em-dash lines** → shortest unique `old_string`; 3+ edits to one file → single `write_file`.
- **Oversized terminal commands get blocked** → split, or write analyzer scripts to `/tmp` and run them.
- **read_file dedup** returns "unchanged" for same-session re-reads; if a patch says "could not find match", re-read the file.
- **No git** in the vault. Log via `cat >>` only, never `write_file` on `log.md`.
- **Never auto-ingest** never-ingested papers found during the sweep — list them for Bob.

## Definition of done

- `python3 scripts/wiki_health_check.py` → 0 errors (warnings ≤ 130, unchanged set).
- 0 `[[…]]` in `summaries/` that fail Obsidian-style resolution (path / slug / title).
- Log entry written; index counts accurate if new pages created.
- Bob gets a ≤10-line summary: buckets fixed, pages created, future-ingest candidates.
