import json, collections, math, itertools
import networkx as nx
from networkx.algorithms.community import louvain_communities

G = json.load(open('graph.json', encoding='utf-8'))
nodes = {n['id']: n for n in G['nodes']}
repo_ids = {x['node_id'] for x in json.load(open('atlas.json',encoding='utf-8'))['repos'] if x.get('in_graph')}

# concept -> set(repos)
c2r = collections.defaultdict(set)
for e in G['links']:
    s, t = e['source'], e['target']
    for a, b in ((s, t), (t, s)):
        if a in repo_ids and b.startswith('concept_'):
            c2r[b].add(a)

# Newman-weighted repo-repo projection: hub concepts (Claude Code, Python) contribute little
W = collections.Counter()
for c, rs in c2r.items():
    k = len(rs)
    if k < 2 or k > 120:            # ponytail: drop universal concepts outright, they carry no signal
        continue
    w = 1.0 / (k - 1)
    for a, b in itertools.combinations(sorted(rs), 2):
        W[(a, b)] += w

P = nx.Graph()
P.add_nodes_from(repo_ids)
for (a, b), w in W.items():
    if w > 0.02:                    # ponytail: prune hairball edges, keeps Louvain stable
        P.add_edge(a, b, weight=w)

print(f'projection: {P.number_of_nodes()} repos, {P.number_of_edges()} edges')
print(f'isolated:   {sum(1 for n in P if P.degree(n)==0)}')

# tune resolution to land in 8-16 communities
best = None
for res in [0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.5]:
    comms = louvain_communities(P, weight='weight', resolution=res, seed=7)
    big = [c for c in comms if len(c) >= 5]
    print(f'  res={res}: {len(comms)} comms, {len(big)} with >=5 members, largest={max(len(c) for c in comms)}')
    if 8 <= len(big) <= 16 and best is None:
        best = (res, comms)
res, comms = best or (0.6, louvain_communities(P, weight='weight', resolution=0.6, seed=7))
print(f'\nCHOSEN resolution={res}')

comms = sorted(comms, key=len, reverse=True)
r2c = {r: i for i, c in enumerate(comms) for r in c}

# distinctive concept labels: overrepresented in cluster vs corpus
r2concepts = collections.defaultdict(set)
for c, rs in c2r.items():
    for r in rs: r2concepts[r].add(c)
N = len(repo_ids)
gfreq = {c: len(rs)/N for c, rs in c2r.items()}
labels = []
for i, c in enumerate(comms):
    cnt = collections.Counter()
    for r in c: cnt.update(r2concepts[r])
    scored = []
    for con, k in cnt.items():
        if k < 2: continue
        lift = (k/len(c)) / max(gfreq[con], 1e-9)
        scored.append((lift * math.log(1+k), nodes[con]['label'], k))
    scored.sort(reverse=True)
    labels.append([s[1] for s in scored[:6]])

deg = dict(P.degree(weight='weight'))
btw = nx.betweenness_centrality(P, k=min(180, P.number_of_nodes()), weight=None, seed=7)

atlas_old = {x['repo']: x for x in json.load(open('atlas.json', encoding='utf-8'))['repos']}
out = {'resolution': res, 'communities': [], 'repos': []}
for i, c in enumerate(comms):
    out['communities'].append({'id': i, 'size': len(c), 'concepts': labels[i],
        'members': sorted(nodes[r]['label'] for r in c)})
for r in sorted(repo_ids, key=lambda x: nodes[x]['label']):
    name = nodes[r]['label']; meta = atlas_old.get(name, {})
    out['repos'].append({'repo': name, 'community': r2c.get(r, -1),
        'degree': round(deg.get(r, 0), 3), 'neighbors': P.degree(r),
        'betweenness': round(btw.get(r, 0), 5),
        'stars': meta.get('stars', 0), 'language': meta.get('language'),
        'is_fork': meta.get('is_fork', False), 'created': meta.get('created'),
        'fine_community': meta.get('community_label')})
json.dump(out, open('atlas2.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

print(f'\n{len(comms)} communities')
for i, c in enumerate(comms):
    if len(c) >= 4:
        print(f'  [{i:>2}] n={len(c):<3} {", ".join(labels[i][:4])}')
