from fastapi import HTTPException
from pydantic import BaseModel

from app.service.ai.service import run_writer


class WriterRunRequest(BaseModel):
    topic: str
    insights: str


class WriterRunResponse(BaseModel):
    topic: str
    article: str
    model_status: dict


def run(request: WriterRunRequest) -> WriterRunResponse:
    """Pure endpoint logic - no router here. writer_router.py is what
    wires this into FastAPI."""
    try:
        result, status = run_writer(request.topic, request.insights)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    return WriterRunResponse(topic=request.topic, article=result, model_status=status)
