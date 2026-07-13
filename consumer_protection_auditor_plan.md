# Consumer Protection Auditor Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a CLI tool that navigates websites, captures data, and assesses compliance with UK consumer protection regulations.

**Architecture:** A modular CLI tool with three core layers — a navigation engine (Playwright) for data capture, a rules engine (structured config + LLM-assisted) for compliance assessment, and a reporting layer (JSON + Markdown). Config files define targets, rules, and assessment parameters.

**Tech Stack:** Python 3.11+, Playwright, Pydantic (config/model validation), async/await, LLM integration for assessment, config via YAML.

---

## Phase 0: Project Setup

### Task 0.1: Create project structure

**Objective:** Initialize the Python project with a clean directory layout.

**Files:**
- Create: `consumer_tool/` (package directory)
- Create: `tests/` (test directory)
- Create: `configs/` (example config files)
- Create: `pyproject.toml`
- Create: `README.md`

**Step 1: Create pyproject.toml**

```toml
[project]
name = "consumer-tool"
version = "0.1.0"
description = "UK consumer protection compliance auditing tool"
requires-python = ">=3.11"
dependencies = [
    "playwright>=1.40",
    "pydantic>=2.0",
    "pyyaml>=6.0",
    "httpx>=0.27",
    "jinja2>=3.1",
]

[project.scripts]
consumer = "consumer_tool.cli:main"

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.backends._legacy:_Backend"
```

**Step 2: Run setup**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
playwright install chromium
```

**Step 3: Commit**

```bash
git init
git add -A
git commit -m "init: project skeleton with pyproject.toml and directory structure"
```

---

## Phase 1: Core Data Model

### Task 1.1: Define target and rule data models

**Objective:** Create Pydantic models for site targets, audit rules, and configuration.

**Files:**
- Create: `consumer_tool/models/target.py`
- Create: `consumer_tool/models/rule.py`
- Create: `consumer_tool/models/config.py`

**Step 1: Target model** (`consumer_tool/models/target.py`)

```python
from pydantic import BaseModel, Field
from typing import Optional

class SiteTarget(BaseModel):
    """A website (or sub-section) to audit."""
    url: str
    name: Optional[str] = None  # Human label
    description: Optional[str] = None  # What this target represents
    allowed_domains: Optional[list[str]] = None  # Same-site navigation scope
    max_pages: int = 20  # Safety limit on pages to visit
    wait_after_load: float = 2.0  # Seconds to wait for JS/rendering

class AuditConfig(BaseModel):
    """Full audit configuration."""
    name: str
    targets: list[SiteTarget]
    rules: list["RuleConfig"]
    output: OutputConfig = Field(default_factory=OutputConfig)
    browser: BrowserConfig = Field(default_factory=BrowserConfig)
```

**Step 2: Rule model** (`consumer_tool/models/rule.py`)

```python
from pydantic import BaseModel
from typing import Optional, Literal, Any

class RuleConfig(BaseModel):
    """A compliance rule to apply during assessment."""
    name: str
    description: str
    regulation: str  # e.g., "CMA Consumer Protection Regulations 2024"
    severity: Literal["low", "medium", "high", "critical"]
    type: Literal["structured", "llm"]  # Which assessment method

    # For structured rules
    checks: Optional[list[StructuredCheck]] = None

    # For LLM rules
    prompt_template: Optional[str] = None
    llm_context_fields: Optional[list[str]] = None

class StructuredCheck(BaseModel):
    """A specific structured check within a rule."""
    name: str
    field_path: str  # e.g., "checkout.total_price"
    condition: str  # e.g., "gte", "contains", "regex_match"
    expected: Any
    message: str  # What this check verifies
```

**Step 3: Output and browser config** (`consumer_tool/models/config.py`)

```python
from pydantic import BaseModel
from typing import Optional
from .rule import RuleConfig

