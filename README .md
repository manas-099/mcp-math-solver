# GenAI Math Toolkit

This project demonstrates a powerful and extensible application of **Large Language Models (LLMs)** by integrating them with a custom-built mathematical tool. Using **langchain-mcp-adapters** and **langgraph**, a **Google Gemini-based agent** can intelligently use a separate Python process (**MathServer**) to perform complex calculations it cannot do on its own.

---

## ✨ Features

The agent is equipped with a comprehensive set of mathematical tools provided by the **MathServer**, including:

- Basic Arithmetic: `add`, `subtract`, `multiply`, `divide`
- Advanced Operations: `power`, `square_root`
- Number Theory: `factorial`, `gcd`, `lcm`
- Trigonometry: `sine`, `cosine`, `tangent`

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.12+**
- **uv** → A modern, high-performance package installer and resolver for Python.  
  Install it with:
  ```bash
  pip install uv
  ```

---

## ⚙️ Setup

Follow these steps to set up the project and install all necessary dependencies:

1. **Clone the repository (or create the project folder if starting from scratch):**
   ```bash
   git clone https://github.com/manas-099/mcp-math-solver.git
   cd mcp-math-solver
   ```

2. **Create your `.env` file** in the project's root directory. This file securely stores your API keys:
   ```bash
   touch .env
   ```

3. **Add your Google AI Studio API key** to the `.env` file:
   ```env
   GOOGLE_API_KEY=YOUR_GOOGLE_AI_KEY_HERE
   ```

4. **Create and activate a virtual environment** using `uv`:
   ```bash
   uv venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

5. **Install the project dependencies** from the `pyproject.toml` file:
   ```bash
   uv pip install
   ```

---

## ▶️ Usage

To run the agent and see it in action, simply execute the `client.py` script from your terminal:

```bash
python client.py
```

The agent will load the **MathServer** as a subprocess and use its mathematical tools to solve the provided expression.

---

## 📂 Project Structure

```
mcp-math-solver/
├── client.py        # Main script that initializes the agent and MathServer tool
├── MathServer.py    # MCP-based server providing mathematical tools
├── pyproject.toml   # Project metadata and dependencies
└── .env             # Stores sensitive information like API keys (not committed to Git)
```

---

## 🛡️ Notes

- Keep your `.env` file private and **never commit it** to version control.
- The project is extensible — you can easily add new mathematical functions to `MathServer.py`.

---

## 🤝 Contributing

Pull requests and suggestions are welcome! If you’d like to contribute, feel free to fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the **MIT License**.
