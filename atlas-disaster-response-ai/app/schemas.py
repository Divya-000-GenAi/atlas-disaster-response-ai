from pydantic import BaseModel, Field
from typing import Literal
class Query(BaseModel):
    question: str = Field(min_length=3,max_length=3000)
    region: str = "North Valley"
    incident_type: Literal["flood","wildfire","earthquake","storm"] = "flood"
    severity: int = Field(default=3,ge=1,le=5)
    affected_population: int = Field(default=1000,ge=0)
    rainfall_mm: float = Field(default=80,ge=0)
    wind_kmh: float = Field(default=25,ge=0)
    available_teams: int = Field(default=4,ge=0)
class Decision(BaseModel):
    incident_id: str
    risk_score: float
    risk_level: str
    actions: list[str]
    resources: dict
    answer: str
    citations: list[dict]
    audit: list[str]
    review_required: bool
    evidence_status: str
