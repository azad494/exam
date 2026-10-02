import time

from crewai import LLM

from app.shared.config import settings


class LLMClient:
    """The one place in this app allowed to talk to Gemini.

    Every agent borrows its LLM connection from here instead of building
    its own, so the API key and model settings live in exactly one spot.
    (This file used to be called mother_model.py / MotherModel.)

    It takes its settings straight from the one ready-made `settings`
    object in config.py - it never builds its own Config.
    """

    def __init__(self):
        self._model_name = settings.model_name
        self._llm = LLM(model=settings.model_name, temperature=settings.model_temperature)

    def get_llm(self) -> LLM:
        return self._llm

    def run_with_retry(self, crew, inputs: dict, max_retries: int = 2):
        """Runs crew.kickoff with simple retry-then-fail fallback logic.

        Returns (result_text, status). status always reports which model
        answered and whether it took a retry, so the API response can show
        the model's health alongside the actual result.
        """
        last_error = None
        for attempt in range(1, max_retries + 2):
            try:
                result = crew.kickoff(inputs=inputs)
                status = {
                    "model": self._model_name,
                    "status": "ok" if attempt == 1 else "ok_after_retry",
                    "attempts": attempt,
                }
                return str(result), status
            except Exception as exc:  # noqa: BLE001 - we want to retry on anything and report it
                last_error = exc
                if attempt <= max_retries:
                    time.sleep(1.5 * attempt)

        raise RuntimeError(
            f"{self._model_name} failed after {max_retries + 1} attempts: {last_error}"
        ) from last_error
