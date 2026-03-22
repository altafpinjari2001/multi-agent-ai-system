"""
Multi-Agent AI System - Web Scraper Tool.

Custom tool for extracting clean content from web pages.
"""

import logging
from typing import Optional

import requests
from bs4 import BeautifulSoup
from crewai.tools import BaseTool

logger = logging.getLogger(__name__)


class WebScraperTool(BaseTool):
    """Scrape and extract clean content from web pages."""

    name: str = "web_scraper"
    description: str = (
        "Extract clean text content from a web page URL. "
        "Input should be a valid URL. Returns the main "
        "text content of the page."
    )

    def _run(self, url: str) -> str:
        """Scrape content from a URL."""
        try:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36"
                )
            }

            response = requests.get(
                url, headers=headers, timeout=15
            )
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Remove unwanted elements
            for tag in soup(
                ["script", "style", "nav", "footer", "header"]
            ):
                tag.decompose()

            # Extract main content
            main = (
                soup.find("main")
                or soup.find("article")
                or soup.find("body")
            )

            if not main:
                return "Could not extract content from the page."

            text = main.get_text(separator="\n", strip=True)

            # Clean up whitespace
            lines = [
                line.strip()
                for line in text.splitlines()
                if line.strip()
            ]
            clean_text = "\n".join(lines)

            # Truncate if too long
            max_chars = 5000
            if len(clean_text) > max_chars:
                clean_text = (
                    clean_text[:max_chars]
                    + "\n\n[Content truncated...]"
                )

            return clean_text

        except requests.RequestException as e:
            logger.error(f"Scraping error for {url}: {e}")
            return f"Failed to scrape {url}: {str(e)}"
