from crewai import Agent, LLM


def build_researcher(llm: LLM) -> Agent:
    return Agent(
        role="Senior Research Analyst",
        goal="Find accurate, current facts about {topic} and surface the most important ones",
        backstory=(
            "You are meticulous and always trace a claim back to a source before repeating it. "
            "You favor recent, verifiable information over speculation."
        ),
        llm=llm,
        verbose=True,
    )
