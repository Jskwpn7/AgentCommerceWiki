---
title: "LiteAgent - Open Source Web Agent Evaluation Framework"
created: 2026-08-19
updated: 2026-08-19
type: raw_repo
tags: [web-agent-evaluation, dark-patterns-liteagent-trickyarena, agent-security, open-source]
sources: ["https://github.com/LiteAgent/liteagent"]
confidence: high
---

# LiteAgent — Open Source Web Agent Evaluation Framework

**Source:** https://github.com/LiteAgent/liteagent  
**Repository description:** The Open Source Web Agent Evaluation Framework  

## Repository Overview

LiteAgent is a framework for evaluating web agents (implemented as chrome extensions, CLI tools, or SDKs) against controlled test scenarios. It supports multiple agent implementations and includes built-in instrumentation for testing dark pattern susceptibility via the TrickyArena testbed.

### Supported Agents

The project has pre-instrumented support for:
- BrowserUse
- DoBrowser
- MultiOn (MultiOn/MultiOn)
- Agent E (AgentE/agent-e)
- Skyvern
- WebArena
- VisualWebArena

Each supported agent lives as a git submodule within the main repository.

### Setup

**Requirements:**
- Ubuntu 24.04.2 LTS (tested) or compatible Linux
- Docker (recommended) or conda + Python 3.11 + Playwright
- OpenAI API keys for agent submodules (in `.env` files)

```bash
git clone https://github.com/LiteAgent/liteagent.git
cd liteagent
git submodule update --init --recursive
# Docker approach:
docker compose up --build <agent>
# Or locally:
conda create -n dark python=3.11
conda activate dark
pip install -r requirements.txt
pip install playwright && playwright install
```

### Running Agents

**Prompts are stored in:** `data/prompts/` (`.txt` files, first line = site URL, remaining lines = tasks)

**Runner CLI:** `./run.sh <agent>` — interactive prompt directory selection  
**Direct module call:** `python main.py <agent> --site <url> --task <prompt> --site-category <category> --timeout 180`

### Output Structure

All data stored in `data/db/<agent>/<category>/<task_name>/`:
- `<task_name>_commands.py` — agent commands
- `<task_name>.db` — SQLite event log
- `<task_name>_site.txt` — target site URL
- `<task_name>_task.txt` — task description
- `html/` — captured HTML snapshots
- `reasoning/` — agent reasoning traces
- `rrweb/` — rrweb replay events + viewer
- `scratchpad.txt` — agent scratchpad
- `trace/<task_name>_trace.zip` — execution trace
- `video/<task_name>.mp4` — video recording of agent run

### Event Database Schema

```sql
CREATE TABLE <task_name> (
    id INTEGER NOT NULL,
    event_type VARCHAR(50) NOT NULL,
    xpath VARCHAR(250),
    class_name VARCHAR(250),
    element_id VARCHAR(250),
    input_value VARCHAR(250),
    url VARCHAR(500),
    additional_info VARCHAR(500),
    time_since_last_action FLOAT,
    PRIMARY KEY (id)
)
```

### TrickyArena Testbed

- **URL:** https://agenttrickydps.vercel.app/
- **Purpose:** Controlled test environment for dark pattern vulnerability testing
- **Usage:** Toggle on/off specific dark patterns via query parameters (e.g., `?dp=bs_da_hc_md`)
- **Dark patterns as unintentional indirect prompt injection** (OWASP LLM01)

### Evaluation Suite

Located in `evaluation/` directory:

- `python -m evaluation.checkers.custom_checker <path>` — checks if agent completed task and was susceptible to dark patterns
- `python -m evaluation.data_transforms.transform_custom_data` — exports results to CSV at `numbers/custom_comparison_results.csv`
- `evaluation/tables_and_figures/single_mult_eval_runner.py` — generates tables/graphs for single and multiple DP experiments

### Analysis Capabilities

- Task Success Rate (TSR) — percentage of successful task completions
- Dark Pattern Susceptibility Rate (DPSR) — percentage of times agents fall for dark patterns
- Confusion Matrix: Deception-Task Outcomes (Evaded Failure, Evaded Completion, Deceived Failure, Deceived Completion)
- Fine-grained and coarse-grained analysis per DP/task/website
- Ablation studies on dark pattern attributes and observation modalities
- Countermeasure analysis (prompt-based)

### Website Source Code

Testbed sites in `sites/react-testbed`. Deploy locally:
```bash
cd sites/react-testbed
yarn && yarn dev
```
