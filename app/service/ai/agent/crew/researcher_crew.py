from crewai import LLM, Crew, Process

from app.service.ai.agent.persona.researcher import build_researcher
from app.service.ai.agent.task.research_task import build_research_task


def build_researcher_crew(llm: LLM) -> Crew:
    researcher = build_researcher(llm)
    task = build_research_task(researcher)
    crew = Crew(agents=[researcher], tasks=[task], process=Process.sequential, verbose=True)
    return crew
