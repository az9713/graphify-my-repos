import json, collections, re
B=''   # run from the repo root
T=json.load(open(B+'topics.json',encoding='utf-8'))
A=json.load(open(B+'graphify-out/atlas2.json',encoding='utf-8'))
R={r['name']:r for r in json.load(open(B+'az9713-corpus/repos.json',encoding='utf-8'))}

NAMES={0:'UI & Canvas Design',1:'Coding-Agent Harness Forks',2:'Documentation Packages',
 3:'Mixed: Plugins, ML & Playbooks',4:'Gemini Media & Extraction',5:'Chat Bridges & Agent Memory',
 6:'Physics & Math Explainers',7:'AI Film & Media Pipelines',8:'Claude Code Workflows & Hooks',
 9:'Trading & Quant',10:'HTML Course & Lecture Builds',11:'Agent Runtime & Instrumentation',
 12:'Gemini Studio Deploys',13:'Knowledge Graphs & Vaults'}
VAGUE={2,3,11}   # clusters whose top terms are generic, not a subject

gd={r['repo']:r for r in A['repos']}
def deriv(r):
    t=((r.get('description') or '')+' '+r['name']).lower()
    return bool(r['fork'] or re.search(r'clone of|fork of|port of|tutorial',t))

rows=[]
for name,cid in T['assign'].items():
    m=R[name]; g=gd.get(name,{})
    rows.append({'repo':name,'cluster':cid,'cluster_name':NAMES[cid],
        'stars':m['stargazers_count'],'language':m['language'],'kb':m['size'],
        'created':m['created_at'][:10],'updated':m['updated_at'][:10],
        'derivative':deriv(m),'topics':len(m['topics'] or []),
        'homepage':bool(m['homepage']),'desc':m['description'] or '',
        'neighbors':g.get('neighbors',0),'betweenness':g.get('betweenness',0),
        'tool_cluster':g.get('fine_community'),'in_graph':name in gd})

cl=[]
for c in T['clusters']:
    mem=[r for r in rows if r['cluster']==c['id']]
    cl.append({'id':c['id'],'name':NAMES[c['id']],'size':len(mem),'terms':c['terms'],
        'exemplars':c['exemplars'],'stars':sum(r['stars'] for r in mem),
        'derivative':sum(1 for r in mem if r['derivative']),
        'vague':c['id'] in VAGUE,
        'median_neighbors':sorted(r['neighbors'] for r in mem)[len(mem)//2]})
cl.sort(key=lambda x:-x['size'])

orphans=sorted([r for r in rows if r['neighbors']<=1],key=lambda r:(r['neighbors'],-r['kb']))
bridges=sorted(rows,key=lambda r:-r['betweenness'])[:15]
hubs=sorted(rows,key=lambda r:-r['neighbors'])[:15]

summary={'total':len(rows),'in_graph':sum(1 for r in rows if r['in_graph']),
 'zero_star':sum(1 for r in rows if r['stars']==0),
 'with_topics':sum(1 for r in rows if r['topics']),
 'with_homepage':sum(1 for r in rows if r['homepage']),
 'derivative':sum(1 for r in rows if r['derivative']),
 'orphan_count':len(orphans),
 'graph_nodes':1569,'graph_edges':2868,'concepts':544,
 'concepts_degree1':331,'tool_communities':146,
 'extraction_tokens':3366498}
json.dump({'summary':summary,'clusters':cl,'repos':rows,'orphans':orphans[:40],
  'bridges':bridges,'hubs':hubs}, open(B+'atlas-data.json','w',encoding='utf-8'),
  indent=1,ensure_ascii=False)

print('CLUSTERS'); 
for c in cl: print(f"  {c['size']:>3} {'~' if c['vague'] else ' '} {c['name']:<34} {c['stars']:>3}★  deriv={c['derivative']}")
print(f"\norphans(<=1 neighbor): {len(orphans)}")
print('  '+', '.join(r['repo'] for r in orphans[:12]))
print('\nTOP BRIDGES:', ', '.join(r['repo'] for r in bridges[:8]))
print('TOP HUBS:   ', ', '.join(f"{r['repo']}({r['neighbors']})" for r in hubs[:8]))
print('\nsummary:',json.dumps(summary))
