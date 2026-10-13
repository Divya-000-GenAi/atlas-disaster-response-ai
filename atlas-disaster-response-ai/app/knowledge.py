from pathlib import Path
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
DATA=Path(__file__).resolve().parents[1]/"data"/"knowledge.json"
class KnowledgeBase:
    def __init__(self, path=DATA):
        self.docs=json.loads(Path(path).read_text(encoding="utf-8"))
        self.vec=TfidfVectorizer(ngram_range=(1,2),stop_words="english")
        self.matrix=self.vec.fit_transform([d["text"] for d in self.docs])
    def search(self, query, kind=None, k=4):
        q=self.vec.transform([query]); scores=cosine_similarity(q,self.matrix)[0]
        hits=[(float(scores[i]),d) for i,d in enumerate(self.docs) if not kind or d["kind"]==kind]
        return [{**d,"score":round(score,4)} for score,d in sorted(hits,key=lambda x:x[0],reverse=True)[:k] if score>0]
