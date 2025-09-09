GenAI Math Toolkit
This project demonstrates a powerful and extensible application of Large Language Models (LLMs) by integrating them with a custom-built mathematical tool. Using langchain-mcp-adapters and langgraph, a Google Gemini-based agent can intelligently use a separate Python process (MathServer) to perform complex calculations it cannot do on its own.

Features
This agent is equipped with a comprehensive set of mathematical tools provided by the MathServer, including:

add, subtract, multiply, divide

power, square_root

factorial, gcd, lcm

sine, cosine, tangent

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.12+

uv: A modern, high-performance package installer and resolver for Python. You can install it with pip install uv.

Setup
Follow these steps to set up the project and install all necessary dependencies.

Clone the repository (or create the project folder if starting from scratch):

git clone [https://github.com/manas-099/mcp-math-solver.git](https://github.com/manas-099/mcp-math-solver.git)
cd mcp-math-solver

Create your .env file in the project's root directory. This file will securely store your API keys.

touch .env

Add your Google AI Studio API key to the file:

GOOGLE_API_KEY=YOUR_GOOGLE_AI_KEY_HERE

Create and activate a virtual environment using uv:

uv venv
.\.venv\Scripts\activate

Install the project dependencies from the pyproject.toml file:

uv pip install

Usage
To run the agent and see it in action, simply execute the client.py script from your terminal.

python client.py

The agent will load the MathServer as a subprocess and use its mathematical tools to solve the provided expression.



Project Structure
This project consists of two main Python scripts and a configuration file:

.
├── client.py
├── MathServer.py
├── pyproject.toml
└── .env

client.py: The main script that initializes the agent and the MathServer tool.

MathServer.py: The MCP-based server that provides the mathematical tools.

pyproject.toml: Defines the project's metadata and dependencies.

.env: (Not committed to Git) A file for storing sensitive information like API keys.



