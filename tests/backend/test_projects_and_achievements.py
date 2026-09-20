import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_projects_catalog_and_detail():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Projects list
        resp = await ac.get("/api/v1/projects")
        assert resp.status_code == 200
        projects = resp.json()
        assert len(projects) >= 3
        p_ids = [p["id"] for p in projects]
        assert "spam-classifier" in p_ids
        assert "rag-knowledge-assistant" in p_ids

        # 2. Project detail
        detail_resp = await ac.get("/api/v1/projects/spam-classifier")
        assert detail_resp.status_code == 200
        detail = detail_resp.json()
        assert len(detail["milestones"]) >= 3
        assert "starter_code" in detail["milestones"][0]

@pytest.mark.asyncio
async def test_viva_simulator_flow():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Fetch Viva question
        q_resp = await ac.get("/api/v1/projects/spam-classifier/viva/question?step=1")
        assert q_resp.status_code == 200
        q_data = q_resp.json()
        assert "question" in q_data
        assert "rubric" in q_data

        # 2. Submit Viva answer
        sub_payload = {
            "project_id": "spam-classifier",
            "question_id": q_data["question_id"],
            "question": q_data["question"],
            "answer": "We chose TF-IDF because of low inference latency under 5ms, explainable feature weights for keywords, and high precision trade-off against false positive spam blocking."
        }
        sub_resp = await ac.post("/api/v1/projects/spam-classifier/viva/submit", json=sub_payload)
        assert sub_resp.status_code == 200
        eval_data = sub_resp.json()
        assert eval_data["score"] >= 70
        assert eval_data["grade"] in ["Distinction", "Merit"]
        assert len(eval_data["strengths"]) > 0

@pytest.mark.asyncio
async def test_portfolio_export():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        resp = await ac.get("/api/v1/projects/spam-classifier/portfolio")
        assert resp.status_code == 200
        data = resp.json()
        assert "# Real-Time SMS & Email Spam Classifier" in data["markdown_readme"]
        assert "```mermaid" in data["architecture_mermaid"]
        assert len(data["resume_bullet_points"]) >= 2

@pytest.mark.asyncio
async def test_achievements_summary():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        resp = await ac.get("/api/v1/achievements")
        assert resp.status_code == 200
        data = resp.json()
        assert data["total_xp"] > 0
        assert data["current_level"] >= 1
        assert len(data["badges"]) >= 8
        assert data["unlocked_badges_count"] >= 5
