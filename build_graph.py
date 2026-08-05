"""Repo-repo projection -> self-contained graph.html (force-graph, Obsidian-style).

Same recipe as buzz_me/buzz-tutorial/audit/graph: slim payload + inlined lib + template.
Projection rules copied from recluster.py so the picture matches the clustering.
"""
import json, collections, itertools

OUT = 'graphify-out/'
G = json.load(open(OUT + 'graph.json', encoding='utf-8'))
label = {n['id']: n['label'] for n in G['nodes']}
repo_ids = {x['node_id'] for x in json.load(open(OUT + 'atlas.json', encoding='utf-8'))['repos']
            if x.get('in_graph')}

# concept -> set(repos)
c2r = collections.defaultdict(set)
for e in G['links']:
    for a, b in ((e['source'], e['target']), (e['target'], e['source'])):
        if a in repo_ids and b.startswith('concept_'):
            c2r[b].add(a)

# Newman-weighted projection; hub concepts dropped (see recluster.py)
W = collections.Counter()
for c, rs in c2r.items():
    k = len(rs)
    if 2 <= k <= 120:
        w = 1.0 / (k - 1)
        for a, b in itertools.combinations(sorted(rs), 2):
            W[(a, b)] += w
edges = [(a, b, w) for (a, b), w in W.items() if w > 0.02]

# ponytail: keep each repo's 6 strongest ties only — the full 7.5k-edge projection
# lays out as one ball. Raise K if the picture looks too sparse.
K = 6
top = collections.defaultdict(list)
for a, b, w in edges:
    top[a].append((w, a, b))
    top[b].append((w, a, b))
keep = {(a, b) for v in top.values() for _, a, b in sorted(v, reverse=True)[:K]}
edges = [(a, b, w) for a, b, w in edges if (a, b) in keep]

atlas = json.load(open('atlas-data.json', encoding='utf-8'))
meta = {r['repo']: r for r in atlas['repos']}
cname = {c['id']: c['name'] for c in atlas['clusters']}
# second coloring: the concept graph's own Louvain communities (recluster.py output)
lou = {r['repo']: r['community'] for r in json.load(open(OUT + 'atlas2.json', encoding='utf-8'))['repos']}

deg = collections.Counter()
for a, b, _ in edges:
    deg[a] += 1
    deg[b] += 1

nodes, seen = [], set()
for rid in sorted(repo_ids, key=lambda x: label[x]):
    m = meta.get(label[rid])
    if not m:
        continue
    seen.add(rid)
    nodes.append({'id': label[rid], 'label': label[rid], 'c': m['cluster'],
                  'cn': cname.get(m['cluster'], '?'), 'g': lou.get(label[rid], -1),
                  's': m['stars'], 'lang': m['language'] or '', 'd': deg[rid]})
links = [{'s': label[a], 't': label[b], 'w': round(w, 3)}
         for a, b, w in edges if a in seen and b in seen]

data = json.dumps({'nodes': nodes, 'links': links, 'clusters': atlas['clusters']},
                  separators=(',', ':')).replace('</', '<\\/')
lib = open('force-graph.min.js', encoding='utf-8').read().replace('</', '<\\/')
html = open('graph-template.html', encoding='utf-8').read()
open('graph.html', 'w', encoding='utf-8').write(
    html.replace('__DATA__', data).replace('__LIB__', lib))
print(f'graph.html: {len(nodes)} repos, {len(links)} edges, '
      f'{sum(1 for n in nodes if n["d"] == 0)} orphans')