class OutputConfig(BaseModel):
    """Where and how to write results."""
    json_output: Optional[str] = "output/results.json"
    markdown_output: Optional[str] = "output/report.md"
    raw_data_dir: Optional[str] = "output/raw/"

class BrowserConfig(BaseModel):
    """Browser automation settings."""
    headless: bool = True
    viewport_width: int = 1920
    viewport_height: int = 1080
    timeout: int = 30000
    user_agent: Optional[str] = None
    wait_for_network_idle: bool = False
```

**Step 4: Run to verify models instantiate**

```bash
python -c "
from consumer_tool.models.target import SiteTarget
from consumer_tool.models.config import AuditConfig
t = SiteTarget(url='https://example.com', name='Test Site')
print(t.model_dump_json(indent=2))
"
```

Expected output: Valid JSON showing the SiteTarget fields.

**Step 5: Commit**

```bash
git add consumer_tool/models/ pyproject.toml
git commit -m "models: define target, rule, and config data models with Pydantic"
```

---

## Phase 2: Configuration Loading

### Task 2.1: Config file loader

**Objective:** Read YAML config files and validate them against the Pydantic models.

**Files:**
- Create: `consumer_tool/config/loader.py`

**Step 1: Write config loader**

```python
import yaml
from pathlib import Path
from consumer_tool.models.config import AuditConfig

