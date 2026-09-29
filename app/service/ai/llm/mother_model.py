from crewai import LLM

from app.shared.config import Settings


class MotherModel:
    """Owns the single shared LLM instance every agent inherits from.

    Every agent is constructed with `llm=mother_model.get_llm(...)`. None of
    them import crewai.LLM, litellm, or a provider SDK, and none of them
    hold the API key -- this class is the only place that does.
    """

    def __init__(self, settings: Settings | None = None) -> None:
        settings = settings or Settings()
        self._model = settings.mother_model_name
        self._api_key = settings.gemini_api_key
        self._default_temperature = settings.mother_model_temperature
        self._llm = LLM(model=self._model, api_key=self._api_key, temperature=self._default_temperature)

    def get_llm(self, temperature: float | None = None) -> LLM:
        """Return the shared LLM, or a one-off variant with a different
        temperature. Never mutates the shared instance -- other agents may
        be holding a reference to it."""
        if temperature is None:
            return self._llm
        return LLM(model=self._model, api_key=self._api_key, temperature=temperature)
