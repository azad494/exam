from crewai import LLM

from app.shared.config import Settings


class MotherModel:
    def __init__(self, settings: Settings | None = None) -> None:
        settings = settings or Settings()
        self._model = settings.mother_model_name
        self._api_key = settings.gemini_api_key
        self._default_temperature = settings.mother_model_temperature
        self._llm = LLM(model=self._model, api_key=self._api_key, temperature=self._default_temperature)

    def get_llm(self, temperature: float | None = None) -> LLM:
        if temperature is None:
            return self._llm
        return LLM(model=self._model, api_key=self._api_key, temperature=temperature)
