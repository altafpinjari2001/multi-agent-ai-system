"""
Multi-Agent AI System - Research Task.
"""

from crewai import Agent, Task


def create_research_task(
    agent: Agent,
    topic: str,
) -> Task:
    """Create the research task."""
    return Task(
        description=(
            f"Conduct comprehensive research on the following topic:\n\n"
            f"**{topic}**\n\n"
            f"Your research should include:\n"
            f"1. Overview and background of the topic\n"
            f"2. Latest developments and trends (2024-2025)\n"
            f"3. Key players, companies, or researchers involved\n"
            f"4. Technical details and methodologies\n"
            f"5. Real-world applications and use cases\n"
            f"6. Challenges and limitations\n"
            f"7. Future outlook and predictions\n\n"
            f"Provide specific data points, statistics, and cite "
            f"your sources with URLs wherever possible."
        ),
        expected_output=(
            "A comprehensive research report with:\n"
            "- Executive summary\n"
            "- Detailed findings organized by subtopic\n"
            "- Key statistics and data points\n"
            "- Source citations with URLs\n"
            "- List of recommended further reading"
        ),
        agent=agent,
    )
