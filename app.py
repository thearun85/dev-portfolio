"""
dev-portfolio - Flask Backend

This flask app serves:
1. The landing page for the app
2. API endpoints for the terminal commands.
"""

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


ABOUT_TEXT = """About ARUN RAGHUNATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Engineering Manager | 10+ years IT experience | On a Career Break

Currently on a career break to study computer science fundamentals and learning by doing.

Goal: Engineering Manager/ Architect
Philosophy: Learn by doing, understand by reading source code.
"""

PROJECTS = [{
    "id": 1,
    "name": "CLI portfolio",
    "description": "interactive CLI-style portfolio",
    "tech": ["Flask", "Javascript", "HTML/CSS"],
    "github": "https://github.com/thearun85/dev-portfolio"
}]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command', '').strip()
    if (command == "projects"):
        return get_projects()
        
def get_projects():
    return jsonify({
        "projects": PROJECTS,
        "count": len(PROJECTS)
    });

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
