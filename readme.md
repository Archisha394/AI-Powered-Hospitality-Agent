# AI Hospitality Agent (FastAPI + Google ADK stub + BigQuery)

End-to-end scaffold for a hotel automation system. It includes:
- Multi-agent style tool routing (food ordering, maintenance) via a stubbed Google ADK client.
- FastAPI API for chat and analytics.
- Optional BigQuery integration (falls back to a local mock store automatically).
- Pydantic models, services, and tests.

## Quickstart (Local Mock Mode)
```bash
cd ai-powered-hospitality-agent
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn src.api.main:app --reload
