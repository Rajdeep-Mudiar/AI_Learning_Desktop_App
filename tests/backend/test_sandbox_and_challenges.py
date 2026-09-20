import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_sandbox_code_execution():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Successful execution
        payload = {
            "code": "print('Hello from AI Sandbox!')\nprint(2 + 2)"
        }
        resp = await ac.post("/api/v1/sandbox/execute", json=payload)
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "success"
        assert "Hello from AI Sandbox!" in data["stdout"]
        assert "4" in data["stdout"]
        assert data["exit_code"] == 0

        # 2. Syntax/Runtime error capture
        err_payload = {
            "code": "print(10 / 0)"
        }
        err_resp = await ac.post("/api/v1/sandbox/execute", json=err_payload)
        assert err_resp.status_code == 200
        err_data = err_resp.json()
        assert err_data["status"] == "error"
        assert "ZeroDivisionError" in err_data["stderr"]

        # 3. Timeout safety protection
        timeout_payload = {
            "code": "import time\ntime.sleep(5)",
            "timeout_seconds": 1.0
        }
        timeout_resp = await ac.post("/api/v1/sandbox/execute", json=timeout_payload)
        assert timeout_resp.status_code == 200
        timeout_data = timeout_resp.json()
        assert timeout_data["status"] == "timeout"
        assert "timed out" in timeout_data["stderr"]

@pytest.mark.asyncio
async def test_challenges_flow():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. List challenges
        challenges_resp = await ac.get("/api/v1/challenges")
        assert challenges_resp.status_code == 200
        challenges = challenges_resp.json()
        assert len(challenges) >= 3

        # 2. Get challenge detail
        c_id = "linear-regression-ols"
        detail_resp = await ac.get(f"/api/v1/challenges/{c_id}")
        assert detail_resp.status_code == 200
        detail = detail_resp.json()
        assert "starter_code" in detail
        assert "problem_statement" in detail

        # 3. Submit solution
        reg_resp = await ac.post("/api/v1/auth/register", json={
            "name": "Challenge Student",
            "email": "challenge_tester@ailearnlab.io",
            "password": "Password123!"
        })
        if reg_resp.status_code == 201:
            token = reg_resp.json()["access_token"]
        else:
            login_resp = await ac.post("/api/v1/auth/login", json={"email": "challenge_tester@ailearnlab.io", "password": "Password123!"})
            token = login_resp.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}

        # Submit correct OLS solution
        solution_code = (
            "import numpy as np\n\n"
            "def fit_ols(X: np.ndarray, y: np.ndarray) -> np.ndarray:\n"
            "    return np.linalg.pinv(X.T @ X) @ X.T @ y\n"
        )
        sub_resp = await ac.post(
            f"/api/v1/challenges/{c_id}/submit",
            json={"challenge_id": c_id, "code": solution_code},
            headers=headers
        )
        assert sub_resp.status_code == 200
        res = sub_resp.json()
        assert res["all_passed"] is True
        assert res["passed_count"] >= 2
        assert res["xp_earned"] == 100
