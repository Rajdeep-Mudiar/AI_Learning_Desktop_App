from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.project import (
    ProjectTrack,
    VivaQuestionResponse,
    VivaSubmitAnswerRequest,
    VivaEvaluationResponse,
    PortfolioExportResponse
)
from app.services.project_service import (
    get_all_projects,
    get_project_by_id,
    get_viva_question,
    evaluate_viva_answer,
    generate_portfolio_markdown
)

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("", response_model=List[ProjectTrack])
async def list_projects():
    """Retrieve full catalog of guided AI project tracks."""
    return get_all_projects()

@router.get("/{project_id}", response_model=ProjectTrack)
async def get_project(project_id: str):
    """Retrieve details, milestones, and starter code for a specific project track."""
    p = get_project_by_id(project_id)
    if not p:
        raise HTTPException(status_code=404, detail="Project track not found")
    return p

@router.get("/{project_id}/viva/question", response_model=VivaQuestionResponse)
async def get_project_viva_question(project_id: str, step: int = 1):
    """Get an oral examination defense question for the project from the AI Viva Examiner."""
    return get_viva_question(project_id, step)

@router.post("/{project_id}/viva/submit", response_model=VivaEvaluationResponse)
async def submit_viva_answer(project_id: str, req: VivaSubmitAnswerRequest):
    """Submit oral defense answer and receive graded evaluation with strengths and improvement notes."""
    return evaluate_viva_answer(project_id, req.question_id, req.answer)

@router.get("/{project_id}/portfolio", response_model=PortfolioExportResponse)
async def get_portfolio_export(project_id: str):
    """Generate production-ready GitHub README markdown, resume bullets, and architecture diagrams."""
    return generate_portfolio_markdown(project_id)
