import pytest
import httpx
from main import app

@pytest.mark.asyncio
async def test_research_papers_catalog():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        resp = await ac.get("/api/v1/research/papers")
        assert resp.status_code == 200
        papers = resp.json()
        assert len(papers) >= 3
        ids = [p["id"] for p in papers]
        assert "attention-is-all-you-need" in ids
        assert "resnet-deep-residual-learning" in ids
        assert "lora-low-rank-adaptation" in ids

@pytest.mark.asyncio
async def test_research_paper_detail_and_equations():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        resp = await ac.get("/api/v1/research/papers/attention-is-all-you-need")
        assert resp.status_code == 200
        paper = resp.json()
        assert paper["title"] == "Attention Is All You Need"
        assert len(paper["equations"]) >= 2
        assert len(paper["reproduction_steps"]) >= 2
        assert "Scaled Dot-Product Attention" in [eq["equation_name"] for eq in paper["equations"]]
