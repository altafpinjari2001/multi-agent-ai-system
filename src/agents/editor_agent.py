"""
Multi-Agent AI System - Editor Agent.

Senior content editor that reviews, fact-checks,
and refines content for publication quality.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_editor_agent(
    llm: ChatOpenAI,
    verbose: bool = True,
) -> Agent:
    """
    Create the Editor Agent.

    This agent specializes in:
    - Content review and quality assurance
    - Fact-checking and accuracy verification
    - Grammar, style, and tone consistency
    - Providing constructive feedback
    """
    return Agent(
        role="Senior Content Editor",
        goal=(
            "Review and refine content to ensure the highest "
            "quality standards. Check for accuracy, clarity, "
            "consistency, and proper formatting. Ensure the "
            "final output is publication-ready."
        ),
        backstory=(
            "You are a meticulous editor with decades of "
            "experience in technical publishing. You have an eye "
            "for detail and a talent for improving any piece of "
            "writing. You ensure every article meets the highest "
            "standards of accuracy and readability."
        ),
        tools=[],
        llm=llm,
        verbose=verbose,
        allow_delegation=True,
        max_iter=5,
        memory=True,
    )
