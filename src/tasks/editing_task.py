"""
Multi-Agent AI System - Editing Task.
"""

from crewai import Agent, Task


def create_editing_task(
    agent: Agent,
    context: list[Task],
) -> Task:
    """Create the editing task."""
    return Task(
        description=(
            "Review and edit the article for publication. "
            "Your review should cover:\n\n"
            "1. **Accuracy** — Verify facts match the research\n"
            "2. **Clarity** — Ensure concepts are well-explained\n"
            "3. **Structure** — Logical flow and organization\n"
            "4. **Grammar & Style** — Professional writing quality\n"
            "5. **Completeness** — No missing critical information\n"
            "6. **Formatting** — Proper markdown, headers, code blocks\n\n"
            "Make direct edits and improvements. The output should "
            "be the final, polished article ready for publication."
        ),
        expected_output=(
            "The final, publication-ready article with all "
            "edits applied. This should be polished, accurate, "
            "and professionally formatted markdown."
        ),
        agent=agent,
        context=context,
    )
