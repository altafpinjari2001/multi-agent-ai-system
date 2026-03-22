"""
Multi-Agent AI System - Entry Point.

Run the multi-agent research pipeline from the command line.
"""

import argparse
import logging
import sys
from pathlib import Path

from src.crew import ResearchCrew


def setup_logging(verbose: bool = False) -> None:
    """Configure logging."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s │ %(name)s │ %(levelname)s │ %(message)s",
        datefmt="%H:%M:%S",
    )


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent AI Research Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --topic "Latest advances in Agentic AI 2025"
  python main.py --topic "RAG vs Fine-tuning" --output markdown
  python main.py --interactive
        """,
    )

    parser.add_argument(
        "--topic",
        type=str,
        help="Research topic",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="markdown",
        choices=["markdown", "text", "json"],
        help="Output format (default: markdown)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output directory (default: output)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="LLM model name (default: from .env)",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive mode",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=True,
        help="Enable verbose output",
    )

    args = parser.parse_args()
    setup_logging(args.verbose)

    if args.interactive:
        print("\n🤖 Multi-Agent AI Research System")
        print("=" * 50)
        topic = input("\n📝 Enter your research topic: ").strip()
        if not topic:
            print("❌ No topic provided. Exiting.")
            sys.exit(1)
    elif args.topic:
        topic = args.topic
    else:
        parser.print_help()
        sys.exit(1)

    print(f"\n🔍 Starting research on: {topic}")
    print("=" * 50)
    print("⏳ This may take a few minutes...\n")

    # Run the crew
    crew = ResearchCrew(
        model_name=args.model,
        verbose=args.verbose,
    )
    result = crew.run(topic)

    # Save output
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    # Create filename from topic
    filename = topic.lower().replace(" ", "_")[:50]
    output_file = output_dir / f"{filename}.md"
    output_file.write_text(result, encoding="utf-8")

    print(f"\n✅ Article saved to: {output_file}")
    print("=" * 50)


if __name__ == "__main__":
    main()
