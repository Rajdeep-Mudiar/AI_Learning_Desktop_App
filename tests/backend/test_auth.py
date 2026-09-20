import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_health_check():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_auth_and_dashboard_flow():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # Register a test user
        user_email = "test_student@ailearnlab.io"
        reg_payload = {
            "name": "Alex Mercer",
            "email": user_email,
            "password": "Password123!",
            "preferred_track": "ai_engineer"
        }
        reg_resp = await ac.post("/api/v1/auth/register", json=reg_payload)
        # 201 or 400 if already exists
        if reg_resp.status_code == 201:
            data = reg_resp.json()
            token = data["access_token"]
            assert "access_token" in data
            assert data["user"]["name"] == "Alex Mercer"
        else:
            # Login if exists
            login_resp = await ac.post("/api/v1/auth/login", json={"email": user_email, "password": "Password123!"})
            assert login_resp.status_code == 200
            token = login_resp.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        
        # Test /auth/me
        me_resp = await ac.get("/api/v1/auth/me", headers=headers)
        assert me_resp.status_code == 200
        assert me_resp.json()["email"] == user_email

        # Test /dashboard/summary
        dash_resp = await ac.get("/api/v1/dashboard/summary", headers=headers)
        assert dash_resp.status_code == 200
        dash_data = dash_resp.json()
        assert "greeting" in dash_data
        assert "skill_mastery_bars" in dash_data
        assert len(dash_data["skill_mastery_bars"]) > 0
