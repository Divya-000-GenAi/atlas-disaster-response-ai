# Atlas Crisis Intelligence — Agentic AI Decision-Support Simulator

> **IMPORTANT:** This is a synthetic educational/portfolio project. It is **NOT** connected to real incidents, sensors, emergency agencies, dispatch systems, or official routing. **Never use it to make real emergency decisions.** Every proposed action requires qualified human review.

## What it does

A multi-stage **agent-style workflow** analyzes a simulated natural-disaster planning question. It retrieves relevant evidence from local knowledge documents using TF-IDF semantic-like lexical similarity, predicts a **synthetic** scenario risk score with Random Forest, proposes simulated resource allocations and a toy network route, and creates an evidence-cited draft response. Optional Azure OpenAI can rewrite the draft. It has a FastAPI service, Streamlit UI, automated tests, Docker, and CI.

## Architecture

`User -> FastAPI/Pydantic -> Guardrails -> Supervisor workflow -> [Retrieval Agent | Risk ML Agent | Resource Tool] -> Response Agent (optional Azure OpenAI) -> Human Review -> JSON + Audit Trace`

**Implementation accuracy:** The modules are Python functions organized as agents; **LangGraph, MCP, vector databases, Azure Blob Storage, Kubernetes, and live data integrations are not implemented** in this version. TF-IDF is not embedding-based vector search. The model uses synthetic training data and is not validated for real-world risk forecasting.

## Project structure

```
app/main.py          FastAPI endpoints
app/schemas.py       Validated request/response contracts
app/agents.py        Multi-stage supervisor workflow
app/knowledge.py     TF-IDF evidence retrieval
app/risk.py          Synthetic Random Forest scoring
app/tools.py         Simulated resource and road tools
app/guards.py        Basic prompt pattern checks
app/llm.py           Optional Azure OpenAI completion
app/__init__.py
dashboard.py         Streamlit demo UI
data/knowledge.json  Sample knowledge base
data/sample_request.json
 tests/test_api.py    API tests
Dockerfile
.github/workflows/ci.yml
```

## Run on Windows (Python 3.11+)

Extract the ZIP. Open CMD inside `atlas-disaster-response-ai` and run:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open **http://127.0.0.1:8000/docs** and use `POST /analyze` with `data/sample_request.json`.

In a **second** terminal, activate the environment and run:

```cmd
streamlit run dashboard.py
```

Streamlit will display a local URL, usually http://localhost:8501.

## Test

```cmd
python -m pytest -q
```

## Docker

```bash
docker build -t atlas-crisis-ai .
docker run --rm -p 8000:8000 atlas-crisis-ai
```

## Optional Azure OpenAI

Set environment variables from `.env.example` in your shell (the app does not automatically load `.env`): `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_DEPLOYMENT`, and optionally `AZURE_OPENAI_API_VERSION`. Without these, the project produces deterministic local draft reports. **Do not commit actual credentials.** Azure output must still be reviewed.

## Example API request

```json
{"question":"What flood shelter preparations should be reviewed?","region":"North Valley","incident_type":"flood","severity":4,"affected_population":2500,"rainfall_mm":130,"wind_kmh":20,"available_teams":5}
```

## Future extensions (not implemented)

- Replace TF-IDF with Azure OpenAI embeddings + FAISS/Qdrant hybrid search and reranking.
- Use LangGraph supervisor-worker state graph, memory, MCP tool contracts and HITL approval checkpoints.
- Add geospatial live feeds only with authorization, provenance, strict latency/quality SLAs, and professional validation.
- Add SQL persistence, ML drift monitoring, evaluation suites (Recall@K, groundedness), and Kubernetes deployment.

## Ethical use

All locations, roads, incidents, and resources are fictional. No live alerts or dispatch. Rule-based prompt checks are illustrative, not a comprehensive security defense.
