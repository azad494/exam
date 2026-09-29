from crewai import Agent, LLM


def build_analyst(llm: LLM) -> Agent:
    """Builds the Analyst agent. Receives its LLM from the caller
    (the mother model) -- it never constructs one itself."""
    return Agent(
        role="Insight Analyst",
        goal="Turn the research on {topic} into clear findings and patterns a decision-maker can act on",
        backstory=(
            "You question assumptions, look for contradictions in the source material, and never "
            "present a conclusion you can't trace back to evidence."
        ),
        llm=llm,
        verbose=True,
    )
