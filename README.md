Here’s the full **refactored `README.md`** with the **Sample Report** section added in:

````markdown
[![CI](https://github.com/ramonbnuezjr/autogpt-research-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/ramonbnuezjr/autogpt-research-agent/actions/workflows/ci.yml)

# Autonomous Research Agent

A modular AI pipeline that plans, executes, stores memory, and reports research—all orchestrated by `main.py`.

## Features - only one feature for now

- **Planner**: Breaks a research goal into actionable subtasks  
- **Executor**: Uses an LLM to research each subtask  
- **Memory**: Persists session results locally (or vector store)  
- **Reporter**: Generates a Markdown report of findings  
- **Fully Tested**: Unit and integration tests with pytest  

## Installation

1. Clone the repo:  
   ```bash
   git clone https://github.com/ramonbnuezjr/autogpt-research-agent.git
   cd autogpt-research-agent
````

2. Copy and configure your environment:

   ```bash
   cp .env.example .env
   # edit .env to add your OPENAI_API_KEY (or set LLM_BACKEND)
   ```
3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the agent from the CLI:

```bash
python main.py --goal "How is AI being used in smart cities?"
```

*(If you haven’t refactored for flags yet, just `python main.py` and type your goal at the prompt.)*

## Sample Report

We’ve saved the latest research report in the `reports/` folder.
Check it out here:

* [How\_are\_AI\_agents\_similar\_to\_new\_species\_20250512\_184941.md](reports/How_are_AI_agents_similar_to_new_species_20250512_184941.md)

Or browse the entire folder:

* [📁 reports/](reports/)

## Testing

We use **pytest** for automated tests.

1. Install dev dependencies:

   ```bash
   pip install pytest
   ```
2. Run the full suite:

   ```bash
   pytest
   ```
3. (Optional) To exercise the real API integration:

   ```bash
   export LIVE_API=true
   pytest -m live
   ```

---

*For more details on CI, linting, and type checking, see [`.github/workflows/ci.yml`](.github/workflows/ci.yml) and the lint configs in the repo root.*

