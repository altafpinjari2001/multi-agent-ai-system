"""
Multi-Agent AI System - Research Agent.

Senior Research Analyst that searches the web and gathers
comprehensive information on any given topic.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI

from ..tools.search_tool import WebSearchTool
from ..tools.scraper_tool import WebScraperTool


def create_research_agent(
    llm: ChatOpenAI,
    verbose: bool = True,
) -> Agent:
    """
    Create the Research Agent.

    This agent specializes in:
    - Web search and information gathering
    - Source verification and cross-referencing
    - Extracting key insights from multiple sources
    - Summarizing research findings
    """
    return Agent(
        role="Senior Research Analyst",
        goal=(
            "Find comprehensive, accurate, and up-to-date "
            "information on any given topic. Gather data from "
            "multiple reliable sources and identify key insights, "
            "trends, and statistics."
        ),
        backstory=(
            "You are a world-class research analyst with 10+ years "
            "of experience in technology research. You have access "
            "to powerful search tools and excel at finding the most "
            "relevant and credible information. You never make up "
            "facts and always cite your sources."
        ),
        tools=[WebSearchTool(), WebScraperTool()],
        llm=llm,
        verbose=verbose,
        allow_delegation=False,
        max_iter=10,
        memory=True,
    )
