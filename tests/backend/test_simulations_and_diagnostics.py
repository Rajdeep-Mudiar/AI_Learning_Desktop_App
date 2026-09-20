import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_linear_regression_simulation():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        req = {
            "points": [
                {"x": 1.0, "y": 2.0},
                {"x": 2.0, "y": 4.0},
                {"x": 3.0, "y": 6.0}
            ],
            "weight": 0.0,
            "bias": 0.0,
            "learning_rate": 0.1
        }
        resp = await ac.post("/api/v1/simulations/linear-regression/step", json=req)
        assert resp.status_code == 200
        data = resp.json()
        assert data["new_weight"] > 0.0
        assert data["mse_loss"] > 0.0
        assert len(data["residuals"]) == 3

@pytest.mark.asyncio
async def test_kmeans_simulation():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        req = {
            "points": [
                {"x": 1.0, "y": 1.0},
                {"x": 1.2, "y": 1.1},
                {"x": 8.0, "y": 8.0},
                {"x": 8.2, "y": 8.1}
            ],
            "centroids": [
                {"x": 0.0, "y": 0.0},
                {"x": 10.0, "y": 10.0}
            ]
        }
        resp = await ac.post("/api/v1/simulations/kmeans/step", json=req)
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["assignments"]) == 4
        assert len(data["new_centroids"]) == 2
        assert data["assignments"][0] == 0
        assert data["assignments"][2] == 1

@pytest.mark.asyncio
async def test_pca_computation():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        req = {
            "points": [
                {"x": 1.0, "y": 1.0},
                {"x": 2.0, "y": 2.0},
                {"x": 3.0, "y": 3.0},
                {"x": 4.0, "y": 4.0}
            ]
        }
        resp = await ac.post("/api/v1/simulations/pca/compute", json=req)
        assert resp.status_code == 200
        data = resp.json()
        assert len(data["components"]) == 2
        assert len(data["explained_variance_ratio"]) == 2
        # On y = x line, PC1 captures ~100% of variance
        assert data["explained_variance_ratio"][0] >= 0.99

@pytest.mark.asyncio
async def test_diagnostics_flow():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. List scenarios
        scenarios_resp = await ac.get("/api/v1/diagnostics/scenarios")
        assert scenarios_resp.status_code == 200
        scenarios = scenarios_resp.json()
        assert len(scenarios) >= 3

        # 2. Get scenario detail
        scen_id = scenarios[0]["id"]
        detail_resp = await ac.get(f"/api/v1/diagnostics/scenarios/{scen_id}")
        assert detail_resp.status_code == 200
        detail = detail_resp.json()
        assert "code_snippet" in detail
        assert "hints" in detail
        assert len(detail["options"]) > 0

        # 3. Submit diagnosis (with user token)
        reg_resp = await ac.post("/api/v1/auth/register", json={
            "name": "Diag Student",
            "email": "diag_tester@ailearnlab.io",
            "password": "Password123!"
        })
        if reg_resp.status_code == 201:
            token = reg_resp.json()["access_token"]
        else:
            login_resp = await ac.post("/api/v1/auth/login", json={"email": "diag_tester@ailearnlab.io", "password": "Password123!"})
            token = login_resp.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}
        sub_resp = await ac.post(
            f"/api/v1/diagnostics/scenarios/{scen_id}/submit",
            json={"scenario_id": scen_id, "selected_option": 1},
            headers=headers
        )
        assert sub_resp.status_code == 200
        res = sub_resp.json()
        assert "explanation" in res
        assert "fix_code_snippet" in res
