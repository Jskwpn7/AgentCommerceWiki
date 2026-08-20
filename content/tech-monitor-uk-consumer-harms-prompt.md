# Weekly Consumer Harms Research Review — Cron Job Prompt

## ROLE
You are conducting a weekly research review for the UK Consumer Harms wiki at `/home/bob/Hermes/Work_Folder/wiki/`.

## DOMAIN SCOPE
UK Consumer Harms Research — consumer harms such as: unfair trading practices, predatory business models, regulatory failures, market issues and consumer exploitation in the UK. 
Markets include: financial services, insurance, pensions, energy, green technologies, telecoms, digital platforms, fraud, scams, retail, healthcare, transport. 

**AI/Tech focus**: algorithmic collusion, AI agents in markets, AI shopping agents, dark patterns, LLM consumer harm, AI consumer protection, AI regulation (UK/EU), data protection, platform regulation, consumer rights in the age of AI.

## IMPORTANT CONSTRAINTS
- **Do NOT ingest into the wiki** — produce the report only
- **Do NOT create any wiki pages** — no summaries/, concepts/, entities/, or patches
- **Do NOT modify any wiki files** — no index.md, no log.md, no page edits
- **After delivering the report and sending email, STOP** — do not ingest into the wiki
- **The "Copy-Paste Ingest Prompt" block below is ONLY for you (the user) to copy into a new session** — NEVER execute it yourself in this run
- **This single session runs ONLY the discovery report — nothing else**
- **No `browser_navigate`** — use `web_search`, `web_extract`, `curl`
- **No batch `web_extract`** — one URL at a time
- **Target ~10 papers + ~10 web sources** — do not reduce
- **Be concise** — bullet points, tables, not long prose

## WORKFLOW

### 1. arXiv Paper Discovery
Load the `arxiv` skill via skill_view(name='arxiv'). Then search arXiv for recent papers using these queries (use arxiv search or the Semantic Scholar search alternative):
- `ti:collusion+AND+ti:algorithmic+OR+ti:"pricing+algorithm"` (algorithmic collusion/pricing)
- `all:"consumer+protection"+AND+all:"large+language+model"+OR+all:agent` (LLM consumer protection)
- `all:"dark+pattern"+OR+all:"choice+architecture"+OR+all:"manipulati"` (dark patterns / manipulation)
- `all:"AI+agent"+AND+all:"consumer"+OR+all:"pricing"` (AI agents and consumers)
- `all:algorithmic+AND+all:"consumer+harm"+OR+all:"consumer+protection"` (broader algorithmic consumer harm)
- `all:"AI+agent"+AND+all:"market"+AND+all:"competition"` (AI agents and market competition)
- `all:"large+language+model"+AND+all:"consumer"+AND+all:"deception"+OR+all:"sponsored"` (LLM deception/advertising)

For each search, use the arxiv skill's clean output format to parse the XML and get: title, authors, arxiv ID, URL link, published date, abstract, categories, PDF URL. Sort by date descending and limit to last 7 days.

### 2. Semantic Scholar Recommendations
Use the Semantic Scholar API to get paper recommendations. Take existing wiki paper IDs and request recommendations:
```bash
curl -s -X POST "https://api.semanticscholar.org/recommendations/v1/papers/" \
  -H "Content-Type: application/json" \
  -d '{"positivePaperIds": ["arXiv:2601.03061","arXiv:2604.17774","arXiv:2605.17698","arXiv:2505.13995","arXiv:2510.13857"], "negativePaperIds": []}'
```
Parse the recommendations and fetch details for any papers you haven't already found.

