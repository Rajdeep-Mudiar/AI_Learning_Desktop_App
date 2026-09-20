import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_quiz_grading_and_progress_tracking():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Login/Register user
        user_email = "quiz_test_student@ailearnlab.io"
        reg_resp = await ac.post("/api/v1/auth/register", json={
            "name": "Quiz Tester",
            "email": user_email,
            "password": "Password123!"
        })
        if reg_resp.status_code == 201:
            token = reg_resp.json()["access_token"]
        else:
            login_resp = await ac.post("/api/v1/auth/login", json={"email": user_email, "password": "Password123!"})
            token = login_resp.json()["access_token"]

        headers = {"Authorization": f"Bearer {token}"}

        # 2. Complete lesson endpoint
        comp_resp = await ac.post("/api/v1/lessons/py-intro-variables/complete", headers=headers)
        assert comp_resp.status_code == 200
        comp_data = comp_resp.json()
        assert comp_data["is_completed"] is True
        assert comp_data["course_percentage"] > 0

        # 3. Submit quiz with deliberate answers
        quiz_submission = {
            "answers": [
                {"question_id": "q1", "selected_answer": 1},  # Correct option for q1
                {"question_id": "q2", "selected_answer": 0}   # Correct option for q2
            ]
        }
        submit_resp = await ac.post("/api/v1/quizzes/quiz-py-intro-variables/submit", json=quiz_submission, headers=headers)
        assert submit_resp.status_code == 200
        result = submit_resp.json()
        assert result["passed"] is True
        assert result["percentage"] == 100.0
        assert len(result["results"]) == 2
        assert result["results"][0]["is_correct"] is True
        assert "explanation" in result["results"][0]

        # 4. Check updated skill tree reflects progress
        skills_resp = await ac.get("/api/v1/skills/tree", headers=headers)
        assert skills_resp.status_code == 200
        skill_tree = skills_resp.json()
        assert len(skill_tree["categories"]) > 0
