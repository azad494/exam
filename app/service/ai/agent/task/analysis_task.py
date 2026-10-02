from crewai import Agent, Task


def build_analysis_task(analyst: Agent) -> Task:
    return Task(
        description=(
            "Read these research notes about {topic}:\n\n{research_notes}\n\n"
            "Identify the key insights and what matters most."
        ),
        expected_output="A short list of the key insights drawn from the research notes.",
        agent=analyst,
    )
