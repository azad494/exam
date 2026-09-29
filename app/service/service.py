from app.service.ai.agent.crew_builder import build_crew
from app.service.ai.llm.mother_model import MotherModel

_mother_model: MotherModel | None = None


def get_mother_model() -> MotherModel:
    global _mother_model
    if _mother_model is None:
        _mother_model = MotherModel()
    return _mother_model


def run_crew(topic: str) -> str:
    mother_model = get_mother_model()
    crew = build_crew(mother_model)
    result = crew.kickoff(inputs={"topic": topic})
    return str(result)
