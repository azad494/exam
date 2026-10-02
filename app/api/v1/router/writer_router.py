from fastapi import APIRouter

from app.api.v1.endpoints.writer_endpoint import (
    WriterRunRequest,
    WriterRunResponse,
    run,
)

router = APIRouter()


@router.post("/run", response_model=WriterRunResponse)
def run_writer_route(request: WriterRunRequest) -> WriterRunResponse:
    return run(request)
