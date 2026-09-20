import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_interviews_and_evaluation():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Tracks list
        resp = await ac.get("/api/v1/interviews/tracks")
        assert resp.status_code == 200
        tracks = resp.json()
        assert len(tracks) >= 2
        track_ids = [t["id"] for t in tracks]
        assert "ml-engineer" in track_ids
        assert "ai-researcher" in track_ids

        # 2. Track detail
        det_resp = await ac.get("/api/v1/interviews/tracks/ml-engineer")
        assert det_resp.status_code == 200
        det = det_resp.json()
        assert len(det["questions"]) >= 2

        # 3. Evaluate answers
        eval_payload = {
            "answers": [
                {
                    "question_id": det["questions"][0]["id"],
                    "question": det["questions"][0]["question"],
                    "user_answer": "Standard gradient descent oscillates in high curvature directions with high Hessian condition number. Momentum uses exponential moving average of velocity to dampen oscillations while Adam adapts per-parameter learning rate scales."
                }
            ]
        }
        eval_resp = await ac.post("/api/v1/interviews/tracks/ml-engineer/evaluate", json=eval_payload)
        assert eval_resp.status_code == 200
        report = eval_resp.json()
        assert "overall_score" in report
        assert report["recommendation"] in ["Strong Hire", "Hire", "Lean Hire", "No Hire"]

@pytest.mark.asyncio
async def test_hackathons_and_submission():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Hackathon list
        resp = await ac.get("/api/v1/hackathons")
        assert resp.status_code == 200
        hackathons = resp.json()
        assert len(hackathons) >= 1
        assert len(hackathons[0]["leaderboard"]) >= 2

        # 2. Submit entry
        sub_resp = await ac.post("/api/v1/hackathons/submit", json={
            "challenge_id": hackathons[0]["id"],
            "code": "from sklearn.ensemble import GradientBoostingClassifier\nclf = GradientBoostingClassifier()",
            "model_name": "Tuned GradientBoosting"
        })
        assert sub_resp.status_code == 200
        entry = sub_resp.json()
        assert entry["username"] == "You (Candidate)"
        assert entry["score"] > 0.8

@pytest.mark.asyncio
async def test_community_and_career_overview():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        # 1. Community posts
        p_resp = await ac.get("/api/v1/community/posts")
        assert p_resp.status_code == 200
        posts = p_resp.json()
        assert len(posts) >= 2

        # 2. Create post
        create_resp = await ac.post("/api/v1/community/posts", json={
            "title": "My first Transformer Attention implementation",
            "category": "Show & Tell",
            "content": "Implemented Scaled Dot-Product attention in PyTorch from scratch!",
            "tags": ["Transformers", "PyTorch"]
        })
        assert create_resp.status_code == 200
        new_post = create_resp.json()
        assert new_post["title"] == "My first Transformer Attention implementation"

        # 3. Upvote post
        upvote_resp = await ac.post(f"/api/v1/community/posts/{new_post['id']}/upvote")
        assert upvote_resp.status_code == 200
        assert upvote_resp.json()["upvotes"] == 2

        # 4. Career overview
        c_resp = await ac.get("/api/v1/career/overview")
        assert c_resp.status_code == 200
        c_data = c_resp.json()
        assert len(c_data["career_paths"]) >= 2
        assert len(c_data["recommended_focus_areas"]) >= 1
