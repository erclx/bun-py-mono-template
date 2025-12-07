# bun-py-mono

A modern monorepo template combining **React (Bun)** and **Python (uv)**.

## Tech Stack

- **Frontend:** React 19, Vite, TypeScript, TailwindCSS (managed by `bun`)
- **Backend:** Python 3.14+, FastAPI (managed by `uv`)
- **Quality:** Pre-commit, Ruff, ESLint, Gitleaks

## Quick Start

### 1. Prerequisites

Ensure you have [Bun](https://bun.sh) and [uv](https://docs.astral.sh/uv/) installed.

### 2. Setup

Initialize dependencies and git hooks:

```bash
# 1. Setup Git Hooks (Root)
uv tool install pre-commit --force
pre-commit install

# 2. Setup Frontend
cd apps/frontend
bun install

# 3. Setup Backend
cd ../backend
uv sync
```

### 3. Run Development

Open two terminal tabs:

**Frontend (UI):**

```bash
cd apps/frontend
bun run dev
# Running at http://localhost:5173
```

**Backend (API):**

```bash
cd apps/backend
uv run uvicorn src.app.main:app --reload
# Running at http://127.0.0.1:8000
```

## 📂 Structure

```text
bun-py-mono/
├── apps/
│   ├── frontend/   # React Application (Vite + Bun)
│   └── backend/    # Python Application (FastAPI + uv)
├── .vscode/        # Unified VS Code settings
└── .pre-commit...  # Unified Git Hooks config
```

## 🤝 Contribution

This repo uses **pre-commit** to enforce code quality.

* **Python:** Linted/Formatted by `ruff`.
* **JS/TS:** Linted by `eslint`.
* **Commits:** Must follow conventional format (e.g., `feat: add login`).
