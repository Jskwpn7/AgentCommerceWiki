#!/usr/bin/env python3
"""Find arXiv papers via Semantic Scholar API - consumer harms domain."""
import urllib.request
import urllib.parse
import json
import time

# Use Semantic Scholar paper search as proxy for arXiv discovery
searches = [
    ('algorithmic collusion pricing', 'Algorithmic Collusion'),
    ('dark patterns consumer protection', 'Dark Patterns'),
    ('AI agent consumer harm deception', 'AI Agent Consumer Harm'),
    ('agentic AI consumer protection', 'Agentic AI'),
    ('algorithmic pricing consumer welfare', 'Algorithmic Pricing'),
    ('LLM consumer deception sponsored', 'LLM Deception'),
    ('algorithmic consumer harm unfair', 'Algorithmic Consumer Harm'),
    ('automated decision making consumer protection', 'Automated Decision Consumer'),
    ('dark UX manipulation consumer', 'Dark UX'),
    ('AI shopping agent consumer welfare', 'AI Shopping Agent'),
]

all_papers = []
for i, (query, label) in enumerate(searches):
    query_enc = urllib.parse.quote(query, safe='')
    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query_enc}&limit=5&fields=title,authors,year,abstract,citationCount,externalIds'
    try:
        print(f'Search {i+1}/{len(searches)}: {query}...', flush=True)
        with urllib.request.urlopen(url, timeout=20) as resp:
            data = json.loads(resp.read())
        papers = data.get('data', [])
        for p in papers:
            ext = p.get('externalIds', {})
            arxiv_id = ext.get('ArXiv', None)
            if arxiv_id:
                arxiv_id_clean = arxiv_id.split('v')[0]
                all_papers.append({
                    'title': p.get('title', ''),
                    'arxiv_id': arxiv_id_clean,
                    'published': f"{p.get('year', '?')}-??-??",
                    'authors': ', '.join(a.get('name', '?') for a in p.get('authors', [])),
                    'abstract': p.get('abstract', '')[:400] or 'No abstract available',
                    'categories': label,
                    'url': f'https://arxiv.org/abs/{arxiv_id_clean}',
                    'pdf_url': f'https://arxiv.org/pdf/{arxiv_id_clean}',
                    'query_source': label,
                    'citationCount': p.get('citationCount', 0),
                })
            elif p.get('title'):
                all_papers.append({
                    'title': p.get('title', ''),
                    'arxiv_id': 'SEM-' + str(len(all_papers)),
                    'published': f"{p.get('year', '?')}-??-??",
                    'authors': ', '.join(a.get('name', '?') for a in p.get('authors', [])),
                    'abstract': p.get('abstract', '')[:400] or 'No abstract available',
                    'categories': label,
                    'url': p.get('url', ''),
                    'pdf_url': p.get('url', ''),
                    'query_source': label,
                    'citationCount': p.get('citationCount', 0),
                    'is_semantic_scholar_only': True,
                })
        time.sleep(1.5)
    except Exception as e:
        print(f'  ERROR: {e}')
        time.sleep(2)

# Deduplicate by title
seen = set()
unique = []
for p in all_papers:
    key = p['title'].lower().strip()
    if key not in seen:
        seen.add(key)
        unique.append(p)

unique.sort(key=lambda x: x.get('citationCount', 0), reverse=True)
print(json.dumps(unique[:20], indent=2))
print(f'\nTotal unique: {len(unique)}')
