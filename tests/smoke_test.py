"""
End-to-End System Smoke Verification Runner for AI Learning Lab (Phases 1-11).
Executes a complete journey through all platform capabilities.
"""
import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_full_system_smoke():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Health & Meta
        res = await ac.get("/health")
        assert res.status_code == 200
        assert res.json()["status"] == "ok"

        # 2. Syllabus & Courses
        res = await ac.get("/api/v1/courses")
        assert res.status_code == 200
        courses = res.json()
        assert len(courses) > 0

        # 3. Algorithm Simulation (Linear Regression Step)
        res = await ac.post("/api/v1/simulations/linear-regression/step", json={
            "points": [
                {"x": 1.0, "y": 2.0},
                {"x": 2.0, "y": 4.0},
                {"x": 3.0, "y": 6.0}
            ],
            "weight": 0.0,
            "bias": 0.0,
            "learning_rate": 0.1
        })
        assert res.status_code == 200
        assert "new_weight" in res.json()

        # 4. Sandbox Python Execution
        res = await ac.post("/api/v1/sandbox/execute", json={
            "code": "import numpy as np; arr = np.array([1, 2, 3]); print(f'SUM={arr.sum()}')"
        })
        assert res.status_code == 200
        assert "SUM=6" in res.json()["stdout"]

        # 5. Datasets Catalog
        res = await ac.get("/api/v1/datasets")
        assert res.status_code == 200
        assert len(res.json()) >= 3

        # 6. Deep Learning Lab (MLP)
        res = await ac.post("/api/v1/deep-learning/mlp/simulate", json={
            "dataset_type": "xor",
            "n_samples": 40,
            "hidden_layers": [4, 4],
            "activation": "tanh",
            "learning_rate": 0.1,
            "epochs": 15,
            "random_seed": 42
        })
        assert res.status_code == 200
        assert len(res.json()["loss_history"]) > 0

        # 7. AI Tutor
        res = await ac.get("/api/v1/tutor/models")
        assert res.status_code == 200

        # 8. Projects & Research
        res = await ac.get("/api/v1/projects")
        assert res.status_code == 200
        res = await ac.get("/api/v1/research/papers")
        assert res.status_code == 200

        # 9. Interview Tracks & Hackathons
        res = await ac.get("/api/v1/interviews/tracks")
        assert res.status_code == 200
        res = await ac.get("/api/v1/hackathons")
        assert res.status_code == 200

        # 10. Community & Career Paths
        res = await ac.get("/api/v1/community/posts")
        assert res.status_code == 200
        res = await ac.get("/api/v1/career/overview")
        assert res.status_code == 200
        assert len(res.json()["career_paths"]) > 0

        print("\n>>> ALL 11 PLATFORM PHASES PASSED END-TO-END SMOKE TEST! <<<")