def load_config(config_path: str | Path) -> AuditConfig:
    """Load and validate an audit configuration from a YAML file."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")

    with open(path) as f:
        data = yaml.safe_load(f)

    return AuditConfig.model_validate(data)

def discover_configs(directory: str | Path) -> list[Path]:
    """Find all YAML config files in a directory."""
    return sorted(Path(directory).glob("*.yml")) + \
           sorted(Path(directory).glob("*.yaml"))
```

**Step 2: Create example config** (`configs/example-audit.yml`)

```yaml
name: "Example Consumer Protection Audit"
description: "Demonstration audit of a sample site"

targets:
  - url: "https://example.com"
    name: "Example Store"
    description: "Single product checkout flow"
    max_pages: 10

rules:
  - name: "price_transparency"
    description: "Verify total price includes all mandatory charges"
    regulation: "Consumer Protection from Unfair Trading Regulations 2008"
    severity: "high"
    type: "structured"
    checks:
      - name: "includes_tax"
        field_path: "checkout.total_price"
        condition: "regex_match"
        expected: "^£\\d+\\.\\d{2} \\(VAT inc\\)$"
        message: "Total price should clearly indicate VAT inclusion"

output:
  json_output: "output/results.json"
  markdown_output: "output/report.md"
  raw_data_dir: "output/raw/"
```

**Step 3: Write test** (`tests/test_config_loader.py`)

```python
import pytest
from pathlib import Path
from consumer_tool.config.loader import load_config
from consumer_tool.models.config import AuditConfig

CONFIG_PATH = Path("configs/example-audit.yml")

def test_load_config():
    config = load_config(CONFIG_PATH)
    assert isinstance(config, AuditConfig)
    assert config.name == "Example Consumer Protection Audit"
    assert len(config.targets) == 1
    assert config.targets[0].url == "https://example.com"
    assert len(config.rules) == 1
    assert config.rules[0].type == "structured"

def test_load_missing_config():
    with pytest.raises(FileNotFoundError):
        load_config("configs/nonexistent.yml")
```

**Step 4: Run test**

```bash
pytest tests/test_config_loader.py -v
```

Expected: 1 passed, 1 failed (FileNotFoundError test confirms proper error).

**Step 5: Commit**

```bash
git add consumer_tool/config/ configs/ tests/test_config_loader.py
git commit -m "config: add YAML config loading with validation"
```

---

## Phase 3: Navigation Engine (Playwright)

### Task 3.1: Browser session manager

**Objective:** Create a context manager that handles browser lifecycle per audit.

**Files:**
- Create: `consumer_tool/navigator/browser.py`

**Step 1: Write browser session manager**

```python
from contextlib import asynccontextmanager
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from consumer_tool.models.config import BrowserConfig

class BrowserSession:
    """Manages a Playwright browser instance for navigation."""

    def __init__(self, config: BrowserConfig):
        self.config = config
        self.playwright = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.captured_pages: list[dict] = []  # Stores captured data per page

    async def __aenter__(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=self.config.headless)
        self.context = await self.browser.new_context(
            viewport={"width": self.config.viewport_width, "height": self.config.viewport_height},
            user_agent=self.config.user_agent,
        )
        if self.config.wait_for_network_idle:
            await self.context.set_default_timeout(self.config.timeout)
        return self

    async def __aexit__(self, *args):
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()

    async def navigate(self, url: str, max_wait: float | None = None) -> Page:
        """Navigate to a URL and return the page."""
        page = await self.context.new_page()
        if max_wait:
            await page.goto(url, wait_until="networkidle", timeout=int(max_wait))
        else:
            await page.goto(url, wait_until="domcontentloaded")
        await asyncio.sleep(self.config.wait_after_load)
        return page

    async def capture_page_data(self, page: Page) -> dict:
        """Extract structured data from the current page."""
        # Core extraction: DOM text, visible elements, links
        title = await page.title()
        url = page.url

        # Extract all visible text content (cleaned)
        body_text = await page.evaluate("""
            () => document.body?.innerText || ''
        """).strip()

        # Extract all links with text
        links = await page.evaluate("""
            () => Array.from(document.querySelectorAll('a[href]'))
                .map(a => ({ text: a.textContent?.trim(), href: a.href }))
                .filter(l => l.text && l.text.length > 0)
        """)

        # Extract all images with alt text
        images = await page.evaluate("""
            () => Array.from(document.querySelectorAll('img'))
                .map(img => ({ src: img.src, alt: img.alt || img.getAttribute('alt') || '' }))
        """)

        # Extract all form elements
        forms = await page.evaluate("""
            () => Array.from(document.querySelectorAll('form'))
                .map(f => ({
                    action: f.action,
                    method: f.method,
                    inputs: Array.from(f.querySelectorAll('input, select, textarea'))
                        .map(i => ({ type: i.type, name: i.name, value: i.value }))
                }))
        """)

        return {
            "url": url,
            "title": title,
            "body_text": body_text,
            "links": links,
            "images": images,
            "forms": forms,
        }

    async def save_raw_data(self, page_data: dict, output_dir: Path):
        """Save raw captured data to disk for later inspection."""
        safe_name = page_data["url"].replace("://", "_").replace("/", "_")
        path = output_dir / f"{safe_name}.json"
        import json
        path.write_text(json.dumps(page_data, indent=2))
        return path
```

**Step 2: Write test** (`tests/test_browser_session.py`)

```python
import pytest
import asyncio
from consumer_tool.models.config import BrowserConfig
from consumer_tool.navigator.browser import BrowserSession

@pytest.mark.asyncio
async def test_browser_session_lifecycle():
    """Test that browser opens and closes cleanly."""
    config = BrowserConfig(headless=True)
    async with BrowserSession(config) as session:
        assert session.browser is not None
        assert session.context is not None
```

**Step 3: Run test**

```bash
pytest tests/test_browser_session.py -v
```

**Step 4: Commit**

```bash
git add consumer_tool/navigator/ tests/test_browser_session.py
git commit -m "navigator: add Playwright browser session manager with page data capture"
```

### Task 3.2: Page visitor (navigation logic)

**Objective:** Navigate from a starting URL, visiting allowed sub-pages up to a limit.

**Files:**
- Create: `consumer_tool/navigator/visitor.py`

**Step 1: Write page visitor**

```python
from pathlib import Path
import asyncio
from consumer_tool.models.target import SiteTarget
from consumer_tool.models.config import BrowserConfig, OutputConfig
from consumer_tool.navigator.browser import BrowserSession

class PageVisitor:
    """Traverses a site, capturing data from each page visited."""

    def __init__(self, target: SiteTarget, browser: BrowserSession, output_config: OutputConfig):
        self.target = target
        self.browser = browser
        self.output_config = output_config
        self.captured_data: list[dict] = []
        self.visited_urls: set[str] = set()

    def _is_same_domain(self, url: str) -> bool:
        """Check if a URL belongs to the same domain as the target."""
        from urllib.parse import urlparse
        target_domain = urlparse(self.target.url).netloc
        target_domain = target_domain.lstrip("www.")
        check_domain = urlparse(url).netloc
        check_domain = check_domain.lstrip("www.")
        return check_domain == target_domain

    async def visit(self) -> list[dict]:
        """Navigate and capture data from the target site."""
        pages_to_visit = [self.target.url]

        while pages_to_visit and len(self.visited_urls) < self.target.max_pages:
            url = pages_to_visit.pop(0)
            if url in self.visited_urls:
                continue
            self.visited_urls.add(url)

            print(f"  Navigating: {url}")
            page = await self.browser.navigate(url)
            data = await self.browser.capture_page_data(page)
            self.captured_data.append(data)

            # Save raw data
            if self.output_config.raw_data_dir:
                raw_dir = Path(self.output_config.raw_data_dir)
                raw_dir.mkdir(parents=True, exist_ok=True)
                await self.browser.save_raw_data(data, raw_dir)

            # Enqueue same-domain links
            if len(pages_to_visit) < 50:  # Soft limit to avoid runaway traversal
                allowed = [
                    link["href"] for link in data["links"]
                    if link["href"].startswith("http") and self._is_same_domain(link["href"])
                ]
                pages_to_visit.extend(allowed)

        return self.captured_data
```

**Step 2: Commit**

```bash
git add consumer_tool/navigator/visitor.py
git commit -m "navigator: add page visitor with same-domain traversal"
```

---

## Phase 4: Assessment Engine

### Task 4.1: Structured rule evaluator

**Objective:** Evaluate structured checks against captured page data.

**Files:**
- Create: `consumer_tool/assess/structured.py`

**Step 1: Write structured evaluator**

```python
import re
from consumer_tool.models.rule import RuleConfig, StructuredCheck
from operator import gt, gte, lt, lte, eq, ne

CONDITION_OPS = {
    "eq": lambda a, b: str(a) == str(b),
    "ne": lambda a, b: str(a) != str(b),
    "gt": lambda a, b: float(a) > float(b),
    "gte": lambda a, b: float(a) >= float(b),
    "lt": lambda a, b: float(a) < float(b),
    "lte": lambda a, b: float(a) <= float(b),
    "contains": lambda a, b: str(b) in str(a),
    "not_contains": lambda a, b: str(b) not in str(a),
    "regex_match": lambda a, b: bool(re.search(str(b), str(a))),
    "regex_nomatch": lambda a, b: not bool(re.search(str(b), str(a))),
}

class StructuredEvaluator:
    """Evaluates structured checks against captured page data."""

    def __init__(self, rule: RuleConfig):
        self.rule = rule
        self.results: list[dict] = []

    def _resolve_field(self, data: dict, field_path: str) -> str | None:
        """Resolve a dotted field path in captured data."""
        current = data
        for part in field_path.split("."):
            if isinstance(current, dict) and part in current:
                current = current[part]
            elif isinstance(current, str):
                # Simple text search: look for the path pattern in body text
                if part in current:
                    return current[:200]  # Return context
                return None
            else:
                return None
        return str(current) if current is not None else None

    def evaluate(self, page_data: dict) -> list[dict]:
        """Evaluate all checks in this rule against a page's data."""
        findings = []

        for check in (self.rule.checks or []):
            value = self._resolve_field(page_data, check.field_path)
            passed = True
            reason = ""

            if check.condition == "regex_match" or check.condition == "regex_nomatch":
                # For regex, search in body text if field path doesn't resolve
                search_target = self._find_text_in_body(page_data, check.field_path)
                match = bool(re.search(str(check.expected), search_target)) if search_target else False
                passed = match if check.condition == "regex_match" else not match
                reason = f"Pattern check: field_path='{check.field_path}' expected='{check.expected}'"
            elif value is not None:
                op_func = CONDITION_OPS.get(check.condition)
                if op_func:
                    try:
                        passed = op_func(value, check.expected)
                    except (ValueError, TypeError):
                        passed = False
                    reason = f"Comparison: '{value}' {check.condition} '{check.expected}'"
                else:
                    passed = False
                    reason = f"Unknown condition: {check.condition}"
            else:
                passed = False
                reason = f"Field '{check.field_path}' not found in page data"

            findings.append({
                "check_name": check.name,
                "field_path": check.field_path,
                "passed": passed,
                "value": value,
                "reason": reason,
                "message": check.message,
            })

        return findings

    def _find_text_in_body(self, page_data: dict, search_pattern: str) -> str:
        """Search for a pattern in page body text."""
        body = page_data.get("body_text", "")
        # Extract a window around the match
        idx = body.lower().find(search_pattern.lower())
        if idx >= 0:
            start = max(0, idx - 100)
            end = min(len(body), idx + len(search_pattern) + 100)
            return body[start:end]
        return body[:500]  # Fallback: return first 500 chars
