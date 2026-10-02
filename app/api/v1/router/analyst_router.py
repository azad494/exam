from fastapi import APIRouter

from app.api.v1.endpoints.analyst_endpoint import (
    AnalystRunRequest,
    AnalystRunResponse,
    run,
)

router = APIRouter()


@router.post("/run", response_model=AnalystRunResponse)
def run_analyst_route(request: AnalystRunRequest) -> AnalystRunResponse:
    return run(request)
