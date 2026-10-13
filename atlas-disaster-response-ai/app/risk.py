import numpy as np
from sklearn.ensemble import RandomForestRegressor
from functools import lru_cache
@lru_cache(maxsize=1)
def model():
    # Reproducible SYNTHETIC training data. Scores are demonstrations, not calibrated forecasts.
    rng=np.random.default_rng(42); X=np.column_stack([rng.integers(1,6,600),rng.integers(0,20001,600),rng.uniform(0,350,600),rng.uniform(0,130,600),rng.integers(0,25,600)])
    y=np.clip(8*X[:,0]+.0015*X[:,1]+.065*X[:,2]+.10*X[:,3]-1.1*X[:,4]+rng.normal(0,3,600),0,100)
    return RandomForestRegressor(n_estimators=70,max_depth=9,random_state=42).fit(X,y)
def score(q):
    X=[[q.severity,q.affected_population,q.rainfall_mm,q.wind_kmh,q.available_teams]]
    s=round(float(np.clip(model().predict(X)[0],0,100)),1)
    return s, "critical" if s>=75 else "high" if s>=55 else "moderate" if s>=30 else "low"
