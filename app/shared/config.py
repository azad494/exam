import os


class Settings:
    def __init__(self) -> None:
        self.gemini_api_key: str = os.environ["GEMINI_API_KEY"]
        self.mother_model_name: str = os.environ.get("MOTHER_MODEL", "gemini/gemini-2.5-flash")
        self.mother_model_temperature: float = float(os.environ.get("MOTHER_MODEL_TEMP", "0.7"))
