import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_tutor_models_and_presets():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Models endpoint
        m_resp = await ac.get("/api/v1/tutor/models")
        assert m_resp.status_code == 200
        m_data = m_resp.json()
        assert "available_models" in m_data
        assert "default_model" in m_data

        # 2. Presets endpoint
        p_resp = await ac.get("/api/v1/tutor/presets")
        assert p_resp.status_code == 200
        p_data = p_resp.json()
        assert len(p_data["modes"]) == 4
        assert len(p_data["quick_questions"]) >= 4

@pytest.mark.asyncio
async def test_tutor_chat_interaction():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Socratic mode chat
        payload = {
            "message": "Why does Scaled Dot-Product Attention divide by sqrt(d_k)?",
            "mode": "socratic",
            "provider": "auto",
            "context": {
                "current_lesson_title": "Scaled Dot-Product Attention",
                "student_level": "intermediate"
            }
        }
        resp = await ac.post("/api/v1/tutor/chat", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert "response" in data
        assert len(data["response"]) > 50
        assert data["mode_used"] == "socratic"
        assert len(data["suggested_followups"]) > 0

        # 2. Math derivation mode
        math_payload = {
            "message": "Derive the OLS Normal Equation step-by-step",
            "mode": "math_derivation",
            "provider": "auto"
        }
        math_resp = await ac.post("/api/v1/tutor/chat", json=math_payload)
        assert math_resp.status_code == 200
        math_data = math_resp.json()
        assert "normal equation" in math_data["response"].lower()