```

**Step 2: Write test** (`tests/test_structured_evaluator.py`)

```python
import pytest
from consumer_tool.models.rule import RuleConfig
from consumer_tool.assess.structured import StructuredEvaluator

def make_rule(checks):
    return RuleConfig(
        name="test_rule",
        description="Test rule",
        regulation="Test",
        severity="medium",
        type="structured",
        checks=checks,
    )

def test_regex_match_check():
    rule = make_rule([
        StructuredCheck(
            name="vat_included",
            field_path="£12.99 (VAT included)",
            condition="regex_match",
            expected=r"£\d+\.\d{2} \(VAT.*\)",
            message="Price should show VAT status",
        )
    ])
    evaluator = StructuredEvaluator(rule)
    findings = evaluator.evaluate({"body_text": "Total: £45.99 (VAT included)"})
    assert len(findings) == 1
    assert findings[0]["passed"] is True

def test_contains_check():
    rule = make_rule([
        StructuredCheck(
            name="no_returns_policy",
            field_path="returns",
            condition="not_contains",
            expected="return",
            message="Returns policy should be visible",
        )
    ])
    evaluator = StructuredEvaluator(rule)
    findings = evaluator.evaluate({"body_text": "No returns accepted."})
    assert findings[0]["passed"] is True
```

**Step 3: Run test**

```bash
pytest tests/test_structured_evaluator.py -v
```

**Step 4: Commit**

```bash
git add consumer_tool/assess/ structured.py tests/test_structured_evaluator.py
git commit -m "assess: add structured rule evaluator with configurable conditions"
```

### Task 4.2: LLM-assisted assessment

**Objective:** Send captured data to an LLM for nuanced compliance analysis.

**Files:**
- Create: `consumer_tool/assess/llm.py`

**Step 1: Write LLM assessor**

```python
from pathlib import Path
from consumer_tool.models.rule import RuleConfig
from consumer_tool.models.target import SiteTarget

