from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from app.api.v1.router.api_router import api_router

app = FastAPI(title="Exam - CrewAI Mother-Model API")
app.include_router(api_router)


@app.get("/")
def health() -> dict:
    return {"status": "ok"}
