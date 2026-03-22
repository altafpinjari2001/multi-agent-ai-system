"""
Multi-Agent AI System - Writer Agent.

Technical content writer that synthesizes research
into well-structured, engaging articles.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_writer_agent(
    llm: ChatOpenAI,
    verbose: bool = True,
) -> Agent:
    """
    Create the Writer Agent.

    This agent specializes in:
    - Transforming raw research into structured articles
    - Technical writing with clear explanations
    - Creating engaging narratives around complex topics
    - Proper formatting and organization
    """
    return Agent(
        role="Technical Content Writer",
        goal=(
            "Transform research findings into engaging, "
            "well-structured, and technically accurate content. "
            "Create articles that are informative yet accessible "
            "to a broad audience."
        ),
        backstory=(
            "You are an accomplished technical writer who has "
            "written for top technology publications. You excel "
            "at taking complex research and transforming it into "
            "clear, compelling narratives. Your writing is known "
            "for its depth, clarity, and engaging style."
        ),
        tools=[],
        llm=llm,
        verbose=verbose,
        allow_delegation=False,
        max_iter=5,
        memory=True,
    )
