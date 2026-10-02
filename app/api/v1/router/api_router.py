from fastapi import APIRouter

from app.api.v1.router.analyst_router import router as analyst_router
from app.api.v1.router.researcher_router import router as researcher_router
from app.api.v1.router.writer_router import router as writer_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(researcher_router, prefix="/agents/researcher", tags=["researcher"])
api_router.include_router(analyst_router, prefix="/agents/analyst", tags=["analyst"])
api_router.include_router(writer_router, prefix="/agents/writer", tags=["writer"])
