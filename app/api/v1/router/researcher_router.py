from fastapi import APIRouter

from app.api.v1.endpoints.researcher_endpoint import (
    ResearcherRunRequest,
    ResearcherRunResponse,
    run,
)

router = APIRouter()


@router.post("/run", response_model=ResearcherRunResponse)
def run_researcher_route(request: ResearcherRunRequest) -> ResearcherRunResponse:
    return run(request)
