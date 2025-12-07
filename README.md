# Bun-Py Monorepo Template

A modern monorepo template combining **React (Bun)** and **Python (uv)**.

## Tech Stack

- **Frontend:** React 19, Vite, TypeScript, TailwindCSS (managed by `bun`)
- **Backend:** Python 3.14+, FastAPI (managed by `uv`)

## Prerequisites

Ensure you have the following installed:
- [Bun](https://bun.sh)
- [uv](https://docs.astral.sh/uv/)

## Setup

Initialize dependencies for both applications.

### 1. Frontend

```bash
cd apps/frontend
bun install
```

### 2. Backend

```bash
cd apps/backend
uv sync
```

## Run Development

You need to run the frontend and backend in separate terminals.

### Frontend

```bash
cd apps/frontend
bun run dev
```

Runs on port 5173.

### Backend

```bash
cd apps/backend
just dev
```

Runs on port 8000.

## Structure

```text
bun-py-mono/
├── apps/
│   ├── frontend/   # React Application (Vite + Bun)
│   └── backend/    # Python Application (FastAPI + uv)
├── .vscode/        # Unified VS Code settings
└── package.json    # Root scripts
```
