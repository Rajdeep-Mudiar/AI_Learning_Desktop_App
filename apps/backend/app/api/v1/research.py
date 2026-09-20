from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.research import (
    ResearchPaper,
    PaperListItem,
    ReproductionRunRequest
)
from app.services.research_service import (
    list_all_papers,
    get_paper_by_id
)

router = APIRouter(prefix="/research", tags=["Research"])

@router.get("/papers", response_model=List[PaperListItem])
async def get_papers_list():
    """Retrieve catalog of foundational AI research papers."""
    return list_all_papers()

@router.get("/papers/{paper_id}", response_model=ResearchPaper)
async def get_paper_detail(paper_id: str):
    """Retrieve detailed research paper breakdown, mathematical equations, and reproduction checklists."""
    p = get_paper_by_id(paper_id)
    if not p:
        raise HTTPException(status_code=404, detail="Paper not found")
    return p
