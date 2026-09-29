from app.service.ai.agent.crew_builder import build_crew
from app.service.ai.llm.mother_model import MotherModel

_mother_model: MotherModel | None = None


def get_mother_model() -> MotherModel:
    """Builds the mother model once (on the first request) and reuses the
    same instance for every request after that."""
    global _mother_model
    if _mother_model is None:
        _mother_model = MotherModel()
    return _mother_model


def run_crew(topic: str) -> str:
    """The one function the API layer calls. Everything about how the crew
    is built and which model backs it is hidden behind this call -- the
    endpoint below knows nothing about CrewAI at all."""
    mother_model = get_mother_model()
    crew = build_crew(mother_model)
    result = crew.kickoff(inputs={"topic": topic})
    return str(result)
