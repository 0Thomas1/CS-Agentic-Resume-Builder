# 🤖 CS Agentic Resume Builder

Turn your GitHub experience into role-targeted resume content automatically.

This repository contains a **multi-agent resume building workflow** built with Python and Google ADK. Instead of manually rewriting project bullets for every job application, the pipeline analyzes job descriptions, matches relevant repositories, and generates polished resume content ready to use.

> ⚠️ **Early Prototype** — Focus is on demonstrating multi-agent coordination for real-world problems.

---

## 🎯 Purpose

Automate the tedious process of tailoring your resume:

- 📋 Analyze target job descriptions for key requirements
- 🔍 Match your GitHub repositories to role demands
- ✍️ Generate polished, schema-aligned resume project content

---

## 💡 Why This Project Exists

Manually tailoring resumes for each job application is tedious and time-consuming. This project:

- **Saves time** — Automate resume content generation
- **Demonstrates real-world AI** — Shows multi-agent systems in practice
- **Improves outcomes** — Present your experience in the best light for each role

---

## 🏗️ Architecture

The workflow is organized as specialized agents coordinated by a manager pipeline:

| Agent             | Responsibility                                     |
| ----------------- | -------------------------------------------------- |
| **Manager**       | Orchestrates workflow and coordinates other agents |
| **Analyst**       | Parses job requirements into structured format     |
| **Repo Matcher**  | Finds best repositories matching the target role   |
| **Resume Tailor** | Transforms matched evidence into polished content  |

Each agent is modular and can be tested independently.

---

## 📁 Project Structure

```
agents/manager/
├── agent.py                          # Coordinator orchestration
├── agents/
│   ├── analyst/                      # Job analysis agent
│   ├── repo_matcher/                 # GitHub data & matching logic
│   ├── resume_tailor/                # Resume content generation
│   └── greeter/                      # User intake agent
```

---

## ⚙️ How It Works

1. **User Input** — Provide target role and job description
2. **Job Analysis** — Analyst agent extracts requirements (skills, seniority, work model)
3. **Repository Fetch** — Retrieve GitHub metadata (README, languages, URLs)
4. **Selection** — Matcher agent identifies strongest project candidates
5. **Generation** — Tailor agent produces schema-aligned resume content

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **GitHub credentials:**
  - `GITHUB_USERNAME`
  - `GITHUB_TOKEN`
- **Google GenAI API key:** [Get one here](https://aistudio.google.com/app/api-keys)

### Setup (5 minutes)

**1. Create virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in each agent's root directory (e.g., `agents/manager/agents/repo_matcher/.env`) with the following content:

```bash
# Google GenAI (required)
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your_api_key_here

# GitHub (required for repo matching)
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token
```

> **💡 Tip:** Use separate API keys per agent in development to avoid rate limits.

### Run the Web Interface

```bash
source .venv/bin/activate
cd agents
adk web --port 8080
```

Then open your browser to `http://localhost:8080`

---

## 🛠️ Tech Stack

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| **Google ADK**   | Agent orchestration and async communication |
| **GitHub API**   | Repository metadata and content retrieval   |
| **Google GenAI** | Language understanding and generation       |
| **Pydantic**     | Schema validation and structured outputs    |
| **Python 3.10+** | Core language                               |

---

## 📋 ResumeProject Schema

The system outputs data that matches this schema for resume content:

```json
{
  "title": "Agentic Resume Builder",
  "description": "A multi-agent Python system that analyzes job requirements, matches GitHub repositories, and generates tailored resume project content.",
  "category": "AI Agent / Career Tooling",
  "tech_stack": ["Python", "Google ADK", "Pydantic", "GitHub API"],
  "core_problem_solved": "Automates the process of selecting and presenting the most relevant project experience for a specific job application.",
  "key_features": [
    "Structured job description analysis",
    "Repository matching based on role requirements",
    "Schema-first output for resume project sections",
    "Modular multi-agent pipeline architecture"
  ],
  "quantifiable_metrics": []
}
```

---

## 🗺️ Roadmap

- [ ] Add iterative revision loop for human-in-the-loop refinement
- [ ] Implement Agent-to-Agent (A2A) communication protocol
- [ ] Add scoring transparency for matching decisions
- [ ] Add guardrails to prevent hallucination
- [ ] Auto-export to ATS-friendly formats

---

**Questions?** Open an issue or start a discussion!
