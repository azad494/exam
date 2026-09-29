import os


class Settings:
    """Central place every other layer reads configuration from.

    Nothing outside this file (and your real environment / a .env) should
    ever reference an env var name directly. Need a new setting later?
    Add it here once, not wherever you happen to need it.
    """

    def __init__(self) -> None:
        self.gemini_api_key: str = os.environ["GEMINI_API_KEY"]
        self.mother_model_name: str = os.environ.get("MOTHER_MODEL", "gemini/gemini-2.5-flash")
        self.mother_model_temperature: float = float(os.environ.get("MOTHER_MODEL_TEMP", "0.7"))