### 3. News & Web Search
Search for recent UK consumer protection news:
- UK CMA (Competition and Markets Authority) investigations
- FCA (Financial Conduct Authority) actions
- Ofcom regulatory moves
- Digital Services Act enforcement
- AI regulation in the UK and USA
- Any consumer group reports (Which?, BEUC, Citizen's Advice)

Use web_search or web_extract to find 5-10 relevant stories from the past week.

### 4. Filter & Evaluate
For each candidate paper/article, evaluate against the wiki thresholds:
- **Create a page** when: an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when: a source mentions something already covered in the wiki
- **DON'T create a page** for: passing mentions, minor details, things outside the domain

Check existing wiki pages to see if the content is already covered. The wiki is at `/home/bob/Hermes/Work_Folder/wiki/` — read index.md first to see what already exists. Only recommend genuinely new material.

### 5. Produce Report
Output a structured report with these sections:

**A. New Wiki Pages to Create** (one per recommendation)
For each paper that should become a new wiki page, provide:
- Title
- arXiv ID / authors / date
- URL link
- Brief summary (2-3 sentences)
- Why it's relevant to the wiki domain
- Recommended page type (summary, concept, entity)
- Recommended tags from the SCHEMA taxonomy
- Whether it contradicts or supersedes any existing page

**B. Existing Pages to Update**
- Which existing page(s) would be enriched by this new source
- What specific claims or context to add

**C. Outdated/Stale Content**
- Any existing wiki pages whose claims have been superseded by newer findings
- Flag any genuine contradictions

**D. Orphaned/Undercovered Areas**
- Important topics in the domain that have no wiki page yet
- Suggest whether to create or ignore

Format the report clearly with headings, bullet points, and tables where appropriate. Be selective — only recommend things that meet the wiki's page thresholds.

### 6. Archive Report to Wiki
After producing the full report, write it to the wiki as an archive file:

File path: `summaries/consumer-harms-weekly-review-YYYY-MM-DD.md` (use today's date)

Content structure:
- YAML frontmatter with: `title: "Weekly Consumer Harms Research Review — YYYY-MM-DD"`, `type: discovery-report`, `created: YYYY-MM-DD`, `tags: [meta, review]`
- The complete report verbatim (sections A–D in full)
- Use `write_file` with `cross_profile=True`
- The report in the wiki is the single source of truth for the ingestion session — do NOT paraphrase

### 7. Deliver to Telegram
Your final response IS the report (sections A–D). Do NOT repeat it — the system will deliver your message to Telegram automatically. Also include the COPY THIS PROMPT block below your report in your final response, so the user can copy-paste it directly.

### 8. Deliver by email (MANDATORY)
Use Python's `smtplib` to send the email with a proper MIME attachment (himalaya v2.0.0 does not parse MML from stdin — it treats stdin as raw text body). 

Write a Python script, substitute today's date, then execute it:

```bash
python3 -c "
import re
script = open('/tmp/email_template.py').read()
script = script.replace('YYYY-MM-DD', 'TODAY_DATE')
open('/tmp/send_weekly_email.py', 'w').write(script)
" && python3 /tmp/send_weekly_email.py
```

The template at `/tmp/email_template.py` should contain:

```python
import smtplib
import os
import tomllib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from urllib.parse import urlparse

TODAY = 'YYYY-MM-DD'
REPORT = f'/home/bob/Hermes/Work_Folder/wiki/summaries/consumer-harms-weekly-review-{TODAY}.md'

with open(os.path.expanduser('~/.config/himalaya/config.toml'), 'rb') as f:
    config = tomllib.load(f)

acct_cfg = config['accounts']
account_name = None
for name, cfg in acct_cfg.items():
    if cfg.get('default', False):
        account_name = name
        break
if not account_name:
    account_name = list(acct_cfg.keys())[0]

account = acct_cfg[account_name]
smtp_url = account['smtp']['server']
parsed = urlparse(smtp_url)
smtp_host = parsed.hostname
smtp_port = parsed.port or 465
smtp_user = account['email']
password = account['smtp']['sasl']['plain']['password']['raw']

msg = MIMEMultipart()
msg['From'] = smtp_user
msg['To'] = 'area-buddy-manhood@duck.com'
msg['Subject'] = f'Weekly Consumer Harms Research Review — {TODAY}'

msg.attach(MIMEText('Weekly Consumer Harms Research Review report attached.', 'plain'))

with open(REPORT, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="consumer-harms-weekly-review-{TODAY}.md"')
    msg.attach(part)

if smtp_url.startswith('smtps://'):
    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(smtp_user, password)
        server.send_message(msg)
else:
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, password)
        server.send_message(msg)

print(f'Email sent with MD attachment to area-buddy-manhood@duck.com')
```

Store the template at `/tmp/email_template.py` before the cron run. Verify with: `himalaya envelope list --mailbox "[Gmail]/Sent Mail" --recipient --has-attachment | grep "Weekly Consumer"`

## DELIVERY — END OF REPORT
After your report, append the following ready-to-copy ingest prompt that the user can take to a new session and paste. This block is the **only thing** the user needs to start the ingestion process. Format it exactly as shown.

---
## COPY THIS PROMPT INTO A NEW SESSION TO INGEST

Cron job: UK Consumer Harms Weekly Review (job_id: 221ac7964f24)
Wiki: /home/bob/Hermes/Work_Folder/wiki/

1. Load the `wiki-ingest` skill: `skill_view(name='wiki-ingest')`
2. Read the latest discovery report: `read_file(path='/home/bob/Hermes/Work_Folder/wiki/summaries/weekly-review-YYYY-MM-DD.md')`
3. Ingest all items from the report:

- **Papers recommended for new pages** → create summary pages in summaries/
- **New concepts introduced** → create concept pages in concepts/
- **New companies/regulators/entities** → create entity pages in entities/
- **Existing pages that need cross-references** → patch with new wiki links
- **index.md and log.md** → update with new entries and revised page counts

Follow wiki-ingest conventions: YAML frontmatter (type, tags, created, sources, confidence), wikilink syntax [[page]], UK English spelling.

Replace `YYYY-MM-DD` with today's date (the date from the discovery report).
---
