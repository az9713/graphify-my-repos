import json, pathlib, re, collections, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

docs = pathlib.Path('az9713-corpus/docs')
names, texts = [], []
for f in sorted(docs.iterdir()):
    t = f.read_text(encoding='utf-8', errors='replace')
    t = re.sub(r'^---.*?^---', ' ', t, flags=re.S | re.M)   # my front matter leaked last time
    t = re.sub(r'```.*?```', ' ', t, flags=re.S)            # code blocks
    t = re.sub(r'<[^>]+>', ' ', t)                          # html/badge markup
    t = re.sub(r'!?\[[^\]]*\]\([^)]*\)', ' ', t)            # md links+images
    t = re.sub(r'https?://\S+', ' ', t)
    t = re.sub(r'\b[\w./-]+\.(md|py|ts|tsx|js|json|html|css|sh|toml|yml|yaml|png|jpg|svg)\b', ' ', t)
    t = re.sub(r'[|`*_#>=\-]{2,}', ' ', t)                  # table/rule chrome
    names.append(f.stem); texts.append(t)

BOILER = ('docs guide guides quickstart getting started overview reference architecture troubleshooting '
          'contributing changelog usage install installation prerequisites requirements getting-started '
          'user developer table contents license mit apache clone cd npm pip uv bun run start dev build '
          'src app index main test tests env key api_key your you your the this that will can then next '
          'step steps note tip warning example examples output input add update version release repo '
          'repository project file files folder directory command commands terminal shell bash '
          'claude code agent agents skill skills anthropic opus sonnet haiku fable model models llm ai').split()

vec = TfidfVectorizer(stop_words='english', max_df=0.30, min_df=5, sublinear_tf=True,
                      ngram_range=(1,2), max_features=40000,
                      token_pattern=r'(?u)\b[a-zA-Z][a-zA-Z\-]{2,}\b')
X = vec.fit_transform(texts)
keep = [i for i, t in enumerate(vec.get_feature_names_out())
        if not any(w in BOILER for w in t.split())]
X = X[:, keep]
terms = vec.get_feature_names_out()[keep]
print('matrix after boilerplate strip:', X.shape)

Xd = TruncatedSVD(n_components=120, random_state=7).fit_transform(X)
Xd = Xd / (np.linalg.norm(Xd, axis=1, keepdims=True) + 1e-9)
for k in [10,12,14,16,18]:
    km = KMeans(k, n_init=10, random_state=7).fit(Xd)
    print(f'  k={k}: silhouette={silhouette_score(Xd, km.labels_):.4f}')

K = 14
km = KMeans(K, n_init=30, random_state=7).fit(Xd); lab = km.labels_
Xa = np.asarray(X.todense())
out = []
print(f'\n=== k={K}, boilerplate removed ===')
for c in range(K):
    idx = np.where(lab == c)[0]
    top = terms[np.argsort(Xa[idx].mean(0) - Xa[np.where(lab != c)[0]].mean(0))[::-1][:9]]
    d = np.linalg.norm(Xd[idx] - km.cluster_centers_[c], axis=1)
    order = idx[np.argsort(d)]
    out.append({'id': int(c), 'size': len(idx), 'terms': list(top),
                'exemplars': [names[i] for i in order[:6]],
                'members': [names[i] for i in order]})
    print(f'\n[{c}] n={len(idx)}\n   terms: {", ".join(top)}\n   repos: {", ".join(names[i] for i in order[:6])}')
json.dump({'k': K, 'clusters': out, 'assign': {names[i]: int(lab[i]) for i in range(len(names))}},
          open('topics.json', 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)
