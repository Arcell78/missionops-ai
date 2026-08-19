from typing import Literal
from pydantic import BaseModel, Field

class IncidentTriage(BaseModel):
    category: Literal[
        "availability", "performance", "security",
        "deployment", "database", "network", "unknown",
    ]
    severity: Literal["low", "medium", "high", "critical"]
    escalation_required: bool
    recommended_action: Literal[
        "investigate", "monitor", "escalate", "request_more_information",
    ]
    rationale: str = Field(
        description="Concise explanation grounded only in the supplied incident."
    )
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="Confidence in the triage decision from 0.0 to 1.0.",
    )
    missing_information: list[str] = Field(
        default_factory=list,
        description="Information that would materially improve triage confidence.",
    )
