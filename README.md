# LangChain RAG Weather Agent

## Overview

This is a Retrieval-Augmented Generation (RAG) agent built with LangChain. It combines LLM-powered question answering over documents with real-time weather tool-calling, providing accurate, context-aware responses for both internal knowledge and external data.

## Features

- **RAG Document QA**: Answers questions using your internal documents.
- **Weather Tool Integration**: Fetches real-time weather for any city.
- **OpenAI Function Calling**: Uses the latest function-calling agent pattern for robust tool selection.
- **Extensible**: Easily add more tools or data sources.
- **Environment-based configuration**: Uses `.env` for secrets and API keys.

## Quickstart

1. **Clone the repository and set up a virtual environment**
    ```sh
    git clone <repo-url>
    cd langchain-rag-agent
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure environment**
    - Copy `.env.example` to `.env` and fill in your OpenAI API key and any other required secrets.

4. **Run the agent**
    ```sh
    python3 -m agent_app.main
    ```

5. **Interact**
    - Enter questions about your documents or ask for the weather in any city.
    - The agent will automatically select the correct tool and return the answer.

## Adding New Tools

- Implement your tool in `agent_app/`.
- Register it in the agent graph (see `langgraph_graph.py`).
- Restart the agent to pick up new tools.