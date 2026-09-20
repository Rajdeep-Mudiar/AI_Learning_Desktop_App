from fastapi import APIRouter
from app.schemas.community import CareerOverviewResponse
from app.services.community_service import get_career_overview

router = APIRouter(prefix="/career", tags=["Career Roadmaps"])

@router.get("/overview", response_model=CareerOverviewResponse)
async def get_overview():
    """Retrieve personalized AI career paths, skill readiness percentages, and learning recommendations."""
    return get_career_overview()
