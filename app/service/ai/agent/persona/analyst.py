from crewai import LLM, Agent


def build_analyst(llm: LLM) -> Agent:
    """Interprets what Researcher already found. Never searches the web
    itself, so it never duplicates Researcher's job."""
    agent = Agent(
        role="Insight Analyst",
        goal="Interpret the research notes about {topic} and extract the key insights",
        backstory=(
            "You are an analyst who works only from notes handed to you. You never "
            "go looking for new information yourself — you find the patterns and "
            "the 'so what' in what the researcher already found."
        ),
        llm=llm,
        verbose=True,
    )
    return agent
