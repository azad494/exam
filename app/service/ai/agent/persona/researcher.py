from crewai import LLM, Agent


def build_researcher(llm: LLM) -> Agent:
    """Gathers the facts Analyst and Writer build on, so nobody re-does this
    job (and nobody pays for a second research pass on the same topic)."""
    agent = Agent(
        role="Researcher",
        goal="Gather the most relevant, concrete facts about {topic}",
        backstory=(
            "You are a meticulous researcher who collects concrete facts about "
            "a topic from what you know, rather than offering opinions."
        ),
        llm=llm,
        verbose=True,
    )
    return agent
