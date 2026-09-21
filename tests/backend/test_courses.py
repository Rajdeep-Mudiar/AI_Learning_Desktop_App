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

        # 6. Verify DSA Course & Lesson Detail
        dsa_resp = await ac.get("/api/v1/courses/dsa-foundations-arrays-strings")
        assert dsa_resp.status_code == 200
        dsa_data = dsa_resp.json()
        assert dsa_data["domain"] == "dsa"
        assert len(dsa_data["modules"]) >= 3

        dsa_lesson_resp = await ac.get("/api/v1/lessons/dsa-big-o-memory-arrays")
        assert dsa_lesson_resp.status_code == 200
        dsa_lesson = dsa_lesson_resp.json()
        assert len(dsa_lesson["theory_sections"]) > 0

        # 7. Verify Cyber Security Course & Lesson Detail
        cyber_resp = await ac.get("/api/v1/courses/cybersecurity-foundations-network-security")
        assert cyber_resp.status_code == 200
        cyber_data = cyber_resp.json()
        assert cyber_data["domain"] == "cybersecurity"
        assert len(cyber_data["modules"]) >= 3

        cyber_lesson_resp = await ac.get("/api/v1/lessons/cyber-cia-triad-threat-modeling")
        assert cyber_lesson_resp.status_code == 200
        cyber_lesson = cyber_lesson_resp.json()
        assert len(cyber_lesson["theory_sections"]) > 0
