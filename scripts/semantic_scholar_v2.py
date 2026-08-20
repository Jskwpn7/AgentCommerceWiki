#!/usr/bin/env python3
"""Find arXiv papers via Semantic Scholar API - consumer harms domain."""
import urllib.request
import json
import time
import urllib.parse

searches = [
    'algorithmic collusion pricing',
    'dark patterns consumer protection',
    'AI agent consumer harm deception',
    'agentic AI consumer protection',
    'algorithmic pricing consumer welfare',
    'LLM consumer deception sponsored',
    'algorithmic consumer harm unfair',
    'automated decision making consumer protection',
    'dark UX manipulation consumer',
    'AI shopping agent consumer welfare',
]

all_papers = []
for i, query in enumerate(searches):
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
                    'abstract': (p.get('abstract', '') or '')[:500],
                    'categories': 'sem-scholar',
                    'url': f'https://arxiv.org/abs/{arxiv_id_clean}',
                    'pdf_url': f'https://arxiv.org/pdf/{arxiv_id_clean}',
                    'query_source': 'sem-scholar',
                    'citationCount': p.get('citationCount', 0),
                })
        time.sleep(1.5)
    except Exception as e:
        print(f'  ERROR: {e}')
        time.sleep(2)

# Deduplicate by arXiv ID
seen = set()
unique = []
for p in all_papers:
    key = p['arxiv_id'].lower().strip()
    if key not in seen:
        seen.add(key)
        unique.append(p)

unique.sort(key=lambda x: x.get('citationCount', 0), reverse=True)
print(json.dumps(unique[:20], indent=2))
print(f'\nTotal unique arXiv papers: {len(unique)}')
