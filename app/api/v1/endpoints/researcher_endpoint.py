from fastapi import HTTPException
from pydantic import BaseModel

from app.service.ai.service import run_researcher


class ResearcherRunRequest(BaseModel):
    topic: str


class ResearcherRunResponse(BaseModel):
    topic: str
    research_notes: str
    model_status: dict


def run(request: ResearcherRunRequest) -> ResearcherRunResponse:
    """Pure endpoint logic - no router here. researcher_router.py is what
    wires this into FastAPI."""
    try:
        result, status = run_researcher(request.topic)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    return ResearcherRunResponse(topic=request.topic, research_notes=result, model_status=status)