class LLMAssessor:
    """Uses an LLM to assess compliance against nuanced rules."""

    def __init__(self, api_key: str | None = None, model: str = "claude-sonnet-4"):
        self.api_key = api_key
        self.model = model

    async def assess(self, rule: RuleConfig, page_data: dict, target: SiteTarget) -> dict:
        """Send page data to LLM for compliance assessment."""
        import os
        api_key = self.api_key or os.environ.get("LLM_API_KEY")

        if not api_key:
            return {
                "llm_assessment": None,
                "error": "LLM_API_KEY not set. Set it as environment variable.",
                "passed": None,
            }

        # Build the prompt
        prompt = self._build_prompt(rule, page_data, target)

        # Call the LLM — using OpenAI-compatible API (works with OpenRouter, Ollama, etc.)
        import httpx
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": "You are a UK consumer protection compliance analyst."},
                        {"role": "user", "content": prompt},
                    ],
                    "temperature": 0.3,
                },
            )
            result = response.json()
            assistant_msg = result["choices"][0]["message"]["content"]

        # Parse the LLM response — expect structured JSON
        import json
        try:
            # Try to extract JSON from the response
            import re
            json_match = re.search(r'\{.*\}', assistant_msg, re.DOTALL)
            if json_match:
                parsed = json.loads(json_match.group())
            else:
                parsed = {"analysis": assistant_msg}
        except (json.JSONDecodeError, AttributeError):
            parsed = {"analysis": assistant_msg}

        parsed["raw_response"] = assistant_msg
        return parsed

    def _build_prompt(self, rule: RuleConfig, page_data: dict, target: SiteTarget) -> str:
        """Build the LLM prompt for this assessment."""
        return f"""Assess this page for potential UK consumer protection violations.

REGULATION: {rule.regulation}
RULE: {rule.name} — {rule.description}
SEVERITY: {rule.severity}

TARGET SITE: {target.name or target.url}

PAGES CAPTURED:
{json.dumps(page_data, indent=2, default=str)[:4000]}

Provide a JSON response with:
- "passed": true/false (overall assessment)
- "findings": array of observations
- "confidence": 0.0-1.0
- "explanation": natural language reasoning

If "passed" is false, explain what concern was identified and why.
"""
```

**Step 2: Commit**

```bash
git add consumer_tool/assess/llm.py
git commit -m "assess: add LLM-assisted compliance assessment"
```

---

## Phase 5: Reporting

### Task 5.1: JSON report writer

**Objective:** Write structured JSON output of all audit results.

**Files:**
- Create: `consumer_tool/report/json_reporter.py`

**Step 1: Write JSON reporter**

```python
import json
from pathlib import Path
from datetime import datetime

