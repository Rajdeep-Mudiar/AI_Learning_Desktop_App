import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_courses_and_lessons_flow():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Reset/ensure seed data
        seed_resp = await ac.post("/api/v1/seed/reset")
        assert seed_resp.status_code == 200

        # 2. List all courses
        courses_resp = await ac.get("/api/v1/courses")
        assert courses_resp.status_code == 200
        courses = courses_resp.json()
        assert len(courses) >= 5
        slugs = [c["slug"] for c in courses]
        assert "python-foundations" in slugs
        assert "math-for-ai" in slugs
        assert "ml-fundamentals" in slugs

        # 3. Get course detail
        course_detail_resp = await ac.get("/api/v1/courses/python-foundations")
        assert course_detail_resp.status_code == 200
        c_detail = course_detail_resp.json()
        assert len(c_detail["modules"]) >= 2
        assert c_detail["title"] == "Python & NumPy Foundations for AI"

        # 4. Get lesson detail
        lesson_resp = await ac.get("/api/v1/lessons/py-intro-variables")
        assert lesson_resp.status_code == 200
        lesson_data = lesson_resp.json()
        assert "theory_sections" in lesson_data
        assert len(lesson_data["theory_sections"]) > 0
        assert lesson_data["code_example"] is not None

        # 5. Get quiz
        quiz_resp = await ac.get(f"/api/v1/quizzes/{lesson_data['quiz_id']}")
        assert quiz_resp.status_code == 200
        quiz_data = quiz_resp.json()
        assert len(quiz_data["questions"]) > 0
        # Ensure correct answers are NOT leaked in quiz detail endpoint
        for q in quiz_data["questions"]:
            assert "correct_answer" not in q
