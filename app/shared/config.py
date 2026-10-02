import os

from dotenv import load_dotenv

# Loaded right here, not in main.py, so any file that imports Config gets
# working settings no matter which entrypoint (main.py, a test, a single
# endpoint run directly) started the process first.
load_dotenv()


class Config:
    """Reads every setting this app needs from the environment, once."""

    def __init__(self):
        self.config()

    def config(self):
        self.gemini_api_key = os.environ["GEMINI_API_KEY"]
        self.serper_api_key = os.getenv("SERPER_API_KEY")
        self.model_name = os.getenv("LLM_MODEL", "gemini/gemini-2.5-flash")
        self.model_temperature = float(os.getenv("LLM_TEMPERATURE", "0.7"))


# Built once, right here, when this module is first imported. Every other
# file imports this one ready-made object instead of building its own
# Config() - so there is exactly one place that ever constructs it.
settings = Config()
