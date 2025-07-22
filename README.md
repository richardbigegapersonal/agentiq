# README.md

# 🤖 AgentIQ: Modular Agentic AI Workflow Toolkit

[![Docker Build](https://img.shields.io/docker/cloud/build/your-dockerhub-username/agentiq)](https://hub.docker.com/r/your-dockerhub-username/agentiq)
[![GitHub last commit](https://img.shields.io/github/last-commit/your-username/agentiq)](https://github.com/your-username/agentiq)

AgentIQ is an open-source, production-ready framework for building agentic applications using LangChain, Pinecone, and Redis. With integrated LangSmith tracing, modular agent design, and out-of-the-box deployment, it’s perfect for GenAI developers and AI infrastructure teams.

![AgentIQ Demo](https://your-image-link.com/screenshot.png)

---

## 🌟 Features
- 🔁 LangChain-powered agent orchestration with LangGraph
- 📚 Retrieval-Augmented Generation (RAG) with Pinecone
- 🧠 Redis-backed memory agent for short-term session context
- 📈 LangSmith integration for tracing and observability
- 🐳 Dockerized architecture + GitHub Actions CI/CD pipeline
- 🌍 One-click deployment to Render

---

## 📦 Project Structure
```
agentiq/
├── agents/             # Agent logic (retriever, memory, planner)
├── api/                # FastAPI server
├── vectorstore/        # Pinecone RAG integration
├── tracing/            # LangSmith tracing hook
├── dashboard/          # Streamlit dashboard UI
├── docker-compose.yml  # Service orchestration
├── .github/workflows/  # CI/CD pipeline
└── README.md           # This file
```

---

## 🚀 Quickstart
### 1. Clone and Configure
```bash
git clone https://github.com/richardbigegapersonal/agentiq.git
cd agentiq
cp .env.example .env  # then fill in API keys
```

### 2. Run Locally with Docker Compose
```bash
docker-compose up --build
```

### 3. Access the App
- FastAPI: http://localhost:8000/query
- Streamlit: http://localhost:8501

---

## 🔐 Environment Variables
Add your secrets to a `.env` file (excluded from Git):
```env
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=...
REDIS_URL=redis://localhost:6379/0
```

---

## 🧠 LangSmith Tracing
AgentIQ uses LangSmith to trace LLM input/output, token usage, and error patterns.
```python
from tracing.langsmith_hooks import tracer
chain.run("question", callbacks=[tracer])
```

Set up your LangSmith API key in the environment as needed.

---

## 🔁 GitHub Actions CI/CD
AgentIQ auto-builds Docker images on every push to `main`. Add the following secrets:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

---

## 🌍 Deployment to Render
Create a new **Web Service** at [Render](https://dashboard.render.com):
- Build Command: `docker-compose build`
- Start Command: `docker-compose up`
- Set env vars: `OPENAI_API_KEY`, `PINECONE_API_KEY`, `REDIS_URL`

Expose port `8000` (API) and `8501` (Streamlit).

---


## 💬 Contact
Built by [Richard Bigega](mailto:richardbigega@gmail.com)

---

## 📄 License
MIT
