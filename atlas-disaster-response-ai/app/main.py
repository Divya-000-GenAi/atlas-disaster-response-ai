from fastapi import FastAPI
from app.schemas import Query,Decision
from app.agents import run
app=FastAPI(title="Atlas Crisis Intelligence | Synthetic Demo",version="1.0.0",description="Research/portfolio simulation. NOT an emergency response system.")
@app.get("/")
def home():return {"project":"Atlas Crisis Intelligence","notice":"SIMULATION ONLY - do not use for real emergency decisions","docs":"/docs"}
@app.get("/health")
def health():return {"status":"ok"}
@app.post("/analyze",response_model=Decision)
def analyze(q:Query):return run(q)
