from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import get_database
from app.api.deps import get_current_user
from app.schemas.skill import SkillTreeResponse
from app.services.skill_service import SkillService

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.get("/tree", response_model=SkillTreeResponse)
async def get_skill_tree(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = SkillService(db)
    user_id = str(current_user["_id"])
    return await service.get_skill_tree(user_id)