class JsonReporter:
    """Writes audit results as structured JSON."""

    def __init__(self, output_path: str):
        self.output_path = Path(output_path)

    def write(self, audit_name: str, results: list[dict]):
        """Write complete audit results."""
        report = {
            "audit_name": audit_name,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "summary": self._summary(results),
            "findings": results,
        }
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(json.dumps(report, indent=2, default=str))
        return self.output_path

    def _summary(self, results: list[dict]) -> dict:
        """Generate summary statistics."""
        total_checks = sum(len(f.get("structured_results", [])) for f in results)
        passed = sum(1 for r in results for c in r.get("structured_results", []) if c["passed"])
        failed = total_checks - passed
        llm_results = sum(1 for r in results if r.get("llm_assessment"))

        return {
            "total_findings": len(results),
            "total_structured_checks": total_checks,
            "passed": passed,
            "failed": failed,
            "llm_assessed": llm_results,
        }
```

### Task 5.2: Markdown report writer

**Objective:** Generate a human-readable Markdown report.

**Files:**
- Create: `consumer_tool/report/md_reporter.py`

**Step 1: Write Markdown reporter**

```python
from pathlib import Path
from datetime import datetime
from jinja2 import Template

MARKDOWN_TEMPLATE = """\
# Consumer Protection Audit Report

**Audit:** {{ audit_name }}
**Date:** {{ timestamp }}

## Summary

| Metric | Value |
|--------|-------|
| Sites audited | {{ findings|length }} |
| Structured checks | {{ summary.total_structured_checks }} |
| Passed | {{ summary.passed }} |
| Failed | {{ summary.failed }} |
| LLM-assessed | {{ summary.llm_assessed }} |

{% for finding in findings %}
## {{ finding.url }}

**Site:** {{ finding.target_name or finding.url }}

{% if finding.structured_results %}
### Structured Rule Results

{% for check in finding.structured_results %}
- **{{ check.check_name }}** — {{ "✅ PASS" if check.passed else "❌ FAIL" }}
  - Rule: {{ check.rule_name }}
  - {{ check.message }}
  - {% if not check.passed %}Observed: `{{ check.value }}`{% endif %}
{% endfor %}
{% endif %}

{% if finding.llm_assessment %}
### LLM Assessment

{{ finding.llm_assessment.explanation }}

{% for obs in finding.llm_assessment.findings %}
- {{ obs }}
{% endfor %}
{% endif %}

{% endfor %}
"""

