from crewai import Agent, Task


def build_research_task(researcher: Agent) -> Task:
    return Task(
        description=(
            "Research {topic} and collect concrete facts and figures - not opinions."
        ),
        expected_output="A list of researched facts about {topic}.",
        agent=researcher,
    )
