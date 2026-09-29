from crewai import Agent, Task


def build_tasks(researcher: Agent, analyst: Agent, writer: Agent) -> tuple[Task, Task, Task]:
    """Builds the 3 chained tasks. Each task's `context` hands it the
    previous task's finished output -- that's the entire hand-off
    mechanism between agents, there's no shared memory beyond this."""
    research_task = Task(
        description="Research {topic} and list the most important, current facts.",
        expected_output="A bullet list of 5 facts about {topic}, each with why it matters.",
        agent=researcher,
    )

    analysis_task = Task(
        description="Analyze the research findings on {topic} and extract patterns.",
        expected_output="3-5 key insights about {topic}, each backed by evidence from the research.",
        agent=analyst,
        context=[research_task],
    )

    writing_task = Task(
        description="Turn the analysis of {topic} into a short, clear write-up for a general audience.",
        expected_output="A well-structured write-up of {topic}, 3-5 paragraphs, plain language.",
        agent=writer,
        context=[analysis_task],
    )

    return research_task, analysis_task, writing_task
