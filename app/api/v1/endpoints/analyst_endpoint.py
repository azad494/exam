from fastapi import HTTPException
from pydantic import BaseModel

from app.service.ai.service import run_analyst


class AnalystRunRequest(BaseModel):
    topic: str
    research_notes: str


class AnalystRunResponse(BaseModel):
    topic: str
    insights: str
    model_status: dict


def run(request: AnalystRunRequest) -> AnalystRunResponse:
    """Pure endpoint logic - no router here. analyst_router.py is what
    wires this into FastAPI."""
    try:
        result, status = run_analyst(request.topic, request.research_notes)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    return AnalystRunResponse(topic=request.topic, insights=result, model_status=status)
