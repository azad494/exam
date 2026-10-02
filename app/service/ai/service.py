from typing import Optional

from app.service.ai.agent.crew.analyst_crew import build_analyst_crew
from app.service.ai.agent.crew.researcher_crew import build_researcher_crew
from app.service.ai.agent.crew.writer_crew import build_writer_crew
from app.service.ai.client import LLMClient

# Built once, reused across requests - this is what each endpoint calls into.
_client: Optional[LLMClient] = None


def get_client() -> LLMClient:
    global _client
    if _client is None:
        _client = LLMClient()
    return _client


def run_researcher(topic: str):
    client = get_client()
    crew = build_researcher_crew(client.get_llm())
    return client.run_with_retry(crew, inputs={"topic": topic})


def run_analyst(topic: str, research_notes: str):
    client = get_client()
    crew = build_analyst_crew(client.get_llm())
    return client.run_with_retry(crew, inputs={"topic": topic, "research_notes": research_notes})


def run_writer(topic: str, insights: str):
    client = get_client()
    crew = build_writer_crew(client.get_llm())
    return client.run_with_retry(crew, inputs={"topic": topic, "insights": insights})
