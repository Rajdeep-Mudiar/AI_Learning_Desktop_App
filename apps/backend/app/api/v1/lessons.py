from typing import Optional
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import get_database
from app.api.deps import get_current_user, get_optional_current_user
from app.schemas.lesson import LessonDetail, LessonCompletionResponse
from app.services.lesson_service import LessonService

router = APIRouter(prefix="/lessons", tags=["Lessons"])

@router.get("/{lesson_slug}", response_model=LessonDetail)
async def get_lesson(
    lesson_slug: str,
    current_user: Optional[dict] = Depends(get_optional_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = LessonService(db)
    user_id = str(current_user["_id"]) if current_user else None
    return await service.get_lesson_by_slug(lesson_slug, user_id)

@router.post("/{lesson_slug}/complete", response_model=LessonCompletionResponse)
async def complete_lesson(
    lesson_slug: str,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = LessonService(db)
    user_id = str(current_user["_id"])
    return await service.complete_lesson(lesson_slug, user_id)
