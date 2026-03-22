"""
Multi-Agent AI System - Web Search Tool.

Custom tool for searching the web using Serper API.
"""

import os
import json
import logging
from typing import Optional

import requests
from crewai.tools import BaseTool
from pydantic import Field

logger = logging.getLogger(__name__)


class WebSearchTool(BaseTool):
    """Search the web for information on any topic."""

    name: str = "web_search"
    description: str = (
        "Search the web for information. Input should be a "
        "search query string. Returns relevant search results "
        "with titles, snippets, and URLs."
    )

    def _run(self, query: str) -> str:
        """Execute web search using Serper API."""
        api_key = os.getenv("SERPER_API_KEY")

        if not api_key:
            return self._fallback_search(query)

        try:
            url = "https://google.serper.dev/search"
            headers = {
                "X-API-KEY": api_key,
                "Content-Type": "application/json",
            }
            payload = json.dumps({
                "q": query,
                "num": 10,
            })

            response = requests.post(
                url, headers=headers, data=payload, timeout=10
            )
            response.raise_for_status()
            data = response.json()

            results = []
            for item in data.get("organic", [])[:5]:
                results.append(
                    f"**{item.get('title', 'N/A')}**\n"
                    f"URL: {item.get('link', 'N/A')}\n"
                    f"Snippet: {item.get('snippet', 'N/A')}\n"
                )

            # Include knowledge graph if available
            kg = data.get("knowledgeGraph", {})
            if kg:
                results.insert(
                    0,
                    f"**Knowledge Graph: {kg.get('title', '')}**\n"
                    f"{kg.get('description', '')}\n",
                )

            return "\n---\n".join(results) if results else (
                "No results found."
            )

        except requests.RequestException as e:
            logger.error(f"Search API error: {e}")
            return f"Search failed: {str(e)}"

    def _fallback_search(self, query: str) -> str:
        """Fallback when no API key is available."""
        return (
            f"[Search API key not configured] "
            f"Unable to search for: {query}. "
            f"Please set SERPER_API_KEY in .env file."
        )
