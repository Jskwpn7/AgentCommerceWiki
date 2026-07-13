---
type: concept
title: "Provenance Relations for LLM Agents"
category: "AI Systems / Agent Architecture"
date: "2026-06-23"
related_papers:
  - "arxiv-2606.04990v1-evidence-tracing-execution-provenance-llm-agents"
tags:
  - "provenance"
  - "relations"
  - "provenance-graphs"
  - "evidence-tracing"
---

# Provenance Relations for LLM Agents

> Seven typed relation types for connecting evidence and execution units in LLM agent provenance graphs, as defined by Wang et al. (arXiv:2606.04990v1).

## Overview

Traditional provenance models (W3C PROV-DM) provide basic relations: used, wasGeneratedBy, wasDerivedFrom. LLM agents require additional relation types because their executions combine semantic evidence use, tool-mediated actions, memory updates, environment observations, and multi-agent communication.

## Seven Relation Types

### Semantic Evidence Relations

| Relation | Description | Example |
|----------|------------|---------|
| **SUPPORT** | Evidence justifies a claim/answer | A retrieved passage supports an intermediate claim |
| **CONTRADICT** | Units conflict semantically | Memory item conflicts with newly retrieved document |
| **INVALIDATE** | New evidence makes prior assumption/plan/claim no longer usable | Failed API response invalidates planned next action |

### Procedural Execution Relations

| Relation | Description | Example |
|----------|------------|---------|
| **DERIVE** | Transformation or summarization | Memory item derived from previous conversation; claim derived from a table |
| **DEPEND-ON** | Execution dependency | Action depends on tool result; tool call depends on generated parameters |
| **TRIGGER** | Causal/procedural activation | Observation triggers diagnostic tool call; error triggers replanning |
| **UPDATE** | State changes | Memory updates, environment updates, database modifications |

### Base PROV Relations

| Relation | Description |
|----------|------------|
| **USE** | An activity used an entity (W3C PROV-DM compatible) |
| **GENERATE** | An activity generated an entity (W3C PROV-DM compatible) |

## Why Relations Matter

A flat chronological log shows: "document retrieved → tool called → answer produced"

A provenance graph additionally shows: "document **SUPPORTED** one claim, tool output **CONTRADICTED** another, contradiction **INVALIDATED** previous assumption, invalidation **TRIGGERED** recovery step"

This relational structure is what enables provenance to support verification, attribution, debugging, safety enforcement, audit, and recovery.

## Security Relevance

**DEPEND-ON** is particularly important for safety: unsafe actions can arise when tool arguments depend on untrusted or injected content. Tracking dependency chains makes it possible to distinguish trusted from untrusted information flows.

## Related Concepts
- [[Agent Provenance Taxonomy]] — Where these relations fit in the five-dimension framework
- [[Provenance Representation Forms]] — How these relations are instantiated in practice
