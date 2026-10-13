import os
import json
from urllib.request import Request,urlopen
from urllib.error import URLError,HTTPError
# Optional Azure OpenAI integration. No keys required for deterministic local mode.
def summarize(question, facts, fallback):
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT","").rstrip("/")
    key=os.getenv("AZURE_OPENAI_API_KEY","")
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT","")
    if not all([endpoint,key,deployment]):return fallback
    version=os.getenv("AZURE_OPENAI_API_VERSION","2024-10-21")
    url=f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={version}"
    messages=[{"role":"system","content":"You are a simulation-only planning assistant. Use only the provided evidence. Never invent sources, routes, operational assurances, or emergency instructions. State uncertainties and require human review."},{"role":"user","content":json.dumps({"question":question,"evidence":facts,"baseline":fallback})}]
    body=json.dumps({"messages":messages,"temperature":0,"max_tokens":450}).encode()
    req=Request(url,data=body,headers={"Content-Type":"application/json","api-key":key})
    try:
        with urlopen(req,timeout=12) as r:
            return json.loads(r.read())["choices"][0]["message"]["content"]
    except (URLError,HTTPError,KeyError,ValueError,TimeoutError):return fallback
