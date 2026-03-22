"""
Multi-Agent AI System - Writing Task.
"""

from crewai import Agent, Task


def create_writing_task(
    agent: Agent,
    topic: str,
    context: list[Task],
) -> Task:
    """Create the writing task."""
    return Task(
        description=(
            f"Using the research provided, write a comprehensive "
            f"article on:\n\n**{topic}**\n\n"
            f"Requirements:\n"
            f"1. Clear, engaging introduction that hooks the reader\n"
            f"2. Well-organized body with logical flow\n"
            f"3. Technical accuracy — use research data directly\n"
            f"4. Include code examples where relevant\n"
            f"5. Conclusion with key takeaways\n"
            f"6. Professional markdown formatting\n"
            f"7. 1500-2500 words in length"
        ),
        expected_output=(
            "A well-structured, publication-ready article in "
            "markdown format with headers, code blocks, bullet "
            "points, and proper formatting."
        ),
        agent=agent,
        context=context,
    )
