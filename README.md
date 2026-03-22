<div align="center">

# 🤖 Multi-Agent AI System

**An agentic AI orchestrator where autonomous agents collaborate to research, write, and review — powered by CrewAI & LangChain**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/🚀_CrewAI-Latest-FF4500?style=for-the-badge)](https://crewai.com)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-0.3+-1C3C3C?style=for-the-badge)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[Features](#-features) • [Architecture](#-architecture) • [Quick Start](#-quick-start) • [Agents](#-agents) • [Tools](#-custom-tools)

</div>

---

## 📌 Overview

This project demonstrates **Agentic AI** — a paradigm where multiple AI agents autonomously collaborate to complete complex tasks. Instead of a single LLM call, the system decomposes tasks into subtasks, assigns them to specialized agents, and orchestrates their collaboration.

### Use Case: AI Research & Content Pipeline

Given a topic, the system:
1. **🔍 Research Agent** — searches the web, gathers sources, extracts key insights
2. **✍️ Writer Agent** — synthesizes research into a well-structured article
3. **📝 Editor Agent** — reviews, fact-checks, and refines the final output
4. **📊 Analyst Agent** — generates data-driven insights and visualizations

---

## ✨ Features

- 🤖 **4 Specialized AI Agents** — each with unique roles, goals, and backstories
- 🔧 **Custom Tool Integration** — web search, content scraping, code execution
- 🧠 **Agent Memory** — short-term, long-term, and entity memory
- 📋 **Task Delegation** — hierarchical and sequential task orchestration
- 🔄 **Human-in-the-Loop** — optional human approval at critical decision points
- 📊 **Structured Output** — Pydantic-validated outputs from each agent
- 🌊 **Streaming** — Real-time agent thought process streaming
- 📝 **Comprehensive Logging** — full trace of agent reasoning and actions

---

## 🏗 Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Crew Orchestrator                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │   Research    │  │    Writer    │  │    Editor    │   │
│  │    Agent      │→│    Agent     │→│    Agent     │   │
│  │              │  │              │  │              │   │
│  │ • Web Search │  │ • Synthesis  │  │ • Review     │   │
│  │ • Scraping   │  │ • Structuring│  │ • Fact-check │   │
│  │ • Analysis   │  │ • Formatting │  │ • Refinement │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
│         │                 │                 │            │
│         ▼                 ▼                 ▼            │
│  ┌────────────────────────────────────────────────────┐  │
│  │              Shared Memory & Context               │  │
│  └────────────────────────────────────────────────────┘  │
│         │                 │                 │            │
│         ▼                 ▼                 ▼            │
│  ┌────────────────────────────────────────────────────┐  │
│  │                  Custom Tools                      │  │
│  │  🔍 Search  │  🌐 Scraper  │  📊 Analyzer        │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/altafpinjari2001/multi-agent-ai-system.git
cd multi-agent-ai-system

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
```

### Run

```bash
# Run the research pipeline
python main.py --topic "Latest advances in Agentic AI 2025"

# Interactive mode
python main.py --interactive

# With specific output format
python main.py --topic "RAG vs Fine-tuning" --output markdown
```

---

## 🤖 Agents

### 1. Research Agent 🔍
```python
role = "Senior Research Analyst"
goal = "Find comprehensive, accurate information on any given topic"
tools = [WebSearchTool, WebScraperTool, WikipediaTool]
```

### 2. Writer Agent ✍️
```python
role = "Technical Content Writer"
goal = "Transform research into engaging, well-structured content"
tools = [FileWriterTool]
```

### 3. Editor Agent 📝
```python
role = "Senior Content Editor"
goal = "Ensure content accuracy, clarity, and professional quality"
tools = [FileReaderTool]
```

### 4. Analyst Agent 📊
```python
role = "Data Analyst"
goal = "Extract quantitative insights and create data visualizations"
tools = [CodeExecutorTool, ChartGeneratorTool]
```

---

## 🔧 Custom Tools

| Tool | Description |
|------|-------------|
| `WebSearchTool` | Searches the web using Serper API with result parsing |
| `WebScraperTool` | Extracts clean content from URLs using BeautifulSoup |
| `WikipediaTool` | Fetches Wikipedia summaries for fact-checking |
| `FileWriterTool` | Writes structured content to files |
| `CodeExecutorTool` | Safely executes Python code for data analysis |
| `ChartGeneratorTool` | Generates charts and visualizations |

---

## 📁 Project Structure

```
multi-agent-ai-system/
├── main.py                    # Entry point
├── requirements.txt
├── .env.example
├── src/
│   ├── __init__.py
│   ├── config.py              # Configuration
│   ├── crew.py                # Crew orchestration
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── research_agent.py
│   │   ├── writer_agent.py
│   │   ├── editor_agent.py
│   │   └── analyst_agent.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── research_task.py
│   │   ├── writing_task.py
│   │   ├── editing_task.py
│   │   └── analysis_task.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── search_tool.py
│   │   ├── scraper_tool.py
│   │   └── code_executor.py
│   └── models/
│       ├── __init__.py
│       └── output_models.py
├── tests/
│   ├── test_agents.py
│   ├── test_tools.py
│   └── test_crew.py
├── output/                    # Generated content
├── .github/workflows/ci.yml
├── LICENSE
└── .gitignore
```

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <b>⭐ Star this repo if you find it useful!</b>
</div>
