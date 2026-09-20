from typing import List, Optional
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.database import get_database
from app.api.deps import get_optional_current_user
from app.schemas.course import CourseSummary, CourseDetail
from app.services.course_service import CourseService

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("", response_model=List[CourseSummary])
async def list_courses(
    current_user: Optional[dict] = Depends(get_optional_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = CourseService(db)
    user_id = str(current_user["_id"]) if current_user else None
    return await service.list_courses(user_id)

@router.get("/{course_slug}", response_model=CourseDetail)
async def get_course_detail(
    course_slug: str,
    current_user: Optional[dict] = Depends(get_optional_current_user),
    db: AsyncIOMotorDatabase = Depends(get_database)
):
    service = CourseService(db)
    user_id = str(current_user["_id"]) if current_user else None
    return await service.get_course_detail(course_slug, user_id)
