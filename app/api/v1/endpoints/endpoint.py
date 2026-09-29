from fastapi import APIRouter
from pydantic import BaseModel

from app.service.service import run_crew

router = APIRouter()


class CrewRunRequest(BaseModel):
    topic: str


class CrewRunResponse(BaseModel):
    topic: str
    result: str


@router.post("/run", response_model=CrewRunResponse)
def run(request: CrewRunRequest) -> CrewRunResponse:
    """Thin on purpose: no crew or agent logic here, just calls the
    service layer and returns what it gets back."""
    result = run_crew(request.topic)
    return CrewRunResponse(topic=request.topic, result=result)