class MarkdownReporter:
    """Writes audit results as a human-readable Markdown report."""

    def __init__(self, output_path: str):
        self.output_path = Path(output_path)
        self.template = Template(MARKDOWN_TEMPLATE)

    def write(self, audit_name: str, results: list[dict], summary: dict):
        """Write the Markdown report."""
        html = self.template.render(
            audit_name=audit_name,
            timestamp=datetime.utcnow().isoformat() + "Z",
            findings=results,
            summary=summary,
        )
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(html)
        return self.output_path
```

**Step 2: Commit**

```bash
git add consumer_tool/report/
git commit -m "report: add JSON and Markdown report writers"
```

---

## Phase 6: CLI Entry Point

### Task 6.1: Main CLI command

**Objective:** Create the CLI entry point that ties everything together.

**Files:**
- Create: `consumer_tool/cli.py`

**Step 1: Write CLI**

```python
import argparse
import asyncio
import sys
from pathlib import Path
from consumer_tool.config.loader import load_config
from consumer_tool.navigator.browser import BrowserSession
from consumer_tool.navigator.visitor import PageVisitor
from consumer_tool.assess.structured import StructuredEvaluator
from consumer_tool.assess.llm import LLMAssessor
from consumer_tool.report.json_reporter import JsonReporter
from consumer_tool.report.md_reporter import MarkdownReporter

async def run_audit(config_path: str):
    """Run a full audit from a config file."""
    # Load config
    print(f"Loading config: {config_path}")
    config = load_config(config_path)
    print(f"Audit: {config.name}")
    print(f"Targets: {len(config.targets)}, Rules: {len(config.rules)}\n")

    # Initialize reporters
    json_reporter = JsonReporter(config.output.json_output)
    md_reporter = MarkdownReporter(config.output.markdown_output)

    # Initialize LLM assessor
    llm_assessor = LLMAssessor()

    all_results = []

    # Initialize browser session
    async with BrowserSession(config.browser) as browser:
        for target in config.targets:
            print(f"=== Target: {target.name or target.url} ===")
            visitor = PageVisitor(target, browser, config.output)
            page_data_list = await visitor.visit()
            print(f"Captured {len(page_data_list)} pages\n")

            for page_data in page_data_list:
                finding = {
                    "url": page_data["url"],
                    "target_name": target.name,
                    "structured_results": [],
                    "llm_assessment": None,
                }

                for rule in config.rules:
                    if rule.type == "structured":
                        evaluator = StructuredEvaluator(rule)
                        results = evaluator.evaluate(page_data)
                        for r in results:
                            r["rule_name"] = rule.name
                        finding["structured_results"].extend(results)
                        print(f"  Rule '{rule.name}': {sum(1 for r in results if r['passed'])}/{len(results)} checks passed")

                    elif rule.type == "llm":
                        print(f"  Rule '{rule.name}': running LLM assessment...")
                        llm_result = await llm_assessor.assess(rule, page_data, target)
                        finding["llm_assessment"] = llm_result

                all_results.append(finding)

            print()

    # Write reports
    summary = json_reporter._summary(all_results)
    json_reporter.write(config.name, all_results)
    md_reporter.write(config.name, all_results, summary)

    print(f"Reports written:")
    print(f"  JSON:  {config.output.json_output}")
    print(f"  MD:    {config.output.markdown_output}")

