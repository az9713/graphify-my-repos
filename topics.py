import json, pathlib, re, collections, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

docs_dir = pathlib.Path('az9713-corpus/docs')
names, texts = [], []
for f in sorted(docs_dir.iterdir()):
    t = f.read_text(encoding='utf-8', errors='replace')
    t = re.sub(r'```.*?```', ' ', t, flags=re.S)          # drop code blocks
    t = re.sub(r'https?://\S+|!\[[^\]]*\]|\|', ' ', t)     # urls, images, tables
    names.append(f.stem); texts.append(t)

# ponytail: these are in ~every repo, they only add noise to the topic model
STOP = 'claude code agent agents skill skills repo repository docs doc documentation project run running use used using build built builds file files md http com github io www new like just make makes made get gets set sets one two also see https readme license mit install setup npm python pip node js ts src main index test tests example examples output input add added update updated version'.split()

vec = TfidfVectorizer(stop_words=list(set(STOP)) + ['english'], max_df=0.35, min_df=4,
                      sublinear_tf=True, ngram_range=(1,2), max_features=40000,
                      token_pattern=r'(?u)\b[a-zA-Z][a-zA-Z\-\.]{2,}\b')
X = vec.fit_transform(texts)
X = TfidfVectorizer(stop_words='english', max_df=0.35, min_df=4, sublinear_tf=True,
                    ngram_range=(1,2), max_features=40000,
                    token_pattern=r'(?u)\b[a-zA-Z][a-zA-Z\-\.]{2,}\b').fit_transform(texts)
print('tf-idf matrix:', X.shape)

Xd = TruncatedSVD(n_components=120, random_state=7).fit_transform(X)
Xd = Xd / (np.linalg.norm(Xd, axis=1, keepdims=True) + 1e-9)

for k in [8,10,12,14,16,18,20]:
    km = KMeans(k, n_init=8, random_state=7).fit(Xd)
    print(f'  k={k}: silhouette={silhouette_score(Xd, km.labels_):.4f}  '
          f'sizes={sorted(collections.Counter(km.labels_).values(), reverse=True)}')

K = 14
km = KMeans(K, n_init=25, random_state=7).fit(Xd)
lab = km.labels_
terms = np.array(TfidfVectorizer(stop_words='english', max_df=0.35, min_df=4, sublinear_tf=True,
        ngram_range=(1,2), max_features=40000,
        token_pattern=r'(?u)\b[a-zA-Z][a-zA-Z\-\.]{2,}\b').fit(texts).get_feature_names_out())
Xa = np.asarray(X.todense())
print(f'\n=== k={K} CLUSTERS: distinctive terms + closest repos ===')
info=[]
for c in range(K):
    idx = np.where(lab==c)[0]
    mean_in = Xa[idx].mean(0); mean_out = Xa[np.where(lab!=c)[0]].mean(0)
    top = terms[np.argsort(mean_in - mean_out)[::-1][:10]]
    d = np.linalg.norm(Xd[idx] - km.cluster_centers_[c], axis=1)
    reps = [names[i] for i in idx[np.argsort(d)[:6]]]
    info.append({'id':int(c),'size':len(idx),'terms':list(top),'exemplars':reps,
                 'members':[names[i] for i in idx]})
    print(f'\n[{c}] n={len(idx)}')
    print('   terms: ' + ', '.join(top))
    print('   repos: ' + ', '.join(reps))
json.dump({'k':K,'clusters':info,'assign':{names[i]:int(lab[i]) for i in range(len(names))}},
          open('topics.json','w',encoding='utf-8'),
          indent=1, ensure_ascii=False)
