from crewai import LLM, Agent


def build_writer(llm: LLM) -> Agent:
    agent = Agent(
        role="Content Writer",
        goal="Turn the analyst's insights about {topic} into a clear, engaging piece of writing",
        backstory=(
            "You are a writer who turns analysis into something a general reader "
            "actually wants to read, without inventing new facts of your own."
        ),
        llm=llm,
        verbose=True,
    )
    return agent