def main():
    parser = argparse.ArgumentParser(description="UK Consumer Protection Compliance Auditor")
    subparsers = parser.add_subparsers(dest="command")

    # Audit command
    audit_parser = subparsers.add_parser("audit", help="Run an audit from a config file")
    audit_parser.add_argument("config", help="Path to YAML config file")

    args = parser.parse_args()

    if args.command == "audit":
        asyncio.run(run_audit(args.config))
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
```

**Step 2: Write CLI test** (`tests/test_cli.py`)

```python
import subprocess

def test_cli_help():
    result = subprocess.run(["python", "-m", "consumer_tool.cli", "--help"],
                          capture_output=True, text=True)
    assert result.returncode == 0
    assert "audit" in result.stdout

def test_audit_requires_config():
    result = subprocess.run(["python", "-m", "consumer_tool.cli", "audit"],
                          capture_output=True, text=True)
    assert result.returncode != 0  # Missing required argument
```

**Step 3: Run tests**

```bash
pytest tests/ -v
```

**Step 4: Commit**

```bash
git add consumer_tool/cli.py consumer_tool/__init__.py tests/test_cli.py
git commit -m "cli: add entry point with audit subcommand"
```

---

## Phase 7: Verification & Dry Run

### Task 7.1: Run end-to-end on a test target

**Objective:** Execute a real audit against a test site and verify outputs.

**Step 1: Run the audit**

```bash
python -m consumer_tool.cli audit configs/example-audit.yml
```

Expected output:
- Browser opens (or runs headless) and navigates to the target
- Captures page data
- Evaluates rules
- Writes JSON and Markdown reports

**Step 2: Inspect outputs**

```bash
cat output/results.json | python -m json.tool | head -50
cat output/report.md
```

**Step 3: Commit**

```bash
git add configs/example-audit.yml output/
git commit -m "verify: end-to-end audit run on test target"
```

---

## Future Work (Noted for Later)

### AI-Driven Navigation Enhancement

The navigation engine currently uses a breadth-first traversal with same-domain filtering. Future enhancements could include:

1. **Stagehand integration** — Replace deterministic traversal with AI-driven "go find X" navigation for pages where the path is unknown
2. **Computer Use fallback** — For pages that resist scripted navigation (heavy JS, SPAs), fall back to visual-agent navigation (screenshot → LLM → action)
3. **Intention-based routing** — Each rule could specify navigation "intent" (e.g., "reach checkout") and the engine picks the most efficient path

### Monitoring Mode

Add support for:
- Scheduled/recurring audits
- Change detection between runs (diff captured data over time)
- Alerting when compliance thresholds change
- Historical data storage for trend analysis

### Anti-Bot Measures

If needed:
- Headless detection evasion
- Browser fingerprint randomization
- Proxy rotation
- Request timing randomization

---

## Project Structure

```
consumer_tool/
├── __init__.py
├── cli.py                    # CLI entry point
├── models/
│   ├── __init__.py
│   ├── target.py             # SiteTarget, AuditConfig
│   ├── rule.py               # RuleConfig, StructuredCheck
│   └── config.py             # OutputConfig, BrowserConfig
├── config/
│   ├── __init__.py
│   └── loader.py             # YAML config loader
├── navigator/
│   ├── __init__.py
│   ├── browser.py            # BrowserSession (Playwright wrapper)
│   └── visitor.py            # PageVisitor (traversal logic)
├── assess/
│   ├── __init__.py
│   ├── structured.py         # StructuredEvaluator
│   └── llm.py                # LLMAssessor
├── report/
│   ├── __init__.py
│   ├── json_reporter.py      # JSON output
│   └── md_reporter.py        # Markdown output
├── configs/
│   └── example-audit.yml     # Example configuration
├── output/                   # Generated audit results
└── tests/
    ├── __init__.py
    ├── test_config_loader.py
    ├── test_browser_session.py
    ├── test_structured_evaluator.py
    └── test_cli.py
```
