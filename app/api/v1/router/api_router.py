from fastapi import APIRouter

from app.api.v1.endpoints.endpoint import router as crew_router

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(crew_router, prefix="/crew", tags=["crew"])
