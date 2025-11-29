PR Review Agent – Demo

A lightweight tool that analyzes code changes using LLM-based multi-agent reasoning.
It accepts unified diffs or GitHub Pull Request diffs and returns structured, actionable review comments.

🚀 Features

Paste a unified diff or fetch a GitHub PR

Detects:

Hardcoded secrets & security risks

TODO/FIXME & style issues

Performance problems (e.g., nested loops)

Missing error handling

Produces structured JSON output

Optional: Auto-post review comments to the PR (GitHub PAT required)

🧪 Quick Test
Example diff:
diff --git a/app.py b/app.py
--- a/app.py
+++ b/app.py
@@ -1,5 +1,8 @@
-MY_SECRET = "12345"
+MY_SECRET = "HARDCODED_SECRET"

# TODO: optimize
for i in range(1000):
    pass

Example PR review:

Owner → MayurDas24
Repo → PR-Agent-Test
PR → 1 or 2

▶️ Run Locally (Windows + PowerShell)
git clone https://github.com/<your-username>/PR-Agent-Test.git
cd PR-Agent-Test

python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

uvicorn main:app --reload

📁 Key Files
diff_parser.py
reviewer_langchain.py
github_integration.py
agents.py
main.py
static/

📌 Note

This project is a demo submission showcasing backend design, GitHub API use, and LLM-based code review automation.
