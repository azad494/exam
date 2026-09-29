from crewai import Agent, LLM


def build_writer(llm: LLM) -> Agent:
    return Agent(
        role="Content Writer",
        goal="Turn the analyst's findings on {topic} into a clear, well-structured write-up",
        backstory=(
            "You are a former journalist who favors plain language over jargon, and you always lead "
            "with the point instead of burying it."
        ),
        llm=llm,
        verbose=True,
    )
