from crewai import Agent, Task


def build_writing_task(writer: Agent) -> Task:
    return Task(
        description=(
            "Using these insights about {topic}:\n\n{insights}\n\n"
            "Write a clear, engaging summary for a general reader."
        ),
        expected_output="A polished, well-written summary about {topic}.",
        agent=writer,
    )
