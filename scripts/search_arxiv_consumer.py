#!/usr/bin/env python3
"""arXiv search for UK Consumer Harms review."""
import sys, xml.etree.ElementTree as ET, urllib.request, json, time, os

queries = [
    ('ti:collusion+AND+ti:algorithmic+OR+ti:pricing+algorithm', 'Algorithmic Collusion / Pricing Algorithms'),
    ('all:consumer+protection+AND+all:large+language+model+OR+all:agent', 'Consumer Protection + LLMs / Agents'),
    ('all:dark+pattern+OR+all:choice+architecture+OR+all:manipulati', 'Dark Patterns / Choice Architecture'),
    ('all:AI+agent+AND+all:consumer+OR+all:pricing', 'AI Agents + Consumer / Pricing'),
    ('all:algorithmic+AND+all:consumer+harm+OR+all:consumer+protection', 'Algorithmic + Consumer Harm'),
    ('all:AI+agent+AND+all:market+AND+all:competition', 'AI Agents + Market Competition'),
    ('all:large+language+model+AND+all:consumer+AND+all:deception+OR+all:sponsored', 'LLMs + Consumer Deception'),
]

all_papers = []
for i, (q, label) in enumerate(queries):
    url = f'https://export.arxiv.org/api/query?search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results=10'
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            raw = resp.read()
        root = ET.fromstring(raw)
        ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
        for entry in root.findall('a:entry', ns):
            title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
            arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1].split('v')[0]
            published = entry.find('a:published', ns).text[:10]
            authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
            summary = entry.find('a:summary', ns).text.strip()[:300]
            cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
            link = entry.find('a:id', ns).text.strip()
            all_papers.append({
                'title': title, 'arxiv_id': arxiv_id, 'published': published,
                'authors': authors, 'abstract': summary, 'categories': cats,
                'url': f'https://arxiv.org/abs/{arxiv_id}',
                'pdf_url': link.replace('/abs/', '/pdf/'),
                'query_source': label
            })
        time.sleep(3.5)
    except Exception as e:
        print(f'  Query {i} ({label}): ERROR {e}', file=sys.stderr)

# Deduplicate by arxiv_id
seen = set()
unique = []
for p in all_papers:
    if p['arxiv_id'] not in seen:
        seen.add(p['arxiv_id'])
        unique.append(p)

unique.sort(key=lambda x: x['published'], reverse=True)

# Output as JSON for easy parsing
print(json.dumps(unique, indent=2))
