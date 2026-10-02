from crewai import LLM, Crew, Process

from app.service.ai.agent.persona.writer import build_writer
from app.service.ai.agent.task.writing_task import build_writing_task


def build_writer_crew(llm: LLM) -> Crew:
    writer = build_writer(llm)
    task = build_writing_task(writer)
    crew = Crew(agents=[writer], tasks=[task], process=Process.sequential, verbose=True)
    return crew
