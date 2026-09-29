from crewai import Crew, Process

from app.service.ai.agent.persona.analyst import build_analyst
from app.service.ai.agent.persona.researcher import build_researcher
from app.service.ai.agent.persona.writer import build_writer
from app.service.ai.agent.task.tasks import build_tasks
from app.service.ai.llm.mother_model import MotherModel


def build_crew(mother_model: MotherModel) -> Crew:
    """Builds the 3-agent crew. Every agent gets its LLM from the mother
    model's get_llm() -- none of them construct or configure an LLM
    themselves, and each can ask for its own temperature without touching
    MotherModel."""
    researcher = build_researcher(mother_model.get_llm(temperature=0.2))
    analyst = build_analyst(mother_model.get_llm(temperature=0.4))
    writer = build_writer(mother_model.get_llm(temperature=0.9))

    research_task, analysis_task, writing_task = build_tasks(researcher, analyst, writer)

    return Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True,
    )
