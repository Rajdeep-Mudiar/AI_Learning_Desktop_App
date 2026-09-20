from fastapi import APIRouter
from app.schemas.achievement import UserAchievementsSummary
from app.services.achievement_service import get_user_achievements

router = APIRouter(prefix="/achievements", tags=["Achievements"])

@router.get("", response_model=UserAchievementsSummary)
async def get_achievements():
    """Retrieve user level, streak count, badge collection, and certificate status."""
    return get_user_achievements()
