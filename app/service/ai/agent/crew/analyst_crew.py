from crewai import LLM, Crew, Process

from app.service.ai.agent.persona.analyst import build_analyst
from app.service.ai.agent.task.analysis_task import build_analysis_task


def build_analyst_crew(llm: LLM) -> Crew:
    analyst = build_analyst(llm)
    task = build_analysis_task(analyst)
    crew = Crew(agents=[analyst], tasks=[task], process=Process.sequential, verbose=True)
    return crew
