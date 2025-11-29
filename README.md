🚀 PR Review Agent – AI-Powered Code Review Demo

A lightweight AI-based Pull Request Review Agent that reads unified diffs or GitHub PR diffs and generates structured, actionable code review feedback.
Built with FastAPI, LLM multi-agent reasoning, and a simple web UI.

✨ Features

🔍 Analyze unified diffs (paste or upload)

🔗 Fetch and review GitHub Pull Requests

🤖 Multi-agent reasoning:

Security issues (e.g., hardcoded secrets)

Style issues (TODO, FIXME)

Performance concerns (nested loops, inefficient code)

Robustness (missing error handling)

📝 Outputs structured JSON with:

path, line, type, message, suggested_fix, confidence

💬 Optional: Post comments directly to GitHub PRs (requires GitHub PAT)

🧪 Example Diff to Test
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1,5 +1,8 @@
-MY_SECRET = "12345"
+MY_SECRET = "HARDCODED_SECRET_ABC"

# TODO: optimize this nested loop
for i in range(1000):
    for j in range(500):
        pass


Use this in the UI to see the tool generate findings.

▶️ Run Locally (Windows + PowerShell)
git clone https://github.com/<your-username>/PR-Agent-Test.git
cd PR-Agent-Test

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

uvicorn main:app --reload


Open the app in your browser:
👉 http://127.0.0.1:8000

📁 Project Structure
agents.py               – LLM agents for security/style/performance checks
diff_parser.py          – Unified diff parser
reviewer_langchain.py   – Multi-agent orchestration
github_integration.py   – GitHub PR fetch + comment API
main.py                 – FastAPI server + endpoints
static/index.html       – Web UI for testing the agent

🎯 Purpose of This Repository

This project is a demo submission showcasing:

Backend engineering

FastAPI development

GitHub API usage

LLM integration & orchestration

A working code-review agent with UI
