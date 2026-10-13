from uuid import uuid4
from app.knowledge import KnowledgeBase
from app.risk import score
from app.tools import allocate
from app.guards import validate_prompt,safe_excerpt
from app.llm import summarize
from app.schemas import Decision
kb=KnowledgeBase()
def run(q):
    audit=["supervisor: validated incident schema"]
    if not validate_prompt(q.question):
        audit.append("guardrail: blocked suspicious instruction")
        return Decision(incident_id=str(uuid4()),risk_score=0,risk_level="blocked",actions=[],resources={},answer="Request blocked by prompt safety policy.",citations=[],audit=audit,review_required=True,evidence_status="blocked")
    risk,level=score(q);audit.append("risk_agent: synthetic ML risk estimated")
    docs=kb.search(f"{q.incident_type} {q.question} {q.region}",k=4)
    audit.append(f"retrieval_agent: {len(docs)} matching knowledge records")
    citations=[{"id":d["id"],"title":d["title"],"score":d["score"]} for d in docs]
    resources=allocate(q,level);audit.append("resource_agent: simulated allocation calculated")
    actions=[]
    if docs: actions=[safe_excerpt(d["text"],160) for d in docs[:3]]
    else: actions=["No matching local guidance found. Request qualified human review."]
    fallback=(f"SIMULATION ONLY: {q.incident_type} scenario for {q.region}. "
              f"Synthetic model risk {risk}/100 ({level}). "
              f"Suggested review items: {'; '.join(actions)} "
              "No live sensors, dispatch systems, or verified field conditions are connected. "
              "A qualified emergency coordinator must approve any operational decision.")
    answer=summarize(q.question,{"citations":citations,"actions":actions,"risk":risk},fallback)
    audit.append("response_agent: grounded response drafted")
    return Decision(incident_id=str(uuid4()),risk_score=risk,risk_level=level,actions=actions,resources=resources,answer=answer,citations=citations,audit=audit,review_required=True,evidence_status="retrieved" if docs else "insufficient")
