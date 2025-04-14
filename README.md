# MCP LangChain Integration Example

This project serves as a tutorial on integrating Model Control Protocol (MCP) with LangChain to build AI agents. By using a web search tool (DuckDuckGo) as an example, it demonstrates how to configure and orchestrate tools to enhance the agent's capabilities. The concepts and implementation can be extended to integrate other tools and models.

## Overview

The application uses:
- **MCP (Model Control Protocol)**: Provides a standardized way for models to interact with external tools
- **LangChain**: For agent creation and orchestration
- **Google's Gemini 2.0 Flash**: As the underlying AI model
- **DuckDuckGo Search**: As an external tool for web searches


## Project Structure

- `server.py`: Implements the MCP server with DuckDuckGo search functionality
- `prompt.py`: Contains the system prompt that instructs the AI how to respond
- `main.py`: Main application that connects the model, tools, and user input
- `requirements.txt`: Lists all required dependencies

## Prerequisites

- Python 3.8+
- Google API key (for Gemini model access)

## Installation

There are two methods to install the dependencies:

### Method 1: Using uv (recommended)

```bash
# Install uv first if you don't have it
# For macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# For Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment and install dependencies
uv venv
uv sync
```

### Method 2: Using pip

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root directory
2. Add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Running the Application

### Start the MCP Server
First, start the MCP server:

```bash
# Using uv
uv run .\src\server.py

# Or using Python directly (after activating virtual environment)
python .\src\server.py
```

### Run the Main Application
In a separate terminal:

```bash
# Using uv
uv run .\src\main.py

# Or using Python directly (after activating virtual environment)
python .\src\main.py
```

## How It Works

1. The MCP server provides a search tool that connects to DuckDuckGo
2. The main application creates a reactive agent using LangChain and Gemini
3. User questions are passed to the agent
4. The agent follows the system prompt to always use the search tool
5. Results are formatted and returned to the user

## Example Usage

When you run `main.py`, you'll be prompted to enter a question. The agent will:
1. Process your question
2. Use the DuckDuckGo search tool to find relevant information
3. Format and return an answer based on the search results