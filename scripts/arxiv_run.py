#!/usr/bin/env python3
import urllib.request, xml.etree.ElementTree as ET, json, time
queries = [
    ('ti:algorithmic+collusion', 'Algorithmic Collusion'),
    ('all:dark+pattern', 'Dark Patterns'),
    ('all:AI+agent+consumer', 'AI Agent Consumer'),
    ('all:algorithmic+pricing', 'Algorithmic Pricing'),
    ('cat:cs.CY+AND+all:consumer', 'CS Cyber + Consumer'),
    ('cat:cs.AI+AND+all:consumer', 'CS AI + Consumer'),
    ('all:agentic+AI+consumer', 'Agentic AI Consumer'),
    ('all:"consumer+harm"+algorithms', 'Consumer Harm'),
]
all_papers = []
for i, (q, label) in enumerate(queries):
    url = f'https://export.arxiv.org/api/query?search_query={q}&sortBy=submittedDate&sortOrder=descending&max_results=3'
    try:
        print(f'Q{i+1}: {label}', flush=True)
        with urllib.request.urlopen(url, timeout=30) as resp:
            raw = resp.read()
        root = ET.fromstring(raw)
        ns = {'a': 'http://www.w3.org/2005/Atom'}
        for entry in root.findall('a:entry', ns):
            t = entry.find('a:title', ns).text.strip().replace('\n', ' ')
            aid = entry.find('a:id', ns).text.strip().split('/abs/')[-1].split('v')[0]
            pub = entry.find('a:published', ns).text[:10]
            s = entry.find('a:summary', ns).text.strip()[:400]
            cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
            authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
            all_papers.append({'title': t, 'arxiv_id': aid, 'published': pub, 'authors': authors, 'abstract': s, 'categories': cats, 'url': f'https://arxiv.org/abs/{aid}', 'pdf_url': entry.find('a:id', ns).text.strip().replace('/abs/', '/pdf/'), 'query_source': label})
        time.sleep(10)
    except Exception as e:
        print(f'  ERR: {e} (waiting 12s)', flush=True)
        time.sleep(12)
seen = set()
unique = [p for p in all_papers if not (p['arxiv_id'] in seen or seen.add(p['arxiv_id']) or False)]
unique.sort(key=lambda x: x['published'], reverse=True)
print(json.dumps(unique, indent=2))
