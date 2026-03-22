"""
Multi-Agent AI System - Crew Orchestrator.

Configures and orchestrates the multi-agent crew for
collaborative task execution.
"""

import logging
from typing import Optional

from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from .config import get_settings
from .agents import (
    create_research_agent,
    create_writer_agent,
    create_editor_agent,
)
from .tasks.research_task import create_research_task
from .tasks.writing_task import create_writing_task
from .tasks.editing_task import create_editing_task

logger = logging.getLogger(__name__)


class ResearchCrew:
    """
    Orchestrates a crew of AI agents for research and content creation.

    The crew follows a sequential workflow:
    1. Research Agent gathers information
    2. Writer Agent creates content from research
    3. Editor Agent reviews and refines the output
    """

    def __init__(
        self,
        model_name: Optional[str] = None,
        temperature: float = 0.7,
        verbose: bool = True,
    ):
        settings = get_settings()
        self.verbose = verbose

        # Initialize LLM
        self.llm = ChatOpenAI(
            model=model_name or settings.model_name,
            temperature=temperature,
            openai_api_key=settings.openai_api_key,
        )

        # Create agents
        self.researcher = create_research_agent(
            self.llm, verbose
        )
        self.writer = create_writer_agent(self.llm, verbose)
        self.editor = create_editor_agent(self.llm, verbose)

        logger.info("ResearchCrew initialized with 3 agents")

    def run(self, topic: str) -> str:
        """
        Execute the full research → write → edit pipeline.

        Args:
            topic: The topic to research and write about.

        Returns:
            Final edited article as a string.
        """
        logger.info(f"Starting crew for topic: {topic}")

        # Create tasks
        research_task = create_research_task(
            agent=self.researcher, topic=topic
        )
        writing_task = create_writing_task(
            agent=self.writer,
            topic=topic,
            context=[research_task],
        )
        editing_task = create_editing_task(
            agent=self.editor,
            context=[research_task, writing_task],
        )

        # Assemble and run crew
        crew = Crew(
            agents=[self.researcher, self.writer, self.editor],
            tasks=[research_task, writing_task, editing_task],
            process=Process.sequential,
            verbose=self.verbose,
            memory=True,
            max_rpm=10,
        )

        result = crew.kickoff()

        logger.info("Crew execution completed")
        return str(result)
