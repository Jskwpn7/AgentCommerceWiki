#!/usr/bin/env python3
"""arXiv search for UK Consumer Harms review."""
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import time

queries = [
    ('ti:collusion+AND+ti:algorithmic+OR+ti:pricing+algorithm', 'Algorithmic Collusion'),
    ('all:consumer+protection+AND+all:agent', 'Consumer Protection + Agent'),
    ('all:dark+pattern+OR+all:choice+architecture', 'Dark Patterns'),
    ('all:AI+agent+AND+all:consumer', 'AI Agents + Consumer'),
    ('all:algorithmic+AND+all:"consumer+harm"', 'Algorithmic + Consumer Harm'),
    ('all:"large+language+model"+AND+all:consumer', 'LLM + Consumer'),
]

all_papers = []
for i, (q, label) in enumerate(queries):
    q_enc = urllib.parse.quote(q, safe='+')
    url = f'https://export.arxiv.org/api/query?search_query={q_enc}&sortBy=submittedDate&sortOrder=descending&max_results=5'
    try:
        print(f'Query {i+1}/{len(queries)}: {label}...', flush=True)
        with urllib.request.urlopen(url, timeout=20) as resp:
            raw = resp.read()
        root = ET.fromstring(raw)
        ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
        count = 0
        for entry in root.findall('a:entry', ns):
            title = entry.find('a:title', ns)
            arxiv_id_el = entry.find('a:id', ns)
            published = entry.find('a:published', ns)
            summary = entry.find('a:summary', ns)
            if all(e is not None for e in [title, arxiv_id_el, published, summary]):
                t = title.text.strip().replace('\n', ' ')
                aid = arxiv_id_el.text.strip().split('/abs/')[-1].split('v')[0]
                pub = published.text[:10]
                s = summary.text.strip()[:300]
                cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
                authors_e = entry.findall('a:author', ns)
                authors = ', '.join(
                    ae.find('a:name', ns).text if ae.find('a:name', ns) is not None else '?'
                    for ae in authors_e
                )
                all_papers.append({
                    'title': t, 'arxiv_id': aid, 'published': pub,
                    'authors': authors, 'abstract': s, 'categories': cats,
                    'url': f'https://arxiv.org/abs/{aid}',
                    'pdf_url': arxiv_id_el.text.strip().replace('/abs/', '/pdf/'),
                    'query_source': label
                })
                count += 1
        print(f'  Found {count} papers')
        time.sleep(5)
    except Exception as e:
        print(f'  ERROR: {e}')
        time.sleep(6)

seen = set()
unique = []
for p in all_papers:
    if p['arxiv_id'] not in seen:
        seen.add(p['arxiv_id'])
        unique.append(p)

unique.sort(key=lambda x: x['published'], reverse=True)
print(json.dumps(unique, indent=2))
